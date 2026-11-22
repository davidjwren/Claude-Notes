#!/usr/bin/env python3
"""Claude Notes GitHub sync. fetch: gather each repository (API when attached, anonymous clone for public ones). build: write the sync file the page applies.
Standard library and the gh CLI only. Set GH_OWNER to the GitHub account that owns the repositories."""
import json, os, re, subprocess, sys
from datetime import datetime, timezone

OWNER = os.environ.get('GH_OWNER', '')

def api(path, raw=False):
    args = ['gh','api', path] + (['-H','Accept: application/vnd.github.raw'] if raw else [])
    r = subprocess.run(args, capture_output=True, text=True, timeout=120)
    if r.returncode: return None, r.stdout[:200] + r.stderr[:200]
    return (r.stdout if raw else json.loads(r.stdout)), None

def fetch(names, outdir):
    import base64, tempfile, shutil
    os.makedirs(outdir, exist_ok=True); report = {}
    for name in names:
        base = f'repos/{OWNER}/{name}'
        meta, err = api(base)
        if meta:
            br,_ = api(base + '/branches?per_page=100')
            op,_ = api(base + '/pulls?state=open&per_page=50')
            cl,_ = api(base + '/pulls?state=closed&per_page=5&sort=updated&direction=desc')
            rd,_ = api(base + '/readme', raw=True)
            tr,_ = api(f"{base}/git/trees/{meta['default_branch']}?recursive=1")
            out = {'meta': {k: meta.get(k) for k in ['name','full_name','html_url','description','private','default_branch','pushed_at','created_at','language']},
                   'branches': [b['name'] for b in (br or [])],
                   'open_prs': [{'n': p['number'], 't': p['title'], 'b': p['head']['ref'], 'u': p['updated_at'], 'url': p['html_url'], 'draft': p.get('draft')} for p in (op or [])],
                   'closed_prs': [{'n': p['number'], 't': p['title'], 'merged': bool(p.get('merged_at')), 'u': p.get('merged_at') or p.get('closed_at'), 'url': p['html_url']} for p in (cl or [])],
                   'readme': rd, 'tree': [(t['path'], t['type']) for t in (tr or {}).get('tree', [])]}
            report[name] = 'api'
        else:
            # Public repositories are not attached, so the API refuses them; read them through an anonymous shallow clone (no pull requests)
            tmp = tempfile.mkdtemp(); url = f'https://github.com/{OWNER}/{name}'
            r = subprocess.run(['git', 'clone', '-q', '--depth', '1', url, tmp + '/r'], capture_output=True, text=True, timeout=600, env={**os.environ, 'GIT_LFS_SKIP_SMUDGE': '1'})
            if r.returncode: report[name] = 'failed: ' + (err or r.stderr)[:160]; continue
            d = tmp + '/r'; g = lambda *a: subprocess.run(['git', '-C', d, *a], capture_output=True, text=True).stdout.strip()
            heads = [l.split('refs/heads/')[-1] for l in g('ls-remote', '--heads', 'origin').splitlines()]
            head = g('rev-parse', '--abbrev-ref', 'HEAD'); tree = []
            for root, dirs, files in os.walk(d):
                dirs[:] = [x for x in dirs if x != '.git']; rel = os.path.relpath(root, d)
                tree += [(os.path.normpath(os.path.join(rel, x)), 'tree') for x in dirs] + [(os.path.normpath(os.path.join(rel, f)), 'blob') for f in files]
            rdp = next((os.path.join(d, f) for f in os.listdir(d) if f.lower().startswith('readme')), None)
            out = {'meta': {'name': name, 'full_name': f'{OWNER}/{name}', 'html_url': url, 'description': None, 'private': False, 'default_branch': head,
                            'pushed_at': g('log', '-1', '--format=%cI').replace('+00:00', 'Z'), 'created_at': None, 'language': None},
                   'branches': heads, 'open_prs': None, 'closed_prs': None, 'readme': open(rdp, errors='replace').read() if rdp else None, 'tree': sorted(tree)}
            shutil.rmtree(tmp, ignore_errors=True); report[name] = 'clone (no pull requests)'
        json.dump(out, open(os.path.join(outdir, name + '.json'), 'w'), indent=1)
    return report


SKIP_DIRS = {'.git', '.venv', 'venv', 'node_modules', '__pycache__', '.pytest_cache', '.mypy_cache', '.ruff_cache', '.idea', 'dist', 'build', '.ipynb_checkpoints'}
SKIP_FILES = {'.DS_Store'}
MAX_TREE = 300
MAX_README = 120_000
MY = '## My notes'

def fmt_date(s):
    if not s: return 'unknown'
    d = datetime.fromisoformat(s.replace('Z', '+00:00'))
    return f"{d.day} {d.strftime('%B %Y')}"

def tree_lines(paths, max_depth=None):
    root = {}
    for p, t in paths:
        parts = p.split('/')
        if any(x in SKIP_DIRS for x in parts) or parts[-1] in SKIP_FILES: continue
        node = root
        for i, part in enumerate(parts):
            last = i == len(parts) - 1
            if last and t != 'tree': node.setdefault(part, None)
            else: node = node.setdefault(part, {}) if isinstance(node.get(part, {}), dict) else node
    out = []
    def count(n): return sum(1 + (count(v) if isinstance(v, dict) else 0) for v in n.values())
    def walk(n, prefix, depth):
        items = sorted(n.items(), key=lambda kv: (not isinstance(kv[1], dict), kv[0].lower()))
        for i, (k, v) in enumerate(items):
            last = i == len(items) - 1
            br = '└── ' if last else '├── '
            if isinstance(v, dict):
                if max_depth is not None and depth >= max_depth and v:
                    c = count(v); out.append(f"{prefix}{br}{k}/ ({c} {'item' if c == 1 else 'items'})")
                else:
                    out.append(f"{prefix}{br}{k}/"); walk(v, prefix + ('    ' if last else '│   '), depth + 1)
            else: out.append(prefix + br + k)
    walk(root, '', 0)
    return out

