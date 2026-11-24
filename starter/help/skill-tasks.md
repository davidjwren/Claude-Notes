Claude Notes has three parts that work together: this page, the `/notes` skill that lets Claude work with your notes from any chat, and optional scheduled tasks that look after the notes overnight.

## The /notes skill
Type `/notes` followed by a request in any Claude chat, or just ask in plain words. The skill finds this page by its title, Claude Notes.

| Ask | What happens |
|---|---|
| "save this as a note in Work/Projects" | Claude writes a note from the chat, with a title, tags, a summary and keywords |
| "find my notes on onboarding" | Searches titles, tags, keywords and summaries, then the text if needed |
| "open …", "add to …: …", "edit …" | Shows, appends to or changes a note; the rest stays as it was |
| "pin …", "delete …" | Pins, or moves to Recently deleted after asking once |
| "add to my to-do list: …" or "remind: …" | Adds a task to the To-do list |
| "add to my Work to-do list: …" | Adds to a named list, creating "Work to-do" if needed |
| "done …", "show my to-do list" | Ticks a task off, or lists open tasks |
| "send … to my work email" | Emails the task (it asks for the address once) and ticks it as sent |
| "capture research auto" | Changes when Claude saves notes for you (below) |
| "save to Web Saves: <link or text>" | Saves a web page as a note in Web Saves ([[Web Saves in Claude Notes]]) |
| "tidy Web Saves" | Combines, files and tidies the Web Saves notes, after showing you the plan |
| "add to my Research to-do list: <topic>" | Queues a topic for the optional Research task (below) |
| "cards …" | Fills in real titles and descriptions for the link cards in a note |
| "sync GitHub" | Refreshes the GitHub repository notes ([[GitHub sync in Claude Notes]]) |
| "change the notes page so that …" | Edits this page ([[Changing Claude Notes with Claude]]) |

**Capture**: Claude can offer to save, or save automatically, at the end of research, a code session or a long chat. Each kind is off, offer or auto; all start at offer. A skill only loads when a request matches it, so for capture to happen reliably add a line to your Claude preferences such as: "At the end of research, a code session or a long chat, use the notes skill and follow my notes capture setting."

## Scheduled tasks (optional)
Scheduled tasks run in Claude on a timetable while you are away. Each is set up once by asking Claude, with the prompts in the project's README on GitHub:

- **Note summaries**, nightly: writes the two-line summary at the top of each note edited since its last summary.
- **Backup**, nightly: saves every note as one dated JSON file to your cloud storage. The sidebar footer shows the last backup.
- **GitHub sync**, nightly: refreshes the repository notes.
- **Reminder digest**, morning and evening: sends a phone notification listing open to-do tasks.
- **Research queue**, nightly: each open task in the to-do list named Research is a topic. Claude searches the web for up to five a night, writes a note of at most 500 words with its sources in the `Research` folder, ticks the task off with a link to the note, and adds any further questions as new tasks for another night.
- **Ideas**, nightly: looks over the notes you made or changed in the last 14 days, what you searched for and what you opened, and writes up to five ideas (recurring themes, links between folders, questions you keep asking), each with its own note in `Ideas`. They show on the start page.
- **Web Saves**, nightly: runs only when you chose **Schedule for overnight** in the Web Saves folder, and writes a note saying what it did.

Without the tasks, everything still works: summaries can be asked for, Settings → Download all (JSON) saves a copy, and "sync GitHub" runs on request.
