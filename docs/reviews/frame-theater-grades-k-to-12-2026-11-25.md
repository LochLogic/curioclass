# Frame read: Theater, grades K to 12 (four band frames), 2026-11-25

Expert cold read, one combined read of the four theater frames written 2026-11-25. Brief:
docs/pipeline/briefs/frame-read.md with the after-core changes (arts subject, combined read, seams, same-band arts
repeats, stagger clashes listed but not counted). Rules per docs/agents/EXPERT.md.

## What was read

- AGENTS.md; docs/pipeline/briefs/frame-read.md; docs/agents/EXPERT.md; docs/agents/lenses/arts.md.
- docs/courses/arts/STANDARD.md (band-year rule, levels rule, 3.4 time figures; theater has no figure) and
  docs/courses/arts/APPROACH.md (rights, scoring creative work).
- The four frames in full: docs/courses/theater-grades-k-to-2/frame.md, theater-grades-3-to-5/frame.md,
  theater-grades-6-to-8/frame.md, theater-grades-9-to-12/frame.md.
- data/progressions/arts.csv, all 98 th-* rows, and the 2026-11-21 backup
  (X:/_preconsolidation-2026-11-24/CurioClass/data/progressions/arts.csv) to diff today's row changes.
- data/standards/ncas-performance-standards.txt (theater ids, by id only).
- docs/CALENDAR.md (stagger rules 3 and 4, the stagger-break list at line 270).
- Same-band arts frames for repeated picks: music, dance, visual arts and media arts, K to 2, 3 to 5, 6 to 8 and
  9 to 12 (searched by name for every theater pick); ELA frames searched for the plays the theater frames use.
- docs/ADOPTION-BAR-SUBJECTS.md arts row; data/plans/later.csv L83.
- Gates run: scripts/frame.py check (all four pass, 0 failures, days add up); scripts/plan.py check (no theater
  failures); scripts/stale.py check (121 files, 0 failures).

## Verdict

All four frames are sound and buildable: day arithmetic, unit ranges, check weeks, short paths and the K to 12
seams all hold, every NCAS theater id is placed once in its own year or level, and today's 42 row-note changes
landed exactly as the frames say. K to 2 and 3 to 5 are ready after small fixes; 6 to 8 and 9 to 12 each carry one
false "no repeat" claim that hides a real cluster of repeated makers (kyogen, commedia, Kamiriithu, Appia,
Stanislavski, Spolin, Chaplin, Shakespeare, Arena Stage) and, in 6 to 8, The Importance of Being Earnest, which is
an ELA grade 12 anchor read whole. Fix the repeats (swap or name as a deliberate revisit) and the frames can go to
unit plans.

## Row changes: did they land?

Yes. A field-by-field diff of the th-* rows against the 2026-11-21 backup shows exactly 42 rows changed, all in
`notes` only, matching each frame's stated count:

- K to 2 (12): th-k-design, th-k-story, th-k-world; th-g1-actor, -design, -story, -world, -notice; th-g2-design,
  -story, -world, -notice.
- 3 to 5 (12): design, story, world, judge for each of grades 3, 4, 5.
- 6 to 8 (18): actor, design, story, world, notice, judge for each of grades 6, 7, 8.
- 9 to 12: none (the frame lists none).

No em dash in any th note. Residual narrow notes are minor finding m5.

## Findings

Confidence: high = checked against the file or source; medium = checked in part; low = judgment from reading.

### Serious

None.

### Moderate

**M1. Cross-band repeats inside theater, under a "no repeat" claim checked only against K to 2.**
LAYER frame. REPEAT new. Confidence high.
- What is wrong: theater 6 to 8 (line 75) says "No pick repeats a K to 2 theater work" and checks only K to 2.
  Against theater 3 to 5 it repeats: kyogen (3 to 5 unit 2, 6 to 8 unit 1, both for walk and voice); commedia
  dell'arte (3 to 5 unit 1, the Scala scenarios; 6 to 8 unit 2, Goldoni and a commedia print); Kamiriithu (3 to 5
  unit 11, 6 to 8 unit 8, the same theater-for-a-cause use, the closing and Ngugi's detention told twice); Adolphe
  Appia (3 to 5 unit 7, 6 to 8 unit 3, both for light); Stanislavski (3 to 5 unit 5, 6 to 8 unit 9); Viola Spolin
  (3 to 5 unit 1, 6 to 8 unit 9); Chaplin (3 to 5 unit 6, The Gold Rush; 6 to 8 unit 1, the 1916 film). The 9 to
  12 frame (line 350) says "none repeats a lower band's maker", but Shakespeare is in 3 to 5 (A Midsummer Night's
  Dream, the First Folio) and 6 to 8 (the Globe), and Arena Stage is in 6 to 8 unit 11 and 9 to 12 unit 14.
