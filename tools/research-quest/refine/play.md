# Play lens: research-quest (round 1)

Played twice: once as a grade 6-8 student alone (ideal run, a careless run that skipped two useful places and
quoted the Butterfly Blend ad, and a "quote everything" cheap run), once as a teacher projecting at 1366x768.
My frames: `S:/CurioClass-codex-scratch/research-quest/play/out/`. Shared audit frames:
`S:/CurioClass-codex-scratch/research-quest/audit-r1/`.

The story holds up well for a solo student: every stop's first screen names the action, the pack and stop badges
make progress clear, the council speech card is center stage, and the persistence across reloads worked (my later
shots reopened straight into the saved trail state). The problems are in the payoff and in how cheaply it can be won.

## Findings

1. **Trail back sends "didn't visit it" failures to Stop 4, not Stop 2.** blocker, general
   - Where: `src.html` `evaluate()`, the `references` table (`['notebook', run.question !== 1 ? 1 : 4], ['library',4],
     ['county',4], ... ['nature',4]`): the stop is fixed per question, whatever choice actually caused the miss.
   - What: skip the garden club notebook and the nature center at Plan, and the trail draws Q1 and Q5 as
     "Still missing · Stop 4" into **4 Organize**, while the evidence line under the same card says "Your visits did
     not bring back this evidence." Opening the line gives "Trail back · Organize ... Follow it to Stop 4 ... No
     matching note in the outline." A student who rewinds to Organize finds nothing to fix there; the real cause was
     the Plan choice. The same happens for Q2 and Q3 if the library or county office is skipped. The Trail back is the
     tool's one idea ("each council question traces a line straight back to the choice that answers it") and spec
     Done when 2 asks that each failed rule's line goes to the stop whose choice decided it. A readout that points to
     the wrong cause is a blocker.
   - Better: compute the stop from the actual cause: not visited = Stop 2, not saved or meaning changed or no source =
     Stop 3, in Not needed / wrong heading / missing plan step = Stop 4, wrong question = Stop 1. Also Q4 with an empty
     outline currently points to Stop 3; the cause there is Stop 4.
   - Seen: `play/out/fail-trail-1366.png`, `play/out/trail-click-q1.png`, `play/out/trail-1000.png`.

2. **Quoting every source word for word earns a full approval; paraphrasing is never needed.** should fix, general
   - Where: `evaluate()`: Q2, Q3, Q5 ignore the note's way; Q4 accepts `quote` with a source; the too-close aside only
     fires for version 1.
   - What: the cheap sweep (tap "Copy it, with quote marks" and "Save note with its source" four times, then the
     obvious headings) gets "Plan approved!" with no aside at all. The three "In my own words" cards, the most
     interesting choice in the tool, are skippable at zero cost, and "always quote, always cite" is exactly the habit
     a grade 6-8 research lesson wants to move past (an outline of four block quotes is a pile, not a case; the chapter
     title says "Make a case, not a pile"). A teacher projecting it will see the class find this in one run.
   - Better: real material, not a penalty game: e.g. when every outlined note is a quote, Principal Okoro (or Lily)
     asks one more question, "Can you say that in your own words?", that only a good paraphrase answers; or the slides
     at Stop 5 show the quotes and a council member reacts. Keep "quote marks are acceptable" for one or two notes.
   - Seen: `play/out/quote-all-ending.png`.

