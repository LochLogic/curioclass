# Play lens: moon-base-drama (round 1)

Played twice: as a K-2 child alone at home, and as a teacher projecting it as Commander Ada. Bundle as built, not re-bundled.
Frames: shared audit `S:/CurioClass-codex-scratch/moon-base-drama/audit-r1/` (all sizes, every state) plus my own in
`S:/CurioClass-codex-scratch/moon-base-drama/play/shots/` (every beat at 1366x768, all three endings, rewind from the end,
map at the end, Motion off on beat 4, 680x425 beats 1, 5 and 8) and voice logs `play/vlog-full.json` (full run plus a
rewind, held clicks 2.5 s apart), `play/vlog-fast.json` (0.3 s taps, Back, mode switch), `play/vlog-mf.json` (Mission first).
No console errors in any run. Nothing cultural, Native or hard-history: no sensitivity review needed.

## Findings

1. **The ending barely changes, so "watch the story change" doesn't land.** Where: beat 8, src.html:113-115, 657-663.
   What: the payoff of the whole tool is the night greenhouse, but the three endings look nearly the same. The painted
   background (lush tomatoes, healthy beds) is identical for every ending, so "the plants are droopy" plays over a
   thriving greenhouse. The only changes are the number of lamp beams and a `scaleY(.55)` squash on one small planter,
   which reads as shorter plants, not wilted ones; the two-full and none-full endings use the same squash. A K-2 class
   comparing two runs after a rewind sees almost nothing. Better: wilt that is unmistakable (leaves hanging, yellowed,
   tomatoes dropped), apply it to the whole greenhouse (or a darkened, desaturated background when Water or Warm is low),
   and a frost or chill cue when Warm is low, so each meter gap has its own picture. How seen: `play/shots/b8-allB.png`
   (1,2,1), `b8-two.png` (3,2,3), audit `state-night-1366x768.png` (3,3,3). Level: **should fix**. Tag: general.

2. **Choice icons are abstract glyphs a pre-reader can't use; one shows as an empty box.** Where: src.html:397-410.
   What: the spec asks for icons (sun and battery, moon, ice cube, wave, blanket, door) because K-2 children can't read
   the button words. The build uses text glyphs: "☀ ▣" for batteries, "≈" for a river, "▧" for a blanket, and "▯" for
   the door, which renders as a plain empty rectangle that looks like a missing character. Only the ice cube is a real
   picture. The same glyphs appear on the map strip and in the Rewind dialog. Better: drawn SVG or painted icons
   (battery with a sun, wave, folded blanket, door). How seen: `b6-warmA.png`, `b6-warmB.png`, `b8-map-open.png`,
   `b3-choiceA.png`. Level: **should fix**. Tag: general.

3. **A child alone can't hear the question or the choices.** Where: src.html:469 (Read), 335-336 (choice buttons).
   What: rule 4 says defaults must work for a solo user. Alone, a K-2 child hears Mission Control's line, but Ada's
   question is never spoken (by design) and the two choice buttons are words only, so a pre-reader on a choice beat
   hears "Commander, read your card. When the crew answers, tap their choice." and then has nothing they can read. Read
   repeats Mission Control, not the options. The welcome also tells a lone child "Teacher, you are Commander Ada".
   Better, without breaking the teacher-in-role design: speak the two crew lines as part of the choice beat ("Crew, you
   could say: Fill the batteries now! Or: Wait until dark."), or let Read on a choice beat say the two options. How
   seen: `state-batteries-1366x768.png` and the code path above. Level: **should fix** (the integrator may weigh this
   against the K-2 teacher-led band in STANDARDS.md). Tag: general.

4. **The how-to goes ahead of the story in Mission Control's voice and on the radio caption.** Where: src.html:440-458
   (`guide`), caption at 518-519. What: the first time each step comes up, Mission Control opens with a UI instruction
   ("When the crew is done, tap Next. The ice block is heavy...") and the radio caption keeps that text on screen. It
   breaks the radio fiction for the class, and it buries the moment: the best beat in the tool, the full-greenhouse win,
   opens with "Tell Ada which choice helped. Tap Rewind." before "Great work, crew!", and tells a crew that just won to
   tap Rewind. Better: story line first, instruction after it (or in the hint only, with the voice at the end), and on
   the all-full ending say "Tap New mission, or Rewind to try another way". How seen: `state-night-1366x768.png`,
   `b5-lift.png`, `b2-greenhouse.png`, `vlog-full.json` (reflect_endTwo). Level: **polish**. Tag: general.

5. **Two choice lines don't make sense as answers.** Where: src.html:409-410, beat 6. What: Ada asks "How do we keep the
   plants warm?" and the crew line is "Wrap it in a blanket" ("it" has no referent; the scene is an airlock with space
   suits). The other option, "Open the doors for air", is not an answer about warmth at all, so a child can't reason to
   it as a tempting mistake. Better: "Wrap the greenhouse in a blanket" against a warmth answer that is wrong for a moon
   fact, for example "Open the windows to let the Sun in" (no Sun at night, and the air would rush out). How seen:
   `b6-warmA.png`, `b6-warmB.png`. Level: **polish**. Tag: general.

