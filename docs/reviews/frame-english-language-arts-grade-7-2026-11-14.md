# Frame read: English Language Arts Grade 7, 2026-11-14

Reader: the curriculum expert (docs/agents/EXPERT.md), cold. Brief: docs/pipeline/briefs/frame-read.md, with the
caller's added checks (text picks, the original-text load, the writing split, the 50-minute day, the proposed row
change for e7-reading-range, repeated picks across frames and subjects, every lettered part, the 15 lessons in
docs/pipeline/briefs/frame-write.md).

## What I read

- docs/courses/english-language-arts-grade-7/frame.md in full; its row in data/plans/frames.csv (6 units, 160 days).
  No base text.
- The grade 7 rows of data/progressions/ela.csv, every column, and the grade 6 and grade 8 rows they take from and
  hand to (e6-reading-range, e8-reading-range in full).
- The neighbour frames: docs/courses/english-language-arts-grade-6/frame.md and
  docs/courses/english-language-arts-grade-8/frame.md; docs/courses/english-language-arts-grade-9/frame.md for the
  Shakespeare sonnets.
- The same-year frames: docs/courses/world-geography-and-ancient-civilizations-ii/frame.md (social studies 7, units
  8 to 12 and its cross-subject lines), docs/courses/science-grade-7/frame.md (units 5 and 6). Every frame searched
  for the grade 7 picks (Elwha, Dust Bowl, Onesimus, smallpox, Pericles, Pheidippides, Sonnet 18, the Drought
  Monitor); docs/courses/biology/frame.md unit 9.
- docs/agents/lenses/ela.md, docs/RUBRIC-ELA.md, the grade 7 lines of data/standards/ccss-ela-standards-full.txt;
  docs/agents/decisions/DESK-ANSWERS.md (2026-11-12 and 2026-11-13); the "For the course frames" sections of the two
  2026-11-13 progression cross reads.
- Gates: `python -X utf8 scripts/frame.py check english-language-arts-grade-7` (0 failures);
  `python -X utf8 scripts/plan.py check` (passes); `python -X utf8 scripts/stale.py check` (56 files, 0 failures).
  By hand: unit days 1 to 30, 31 to 56, check 57 to 60, 61 to 86, check 87 to 90, 91 to 112, 113 to 134, 135 to 156,
  check 157 to 160.
- Not opened, as told: the earlier grade 6 ELA planning and its reviews.

## Verdict

The frame has a real year in it: two narrators in the drought novella, a Dust Bowl unit that reads the government
film beside the record, a smallpox research unit with a credit question students can actually argue, and threads
that reach science 7's floods and droughts. It has three faults a scope and sequence writer would carry forward: the
same rule 29 contradiction as grades 6 and 8 (Pericles and the 1717 and 1798 letters anchor in function), lettered
parts written at the grade 6 level so that seven grade 7 demands are missing, and two picks that repeat other
courses (the Elwha in biology, Sonnet 18 in grade 9). The proposed e7-reading-range change is right in substance but
needs its other ends written before it is applied.

## Findings

### 1. Older texts anchor in function while the frame says they never do

- **What is wrong.** The Base text bullet repeats rule 29 (older texts paired only). Unit 4 teaches RI.7.8 on
  Pericles' funeral oration (Jowett's translation); unit 3's RI.7.9 compare rests on the 1717 Mather letter and the
  1798 Jenner account; unit 6 reads Theodore Roosevelt's 1912 address for argument. In each case the standard's work
  is on the older text, so it is the anchor in all but name.
- **Why it matters.** As in grade 6: the 55 percent informational count, the text records and Cory's rule all
  depend on which texts are anchors.
- **Fix.** The same "For the lead" item as the grade 6 read, finding 1 (one question to Cory for the band), naming
  these four texts. Until he decides, call them "paired primary sources, excerpted and read with full support" in
  the units.
- LAYER frame. REPEAT new. Confidence: firm.

### 2. Seven grade 7 lettered demands are written at the grade 6 level

- **What is wrong.** Checked against data/standards/ccss-ela-standards-full.txt:
  - W.7.1c and W.7.2c: the frame says "transitions to clarify relationships"; grade 7 adds "create cohesion".
  - SL.7.1b: the frame has norms and roles; grade 7 adds "track progress toward specific goals and deadlines".
  - SL.7.1c: the frame has "pose questions"; grade 7 asks questions "that elicit elaboration and respond to others'
    questions and comments with relevant observations and ideas that bring the discussion back on topic as needed".
  - L.7.4c: the frame says "a dictionary"; the standard asks for general and specialized reference materials
    (dictionaries, glossaries, thesauruses), print and digital.
  - W.7.6: the frame has publishing and citations; grade 7 adds "to link to and cite sources as well as to interact
    and collaborate with others".
  - SL.7.5: the frame has multimedia "to clarify"; grade 7 adds "and emphasize salient points".
