What the notes page shows for each piece of markdown. Type it in the editor; the reader formats it. See [[Claude Notes basics]] for the editor itself.

## Text
- `**bold**` shows as **bold**
- `*italic*` or `_italic_` shows as *italic*
- `~~struck~~` shows as ~~struck~~
- Single backticks around text show it as `code`

A single line break inside a paragraph is kept as a line break. A blank line starts a new paragraph.

## Headings
```
# Heading 1
## Heading 2
### Heading 3
```
A first line that repeats the note's title is hidden in the reader, so imported notes don't show their title twice.

## Lists and tasks
```
- bullet (also * or +)
1. numbered (also 1))
- [ ] open task
- [x] done task
```
Nested lists show as one flat list. Task boxes are for display; tick a task by editing the text or asking Claude ("done <task>").

## Quotes, rules and code
```
> quoted text
---
```
Three backticks on their own line open and close a code block.

## Tables
```
| Country | Rate |
|---|---|
| Spain | 19% |
```

## Links
- `[text](https://…)`: a web link inside a sentence
- A web address inside a sentence links automatically
- A link on a line of its own, either a bare address or `[text](https://…)`, shows as a card with the site's icon, the title and the site name
- `[[Note title]]`: links to another note, matched by title in any case
- `[[Note title|label]]`: shows the label instead of the title
- `[[Note title#Heading]]`: shows "Note title › Heading"
- `[[card:https://…|Title|Description]]`: a link card with the site's icon
- `[[passwords:Item name]]`: a chip that copies the item name for Apple Passwords

A `[[link]]` to a title that doesn't exist shows struck through. Images and HTML are not shown.
