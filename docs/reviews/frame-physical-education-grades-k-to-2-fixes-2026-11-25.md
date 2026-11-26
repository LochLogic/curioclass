# Fix pass: course frame of Physical Education, grades K to 2 (2026-11-25)

COURSE-RUN stage 3, the one fix pass of the after-core PE pilot. Reads fixed: the fresh expert read
(docs/reviews/frame-physical-education-grades-k-to-2-2026-11-25.md, 13 findings) and the second-model read
(docs/reviews/frame-physical-education-grades-k-to-2-codex-2026-11-25.md, 8 findings). Files changed: the frame,
six notes in data/progressions/physical-education.csv (k-bounce-throw-tries, k-express-feel, g1-calm-steps,
g2-water-skills, g2-foods-energy, g2-talk-problems), and frames.csv, calendar.csv and CALENDAR.md through sync. No
file in docs/courses/physical-education/ needed a change: neither read named one stale, and STANDARD.md 3 rule 3
already holds the kindergarten attempts the frame now teaches.

## Gates

| Gate | Result |
|---|---|
| `python -X utf8 scripts/frame.py sync` | frames.csv 66 courses; calendar.csv 962 rows |
| `python -X utf8 scripts/frame.py check physical-education-grades-k-to-2` | 0 failures (notes: K 74, 1 74, 2 74 unit days; 22 units, 240 days, 222 in units, 18 for checks) |
| `python -X utf8 scripts/progression.py check physical-education` | 203 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 70 files, 0 failures |

Calendar after the fix: every PE check day keeps its week (K and grade 1 weeks 18 and 28, grade 2 weeks 17 and 27),
all off the core check weeks of the same grade. Kindergarten units 5 and 6 now run weeks 19 to 24 and 24 to 27.

## Findings

| Read | # | Applied or rejected | What changed, or why not |
|---|---|---|---|
| Expert | 1 | Applied | Shorter path drops 16 Fluency days a year, at most 3 a unit, never a unit's last Fluency day, never a check, respond, baseline or first-teaching day; dropped by load; the scope names them and confirms every outcome stays taught and checked |
| Expert | 2 | Applied | (a) Unit 18 opens with retrieval on health unit 12's energy-snack sort (grade 2 weeks 1 to 5) and teaches only choosing food and water for play; (b) unit 22 opens with retrieval on health unit 13's water rules (weeks 6 to 10), its days go to the dry-land skills and swimming knowledge; (c) calm-steps is now "not new": SEL's calm-down steps in SEL's words, retrieved in unit 11; (d) Ampe dropped (expert 5). Extended to the same pattern in grade 2: team talk (unit 17) now uses health's conflict-step words, unit 19 retrieves SEL unit 13's rules, unit 10 uses SEL's feelings faces. Row notes changed: g1-calm-steps, g2-foods-energy, g2-water-skills, g2-talk-problems |
| Expert | 3 | Applied | Unit 8 teaches S2.2.3 with an object (ball path, scarf level); unit 21 adds a scarf moved along a path or level (S2.2.4 in full); unit 22 adds floating and kicking shown on the floor (S2.2.12 in full); each knowledge task asks the added part |
| Expert | 4 | Applied, day move changed | k-class-chances (S4.2.8) moved from unit 7 to unit 5. The read's day move (unit 5 to 15, unit 7 to 7) is rejected by evidence: units 5 and 6 must total 22 days to keep the K year-end check on days 68 and 69 (week 28); adding 3 to unit 5 pushes it into week 29, a core check week. Instead unit 5 is 14 days (+2) and unit 6 is 8 (-2, two knowledge rows taught inside moving circuits); unit 7 keeps 10 as kindergarten's dance and expression unit with year-review stations. Each year's checks now sample S1 to S4: K S3 at mid-year (unit 1), S4 at year-end (unit 5); grade 1 S3 (unit 10) and S4 (unit 11); grade 2 S3 (unit 17, unit 19) and S4 (unit 16). The pattern rule is in the checks preamble and For the lead 1 |
| Expert | 5 | Applied | Ampe replaced by Mugunghwa kkochi pieotseumnida (Korea), no-one-out form, spot-checked at Korea's Ministry of Culture, Sports and Tourism page "Korea's Culture of Play" (from Korea.net), with a note that it is never tied to any television show; Doña Blanca with a rotating chaser; Seven Jumps named "a folk dance from Denmark and the Netherlands"; La Raspa with teacher-set partners and no gender roles; unit 21's US pick named: Paw Paw Patch, with an invented name in the verse. Kept two Mexican picks in grade 1 (a dance and a game): the band now spans Europe, Mexico, Korea and the US; the sensitivity agent may swap one |
| Expert | 6 | Applied | Alberta entry replaced by SPHEReS (https://myspheres.ca/en/), opened 2026-11-25 (home page: the University of Alberta's Injury Prevention Centre resource that replaced the Alberta print guidelines); Nova Scotia and CDC marked opened 2026-11-25; "from memory" and "not yet opened" removed |
| Expert | 7 | Applied | "Their frames are not written" replaced with the written health, SEL and visual arts frames, cited by unit and weeks; dance alone stays unguessed, under a Pending marker; old For the lead 5 and 8 removed (settled) |
| Expert | 8 | Applied | Math citation is math grade K unit 1 (days 1 to 18, weeks 1 to 4, K.CC.B.4a), with K.CC.A.1 named in unit 8 |
| Expert | 9 | Rejected (move), recorded | Moving checks to fix after-core clashes is the lead's single calendar pass (CALENDAR.md rule 1, this pass's instruction); the clash list and PE's free weeks are For the lead 6 in the frame |
| Expert | 10 | Applied | "Begun toward" kept only where the owner is later (units 1, 5, 9, 10); every earlier-owned code now reads "used in new settings" (units 9, 10, 12, 15, 17, 21); the gate still sees every `~` code |
| Expert | 11 | Applied | Space bullet: water break and shade on warm outdoor days; new Logic model bullet |
| Expert | 12 | Applied | Assessment bullet: one skill task plus a knowledge prompt per visit on a one-day check; a second skill task is the last Fluency day's closure watch, carried, or a second check day; units 2, 4 and 11 now say which is carried |
| Expert | 13 | Applied | Unit 22: "grade 2 weeks 28, 29, 31 and 32 hold the core year-end checks" |
| Codex | 1 | Applied, paraphrase change rejected | Unit 7 teaches and checks two ways moving helps a child feel well (S4.2.3); k-express-feel note changed; S2.2.4 and S2.2.12 as expert 3. The data/standards paraphrase ("Name ways that moving helps you feel well") already carries the full indicator, so it is not changed, and the file is outside this pass |
| Codex | 2 | Applied | Units 6, 7, 14, 20 name a reviewed motor cue watched at baseline and check (travel and freeze, soft landing, travel and freeze with a speed change, controlled direction change); knowledge prompts added to units 2, 3, 4, 5, 9, 10, 11; unit 12 asks what moving often does to the heart and how it helps health; unit 19 watches a fair choice made in the moment; unit 22 asks why a PE experience mattered; every unit's Ends names one S3 behavior; grade outcomes carry their indicator ids |
| Codex | 3 | Applied as record | The six clashes are listed in For the lead 6, with no check moved (expert 9). The read's For Cory 2 (does rule 1 cover after-core subjects) is not Cory's: CALENDAR.md rule 1 already says no week holds two subjects' checks, so it is the lead's calendar pass |
| Codex | 4 | Applied | "The low-equipment path costs nothing" removed; a Required access bullet names the soft surface (units 2, 9, 15) and real life jackets (unit 22), with substitutes and purchases; costs stay provisional; the ceiling question goes to Cory |
| Codex | 5 | Applied | Unit 5 and k-bounce-throw-tries add repeated hand bounces and a self-turned rope with teacher support, growth marked, no repetitions required; Out reads "mastery of continuous hand bouncing and of the self-turned rope" |
| Codex | 6 | Applied | As expert 1; "one or two a unit" deleted |
| Codex | 7 | Applied (replaced, not dropped) | A replacement was found and opened (SPHEReS), so Alberta's successor stays in the list rather than leaving one guide |
| Codex | 8 | Applied | As expert 7, with the health units the read named plus SEL's (its frame now exists) |

