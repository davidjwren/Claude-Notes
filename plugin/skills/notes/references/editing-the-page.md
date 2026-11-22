# Changing the notes page

The notes page is one HTML file published as a Claude artifact. Its notes live in the artifact's database, which is kept when the page is republished, so changing the page never touches the notes, as long as the record shapes in `schema.md` stay the same.

## Before changing anything

1. Find the page (SKILL.md, Finding the notes page) and read it with the Artifact tool (`action: read`). Read every line of the saved file it returns; a publish is refused until you have.
2. Work on a copy: the saved file has a service wrapper (a first line starting `<!doctype html><html><head><meta charset=utf8>` and closing `</body></html>` lines). Copy the inner document (from `<!DOCTYPE html>` to its `</html>`) to the working directory and edit that.
3. Confirm the change with the user in plain terms if it is more than a small tweak: what will look or behave differently, and on which devices.

## Making the change

- Keep the page self-contained: inline CSS and JS, no new external scripts except from the hosts the Artifact tool allows.
- Keep colours in the CSS custom properties at the top (`--acc`, `--sys`, `--ink` and the palettes), so light, dark and every colour scheme keep working.
- Keep the database contract: records `notes/<id>`, `bodies/<id>`, `trash/<id>`, `activity/<date>` and the `meta/*` records, with the fields in `schema.md`. If a change needs a new field, add it without removing old ones, and tell the user.
- Keep the layouts: under 600px, 600 to 1100px, and over 1100px (see the Help note "Claude Notes on each device").
- Test before publishing where code execution is available: load the copy in a headless browser with a small stand-in for `window.claude` (a `use()` that returns a fake `db` with `collection().orderBy().where().limit().get()/onSnapshot()` and `doc().get()/set()/update()/delete()`), with a handful of sample notes. Check for script errors and take a screenshot of the changed part.

## Publishing

- Publish the edited file to the same artifact (`url` = the page's URL) so the link stays the same. Leave `capabilities` out, so the stored declaration (db rules, sample, user, downloads, assets) carries over unchanged.
- If the publish is refused because the page changed elsewhere, read it again, merge your change into the newer version, and publish once more. Make page changes in one conversation at a time.
- Earlier versions stay in the artifact's history, so a change can be rolled back.

## Afterwards

- Update the Help notes that describe the changed feature (notes tagged `Help`), so the page and its help agree.
- Tell the user in a line or two what changed and what to check on their devices.