- Why it matters: the world-range rule asks for range across the whole K to 12 ladder; a student meets the same
  maker making the same point twice, and the Kamiriithu story (a detention) is retold at two ages for the same
  standard. Japan's nogaku also runs across three bands (kyogen twice, Noh in 9 to 12), plus kabuki and bunraku
  elsewhere, which weights Japan heavily.
- Fix: in 6 to 8, swap kyogen for a living physical-theater maker from Africa or Latin America; swap Kamiriithu
  in one band (a fit: Sistren Theatre Collective of Jamaica, a women's company making plays from members' lives);
  swap Appia in 6 to 8 for a lighting maker no other band uses (9 to 12 unit 4 already has Svoboda and Rosenthal,
  so not those). Commedia, Stanislavski, Spolin and Shakespeare may stay if the later frame names each as a
  deliberate revisit with a different job (for example 6 to 8 commedia as Goldoni's written comedy, not the
  improvised scenario). Rewrite both claims to check against every lower theater band. Move Chaplin per M2.

**M2. Chaplin three times across arts, twice in grades 6 to 8.**
LAYER frame. REPEAT new. Confidence high.
- What is wrong: theater 3 to 5 unit 6 (The Gold Rush, 1925), theater 6 to 8 unit 1 (a 1916 short) and media arts
  6 to 8 (The Kid, 1921, its Cr3/Re8 unit). Same maker, same band, two arts.
- Why it matters: the same-band repeat check exists so a grade 6 to 8 student does not meet one maker as the anchor
  in two arts courses; Chaplin is also the only public domain film in either theater frame.
- Fix: in theater 6 to 8 unit 1, replace Chaplin with another public domain silent physical performer (Buster
  Keaton, a 1920s short public domain in the United States, or Harold Lloyd), or drop the film and use a living
  clown company's own page.

**M3. The Importance of Being Earnest in theater 6 to 8 is an ELA grade 12 anchor.**
LAYER frame. REPEAT new. Confidence high.
- What is wrong: theater 6 to 8 unit 9 (line 305) adapts Lady Bracknell's interview from Earnest. ELA grade 12
  (frame line 11 and unit at line 117) reads Earnest whole as the comic pair to Hamlet. The theater 9 to 12 frame
  (line 352) avoids it for exactly this reason, so the band below breaks the rule its own subject set.
- Why it matters: the scene is the play's best-known moment; meeting it adapted in grade 7 or 8 spends the found
  handbag and the interview before the grade 12 read.
- Fix: replace with another public domain comedy-of-manners scene not used by any ELA frame (for example Sheridan,
  The Rivals, a Mrs. Malaprop scene, or Goldsmith, She Stoops to Conquer), after a grep of the ELA frames for the
  replacement. Add the ELA anchor list to the 6 to 8 lead item as 9 to 12 has it.

**M4. Kamishibai in both theater K to 2 and media arts K to 2.**
LAYER frame. REPEAT new. Confidence high.
- What is wrong: theater K to 2 uses kamishibai in units 1, 2 and 5; media arts K to 2 uses it in its unit 3 and a
  year 2 revisit. Same band, same form, both as picture-sequence storytelling.
- Why it matters: same-band repeat across arts; a K to 2 child would meet kamishibai as a new form in two courses.
- Fix: keep it in one course. Theater has the stronger claim (it is performed, the teller's voice and the
  sliding cards); media arts can swap to another sequence form (for example a Chinese lianhuanhua picture book or
  a Mexican fotonovela page). If both stay, each frame names the other and the second use is a revisit, not an
  introduction. This is a joint call with the media arts frame owner.

### Minor

