# Worklog

## 2026-11-24 (later): Phase 2, and two fixes

Live page published as version 59.

- Graph view and Statistics are left out of the button rule: their controls are plain again (one CSS block scoped to `.graphview, .statsview`).
- Statistics heatmap looked blank: the shade was a share of the busiest day, and the import day (221 notes) pushed every other day to the faintest step. Now fixed steps (1, 2 to 3, 4 to 7, 8 or more), and the first step is a little darker.
- Mermaid: a `mermaid` code block is drawn in the reader (`mmdSvg`, `drawMermaid`); mermaid 10.9.1 loads from jsdelivr on first use; redrawn on theme change.
- Mind map this note (Actions): one Claude call, checked by `mermaid.parse`, preview, then Insert or Discard.
- Format code (Actions): JSON by `JSON.parse`, YAML by the `yaml` package (`import()` of its jsdelivr `+esm` build), Python by Claude with a white-space-only check. It reuses the Auto-improve dialog.

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
