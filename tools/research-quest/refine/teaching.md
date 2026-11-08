# Teaching lens: research-quest (round 1)

Cold lens, 2026-11-06. Read spec.md, src.html, notes.md, tool.draft.json, audit-states.json and audit-r1/audit.md.
I drove the bundle in my own Chrome (port 9861). Council logic was checked by running `__tool.evaluate` on seeded runs.
Frames: `S:/CurioClass-codex-scratch/research-quest/teaching/frames/`, outputs `.../teaching/out-*.json`,
logic table `.../teaching/logic-out.json`.

Counts: blockers 2, should fix 4, polish 4, nit 2.

## Blockers

1. **Trail back sends a skipped visit to Stop 4, not Stop 2** (src.html:677-678, `references`; traceEvidence 1039).
   Leave out the library, county office, nature center or notebook at Plan and its council question fails, but the
   Trail back line and card say "Stop 4" (Organize). The dialog title says "Trail back · Organize" and the text says
   "Your visits did not bring back this evidence", so the label and the reason disagree. The real shortcut was the
   Stop 2 plan. Trail back is the tool's one idea ("traces a line straight back to the choice"), so pointing at the
   wrong stop teaches the wrong lesson. It also fails Done when 2: changing one earlier choice (the visit plan) does
   not send the line to that stop. The same applies when every note goes in Not needed: question 4 points to Stop 3
   and says "Your visits did not bring back this evidence", but the cause is Organize (allnotneeded-trail).
   How seen: logic-out.json (q2_libraryNotVisited, q3_countyNotVisited, q5_natureNotVisited, q1_notebookNotVisited
   are all `X@4`); frames skiplib-trail.png, skiplib-trace-q2.png, allnotneeded-trail.png. Better: when the note's
   place was never visited, use Stop 2 and say "You did not plan a visit to the library". When the note is in Not
   needed, use Stop 4. Tag: general.

2. **A plan built on unattributed copied words gets "Plan approved!"** (src.html:674, question 4 checks one note only).
   Save the library note well with its source. Save the other three as "Copy it, no quote marks" with **Save note**
   (no source). The council approves with zero missing pieces and no aside. Trail back shows five green ticks,
   including "Where did that fact come from? You kept the source with this note." Three of four notes are someone
   else's exact words with no quote marks and no source, and the tool's only verdict praises it. That undoes
   AASL Engage VI.B.1 (the code this tool claims for quoting and paraphrasing) and the spec's own premise that
   "every shortcut you take comes back". How seen: logic-out.json `onlyLibrarySourced: approved`; frames
   onlylib-ending.png, onlylib-trail.png. Better (stays inside the story): any outlined note copied without quote
   marks, or saved with no source, brings back question 4's challenge for that note (the principal points at it),
   or adds an uncounted aside like the too-close one. This changes a council rule, so the integrator may route the
   exact rule to the spec's open questions. The flaw itself must be fixed before Cory. Tag: general.

## Should fix

3. **Meaning-changed notes count as "Answer held"** (src.html:671-676, 697-699). If every note uses the
   changed-meaning version, questions 2, 3 and 5 are still answered with a tick. Lily asks "When should our flowers
   bloom?" and the answer on screen is "Monarchs only visit flowers in the spring. Our plan: Plant flowers that bloom
   in late summer and fall." That contradicts itself and still counts as held. Q2 is answered by "they can use other
   plants too". Q3 is answered by "Any milkweed from any store works, and a little pesticide is fine." The ending is
   "Approved, with homework" (one missing piece) while every note says the opposite of its source. How seen:
   logic-out.json `allChanged`; frames allchanged-q2.png, allchanged-q5.png, allchanged-ending.png,
   allchanged-trail.png. Better: a question whose answering note is a changed version is not answered, and its trail
   card says the note changed the source's meaning (Stop 3). Tag: general.

4. **"Those are the book's exact words... name the book" on notes that are not from the book** (src.html:694).
   Question 4 targets the first note under "What monarchs need", or else the first outlined note. When that note is
   the county page or the club notebook copied without quote marks, the principal still says "the book's exact
   words" and "name the book". In the county case the source line is shown right above it, so "name the book" is
   also wrong. How seen: out-county-copy-q4.json, out-notebook-copy-q4.json; frames county-copy-q4.png,
   notebook-copy-q4.png. Better: "Those are the exact words from [title]. Put them in quote marks." (Spec Content
   wording carries the same flaw: fix both.) Tag: general.

5. **AASL Collaborate is only represented, not taught** (spec Standards; notes.md "Standards in the activity").
   Every council answer is "filled in automatically from your pack". The student presses Next question and reads.
   They never choose, say or defend an answer, so "presenting findings to a group and answering its questions" is
   watched, not done. notes.md itself says Collaborate is "represented". Per BASELINE rule 2, either add a real step
   (for example, at each question the student taps the pack note or slide they would answer with, then the council
   reacts to that choice), or move the code to a tool that teaches it. Tag: general.

6. **"Save note with its source" is styled as the main button** (src.html:796, `btn('save-source',..., primary)`
   against a plain "Save note"). The spec says choices "never show right or wrong when made". The teal primary
   styling tells the student which save is right before the council does. How seen: audit-r1
   state-gather-1366x768.png. Better: give both save buttons the same style. Tag: general.