**m1. Repeated unit title.** LAYER frame. REPEAT new. Confidence high. "One story, many tellings" is the title of
K to 2 unit 12 (line 254) and 3 to 5 unit 12 (line 292). Fix: retitle 3 to 5 unit 12 (for example "Same story,
new eyes").

**m2. "Two silent films" names one.** LAYER frame. REPEAT new. Confidence high. 3 to 5 Base text bullet (line 63)
says "two silent films public domain" and names only The Gold Rush. Fix: name the second film with its unit, or
say "one".

**m3. Ngugi's detention date.** LAYER frame. REPEAT new. Confidence medium (from general sources, not reopened
today). 3 to 5 lead item (line 372) and unit 11 say the 1978 detention; it began 31 December 1977 and ended
December 1978. Fix: "held without trial from the last day of 1977 through 1978". If Kamiriithu is swapped out of
3 to 5 per M1, the point falls away.

**m4. Stale ordering note on the national time figure.** LAYER process. REPEAT yes (the figure has been owed
since the 2026-11-20 prework read). Confidence high. K to 2 (around line 319) asks for the Educational Theatre
Association opportunity-to-learn document to be read "before the theater 3 to 5 and 6 to 8 frames"; those are
written. 3 to 5 (line 360) and 6 to 8 (lines 376 to 379) each carry the same owed read; 6 to 8 notes a middle
school figure of at least 45 minutes a day (about 67 hours against the course's 43). All three frames state no
figure meanwhile, so they agree. Fix: one read at source by the lead (it needs a download), then one line in
STANDARD.md 3.4 and drop the three lead items; reword the K to 2 item now so it does not point at past frames.

**m5. Progression notes narrower than the frame's evidence.** LAYER progression. REPEAT new. Confidence high.
The "Assessed by" note names one form where the frame's evidence line uses two or a different one (the frame
governs, so nothing breaks): th-k-actor; th-k-notice (spoken reaction, but TH:Re7.1.Ka is also a kept audience
card); th-g1-show and th-g2-show (vote cards); th-g2-actor (TH:Pr5.1.2a is a talk item); actor, notice and show for
grades 3, 4 and 5; all 9 to 12 rows. Also the 6 to 8 notes are identical across grades 6, 7 and 8 and name "grade 7
/ grade 8" inside the grade 6 rows. Fix: one sweep aligning each note to its frame's evidence line, with grade 6
notes naming grade 6 only.

**m6. Stale "Owed: the standards gate" in the arts row.** LAYER process. REPEAT yes. Confidence high. The 9 to 12
lead item says the ADOPTION-BAR-SUBJECTS.md arts row (line 568) still says "Owed: the standards gate (later.csv
L83)"; it does, and later.csv L83 is done (2026-11-21). The frame's item is right. Fix: the lead drops that clause
from the row (not a frame change).

### Judgment calls

**J1. Japan weighting.** Even after M1, Japan appears in K to 2 (kamishibai, bunraku), 3 to 5 (kyogen), 6 to 8
(kyogen, kabuki) and 9 to 12 (Noh, Zeami, Ninagawa if kept). The forms are real and distinct, and Japan's theater
heritage is deep, so this is defensible; but Africa and Latin America have fewer named forms per band. Pick: after
the M1 swaps, count named forms per region per band and add one Latin American form in 6 to 8 (for example
Teatro Experimental de Cali or Yuyachkani of Peru, both living companies with their own pages).

**J2. Shakespeare in three bands.** Midsummer in 3 to 5, the Globe in 6 to 8, Macbeth in 9 to 12. Shakespeare is
the one maker most schools expect at every level, and each use has a different job (a comedy retold, a playhouse
studied, a tragedy performed). Pick: keep all three, fix only the 9 to 12 claim wording per M1.

**J3. 9 to 12 supplies ceiling.** $150 a class a level is three to four times the lower bands. It is plausible for
lighting gels, a small LED kit and makeup, but it is a money line, so it is listed For Cory.

## Calendar clashes (listed, not counted)

Theater appears in these entries of the CALENDAR.md stagger-break list (line 270); the lead's calendar pass owns
them:

- Grade K: week 19 (with music); week 27 (computer science, health, library, media arts).
- Grade 1: week 27 (computer science, health, media arts).
- Grade 2: week 17 (dance, ELD, music, PE, visual arts); week 27 (ELD, health, library, media arts, PE).
- Grade 3: week 17 (dance, media arts); week 27 (ELD).
- Grade 4: week 17 (dance, media arts, visual arts); week 26 (dance, PE, SEL).
- Grade 5: week 18 (computer science, dance, ELD, media arts, PE, visual arts).
- Grades 6, 7, 8: day 83 (dance, media arts, PE, visual arts).
- 6 to 8 year-end checks in week 32 are legal (rule 3: week 32 is finals and may hold every subject's year-end
  check); 9 to 12 week 32 is finals (rule 4).

