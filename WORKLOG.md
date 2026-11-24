# Worklog

## 2026-11-24 (usage ring fixed)

Live page is version 81. The ring read zero because its figures lived in the day's activity record, which Claude's skill also writes; on 24 Nov that record had been replaced (58 versions, two `edited` entries, no tokens). The ring now has its own record, `meta/usage` (8 days, page only), shows a call at once, and reports a failed save in the usage box. schema.md and SKILL.md now say to add to a day record with `update`, never `set` over it. Test: `pu.js`.

## 2026-11-24 (sidebar hover)

Live page is version 80. Sidebar rows (folders, Most recent, Help, GitHub) show the note list's hover: the tint plus a slim accent bar on the left; the open folder keeps a solid bar. One CSS rule on `.frow`, asked for in a comment.

## 2026-11-24 (note bar buttons; Web Saves drop-down)

Live page is version 79. Actions and Edit/Done in the note bar are 1pt bigger again (12.33px, `.modebtn`), asked for in a comment. Another session had replaced the four Web Saves buttons with one drop-down (`#wssel`, "Tidy Web Saves with Claude…"); that is kept on the live page and copied into the repo, and `p34.js` now drives the drop-down. The Help note still says "four buttons".

## 2026-11-24 (live edits from another session)

Live page is version 77. While the colour scheme change was going out, another session published to the live page several times. Those edits were kept on the live page and copied into the repo: the brand reads "Notes" on the live page only (repo still "Claude Notes"); selects draw their own drop-down arrow; "Mind map the links" is now "Map Links"; larger colour chips in the scheme pickers; Settings headings in the accent colour. Make page changes from one conversation at a time, or each publish has to be merged by hand.

## 2026-11-24 (colour scheme boxes)

The Day and Night colour scheme pickers in Settings are no longer tinted: they take the page background and the same border as the Font and Text size boxes (asked for in a comment). One CSS rule, `.csbtn`.

## 2026-11-24 (button text)

Live page published as version 72 (71 was a rename to "Notes" on the live page, made elsewhere and kept). Text on action buttons is 11px, 1pt up from 9.67px (asked for in a comment on the Edit button); the sidebar and the Graph and Statistics bars are unchanged.

## 2026-11-24 (code colours)

Live page published as version 70.

- A fenced code block that names its language is syntax-coloured in the reader (`drawCode`): highlight.js 11.9.0 from jsdelivr, loaded on first use; `md()` now puts the language on the block as `data-lang`. Colours are the `.hljs-*` rules, taken from the page tokens. No linting; the text is unchanged; offline or unknown language leaves the block plain.
- Not coloured: the before and after panes in the Format code review, and code in Edit and View mode.
- Test: `pc.js` (light, dark, library blocked).

## 2026-11-24 (last): bookmarklet removed

The Web Saves bookmarklet was clunky in use, so it is gone: `docs/bookmarklet.md` deleted, and its mentions taken out of the README, the skill (SKILL.md, web-saves.md) and the Help note "Web Saves in Claude Notes" (starter and live). Captures now come only from "save to Web Saves" in a chat. The page never held bookmarklet code, so it stays at version 69.

## 2026-11-24 (late night): Format code takes XML

Live page published as version 69.

- `fmtXml`: blocks marked `xml`, `xsd`, `xsl` or `xslt`. The browser's parser checks the block is well formed; the text is then re-indented tag by tag (two spaces), so the declaration, comments, CDATA and attributes stay as written. Refused unless only white space changed. No Claude call.
- Known limit: text mixed with child elements is trimmed onto its own line, and `xml:space="preserve"` is not honoured.
- Test: `px.js`.

## 2026-11-24 (night): large mind maps, process diagram, tabbed Settings

Live page published as version 68.

