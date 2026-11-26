# Expert read: music frames, kindergarten to grade 12 (2026-11-25)

A cold read of the four Curio Class music frames as one combined read, by the brief
docs/pipeline/briefs/frame-read.md with the after-core changes (subject arts, mu-* rows).

## What was read

- AGENTS.md; docs/pipeline/briefs/frame-read.md; docs/agents/EXPERT.md; docs/agents/lenses/arts.md.
- docs/courses/arts/STANDARD.md (sections 3.1 to 3.4) and docs/courses/arts/APPROACH.md.
- The four frames: docs/courses/music-grades-k-to-2/frame.md, music-grades-3-to-5/frame.md,
  music-grades-6-to-8/frame.md, music-grades-9-to-12/frame.md.
- data/progressions/arts.csv (all 100 mu-* rows), data/plans/frames.csv, data/plans/calendar.csv,
  the stagger list in the calendar doc, data/standards/ncas-performance-standards-words.txt (music lines).
- The other arts frames of each band (visual arts, media arts, theater, dance), searched for repeated
  works and check weeks.
- docs/reviews/frame-visual-arts-grades-k-to-2-fixes-2026-11-25.md (the pilot's pattern notes).
- docs/ADOPTION-BAR-SUBJECTS.md, arts row.
- Script checks run read only: scripts/plan.py check (0 failures for all music frames), scripts/stale.py
  check, plus an id-coverage pass of my own over the rows and the id file.

## Verdict

The four frames are sound and buildable: every owned id sits in exactly one row and is taught at least
twice in its unit, the day arithmetic and short paths add up, and the three seams tables match row for row.
No finding is serious. The weak spots are bookkeeping and facts: notes that point at a "Row changes" section
none of the frames has, several works and makers that repeat across bands against the frames' own
"no work repeats" claim, two words-line questions that need a browser check at the source, and one rights
claim that is likely wrong.

- K-2: sound; fix the stale pointers and the Kb question.
- 3-5: sound; fix the stale ELA table line and the Cr1.1.3b wording; two judgment calls on order.
- 6-8: sound; fix the Ives rights claim and the stale tool note.
- 9-12: sound; swap or name the revisits from earlier bands; two small wording fixes.

## Row changes landed

All landed in data/progressions/arts.csv:

- mu-k-choose and mu-g1-choose: Cn10 wording with a story-character or public option. Landed.
- mu-g6-choose, mu-g7-choose, mu-g8-choose: end "Every personal tie has an invented or public option
  beside it, marked the same". Landed.
- mu-g5-respond cross_subject: "ela:W.4.1 (an opinion supported by reasons, taught the year before)". Landed.
- Not changed and worth a look: mu-g2-choose has no public option in its row (see finding 11).

## Findings

Counts: serious 0, moderate 6, minor 6, judgment call 2.

### Moderate

**1. Stale notes point at a section that does not exist.**
LAYER: process. REPEAT: new. Confidence: firm.
Evidence: K-2 "For the lead" item 3, the 3-5 ELA table note and 6-8 "For the lead" item 3 each say
"see Row changes", but none of the four frames has a Row changes section, and the changes have now landed.
The 3-5 ELA table still lists "mu-g5-respond, ela:W.5.1"; the row now says W.4.1, so a builder reading the
table would pin the wrong standard. HS "For the lead" item 5 says the 6-8 frame "is being written"; it
exists and its seam matches. 6-8 "For the lead" item 2 says stale.py flags the 3 to 5 Pending line; it now
flags only physical education. The 3-5 note that "the music expert read checks the two tables" is done.
Cost of leaving it: a writer builds from a wrong ELA id or chases a missing section.
Change: replace each "see Row changes" with "landed in data/progressions/arts.csv 2026-11-25"; set the 3-5
table line to ela:W.4.1; drop the HS "is being written" and 6-8 stale.py notes and the 3-5 "expert read
checks" note.

**2. Works and makers repeat across music bands, against the frames' own claim.**
LAYER: frame. REPEAT: new. Confidence: firm.
Evidence: Florence Price, Symphony No. 1 "Juba Dance": K-2 unit 12 and HS unit 4. Jerod
Impichchaachaaha' Tate: 3-5 unit 11 and HS unit 4. "Shenandoah": 3-5 unit 5 (menu) and HS unit 10.
Dvořák, New World Symphony with Burleigh: 3-5 unit 5 and HS unit 14. Makers repeat too: Joplin (K-2 unit 9,
The Entertainer; HS unit 1, Maple Leaf Rag), Mozart (K-2 unit 10; HS unit 8), Beethoven (K-2 unit 3,
3-5 unit 9, HS unit 13). The 3-5 and 6-8 frames state that no work repeats from an earlier band.
Cost: the lens asks for works from many places across the years; repeats narrow the catalog and make the
claim false.
Change: for each, either swap in a new work (keeping the place and period the unit needs), or keep it and
name it as a revisit at a new depth ("first heard in grade K; here studied for form"). Then correct the
"no work repeats" lines to match. My pick: keep Price and Dvořák as named revisits (the HS units study
them at real depth), swap "Shenandoah" and the Tate piece at HS for unheard works.

**3. MU:Cr1.1.3b words line has likely drifted from the national text.**
LAYER: standard. REPEAT: new. Confidence: likely (from memory; needs the source).
Evidence: the words line reads "Invent rhythm and melody ideas inside a chosen tonality or meter." From
memory the national text says "within a given tonality and/or meter". "Chosen" hands the student the pick,
which is a different skill. It feeds 3-5 unit 2, the year 3 mid-year check, row mu-g3-invent and the K-2
hand-on table.
Change: browser check of the music "at a glance" handout; if confirmed, fix the words line to "given" and
have unit 2 teach the student naming the given tonality or meter before inventing in it.

**4. MU:Cr2.1.Kb may be missing from the id file.**
LAYER: standard. REPEAT: new. Confidence: likely (from memory; needs the source).
Evidence: the MU:Cr2.1.Ka words line folds the pick and the organize actions together. From memory a
separate Kb exists (organize personal musical ideas with iconic notation or recording, with guidance).
If so, K is 19 ids, not 18, and the band 59.
Change: browser check at the same handout. If Kb exists: add it to the id file and the words file, set it
as mu-k-document's standard, change the counts in STANDARD.md 3.1 and the K-2 frame to K 19 / band 59,
and name it in K-2 unit 3 with its evidence line.

**5. The Ives score is called public domain.**
LAYER: frame. REPEAT: new. Confidence: likely.
Evidence: 6-8 unit 7 calls Ives's Variations on "America" "a public domain score". It was written about
1891 but first published in 1949, so the printed score is likely still in copyright in the US.
Change: "described and linked" with a rights check before any copy is made; use a recording the class
can stream, and the 1891 public-domain hymn tune itself for the variation work.

**6. The ADOPTION-BAR arts row still owes items the frames depend on.**
LAYER: process. REPEAT: yes (the visual arts pilot raised it).
Confidence: firm.
Evidence: HS "For the lead" item 6 and docs/ADOPTION-BAR-SUBJECTS.md say the standards gate (later.csv L83)
and "load the 63 strand ids when the high school music frame is written" are still owed. The HS frame is
now written and the strand ids pass scripts/standards.py, so the second item is likely done but not
recorded.
Change: the lead records the strand-id load as done in the arts row and leaves L83 as the one open item.

### Minor

**7. HS "both finals weeks" for week 16.**
LAYER: frame. REPEAT: new. Confidence: firm.
Week 16 is a finals week only for a half-year course (rule 4), which here means the short path. Change: "week 32, and week 16 on the
short path".

**8. Pending anchor with no target.**
LAYER: frame. REPEAT: new. Confidence: firm.
The HS frame's Pending(docs/courses/arts/STANDARD.md#Music, high school) points to a heading that does not
exist; the music time text is in 3.4. Change: point it at the 3.4 heading, and keep the Pending until a
high school music time source is named (see "What it could not judge").

**9. Ella Jenkins dates.**
LAYER: frame. REPEAT: new. Confidence: likely.
K-2 unit 4 gives "born 1924" with a hedge on whether she is living. From memory she died in 2024.
Change: check and write "1924 to 2024" and drop the hedge.

**10. UK spelling.**
LAYER: frame. REPEAT: new. Confidence: firm.
"catalogue" on line 3 of the K-2 and HS frames. Change: "catalog".

**11. mu-g2-choose has no public option in its row.**
LAYER: progression. REPEAT: new. Confidence: firm.
The K and grade 1 rows gained a story-character or public option; grade 2's row did not, though the unit
offers one. Change: add the same clause to the row so the row and the unit agree.

**12. Same-band repeats with other arts frames.**
LAYER: frame. REPEAT: new. Confidence: firm.
Saint-Saëns, Carnival of the Animals: music K-2 unit 1 and dance K-2 unit 2, both grade K. Tango: music
6-8 unit 3 (Piazzolla, grade 6) and dance 6-8 unit 8 (grade 7). Powwow: music 6-8 unit 4 (grade 6) and
dance 6-8 unit 12 (fancy shawl, grade 8). These can be strengths if named as a link. Change: name each as
a cross-arts link in both frames ("the class may have danced to this in dance"), or swap the music work in
K-2 unit 1, which is the tightest overlap (same grade, same term). Samba de roda against Cheri Samba is a
word match only, no change.

### Judgment calls

**13. 3-5 unit 12 leans on fractions mid-unit.**
LAYER: frame. REPEAT: new. Confidence: judgment call.
It uses math 5.NF.A.1 from week 25, while math grade 5 unit 9 runs weeks 24 to 27. The "if later" line
exists. My pick: put the fraction-reading days at the end of the unit (week 28 on) and keep half-beat
counting before then.

**14. 3-5 year 3 writes standard notation before unit 4 teaches staff reading.**
LAYER: frame. REPEAT: new. Confidence: judgment call.
Grade 2 already read so-mi-la on a staff, so it holds. My pick: keep the order and add one line to unit 3
naming the grade 2 reading it builds on.

## Calendar clashes (for the lead's pass, not counted)

From data/plans/calendar.csv; the stagger keys on subject `arts`, so all five arts share it.

- Grade K week 19: music, theater.
- Grade 1 week 17: dance, music. Grade 1 week 25: dance, music.
- Grade 2 week 17: dance, ELD, music, PE, theater, visual arts. Grade 2 week 25: dance, music.
- Grade 3 week 15: health, music.
- Grade 4 week 15: ELD, music, SEL. Grade 4 week 24: computer science, music.
- Grade 5 week 15: health, music, SEL.
- 6-8 (week 19 mid-year on school days 93 and 95; week 32 year-end): no clash under rule 3.
- 9-12 (weeks 16 and 32): no rule broken.

The frames' own calendar notes understate these (K-2 names only grade 2 week 17; 3-5 says week 24 holds no
other check). The lead's pass should rewrite them.

