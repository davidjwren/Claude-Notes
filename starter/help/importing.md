Notes can come in from files, from other apps through Claude, and from any Claude chat. Notes that are already here are never duplicated.

## Settings → Import (on the page)
- Choose a Claude Notes JSON file: a nightly backup, a Download all file, or a file Claude has prepared from another app.
- Notes whose id already exists are skipped, so importing the same file twice is safe. The page writes two records per note, retries if the database is busy, and shows progress. Keep the page open until it finishes.
- This is also how you **restore from a backup**: import the backup file, after deleting any notes you want replaced.

The file is JSON in this shape:

```
{"backup_of": "Claude Notes", "notes": [
  {"id": "v-1a2b3c4d5e6f",
   "index": {"title": "…", "tags": ["Work/Projects"], "keywords": [], "links": [], "summary": "", "source": "import", "created": "2026-11-22T10:00:00Z", "updated": "2026-11-22T10:00:00Z", "summarised": null, "words": 120, "pinned": false},
   "body": {"text": "markdown…"}}
]}
```

## Other apps
- Ask Claude to bring notes across through a connection to the app (for example Apple Notes on a Mac, or a notes app with a Claude connector). Images are not imported; they are marked where they were.
- Claude leaves out anything holding secrets (account numbers, passwords). Long poems, lyrics and book quotes are not copied in full; a placeholder marks where to paste them.

## From a Claude chat
- `/notes save this` (or "save this as a note in Work/Projects") turns research, a chat or code work into a note, with a summary and keywords.
- With the capture setting on, Claude offers (or saves automatically) at the end of research, a code session or a long chat. Change it with `/notes capture research auto`, `… offer` or `… off`.

## From a document
- In the editor, **Summarise a document** reads a text, markdown, HTML, CSV, Word or PDF file in the browser and inserts Claude's summary into the note.

To bring in notes from another app (Obsidian, Apple Notes, a folder of markdown files), ask Claude to turn them into a file in the format above, then use Settings → Import. For GitHub repositories, see [[GitHub sync in Claude Notes]].
