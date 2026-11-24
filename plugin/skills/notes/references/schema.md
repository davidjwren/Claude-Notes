# Claude Notes database: records and rules

The page keeps the newest 1,000 notes (ordered by `updated`) live and reads older ones in batches, so a write shows on every open page within seconds.

## Notes: two records per note, same id

### `notes/<id>`: the index record

| Field | Type | Rule |
|---|---|---|
| `title` | string | Shown everywhere; `[[links]]` resolve by title, case-insensitively |
| `tags` | list of strings | Folder paths such as `Tax/Withholding/FASTER/Spain`; `/`-separated, at most 4 levels, case kept as typed, compared case-insensitively, no duplicates. A note with several tags appears in several folders. Empty list = Untagged |
| `keywords` | list of strings | Lower case, no duplicates |
| `links` | list of strings | Ids of the notes this note links to with `[[…]]` (see Links) |
| `summary` | string | Two lines; may be empty |
| `source` | string | Where the note came from: `manual`, `chat`, `research`, `code`, `starter`, `github`, or an import source |
| `created` | ISO date-time (UTC, `Z`) | Set once |
| `updated` | ISO date-time | Every change to the body or index fields (not pins or moves) |
| `summarised` | ISO date-time or null | When `summary` and `keywords` were last written by Claude |
| `words` | number | Whitespace-separated words in the body |
| `pinned` | boolean | Pinned notes show on the start page |


Repository notes (`gh-<repo>`, source `github`) also carry `overview`, `pushed`, `url`, `repo`, `private` and `synced`. They are written by the GitHub sync; do not edit their index records.

### `bodies/<id>`: the body record

`{text, updated}`. `text` is markdown, at most about 250 KiB (the database limit is 256 KiB per record). `updated` equals the index's `updated` for the same change.

### Ids

- Notes Claude creates: `c-<YYYYMMDD>-<HHMMSS>-<4 random a-z0-9>` in UTC, e.g. `c-20261122-171502-k3f9`.
- To-do lists: `todo` (standard) and `todo-<slug>` (named).
- Existing ids keep their form: notes made on the page (`<base36 time>-<4 chars>`), imported notes (whatever the import file used) and the starter notes (`welcome`, `help-…`).

## Links

For each `[[target]]` in the body (not `[[card:…]]` or `[[passwords:…]]`): take the text before `|`, then before `#`, trim it, and look it up among index titles case-insensitively (if two notes share a title, the most recently updated wins). `links` = the distinct ids found, excluding the note's own id. Unmatched links are kept in the text; the page shows them struck through.

## Writing a new note

One `batch` with two `set` writes and no `if_version`:

```json
{"op": "set", "collection": "bodies", "doc_id": "<id>", "data": {"text": "<markdown>", "updated": "<now>"}}
{"op": "set", "collection": "notes", "doc_id": "<id>", "data": {"title": "…", "tags": [], "keywords": [], "links": [], "summary": "…", "source": "chat", "created": "<now>", "updated": "<now>", "summarised": "<now>", "words": 0, "pinned": false}}
```

For long bodies, write the record to a local JSON file and pass `file_path` instead of `data`.

## Editing

1. `get` both `bodies/<id>` and `notes/<id>`; keep their versions.
2. Change the text. Keep everything you were not asked to change exactly as it was.
3. One `batch`: `set` `bodies/<id>` `{text, updated: now}` with its `if_version`, and `update` `notes/<id>` with its `if_version` for `title`, `tags`, `keywords`, `links` (recomputed), `words` and `updated: now` (plus `summary` and `summarised` if you rewrote the summary).
4. On a conflict, start again from step 1.

Pinning: `update` `notes/<id>` `{pinned}` only; `updated` stays as it was.

## Deleting (Recently deleted, 30 days)

Mirror the page: `set` `trash/<id>` `{index: <the index record without id>, body: {text, updated}, deletedAt: <now>}`, then `delete` `bodies/<id>` and `notes/<id>` (with their versions). The page restores from `trash` and purges entries older than 30 days. Never delete permanently.

## Activity (Statistics view)

`activity/<YYYY-MM-DD>` (the user's local date): `{edited: {<noteId>: <top-level folder>}, tokens: {<feature>: n}, hours: {<HH>: n}, models: {<model id>: n}}`. The top-level folder is the first segment of the note's first tag, or `Untagged`. After saving or editing a note, `get` the day's record, add `edited.<id>`, and `set` it back with its version (or create it). Leave `tokens`, `hours` and `models` alone: they count the page's own Claude features (by feature, by local hour 00 to 23, and by the model asked for).

## Other records (read only for Claude unless a reference file says otherwise)

| Record | Holds |
|---|---|
| `meta/settings` | Theme, day and night colour schemes, font, text size, plus `model` and `factModel` (`haiku`, `sonnet`, `opus` or `fable`) and `budget` (estimated tokens per 5 hours for the usage ring) |
| `meta/folders` | `{pinned: [folder keys]}`, pinned folders, lower case |
| `meta/backup` | Last nightly backup, if a backup task is set up: time, file id, note count |
| `meta/github`, `meta/githubprefs`, `meta/ghapplied` | GitHub sync (see github-sync.md); `meta/githubprefs` holds `owner` and `exclude` |
| `meta/capture` | Capture setting: `{research, code, chats, updated}`, each `off`, `offer` or `auto`. Claude writes this one |
| `meta/prefs` | Claude's preferences for this user, such as `workEmail` for handing tasks to a work inbox. Claude writes this one |
| `meta/split` | A request to move a top-level folder to a second database (written by the page) |
| `trash/<id>` | Recently deleted notes |

## Limits

25,000 records (about 12,500 notes), 256 KiB per record, 100 MB in total. A query returns at most 1,000 records; the page reads beyond that in batches. Deleting the artifact erases the database; Settings → Download all (JSON), or an optional nightly backup task, is the safeguard.
