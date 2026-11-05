# Codex review brief, any tool (Curio Class)

You are a fresh, cold reviewer of ONE Curio Class tool that another Codex chat just built. You did not build it and you
owe it nothing. After you finish, three blind Claude lenses check the same tool, and every finding they raise costs far
more to fix than the same finding fixed now. Your job is to find what they would find, fix it, and leave them little to do.

The tool id is in the prompt that sent you here, and `<id>` below means that id. The repo root is `S:\CurioClass-codex`,
shared with other chats. Run every command from there. Scratch means `_scratch/<id>` in it.

## Rules

Every rule in `docs/agents/CODEX-BUILD.md` holds here: Ground rules, Do not hang (a time limit on every command), Images
and the people rule. Read that brief first. In short: write only inside `tools/<id>/` and Scratch, no git commits, use only
the ports your prompt names, and keep the tool folder tidy.

- Keep what is strong. You are here to fix faults and lift weak spots, not to restyle the tool or strip it down. Do not
  make the graphics or the play plainer to clear a check.
- Add no features or topics beyond the spec.
- One pass. Look once, fix once, re-check what you fixed. Do not start a second full review or a polish round.

## 1. Look, before you read what the builder said

Read `docs/agents/STANDARDS.md`, `docs/agents/decisions/BASELINE.md`, `tools/<id>/spec.md`, `docs/POLISH.md`, then in
`docs/agents/REFINE.md` the three lenses (Teaching, Play, Craft) and how a lens reports, and in `docs/agents/BUILD.md`
the wave lessons. Then bundle (`$env:CURIO_DRAFT=1; python scripts/bundle_tool.py <id>`) and play the whole tool once as
a student of that grade, using `scripts/drive.py` as CODEX-BUILD.md shows.

Only then read `codex-report.md`, `handoff.md`, `notes.md` and `src.html`.

## 2. Find

Walk all three lenses, as written in REFINE.md, plus these. Open the frames and look at them.

- **The repeat findings.** Check every BUILD.md wave lesson yourself. Do not trust a PASS in the report.
- **Teaching.** Recompute the spec's numbers. Check that a wrong path teaches, nothing gives the answer away, and the
  notes open with `## What it teaches`, `## Key skills` and `## Support at home`.
- **Play.** Hold it to the Gameplay list in CODEX-BUILD.md. Name the flattest moment.
- **Graphics.** Look at every image at its final size, and hold the scenes to the Graphics list in CODEX-BUILD.md. Is the
  set one style? Is any picture untrue to what the tool teaches? Is a person missing where the scene needs one (a classroom, a job, a family), or drawn with a stereotype? Is every people image marked `"people": true`? Is any image in
  `art:<name>` still missing that could be made?
- **Craft.** Every STANDARDS size, Motion off, grayscale, keyboard only, the voice checks, every extreme in POLISH.md.

- **Break it.** For every score, meter, check, quiz, reflection gate or "you got it" moment, write down the cheapest way
  to pass without the skill (a tap rhythm with pauses, sweeping a slider end to end, every option in turn, reading a
  percent or a badge, three easy inputs where the check wants three hard ones, guessing by elimination) and actually run
  it with drive.py. A cheat that passes is a blocker. So is a meter that rewards the wrong thing, a "best score" a cheat
  can set, or a reflection question that assumes a mistake the student never made. Do this on the paths students take,
  not only on the steady, correct path.
- **The main path, in the voice.** Follow the welcome's own instructions in order, as a student would (if it says turn
  the power on first, do that first), with held clicks at a 2 s pace and the default settings, then read `__tool.vlog`.
  Every mode's how-to line must be heard on that path, once, when it fits; nothing said while the screen says something
  else. Testing voice only on side paths missed whole modes before.
- **Facts against named guidance.** Health, safety, first aid, law, money and science facts are checked against the
  current guidance of a named body (for example the American Red Cross or American Heart Association for first aid, the
  CDC or NIH for health). History, music and culture facts are checked for dates, credits and who is named, and against
  the spec's Sources. In the report, write the source beside each fact you checked. A fact that disagrees with current
  guidance is a blocker in a health or safety tool and a should fix elsewhere.
- **Sensitivity.** If the tool touches a culture other than the student's own, Native or Indigenous peoples, religion,
  hard history, or people's bodies, flag it in the report under `## Sensitivity` with what a cultural reviewer should
  look at (a date that frames a tradition by when Europeans heard it, a credit that leaves out who made it, an image that
  stands in for a whole people). A Claude sensitivity reviewer reads that section before Refine. Fix what is plainly
  wrong; leave judgment calls for that reviewer, named.

Rank each finding as REFINE.md does: blocker, should fix, polish or nit.

## 3. Fix

Fix every blocker and should fix, in `src.html`, `notes.md`, `voice/lines.json`, `audit-states.json`, `handoff.md` and
the art. Make images that are missing and redraw poor ones as the Images section says. Fix a polish item when it takes a
few minutes. Leave nits.

If you disagree with the spec, or a fix would need a new feature or a kit change, do not make it. Write it under Left open.

## 4. Check

Re-shoot only what your fixes touched, at every size the finding was seen at: a phone finding is not fixed by a 1366
frame, and a fix that looked right at one size has failed at another before. Re-run each cheat from Break it after your
fix, and the main-path voice walk if you changed voice or the order of steps. Then run the audit once, last, with the same 40 minute limit:
`python scripts/audit_tool.py <id> <Scratch>/review-audit --port <your second port> --profile <Scratch>/chrome-prof-review`.
Fix what it confirms, re-shoot those frames, and stop. If the audit does not finish, its partial `audit.md` still holds every lead it found: fix those, say it did not finish, and stop.

## Report: `tools/<id>/codex-review.md`

Under 130 lines. Write it as you go, so it survives a stuck command.

```
# Codex review: <id>
## Played                (what you did, as what grade, one line on how it felt)
## Findings fixed        (level, where, what was wrong, what you changed)
## Findings left         (level, where, why it stays)
## Break it              (each score, check or meter: the cheats tried and what happened after your fixes)
## Voice walk            (the main path you followed and the lines heard, in order)
## Facts checked         (each fact and the source you held it to)
## Sensitivity           (what a cultural reviewer should look at, or "none: why")
## Flattest moment left
## Graphics              (images checked, redrawn, added; bundle KB)
## Audit                 (leads fixed, or "audit not finished")
## Left open
```

Be honest: a finding you leave and name is worth more than one you hide. When the report is written, say "Review done"
and stop.
