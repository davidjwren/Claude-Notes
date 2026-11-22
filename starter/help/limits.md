Claude Notes keeps every note in the notes page's own database, which has fixed limits. This note says what they are, and how to move a folder to a second database if one ever gets close.

## The limits
- **About 12,500 notes**: the database holds 25,000 records and each note uses two (its index and its text). A few more records hold settings, activity and Recently deleted.
- **100 MB in total**, and about 250 KB of text per note.
- **1,000 records per request**: the database hands over at most 1,000 records at a time. The page keeps the newest 1,000 notes live and reads older notes (and note text, for search) in further batches of 1,000, so every note shows however many there are. With several thousand notes, opening the page and the first search take a little longer.

## Asking for a second database
1. Right-click a top-level folder (press and hold on a touch screen) and choose **Move to a second database…**. Only top-level folders have this option.
2. The dialog shows the folder's note count and how full this database is. **Record request** saves your choice; nothing moves yet.
3. Ask Claude to "move <folder> to a second database". A page can't create another database itself, so Claude does the move.

## What Claude does
1. Reads the request (`meta/split`: folder, note count, date).
2. Publishes a second notes page from this page's design, for example "Claude Notes 2", with the same settings and access rules.
3. Copies every note in the folder and its sub-folders, both records with the same ids, into the new database, then checks the counts and opens a few notes.
4. Only after the check, and after a nightly backup has run, moves the originals here to Recently deleted, and records the result and the new page's link in `meta/split`.
5. Updates any scheduled tasks (backup, summaries, GitHub, reminders) and points the `/notes` skill at both pages.

## What changes after a split
- The two pages are separate: search, the graph, Statistics and `[[links]]` work within each page only. A link to a note on the other page shows struck through.
- Your settings, colour schemes and pinned folders are kept per page.
- Moving a folder back later works the same way in reverse.

See also [[Claude Notes basics]] and [[Importing notes into Claude Notes]].