Counts: 21 findings; 20 applied (expert 4 and codex 1 in part, with the rejected part's reason above), 1 rejected
(expert 9's move, recorded for the lead).

## Pattern notes for the other PE frames

- Compute the short path from the band's own dose: (sessions less the short target) Fluency days a year, capped per
  unit.
- Before naming a model or placing food, water, calm, rules, conflict or a cultural game, read the same grades'
  health, SEL, arts and dance frames; where one teaches first in the year, open with retrieval and teach only PE's
  part, in their words.
- Across a year's two checks, sample every standard from units before the check; place S4 rows before the
  year-end check, moving days only inside the window the check weeks fix.
- Every unit's Ends: one skill task (a reviewed cue in concept units), one knowledge prompt, one S3 behavior.
- "Begun toward" only for a later owner; "used in new settings" for an earlier one.
- Name every cultural pick with a source spot-checked, and a no-one-out and no-gender-role form.
- No "costs nothing" claim; a Required access bullet for what substitutes cannot replace.

## Left for the lead

- Calendar pass: the six after-core check clashes (frame, For the lead 6); and whether respond days count (For the lead 5).
- Health K to 2 side: its PE table should cite PE units 6, 12, 18, 22 (it says no PE unit is guessed), add g2-s-outdoor-and-home-safety with PE unit 22, and its unit 14 should open the conflict steps as retrieval on PE unit 17 (same words, PE first in the year).
- SEL K to 2 side: name PE unit 11 (uses SEL's calm-down card), unit 17 (team talk) and unit 19 (rules, after SEL unit 13).
- Dance K to 2 frame, when written, places g1-dance-moves, g1-dance-ideas and g2-dance-sequence against PE units 13 and 21.
- C3 column header for PE (frame, For the lead 3) and the cross_subject choice for after-core links (For the lead 4).
- Paw Paw Patch was not found at the national folklife archive in one search: the sensitivity agent checks it there or swaps it.

## For Cory

- Money: may the complete PE course require mats and child life jackets (borrowed or about $80 bought), and is a per-year PE equipment ceiling of $150 right (about $370 across the band from nothing)?
