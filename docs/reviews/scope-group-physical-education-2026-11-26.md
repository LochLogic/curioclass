# Scope group read: physical education, 2026-11-26

The four PE band scopes read side by side, as build/scope-writes/GROUP-READ.md asks. Courses:
physical-education-grades-k-to-2, physical-education-grades-3-to-5, physical-education-grades-6-to-8,
physical-education-grades-9-to-12. This read covers only what no single-course read could see; findings the four
course reads and their fix passes settled are not repeated.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/pipeline/briefs/sequence-read.md; build/scope-writes/AFTERCORE-BRIEF.md.
- docs/courses/physical-education/STANDARD.md and APPROACH.md; docs/agents/lenses/physical-education.md;
  data/progressions/physical-education.csv and -edges.md (read by script: assumes, hands_on, model columns).
- All four scope-and-sequence.md files in full; all four days.csv files by Python script (skills, codes, retrieves,
  assess, school_day, notes); the frames for their Models carried and Seams rows, unit 9 of 9 to 12 and the For the
  lead lists; all four -fixes-2026-11-26.md reports.
- docs/courses/CALENDAR.md (PE rows of the check-week table); the DESK-ANSWERS entry "2026-11-26: after-core frame
  calls".
- Health and SEL at the same bands: SEL STANDARD section 7 ("Shared steps", it sits under "Leans on other
  subjects"); the health 3 to 5, 6 to 8 and 9 to 12 scopes for their card and conflict-step wording; the SEL 3 to 5,
  6 to 8 and 9 to 12 scopes for unit names and weeks; health 3 to 5 days.csv for the conflict steps; SEL 9 to 12
  days.csv for the balanced week.
- Scripted checks over the group: every progression row is taught on some day (all 203 are); every one of the 210
  SHAPE ids appears plain on some day (all do; no `~` id is left begun and never owned); every row a later band
  assumes is retrieved or readiness-checked (all are, with the day named); each readiness check's "last used" against
  the one-hop rule; course-level check weeks from school_day against CALENDAR.md (all match).

## Findings

### 1. "Team talk" is a different card in grades 3 to 5 (scope)

- **Both sides.** K to 2 unit 17 starts the team-talk model in health's conflict-step words, "stop, say what happened,
  listen, find a fair way, an adult helps when words do not work" (days 183, 185, 189, 207). The 3 to 5 frame's Models
  carried row says the same model arrives "in health's conflict-step words". So do the 6 to 8 frame (day 39: "in
  health's conflict-step words") and the 9 to 12 frame (day 285). But the 3 to 5 days print team talk as SEL's talk
  turn card, "listen, say back, ask a question, add your idea" (days 49, 103, 181; used on 51, 106, 110, 112, 185,
  187, 190, 203). Health 3 to 5 grows the conflict steps to "stop, calm down, each says their side, find a fair way,
  or walk away and get help" in grade 5 unit 18 (health days 77 to 79), and PE 3 to 5 unit 18 settles calls in the
  same grade with the talk turn card.
- **Why it matters.** One name on two cards. A child who learned team talk as conflict steps in grade 2 meets a
  listening card under that name in grades 3 to 5, then conflict steps again in grade 6. The adult-help step drops out
  for three years, in the units where disagreements over calls are taught (S3.5.5). It also breaks the one-card rule
  of SEL STANDARD section 7.
- **Fix.** In 3 to 5, team talk quotes the conflict steps: the K to 2 grade 2 form on days 103, 181 and their uses
  until health grade 5 unit 18 grows it, then health's grade 5 form. The talk turn card stays on day 49 as the
  listening card it is, named as SEL's card and not as team talk. Grades 6 to 8 and 9 to 12 print the words wherever
  team talk appears (6 to 8 days 1, 39, 45, 135; 9 to 12 days 8, 47, 50, 285) in health 6 to 8's form, "stop, calm
  down, each says their side, find a fair way, or walk away and get help". The 6 to 8 .md line "PE uses no ...
  talk turn card" can stay, with the conflict steps added to its Shared cards bullet.

### 2. Grade 9's first readiness check tests rows grade 8 used (scope)

- **Both sides.** 9 to 12 day 1 holds a readiness check on g7-effort-aerobic and g7-fitt-principles, "both last used
  in grade 7". But 6 to 8 day 194 (grade 8, unit 15 day 2) retrieves both in its instant activity, and
  g8-fitness-test-track, taught on 6 to 8 days 193 to 202, assumes both. By rule 2 with one hop (settled in the 6 to 8
  fix pass: "a row a later row assumes counts as used in that later row's grade"), their last use is grade 8, the year
  before grade 9.
- **Why it matters.** The rule says a row used the year before opens as retrieval, not a readiness check, and the
  check costs grade 9's first day ten minutes. The 3 to 5 and 6 to 8 fix passes applied this rule. Only the 9 to 12
  pass did not.
- **Fix.** Day 1: clear `assess`, and the ten minutes go back to the hook and first tries. Day 2's retrieval (it already
  retrieves g8-fitness-test-track) adds both rows to `retrieves` and says so in the note. The .md unit 1 paragraph
  changes to match. The other 9 to 12 readiness checks hold (g6-analyze-skill on day 24, g7-dance-ideas on 52,
  g7-skill-fitness-use on 81, g7-rest and g8-tech-judge on 91, g8-culture-matters on 106, g8-outdoor-safety and
  g7-eat-move-well on 120, g8-water on 134): none has a use in the year before.

### 3. The four water units: a missing first step, a misquoted source, and the same tasks with nothing named as new (scope)

- **Both sides.** K to 2 unit 22 (days 229 to 240), 3 to 5 unit 23 (226 to 232), 6 to 8 unit 21 (268 to 274) and 9 to
  12 unit 11 (135 to 141).
  - K to 2 day 230 teaches "reach or throw, don't go" with no call-for-help step and no source. 3 to 5 (day 226,
    "shout for a grown-up first"), 6 to 8 (day 268) and 9 to 12 (day 137) all open with calling for help and cite the
    Palm Beach County "Reach, Throw, Don't Go" page. The 3 to 5 fix pass left this for K to 2 under "For the structure
    pass", but it is a scope fix.
  - 3 to 5 days 226, 227 and 231 cite that page for reaching "from a lying or kneeling base". The page, opened
    2026-11-26, says to reach lying on your stomach and does not mention kneeling. 6 to 8 and 9 to 12 say "lying flat".
  - Every band repeats the same three tasks (life jacket "buckle, zip, check", reach to a target, throw to a target)
    and sends home the same "family water-safety card" (K to 2 day 236, 3 to 5 day 230, 6 to 8 day 271, 9 to 12 day
    139). No scope says what its band adds. Cold-water risk is taught in both 6 to 8 (day 268, and on the grade 8
    year-end check day 287) and 9 to 12 (day 137).
- **Why it matters.** For a young child, calling a grown-up is the step that matters most, and K to 2 is the only band
  that leaves it out. A misquoted safety source is the kind of fact the safety read is meant to catch. And four near
  copies of one unit and one card, with no new step named, read as repetition to a teacher and to a family.
- **Fix.** K to 2 days 230, 231 and 238: the cue becomes "shout for a grown-up, then reach or throw, don't go", with
  the Palm Beach source line. 3 to 5: change "a lying or kneeling base" to "lying flat". Each band's .md water
  paragraph names its new part in one line: K to 2, fastening plus a grown-up first; 3 to 5, the buddy rule and the
  strokes shown on the floor; 6 to 8, choosing reach or throw for a scene, plus cold water; 9 to 12, hypothermia,
  currents and planning an outing's water safety, with day 137 retrieving 6 to 8's cold-water rule rather than
  teaching it new. The family card names its band's new step, so the four cards differ.

### 4. Records are handed on and never picked up (scope)

- **Both sides.** K to 2 day 240 hands "the band's records on to grades 3 to 5", but 3 to 5 day 2 has "each child
  starts a private skill sheet". 3 to 5 day 240 sends "three-year records ... on to grade 6", and no 6 to 8 day names
  them. 6 to 8 day 288 hands "the band's records to grade 9", and no 9 to 12 day names them. Inside the 3 to 5 band
  the skill sheet does travel (days 80, 137, 160, 237).
- **Why it matters.** The handoff exists on one side only. A grade 6 teacher builds day 2's groups from a readiness
  check, while the child's own three-year sheet sits unused. Growth against the student's own earlier work is a lens
  point.
- **Fix.** Name the pickup. 3 to 5 day 2: "the K to 2 record, where the school kept it, sets the first groups; each
  child starts the skill sheet". 6 to 8 day 2: "each student reads the grade 5 skill sheet and circles one cue". 9 to
  12 day 2: "the grade 8 record and private fitness plot, where kept, open the effort log". Each adds "where a child
  has no record, nothing changes".

### 5. A family's own game is handled four ways (scope)

- **Both sides.** K to 2 day 157 keeps a family games book: an optional page, only with family consent, no day cost.
  3 to 5 day 157 drops the family-shared game because "family consent and a source check per game do not fit a day".
  6 to 8 unit 22 keeps a family activity story, optional and at home, only with consent. 9 to 12 day 112 lets a
  student make "a game their family plays" the scored two-culture case, "only by the student's choice", with no source
  check. Yet 9 to 12's own unit 22 (days 283, 290) allows a family game only "where its source says it is open to be
  taught", with the sensitivity agent reading it first.
- **Why it matters.** APPROACH.md's cultural rule (each cultural claim checked against a source before a unit names
  it) is applied by 3 to 5 and by 9 to 12 unit 22, and skipped exactly where a family game is scored. A student's
  write-up could present a sacred or ceremonial practice as a game.
