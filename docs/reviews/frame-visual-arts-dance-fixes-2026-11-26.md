# Frame fixes: Visual Arts, grades 3 to 12, and Dance, grades K to 12 (2026-11-26)

The one fix pass of COURSE-RUN stage 3 for seven after-core arts frames: docs/courses/visual-arts-grades-3-to-5,
visual-arts-grades-6-to-8, visual-arts-grades-9-to-12, dance-grades-k-to-2, dance-grades-3-to-5, dance-grades-6-to-8
and dance-grades-9-to-12 (each frame.md). Reads settled: the visual arts expert read
(docs/reviews/frame-visual-arts-grades-3-to-12-2026-11-25.md, "VE"), the dance expert read
(docs/reviews/frame-dance-grades-k-to-12-2026-11-25.md, "DE") and the Codex read of each frame
(frame-<id>-codex-2026-11-25.md: "C-35", "C-68", "C-912" for visual arts; "C-K2", "C-35", "C-68", "C-912" in the dance
section). The model is docs/reviews/frame-visual-arts-grades-k-to-2-fixes-2026-11-25.md.

Files changed:

- The seven frames.
- data/standards/ncas-performance-standards-words.txt: 5 lines replaced, all visual arts (VA:Cr1.2.7a,
  VA:Pr5.1.4a, VA:Re8.1.5a, VA:Re8.1.7a, VA:Cn10.1.7a); each line is 14 words or fewer.
- data/progressions/arts.csv: 8 va rows and 38 da rows. Each was changed by an exact replacement of its own text, so
  no id moved and no other discipline's row was touched; the file is still LF.
- data/plans/frames.csv, data/plans/calendar.csv and docs/courses/CALENDAR.md, through `frame.py sync`.

No PE frame, no music, theater or media arts frame, and no shared doc was edited; their changes are listed for the
lead below.

## Gates

| Gate | Result |
|---|---|
| `python -X utf8 scripts/frame.py sync` | frames.csv 117 courses, calendar.csv 2,119 rows |
| `python -X utf8 scripts/frame.py check <id>`, all seven | 0 failures each. Visual arts 3 to 5 and 6 to 8: 192 days (180 in units). Visual arts 9 to 12: 640 days (624 in units). Dance K to 2, 3 to 5 and 6 to 8: 192 days each. Dance 9 to 12: 640 days. |
| `python -X utf8 scripts/progression.py check arts` | 498 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 121 files, 0 failures |
| Text rules (grep of the seven frames and arts.csv) | No em dash; "Curio" never stands alone; no "practise", "licence", "labelled", "travelling" or "colour" in the frames |

## Visual arts

### Expert read (VE)

