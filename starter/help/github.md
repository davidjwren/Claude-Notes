Claude can keep one note per GitHub repository, in a GitHub section of the sidebar, rewritten from GitHub on request or each night. Each note keeps a **My notes** section at the end for your own text.

## Getting started
- Ask Claude to "sync GitHub" (or `/notes sync github`). The first time, Claude asks which GitHub account to sync. Claude needs read access to your repositories through its GitHub connection.
- Open this page afterwards: it applies the sync and the GitHub section appears in the sidebar.

## What a repository note holds
- Repository link, private or public, main language, last push and default branch.
- **Overview (generated)**: one paragraph written by Claude from the README and file tree. It is rewritten only after a new push.
- Branches, open pull requests and the five most recently closed.
- The README (headings shifted down a level), and the file structure, with deep folders folded to an item count.
- **My notes**: anything under this heading is kept at every sync. Pins are kept too.

## When it syncs
- Nightly, if you set up the optional scheduled task (see the project's README on GitHub).
- For a sync now, ask Claude to "sync GitHub" (or `/notes sync github`).
- Right-click the GitHub heading (press and hold on a touch screen) for **Sync now** and the last sync time. A page cannot start Claude, so Sync now records a request for the next run.

## How it reaches the page
1. Claude reads each repository through its GitHub access (read only), builds one file of repository notes, and attaches it to the notes page.
2. The next time you open the page, it applies the file: it writes the repository notes, keeps My notes and pins, and moves notes for repositories no longer synced to Recently deleted.
3. A message at the bottom of the page reports what was updated.

## Choosing repositories
- Right-click GitHub → **Choose repositories…**, then untick any you do not want. Their notes go to Recently deleted at the next sync.
- New repositories on your account are added when Claude can list them. If it can't in a run, it syncs the ones it already knows about and says so.

## Limits
- Public repositories are read without signing in, so their pull requests can't be shown.
- Repository notes have no tags: they appear under GitHub, not in Untagged, Most recent or the folders. In the graph they hang from a GitHub node.
- Only My notes is yours to edit; everything above it is replaced at the next sync.

See also [[Claude Notes basics]] and [[Importing notes into Claude Notes]].