- **Fix.** 9 to 12 day 112 and the frame's unit 9 Candidate cell get the unit 22 wording: "a family game only where
  its source says it is open to be taught; no sacred or ceremonial game; the teacher reads the source with the
  student". The frame cell is wording only. The 3 to 5 drop stands; K to 2 and 6 to 8 stay as they are (unscored, at
  home, with consent).

### 6. Sepak takraw is both confirmed and not confirmed (scope)

- **Both sides.** The 9 to 12 .md Sensitivity bullet says sepak takraw "is confirmed at a Southeast Asian body's own
  page". Days 107 and 111 and the frame's unit 9 cell say "the sensitivity agent still confirms sepak takraw at a
  Southeast Asian body's own page". The .md's "Sources not loaded" says unit 9's sources were not opened this run.
  The ActiveSG page the frame cites opened on 2026-11-26: a Singapore government sport platform that gives basic play
  (three a side, no hands or arms).
- **Why it matters.** Across the group, a cultural pick stays a candidate until the sensitivity agent confirms it (K
  to 2 dances, 3 to 5 unit 8, 15 and 16 picks, 6 to 8 cumbia and capoeira, 9 to 12 bhangra). A writer reading the .md
  would skip that step for sepak takraw.
- **Fix.** The .md bullet says what the days say: the rules are sourced to ActiveSG (opened 2026-11-26), and it stays
  a candidate until the sensitivity read.

