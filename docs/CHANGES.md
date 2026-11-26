# Changing the curriculum

One page, for any change that reaches past one day (consolidation 4.H, 2026-11-25). A day rewritten inside its
own job follows its brief instead.

1. **Request.** Every change starts from one place: a consolidation step, a row of data/plans/later.csv, or a Desk
   answer. Name it in the change's log line.
2. **Impact.** `python -X utf8 scripts/uses.py <id>` lists everything that uses the id, by course and day, hard uses
   and soft mentions in prose apart. `--changed` lists what your uncommitted files reach.
3. **A script, with a dry run.** A change to more than a handful of rows or files is a script that prints what it
   would change (`--dry-run`) and a diff summary before it writes. CSV rows go through
   `python -X utf8 scripts/rows.py upsert` (or `ledger.py` for ledgers), never by hand.
4. **Ids.** A revised item keeps its id (its version goes in the `version` column); a retired or merged id is recorded
   with `python -X utf8 scripts/ids.py retire <old_id> [<new_id>] --reason "..."` and never reused; day numbers are
   permanent once a course's scope and sequence is signed off (data/plans/README.md).
5. **Homes.** data/homes.csv says where each kind of file lives, who writes it and what is never touched;
   `python -X utf8 scripts/homes.py kind <path>` answers for one path.
6. **Gate.** `python -X utf8 scripts/gate.py --course <course>` before you start (an unchanged course stores its own baseline) and after; for a change across
   many courses, `gate.py --all --site --save <name>` before and after, then `gate.py compare`.
7. **Log line.** One line in the place the request came from: the step's Built note, the later.csv row's detail, or
   the Desk decision log.

Reports a change writes go to docs/reviews/<course>/ when they belong to one course, and to the top of docs/reviews/
when they span courses. When a course is signed off, its per-job reports are zipped to the archive with one summary
left behind.

Errata for taught courses wait until a course is taught.
