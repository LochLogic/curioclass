OPEN (round 1 merged 2026-11-04, polish not started)
Counts: blockers 0 (general 0, family 0), should fix 6 (general 4, family 2), polish accepted 11

# Refine: levels-and-pathways (round 2026-11-04, after the Codex rework)

The 2026-10-28 Refine is kept in refine-2026-10-28.md and refine-2026-10-28/ (it ran before Codex reworked the tool).
Lenses: refine/teaching.md, refine/play.md, refine/craft.md. Shared audit: 13 leads, all wrong on the lenses' own
runs (an empty barrier line in the voice queue fooled it; see P10). Measure-first run: the lenses did not read
codex-report.md or codex-review.md.

## Should fix

1. **Draw a path at 680x425 and 375 wide: the part badges stack and their leaders tangle** across the path and each
   other, so nobody can tell which badge changes which part. `drawParts()` leader routing. On small stages put each
   badge on or right beside its own part; a leader never crosses the ribbon or another leader. (Play 1, Craft 1) general
2. **The painted dancer breaks apart at Low**: kneeling Bend, Twist and Swing show thigh boxes, missing shins and
   skin patches at the knees; the low stand has forearms hanging as detached strips with green fringe at the
   fingertips; the head sinks in Low Swing; the low gallop is out of joint. Pieces overlap at the joints, fix the
   low-stand arms (hands on knees), re-despill the hands, limit the neck. (Play 2, Craft 2) family:dance
3. **DA:Pr4.1.2a is cited for pathways only**: the grade 2 expectation adds facings, symmetrical and asymmetrical
   shapes and circling versus turning, which no activity teaches. Move the code to choreography-board (or another
   dance sibling) in the spec, notes and header; do not add a thin activity to keep it. (Teaching 1) general
4. **The level guide looks like three big buttons and does nothing** when tapped. Make each band set the level, the
   same as the panel button (simplest for K-2), or restyle it so it no longer reads as a control. (Play 3) general
5. **The end of Mystery path names no next action**: after round 8 the hint and line should say "Tap Play again for
   new mysteries." (once spoken, then hint only). (Play 4) general
6. **The Mystery hint names the dimmed Go during the trip**: on Go, the hint becomes the watching step ("Watch the
   dancer. Draw the pathway in the air with your finger."). (Play 5) general

## Polish accepted

7. "Middle level. Stay in the middle." gets a body cue, for example "Middle level. Stand up, not too high and not too
   low." (new line in lines.json and the spec voice table). (Teaching 2, Play 6) general
8. High reads only by the arms: a visible rise of the whole figure (heel lift), or a small hop in Shake High.
   (Teaching 3) family:dance
9. Name locomotor and nonlocomotor once: "These moves stay in one place." in the Levels welcome, "Now we travel!" in
   Pathways, and a notes line. (Teaching 4) general
10. Empty barrier lines in the voice queue (`newRun()`, `afterRead()`): use `V.hush()` / `V.dropQueued()` and a kit
    way to wait for Read, so the log holds only real lines. (Craft 3) general
11. Support at home rewritten to be about this tool and doable tonight (draw a pathway on paper and walk it; sky,
    table, grass freeze; curved around a chair, straight back). (Teaching 5) general
12. Notes: low is on the floor for moves in place and a deep crouch when traveling. (Teaching 6) general
13. Older ribbons keep readable end badges (stagger them or place each at its ribbon's middle). (Teaching 7)
    family:dance
14. Mystery round 7: after the right answer, once, "A circle is a curved pathway too!" (Teaching 8) general
15. The first move takes about 8 s from tap to motion: fold Copy me into the Levels welcome, or let the dancer take
    the move's first shape as the call ends. (Play 7) general
16. The gallery start star covers the fifth ribbon: hide it in the gallery or shift the row. (Play 8) family:dance
17. Part badges sit inside the `role="img"` stage, so screen readers miss them: move them to a group outside it.
    (Craft 4) general

## Nits (optional)

- "Which level was the dancer?" could read "Was the dancer high, middle or low?" (Teaching 9)
- Small 30 px zigzags and loops clamped at the left edge read wrong in `Dance.readPath` (Teaching 10, family:dance)
- Close the spec's open question on sharing the dancer with PE: BASELINE w1-21 settles it (Teaching 11)
- A Low trip's end badge touches the crouched dancer (Play 9)
- 760x900 Draw a path leaves about 120 px unused under the panel (Play 10)
- Tab order in Levels at 1366x768 differs from the visual order (Craft 5)
- A part badge tap says "Get close to the floor" when nobody dances yet; "Part 1, low." fits better (Craft 6)
- 31 superseded `dancer-*` entries in art/prompts.json: remove or mark deferred (Craft 7)
- Spec voice table and its "Art: none" line are out of date (Craft 8)

## Settled calls

- Rule 5 does not apply. Every Done when passes (Teaching). Voice counts right (Craft). Contract clean at 946 KB.
