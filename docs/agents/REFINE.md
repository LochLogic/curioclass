# Refine brief

Refine takes ONE Curio Class tool from a first solid draft (Build) to something ready for Cory's review. It has
three parts: **look** (three cold lens agents), **polish** (the build agent fixes), **exit check** (one cold agent
confirms the gate). Read `docs/agents/STANDARDS.md` and `docs/agents/decisions/BASELINE.md` first; they win over
this brief.

## Look: three lenses, run at once

Each lens agent is fresh and cold: you did not build the tool and you owe it nothing. Do not fix anything. Each lens
reads `tools/<id>/spec.md`, then `src.html`, `notes.md`, `art/prompts.json` and `voice/lines.json`, bundles with
`CURIO_DRAFT=1 python scripts/bundle_tool.py <id>`, and works in its own scratch folder with its own Chrome profile
and port (RUNBOOK, Agent Chrome hygiene). Write `tools/<id>/refine/<lens>.md` only.

**Audit first (pilot, Cory 2026-10-28; tuned after BR2).** Before looking, each lens runs
`python scripts/audit_tool.py <id> <scratch>/audit --port <your first port> --profile <absolute dir>` (it uses that
port and the next one; about 15 minutes; add `--no-walk` for the sizes and states only). It checks every size's first
screen (targets, fold, overlaps, clipped text, the hint, focus on load, console errors), the same at every size after
each mode button and each state in the builder's `audit-states.json`, Motion off, one held click per control at
1366x768 (with focus once things settle and Enter twice after), five clicks 2 s apart and two quick taps on the
controls that speak. Boxes are clipped by their stage and scroll panels first, so what those hide is no longer a lead.
BR2 showed its clean rows hold (sizes, Motion off, focus on load, console errors, the voice repeats): a lens may cite
them instead of re-shooting. It adds to the lens and replaces nothing else: do your full lens as written. It can't see
teaching, giveaways, feel, art, whether a line or hint is the right one, or states nobody listed. At the end of your
lens file add `## Audit pilot`: the leads you confirmed, the leads that were wrong, and what you found that it missed.

**Teaching lens: does it teach what it claims, to this grade?**
1. Every standard code on the tool's module is really taught by something the student does (BASELINE rule 2). A
   code that is only mentioned is a finding: name the activity that would teach it, or say the code should move.
2. Every "Done when" in the spec, tested.
3. Facts: every number, date and claim on screen or in notes matches the spec's Sources. Recompute numbers yourself.
4. Nothing gives an answer away in a predict, quiz or hidden-information mode (POLISH, Games and quizzes).
5. Language is plain and right for the grade; teacher notes name sensitive topics the standards cover (rule 8).
6. Guardrails: K-2 teacher-led; hard history has no points, timers or win states; health topics neutral.
7. Flag anything cultural, Native or hard-history for the sensitivity agent (rule 5). Don't judge it yourself.

**Play lens: what is it like to use?** Play it twice: once as a student of that grade alone at home with no teacher
(rule 4), once as a teacher projecting it to a class.
1. Frames (`scripts/shoot.py` or `scripts/drive.py`) of the default screen, every mode, the extremes (smallest and
   largest values, empty states, the end of a round), a narrow window and 1366x768. Look at every frame: overlaps,
   clipping, text over art, unreadable sizes, placeholder art in odd spots.
2. The defaults work for a solo student: the first screen says what to do, every waiting moment names the next
   action and the control (spoken once, then hint only).
3. POLISH.md, all of it: pacing for reading aloud, calm mode keeps time, anything shown twice matches, words match
   the state.
4. Feel: where did you get bored, lost or unsure? Where is a moment flat that could land? These are polish items.

**Craft lens: is it built right?**
1. Contract: one file, no network requests, under 2 MB, kit used (not re-implemented), no console errors.
2. Access: keyboard, visible focus, 44 px targets (60 px for K-2), color never the only signal; Motion, Sound and
   Read work.
