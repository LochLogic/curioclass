# Frame fixes: Health, grades K to 2 (2026-11-25)

The one fix pass of COURSE-RUN stage 3 for the health K to 2 band pilot, after the fresh expert read
(docs/reviews/frame-health-grades-k-to-2-2026-11-25.md) and the second-model read
(docs/reviews/frame-health-grades-k-to-2-codex-2026-11-25.md). Files changed: docs/courses/health-grades-k-to-2/frame.md,
data/progressions/health.csv (12 K to 2 row cells), and data/plans/frames.csv, data/plans/calendar.csv and
docs/courses/CALENDAR.md through `frame.py sync`. No check week moved.

## Gates

| Gate | Result |
|---|---|
| `python -X utf8 scripts/frame.py sync` | frames.csv 66 courses; calendar.csv 962 rows |
| `python -X utf8 scripts/frame.py check health-grades-k-to-2` | 0 failures; unit days by year K 24, 1 24, 2 24; 84 days (72 in units, 12 for checks and respond days) |
| `python -X utf8 scripts/progression.py check health` | 207 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 70 files, 0 failures |
| Two-topic recount (scratch script, sensitive rows out) | Standard 2: phw, fn, meh; 3: s, meh; 4: meh, s, t, v; 5: s, fn; 6: phw, pa; 7: phw, fn, pa; 8: meh, s, pa |

## Findings

