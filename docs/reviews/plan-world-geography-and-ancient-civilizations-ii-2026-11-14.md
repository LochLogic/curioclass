# Plan read: World Geography and Ancient Civilizations II, units 1 to 12 (2026-11-14)

Expert cold read of every unit plan, following docs/pipeline/briefs/plan-read.md. No file was edited except this report.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/GLOSSARY.md, docs/pipeline/briefs/plan-read.md, docs/agents/lenses/social-studies.md.
- docs/ADOPTION-BAR-SUBJECTS.md section 1 (social studies) and docs/courses/social-studies/STANDARD.md.
- docs/courses/world-geography-and-ancient-civilizations-ii/frame.md, scope-and-sequence.md, s01.md to s12.md (all twelve, in full).
- data/plans/world-geography-and-ancient-civilizations-ii/days.csv (all 160 rows) and data/progressions/social-studies.csv (the rows these units own, assume and hand on); data/standards/ma-hss-2018.txt for the own-word lines quoted in the plans.
- The "Settled by the expert" tables of plan-social-studies-kindergarten, grade-1, grade-3 and grade-4 (all 2026-11-14), applied here and cited, not re-argued.
- Web checks on 2026-11-14: Vietnam's 2024 population figures (mid-term census and annual average); the Harappa unfinished elephant seal; the Met Heracles cup record; the Rangitane o Wairau control and management agreement for Te Pokohiwi o Kupe (signed February 2026, so the "2026 custodianship statement" is real and current). From knowledge, checked against the plans' own sources: Thucydides 1.23 and 1.88; Hesiod's jar; the Dipylon jug (Athens A 192, about 740 to 730 BCE); Eurysaces's tomb inscription; Naevoleia Tyche; Tacitus Annals 6.16 to 17 (the 33 CE credit crisis); Frontinus 17; Lactantius 48; Eugippius 20; Ai Khanoum's Delphic maxims; Eratosthenes; 509 BCE, 264 BCE, 117 CE, 44 BCE, 27 BCE, 313, 380, 476 and 1453; C3 D2.Eco.12 and D2.Eco.15 wording; time zones and the 1884 resolutions (unit 7); Ashoka's Topra pillar, Article 17 (1950), Cai Lun, Pliny NH 6.101 and Periplus 30 (units 2 and 4). All correct unless noted below.

## Course verdict