- **Why it matters.** Lesson 4: every lettered part in full. A unit writer copies the frame's wording, and seven
  grade 7 demands vanish without anyone choosing to drop them.
- **Fix.** Quote each part in full in the unit that owns it: W.7.1c in unit 2's process argument ("transitions that
  create cohesion and clarify the relationships among claims, reasons and evidence"), W.7.2c in unit 3's research
  report, SL.7.1b in unit 3 ("each group sets goals and deadlines for its research and checks progress at the end
  of each week"), SL.7.1c in unit 4's seminar, L.7.4c in unit 2 (a glossary of soil and farm terms and a thesaurus
  task beside the dictionary), W.7.6 in unit 3 (students comment on a partner's draft in the shared document, and
  the paper path does the same on a printed draft), SL.7.5 in unit 6's presentation.
- LAYER frame. REPEAT yes (lesson 4). Confidence: firm.

### 3. The Elwha River repeats biology unit 9

- **What is wrong.** Unit 6 anchors on the Elwha dam removal. Biology's unit 9, "Designing for a river", is built on
  the same river and the same removal. Lesson 11: picks named and not repeated.
- **Why it matters.** A student reads the same case study in grade 7 and again in high school, and the high school
  unit, which needs it more for its data, loses its surprise.
- **Fix.** Use the Klamath River dam removal (four dams, removed 2023 to 2024, the largest in US history), from
  USGS, NOAA Fisheries and Bureau of Reclamation pages (public domain, images checked one by one). The argument and
  the science 7 link hold as written. Sensitivity readers: a Karuk and a Yurok reader (the tribes who pressed for
  removal), named in the unit's reader line.
- LAYER frame. REPEAT yes (lesson 11). Confidence: firm (the repeat); judgment call (the Klamath, settled below).

### 4. The e7-reading-range row change is sound but one-ended

- **What is wrong.** For the lead item 3 proposes dropping "the republic" from e7-reading-range because grade 7
  reads Athens, not Rome. The substance is right: this frame has no Roman text. But lesson 7 asks for both ends of
  every handoff, and two other ends still point at grade 7 Rome: e8-reading-range's note lists "republic" among the
  words reused from grade 7, and the social studies 7 frame's cross-subject line expects ELA 7 Rome texts beside its
  unit 10 (days 121 to 133). The item also says grade 8 unit 2 "meets the republic", but no text in grade 8 unit 2
  is about a republic as a form of government.
- **Why it matters.** Applied alone, the change leaves grade 8 reusing a word grade 7 never taught and social studies
  7 waiting for texts that will not come.
- **Fix.** Apply together. e7-reading-range, thread 1 text becomes: "Thread 1, citizens and government in Greece:
  inherited from grade 6 law codes (e6-reading-range); grade 7 adds Athenian democracy and who counted as a citizen,
  beside social studies ss7-athenian-democracy and ss7-greek-myth; words reused: law, code, justice, with citizen
  and democracy added; used again in e8-reading-range (founding documents)." In e8-reading-range, replace
  "republic" in the words reused with "citizen, democracy". In For the lead, add a line for the social studies 7
  frame: "Cross-subject, Rome (social studies 7 unit 10): ELA grade 7 reads no Roman text; Latin roots stay in
  L.7.4b's word work beside unit 11." Drop "grade 8 unit 2 meets the republic".
- LAYER progression. REPEAT yes (lesson 7). Confidence: firm.

### 5. Unit 4 asks social studies unit 8's question, and "after" is not true

- **What is wrong.** Social studies 7 unit 8 (days 87 to 101) asks "Was Athens a democracy?" ELA unit 4 (days 91 to
  112) reads Pericles and asks, in effect, the same thing, and its reason says it comes "after" social studies'
  Athens unit; the two run side by side for eleven days.
- **Why it matters.** The same argument twice in a fortnight, as in grade 6 unit 2.
- **Fix.** Compelling question: "How did Pericles want the world to see Athens, and who did his picture leave
  out?" (RI.7.6 and RI.7.8, answerable from the oration and the unit's original feature on who could vote). In the
  reason, replace "after" with "beside social studies 7 unit 8 (days 87 to 101), which asks whether Athens was a
  democracy; ELA reads how one speech made the case." With finding 12's check move, unit 4 becomes days 87 to 108,
  in step with social studies.
