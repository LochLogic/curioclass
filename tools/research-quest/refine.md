OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 2 (general 2, family 0), should fix 8 (general 8, family 0), polish accepted 15

# Refine: research-quest

Lenses: teaching.md, play.md, craft.md (no sensitivity.md; all three lenses found nothing cultural, Native or
hard-history). Not a Curiosity. Integrator spot-checks: read src.html 664-700 (`evaluate`, `answerText`), 790-797
(save buttons), 838-848 (`endingView`), 1035-1042 (`traceEvidence`), 1262-1279 (pointer drag fallback); each claim
below that cites those lines was confirmed in the code.

## Blocker
1. **Trail back points to the wrong stop when the cause was not at Stop 4.** src.html:677-678 (`references` in
   `evaluate()`), with `traceEvidence` at 1039. The stop is fixed per question (`['library',4]`, `['county',4]`,
   `['nature',4]`, notebook 4 once B is chosen), so leaving a useful place out at Plan sends the red line to
   "4 Organize" while its own card says "Your visits did not bring back this evidence." The student rewinds to
   Organize and finds nothing to fix. Same flaw the other way: question 4 with an empty outline (every note in Not
   needed) points to Stop 3, but the cause is Stop 4. This is the tool's one idea and fails Done when 2. Seen:
   teaching/frames skiplib-trail.png, skiplib-trace-q2.png, allnotneeded-trail.png, teaching/logic-out.json
   (q1/q2/q3/q5 not-visited runs all `X@4`); play/out/fail-trail-1366.png, trail-click-q1.png; craft finding 3
   (code read). Fixed: compute the stop from the actual cause for each result: place never visited = Stop 2 (card:
   "You did not plan a visit to [place]."); note saved without source, copied without quote marks, or meaning
   changed = Stop 3; note in Not needed, wrong heading, or missing plan step, or an empty outline for question 4 =
   Stop 4; question not B = Stop 1. Add a failing run (one skipped useful place, one all-Not-needed run) to
   `audit-states.json` so the audit sees a red trail. (general)

## Should fix
2. **"Save note with its source" is styled as the right answer.** src.html:796: `save-note` gets the plain class
   `''`, `save-source` gets the default primary (teal) style. Spec: choices "never show right or wrong when made".
   Seen: audit-r1/state-gather-1366x768.png. Fixed: both save buttons the same style (both plain, or both primary).
   (general)
3. **A stale pointer drag can silently move a note.** src.html:1265-1279. `pointerDrag` is set on pointerdown and
   cleared only on pointerup; there is no `pointercancel` or `dragstart` handler, and Chrome fires `pointercancel`
   when the HTML5 drag starts on the `draggable` card. The next pointerup on any heading 8 px or more away moves the
   old card while the hint says "Tap a note card first...". Seen: craft/f1 `drag-stale` (`headings` became
   `{library: 2}`). Fixed: clear `pointerDrag` on `pointercancel` and on `dragstart`. (general)
4. **Organize note cards clip the note to two lines, with empty space above it.** src.html:318 (and 411 at 600 px
   wide), `.note-card .note-copy`, at every height under 641 px and at 375 wide. The cut words are what tell a good
   note from a too-close one, and the source line ("× no source") is cut too; the full text is only a hover
   `title` that touch and keyboard users never get. All three lenses and the audit lead agree. Seen:
   audit-r1/state-organize-1000x625.png, state-organize-680x425.png, state-organize-800x500.png,
   state-organize-375x812.png. Fixed: text starts at the top of the card and uses its height; the source line is
   never clipped; a selected card (tap-then-tap) shows the full note. (general)
5. **"Those are the book's exact words... name the book" on notes not from the book.** src.html:694. Question 4's
   note can be the county page or the club notebook, and the source line can be shown right above "name the book".
   Seen: teaching out-county-copy-q4.json, out-notebook-copy-q4.json; frames county-copy-q4.png,
   notebook-copy-q4.png. Fixed: "Those are the exact words from [source title]. Put them in quote marks." and, when
   the note has no source, "...Put them in quote marks and name where they came from." Update the matching line in
   spec.md Content (question 4) to the same wording; it is a factual correction, not a rule change. (general)

