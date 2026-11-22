Everything you can do on the notes page, in one place. For how the page looks on each device, see [[Claude Notes on each device]].

## Writing
- **New note**: the pencil button at the top of the sidebar, the New note button on the start page, or the one in a folder's notes list (that one tags the note with the folder).
- **New to-do list**: the button on the start page opens a new note tagged To-do, with a first empty task. Give it a title and add tasks.
- **Quick note**: click into the Quick note box at the top of the sidebar and it opens out. The first line becomes the title; Save (or Ctrl or Cmd + Enter) puts it in Untagged, and Cancel or Esc clears it.
- **Edit and Done**: press Edit (or double-click the text) to write in markdown. Notes save about 1.5 seconds after you stop typing, and the note bar shows "Saved" with the time. See [[Markdown cheatsheet]].
- **View mode**: in the editor, View mode shows headings, bold and links formatted while you type. The text underneath is still plain markdown.
- **Another device**: if the note changes on another device while you are editing, a warning offers "Load theirs" or "Keep mine".

## Tags, folders and keywords
- **Tags** are comma-separated; a slash makes a sub-folder, up to 4 levels: `Work/Projects/Alpha, Reading`. A note with several tags appears in several folders.
- **Folders** in the sidebar come from the tags. A folder lists the notes tagged with that folder itself; sub-folders appear as rows at the top of the list.
- **Keywords** are extra search words, kept in lower case.
- **To-do**: the first row of the sidebar lists every note tagged `To-do`, such as your to-do lists. These notes do not appear under Folders.
- **Pinned**: pin a note, or a folder, from its menu. Pinned notes show on the start page; pinned folders sit below Untagged.
- **Help**: the Help section, below Most recent, lists every note tagged `Help` (including sub-folders such as `Help/Setup`). These notes do not appear under Folders.
- **Sections**: Folders, GitHub (once you have synced repositories), Most recent and Help open and close with the + and − on the right of each heading.

## Menus, moving and deleting
- **Menus**: right-click a note or folder, or press and hold it on a touch screen.
- **Notes**: Pin, Move to… (pick or type a folder) and Delete.
- **Folders**: Pin folder, Rename… and Move to…. Renaming or moving a folder retags every note under it, after a confirmation, with Undo for 10 seconds.
- **Drag and drop** (mouse or trackpad): drop a note on a folder to move it there; hold Option or Alt to add the tag and keep the others. Drop a folder on another folder to nest it.
- **Delete** moves a note to Recently deleted (sidebar footer) for 30 days, where you can restore it.

## Finding notes
- **Search** (or press `/`): every word must match. It looks at titles, tags, keywords and summaries straight away, then at note text.
- **Sort and filter**: the notes list sorts by date modified, date created or title, and filters by tagged, untagged or top-level folder.
- **Most recent**: the 10 latest edited notes, in the sidebar.
- **Back and forward**: ‹ and › in the note bar, or Alt + ← and Alt + →, step through the notes you have opened.
- **Direct link**: each note has its own address ending `#n-<id>`.

## Links between notes
- Type `[[Note title]]`, or use **Link a note** in the editor. The reader shows "Linked from" under any note that others link to.
- **Graph view** shows notes as dots and links as lines, coloured by top-level folder. With **Folders** on, each folder is a ring joined to its notes, so unlinked notes sit with their folder. Click a note to open it, or a folder to open its list.

## Claude on the page
- **Summary box**: a two-line summary at the top of most notes, written by Claude and refreshed nightly after edits.
- **Chat** (speech bubble): ask about the open note; insert the answer, replace the note text, or save it as a new note.
- **Auto-improve** (wand): suggests keywords, links to other notes and sources the note names. You tick what to apply; Undo reverses it.
- **Write with Claude** and **Summarise a document**: in the editor.
- **Paragraph tools**: in the reader, the sparkle button beside a paragraph offers Rewrite, Shorten and Expand.

## Other features
- **Statistics**: a 12-month activity heatmap, notes this day, week and month, and an estimate of Claude use on the page.
- **Settings**: Light, Dark or System; day and night colour schemes; font; text size; Import. Settings apply on every device.
- **Passwords links**: `[[passwords:Item name]]` shows a key chip that copies the item name to search in Apple Passwords. No secret is stored.
- **Link cards**: a link on a line of its own (a web address, or `[text](address)`) shows as a card with the site's icon, a title and the site name, automatically. A link inside a sentence stays an ordinary link. The page can't read other websites, so the title comes from the link text or the address; ask Claude (`/notes cards <note>`) for real titles and descriptions.
- **Backups**: the sidebar footer shows the last nightly backup (if you set up the optional backup task); Settings → Download all (JSON) saves a copy now.
- **From any Claude chat**: the `/notes` skill saves, finds and edits notes, and keeps the To-do lists. See [[Claude Notes skill and scheduled tasks]].
- **Changing the page**: Claude can change this page to suit you. See [[Changing Claude Notes with Claude]].