- LAYER frame. REPEAT yes (distinct questions for shared topics, the progression cross reads). Confidence: likely
  (I paraphrase the ELA question's thrust).

### 6. RL.7.7 is taught on audio only

- **What is wrong.** RL.7.7 asks students to compare a text with its "audio, filmed, staged, or multimedia version",
  "analyzing the effects of techniques unique to each medium (e.g., lighting, sound, color, or camera focus and
  angles in a film)". Unit 5 compares the play script with the course's audio recording only. The Dust Bowl film in
  unit 2 is informational and serves RI.7.7.
- **Why it matters.** Half the standard's examples (lighting, color, camera) cannot be taught from audio.
- **Fix.** Add a course-made short video of one scene of the unit 5 play, with deliberate camera, lighting and
  sound choices, beside the audio; students compare script, audio and film. The paper path gives stills and a shot
  list.
- LAYER frame. REPEAT new. Confidence: firm.

### 7. One author for the literature, and the original-text count is off

- **What is wrong.** As in grade 6, every literary anchor is an original Curio Class text. For the lead 4 says
  about 30 originals; the units name about 26, with 9 poems (not 11) and 2 stories (not 4).
- **Why it matters.** RUBRIC-ELA 2a and 2e, and the band load (finding 4 of the grade 6 read).
- **Fix.** Correct the count to the units' own list; add the text-spec voice line and the open-licence search
  first, worded as in the grade 6 read; the question of human writers goes to Cory.
- LAYER frame. REPEAT new. Confidence: likely.

### 8. The weekly conference and the choice book, as in grade 6

- **What is wrong.** The same Days bullet: weekly conferences with no in-class independent reading, and no free
  source for choice books.
- **Fix.** The grade 6 read's finding 5 text, with "grade 6" for the seam line removed.
- LAYER frame. REPEAT new. Confidence: likely.

### 9. No readiness checks are placed

- **What is wrong and fix.** As in the grade 6 read, finding 6: a line under the Seams table and a readiness task
  named in each unit that first uses a grade 6 skill.
- LAYER frame. REPEAT yes (lesson 5). Confidence: firm.

### 10. Sonnet 18 repeats grade 9

- **What is wrong.** Unit 5 pairs Shakespeare's Sonnet 18; grade 9 unit 8 reads Sonnets 18, 116 and 130 as its
  form study.
- **Fix.** Pair John Keats, "On First Looking into Chapman's Homer" (1816, public domain): a sonnet about reading
  Greek epic, which fits the unit's Greek setting and still teaches the form for RL.7.5.
- LAYER frame. REPEAT yes (lesson 11). Confidence: firm.

### 11. The US Drought Monitor is not a federal work

- **What is wrong.** Unit 2's rights line calls the Drought Monitor maps public domain. The Drought Monitor is
  produced by the National Drought Mitigation Center at the University of Nebraska-Lincoln with USDA and NOAA, and
  its pages carry the university's terms.
- **Fix.** Check its terms and record them, or use NOAA's National Integrated Drought Information System
  (drought.gov) pages, which are federal.
- LAYER frame. REPEAT new. Confidence: likely (from memory, not re-fetched).

### 12. Unit 5's question cannot be answered from its texts, and the legend is presented as history

- **What is wrong.** Unit 5 asks why the marathon story lasts, but its texts are poems and a play; none tells how
  the 1896 race came to be or where the legend comes from. The Pheidippides run to Athens is not in Herodotus, who
  has him run to Sparta for help; the Athens run comes from much later writers.
- **Why it matters.** Lesson 10: questions answerable from the unit. And a teacher would teach a legend as fact.
- **Fix.** Add a short original feature on the 1896 Athens marathon and the legend's sources (Herodotus' run to
  Sparta, the later Athens story, Michel Breal's proposal of the race). Teacher note: the legend is a legend.
- LAYER frame. REPEAT yes (lesson 10). Confidence: firm.

### 13. Sixty-six unit days with no course check

- **What is wrong.** Check 1 (days 57 to 60) and check 2 (days 87 to 90) are 26 days apart; then units 4, 5 and 6 run
  66 days to check 3.
- **Fix.** Move check 2 after unit 4: unit 4 days 87 to 108, check 2 days 109 to 112, unit 5 days 113 to 134, unit 6
  days 135 to 156. The gaps become 48 and 44 days, and unit 4 lines up with social studies unit 8 (finding 5).