6. **Ada's card has nothing to say after a choice.** Where: src.html:623-624. What: after a choice the card keeps the
   question that was just answered; only beat 3, choice B, gets a response ("Hmm. Should we rewind and try again?").
   The teacher in role has no line for the good outcomes or for the river and open-doors results. Better: one short
   reaction line per result on the card ("Great work, Rover Driver! Bring it home."). How seen: `b3-choiceA.png`,
   `b4-choiceA.png`, `b6-warmB.png`. Level: **polish**. Tag: general.

7. **The premise is lost if the first tap is a badge or Mission.** Where: src.html:467. What: the welcome ("Teacher, you
   are Commander Ada. Tap a job badge for each crew member.") is dropped when a badge is tapped first, which is what
   the screen invites ("Choose a job. Mime your prop."), and it never comes back. Mission first gives "Tap a job badge"
   and then the badge line; the welcome is never heard. Better: bring the premise back once in the first job line or at
   Start mission. How seen: audit table rows 1 and 5-10, confirmed in `vlog-mf.json`. Level: **polish**. Tag: general.

8. **"Back to base" in the Rewind dialog.** Where: src.html:363. What: it closes the dialog and returns to the story,
   but "base" is also the Crew screen's name (Moon Base Luna), so a teacher may expect to go to Crew. Better: "Back to
   the story". How seen: `b8-map-open.png`. Level: **nit**. Tag: general.

9. **A job badge can't be unchecked.** Where: src.html:559-566. What: badges look like toggles (aria-pressed, a check),
   but a second tap only repeats the line; a mistaken tap stays checked. Level: **nit**. Tag: general.

10. **Rewind offers Batteries before any battery choice exists.** Where: src.html:651. What: on beat 3 with no choice
    yet, Rewind enables Batteries, which "rewinds" to the beat already showing and says "Rewinding to the batteries".
    Better: enable a node once its choice is made. How seen: audit `state-rewind-open-1366x768.png`. Level: **nit**.
    Tag: general.

What works: the beats read well aloud at a teacher's pace, every tap cuts the radio at once and nothing stale followed
in the fast run, Back undoes a choice, rewinding from the end restores the meter and fades later nodes (`b8-rewind-water.png`:
3,1,1 with Warmth faded), all three endings are reachable and correct, the choice order varies, and the painted scenes
are inviting at every size including 680x425 and the 375 iframe.

## Audit pilot

- Confirmed: the welcome is not heard after a first tap on a badge or on Mission (finding 7; `vlog-mf.json`).
- Wrong or by design: "two quick taps cut the line" rows. The spec wants any tap to stop the radio at once (Done when 5),
  so a line cut by the second tap is correct here, not a fault. All size and state rows were clean and held on my frames.
- Missed: glyph icons and the empty-box door (2), the near-identical endings (1), choices unreadable for a lone
  pre-reader (3), how-to before the story in the voice and caption (4), and the choice wording (5, 6). None of these are
  mechanical.