### 7. Heart rate is counted three ways, and the neck caution is in one band (scope)

- **Both sides.** 3 to 5 day 81: count to ten at the wrist or neck, no beats per minute, with "at the neck, press
  gently with two fingers on one side only (from memory)". 6 to 8 day 25: wrist or neck, "count fifteen, times four",
  with no neck caution. 9 to 12 unit 1 (days 1 to 3): "count ten seconds, times six".
- **Why it matters.** A student changes method in grade 9 with no reason given, and the one safety line is lost after
  grade 5. Drift of this kind is what a cross-band read is for.
- **Fix.** Pick one count from grade 6 on. My pick is "count fifteen, times four", because 6 to 8 day 25 already ties
  it to the grade 6 ratio lean. 9 to 12 day 1 retrieves it, and a ten-second count is shown as a quicker option for
  between intervals. 6 to 8 day 25 and 9 to 12 day 1 carry 3 to 5's neck line, still "from memory" for the safety
  agent.

### 8. Reduced paths are counted differently, and two bands lack a shorter period (scope)

- **Both sides.** K to 2 and 6 to 8 each have "A shorter period" (20 to 25 minutes; 35 to 40 minutes). 3 to 5 and 9
  to 12 have none, though the sequence-read bar asks for one in every scope. For "a year about 10 days short", K to 2
  drops 5 sessions and 6 to 8 drops 6 (three a week), each counted in whole sessions. 3 to 5 names 5 fold-in days but
  counts "25 minutes each, 125 in all". 9 to 12 names 10 fold-in days a year (450 minutes), though at 2.5 sessions a
  week ten school days is about 5 sessions.
- **Why it matters.** A school runs the same calendar cut across all four bands and gets two different answers. 9 to
  12 cuts twice the content it needs to, and the 3 to 5 sum does not match the sessions lost.
- **Fix.** 3 to 5 adds "A shorter period" (25 to 30 minutes: warm-up and cool-down 2 minutes each, the closure watch
  kept, one-check-day units hold the rotation and the knowledge task). 9 to 12 adds one (35 to 40 minutes, as 6 to 8
  words it). 3 to 5 counts its fold-ins as 5 sessions not met, 175 minutes. 9 to 12 names the first 5 of its 10
  fold-ins for a 10-day loss and keeps the other 5 for a 20-day loss.