3. Lines: every spoken line is in `voice/lines.json` and `allLines()`, word for word; each line matches the state.
4. Voice balance: the standard voice check below, with its counts table. Check every spoken line against what the
   screen shows then.
5. Art: every `art:` token has a prompts.json entry; people are marked `people: true`; local models never draw people.
6. Words: no em dashes, "Curio Class" never "Curio" alone, classroom-safe language (rule 6), privacy stated where
   anything is stored (rule 7).

**Sensitivity agent (only when rule 5 applies):** a fresh agent checks accuracy and respect for the cultural,
Native or hard-history content and writes `refine/sensitivity.md`. Its PASS is part of the gate.

**Every lens reports the same way:** each finding as where (file:line or mode), what, how you saw it (the frame or
the check), and a level:
- **blocker**: wrong, broken or unsafe; cannot go to Cory;
- **should fix**: a real flaw a teacher or student would notice;
- **polish**: not wrong, but a clear step up (a flat moment, a confusing word, a tighter layout). Say what better
  looks like;
- **nit**: small and optional.

Tag each finding **general** (any tool could have it) or **family:<name>** (it comes from this tool's engine or
format). The tags decide where the lesson is written down after the wave (RUNBOOK, Wave cadence).
Don't pad a short list. A lens with nothing to say writes "Nothing found" and the frames it looked at.

## Standard voice check

Drive it with `scripts/drive.py` and held clicks (`"hold": 0.12`, a `"gap"` longer than the lines), Sound on, Motion on.
Read the log after each run: `__tool.vlog` (on `Curio.voice` it is `V.log`, with `as` = spoken, silent, dropped or read).

1. **Repeats:** each action five times in a row. Count how often each line is spoken. How-to and teaching lines: once,
   then `silent` (the hint still shows them). Event lines (praise, results, failures, "that code doesn't work"): five.
   A result that goes quiet after the first time fails, and so does a how-to that comes back after every tap.
2. **Stale lines:** tap fast (gap about 0.2 s) through two or three actions, then switch mode and Reset. No line may
   play after its moment has passed: compare each spoken line with the frame at its time. A line naming a control that
   is hidden or off must not play.
3. **First-tap timing:** one fresh page per kind of first tap: the stage, a control that speaks for itself, a mode
   button, Read, Sound, a key. Nothing speaks before the tap. A plain tap gets the welcome within about half a second; a
   control with its own line gets only that line; Read speaks the hint only; Sound says nothing. Then Sound off and on,
   or the next mode entry, must bring a skipped welcome, once.
4. **Read:** Read during a line stops it and speaks the hint, with Sound off too; nothing cuts Read off; a mode change
   right after Read lets the next line start at once.
5. **Order:** spoken lines follow the order of the actions; no line from an older action plays after a newer one.

Report the counts as a small table (line, kind, expected, spoken). On `Curio.voice`, the helper's own rules are covered
by `python scripts/test_voice.py`; the tool's job is choosing the right kind, `valid` and `needs` for each line.

## Merge (the integrator)

Read the three lens files. Merge duplicates, settle any lens disagreement with BASELINE, and write
`tools/<id>/refine.md`: one ranked list (blockers, should fix, then the polish items you accept). Accept a polish
item when it improves what the student sees or hears and stays inside the spec. A polish item that would change the
spec (what the tool teaches, a new mode) goes to the spec's open questions, not to the builder. Keep each finding's
tag. Under the verdict line, write a counts line for round 1: `Counts: blockers N (general N, family N), should fix N
(general N, family N), polish accepted N`. The batch log's wave table is built from these lines.

## Polish (the same build agent)

SendMessage the merged list to the build agent that built the tool, blockers first. It fixes every blocker and
should-fix and the accepted polish items, re-shoots its own frames, and reports what it changed.

## Exit check (one fresh cold agent)