| Read | # | Finding | Applied or rejected | What changed, or why not |
|---|---|---|---|---|
| Expert | 1 | Checks share weeks with other after-core checks (stagger rule) | Not moved (lead's instruction) | The lead runs one calendar pass across all after-core frames. Clashes listed in For the lead 2 and below, with the weeks free of every check today. Health checks stay off every core check week |
| Expert | 2 | Stale For the lead 1, 3, 7 and Cross-subject notes | Applied | For the lead rewritten: the "Data:" sentences, the frame.py "None" item and the "when SEL and PE are written" item are gone. Both Cross-subject tables now give the PE and SEL unit numbers and school weeks from calendar.csv, and "no unit number is guessed" is dropped. The k-sa-name-feelings condition is now a fact (SEL unit 2, weeks 5 to 10, comes first) |
| Expert | 3 | Standard 3 in one topic once sensitive units go | Applied | g1-meh-tell-a-helper gains `~NHES.S3.2.2` and a note line. Unit 7 says the worry scene practices the help steps. The Standard bullet now gives the two-topic count per standard with sensitive rows out |
| Expert | 4 | S3.2.1, S7.2.1, S4.2.2 and kindergarten standard 8 taught in part | Applied | Unit 4: the two signs of a trusted adult, a sort by them, a sign-card check item and one scripted "Can you help me?" (`~NHES.S8.2.1`). Unit 1: washing protects me and the people I touch, and the check item asks who it protects. Unit 3: listening in two places. Rows k-phw-hand-washing, k-meh-good-listening and k-s-trusted-helpers match |
| Expert | 5 | Bar criterion 4 (norms) has no named place | Applied | The unit shape bullet names one plain-word norm a year with no figure: kindergarten unit 4 and grade 2 unit 13, "most grown-ups do not smoke or vape" (CDC adult tobacco pages, source at the expert read); grade 1 unit 6, the class's own routine tally. Kindergarten unit 4 was picked over unit 1 because a class hand-washing norm states a rule, not what peers really do |
| Expert | 6 | Calm-down tools and step words differ from SEL's | Applied (health side) | Units 3 and 14 use SEL's calm-down card. The SEL paragraph names one feelings chart, one card (SEL's, also PE grade 1 unit 11's) and one I-statement (health's). Row k-meh-calm-body now says the card is shared. SEL's side is in Left for the lead |
| Expert | 7 | Unit 9 and 15 reasons fail the calendar | Applied | Unit 9: "ten weeks of the school year left to try it". Unit 15: the season clause is dropped |
| Expert | 8 | Year-end checks promise carried items they do not name | Applied | Kindergarten, grade 1 and grade 2 year-end rows name their carried items and codes as the read listed |
| Expert | 9 | "With an adult" emergency wording could teach the wrong rule | Applied | Unit 13 and row g2-s-hurt-or-sick-get-help: get an adult first; if no adult can help, call 911, practiced on a paper or toy phone. The HECAT Safety PreK-2 read confirms it at the unit plan |
| Expert | Spot check | Hand washing is 20 seconds, the song sung twice (CDC) | Applied | Unit 1 C3 and row k-phw-hand-washing |
| Expert | Spot check | Child Welfare Information Gateway sexual abuse prevention page not found | Applied | The brief now says the sensitivity read names the exact page, starting from the Prevention page url |
| Expert | Spot check | NHTSA and Poison Help pages returned 403 | Listed | Browser check, For the lead 7 (standing rule 2026-11-22) |
| Expert | Days | Unit 6 should say where the cough-and-wash card's model and pair practice fit | Applied | Unit 6 day 2 models the card and practices it in pairs. No day moved, as the read advised |
| Codex | 1 | S3.2.1 helper qualities and S1.2.6 community health missing | Applied (frame and rows); description sent to lead | S3.2.1 is taught through the row's own two signs (keeps you safe, listens) rather than Codex's longer three-part list: a kindergarten card holds two pictured signs, and the row already sets them. Unit 8 adds how a clean, safe shared place helps everyone who uses it, with a check item; row g1-phw-surroundings matches. data/standards/nhes-2024.txt is outside this pass's files: For the lead 5 |
| Codex | 2 | Doing indicators (S7.2.2, S6.2.5) awarded without observed action | Applied | The End-of-unit evidence bullet adds a teacher record of each child doing the routine or goal action at school, scored on steps, never on health or success. A character's chart alone never stands for a doing indicator. Unit 6 adds a routine record carried into its judgment; unit 15 has every child run a movement-break goal at school. The grade 1 mid-year and grade 2 year-end checks carry those records rather than scoring a character. Rows g1-phw-daily-habits and g2-phw-goal-do-it match |
| Codex | 3 | Goal setting (standard 6) only in personal health | Applied | Unit 15's movement-break goal is the goal plan in the physical activity topic; g2-pa-invite-friends-to-move gains `~NHES.S6.2.5`. The recount above holds |
| Codex | 4 | Kindergarten cost total wrong ($29 for $44) | Applied | Cost line: $14 printing, +$15 tasting, +$15 helmet, $44 with both; supplies ceiling figures corrected |
| Codex | 5 | Stale lead notes (same as expert 2) | Applied | As expert 2. Codex's replacement wording for item 1 (weeks per year) was not kept as a lead item because nothing is left to decide |

Where the two reads disagreed: the expert read noted the calendar clashes as a finding to fix, and Codex said the
frame met its brief and needed shared coordination. The lead's instruction for this pass settles it: weeks stay, the
clashes are listed. On helper qualities, both reads named the same gap; the row's wording settled which signs.

### After-core check clashes (stagger rule, CALENDAR.md rule 1)

- Kindergarten week 12: computer science, health.
- Kindergarten week 27: computer science, health, library.
- Grade 2 week 27: ELD, health, PE.
- Grade 1: none involving health. Weeks free of every check today: kindergarten 9, 10, 19 to 25; grade 2 21 to 25
  and 30.

## Pattern notes for the other health frames

- Count the two-topic rule with the sensitive rows taken out, and write the count per standard in the Standard bullet.
- An indicator that asks the child to do something (S7, S6 "act on") needs a school-based doing record. A character's
  chart stands for understanding only. Score steps, never health or success.
- One plain-word norm a year in a non-sensitive Understanding day, about what people really do. A figure is used only
  from grade 6, where a survey of the age exists.
- Name the carried items of every year-end check by code.
- Before placing checks, read your own grades' core weeks and `frame.py calendar`. Do not copy "ends in week 28":
  grades 3 to 5 core year-end checks run weeks 28 to 32.
- Write the PE and SEL seams from their frames' unit numbers and calendar.csv weeks. Use one shared calm-down card
  (SEL's) and one I-statement.
- Check unit reasons against the calendar (no season words) and sum the cost totals.
- Getting help: name the emergency rule in full (adult first; call 911 if no adult can help).

## Left for the lead

- Stagger clashes above: settle them in the one calendar pass across after-core frames.
- STANDARD.md section 4: add "counted with the sensitive rows taken out (section 5)", with its DESK-ANSWERS line.
- data/standards/nhes-2024.txt NHES.S1.2.6: after checking the 2024 text, it reads "touch personal and community
  health".
- SEL frame: its health seam (line 210) and For the lead 5 can cite health units 3, 4, 7, 9 and 14. SEL grade 1's
  I-statement takes health's words, and grade 2's "I would like ___" is the same request slot. Squeezing hands or
  asking for a break join the calm card only if SEL adds them.
- PE frame: its "After-core courses ... frames are not written" table can cite health units 2, 9, 12, 13 and 15.
- Browser check: the NHTSA car seat page and the Poison Help page (403 to the fetcher).
- Body names L89: the person read of unit 1 day 3 and its family note before publishing.

## For Cory

- Health supplies ceiling (money). Kindergarten costs $14 in printing, or $44 with the optional tasting and a bought
  helmet; grade 1 $17; grade 2 $16. Pick: $30 a year for a class of 30, with the two optional purchases outside it.