def tree_text(paths):
    for d in [None, 4, 3, 2, 1]:
        lines = tree_lines(paths, d)
        if len(lines) <= MAX_TREE: return lines, d
    return lines[:MAX_TREE] + ['… (cut at 300 lines)'], 1

def demote(md):
    out, code = [], False
    for l in md.split('\n'):
        if l.startswith('```'): code = not code
        if not code and re.match(r'^#{1,4}\s', l): l = '##' + l
        out.append(l)
    return '\n'.join(out)

def build(d, overview, old_body, synced):
    m = d['meta']; name = m['name']
    lines = [f"> Synced from GitHub on {fmt_date(synced)}. Claude rewrites this note at each sync, apart from the My notes section at the end.", '',
             f"**Repository:** [{m['full_name']}]({m['html_url']}) · {'Private' if m['private'] else 'Public'}" + (f" · {m['language']}" if m.get('language') else ''),
             f"**Last updated:** {fmt_date(m['pushed_at'])} (last push)", f"**Default branch:** {m['default_branch']}"]
    if m.get('description'): lines.append(f"**Description:** {m['description']}")
    lines += ['', '## Overview (generated)', overview, '']
    br = sorted(d['branches'], key=lambda b: (b != m['default_branch'], b.lower()))
    lines += [f"## Branches ({len(br)})"] + [f"- `{b}`" + (' (default)' if b == m['default_branch'] else '') for b in br] + ['']
    lines.append('## Pull requests')
    if d['open_prs'] is None:
        lines.append('Not available: pull requests cannot be read for this repository.')
    else:
        op = d['open_prs']
        lines.append(f"**Open ({len(op)}):**" + (' none.' if not op else ''))
        lines += [f"- [#{p['n']} {p['t']}]({p['url']}) · `{p['b']}`{' · draft' if p.get('draft') else ''} · updated {fmt_date(p['u'])}" for p in op]
        cl = d['closed_prs'] or []
        lines.append('')
        lines.append('**Recently closed:**' + (' none.' if not cl else ''))
        lines += [f"- [#{p['n']} {p['t']}]({p['url']}) · {'merged' if p['merged'] else 'closed unmerged'} {fmt_date(p['u'])}" for p in cl]
    lines.append('')
    lines.append('## README')
    rd = (d.get('readme') or '').strip()
    if not rd: lines.append('This repository has no README.')
    else:
        if len(rd) > MAX_README: rd = rd[:MAX_README] + f"\n\n… README cut at {MAX_README:,} characters; read the rest [on GitHub]({m['html_url']}#readme)."
        lines.append(demote(rd))
    lines.append('')
    tl, depth = tree_text(d['tree'])
    lines.append('## File structure')
    if depth is not None: lines.append(f"Folders below level {depth} are folded, with their item count.")
    lines += ['```', m['name'] + '/'] + tl + ['```', '']
    mine = ''
    if old_body and MY in old_body: mine = old_body[old_body.index(MY):].strip()
    lines.append(mine or MY + '\nAnything written under this heading is kept when the note is re-synced.')
    text = '\n'.join(lines).rstrip() + '\n'
    idx = {'title': name, 'tags': [], 'keywords': sorted({'github'} | ({m['language'].lower()} if m.get('language') else set())), 'links': [],
           'summary': '', 'overview': overview, 'source': 'github', 'created': m.get('created_at') or m['pushed_at'], 'updated': m['pushed_at'],
           'pushed': m['pushed_at'], 'url': m['html_url'], 'repo': m['full_name'], 'private': bool(m['private']), 'synced': synced,
           'summarised': None, 'words': len(text.split()), 'pinned': False}
    return idx, {'text': text, 'updated': m['pushed_at']}


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'fetch':   # GH_OWNER=<account> ghsync.py fetch <outdir> <name> [<name> ...]
        if not OWNER: sys.exit('Set GH_OWNER to the GitHub account that owns the repositories.')
        print(json.dumps(fetch(sys.argv[3:], sys.argv[2]), indent=1))
    elif cmd == 'build': # ghsync.py build <repo json dir> <overviews.json> <out.json>
        src, ov, outp = sys.argv[2:5]; overviews = json.load(open(ov))
        synced = datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z'); out = {}
        for f in sorted(os.listdir(src)):
            if not f.endswith('.json'): continue
            d = json.load(open(os.path.join(src, f))); name = d['meta']['name']
            idx, body = build(d, overviews.get(name) or 'Overview not written yet.', None, synced)
            out['gh-' + name] = {'index': idx, 'body': body}
        json.dump({'backup_of': 'Claude Notes GitHub sync', 'stamp': synced, 'notes': out}, open(outp, 'w'), ensure_ascii=False, indent=1)
        print(json.dumps({'stamp': synced, 'notes': len(out), 'bytes': os.path.getsize(outp),
                          'available': [{'name': v['index']['title'], 'pushed': v['index']['pushed'], 'private': v['index']['private']} for v in out.values()]}))