## Polish accepted
6. **Ending repeats its heading.** `endingView()` (src.html:842-848): "Plan approved!" heading then "Plan
   approved! ..." in the paragraph; "Not yet." the same. Drop the repeat from the paragraph (spoken line unchanged).
   Seen: audit-r1/state-ending-1366x768.png, play/out/fail-ending-1366.png. (general)
7. **Homework list blurs when piece 1 is missing.** src.html:843-844. "a clear question and what our garden has now
   and when the flowers should bloom." Join pieces with ", and " (or "; and ") so piece 1's own "and" reads clearly.
   Seen: teaching two-missing-ending.png. (general)
8. **Meaning-changed paraphrase is always the shortest.** spec Content, src.html:525-576 (good/close/changed
   lengths, e.g. nature 120/123/42, county 143/131/66). "Skip the short one" solves it without reading. Rewrite the
   six changed versions to be about as long and fluent as the good one (within about 15 percent), same wrong
   meaning; e.g. nature "Grown monarchs feed on nectar from many flowers, mostly in spring before they head north."
   Update the same strings in spec.md Content. Seen: teaching lens length table. (general)
9. **Question 4 does not show which note it asks about.** src.html:688-695. Show the note's text above the source
   line in the speech card. Seen: teaching nbcopy-q4.png. (general)
10. **Trail back lines hidden under cards.** Lines from second-row cards (Q5, Q7; Q3-Q5 at 375 wide) run behind
    first-row cards. Draw the lines above the cards with a light halo, or route them around. Seen:
    play/out/fail-trail-1366.png, trail-focus-q5-1366.png; craft/f2 kb-trail.png;
    audit-r1/state-trail-back-375x812.png. (general)
11. **Trace card has no way to act.** `trace()` dialog says "Follow it to Stop N" but offers only "Back to quest".
    Add "Rewind to Stop N" that goes through the existing Yes / No check. Seen: play/out/trail-click-q1.png.
    (general)
12. **After a saved note the hint points to the pack while the place buttons are right below.** `how()` stop 3,
    `gatherNext`. On layouts where `.visit-tab` shows in the card, say "Tap the next place below."; keep the pack
    wording where the tabs are hidden (this is a hint change only; keep the spoken line if its clip exists, or
    update lines.json to match). Seen: audit-r1/state-saved-note-1366x768.png. (general)
13. **Read reads decoration.** src.html:642-643 reads the chapter `innerText`: caps eyebrow, aria-hidden seal
    ("FRIDAY COUNCIL", "0 / 4 NOTES"), footer, "Tap me, then a heading" x4. Build the Read text from the card's
    title, choices and status, skipping `aria-hidden` and decoration. Seen: audit held-click table row #read.
    (general)
14. **Empty stop badges show as blank white pills.** src.html:41 `.stop small`. Hide `.stop small:empty`. Seen:
    audit-r1/size-1366x768.png. (general)
15. **Marker covers the current stop's label under 641 px tall.** ("Orga ze", "Ga er"). Lift the marker above the
    dot or set it beside the label. Seen: audit-r1/state-organize-680x425.png, state-gather-680x425.png,
    state-organize-1000x625.png. (general)
16. **Nit: two tab stops per council question on Trail back.** SVG `g.trace-path` has `tabindex="0"` and its card
    opens the same dialog. Set the paths to `tabindex="-1"`; cards stay the keyboard route (paths stay clickable).
    Seen: craft/f2 kb-trail. (general)
17. **Nit: company name in the bundle header and missing people flags.** src.html:14 "Illustrations generated with
    OpenAI gpt-image" (rule 15): drop the company name (e.g. "Illustrations generated for Curio Class"). Add
    `"people": false` to rq-trail-map, rq-garden-bed and rq-garden-bloom in prompts.json. (general)
