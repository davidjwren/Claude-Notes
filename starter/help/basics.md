Everything you can do on the notes page, in one place. For how the page looks on each device, see [[Claude Notes on each device]].

## Writing
- **New note**: the pencil button at the top of the sidebar, the New note button on the start page, or the one in a folder's notes list (that one tags the note with the folder).
- **New to-do list**: the button on the start page opens a new note tagged To-do, with a first empty task. Give it a title and add tasks.
- **Ticking tasks**: tick a task's box in the reader (not in Edit). In a To-do list the task gets ` · done <date>` and moves to the end of `## Done`; unticking it there sends it back to the open tasks. In any other note the box just ticks in place. To add a task, press Edit or ask Claude (`/notes`).
- **Quick note**: click into the Quick note box at the top of the sidebar and it opens out. The first line becomes the title; Save (or Ctrl or Cmd + Enter) puts it in Untagged, and Cancel or Esc clears it.
- **Edit and Done**: press Edit (or double-click the text) to write in markdown. Notes save about 1.5 seconds after you stop typing, and the note bar shows "Saved" with the time. See [[Markdown cheatsheet]].
- **Tools menu**: the Tools button beside the tags holds Link a note, View mode and Focus mode. View mode and Focus mode show a tick when on.
- **View mode**: shows headings, bold and links formatted while you type, and is on unless you turn it off. The text underneath is still plain markdown.
- **Tags and keywords**: in the editor they sit folded on one line under the title; click it to change them.
- **Focus mode**: hides everything but the title and text, and fades the lines away from the cursor. Choose it from Tools, or press Ctrl or Cmd + Shift + F; Esc or Done leaves it.
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
- **Ideas**: with the optional Ideas task set up, the start page lists up to five ideas Claude found across your recent notes, under Pinned. Click one to open its note; Dismiss takes it off the list (the note stays).
- **What is recorded**: so that Ideas has something to work from, the page keeps your search terms (up to 50 a day, in lower case) and a count of the notes you open, in the notes database beside the activity it already logs for Statistics. The page sends them nowhere.
- **Back and forward**: ‹ and › in the note bar, or Alt + ← and Alt + →, step through the notes you have opened.
- **Direct link**: each note has its own address ending `#n-<id>`.

## Links between notes
- Type `[[Note title]]`, or use **Link a note** in the editor's Tools menu. The reader shows "Linked from" under any note that others link to.
- **Graph view** shows notes as dots and links as lines, coloured by top-level folder. With **Folders** on, each folder is a ring joined to its notes, so unlinked notes sit with their folder. Click a note to open it, or a folder to open its list.
- **Mind map the links** (Actions menu): draws the open note in the centre, the notes it links to or is linked from around it, and their own links on the outer ring, without using Claude. **Ask Claude to group the branches** sorts the same notes into themes.
- **Mind map these notes**: the branch button at the top of a notes list draws a mind map of that folder (with its sub-folders) or of the current search. It shows how many notes are involved and an estimate before Claude is asked, and sends each note's title, tags, keywords and summary, never its text. Save it as a new note in `Mind maps`, or Discard. In a saved map, a note's name opens that note.