The content is accurate, current where it touches the present (the 2026 Rangitane agreement, Mexico's 2022 end of daylight saving), carefully sourced, and honest about what each source cannot show; the sensitivity notes are thoughtful and mostly complete. It is not yet to the bar: unit 5 has no exit tickets and assesses the fair-comparison skill two days before it is taught, unit 1 sets a sitting before day 1 against the lead rule, unit 6's file has lost every macron and quote mark (Maori names included), and the settled sizing rule is broken again in six assessments. Every fix is an edit inside existing days; no day moves and nothing needs Cory.

Unit 8's split (days 87 to 100 plus day 120) is handled clearly: the header, supporting questions, field 4, an exit ticket, field 8's action paragraph and the day list all carry day 120, and unit 10 notes that day 120 intervenes before day 121. One teacher line is missing (8.2).

## Course-wide findings

### CW1. Assessments overloaded for their minutes (moderate, plan, REPEAT of the settled sizing rule)

Grade 4's Settled table sets about 1 minute per locate item, 2 per one-sentence explanation, 4 to 5 per constructed map and 8 per paragraph. Six units break it: s02 (about 48 minutes of work in 40), s04 (item 4 six mechanisms in 5 minutes, item 8 four drawn graphs plus Pliny in 9), s06 (items 5a and 5b in 11), s10 (items 2 and 5), s12 (item 3), and s01 is borderline. Fixes are per unit below: trim parts that other evidence already covers, never add minutes.

### CW2. Reteaching on assessment days (moderate, plan, REPEAT in s07 and s08)

s07 field 5 and s08 field 5 both open with "Ten minutes for directions and targeted reteaching". Reteaching on the assessment day contaminates the evidence and shortens the unaided work. Directions take at most five minutes; a gap seen the day before goes into that day's own warm-up or is recorded for the respond day. See 7.1 and 8.1.

### CW3. Sensitivity flag stripped to an empty or dangling line (minor, skeleton, REPEAT in s02, s03, s04, s07, s12)

Field 10 "Days flagged for the sensitivity read" reads "Day 12: . Not an "invasion" story" (s02), "Day 26: . Partial base ..." (s03), "Day 38: " (s04), "Day 78: " (s07), "Day 145: " (s12). scripts/unit_skeleton.py removes the "Sensitivity read (...)" sentence and leaves nothing when the note starts with it. It works in s05, s06, s08 to s11. Fixer: restore each line from the days.csv note. Structure pass: fix the strip.

### CW4. Pipeline notes in teacher-facing text (minor, process, REPEAT in all twelve)

Every plan carries lines such as "Reading pack failed on missing check_min", "No lesson or Tomorrow line was inspected because courses/ is excluded", "This corrects the skeleton's absence claim", "The skeleton expanded parent code MA.7.T4c.3 beyond this unit's assigned share". These belong in the Codex write report, not in a plan a teacher reads. Fixer: delete them from fields 3, 4, 5 and 10 (keep "Still to make" items that name real work). Structure pass: the Codex brief says pipeline notes go in the report only.

### CW5. Encoding and line endings (process, REPEAT)

s06 is ASCII with 115 literal "?" replacing macrons, degree signs, apostrophes and quotes (see 6.1). The other files are clean, but several have CRLF line endings and s04 alone is UTF-8. Structure pass: Codex writes UTF-8 with LF; a checker rejects a plan with "?" inside a word.

### CW6. Field 2 loses its bullets (minor, plan and template, REPEAT in s06 to s12)

After the compelling question, Hook, Supporting questions, Closing claim and Teaching moves run on as bare bold lines with no bullet or blank line, so in rendered Markdown they merge into one paragraph in s06, s07, s08 (s09 to s11 the same). Fixer: start each with "- ". Structure pass: put those four labels in the template as bullets.

### CW7. "Carried" tags say "introduced or first used here" for returning models (minor, skeleton, REPEAT)

The skeleton tags C3 codes and some models as first used even where the frame says used again. Structure pass only; the plans' own Carried lines are right.

### CW8. New York check set not read in eleven plans (minor, process, REPEAT)

Every plan but s12 says the official New York PDF "timed out" and leans on an indexed excerpt; s12 cites "printed page 84, 6.5a" from a local reference copy. If a local copy exists, the other plans should use it. Structure pass: put the local New York path in the plan brief so every unit reads it; this is not the settled Tennessee block.

## Unit 1 (s01, days 1 to 11): South Asia and the Indus cities

### 1.1 Start-of-year check invents a sitting before day 1 (serious, plan and skeleton, REPEAT of grade 4 1.1)

Field 4 says "Given: the start-of-year check, before day 1" and "Use ten minutes in the existing start-of-year administration, at most a few days before the unit." The lead rule of 2026-11-14 forbids any sitting before day 1. Every assumed row is a grade 6 row needing retrieval only, so unit 1 has no readiness rows. Fix (s01 field 4): replace the Given line and the three items with "**Given:** none needed; retrieval only. The day 1 and day 6 retrieval tasks are this unit's start-of-year evidence." Rekey the day 1 and day 2 "bridge" notes from items 1 to 3 to misses on the day 1 and day 6 retrieval tasks. Structure pass: the skeleton's unit 1 Given line must read "none needed; retrieval only" when days.csv holds no readiness rows.

### 1.2 Object X catalogue number does not match the known object (moderate, plan, exact citations rule)

Field 5's Object X is "H-1533", an Early Harappan unfinished elephant seal, cited to Kenoyer and Meadow. The published unfinished Kot Diji-phase elephant seal from Harappa is catalogued H2000-4474/8994-01 (harappa.com, node 2339); no H-1533 record was found. Fix: cite the object by its published number and source page, or mark it "an original card based on" that object. Keep the teacher-key-only rule.

### 1.3 Assessment tight (minor, plan, REPEAT of CW1)

Six items, three multi-part, in 40 minutes. Trim item 6 to one inference and one limit.

### 1.4 Day 6 exit asks about a weight's "signs" (minor, plan)

Harappan cubical weights rarely carry signs. Change "signs" to "size and material".

### 1.5 Closing claim narrows the answer (minor, plan)

"Defend coordinated production or exchange as the stronger inference" offers two answers. Change to "Defend the inference the evidence best supports, and name one it cannot rule out."

## Unit 2 (s02, days 12 to 25): early India, its faiths and its legacy

### 2.1 Sensitivity sources miss the caste-teaching dispute (moderate, plan)

Field 10's Hindu community voices are one sampradaya's page and one magazine. How caste is taught is a live, published dispute in US schools (California's framework revisions; recent caste-bias laws and the Hindu American and Dalit and Ambedkarite organizations on each side). The sensitivity agent must study both sides' published voices and a second Hindu source from another tradition. Fix: add that sentence to "Sensitivity study, owed".

### 2.2 Assessment overloaded (moderate, plan, REPEAT of CW1)

About 48 minutes of work in 40. Item 3 asks all eight path elements; item 6 asks five fields, medicine and why. Fix: item 3 asks four elements and how they fit together; item 6 asks two fields and one reason.

### 2.3 Upanishad passage numbers disagree (minor, plan)

The source list names 4.4.5; item 1 uses 4.4.6 as unseen. State which passage is taught and which is withheld for the assessment.

### 2.4 Day 12 flag dangling (minor, skeleton, REPEAT of CW3)

## Unit 3 (s03, days 26 to 37): East Asia's land and early China

### 3.1 "All four named relationships" (minor, plan)

The tradition names five relationships (ruler and subject, parent and child, husband and wife, elder and younger brother, friend and friend). Check the wording against the Analects reading; if four are taught, say "four of the five".

### 3.2 Item 6 heavy for 8 minutes (minor, plan, REPEAT of CW1)

Sourcing, four relationships and Taoism. Drop the Taoism part (covered by the day 34 exit).

### 3.3 Day 26 flag dangling (minor, skeleton, REPEAT of CW3)

## Unit 4 (s04, days 38 to 50): Qin, Han and the Silk Road

### 4.1 Day 45 carries two retrieval bridges on its only teaching day for the graph (moderate, plan)

Day 45 is the supply-and-demand graph's only Understanding day, yet the plan allows two five-minute bridges (Phoenician coins and opportunity cost; 6.RP percent and graph reading) "by replacing practice". That eats the first practice of a new skill (grade 1 and kindergarten Settled: observations and side tasks never take the only teaching minutes). Fix: move the percent retrieval to day 46, the toll-percent day.

### 4.2 Assessment overloaded (moderate, plan, REPEAT of CW1)

Nine items in 40 minutes; item 8 asks four drawn graphs plus Pliny in 9 minutes; item 4 asks six mechanisms in 5. Fix: item 8 two graphs (one shift each way) plus Pliny; item 4 three mechanisms.

### 4.3 Li Si wording (minor, plan)

"Transmitted about a century later": Sima Qian wrote roughly 110 to 140 years later. Say "recorded by Sima Qian more than a century later".

### 4.4 Day 38 flag empty (minor, skeleton, REPEAT of CW3)

## Unit 5 (s05, days 51 to 62): Korea, Japan and comparison

### 5.1 No daily exit tickets (serious, plan)

Field 5 has no exit tickets for teaching days 52 to 60; "exit tickets" sits under Still to make. Every other unit has them, and the bar asks for daily evidence. Fix: add an exit table (day, prompt and answer, wrong answer and error letter) for days 52 to 60 in the same form as s07.

### 5.2 Fair comparison assessed before it is taught (serious, plan)

The day 56 and 57 India and China products are filed as summative evidence for MA.7.T1b.2 and MA.7.T2b.2 and all thirteen lettered parts, but "how to compare fairly" and the qualified comparison are taught on day 58. Fix (lower ripple, no day swap): in day 56's first ten minutes, model one worked qualified comparison with a pair not on the cards; day 59 lets each student revise one cell, and only the revised product counts as summative evidence. Field 5's evidence note says so.

### 5.3 Day 56 tight (minor, plan)

Seven cards plus a conclusion in 25 minutes, now less after 5.2's model. Cut to five cards.

### 5.4 Day 53 crowded (minor, frame scope, note only)

Buddhism in Japan from the 6th to 13th century, Shinto, Heian and Genji in one day. Keep; the lesson writer should choose one source per strand.

## Unit 6 (s06, days 63 to 75): Southeast Asia, Australia and Oceania

### 6.1 Every macron, degree sign and quote mark is a literal "?" (serious, process)

115 replacements: "Ng?i Tahu", "M?ori", "Rangit?ne", "wh?nau", "hap?", "p?", "35? south", and quotes as "?Why ... ?". Misspelling the names of a living people is a dignity issue, and the assessment items cannot be read. This is far larger than grade 4 5.2. Fix: rewrite the file in UTF-8 restoring Ngai Tahu with a macron on the first a (Ngāi Tahu), Māori, Rangitāne, whānau, hapū, pā, the degree signs, apostrophes and quotation marks. Check every "?" by hand.

### 6.2 The standards file's own-word line uses outdated names (moderate, data)

The MA.7.T3b.1 line in data/standards/ma-hss-2018.txt says "the Aborigines of Australia and the Maoris of New Zealand", which reaches the plan's skeleton field and contradicts the frame's own rule. Fix (data): "the Aboriginal peoples of Australia and the Māori of Aotearoa New Zealand". Then regenerate the line in s06.

### 6.3 Vietnam figure mislabelled (minor, plan, current official facts)

"Vietnam about 101.1 million in the annual estimate": 101.1 million is the 1 April 2024 mid-term census count; the 2024 annual average is about 101.3 million. Fix: "Vietnam about 101.1 million at the April 2024 mid-term census".

### 6.4 Items 5a and 5b heavy (minor, plan, REPEAT of CW1)

Eleven minutes for two sourced explanations with ochre, shell and custodianship. Drop the second relationship from 5b.

## Unit 7 (s07, days 76 to 86): Europe's land and time zones

### 7.1 Reteaching on assessment day 85 (moderate, plan, REPEAT of CW2)

Old: "Ten minutes for directions and targeted reteaching, then forty minutes unaided work. Printed directions keep the opening available for a day 84 gap." New: "Five minutes for directions, then forty-five minutes unaided work. A day 84 gap is retaught in day 84's own last minutes or recorded for day 86." Give item 4 (12 minutes) the extra five only if needed; otherwise add them to item 3.

### 7.2 Day 78 flag empty; field 2 bullets (minor, skeleton and plan, REPEAT of CW3 and CW6)

## Unit 8 (s08, days 87 to 100 and 120): Greece's land, city-states and democracy

### 8.1 Reteaching on assessment day 99 (moderate, plan, REPEAT of CW2)

Same wording as 7.1. New: "Five minutes for directions, then forty-five unaided", and move the closing claim from 6 to 8 minutes and the institutional grid from 9 to 12.

### 8.2 Day 120 needs one return line for the teacher (minor, plan)

The split is clear, but the plan never says day 120 comes about four weeks later, after unit 9 and course-level check 2, or what to keep. Fix (field 8, end of the "Action, 92 to 94 and 120" paragraph): "Day 120 comes after unit 9 and course-level check 2, about four weeks later. Keep the action log and the day 94 letter on file; any reply arrives in that time."

## Unit 9 (s09, days 101 to 115): Greek wars, myths and accomplishments

### 9.1 Day 112 carries too much (moderate, plan)

Day 112 holds hand-in, five-area sharing, the listening grid, and now four cross-society comparisons ("On 112 attach four brief comparisons"). That cannot fit 50 minutes. Fix: write the four comparisons as day 108's note-taking step (each student writes one, the class pools four), and on 112 only attach them.

### 9.2 Two retrievals on day 105 in one five-minute slot (minor, plan)

Field 4 retrieves the grade 6 research rows on 105; field 5 also retrieves "the unit 5 comparison chart" on 105. Move the comparison-chart retrieval to day 108's opening, beside 9.1's comparisons.

### 9.3 Pipeline notes (minor, process, REPEAT of CW4)

"Lesson files and the Tomorrow line were excluded by the brief"; "The reading pack failed on missing check_min".

Content checks passed: Thucydides 1.88 paraphrase is faithful and labelled; Hesiod's jar note; Dipylon jug A 192; Heracles cup record 255020 exists (its accession number 59.15 was not confirmed; the image-rights check already listed covers it).

## Unit 10 (s10, days 121 to 133): the Roman Republic and its end

### 10.1 Readiness reteach takes day 121's first teaching minutes, and two fields disagree (moderate, plan)

Field 4 says a miss uses "day 121's warm-up after the hook and first five teaching minutes"; field 5 says "On 121, readiness reteaching replaces ten minutes of repeated practice after the hook". Day 121 is the first teaching of map location, and branches do not return until day 123. Fix: both lines read "If more than a third miss, use day 122's warm-up and five minutes of its map practice for a ten-minute card sort; otherwise teach a small group during day 122's map work." Delete the field 5 sentence about 121.

### 10.2 Items 2 and 5 overloaded (moderate, plan, REPEAT of CW1)

Item 2 asks the rise, a four-row chart and four principles plus a breakdown in 9 minutes; item 5 asks a source reading, four statuses, two routes, two workplaces, resistance and a limit in 10. Fix: item 2 drops the transition question (covered by the day 123 exit); item 5 asks one route and one workplace. Move the freed minutes to item 5.

### 10.3 Sensitivity study should include one source on teaching slavery to US middle schoolers (minor, plan)

For ancient Rome, "two community publications" has no obvious community. In US classrooms, Roman slavery sits beside students' learning about American slavery. Fix: add "one published framework for teaching slavery to middle-grade students, written with descendant communities" to the study list, plus a historian of ancient slavery (Scheidel is listed, unread).

### 10.4 Cross-reference rows for 3b and 3c (minor, skeleton, process)

The rows say "The skeleton expanded parent code ...". Keep the rows, cut that sentence (CW4). Structure pass: the skeleton lists only the parts days.csv assigns to the unit.

Content checks passed: 509, 264 BCE, 117 CE, 44 and 27 BCE; Eurysaces's inscription (baker, contractor, attendant; birth status not stated); Naevoleia Tyche; Res Gestae 34; maniples as Republican.

## Unit 11 (s11, days 134 to 144): what held Rome together

### 11.1 Exit tickets sit in field 2 with no wrong-answer column (minor, plan)

The exit table is under field 2 and its last column mixes answer and error letter. Fix: move it to field 5 and split into "Prompt and answer" and "Wrong answer and error", as in s10.

### 11.2 Item 6 tight; item 7 filed under 3c (minor, plan)

Item 6 asks two spread routes, Romance development, two root inferences and script versus language in 7 minutes; drop the Romance-development part (covered by the day 141 exit). Item 7, the closing claim, should have its own row, not sit inside the MA.7.T4c.3c row.

### 11.3 Pipeline notes (minor, process, REPEAT of CW4)

Content checks passed: the 33 CE case is framed as a credit crisis with deflation labelled illustrative, as days.csv requires; Tacitus 6.16 to 17; Frontinus 17 (the maps of valleys and river crossings); telescope's roots; English's Germanic descent; C3 D2.Eco.12 and 15 own words. The assessment fits 50 minutes exactly.

## Unit 12 (s12, days 145 to 156): Rome's fall and the spread of ideas

### 12.1 Item 3 overloaded (moderate, plan, REPEAT of CW1)

Fifteen minutes for four drawn routes, four mechanisms, three idea types, three continents and a Han and Rome comparison. Fix: drop the Han and Rome comparison from item 3 (it is assessed in the day 153 exit and the day 154 claim) and give its three minutes to the routes.

### 12.2 "Brooks's floor mosaic" (minor, plan, exact citations)

The hook says "Brooks's floor mosaic of Ktisis". Brooks wrote the essay; the mosaic is a museum object. New: "the Ktisis floor mosaic, 500 to 550, shown in Brooks's essay on Byzantium".

### 12.3 No minute plan for teaching days (minor, plan)

Other units give each teaching day's minutes; s12 gives only exits (three minutes). Add one line: "Teaching days: five minutes retrieval, ten teaching, thirty-two supported then independent work, three exit."

### 12.4 Constantine source from one tradition (minor, plan, sensitivity)

The Christian voice is one Orthodox page, where Constantine is a saint. Add a source from another tradition or a historian of the period so the sensitivity agent checks how his conversion is told.

### 12.5 Day 145 flag empty (minor, skeleton, REPEAT of CW3)

Content checks passed: Lactantius 48; 380 as the establishment of Nicene Christianity; Eugippius 20 (Batavis soldiers seeking pay); Ai Khanoum and the Delphic maxims; Eratosthenes's three cities; the counterclaim named but not answered, as the frame sets.

## Settled by the expert

| # | Question | Ruling | Applies to |
|---|---|---|---|
| 1 | Unit 1 when every assumed row is from earlier grades | Field 4 says "none needed; retrieval only"; the day 1 and early retrieval tasks are the start-of-year evidence; no items, no sitting | s01; every course's unit 1 |
| 2 | Reteaching on an assessment day | Never. Directions take at most five minutes; a gap seen the day before is handled that day or recorded for the respond day | s07, s08; all courses |
| 3 | A skill assessed through a teaching day's product before its own teaching day | Model one worked example in the product day's first ten minutes and count only the revised product; no day swap | s05; all courses |
| 4 | Outdated group names in a standard's own-word line | The data line uses current, respectful names; the anchor's wording is quoted only when quoted as the anchor | data/standards; all courses |
| 5 | Exit tickets | Every teaching day has one in field 5, with a prompt, an answer and a wrong answer with its error letter | s05, s11; template |
| 6 | Readiness reteach when the dependent skill returns later | Reteach in the warm-up of the next day that is practice, not first teaching, and before the skill returns | s10 |
| 7 | Pipeline notes | Never in plan text; they go in the Codex write report | all plans |
| 8 | A population or similar figure | Name the measure and date (census count, annual average, mid-year estimate) | s06; all courses |
| 9 | Unit 8 split | Handled; plans name the return day and what to keep (one line) | s08 |

Cited from earlier reads, not re-argued: assessment sizing (grade 4); observations never take the only teaching minutes of a new skill (kindergarten, grade 1); exact citations; current official facts; Tennessee block.

## For the fixer

Edit in this order; no day changes, days.csv untouched.

1. s06: rewrite in UTF-8, restoring every "?" by hand (6.1). Then regenerate the MA.7.T3b.1 line after the data fix (structure pass item 5) and fix the Vietnam line (6.3).
2. s01 field 4: replace the Given line and the three items with "none needed; retrieval only" and rekey the bridges (1.1). Fix the H-1533 citation (1.2), day 6 exit wording (1.4), closing claim (1.5), trim item 6 (1.3).
3. s05: add the exit table for days 52 to 60 (5.1); add the day 56 worked comparison and the day 59 revision note, and change field 5's evidence note (5.2); cut day 56 to five cards (5.3).
4. s07 field 5 and s08 field 5: replace the "directions and targeted reteaching" lines (7.1, 8.1). s08 field 8: add the day 120 return line (8.2).
5. s10: replace the two readiness-reteach lines (10.1); trim items 2 and 5 (10.2); add the slavery-teaching source (10.3); cut the skeleton sentence in the 3b and 3c rows (10.4).
6. Trim assessments: s02 items 3 and 6 (2.2); s03 item 6 (3.2); s04 items 4 and 8 (4.2); s06 item 5b (6.4); s11 item 6 and split item 7 into its own row (11.2); s12 item 3 (12.1).
7. s04: move the percent retrieval to day 46 (4.1); fix the Li Si line (4.3).
8. s09: move the four comparisons to day 108 and the comparison-chart retrieval to 108's opening (9.1, 9.2).
9. s02: add the caste-dispute sources (2.1); state which Upanishad passage is withheld (2.3). s03: check "four relationships" (3.1).
10. s11: move the exit table to field 5 with a wrong-answer column (11.1).
11. s12: fix the mosaic wording (12.2); add the teaching-day minutes line (12.3); add a second Christian source (12.4).
12. All plans: restore the empty or dangling day flags from days.csv (CW3); add field 2 bullets (CW6); delete pipeline notes (CW4).

## For the structure pass

1. scripts/unit_skeleton.py: the sensitivity-flag field drops the whole note when it begins "Sensitivity read"; keep the sentence or the rest of the note (CW3).
2. scripts/unit_skeleton.py: unit 1's Given line says "none needed; retrieval only" when days.csv has no readiness rows (1.1).
3. scripts/unit_skeleton.py: find a readiness check placed on a day outside the units (day 119, a course-level respond day) and fill the Given line from it (s10 field 4).
4. scripts/unit_skeleton.py: list only the lettered parts days.csv assigns to the unit, not every part of a parent code (10.4); tag "used again" from the frame rather than "introduced" (CW7).
5. data/standards/ma-hss-2018.txt: MA.7.T3b.1 own-word line to "the Aboriginal peoples of Australia and the Māori of Aotearoa New Zealand"; scan other lines for outdated group names (6.2).
6. Codex unit-plan brief: write UTF-8 with LF; no pipeline notes in the plan; no reteaching on assessment days; every teaching day gets an exit with a wrong answer; a skill assessed through a product must be taught before it; name the measure of any population figure. Add a checker that rejects "?" inside a word (CW5).
7. Template UNIT-PLAN.md: field 2's Hook, Supporting questions, Closing claim and Teaching moves as bullets (CW6); field 5 requires the exit table with its columns (Settled 5).
8. Plan brief: give the local New York framework path so every unit reads it, not only unit 12 (CW8).

## For Cory

None.
