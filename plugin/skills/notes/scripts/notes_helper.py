#!/usr/bin/env python3
"""Helpers for the Claude Notes skill. Standard library only.

The index directory is where a `list` of the `notes` collection was saved with
out_dir (files <dir>/notes/<id>.json or <dir>/<id>.json, each {id, data, version}
or the bare record).

  notes_helper.py find <index dir> <word> [<word> ...]
      Notes whose title, tags, keywords or summary contain every word.
  notes_helper.py folders <index dir>
      Every folder path in use, with note counts, in the case first used.
  notes_helper.py new <index dir> <body.md> --title T [--tags "A/B, C"] [--keywords "x, y"]
                  [--summary S] [--source chat|research|code] [--id ID] [--pinned] --out <dir>
      Writes <dir>/body.json and <dir>/index.json for a new note (links and words worked out)
      and prints the id.
  notes_helper.py reindex <index dir> <body.md> <id>
      Prints {links, words} for an edited body.
  notes_helper.py todo-add <body.md> "<task>" [--due "28 Nov 2026"]
  notes_helper.py todo-done <body.md> "<words of the task>"
      Edit a to-do list body in place and print the result; todo-done exits 2 if no task
      or several tasks match.
"""
import json, os, random, re, string, sys
from datetime import datetime, timezone

DEPTH = 4
LINK = re.compile(r'\[\[([^\]\n]{1,200})\]\]')


def now():
    return datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')


def load_index(d):
    rows = []
    for root, _, files in os.walk(d):
        for f in files:
            if not f.endswith('.json'):
                continue
            r = json.load(open(os.path.join(root, f), encoding='utf-8'))
            data = r.get('data', r) if isinstance(r, dict) else {}
            rows.append(dict(data, id=r.get('id') or f[:-5]))
    return rows


def norm_tags(s):
    seen, out = set(), []
    for raw in s.split(','):
        segs = [re.sub(r'\s+', ' ', x.strip()) for x in raw.split('/') if x.strip()][:DEPTH]
        if segs and '/'.join(segs).lower() not in seen:
            seen.add('/'.join(segs).lower()); out.append('/'.join(segs))
    return out


def links_for(text, rows, self_id=None):
    by_title = {}
    for r in sorted(rows, key=lambda r: str(r.get('updated') or '')):
        if r.get('title'):
            by_title[r['title'].lower()] = r['id']
    out = []
    for m in LINK.finditer(text):
        t = m.group(1)
        if t.lower().startswith(('card:', 'passwords:')):
            continue
        i = by_title.get(t.split('|')[0].split('#')[0].strip().lower())
        if i and i != self_id and i not in out:
            out.append(i)
    return out


def words(text):
    return len(text.split())


def new_id():
    return 'c-' + datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S') + '-' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))


def opt(args, name, default=None):
    if name in args:
        i = args.index(name); v = args[i + 1]; del args[i:i + 2]; return v
    return default


def main():
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    cmd = a.pop(0)
    if cmd == 'find':
        rows, ws = load_index(a[0]), [w.lower() for w in a[1:]]
        hits = [r for r in rows if all(w in ' '.join([r.get('title') or '', ' '.join(r.get('tags') or []), ' '.join(r.get('keywords') or []), r.get('summary') or '']).lower() for w in ws)]
        hits.sort(key=lambda r: str(r.get('updated') or ''), reverse=True)
        print(json.dumps([{k: r.get(k) for k in ('id', 'title', 'tags', 'updated', 'source')} for r in hits], ensure_ascii=False, indent=1))
    elif cmd == 'folders':
        counts, case = {}, {}
        for r in load_index(a[0]):
            for t in r.get('tags') or []:
                segs = t.split('/')
                for i in range(1, len(segs) + 1):
                    p = '/'.join(segs[:i]); k = p.lower()
                    case.setdefault(k, p); counts[k] = counts.get(k, 0) + 1
        for k in sorted(counts):
            print(f'{case[k]}\t{counts[k]}')
    elif cmd == 'new':
        title, tags, kw = opt(a, '--title'), opt(a, '--tags', ''), opt(a, '--keywords', '')
        summary, source, nid, out = opt(a, '--summary', ''), opt(a, '--source', 'chat'), opt(a, '--id'), opt(a, '--out', '.')
        pinned = '--pinned' in a
        if pinned: a.remove('--pinned')
        if not title: sys.exit('--title is required')
        rows, text = load_index(a[0]), open(a[1], encoding='utf-8').read()
        nid = nid or new_id(); t = now()
        if any(r['id'] == nid for r in rows): sys.exit(f'id {nid} already exists')
        index = {'title': title.strip(), 'tags': norm_tags(tags), 'keywords': sorted({k.strip().lower() for k in kw.split(',') if k.strip()}),
                 'links': links_for(text, rows, nid), 'summary': summary, 'source': source, 'created': t, 'updated': t,
                 'summarised': t if summary else None, 'words': words(text), 'pinned': pinned}
        os.makedirs(out, exist_ok=True)
        json.dump({'text': text, 'updated': t}, open(os.path.join(out, 'body.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        json.dump(index, open(os.path.join(out, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        dup = [r['id'] for r in rows if (r.get('title') or '').lower() == index['title'].lower()]
        print(json.dumps({'id': nid, 'links': index['links'], 'words': index['words'], 'same_title': dup}))
    elif cmd == 'reindex':
        rows, text = load_index(a[0]), open(a[1], encoding='utf-8').read()
        print(json.dumps({'links': links_for(text, rows, a[2]), 'words': words(text), 'updated': now()}))
    elif cmd in ('todo-add', 'todo-done'):
        path, arg = a[0], a[1]
        due = opt(a, '--due')
        lines = open(path, encoding='utf-8').read().rstrip('\n').split('\n') if os.path.exists(path) else []
        if lines == ['']: lines = []
        done_at = next((i for i, l in enumerate(lines) if l.strip().lower() == '## done'), len(lines))
        d = datetime.now(); today = f"{d.day} {d.strftime('%b %Y')}"
        if cmd == 'todo-add':
            item = f'- [ ] {arg.strip()}' + (f' · due {due}' if due else '')
            last_open = max((i for i, l in enumerate(lines[:done_at]) if l.startswith('- [ ]')), default=None)
            at = last_open + 1 if last_open is not None else 0
            lines.insert(at, item)
        else:
            ws = arg.lower().split()
            hits = [i for i, l in enumerate(lines[:done_at]) if l.startswith('- [ ]') and all(w in l.lower() for w in ws)]
            if len(hits) != 1:
                print(json.dumps({'matches': [lines[i] for i in hits]}), file=sys.stderr); sys.exit(2)
            line = lines.pop(hits[0]).replace('- [ ]', '- [x]', 1) + f' · done {today}'
            done_at = next((i for i, l in enumerate(lines) if l.strip().lower() == '## done'), None)
            if done_at is None:
                while lines and not lines[-1].strip(): lines.pop()
                lines += ['', '## Done', line]
            else:
                end = next((i for i in range(done_at + 1, len(lines)) if lines[i].startswith('#')), len(lines))
                while end > done_at + 1 and not lines[end - 1].strip(): end -= 1
                lines.insert(end, line)  # end of the Done section, as the page does when a task is ticked there
        text = '\n'.join(lines).strip('\n') + '\n'
        open(path, 'w', encoding='utf-8').write(text)
        print(text)
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main()
