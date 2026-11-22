The page picks its layout from the width the screen reports to it in CSS pixels (about a third of a phone's physical pixels), not from the device type.

| Width | Typical screens | Layout |
|---|---|---|
| Under 600px | Phones in portrait, Galaxy Fold cover screen | One pane at a time |
| 600 to 1100px | Fold inner screen, iPad in portrait, phones in landscape | One sidebar column beside the note |
| Over 1100px | Desktop and laptop browsers, most iPads in landscape | Three columns |

## Phone (under 600px)
- One pane at a time: folders, then a folder's notes, then the note. Back buttons at the top move between them.
- Larger buttons for touch. The folder sidebar scrolls as one, with the footer (backup, Recently deleted, Settings) at the end.
- Menus open with a long press. Drag and drop is not available.
- The hide-sidebars button and the breadcrumb are not shown.

## Tablet and folding phone opened out (600 to 1100px)
- One sidebar column beside the note. It shows either the folders or the open folder's notes list, with a back button at the top.
- The hide-sidebars button gives the note the full width.
- On touch screens, rows and buttons are a little taller.

## Desktop and web (over 1100px)
- Three columns: folders, the notes list (it slides out when you choose a folder or search), and the note.
- The notes list has its own hide button; a matching show button appears in the note bar.
- The diagonal-arrows button hides both sidebars, widens the text and shows the note's folder path as a breadcrumb.
- Drag and drop, right-click menus and keyboard shortcuts: `/` to search, Alt + ← and Alt + → for back and forward, Ctrl or Cmd + Enter to save a quick note, Esc to close dialogs.

## Every width
- The Chat panel sits beside the page on screens 1000px and wider, and covers it on narrower ones.
- The notes list closes when you open a note from anywhere other than the list (Most recent, the start page, a link, GitHub), and when Statistics or the graph opens.
- If the screen is under 560px tall, the folder sidebar scrolls as one.

## Where the page runs
- Open it in Claude (the app on iPhone, Android or iPad, or claude.ai in a browser), signed in as yourself. Elsewhere it shows "Notes are unavailable in this view".
- Settings, pins and pinned folders follow you to every device. Sort, filter and which sections are open are kept per device.
- See [[Claude Notes basics]] for what each feature does.