## Claude on the page
- **Summary box**: a two-line summary at the top of most notes, written by Claude and refreshed nightly after edits.
- **Chat** (speech bubble): ask about the open note; insert the answer, replace the note text, or save it as a new note.
- **Actions menu**: the Actions button in the note bar (three dots on a phone) holds Auto-improve, Write with Claude, Summarise, Mind map this note, Mind map the links, Format code, Export as Markdown and Export as PDF. It works in the reader and in Edit; in the reader, new text goes at the end of the note.
- **Auto-improve**: suggests keywords, links to other notes and sources the note names. You tick what to apply; Undo reverses it.
- **Summarise**: choose **This note** (the summary goes at the top under `## Summary`, with Undo) or **A document** (text, markdown, HTML, CSV, Word or PDF), a length and a model.
- **Mind map this note**: Claude draws the note as a mind map: the subject in the centre, the main branches around it with an icon each, up to three details on the outer ring for each branch, short bulleted points beside a detail where they add something, and two or three boxes of key points beside the map (under it on a narrow screen). A map too large to read as a ring is drawn as a tree instead, with the branches down both sides of the centre (on a phone, under it), so the text keeps its size and the map grows down the page. It uses two colours, your accent and the text colour. You see a preview first; Insert adds it to the note as a `mermaid` block, Discard drops it. See [[Markdown cheatsheet]] to write or change one by hand.
- **Format code**: tidies the code blocks marked `json`, `yaml`, `xml` (also `xsd`, `xsl`) or `python` in the open note. Each block is shown before and after with a tick box; only ticked blocks change, and Undo reverses it. JSON, YAML and XML are formatted on the page (YAML and XML comments are kept; XML is only re-indented, and a block that is not well formed is reported and left alone); Python is re-spaced by Claude and refused if anything but spacing changed. It formats; it does not check the code for mistakes.
- **Export**: **Export as Markdown** saves the note as a `.md` file. **Export as PDF** saves it laid out as a document, in light mode with your day colour scheme whatever the page is showing, with diagrams as pictures. The PDF uses its own font (Roboto), so code is not monospaced and characters outside Latin, Greek and Cyrillic are left out.
- **Paragraph tools**: in the reader (not in Edit), the sparkle button beside a paragraph offers Rewrite, Shorten, Expand, Process diagram and Fact-check.
- **Process diagram**: Claude draws the steps and decisions in the paragraph as a flowchart. Select text in the reader first (a list, or several paragraphs) and it draws the selection instead. You see a preview; Insert puts it under the paragraph as a `mermaid` block.
- **Fact-check**: lists the checkable claims in one paragraph with a verdict each (supported, doubtful, incorrect, can't verify), a reason and what to check. Claude has no live web access on this page: it checks against its own knowledge and your other notes, so verify anything important at source. Nothing changes in the note unless you choose Insert, which adds the result as a quote under the paragraph (Undo reverses it).
- **Model choice**: Settings has "Claude model for notes tasks" (Sonnet unless you change it) and a separate "Fact-check model" (Opus unless you change it). Haiku uses least of your plan; Opus and Fable use more of your plan's limits. If the chosen model can't answer, Claude's nearest model does and the result says so.

## Encrypted notes
Encryption makes the stored copy of a note unreadable and unsearchable to anyone with access to the notes database, including Claude's `/notes` skill and the scheduled tasks. It is meant to keep private notes out of reach, not to be unbreakable.

- **Set up**: Settings, Security, **Set up encryption** (or the first time you encrypt something). Choose a password of at least 12 characters. You are then shown a **recovery key** once: copy or download it and keep it somewhere that is not this page.
- **Encrypt a folder**: in the folder's menu, **Encrypt folder…**. Notes saved in it and its sub-folders from then on are encrypted, and it offers to encrypt the notes already there. The folder shows a padlock; its name stays readable.
- **Encrypt one note**: the padlock button in the note bar says **Not encrypted** or **Encrypted**. Its menu encrypts or decrypts the note, or locks everything.
- **What is hidden**: the title, text, tags, keywords and links. In the database the note is listed only as "Locked note", with its dates and the encrypted folder it is in.
- **Unlocking**: the password is asked once each time the page is opened, when you open an encrypted note or press the padlock at the foot of the sidebar. Until then encrypted notes show as "Locked note" and search does not find them. **Lock now** hides them again.
- **Moving**: moving a note into an encrypted folder encrypts it, after asking. Moving one out asks whether to decrypt it or keep it encrypted. Typing an encrypted folder's name into a note's tags encrypts it at the next save.
- **Claude**: an unlocked encrypted note can still use the Claude features and the exports, but each one first asks "This sends the note text to Claude in plain text. Continue?". Settings, Security can turn the question off. Encrypted notes are left out of everything Claude does across notes: Auto-improve's list of other notes, mind maps of folders, fact-check look-ups and Web Saves.
- **Forgotten password**: on the unlock box choose **Use the recovery key**, then set a new password. Changing the password never rewrites your notes.
- **Limits**: it does not protect text you send to Claude, or a note while it is open on screen. If the password and the recovery key are both lost, nobody can recover the notes. Recently deleted and Download all keep encrypted notes encrypted. Claude's skill cannot read, summarise or edit an encrypted note, and there are no passkeys.

## Other features
- **Diagrams**: a code block marked `mermaid` shows as a diagram in the reader. See [[Markdown cheatsheet]].
- **Statistics**: a 12-month activity heatmap, notes this day, week and month, and an estimate of Claude use on the page.
- **Settings**: four tabs. Appearance (Light, Dark or System; day and night colour schemes; font; text size), Model Selection, Security (encryption, below) and Import/Export. Settings apply on every device.
- **Passwords links**: `[[passwords:Item name]]` shows a key chip that copies the item name to search in Apple Passwords. No secret is stored.
- **Link a file**: **Link a file** in the Actions menu (or the editor's Tools menu) takes a share link from Google Drive, OneDrive, SharePoint, Dropbox or iCloud and adds a card with a label you choose. Nothing is uploaded or stored in Notes, and only `https` links are accepted. Pictures are not shown inline.
- **Link cards**: a link on a line of its own (a web address, or `[text](address)`) shows as a card with the site's icon, a title and the site name, automatically. A link inside a sentence stays an ordinary link. The page can't read other websites, so the title comes from the link text or the address; ask Claude (`/notes cards <note>`) for real titles and descriptions.
- **Web Saves**: pages you capture from the web land in the `Web Saves` folder, where four buttons tidy them into proper notes with Claude. See [[Web Saves in Claude Notes]].
- **Backups**: the sidebar footer shows the last nightly backup (if you set up the optional backup task); Settings → Download all (JSON) saves a copy now.
- **From any Claude chat**: the `/notes` skill saves, finds and edits notes, and keeps the To-do lists. See [[Claude Notes skill and scheduled tasks]].
- **Changing the page**: Claude can change this page to suit you. See [[Changing Claude Notes with Claude]].
