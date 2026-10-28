# Teaching lens: snowy-mail-route (grade 1, robot family)

Round 1, 2026-10-28. Cold read of spec.md, src.html, notes.md, voice/lines.json, art (none: drawn in code), against
REFINE.md (Teaching lens), STANDARDS.md and BASELINE.md. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py
snowy-mail-route` (127 KB). Driven with `scripts/drive.py` (port 9701, own profile), 1366x768 unless named.

Counts: blockers 0, should fix 2 (general 2, family 0), polish 6 (general 4, family 2), nits 3.

## What I recomputed (Python BFS and a walk simulator, then the real page)

- **Snow Town** (Post Office (1,4); banks (2,3) (3,2) (5,3)): shortest steps Fish 3, Star 4, Sun 2, Tree 5, Moon 5,
  Heart 8. Every notes path is a shortest path and delivers in the page (tapping each house addresses the letter,
  `town.delivered` ends with all six).
- **Levels**, page map equals the spec table for all eight (start, house, other houses, banks, starting cards).
  Shortest lengths 3, 5, 6, 6, 7, 7, 8, 8, as listed; each listed path is one of them (count of shortest paths: 1, 10,
  4, 3, 3, 6, 17, 1) and each delivers in the page.
- **Fix-its:** L4 `U U R R D R` bumps the bank (3,3) on card 5 from (3,2); fix (card 5 to R) delivers. L6
  `D D R R R R R U` reaches (6,3) after card 6, card 7 bumps the right edge; removing any of cards 3 to 7 (the Rights)
  delivers, removing a D or the U does not. L7 `R U R U U R R R` bumps the bank (2,3) on card 2 from (2,4); the 2-3
  swap is the only adjacent swap that delivers. Page agrees: `?` badge on card 5, 7 and 2.
- Guess: flag on (3,2) before the L4 bump gives line 24, flag on (3,3) gives line 25 (a bump counts as where Pip
  stopped). Flag places, moves ((2,2) then (4,2)) and removes.

## Standards (rule 2)

The 2026 statements are not in the repo; I used the gap-fill reading (docs/agents/gapfill/cs/notes.md) and the 2017
crosswalk.
- **E1-ALG-PS-01** (create and follow an algorithm for a daily process): taught. The class builds a mail route and
  follows it before running (trace with a finger, Guess flag, checked by line 24/25).
- **E1-PRO-PD-04** (a program as a sequence that does a task): taught. Five build levels and Snow Town; the card
  strip is the sequence, Step shows one card at a time.
- **E1-PRO-TR-07** (find and fix errors): taught. Three fix-it levels (wrong card, extra card, swapped order), each
  verified above, plus the footprint-to-card link.
- **E1-ALG-IM-03** (grade 1: change a step, the result changes): taught by doing (every fix-it is one change that
  turns a bump into a delivery; Mixed Up is the same cards in a new order). It is never said out loud; see polish P4.

## Done when

1. Snow Town: PASS (each house tap addresses; all six notes paths deliver).
2. Levels load the table exactly, each build level delivers with its listed path: PASS.
3. Fix-its bump at card 5, card 7 (edge), card 2, and the fixes deliver: PASS.
4. Footprints numbered; tapping footprint 3 on L4 selects card 3 (`strip.sel = 2`) and pulses its pair: PASS.
5. Guess places, moves, removes; 24/25 right including after a bump: PASS.
6. Step one card (paused, `next` 1), Step again, an edit (add Up) resets Pip to start and clears footprints, Step
   then Go finishes, Stop halts at once (Pip unchanged 1.5 s later): PASS.
7. Keyboard only: L4 fixed with real keys (Tab to Go, Enter; Tab to card 5, Enter; Shift-Tab to Right, Enter; Go):
   delivered. L6 card removed with Delete. G and S work (synthetic keydown; drive.py has no letter keys): PASS.
8. Tray, Go and all 12 strip slots visible, no horizontal scroll at 680x425, 800x500, 1000x625, 1280x720, 1366x768,
   1920x1080, 760x900; 60 px minimum at 1280 and up: PASS (see nit N3 for the preview).
9. Voice, light check only (the Craft lens owns the counts): five held Go taps on L4 spoke line 21 five times, line 3
   once, line 6 once. Line 7 was dropped and never came back: see should fix S2.
10. Motion off (reduce): all eight levels deliver, no console errors in any run: PASS.

## Findings

### Should fix

**S1. Level 3 line says Pip can't walk through snow.** src.html:314 (`lv3`), voice/lines.json, spec line 10:
"Pip can't walk through snow. Find a way around." The whole town is snow, Pip walks on it every step, and line 20 says
"Pip stopped in the snow". A grade 1 class hears a contradiction on the first level about obstacles. Better: "Pip
can't walk through a snowbank. Find a way around." (Seen: read against lines 20 and the L3 frame.) **general**

**S2. Line 7, the tool's main debugging move, can be lost for the whole page load.** src.html:983 queues `hFoot`
(line 7) only on the page's first problem, after the event line; if that how line goes stale (the class presses Go
again or edits a card while line 21 is still being read, a normal classroom moment), it is dropped and never queued
again: the second problem queues line 6, later ones nothing, and `hFoot` is not in `SPEAK_HOW`, so the hint changes
silently. Seen: five held Go taps on L4, 14 s apart: `hFoot` "dropped, stale" at t=17.6 s, never spoken in the run.
K-2 reads nothing, so "Tap a footprint to find the card that made it" may never reach the class. Better: keep line 7
pending until it is actually spoken (queue it again on the next problem if it was dropped), and do the same for line
6. **general**

### Polish

**P1. The `?` badge answers the question the narrator just asked.** src.html:935: on a bump the bumping card gets a
red `?` at once, while line 21/22 asks "Which card sent Pip that way?". On L4 and L7 the badged card is the bug (L6:
one of the extra Rights), so the fix-its are solved by looking at the badge, not by reading the footprints, which is
the tool's stated idea ("the footprint trail is the evidence they read to find the bug themselves", spec Not like).
The badge is in the spec, so this goes to the spec's open questions: e.g. show the snow puff only, and put the `?` on
the card after the class taps the last footprint (or after Step reaches it). Frames: out/l4bump.png, l7bump.png,
l6bump.png. **family:robot**

**P2. After a bump the hint points at footprints the bad card never made.** src.html:1085: the hint after a bump is
"Tap a footprint to find the card that made it." The bumping card leaves a snow puff, not footprints, so the trail
ends one card before the bug. Notes' talk question gets it right ("Which footprint is the last one? Which card comes
right after it?"). Better hint after a bump: "Tap the last footprint. The card after it bumped." **family:robot**

**P3. The words bug and debugging are never heard.** notes.md:46 says "Words used: algorithm, program, bug,
debugging", but no line or on-screen text uses any of them; only the teacher's talk questions do. For TR-07 the word is
part of the idea at this grade (Code.org glossary, the spec's source). Better: the fix-it level lines name it, e.g.
L4 "One card is wrong. A mistake in the cards is called a bug." and the delivery after a fix-it "You fixed the bug!"
**general**

**P4. IM-03 is done but never named.** The class changes one card and Pip's whole route changes, but nothing asks
them to notice that. Add a talk question to notes.md (and optionally the delivery line after a fix-it): "We changed one
card. What changed for Pip?" **general**

**P5. Level 8 says "Go slowly"; Go is a button that walks every card.** src.html:319: "Go slowly, one arrow at a
time." A grade 1 class hears "Go" as the yellow button. Better: "Press Step to walk one arrow at a time." **general**

**P6. Stopping on the Post Office is called "in the snow".** src.html:324 and the outcome code: Snow Town `U D`
ends on the Post Office square and line 20 plays, "Pip stopped in the snow. Is there a card missing?" (seen in the
town run). Words don't match the picture. Better: a Post Office case ("Pip came back to the Post Office!") or treat
it as snow without the missing-card guess. **general**

### Nits

**N1.** notes.md:18: "Pip walks off the edge at card 7". Pip bumps the edge and slides back; say "bumps the edge of
town at card 7". **general**

**N2.** src.html:334 `hFix` "find the card that is wrong" stays on L6 (an extra card) and L7 (two swapped cards); the
level lines are right, the hint is generic. Optional per-level hint. **general**

**N3.** At 680x425 (site preview) Start over and Next are 29 px wide (frame out/sz680x425.png). Full screen is 60
px, so Done when 8 passes; noting it for the Craft and Play lenses. **general**

## Guardrails and flags

- K-2 teacher-led: driver "teacher", every fixed line spoken, icons on every control. No points, timers or score;
  delivery is a win state, which is fine here (not hard history). No health content.
- Nothing gives the stop square away before Go in Guess mode (no ghost path; the strip carries no marks before a run).
  The only give-away is P1, after the run.
- Sensitivity (rule 5): nothing cultural, Native or hard-history (a penguin, snow, houses with symbol addresses). No
  sensitivity review needed. Rule 8: no sensitive topics in these standards.

Frames and data: C:\Users\Cory\AppData\Local\Temp\claude\S--\98b8b046-f7f2-48d0-a719-c61ce01237be\scratchpad\lens-smr-teaching\out
(default, l4start, l4bump, l6bump, l7bump, l8open, sz680x425 to sz1920x1080, sz760x900, kbfix2, motionoff, voice5) and
levels.json, town.json, guess.json, step.json; sim.py is the BFS and walk simulator.