Re-check each item on the merged list yourself and look for regressions (re-shoot the default screen, every mode
and the frames tied to each fix). Then check the gate. **All must hold:**
1. every "Done when" passes;
2. every code on the module is taught, or its move is written down (rule 2);
3. the defaults work for a solo student (rule 4);
4. the sensitivity agent passed, where rule 5 applies;
5. no blocker or should-fix is open;
6. the bundle is clean, under 2 MB, no console errors, no network requests;
7. the voice check counts are right.
Write the verdict as the first line of `refine.md`, `PASS` or `ROUND 2` with the open items, and append the
check below the merged list.

## Rounds

At most two rounds (look, polish, exit check). Round 2 runs only the lenses that had open items. A round 2 exit
check re-checks the open items plus a short no-regression look at the frames and voice they touch, not the whole
tool again (BR1, 2026-10-28: a scoped re-check cost about 100k tokens against 150k or more for a full one). When
one or two narrow items are left, the integrator may fix them and send the same exit agent back to re-check.

Lenses also check the BUILD.md wave lessons: any lesson missed is at least a should-fix. Teaching and Play both
try to solve each puzzle the cheap way: sweep every slider, try every option, read the badges, flag names and
option lengths. A meter or estimate that misleads when its assumption doesn't hold is a blocker. If round 2 still
fails the gate, the tool does not go on: the integrator either fixes one narrow item itself (with an "Integrator
fix" note, as today) or brings it to Cory with the open list. Polish items left over never block; they go in the
Review Desk "changed" note as "known, not done".

## Final look (after art and voice, before the plan) (Cory, 2026-10-27)

Refine runs on placeholder art and the browser voice. Real pictures and recorded clips can break what passed: text
over a busy picture, a bad crop, a style that misses the spec, a clip longer than the browser read so a line runs into
the next moment or gets cut. Final look checks the finished tool as a student and a teacher will meet it. It is not
light: it is the last check before Cory sees the tool.

**Look (one fresh cold agent, plus the sensitivity agent again when rule 5 applies or any picture shows people).**
Read refine.md and handoff.md first, so you know what was already settled; then check the tool with real assets:
1. **Frames, all of them again:** the default screen, every mode, the extremes, the end of a round, a narrow window
   and 1366x768, Motion on and off. Look at every frame for text over art, cropping, art at the wrong size or
   resolution, placeholders left anywhere, contrast of words on pictures (AA).
2. **Art against the spec:** every `art:` token shows its .webp; each picture matches its spec entry and the tool's
   look (palette, style, one artist feel across the set); facts in pictures are right for the subject (era, objects,
   counts, labels); no garbled lettering; people pictures have a varied cast and Cory's review where required.
3. **Voice with the real clips:** the full standard voice check (above) again with the recorded clips, plus timing:
   no clip runs past its moment or into the next line, nothing is cut off, waiting lines leave room for the action,
   K-2 every fixed line has its clip. Every clip says exactly its line (listen through the log: each played clip's
   text matches `voice/lines.json`); flag a take that sounds wrong for the moment from the liveliness reading.
4. **A full run as a solo student and as a teacher projecting it** (the Play lens, step 2 and 4), start to finish.
   Where does the finished tool feel flat, slow or confusing now that it looks and sounds real?
5. **Contract again:** bundle under 2 MB with the art and clips in, no console errors, no network requests.
Write `tools/<id>/final.md`: findings with the same levels and tags as the lenses, frames named.

**Fix (a fresh fix agent, or the builder if it is still around).** It reads handoff.md, refine.md and final.md and
fixes every blocker and should-fix and the accepted polish items. A picture that misses goes back to art (redraw with
a better prompt, never a weaker route); a bad take goes back to voice (`localvoice.py --redo`).

**Re-check (the same Final look agent, by message).** Re-shoot the frames tied to each fix, re-run the voice check if
any clip or line changed, and write `PASS` or `ROUND 2` as final.md's first line. At most two rounds, as above. The
plan agent and the Review Desk come only after a Final look PASS.