- LAYER frame. REPEAT new. Confidence: likely.

### 14. Onesimus needs a named reader

- **What is wrong.** Unit 3 tells how an enslaved African man, Onesimus, brought inoculation to Boston. Grade 8
  names an African American history reader for its founding-era units; grade 7 names none for this one.
- **Fix.** Add "an African American history reader" to unit 3's reader line, and a teacher note that the unit
  credits Onesimus by name and does not dwell on his enslavement beyond what the credit question needs.
- LAYER frame. REPEAT yes (lesson 12, sensitivity reads). Confidence: firm.

### 15. Narrative writing at 25 percent

- **What is wrong and fix.** As in grade 6, finding 8. Add a one-sitting narrative in unit 2: "a scene on Black
  Sunday, April 14, 1935, told by a character in the ranch family's grandparents' generation" (W.7.3), making 3, 3
  and 3.
- LAYER frame. REPEAT new. Confidence: likely.

### 16. Stale notes

- **What is wrong and fix.** The same three as the grade 6 read, finding 10 (the dash note in the punctuation row,
  RUBRIC-ELA's answer column, the lens's rights pointer); one "For the lead" line pointing at that text.
- LAYER process. REPEAT yes (lesson 15). Confidence: firm for the dash note.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Klamath dam removal replaces the Elwha | The Elwha is biology unit 9's case; the Klamath is newer, larger, federal-sourced | grade 7 frame, unit 6 |
| Keats, "On First Looking into Chapman's Homer", replaces Sonnet 18 | Sonnet 18 is in grade 9; Keats fits the Greek unit | grade 7 frame, unit 5 |
| A course-made video scene for RL.7.7 | The standard needs film techniques | grade 7 frame, unit 5 |
| Unit 4's compelling question as in finding 5 | Distinct from social studies' question | grade 7 frame, unit 4 |
| Check 2 after unit 4 | Even spacing, in step with social studies | grade 7 frame, Days and units table |
| e7 and e8 reading-range texts as in finding 4 | Both ends of the handoff | data/progressions/ela.csv (via the lead) |
| A Black Sunday one-sitting narrative in unit 2 | Narrative share | grade 7 frame, unit 2 |

## For Cory

- **Primary sources as anchors** (finding 1): one question for grades 6 to 8, asked in the grade 6 read.
- **Who writes the literary originals**: the band question, asked in the grade 6 read.
- **Readers:** a Karuk and a Yurok reader for unit 6, an African American history reader for unit 3. People.

## For the lead items, judged

- **1 (minutes):** sound; add in-class reading time (finding 8).
- **2 (the "Texts" column):** sound.
- **3 (e7-reading-range):** right in substance; apply with the other ends (finding 4).
- **4 (about 30 originals):** count corrected (finding 7); the load is sound for informational texts, a risk for the
  literary ones.

## What is right and should not be touched

- The two-narrator novella for RL.7.6, and the drought thread that runs from the novella to the Dust Bowl to the
  river, beside science 7 unit 6 (days 129 to 158, floods and droughts).
- The Dust Bowl unit's film-and-record compare (RI.7.7) and the smallpox credit question, an argument students can
  build from the unit's own sources.
- Days by load, and the fluency and paper-path lines, as in grade 6.

## Lens checklist

- Every lettered part in full: missed (finding 2).
- Text picks public domain or licensable: met except the Drought Monitor (finding 11).
- Reading level and range: met.
- Informational share near 55 percent: met if the primary sources count (finding 1).
- Writing split: narrative low (finding 15).
- Picks not repeated: missed twice (findings 3 and 10).
- Same-year alignment: unit 4 overlaps social studies (finding 5); science aligned.
- Readiness checks: missed (finding 9).
- Sensitivity reads: one missing (finding 14).
- Paper path: met.

## What I could not judge

- The copyright status of Virgil Thomson's score in "The Plow That Broke the Plains" (1936); the film is a federal
  work, the score may not be. Check before the film is embedded with sound.
- The Drought Monitor's current terms (finding 11).
- The quality of texts not yet written.

## Sources

- data/standards/ccss-ela-standards-full.txt for every grade 7 lettered part quoted.
- The social studies 7, science 7, biology and grade 9 ELA frames for the calendar and repeats.
- From memory, not re-fetched: Herodotus, Histories 6.105 to 106 on Pheidippides; the Klamath removal dates; the
  Drought Monitor's authorship.