## Settled by the expert

| Question | Settled as |
| --- | --- |
| Keep K-8 connecting ids as .1 and HS as .0? | Yes, as printed in the id file |
| Level 4 repeating the .IIIa ids marked "~"? | Correct; it matches the levels rule |
| 6-8 year-end check in week 32? | Allowed by rule 3 |
| Powwow as listening only, no costume? | Right; keep it |
| Repeated works across bands | Revisit allowed only if named and at a new depth (finding 2) |
| 3-5 notation order | Keep, with a pointer line (finding 14) |
| Fraction lean in 3-5 unit 12 | Late in the unit (finding 13) |

## For Cory

- Money, supply ceilings as written: K-2 $55 / $20 / $20 (pick $75 a class a year); 3-5 $30 / $25 / $25
  plus $20 once for rhythm sticks; 6-8 $35 / $20 / $20; HS $35 / $30 / $30 / $20 (pick $40 a class a level).
  No change proposed; listed so the figures are seen.

## What is right

- Complete id coverage, with the evidence written id by id.
- Check-day minutes stated inside the session.
- Strong sensitivity notes (powwow listening only, no costume; every personal tie has an invented or
  public option).
- Safety bullets name free guides.
- Math leans carry "if later" lines.
- HS levels, the bridge unit, the review units and the Level 4 "~" rows are handled cleanly.
- Day arithmetic, once-a-week paths and the HS short path all add up; the seams match row for row.

## What it could not judge

- The national words for Cr1.1.3b, Cr2.1.Kb and Pr6.1.8a without the source. Pr6.1.8a ("culturally
  authentic practice") matches my memory.
- A high school music time figure: the NAfME opportunity-to-learn standards, high school part, were not read.
- The rights status of the Ives score.
- Whether a real music teacher would find two 40-minute sessions enough for the K-2 units (the K-8 gap
  to NAfME's 90 minutes is noted in STANDARD.md; not reopened).

## Sources (browser checks needed; no downloads or sign-ins made)

- The NCAS music "at a glance" handout (Cr2.1.Kb, Cr1.1.3b, Pr6.1.8a).
- The NAfME opportunity-to-learn standards, high school part.
- A rights check for Ives, Variations on "America" (1949 publication).
- A dates check for Ella Jenkins.
