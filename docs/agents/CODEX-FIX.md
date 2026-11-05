# Codex fix brief, any tool (Curio Class)

You are fixing ONE Curio Class tool after its Claude Refine. Three cold Claude lenses (Teaching, Play, Craft), and a
sensitivity reviewer where the topic needed one, played the tool and merged what they found into
`tools/<id>/refine.md`. Your job is to fix what that list asks for, prove each fix, and say plainly what you did not fix.
A fresh Claude exit check reads your work next and re-tests every item itself, so a fix you claim but did not make
costs a whole extra round.

The tool id is in the prompt that sent you here, and `<id>` below means that id. The repo root is `S:\CurioClass-codex`,
shared with other chats. Run every command from there. Scratch means `_scratch/<id>` in it.

## Rules

Every rule in `docs/agents/CODEX-BUILD.md` holds here: Ground rules, Do not hang (a time limit on every command), Images
and the people rule. Read that brief first. In short: write only inside `tools/<id>/` and Scratch, no git commits, use only
the ports your prompt names, keep the tool folder tidy, never an em dash, write "Curio Class", never "Curio" alone.

- `refine.md` is the list. Do not edit it, and do not edit anything in `tools/<id>/refine/`.
- Fix the cause, not the symptom the reviewer happened to see. If a reviewer found a cheat with one pattern of taps, close
  every pattern that cheats the same way, then try two more of your own.
- Keep what is strong. Do not make the graphics or the play plainer to clear an item.
- Add no features or topics beyond the spec. An item under "To the spec's open questions" is not for you: leave it.
- Facts: when an item says a fact is wrong, fix it to the current guidance the item names, or to a source you name in
  `polish.md`. Never trade one unsourced claim for another.
- One pass. Fix, re-check what you fixed, write the report, stop. Do not run the three lenses again.

## 1. Read

1. `tools/<id>/refine.md`, all of it: the verdict, Blocker, Should fix, Polish accepted, Settled calls.
2. `tools/<id>/refine/sensitivity.md` if it exists. A FAIL there is a blocker list of its own, already merged into
   refine.md; read the reviewer's reasoning so your words fix the meaning, not just the sentence.
3. `docs/agents/STANDARDS.md`, `tools/<id>/spec.md`, `docs/POLISH.md`, and in `docs/agents/REFINE.md` the Exit check gate,
   which is what the next reader holds you to.
4. Then `src.html`, `notes.md`, `voice/lines.json`, `audit-states.json`, `handoff.md`.

Older Refine files (`refine-<date>.md`, `refine-<date>/`), `codex-report.md` and `codex-review.md` are history. Do not
treat them as the list.

## 2. Reproduce, then fix

For each blocker and should fix, in that order:

1. Reproduce it first with `scripts/drive.py`, at the size and in the state the item names. Keep the frame in Scratch.
   If you cannot reproduce it, say so in `polish.md` with what you tried. Do not mark it fixed.
2. Fix it in `src.html`, `notes.md`, `voice/lines.json`, `audit-states.json`, `handoff.md` or the art.
3. Re-shoot the same steps at the same size and look at the frame. A fix is done when the before and after frames, or
   the before and after numbers, show it.

Then every item under Polish accepted, the same way but without the before frame. Apply the Settled calls. Leave Nits
unless one takes a minute and touches what you already changed.

**Scores, meters and checks.** Where an item is about a score, a check, a meter or a quiz, after the fix write the
cheapest way you can think of to pass without the skill (tap pattern, sweep a slider, read a badge, guess by elimination)
and run it. Write each attempt and its result in `polish.md`. A cheat that still passes means the item is not fixed.

**Voice.** Where an item touches voice, walk the tool in the order the welcome tells a student, with held clicks at a 2 s
pace, then read `__tool.vlog`: every line the item names must be heard, once, at the moment it fits. Keep
`voice/lines.json` equal to `allLines()`.

**Sizes.** Re-shoot every fix at each size its item names. An item that names a phone or 680x425 is not fixed by a
1366 frame.

If a fix needs a kit engine change, do not make it: write the exact change under Engine changes wanted in `handoff.md`
and name it in `polish.md`.

## 3. Check

Bundle (`$env:CURIO_DRAFT=1; python scripts/bundle_tool.py <id>`): clean, no console errors, no network requests. Re-shoot
the default screen and every mode once at 1366x768 to catch regressions. Then run the audit once, last, with a 40 minute
limit: `python scripts/audit_tool.py <id> <Scratch>/fix-audit --port <your second port> --profile <Scratch>/chrome-prof-fix`.
Answer each new lead in the report. If it does not finish, say so and stop.

## Report: `tools/<id>/polish.md`

One line per item from refine.md, in its order, then the rest. Write it as you go, so it survives a stuck command.

```
# Polish: <id> (Codex fix, round <n>)
## Blocker              (each: FIXED or NOT FIXED, what changed, the frame or numbers that prove it)
## Should fix           (same)
## Polish accepted      (same)
## Settled calls        (applied, or why not)
## Cheats tried         (each attempt and what happened)
## Voice walk           (lines heard, in order)
## Engine changes wanted
## Audit                (new leads and what you did, or "audit not finished")
## Left open
```

Be honest. An item marked NOT FIXED with a reason is cheap for the exit check; an item marked FIXED that is not costs a
round. When `polish.md` is written, say "Fix done" and stop.

## For the integrator (Claude)

- **Hand over:** the tool's merged list (`refine.md`, plus `refine/` for the lens files) must be in the Codex checkout.
  Merge main into codex/queue after committing it (`git -C S:/CurioClass-codex merge origin/main`). The runner starts a
  fix for every tool whose `refine.md` first line starts with `OPEN` or `ROUND 2` and that has no `polish.md`.
- **Round 2:** rename the round 1 report to `polish-r1.md` before handing back, so the runner sees the tool as wanting a
  fix again. The exit check's open items go into refine.md as REFINE.md says.
- **Pull back:** `git checkout codex/queue -- tools/<id>` in main after the codex/queue commit, plus any art/raw the fix
  made (raw art is not committed on codex/queue either; copy it by hand), then bundle, run the checks and the Claude exit
  check.