The K to 2 frame's own list of sharing weeks is incomplete against this list (it omits grade K week 19 with music
and media arts in week 27); the calendar pass should treat CALENDAR.md as the record.

## Settled by the expert

| Question | Settled |
|---|---|
| Do the day counts and check weeks hold? | Yes, all four, by frame.py and by hand: K to 2 and 3 to 5 years of 60 unit days plus checks; 6 to 8 units of 18, 14, 14, 14; 9 to 12 Levels 1 to 3 with bridge 12 or review 6 plus 34/35, 45, 42; Level 4 38, 38, 25, 22, 33. |
| Is every theater id placed once in its own year or level? | Yes; K 17 ids, grades 1 to 8 24 each, 24 per level, Level 4 reassessing `.III`. |
| Do the band seams match the progression? | Yes; each frame's "Handed on" rows match the next band's `assumes` and the `hands_on` cells. |
| Did today's row changes land? | Yes, 42 notes-only changes, counts match the frames. |
| Are the 6 to 8 week-32 year-end checks a clash? | No, legal under CALENDAR.md rule 3. |
| Is media arts K to 2 shadow work a repeat of theater's Chinese shadow puppetry? | No; it is Lotte Reiniger's cut-paper animation, a different form and job. |
| Are griot (music 3 to 5), Cinderella (media arts 3 to 5, Melies) and Roadside Theater / broadside (media arts 3 to 5, Posada broadside) repeats of theater 3 to 5? | Griot: music 3 to 5 uses kora players from griot families for sound; theater uses the jeli as tellers and the Sosso-Bala; overlapping culture, different job, acceptable if each names the other. Cinderella: different tellings (Melies film vs Ye Xian / Zuni retellings), acceptable. "Roadside" and "broadside" are not the same work. |
| Are Gregory Maqoma (dance 9 to 12) and Lady Gregory (theater 9 to 12) a repeat? | No, different makers. Ming Cho Lee is not in theater. |

## What is right and should not be touched

- The seam tables in all four frames ("Handed on" / pick-ups); they are the clearest in the arts set.
- The 9 to 12 levels arithmetic and the bridge/review pattern; the Level 4 reassessment layout.
- The rights posture: works described in Curio Class's words and linked to the maker's own page, retellings of
  public domain texts credited, no copying or embedding.
- The cultural care lines (no student dresses as a real people; the maker's own published words read first).
- The ELA cross-subject tables in every band and the 9 to 12 ELA anchor avoidance list (extend it down to 6 to 8).
- The once-a-week and short-path session counts.

## What I could not judge

- The two 9 to 12 safety guides that are PDFs were not opened (a download), so their fit is unchecked.
- The Educational Theatre Association opportunity-to-learn figure (a download).
- Whether every linked maker's page is live; spot checks only, no fetches today.
- Rights lines on the 9 to 12 recorded productions (each needs its own page at unit-plan time).

## For Cory

- Money: supplies ceilings of $40 a class a year (K to 2), $40 (3 to 5), $45 (6 to 8) and $150 a class a level
  (9 to 12). The 9 to 12 figure is the one to look at.
- Downloads the lead would need (none done): the Educational Theatre Association opportunity-to-learn standards
  (schooltheatre.org); the two 9 to 12 safety guide PDFs named in that frame's Safety read bullet.

## For the source list

- Sistren Theatre Collective (Jamaica), candidate swap for Kamiriithu.
- Yuyachkani (Peru) and Teatro Experimental de Cali (Colombia), candidate Latin American companies for 6 to 8.
- Sheridan, The Rivals, and Goldsmith, She Stoops to Conquer, public domain comedy-of-manners candidates for the
  6 to 8 Earnest slot.
- Buster Keaton and Harold Lloyd shorts (public domain in the United States), candidates for the 6 to 8 Chaplin slot.

## Sources

The frames, arts.csv and its 2026-11-21 backup, STANDARD.md, APPROACH.md, CALENDAR.md, ADOPTION-BAR-SUBJECTS.md,
later.csv, the other arts frames and the ELA grade 12 frame, all in S:\CurioClass. Work facts (dates, makers) were
checked from general knowledge; no web fetch was made.