| Read | # | Applied or kept | What changed, or why not |
|---|---|---|---|
| VE | S1 | Applied, with one swap changed | The swaps were made as the read's table gives them. 3 to 5: unit 3 Caillebotte became Pissarro's Boulevard Montmartre on a Winter Morning (1897, the Met). Unit 6 keeps Chicano Park and replaces the Great Wall with the painted walls of Tiébélé, Burkina Faso (Kassena women). Unit 9 State Names became an Anishinaabe (Ojibwe) beaded bandolier bag. Unit 10 Leonardo's notebooks became Merian's Metamorphosis insectorum Surinamensium (1705). Unit 11 Fan Kuan became Qian Xuan's Wang Xizhi Watching Geese (about 1295, the Met). Unit 12 Nation to Nation became Te Papa's Te Taiao Nature exhibit, and Maya Lin became Moran's Yellowstone paintings. The WPA poster is a national parks poster only. 6 to 8: unit 2 Bearden became Antonio Berni's Juanito Laguna collage (Argentina, 1960s). Unit 9 Warhol v. Goldsmith became Curio Class original case cards. The WPA posters are work-safety and travel only, named as a return. 9 to 12: unit 1 Catlett became Dürer's Melencolia I (1514, the Met). Unit 10 Wiley became Sherald's Michelle LaVaughn Robinson Obama (2018, the National Portrait Gallery). Unit 15 Benin became Siqueiros's América Tropical and its Getty conservation (see below). **Changed:** for 6 to 8 unit 1 the read proposed Bruegel's The Harvesters, but the K to 2 frame already studies it. So unit 1 uses Lawrence's Street to Mbari (1964, the National Gallery of Art), a different Lawrence work named as a return of the maker (the C-68 F6 suggestion). The one-band rule line ("No work studied in another visual arts band is studied again as new work...") is in all three Base text bullets. The range was re-checked by year in 3 to 5: every year still has Africa, Asia, Europe, the Americas, a Native maker or community and a living maker. |
| VE | S1, 9 to 12 unit 15 | Applied, candidate changed | The read asked for the candidate conservation case "from Asia or the Americas". The obvious Asian pick, Mogao at Dunhuang, is already in 3 to 5 unit 8, and the Great Wave is in K to 2. So the pick is David Alfaro Siqueiros, América Tropical (Los Angeles, 1932, painted over within a few years, conserved by the Getty Conservation Institute with the City of Los Angeles and shown again from 2012 under a shelter). It is an outdoor case to set beside the Night Watch's indoor one, and it fits the unit's Mexican mural thread (Rivera). It is used in no other frame. The candidate cell now asks for a case from Africa or Asia, because Level 3 lost its African work. The leave-out, sensitivity and social studies lines were updated. Dates are from memory: For the lead item 8 in the frame. |
| VE | S2 | Applied | VA:Cr1.2.7a is now taught as criteria: the unit 6 question, words, card, evidence, tools and rationale in 6 to 8, the year 7 year-end check and the seams line. The words line now reads "Set criteria a work must meet for its aim, and let them steer making." In row va-g7-ideas, "guideline" became "criteria" in the words cell and in both description clauses. |
| VE | M1 | Applied | 3 to 5: handling items are observed on making days from the record sheet's rotating list, never on a check day. VA:Cr2.2.4a is the tool-check gate record plus one making-day observation. The check-day table now serves only children answering aloud, and the teacher reads every prompt aloud once first. The Day kinds "Check" line matches. Notes were added to rows va-g3-craft, va-g4-craft and va-g5-craft. |
| VE | M2 | Applied | Words lines VA:Pr5.1.4a and VA:Re8.1.5a and line VA:Cn10.1.7a were replaced with the read's 14-word lines. Row va-g4-show got the read's description, and the video was dropped. Row va-g5-judge gained "visual elements". |
| VE | M3 | Applied | 9 to 12 seams sentence now reads: "The rows below match Visual Arts, grades 6 to 8's handed-on table and the Level 1 rows' `assumes` cells." The 3 to 5 clash list was replaced with the course-keyed list. The "labelled" and "open licence" items were dropped (3 to 5 old item 3, 9 to 12 old item 8). The 6 to 8 Standard bullet's stale "two rows" clause was replaced. The 6 to 8 works-unchecked item and the 3 to 5 words-line item were replaced with the settled lines. |
| VE | M4 | Applied | 9 to 12 Course-level checks: the curating unit "runs in weeks 24 or 25 to 32 (days 119 or 121 to 158), its show by day 155 and its respond days in week 32 beside the year-end check". The Grade 12 bullet now says a day-155 finish needs five merged days and a day-150 finish needs ten, and the show, critique, revision, checks and respond days never fold (with C-912 F5). |
| VE | M5 | Applied in part | The Lakota winter count (3 to 5 unit 4) and Hine (3 to 5 unit 12) are named in visual arts as planned links to media arts 3 to 5 unit 12 and media arts 6 to 8 unit 4. Media arts is not this job's file, so the swap choice is For the lead. Shaun Tan: the media arts 3 to 5 frame no longer names him (grep found nothing), so there is nothing to fix. Shared makers with different works (LeWitt, Mutu, Red Star) are cross-links for the unit plans, as the read says. |
| VE | m1 | Applied | 6 to 8 check-day minutes are stated one way: the Course-level checks paragraph follows the brief's check day. |
| VE | m2 | Applied | 9 to 12 Base text: "six Native makers or Native-led shows, in units 5, 9, 13, 18 and 19". |
| VE | m3 | Applied (C-912 F9's form) | 9 to 12 Day kinds now gives the 32-day unit: 8 understanding, 5 fluency, 14 application, 1 mid-unit check, 1 respond, 2 end checks and 1 respond. Longer units add days by load. |
| VE | m4 | Applied | 6 to 8 unit 9 free path is a card collagraph rubbing (cereal-box card, thickened tempera, spoon). 9 to 12 unit 7 food-tray plates: "never from raw meat or poultry". |
| VE | m5 | Applied | 6 to 8 unit 11: the Great Wall is "conceived 1974 and painted from 1976", and the unit plan confirms. It is gone from 3 to 5 (S1). |
| VE | m6 | Applied | 6 to 8 unit 7: Jaune Quick-to-See Smith "1940 to 2025". |
| VE | m7 | Applied | Row va-g1-craft: "practise" became "practice". |
| VE | m8 | Applied | 9 to 12 Readiness: "Level 4 has no review unit: a returning student's readiness check is ten minutes on unit 16's day 2, on the Level 3 guide." |
| VE | m9 | Applied | 9 to 12 unit 2: VA:Re7.1.Ia is "a short hypothesis", and its evidence is "the kept written hypothesis ... evidence from three panels". |
| VE | J1 | Kept | Paper web-page mock-up and paper tools in 3 to 5, as the read advises. The unit plans may offer a shared device in turns. |
| VE | J2 | Kept; question for Cory | No blades, so no linocut, until the safety agent's read (Questions, 3). |
| VE | J3 | Kept; question for Cory | Two levels in one room: the frame's pick stands (Questions, 2). |
| VE | J4 | Kept | Lawrence's Migration Series stays in grade 3 and Level 1. The 9 to 12 Base text names it as Level 1's entry work for a student new to the band. 6 to 8 now uses a different Lawrence work (S1). |

### Codex 3 to 5 (C-35)

| Read | # | Applied or kept | What changed, or why not |
|---|---|---|---|
| C-35 | 1 | Applied | Five ids widened. VA:Cr2.2.3a is observed across all three processes. VA:Re8.1.3a adds form (unit and year 3 year-end check). VA:Pr6.1.3a is a kept two-culture card. VA:Pr4.1.4a covers earlier, current and emerging technology. VA:Pr5.1.4a gives reasons plus paired cases. A note was added to row va-g4-show. |
| C-35 | 2 | Applied | The Cradle's reception claim was replaced with the museum's own account. The Tiébélé swap (S1) removed the other passage. |
| C-35 | 3 | Applied | Unit 9 scores materials use, never neatness. "Paper edges kept clean" became "shared paper protected". A deliberate rough edge is accepted when it serves the student's stated choice. A note was added to va-g5-craft. |
| C-35 | 4 | Applied | Reading load: three to five words taught in depth a unit. |
| C-35 | 5 | Applied | Both stale lead notes were rewritten (as VE M3). |

### Codex 6 to 8 (C-68)

| Read | # | Applied or kept | What changed, or why not |
|---|---|---|---|
| C-68 | 1 | Applied | VA:Cr1.2.7a is taught as criteria (VE S2). VA:Re8.1.7a covers ideas and mood: in the unit, the year-end check, the words line ("Find an artwork's ideas and mood from its making, form, structure, context, subject, media.") and row va-g7-judge ("to find its ideas and mood"). |
| C-68 | 2 | Applied | Five evidence lines widened. Unit 1 VA:Re7.2.6a gains a cultural association (unit and mid-year check). Unit 4 Pr4.1.6a covers three columns and Cn11.1.6a adds uses. Unit 8 Pr4.1.7a is a kept before-and-after card. Unit 12 Pr6.1.8a covers why, how, thoughts, beliefs and experience. |
| C-68 | 3 | Applied | Once-a-week unit 11 has a merged check with Re8.1.8a and Re9.1.8a scored apart. The rotations paragraph was rewritten so every id keeps its order and evidence. |
| C-68 | 4 | Applied | Free paths that bought or needed a set were fixed. Unit 1 runs on graphite. Unit 5 uses graphite plus found-paper collage. Unit 9 is a card collagraph (VE m4). |
| C-68 | 5 | Applied | Unit 6 perspective: Caillebotte's street has more than one vanishing point. One-point perspective is taught from a Curio Class diagram, and the painting is studied for its structure. |
| C-68 | 6 | Applied | The cross-band check is done (VE S1). Codex's Street to Mbari pick is used for unit 1. |
| C-68 | 7 | Applied | Reading load: three to five words in depth. |
| C-68 | 8 | Applied | Days: the middle school checklist (read 2026-11-25) gives no weekly minute minimum, so no gap is stated. The STANDARD.md 3.4 row is For the lead. Stale notes were rewritten. The 9 to 12 seams line was fixed (VE M3). The ADOPTION-BAR line is For the lead. |

### Codex 9 to 12 (C-912)

| Read | # | Applied or kept | What changed, or why not |
|---|---|---|---|
| C-912 | 1 | Applied | Level 4 units now require, with the ids named. Unit 16: a social-change hypothesis (Cr1.1.IIIa), justified material, method and convention choices (Cr1.2.IIIa, Cr2.1.IIIa), and revision against a traditional and a contemporary criterion beside the student's vision (Cr3.1.IIIa). Unit 17: shared features across a named group of works, always (Re7.2.IIIa), with reactions over time (Re7.1.IIIa). Unit 18: how a culture's images or objects shape lives (Cr2.3.IIIa) and the knowledge that steered the making (Cn10.1.IIIa). Unit 19: two or more preservation methods compared (Pr5.1.IIIa), an intended understanding for viewers (Pr6.1.IIIa), and an appraisal of an artist's effect on society (Cn11.1.IIIa). |
| C-912 | 2 | Applied | Placement: the sitting alone never places a student. The review unit fills a placement checklist of the level before's four processes, from brought work with a short account or a short task, scored on the level before's guides. This is in the Levels bullet and in the evidence of units 6 and 11. |
| C-912 | 3 | Applied | Unit 4: the model may be built alone, but the proposal is developed with a partner (a classmate from another team, or the home adult). The log records both people's ideas and one decision settled together. A look-for was added. A wholly solo proposal does not meet VA:Cr2.3.Ia. The Ordinary room bullet matches. |
| C-912 | 4 | Applied | Safety: "windows or a fan" was replaced. The label and safety data sheet are followed. Fresh air carries used air away from users. A fan that only stirs the air is not enough, and a room that cannot give fresh air uses the pencil or dry path. Units 2 and 12 point to it. |
| C-912 | 5 | Applied | Show weeks (VE M4) and the senior finish (155 needs five merged days, 150 needs ten, scope numbers the days). Level 4 short path: check on day 40 (week 8), respond on day 41 (week 9), in the Short path bullet and the checks paragraph. English contact: grade 11 unit 3 ends on day 55, so it overlaps unit 17's days 51 to 55. The fallback now applies whenever English has not taught it, on either path. |
| C-912 | 6 | Applied | Level 1 mid-year check: "a fresh unplanned pencil drawing with a short log of the decisions made while drawing (VA:Cr2.1.Ia)". |
| C-912 | 7 | Applied | Leave-out: "A student aged 18 or older gets the family note directly and makes their own leave-out and consent choices; the school's rules still apply." |
| C-912 | 8 | Applied | Seams line (VE M3). Old item 8 dropped. Days bullet: the high school checklist (read at source by the Codex read) gives no numeric minimum, so no gap is stated. For the lead item 5 now asks for the STANDARD.md 3.4 row. The ADOPTION-BAR line is For the lead. |
| C-912 | 9 | Applied | Day kinds 32-day example (as VE m3). |

### Visual arts counts and row edits

**Counts.** VE: 20 findings (S1 to S2, M1 to M5, m1 to m9, J1 to J4), with 15 applied, 1 in part (M5) and 4 kept
(J1 to J4, as the read advises). C-35: 5 applied. C-68: 8 applied. C-912: 9 applied. In all, 42 visual arts findings:
37 applied, 1 in part and 4 kept.

**arts.csv va rows edited (8).**
- va-g4-show: new description (VE M2) and a note (C-35 F1).
- va-g5-judge: adds "visual elements" (VE M2).
- va-g7-ideas: criteria in the words cell and both clauses (VE S2).
- va-g7-judge: "to find its ideas and mood" (C-68 F1).
- va-g1-craft: "practice" (VE m7).
- va-g3-craft, va-g4-craft and va-g5-craft: "Fix pass 2026-11-26" notes on handling observations, the VA:Cr2.2.4a
  record and materials use over neatness (VE M1, C-35 F3).

**Words-file lines changed (5):** VA:Cr1.2.7a, VA:Pr5.1.4a, VA:Re8.1.5a, VA:Re8.1.7a, VA:Cn10.1.7a.

### Pattern notes

- Every swap was grepped across docs/courses for a repeat before it was picked. Two of the read's own proposals would
  have repeated a work: The Harvesters (in K to 2) and an Asian conservation case (Mogao, in 3 to 5). A swap list
  needs that check too.
- Level 3 of 9 to 12 now has no African work after the Benin swap. The band still has El-Salahi, Mutu and Shonibare,
  and the unit 15 candidate asks for Africa or Asia. The Level 3 unit plans should pick the candidate if a level-by-
  level range is wanted.
- Visual arts 9 to 12 has a Level 4 short path (25, 14, 19 and 18 days), while dance 9 to 12 has none. Both follow
  their own frames. STANDARD.md 3.2 sets the 80-day path for Levels 1 to 3, so Cory's dance question 3 below applies
  to both.

## Visual arts: for the lead

1. **Works shared with media arts.** The Lakota winter count (visual arts 3 to 5 unit 4; media arts 3 to 5 unit 12)
   and Hine's child labor photographs (visual arts 3 to 5 unit 12; media arts 6 to 8 unit 4) are named in visual arts
   as planned links. Proposed: visual arts keeps both, since VA:Pr6.1.3a is about how cultures record history and
   Moran now carries unit 12 beside Hine. Media arts 3 to 5 swaps its winter count for another record of an event
   (for example a Plains ledger drawing, but not the one in visual arts 6 to 8 unit 7), or names the link both ways.
   This is not edited here.
2. **ADOPTION-BAR-SUBJECTS.md line 568 (arts row, shared doc).** Drop "the standards gate (later.csv L83)" and "load
   the 63 strand ids", both done 2026-11-21 (also in visual arts 9 to 12 For the lead 6, and in the dance section).
3. **STANDARD.md 3.4 (shared doc).** Fill the visual arts 6 to 8 Pending row from the middle school checklist (no
   weekly minimum, several schedules, so no gap), and add a visual arts 9 to 12 row from the high school checklist
   (regular instruction on a par with other academic subjects, semester and other schedules, no numeric minimum).
   Add the dance 9 to 12 row (dance section).
4. **Calendar clashes, for the one calendar pass.**
   - 3 to 5: grade 3 week 18 (PE), week 26 (computer science, dance, media arts, PE, SEL); grade 4 week 17 (dance,
     media arts, theater), week 25 (media arts); grade 5 week 18 (computer science, dance, ELD, media arts, PE,
     theater), week 26 (dance, PE, SEL).
   - 6 to 8: day 83 in week 17 is shared with dance, media arts and theater, with PE day 82 and health day 84 beside it.
   - 9 to 12: weeks 16 and 32, shared with health and PE; week 32 is the finals rule.
5. **DESK-ANSWERS lines.** None of these fixes is a new decision. If the lead records the swaps or the criteria
   wording, it is one log line.
6. **Facts to confirm at source.** Every 2026-11-26 swap is from memory: Pissarro, Tiébélé, the bandolier bag, Merian,
   Qian Xuan, Te Taiao, Moran, Street to Mbari, Berni, Dürer, Sherald and América Tropical. They are listed in each
   frame's For the lead. Each unit plan opens the item's own page for its rights line.
7. **Cosmetic.** One 6 to 8 line (the Standard bullet) runs past the wrap width. No gate checks it.

## Questions for Cory (visual arts)

1. **Supplies ceilings.** $75 a class a year for 3 to 5, $100 a class a year for 6 to 8 (year 8's print unit carries
   brayers and block ink), and $150 a class a level for 9 to 12. Every unit keeps its free path. Recommend: yes.
2. **Two levels in one room (9 to 12).** Many high schools teach Level 1 and Level 2 in one period. Recommend: the
   frame's pick. Each level keeps its own units and ids, and the two levels share the opening look and the critique
   days where their units sit side by side (unit 2 with unit 7, and so on). The scope and sequence marks the shared
   days.
3. **Linocut in Levels 2 and 3.** APPROACH "Safe use" keeps blades adult-only, so the frame prints with foam plates and
   collagraphs, while linocut is usual in high school. Recommend: keep blades adult-only for now. After the safety
   agent reads the two named guides, decide through APPROACH (with a DESK-ANSWERS line) whether Levels 2 and 3 may
   cut lino with a hand guard and a bench hook under an adult's watch.

## Dance, grades K to 12 (four frames)

Files changed: docs/courses/dance-grades-k-to-2/frame.md, dance-grades-3-to-5/frame.md, dance-grades-6-to-8/frame.md,
dance-grades-9-to-12/frame.md, data/progressions/arts.csv (da-* rows only, notes plus one spelling fix). Words file:
no line changed (no finding needed one).

### Dance expert read (DE), docs/reviews/frame-dance-grades-k-to-12-2026-11-25.md

| Read | # | Applied / in part / kept | What changed, or why not |
|---|---|---|---|
| DE | 1 | Applied | Stale For the lead notes rewritten as done in all four frames (K to 2 items 2, 3; 3 to 5 items 2 to 4; 6 to 8 items 1 to 4; 9 to 12 items 2, 6, 9). "Being written" and "not written" seam lines replaced. 9 to 12 seam cell now says "time-stamped or moment-named". PE frames' own stale lines listed for the lead (below). |
| DE | 2 | Applied | 9 to 12 bridge now shows Ella Lola, a la Trilby (1898, Edison studio, public domain), used in no other frame or data file (grepped docs and data). Its loc.gov record returned 403, so the unit plan confirms it as a browser check. K to 2 unit 1 names "Annabelle Whitford Moore". 9 to 12 unit 10's serpentine film is marked as not the Annabelle film. |
| DE | 3 | Applied | 6 to 8 names capoeira as a planned return both ways: Base text, the dance-here bullet, and a new PE table row (da-g7-connect, unit 8, against g8-culture-matters, PE unit 22). |
| DE | 4 | Applied | 9 to 12 unit 3 names PE grade 9 unit 5 with the boundary line. 6 to 8 unit 2 names PE unit 13 (canon and contrast are shared words with different purposes). "No motor cue" is gone from all four frames, replaced by: dance teaches the technique its own ids need and assumes no PE instruction. |
| DE | 5 | Applied | K to 2 unit 12: DA:Cn10.1.2b now uses a Kpanlogo excerpt (notice, meaning, wonder, one original move). The hoop dance stays watch-and-talk. |
| DE | 6 | Applied | arts.csv da-g2-technique: "travelling" changed to "traveling". da-g1-ideas had the same spelling and was fixed too. |
| DE | 7 | Applied | 3 to 5 course check: set-up 3, warm-up 2, written 10, showing 18, cool-down and reset 5, which is 38 minutes. At most two look-fors a student. |
| DE | 8 | Applied | Repeat lists corrected. 6 to 8 names Trisha Brown's return through Grand Union. 9 to 12 names Swan Lake (Masilo), the École des Sables (unit 9) and the serpentine return, and drops the absolute "none repeats" claim. |
| DE | 9 | Applied | 3 to 5 PE list now names the Virginia Reel, Alunelul, La Bastringue and its line dance, with Pilolo as a game. 6 to 8 now names cumbia, kolo and a line dance. |
| DE | 10 | Applied | One agent read label in all four frames: "safety (moving)" (K to 2: 12, 3 to 5: 12, 6 to 8: 12, 9 to 12: 19). |
| DE | 11 | Kept (lead) | PE 9 to 12 unit 5 already swapped the Virginia reel for bhangra. Nothing is left in dance. |
| DE | 12 | Applied | K to 2 unit 5 names La Raspa (PE K to 2 unit 13) both ways. |
| DE | other | Kept | Sankai Juku across 6 to 8 and 9 to 12 is acknowledged, as the expert advised. |

### Codex K to 2 (C-K2)

| Read | # | Applied / in part / kept | What changed, or why not |
|---|---|---|---|
| C-K2 | 1 | Applied | The narrowed ids are taught in full: Pr5.1.Kc (recall after the demonstration), Pr4.1.Ka (circle bigger and smaller), Pr4.1.1a and 1b (straight paths, return to a spot, how long moves take), and unit 9 (facing, body-part relations, count groups, unprompted spacing fix). Evidence matches. Row notes added. |
| C-K2 | 2 | Applied | Participation bullet: each unit plan maps the movement version to the look-fors it shows. A caller's or drummer's role counts only for what it shows, and an unseen action gets a short supported movement version. |
| C-K2 | 3 | Applied | Leave-out fallbacks: units 3, 7 and 11 change a Curio Class original sequence; units 4, 8 and 12 start from a fresh neutral starting point. Omitted ids stay unclaimed. |
| C-K2 | 4 | Applied | Unit 12's boundary: the movement is an original one prompted by the question, never imitation. The candidate cell asks for a sensitivity check of the excerpt. |
| C-K2 | 5 | Applied | Five-session merge map for year K unit 4 on the once-a-week path. |
| C-K2 | 6 | Applied | Stale notes rewritten (as DE 1). |

### Codex 3 to 5 (C-35)

| Read | # | Applied / in part / kept | What changed, or why not |
|---|---|---|---|
| C-35 | 1 | Applied | 16 additions in the owning units: Pr4.1.3b, Pr5.1.3c, Cr1.1.3a, Pr4.1.4a, Pr4.1.4b, Pr5.1.4b, Pr5.1.4c, Pr4.1.5a, Pr4.1.5c, Pr5.1.5b, Pr5.1.5c, Cn10.1.4b, Cn10.1.5a, Cn10.1.5b, Re9.1.4a, Pr6.1.5b. Row notes added. |
| C-35 | 2 | Applied | Participation evidence mapping, as C-K2 2. |
| C-35 | 3 | Applied | Leave-out fallbacks for units 4, 8, 11 and 12. |
| C-35 | 4 | Applied | Mid-year checks no longer score units 2, 6 or 10. Year-end swaps: Re9.1.3a to Cn10.1.3a, Cr2.1.4a to Cr1.1.4b, Cr2.1.5a to Cr1.1.5a. |
| C-35 | 5 | Applied | 38-minute check day (as DE 7). |
| C-35 | 6 | Applied | Short-path merge map for unit 12 keeps its required order. |
| C-35 | 7 | Applied | Retrieval is a separate ten-minute block on day 2, after the warm-up, with one combined reteach. Feedback-loop is first used in unit 1's critique. |
| C-35 | 8 | In part | Safety guide URLs added (Nova Scotia, the dance educators' opportunity-to-learn standards). Deferred work picks stay with the unit plan, which links each item on its own page after its rights check. No URLs were written from memory. |
| C-35 | 9 | Applied | Cited assessment windows moved to each unit's third-last and second-last days, so the respond day stays free (units 2, 3, 6, 7, 10, 11). |
| C-35 | 10 | Applied | Stale notes rewritten. |

### Codex 6 to 8 (C-68)

| Read | # | Applied / in part / kept | What changed, or why not |
|---|---|---|---|
| C-68 | 1 | Applied | Teaching and evidence extended: Pr5.1.6a to 6c, Pr5.1.7a, Pr4.1.8b, Re8.1.6a, Re8.1.7a, Re8.1.8a, Re7.1.8a, Pr6.1.8a, Cn11.1.6a (written and shown), Cn10.1.7b (lecture demonstration), Cn10.1.8b (one study, two methods, new understanding), Cn11.1.7a (likenesses and community views). Row notes added. |
| C-68 | 2 | Applied | Floor rule in all four frames: resilient surface; low and no-impact on an unsuitable floor; the look-for is seen in a suitable space, never from a written stand-in. 6 to 8 and 9 to 12 add rotating traveling lanes. |
| C-68 | 3 | Applied | Participation evidence mapping. |
| C-68 | 4 | Applied | Feedback-loop, look-and-say, describe-interpret, performing-space and etiquette are now first modeled or retrieved in unit 1. |
| C-68 | 5 | Applied | Ten-minute day 2 retrieval block (set-up 3, warm-up 5, retrieval 10, teaching 15, cool-down 4, room back 3), one combined reteach, kept on the once-a-week path. |
| C-68 | 6 | Applied | Fallbacks for units 3, 7, 11 and 12. |
| C-68 | 7 | Applied | Mid-year checks now score earlier-unit ids only: year 6 Pr5.1.6a, year 7 drops the unit 6 study, year 8 Pr4.1.8b. |
| C-68 | 8 | Applied | Capoeira row, boundary wording and the PE unit 13 line (as DE 3 and 4). |
| C-68 | 9 | In part | Weave dated as a 2018 to 2020 project, premiered January 2019. The step team, the Sankai Juku work and the Moiseyev piece stay unit plan picks after a rights check on their own pages. Links are left to the unit plan (no URLs from memory). |
| C-68 | 10 | Applied | Stale notes rewritten. The week 17 calendar note now gives PE day 82, health day 84 and the other arts on day 83; week 32 is the finals rule. |

### Codex 9 to 12 (C-912)

| Read | # | Applied / in part / kept | What changed, or why not |
|---|---|---|---|
| C-912 | 1 | Applied | Floor rule (as C-68 2), with jumps, leaps, rolls and slides named. |
| C-912 | 2 | Applied | Additions in units 2 (Pr4.1.Ia, Ib, Pr5.1.Ia, Ic), 5 (Cn10.1.Ib compared with another field's procedure), 7 (Pr5.1.IIb live, IIc carried out), 8 (Cr1.1.IIb, Cr2.1.IIb performed), 12 (Pr4.1.IIIa to IIIc, Pr5.1.IIIa), 14 (Cr3.1.IIIa criteria), and 15 and 19 (Cn11.1.IIIa). Row notes added. |
| C-912 | 3 | Applied, plus a Cory question | The Standard bullet now promises reassessment of the 11 ids only. New For the lead 10 lists the ten others and the expansion plan. |
| C-912 | 4 | Applied | Boundary wording from the read. Units 2 and 3 name PE grade 9 unit 5, and the PE cross-subject cell was rewritten. |
| C-912 | 5 | Applied | Year-end sittings no longer claim Cr2.1.Ib, Cr2.1.IIa or Cr2.1.IIIa from unseen dances. Level 3 mid-year self-evaluation uses the student's own unit 12 showing. Unit 16 is scored once, at checkpoint 1 (days 71 and 72). Checkpoint 2 swaps the unit 18 self-evaluation for Re8.1.IIIa. |
| C-912 | 6 | Applied | Fallbacks for units 4, 10 and 17 to 19. Supplied work never recovers omitted creating ids. "Each unit stands alone" removed. |
| C-912 | 7 | In part | The Statement is now made for a Dutch company's dancers and premiered in The Hague, 2016, with the company's work page linked (URL taken from the read). Pite is named as a Canadian choreographer. The bridge swap and repeat claims are fixed as DE 2 and 8. Other fixed works' links are left to the unit plan. |
| C-912 | 8 | Applied | 45-minute day 2 block: 3, 7, 10, 18, 4, 3. One combined reteach inside the teaching time; same block on the short path. |
| C-912 | 9 | Applied | Leave-out: a student aged 18 or older receives the family note directly and makes their own leave-out and consent choices. |
| C-912 | 10 | Applied | For the lead 6 marked done, with the leftover PE items listed. Item 2 now states the opportunity-to-learn high school lines the read opened. The seam cell is fixed. The ADOPTION-BAR line is for the lead (below). |

**Counts.** DE: 12 numbered, 11 applied, 1 kept (DE 11, already fixed in PE); other judgment calls kept. C-K2: 6 applied.
C-35: 9 applied, 1 in part. C-68: 9 applied, 1 in part. C-912: 9 applied (one with a Cory question), 1 in part. In
all, 54 findings: 48 applied, 3 in part, 1 kept, plus the DE judgment calls kept as advised.

**arts.csv rows edited (38).** Notes appended ("Fix pass 2026-11-26: ..."), with no id moved or renumbered:
- K to 2: da-k-technique, da-k-elements, da-g1-elements, da-g2-elements, da-g2-connect.
- 3 to 5: da-g3-ideas, da-g3-elements, da-g3-technique, da-g4-elements, da-g4-technique, da-g5-elements, da-g5-technique, da-g4-respond, da-g4-connect, da-g5-connect, da-g5-stage.
- 6 to 8: da-g6-technique, da-g7-technique, da-g8-elements, da-g8-stage, da-g6-respond, da-g7-respond, da-g8-respond, da-g6-connect, da-g7-connect, da-g8-connect.
- 9 to 12: da-g9-elements, da-g9-technique, da-g9-connect, da-g10-technique, da-g10-ideas, da-g10-form, da-g11-elements, da-g11-technique, da-g11-revise, da-g11-connect.
- Spelling fix: da-g2-technique and da-g1-ideas ("traveling").

**Words-file lines changed:** none.

### For the lead (dance)

- **PE K to 2:** near line 287 it still says the dance K to 2 frame is not written.
- **PE 3 to 5:** its middle cross-subject cell's row ids need fixing to match dance's rows (dance 3 to 5 For the lead 2).
- **PE 6 to 8:** its Cross-subject row-id cell should also name da-g6-technique, da-g7-technique and da-g8-technique. Its capoeira row already names dance both ways.
- **PE 9 to 12:**
  - Near line 377 it says the dance and SEL 9 to 12 frames are not written.
  - Its unit 5 cell should name dance unit 3 (Level 1 course days 51 to 84).
  - Unit 5's question ("says something") and its "stated idea" step belong to dance. PE keeps the phrase as a movement problem.
- **ADOPTION-BAR-SUBJECTS.md line 568 (arts row):** replace the outstanding standards-gate and music-loading tasks with a statement of completion, consistent with arts STANDARD.md. This is a shared file.
- **STANDARD.md 3.4:** add a dance 9 to 12 row. The opportunity-to-learn lines say Proficient and Accomplished get 60 to 90 minutes at least three times a week, and Advanced a typical 90-minute class. Compare the frame's 45-minute daily periods by weekly total.
- **Calendar clashes (listed, not counted):**
  - Week 17 holds dance's day 83 with visual arts, media arts and theater, PE's day 82 and health's day 84, all in grades 6 to 8.
  - Week 32 in 9 to 12 is the finals rule.
  - The K to 2 and 3 to 5 clash lists stay in their For the lead item 1.
- **Shared with music, theater or media arts:** none found. Kpanlogo, the serpentine films and Ella Lola appear only in dance frames, so no swap is needed.
- **CRLF:** the four dance frames read as LF on disk (0 CR characters), and the edit helper kept each file's own endings. The parent may want to check whether CRLF was expected.

### Questions for Cory (dance)

1. **Supplies ceiling:** $50 a class a year for K to 8 dance and $75 a class a level for 9 to 12, every unit keeping its free path. Recommend: yes.
2. **Filmed phrase set:** whether Curio Class should film its own step-card phrases. Recommend: keep teacher-danced originals from step cards for now, and revisit when voice and art work runs.
3. **Level 4 short path:** Level 4 has none, since STANDARD.md 3.2 sets the 80-day path for Levels 1 to 3. Recommend: leave it so.
4. **Level 4 recovery scope:** keep the limited promise (11 Advanced ids reassessed), or add recovery for the other ten ids. Recommend: the limited promise, as the frame now states.

## Sources read for this pass

- The eight reads named at the top, and the model fix report (frame-visual-arts-grades-k-to-2-fixes-2026-11-25.md).
- docs/courses/arts/STANDARD.md (3.2, 3.4) and APPROACH "Safe use", for the rules the fixes cite.
- The other arts and PE frames, read only (and grepped) to find repeated works and stale cross-references. None of
  them was edited.
- The national visual arts standards' grade and high school lines, through data/standards/ (the ids' words-file lines),
  and the Codex reads' quoted standard text for the Level 4 additions.
- No outside page was fetched in this pass. The opportunity-to-learn facts come from the Codex reads, which opened
  them at source on 2026-11-25. The dance bridge film's loc.gov page returned 403 to the dance fork and is marked as
  a browser check. Work facts for the swaps are from memory and listed for the unit plans to confirm.