3. **Organize note cards clip the note to two lines while the card is mostly empty.** should fix, general
   - Where: Stop 4 `.note-card .note-copy` at 680x425, 800x500, 1000x625 and 375.
   - What: at 1000x625 each card is about 160 px tall with the text pushed to the bottom and cut ("...so no milkweed
     means no..."), with a large blank area above it. The student has to place notes by meaning, and a too-close or
     changed version can only be told apart by reading it; the full text lives only in a hover `title`. Confirms the
     audit's clipped-text lead.
   - Better: let the copy fill the card from the top (no clamp when there is room), clamp only when truly short of
     space, and give the open card in the pack the full text.
   - Seen: `audit-r1/state-organize-1000x625.png`, `audit-r1/state-organize-680x425.png`.

4. **Trail back lines run under the cards and the painted map does not match the stops.** polish, general
   - Where: Trail back, all sizes (audit overlap leads, confirmed).
   - What: lines from the second row of cards (Q5, Q7) start under the first-row cards and are hidden for part of
     their run; with five or more lines converging on "4 Organize" the picture becomes a fan of identical curves. The
     painted trail and its clearings sit in different places from the code stop labels in a row along the top, so the
     lines end on labels, not on places on the map. Better: one row of cards, or lines routed around cards, and stop
     labels placed on the painted clearings so the line lands on the place where the choice was made.
   - Seen: `play/out/fail-trail-1366.png`, `play/out/trail-focus-q5-1366.png`, `audit-r1/state-trail-back-1366x768.png`.

5. **The ending lands flat and repeats itself.** polish, general
   - Where: `endingView()`.
   - What: the heading "Plan approved!" is followed by body text starting "Plan approved! ..."; "Not yet." is followed
     by "Not yet. The council asks...". After five stops of work the approved moment is one sentence and a picture; the
     "Not yet" ending names nothing the student could do (only the homework band lists pieces). Better: drop the
     repeated words, and let the council react in story terms (Lily's line about the bed, Mr. Hale's about planting
     day), and give "Not yet" the same named missing pieces the homework ending has.
   - Seen: `audit-r1/state-ending-1366x768.png`, `play/out/fail-ending-1366.png`.

6. **The trace card has no way to act on what it shows.** polish, general
   - Where: `trace()` dialog.
   - What: the read-only card says "Follow it to Stop 4" but offers only "Back to quest"; the student then has to find
     Rewind, open its menu, pick the stop and confirm. Better: a "Rewind to Stop N" button in the card (still with the
     Yes / No check), which turns the Trail back into the second run the spec plans for.
   - Seen: `play/out/trail-click-q1.png`.

7. **After saving a note the hint says "Tap a place in your pack" while the place buttons are right below the note.**
   polish, general
   - Where: `how()` stop 3, `gatherNext`; wide layouts show the `.visit-tab` row in the card.
   - What: the hint points the student to the side panel when the nearer control is the row of place buttons just
     under the note (the `needs` already targets `.visit-tab`). Better: "Tap the next place below." on wide layouts,
     keeping the pack wording where the tabs are hidden.
   - Seen: `audit-r1/state-saved-note-1366x768.png`.

8. **Marker covers the current stop's label in the short layouts.** nit, general
   - Where: stop strip at 680x425 and 1000x625 ("Orga ze", "Pres", "Ga er" under the backpack).
   - Seen: `audit-r1/state-organize-680x425.png`, `audit-r1/state-gather-680x425.png`, `play/out/trail-1000.png`.

9. **Pack list cuts "Your outline" at the panel bottom.** nit, general
   - Where: side panel at 1280x720 and 1366x768 from Stop 4 on; the last pack item is half hidden above Rewind.
   - Seen: `audit-r1/state-ending-1366x768.png`.

10. **Mr. Adeyemi's reply to B reads as "correct".** nit, general
    - "That's a question you can answer, and it's about our garden." is the only reply with no question back, so the
      cheap sweep (tap each card, listen) finds the answer at Stop 1. Spec says choosing shows no right or wrong; a
      reply that still nudges (for example "Good. What will you need to find out first?") keeps the pattern even.

No cultural, Native or hard-history content; nothing for a sensitivity review.

## Counts
blocker 1, should fix 2, polish 4, nit 3.

## Audit pilot
- Leads confirmed: Organize note text clipped (680, 800, 1000, 375); Trail back lines overlapping and hidden under
  cards; pack list cut short by its scroll panel at 1280x720 (also visible at 1366x768).
- Leads wrong or harmless: "welcome not heard" after a first tap on a question card is allowed (BASELINE rule 16); the
  premise is on the Stop 1 card and in the story text. The many trail-back "overlap" rows between `g` groups are the
  invisible 44 px hit paths overlapping each other, not visible clutter; only the visible-line cases above matter.
- Missed: the Trail back pointing to the wrong stop (needs a failing run, the audit states only cover the ideal
  run); the quote-everything cheap pass; the empty space above the clipped note text; the duplicated ending words;
  the marker covering stop labels. A failing-run state in `audit-states.json` would have caught finding 1.