- Mind maps have two layouts (`mmSvg` picks, `mmDraw` draws). A map whose ring would be wider than 760px (358px on a phone) is drawn as a tree: centre in the middle with branches down both sides, or on a phone the centre on top and the branches in a chain under it. Type is larger in the tree (lists 11px) and the map grows down the page. The ring's first circle of spokes is now only as long as its circles need.
- Process diagram in the paragraph tools (`runFlow`): Claude returns a mermaid flowchart of the paragraph, or of the text selected in the reader; mermaid parses and draws it; it reuses the mind map dialog and goes in under the paragraph.
- Settings has four tabs down the left, styled like the sidebar: Appearance, Model Selection, Security (a placeholder until Phase 5) and Import/Export.
- Text action buttons (`.btn`) are 4pt smaller (9.67px), except in the sidebar and the Graph and Statistics bars.
- Tests: `p5.js` (7 checks), `mm.js` now also checks that no line crosses a circle it does not join and that the text is not shrunk below 0.75.

Not done from the mind map ideas: staggered spoke lengths, detail spokes turning back to the centre, and several centres in one map (mermaid allows one root).

## 2026-11-24 (evening): Phases 3 and 4

Live page published as version 67.

- Mind map the links (Actions, `runLinks`): the open note, its links and backlinks, and theirs, capped at about 60 circles; no Claude call. "Ask Claude to group the branches" regroups the same notes.
- Mind map these notes (`#nmap` in the notes list head, `runTopicMap`): a folder with its sub-folders, or the current search. Sends title, tags, keywords and summary only (60,000 character cap), shows count and estimate first, and saves as a note tagged `Mind maps`, source `mindmap`. A map label that is a note's title (also written `[[Title]]`) opens that note in the reader.
- Ideas: `meta/ideas` drives a start-page section under Pinned, with Dismiss. The page now logs `activity.searches` (list, 50 a day) and `activity.opened` (counts).
- Web Saves (`wsRun`, `WS_PLAN`, `WS_APPLY`): four buttons in the Web Saves folder; each step is planned by Claude, reviewed in the Auto-improve dialog, then applied; a replacement is written before its original goes to Recently deleted. Over 10 notes: Proceed, Cancel or Schedule for overnight (`meta/websaves`). `confirmBox` takes an optional third button.
- Combine differs from the brief: one call groups all web saves from titles and opening lines, then one call per group drafts the merge, so related saves are found across batches. Add and Create run in batches of 8.
- Docs: `docs/bookmarklet.md`, `plugin/skills/notes/references/web-saves.md` (the page's prompts follow it), three new prompts in `docs/scheduled-tasks.md` (Research queue, Ideas, Web Saves), a new Help note "Web Saves in Claude Notes", SKILL.md, schema.md, README.
- Tests: `p34.js` (17 checks: maps, Ideas, activity, Web Saves at desktop, phone dark and read-only), `bm.js` (both bookmarklet versions agree; a long page is cut), `help.js`; the older suites still pass on both copies.

Not checked: whether `claude.ai/new?q=` fills the message in (the built-in browser was not signed in), so the bookmarklet also copies to the clipboard. None of the three new scheduled tasks is set up, and their prompts have not been run. The Web Saves prompts were tested against a stand-in for Claude, not real answers.

Not done: Phase 5 (encrypted folders, file links).

## 2026-11-24 (later): Phase 2, and two fixes

Live page published as version 59.

- Graph view and Statistics are left out of the button rule: their controls are plain again (one CSS block scoped to `.graphview, .statsview`).
- Statistics heatmap looked blank: the shade was a share of the busiest day, and the import day (221 notes) pushed every other day to the faintest step. Now fixed steps (1, 2 to 3, 4 to 7, 8 or more), and the first step is a little darker.
- Mermaid: a `mermaid` code block is drawn in the reader (`mmdSvg`, `drawMermaid`); mermaid 10.9.1 loads from jsdelivr on first use; redrawn on theme change.
- Mind map this note (Actions): one Claude call, checked by `mermaid.parse`, preview, then Insert or Discard.
- Format code (Actions): JSON by `JSON.parse`, YAML by the `yaml` package (`import()` of its jsdelivr `+esm` build), Python by Claude with a white-space-only check. It reuses the Auto-improve dialog.

- Follow-up (version 60): on a phone the heatmap scrolls sideways and opened at the oldest months, so recent activity was off screen; that was what looked blank. It now opens at the newest weeks.

- Follow-up (version 61): mind maps are two colours from the page tokens (accent for root, branches and outlines; ink for words), by CSS over mermaid's own SVG classes, so palettes and dark mode follow with no redraw. Other diagram types keep mermaid's theme.
- For Phase 5: every option that sends an encrypted note to Claude must confirm first, with a Security setting to turn that off. Written into item 16 of the build brief.

- Follow-up (version 62): all diagrams take their look from the page (`mmdLook`: page font at 13px, thin quiet lines, accent outlines; `mmdPut` shrinks arrowheads and rounds boxes). Mermaid loading from jsdelivr is confirmed working in the real Claude frame on iPhone.

- Follow-up (version 63): mind maps are now drawn by the page, not mermaid (`mmParse`, `mmSvg`, `mmHtml`, `mmIcons`): a ring layout of circles, icons on the centre and main branches, key-point boxes beside or under the map. The note text stays mermaid mindmap syntax; `::icon(name)` takes a Material Symbols name and `%% box: Title | text` lines are the boxes. Font Awesome cannot load in the Claude frame (only Google Fonts stylesheets and fonts are allowed), so icons come from Google's Material Symbols, fetched as a subset of just the names used. The earlier mermaid mind map CSS is gone.

- Follow-up (version 64): the two sidebar rows, Graph view and Statistics, are plain again too (that is what was meant by excluding them); the controls on those two pages stay plain as well.

- Follow-up (version 65): mind map labels are centred and move down only once an icon is really showing; Export to Mermaid in the mind map dialog (a .mmd file, else the clipboard); fixed a race where two maps on one page left the first without icons. Open: icons did not show in the Claude iPhone app (seen in the user's screenshot of version 63); not yet known whether that is the app blocking the font or a WebKit difference. Not tested in WebKit here.

- Follow-up (version 66): mind maps have three circle levels (centre, main branches, up to three details each); a detail's own points show as a list of up to six beside its circle, always left or right, with an accent bar. Key-point boxes capped at three, set smaller, with more space above. Icons confirmed working on Mac and still missing in the Claude iPhone app; added ligature hints for Safari's engine to `.mmi`, untested (no WebKit on this PC).

Tested the same way as before, now 38 checks. Not checked in the real Claude frame: that the two jsdelivr loads pass the frame's content rules (the `+esm` import is the one to watch), and whether the frame draws `mermaid` blocks itself as well.

Not done: Phases 3 to 5.

## 2026-11-24: build brief, Phase 1 and 1b

Built from `docs/build-brief.md` (kept local, not committed). Live page published as version 58.

- Actions menu on the note bar (Auto-improve, Write with Claude, Summarise, Share); the wand button and the two Claude items in the editor's Tools menu are gone.
- Summarise: "This note" (goes at the top under `## Summary`, with Undo) or "A document"; model picker remembered per device.
- Share: share sheet, falling back to copy.
- To-do lists tick in the reader. `tickTask` in the page and `notes_helper.py todo-done` now both put a ticked task at the end of `## Done`.
- Model choice: `MODELS` and `modelOpts(task)` are the only place for ids and tiers; `meta/settings` gained `model`, `factModel`, `budget`.
- Fact-check in the paragraph menu, with a `search_notes` page tool (5 calls at most).
- Usage ring in the sidebar footer; `activity/<date>` gained `hours` and `models`.
- Rule 8 (buttons accent or secondary) and rule 9 (menu icons) applied in one CSS block near the end of the stylesheet.

How it was tested: headless Chrome through playwright-core with a stand-in `window.claude` (in-memory db, scripted `sample`), 29 checks at desktop, tablet, phone, dark and read-only. The harness lived in the session scratchpad and is not in the repo.

Not done: Phases 2 to 5 of the brief (Mermaid, mind maps, code formatting, research queue, Ideas, Web Saves, encrypted folders, file links). Share and model fallback are untested inside the real Claude frame. `docs/screenshots` still show the old note bar.

The live page differs from `page/claude-notes.html` by more than the five strings the brief lists (prompts name the owner, the GitHub section always shows). To publish: read the live artifact, apply the same change to its inner document, publish to the same URL without `capabilities`.