## Polish

7. **Meaning-changed paraphrase is always the shortest** (spec Content, src.html:525-576). Lengths (good/close/
   changed): library 103/106/74, county 143/131/66, nature 120/123/42, notebook 73/69/40, video 78/56/44,
   seed 61/61/53. On a second run, or in a teacher-led class vote, "skip the short one" works without reading for
   meaning. The shuffled order does not hide this. Better: make the changed versions as long and as fluent as the
   others (for example, nature: "Grown monarchs feed on nectar from many flowers, mostly in spring before they head
   north."). Tag: general.

8. **The homework list reads badly when piece 1 is missing** (src.html:843-844). Output: "come back with a clear
   question and what our garden has now and when the flowers should bloom." Piece 1 already contains "and", so the
   list blurs. Frame two-missing-ending.png. Better: join with a semicolon or "; and", or reword piece 1 ("a clear
   question about our garden's needs"). Tag: general.

9. **Question 4 never says which fact it is asking about** (src.html:688-695). The speech card shows "Where did
   that fact come from?" and then a citation, but not the note it is about. The student can't connect the answer to
   a note without opening the pack. Better: show the note text above the source line (frame nbcopy-q4.png).
   Tag: general.

10. **Organize note cards clip the fact that decides the heading** (audit lead, confirmed on
    audit-r1/state-organize-800x500.png). At 680x425, 800x500, 1000x625 and 375 wide, the note text is cut to two
    lines ("It's the only plant they eat, so no...") and the source line is cut too. "× no source" is the
    information a student should notice here. Better: keep the source line whole and let the card grow, or open the
    full note on the first tap. Tag: general.

## Nit

11. **The approved ending says "Plan approved!" twice**, once as the heading and again at the start of the line
    (audit-r1/state-ending-1366x768.png). Tag: general.
12. **Question 3 accepts the county note under any heading**, including "What our garden has now". It is harmless,
    but a teacher discussing "Did your outline make the note useful?" may notice. Tag: general.

## Checked and fine

- **Done when 1:** the ideal run is approved with five ticks (logic-out `ideal`; audit state-ending and
  state-trail-back frames).
- **Done when 2:** each of questions 1 to 5 fails on its own when one choice changes (question A, notebook heading,
  library in Not needed, no milkweed step, no source, copy without quotes, no fall step). The stop is wrong when the
  changed choice is the visit plan (blocker 1).
- **Done when 3:** question 6 appears only with a changed note, question 7 only with the seed step, and the
  too-close aside only with a too-close note. With no notes in the outline, question 4 says "There's nothing in the
  outline to point to." (allnotneeded-q4).
- **Done when 4:** endings follow the count (0 approved; 1 or 2 homework, with pieces named; 5 not yet).
- **Done when 5:** Go is enabled only at exactly four places. On to Stop 4 is enabled only at four notes. A fourth
  plan step is disabled with a title. Tap-then-tap reaches the end (audit states organize to trail-back).
- **Done when 6:** the run survives a fresh tab (rewind-reload: stop 4 restored). Rewind to Plan keeps the question
  and places and clears notes and headings (rewind-check). Start over, No then Yes, clears both state and `rq-run`
  (restart-check).
- **Facts:** "caterpillars eat only milkweed", "adults feed on nectar of many flowers during breeding and
  migration" and "up to 3,000 miles" match the FWS monarch page (fetched 2026-11-06). That page's overview also
  says "more than 2,000 miles (3,000 km)", but the video passage uses the Behavior figure, so it is fine. Native
  common milkweed and butterfly weed, fall nectar and no pesticides match the Xerces and USDA lines in the spec.
  All story places and people are labeled fictional in notes.md.
- **Grade fit:** language is plain for 6-8. The notes' What it teaches, Key skills, Support at home and Talk about
  it are true of this tool, and the home ideas are doable tonight. No sensitive topic, so no rule 8 note is needed.
  No cultural, Native or hard-history content, so there is no sensitivity referral.
- **Codes taught by doing:** I.A.1 (Ask), I.B.2 and C3 D1.5 (Plan), D3.1 and W.6-8.7 (four sources into an
  outline). Engage VI.B.1 is practiced at Gather but undercut at judging (blocker 2). Collaborate is not taught
  (should fix 5).

## Audit pilot

- **Leads confirmed:** the organize note-copy clipping at small sizes (polish 10, which also matters for teaching).
- **Leads wrong or not mine:** the many trail-back "overlap" and "hidden under path" rows come from the SVG route
  hit areas (44 px transparent strokes) overlapping cards and each other. On my 1366x768 frames the visible lines
  and cards read clearly, so I'm leaving those for Play and Craft. The "pack item cut by a scroll panel" row at
  1280x720 is not a teaching issue.
- **Missed (out of its reach):** wrong Trail back stop for skipped visits (blocker 1), approval of unsourced
  copies (blocker 2), changed-meaning answers held (should fix 3), the "book's exact words" mismatch (should fix 4),
  the styled-right save button (should fix 6) and the shortest-option tell (polish 7). None of these show in a
  layout or voice check.
