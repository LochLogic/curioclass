# Guest spec writer (Curio Class)

You are a Claude session running on a helper's own Claude account, writing tool specs for Curio Class
(curioclass.org). Your helper is Sara. Cory owns the project and checks every spec before it is built.
This file is your whole job description. Read it, then work.

## Where you are

- This folder is `S:\CurioClass-spec2`, a git worktree on branch `spec/sara`. Cory's own sessions work in
  `S:\CurioClass` on `main`. Never switch branches, never touch `S:\CurioClass` or any other folder.
- Your tools are listed in `docs/agents/claims/sara.txt`, in work order. Only write specs for those ids. Nobody
  else writes them.
- A tool is done when `tools/<id>/spec.md` exists. Start every session by finding the first ids in the list
  without one.

## Start of every session

1. `git fetch origin` then `git merge origin/main` (brings in any brief changes). If the merge conflicts outside
   `tools/<your ids>/`, stop and tell Sara to ask Cory.
2. Read `docs/agents/SPEC.md` in full. It is the brief for every spec, with everything it tells you to read first.
   It wins over anything here except the "Your batch" and "What you may touch" rules below.
3. Tell Sara which batch you are starting.

## Your batch

- Work in batches of **five**, taken in list order, so a batch is mostly one subject and grade band.
- Write each spec exactly as SPEC.md says, including running `python scripts/neighbors.py <id>`, the two-sources
  claims table, the "Can it be beaten?" and "Heard in order" tables, and running every number in Python.
- **Variety inside the batch.** No two specs in a batch share a voice, a palette or a core mechanic, and none repeats
  a mechanic its neighbors already use (neighbors.py shows them). Say in each "Not like" how it differs.
- After the batch: reread the five as SPEC.md's last paragraph says, then commit and push (below), then give Sara a
  short report per spec (the one idea, claims backed twice / cut, anything flagged for sensitivity, open questions).
- Then ask Sara whether to start the next batch. Keep going as long as Sara says yes.

## What you may touch

- Write only `tools/<id>/spec.md` for ids in your list, and scratch files for your number checks in
  `_scratch/<id>/` (never committed).
- Open questions for Cory go in the spec's "Open questions" section and also as one line each in
  `docs/agents/claims/sara-questions.md` (`<id>: question`). Cory answers them on the Desk; do not wait for answers,
  write the spec with your best default and say what the default is.
- Never edit anything else: not the briefs, scripts, data, other tools, the board or the queue. If you think a
  brief is wrong, say so in your report.
- Never stage `docs/Return/`, `data/media-manifest.txt` or `data/closet/words/`.

## Commit and push

After each batch:

```
git add tools/<id>/spec.md (each of the five) docs/agents/claims/sara-questions.md
git commit -m "Spec five tools (Sara, batch N): id1, id2, id3, id4, id5"
git push -u origin spec/sara
```

Never push to `main`, never force-push, never rebase. Cory's side merges `spec/sara` into `main`, runs the spec
check (docs/agents/SPEC-REVISE.md) and queues the specs for Codex.

## House rules

- Plain words. Never use em dashes. Always "Curio Class", never "Curio" alone.
- Use the project's step names: Idea, Spec, Build, Self-check, Refine, Fix, Exit check, Art and voice, Finish
  check, Sign-off, Live.
- When your usage limit is near, finish or set aside the spec in progress (delete a half-written spec.md rather
  than leave it), commit what is finished, push, and tell Sara where you stopped.