### 9. Conduct reviews outside the owning unit are coded three ways (scope)

- **Both sides.** The K to 2 fix pass settled "a reused S3 conduct code outside its owning unit takes `~`", and listed
  its reuse as "All PE bands". K to 2 writes `~` (days 19, 38, 74, 118, 142 and others). 6 to 8 writes `~` only across
  years (days 131 to 284) and leaves same-year conduct reviews uncoded (days 62, 76, 90: "conduct recorded" in the
  note only). 3 to 5 codes none ("the conduct mark reviews S3.5.3 or S3.5.4 ... with no claim"; days 41, 61, 89 mark
  conduct with no S3 id). 9 to 12 day 47 writes "(S3.12.2 review)" in the note only.
- **Why it matters.** A settled rule applied in one band and not the others. A later script or unit plan that counts
  conduct evidence by id will see none in three bands.
- **Fix.** Each band writes the reviewed S3 id with `~` on the day that marks it (3 to 5 days 41, 61, 89 and the
  rest; 6 to 8 same-year conduct days; 9 to 12 days 47 and 50), and says so once in the .md assessment bullet.

## What holds

- Every progression row is taught; all 210 SHAPE ids appear plain on a day; no begun `~` id is left without its owner.
- Every row a later band assumes has a named retrieval or readiness day. The 3 to 5 and 6 to 8 readiness checks are
  right under the one-hop rule (g1-world-games 153, g2-foods-energy 196, g3-strike-tools 205, g2-water-skills 225;
  g4-object-ideas and g3-stay-safe-own day 1, g5-food-drink 174, g5-water-skills 267, g4-world-activities 274).
- Course-level check weeks in all four days.csv files match CALENDAR.md's PE rows (K to 2 18/28, 18/28, 17/27; 3 to
  5 18/26; 6 to 8 16/32, 16/32, 15/32; 9 to 12 16/32, grade 12 16/28).
- Calm-down and goal steps cards are quoted in the right band form. The 3 to 5 rule (keep the band-before form until
  the partner course grows it) is applied on days 36 and 67. Health 6 to 8's note that HECAT PA 3, 4 and 6 are taught
  in PE matches PE 6 to 8 units 2, 3 and 20.
- The cultural picks do not repeat across bands. The Virginia reel appears once as a dance (3 to 5) and once as a read
  case (9 to 12 unit 9, which names the link).
- The PE 9 to 12 day 296 citation of "SEL 9 to 12 unit 22's balanced week" is right (SEL day 229 designs one). The SEL
  9 to 12 frame's For the lead 5, which calls it wrong, is stale, as are its other two PE points (day 66 now cites
  unit 1; the PE frame names data/plans/calendar.csv).

## Sources

- Drowning Prevention Coalition of Palm Beach County, "Reach, Throw, Don't Go",
  https://discover.pbc.gov/drowningprevention/Pages/Reach-Throw-DontGo.aspx, opened 2026-11-26 (call for help; reach
  lying on the stomach; throw something that floats; don't go; no kneeling named).
- ActiveSG Circle, sepak takraw rules, https://www.activesgcircle.gov.sg/learn/sepak-takraw/rules-and-regulations-of-sepak-takraw?tab=how_to_play,
  opened 2026-11-26 (a Singapore government sport platform; three a side, no hands or arms).
- UNESCO Intangible Cultural Heritage, Naadam, https://ich.unesco.org/en/RL/naadam-mongolian-traditional-festival-00395,
  opened 2026-11-26 (inscribed 2010; horse racing, wrestling, archery; ritual praise songs): 6 to 8's line holds.
- National Weather Service, "Cold Water Hazards and Safety", https://www.weather.gov/safety/coldwater, opened
  2026-11-26 (cold shock and hypothermia): 9 to 12 day 137 holds.
- Folk Dance Footnotes, Seven Jumps,
  https://www.folkdancefootnotes.org/dance/a-real-folk-dance-what-is-it/1st-generation-dances/childrens-dances-1st-generation-or-living/seven-jumps-l-syvspring-denmark-de-zevensprong-netherlands/,
  opened 2026-11-26 (listed as a children's dance, Denmark and the Netherlands; page body only partly read).
- National Folk Museum of Korea, Encyclopedia of Korean Folk Culture (Mugunghwa, K to 2 unit 14): browser check,
  already open from the K to 2 read; not opened here.