18. **Nit: unused lines.** `L.next` and `L.endingNext` are in voice/lines.json but never spoken. Remove them from
    the spoken lines (keep them as hint text). (general)

## Settled calls
- **Blocker count.** Teaching had two blockers, Play one, Craft rated the Trail back stop a should fix (from code
  only). Teaching and Play confirmed it on runs, so it stays a blocker. Teaching's blocker 2 (unsourced copies
  approved) is also a blocker: see item 19 (integrator call, 2026-11-06).
- **Severity of clipped Organize cards.** Teaching polish, Play and Craft should fix: should fix, since the cut
  text is the information the student sorts by.
- **Audit "overlap" rows on Trail back.** All three lenses agree they are the 44 px transparent hit strokes and
  the lines' bounding boxes, not visible clutter. Only the visible lines-under-cards case (item 10) is taken.
- **"Welcome not heard" after a first tap on a question card, the pack chip or Start over** is allowed (BASELINE
  rule 16). Do not change.
- **Pack list at 1280x720 / 1366x768** is a working scroll panel (Craft); not a fix.
- Keep the ending bands and the seven questions. The council rules change only as items 19 to 22 say.
- Keep "Copy it, with quote marks" a valid, approvable choice for some notes.

## Integrator calls (2026-11-06, BASELINE: a check must reward the right practice; rule 2 for codes)

The merge routed these to the spec's open questions. They are settled here from Cory's standing rules, not sent to
Cory: the tool claims Engage VI.B.1 (quote and paraphrase with credit), so a council that approves uncredited copies
fails the spec's own "Scores and checks reward the right thing" lesson. Update spec.md's Content and Done when to
match each change.

19. **Blocker: unsourced or unquoted copies are approved.** Save the library note well with a source and the other
    three as "Copy it, no quote marks" with no source: "Plan approved!" with five ticks (teaching onlylib-ending.png,
    onlylib-trail.png). Fix: question 4 checks every outlined note, not one. Any outlined note copied without quote
    marks or saved without a source brings back question 4's challenge for that note (name the note), and Trail back
    points to Stop 3. Re-run the brute force on the council: the all-good plan approves, every uncredited copy fails.
20. **Should fix: quoting everything wins.** Four quotes with sources, obvious headings: approved with no aside
    (play/out/quote-all-ending.png). Fix: when every outlined note is a quote, one council member asks "Can you say
    that in your own words?" as an uncounted aside (the plan still approves; the paraphrase cards now have a reason).
21. **Should fix: meaning-changed notes still answer questions 2, 3 and 5.** All-changed run counts Lily's question as
    held (teaching allchanged-q2.png, allchanged-ending.png). Fix: a question whose answering note is the changed
    version is not answered, and Trail back points to Stop 3.
22. **Should fix: "Not yet" ending names nothing to do (Play 5).** Give it the same named missing pieces as the
    homework ending.
23. **Should fix: AASL Collaborate is represented, not taught (Teaching 5).** Answers are filled in automatically.
    Drop the Collaborate code from the tool's standards (tool.draft.json, spec Map and Standards map, notes.md),
    BASELINE rule 2; note the move in notes.md so the catalog can give it to a tool that teaches it.
24. **Polish: Mr. Adeyemi's reply to B reads as "correct" (Play 10).** Give it a question back, e.g. "Good. What will
    you need to find out first?", so the four replies stay even.
25. **Polish: spec Art line says "All local FLUX"** but prompts.json records 11 of 13 images as gpt-image (Craft 10).
    Correct the spec's Art line to what prompts.json records; flag any people image for Cory's contact sheet.

## Not taken
- Stop labels moved onto the painted clearings (Play 4, second half): needs art-coordinate rework; revisit at Final
  look with the real map.
- Question 3 accepting the county note under any heading (Teaching 12): matches spec, harmless.
- Pack list cut at 1280x720 (Play 9): working scroll panel, not clipped content.
