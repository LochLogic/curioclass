# Batch log: Computer Science, first five (2026-10-26)

Batch note: `docs/agents/BATCH-CS.md`.

## Specs (all five written 2026-10-26)

| Tool | One idea | Accent | Voice | Art |
|---|---|---|---|---|
| robot-dance | Bolt dances the cards beside Dot; trips on the first step that differs; the class fixes the bug | magenta #b0206a on navy stage | lively-host | none (code) |
| computer-builder | each part gives the computer one power; leave it off and see what it can't do | cobalt #2049b8 on wood desk | bright-teacher | 6 (backdrop FLUX.2; goldfish, mouse, panda via Codex) |
| score-keeper | Star Catch runs beside its program; variables are labeled boxes that change live | raspberry #a82755 on indigo night | friendly-dad | 3 (desert backdrop FLUX.2; ship, rock via Codex) |
| code-tracer | guess each value in a trace table before the line runs | pencil orange #a8461a on graph paper | clear-teacher | none (code) |
| game-remix | remix a kid-made game, see what changed, credit the original | deep teal #0b6b6f | big-sister | 13 (3 backdrops FLUX.2; 10 sticker sprites via Codex) |

Spec check: no shared idea, accent, voice or image across the five; score-keeper keeps the space theme, game-remix
is park, pumpkins and snow.

## Decisions on open questions (integrator, 2026-10-26)

- Standards: every spec lists the module's CSTA 2026 ids plus a 2017 crosswalk. The 2026 wording is not in the repo
  (only ids), so the crosswalk is inferred by topic; check against the official 2026 PDF when it is at hand.
- Code.org glossary wording was quoted from memory in three specs: the verify agents check it.
- robot-dance: Teams on by default (toggle for whole-class play).
- computer-builder: account safety (E1-SYS-SE-12) left out to keep one idea (secret-keeper covers privacy);
  microphone and camera stay pretend (no permission prompts, nothing records children).
- code-tracer: Trace opens first; quiet first-try tally, no stars; progress not saved.
- game-remix: typed title and remixer name kept as specced (limited characters, nickname default, "first name or a
  nickname" note); print card names the tool only; no QR code for now.

## Progress

- robot-dance: built; verify PASS WITH FIXES (4 should-fix, 10 nice); fix round 1; re-verify PASS WITH FIXES (1 small); fix round 2; re-verify 2 PASS WITH FIXES (one phone edge: ran out at step 5 hid the "?" cell), fixed by the integrator (second strip row stays while the step or bug is in it) and checked. Line 25 now follows 24 only; spec updated. Plan passes check_plans. Live 2026-10-26.
  - Follow-up: no round picker and nothing saved, so a class stopping at round 5 replays 1-5 to reach 7 and 8 (plan puts 7 and 8 in the stretch). A 60 px round chooser is a layout change at every tier; left for a later pass.
  - 2026-10-26, after Cory's review: Fix-It trips now always end on a how-to line for that kind of bug (pick the wrong card and a move, arrows for order, add a missing move, trash the extra card), shown as the hint too; picking a card after a trip says what the buttons do (once per round). Three new lines (43-45), voiced. Checked on rounds 1, 5 and 8.
- score-keeper: built; verify PASS WITH FIXES (1 must, 7 should); fix round 1; art and voice recorded; re-verify PASS WITH FIXES: all original items hold, no regressions; new N1 (say-how-to-act gaps at Play start, game over, Lab idle, result card, Notebook), N2 (zero-runs Notebook copy), N3 (praise line on wrong sorts), N4 ("1 drops"), nits N5-N6. Fix round 2 sent to the builder 2026-10-26.
  - Fix round 2 done: N1-N6 fixed (5 new how-to lines over1, result1, nb0, fix1, fix2; 13 changed), checked at 5 sizes. fix2 path not driven by the builder. Voice re-recorded; plan agent started.
- game-remix: built 2026-10-26 (draft art stand-ins, 35 lines unrecorded, 20 spec deviations listed in the build report); cold verify started.
  - Plan passes check_plans (explore-first, E3-PRO-VD-06). Plan agent findings fixed by the integrator: Next/Prev now reset the Lab dials (questions matched the teacher table only from defaults; also cures "press Run" vs "Run again"), running hints for Play and Lab (2 new voiced lines), log titled Game log in Play. Checked by drive. Live 2026-10-26, Review Desk order 50.
- computer-builder: fix round 2 done (how-to rule via howText/howLater, 3 should-fix, nits 4, 6-8; nit 5 accepted phone fallback); 15 changed + 11 new lines re-recorded; plan agent started.
- game-remix art: Cloudflare allowance still out at 03:13 UTC, so backdrops via Codex too. Picked puppy c21, park c20, pumpkin-patch c20, snowy-hill c21; nine siblings generating with ref puppy.
