# The Review Desk page

desk.html is the page source of the Review Desk, the private claude.ai artifact where Cory answers question cards
and reads the plan flow (https://claude.ai/artifact/SVXBzgyS941dyqmEzQHgNC). It moved here from drafts/desk/ on
2026-11-24 (consolidation step 1). The Desk's data lives in the artifact's own database, not in this folder.

## What the Dashboard shows

Top to bottom (rebuilt 2026-11-25): "Curio Class, built so far" (a ring for every piece done, a ladder of the layers
from progressions to tools live, for the 52 core courses or every course, and a pace strip of files added per day);
"Every course, top to bottom" (one row per course, opened down to units, sections and days); "Health of the build"
(the 12 goal tests, known misses, Saved for later, debt, kit version, open questions); then "Stage by stage" (the
seven-stage flow), Saved for later and the tool counts. All of it reads the stats/plan parts from plan_flow.py:
course keys, section splits (secs), health and history are in that export.

## Refreshing and publishing

1. Stats: `python -X utf8 scripts/plan_flow.py <out>.json` (writes `<out>.json.parts/plan-c0..c4.json`) and
   `python -X utf8 scripts/course_status.py <out>.json`; write them to the artifact's `stats` collection in one
   ArtifactData batch (`op: "set"`, with `if_version`).
2. Snapshot for viewers who are not signed in: list the artifact's `items` and `stats` collections into a scratch
   folder, then `python -X utf8 scripts/desk_snap.py <snap dir> <publish dir>`.
3. Publish: copy desk.html into the publish dir and publish it to the same artifact URL with
   `files: {"snap.json": ...}`.

snap.json is never committed (the repository is public and it copies the Desk's cards); it is git-ignored and rebuilt
on every refresh.
