#!/usr/bin/env python3
"""Turn a Claude Notes import file into database writes.

Usage: python3 starter_writes.py <starter.json> <out dir>

Writes body_<id>.json and index_<id>.json into <out dir> and prints a JSON list of
batch writes ({op, collection, doc_id, file_path}) for the artifact database tool.
Standard library only.
"""
import json, os, sys
from datetime import datetime, timezone


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, out = sys.argv[1:]
    os.makedirs(out, exist_ok=True)
    data = json.load(open(src, encoding='utf-8'))
    now = datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')
    writes = []
    for n in data.get('notes', []):
        nid, index, body = n['id'], dict(n['index']), dict(n.get('body') or {})
        index['created'] = index['updated'] = now  # the starter notes are new in this database
        if index.get('summarised'):
            index['summarised'] = now
        body = {'text': body.get('text', ''), 'updated': now}
        bp, ip = os.path.join(out, f'body_{nid}.json'), os.path.join(out, f'index_{nid}.json')
        json.dump(body, open(bp, 'w', encoding='utf-8'), ensure_ascii=False)
        json.dump(index, open(ip, 'w', encoding='utf-8'), ensure_ascii=False)
        writes.append({'op': 'set', 'collection': 'bodies', 'doc_id': nid, 'file_path': os.path.abspath(bp)})
        writes.append({'op': 'set', 'collection': 'notes', 'doc_id': nid, 'file_path': os.path.abspath(ip)})
    print(json.dumps(writes, indent=1))


if __name__ == '__main__':
    main()
