# Sequence read: world-history-ii (World History II, 1800 to today, grade 10, full year), 2026-11-14

Expert cold read per docs/pipeline/briefs/sequence-read.md. Independent of any other read of this scope and sequence.

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/social-studies.md; the social studies part of
docs/ADOPTION-BAR-SUBJECTS.md; docs/courses/social-studies/STANDARD.md; docs/courses/world-history-ii/frame.md (units,
course-level checks, cross-subject, the shared research brief with ELA 10); docs/courses/world-history-ii/scope-and-sequence.md;
data/plans/world-history-ii/days.csv (all 160 rows); data/plans/world-history-ii/source-map.csv (the ETSU base, every
row); the 40 wh2-* rows of data/progressions/social-studies.csv and the grade 9 rows' assumes; the MA.WHII lines of
data/standards/ma-hss-2018.txt; docs/courses/CALENDAR.md and the grade 10 rows of data/plans/calendar.csv (ELA 10's
units and checks); docs/pipeline/briefs/sequence-write.md rule 2; the earlier sequence reads of this date (not the Codex
reads).

Gates: `plan.py check`: sequence world-history-ii 0 failures, frame 0 failures. `frame.py calendar`: no break; weeks 8 to
9, 18 to 19 and 32 as the frame sets. `stale.py check`: 0 failures. Every unit and check in days.csv matches
data/plans/calendar.csv. A script check: every MA.WHII code and lettered part appears on at least one day.

## Verdict

A strong year: eleven units in time order, every MA.WHII code and lettered option on a named day and in its unit's
end-of-unit assessment, genocide and hard history taught plainly with each community's own institutions named for the
sensitivity read, the shared research product placed exactly on the brief's milestones with ELA 10, and the ETSU base
placed section by section. The biggest risk is one line the standard and the values rule both depend on: day 114 gives
the Palestinians' "loss of land and flight" without the cause MA.WHII.T5.7d names, so a writer would build the one most
contested day of the year with one telling short. The one change that matters most: rewrite day 114's goal to carry
expulsion and flight both (finding 1); next, give the Herero and Nama genocide room of its own (finding 2).

## Findings, most serious first

### 1. Day 114 drops the cause MA.WHII.T5.7d names (moderate; firm). LAYER sequence. REPEAT yes (a code taught in part, WGAC I finding 5)

**What is wrong.** MA.WHII.T5.7d asks students to describe how Israeli military action caused Palestinians to lose land
and become refugees; T5.7e, how neighbouring Arab states rejected the UN decision and invaded. Day 114's goal names "the
Arab states' rejection and invasion" with its agent, but only "Palestinians' loss of land and flight" without one.

**Why it matters.** A busy writer builds from the goal line. Read as written, one side's account names who acted and the
other names only what happened, which is both a standard part not carried and a one-sided telling (lens: a contested
event given one telling). Historians working from the archives (from memory: the Israeli "new historians" and
Palestinian historians alike) record both expulsion by Israeli forces and flight in the fighting; values rule (b) lets
the evidence say so plainly.

**Fix (data/plans/world-history-ii/days.csv row 114).** Goal: "Explain the 1947 partition vote and the war of 1948 (the War
of Independence and the Nakba) from more than one account: the Arab states' rejection and invasion; Palestinians' loss of
land and homes through expulsion by Israeli forces and flight from the fighting; and Jewish refugees from Arab countries
after it". The note keeps "every contested event carries more than one account; maps dated and sourced". Settled by the
expert (wording inside the standard).

### 2. Day 32 holds a genocide among four topics (moderate; likely). LAYER sequence. REPEAT yes (hard content crowded into one day, grade 2 finding 2)

**What is wrong.** Day 32 carries the Berlin Conference, the Congo Free State, the Herero and Nama genocide, Adwa, and
(by its note) ETSU chapter 8's African states before the scramble. Two of the five are mass killing. Day 36 ("three
answers to empire by the people ruled: resisting, negotiating and governing") has room, and both the Herero and Nama
rising of 1904 and Adwa are answers to empire.

**Why it matters.** A genocide given a fifth of a lesson becomes a line on a list, which the lens and BASELINE rule 5
warn against, and the Congo day already has the hardest images-policy note of the unit.

**Fix (days.csv rows 32 and 36).** Day 32 keeps African states before the scramble, the Berlin Conference and the Congo
Free State. Day 36's goal becomes "Compare three answers to empire by the people ruled (resisting, negotiating,
governing), with Ethiopia's victory at Adwa and the Herero and Nama rising of 1904 and the German genocide that answered
it"; its note takes over day 32's sensitivity line for the Ovaherero and Nama authorities. MA.WHII.T3.3 stays on both
days. Settled by the expert (a swap inside the unit).

### 3. The informed action has no day to act or look back (moderate; likely). LAYER sequence. REPEAT yes (informed-action timing, Government and US History II reads)

**What is wrong.** Day 153 assesses options; day 154 "each student decides whether and how to act". No day takes the
action, and none looks back on it. The bar's item 8 asks students to apply what they concluded to a real problem near
them; deciding is not applying.

**Fix (days.csv rows 154 and 157; scope-and-sequence.md unit 11 arc).** Day 154: "Informed action, step 2: decide, then
take the action through an adult (or record a reasoned choice not to act), at the scale nearest the student". Day 157
note adds "look back on the action: the response or its absence so far, and what the student would do next; no visible
change is needed for the action to count". Settled by the expert, the same call as the US History II and Government
reads.

### 4. Check 1 repeats unit 3's two-scale map task three days later (minor; likely). LAYER sequence. REPEAT yes (Civics, WGAC I and II finding 1)

**What is wrong.** Day 38 (unit 3 assessment) holds "a two-scale map task and an unseen source"; day 41 (check 1, day 2)
is "a map and data task at two scales across units 1 to 3". Day 37 already answers the unit question on a map at two
scales.

**Fix (days.csv row 39, day 38).** Day 38 goal: "End-of-unit assessment: unification, the causes and impact of empire and
its cultural effects, with an unseen source". The two-scale map is tested once, on day 41, across three units.
Settled by the expert.

### 5. Day 117 leans on grade 5 and 8 rows with no readiness check (minor; firm). LAYER sequence. REPEAT yes (readiness calls in the Civics, WGAC II and grade 5 reads)

**What is wrong.** Under the settled rule, a row from the year before (grade 9) or earlier this year opens as retrieval;
any other earlier-grade row the unit assumes opens the unit with a readiness check. Day 117 retrieves "grade 5 and 8 civil
rights laws" (ss5-civil-rights-movements, ss8-civil-rights-laws); neither is used in grade 9. Every other lean is right:
the World History I rows are from the year before, ss8-civic-action (wh2-global-problems) was used in grade 9 (World
History I day 13), and the science and math leans are cross-subject retrievals.

**Fix (days.csv rows 108 and 117; scope-and-sequence.md readiness paragraph).** Day 108: assess `readiness`; note adds
"readiness: ss8-civil-rights-laws, ss5-civil-rights-movements (not used in grade 9), used on day 117". Day 117 note:
"uses day 108's readiness check". The scope and sequence's paragraph "No unit opens with a readiness check" becomes "Unit
8 opens with a readiness check on the grade 5 and 8 civil rights rows day 117 uses; every other earlier row is from World
History I or used there, and opens as retrieval." If the lead prefers, add the two rows to wh2-social-movements' assumes
in data/progressions/social-studies.csv so the progression says what the day uses.

### 6. A school teaching the course alone gets one research launch day (minor; judgment call). LAYER sequence. REPEAT new

**What is wrong.** For the lead 1 is right that unit 11 starts on day 145, the last day of week 29. In a paired school
the question and source plan are made in ELA that week (day 142's note). A school without ELA 10's project finds and judges
five sources on day 145 and drafts on day 148, with two content days between.

**Why it matters.** The research cycle is wh2-research-argument's whole point; a thin launch gives a thin report.

**Fix (my call: no frame change).** Cutting unit 10's survey day, as the lead item offers, would fold eight lettered parts
of MA.WHII.T7.1 into the terrorism day. Instead, days 146 and 147 notes add: "each student reads two of their own
sources against today's content and logs them; the source list may grow to the draft day". Unit 11's questions are the
global problems these two days teach, so the content days double as research time without losing content. Settled by
the expert; For the lead 1 is answered by it.

### 7. The source map leaves order and some days unrecorded (minor; firm). LAYER base text. REPEAT yes (the World History I read of this date, finding 8)

**What is wrong.** (a) ETSU is used out of its own order in places (chapter 8's Russia on day 3 before chapter 6;
chapter 9's Meiji on day 18 before chapter 8's unification on day 27; chapter 11's India on day 109 after chapter 14),
each for the course's time order, but every `order_conflict` cell is blank. (b) The "ours" rows skip days 1, 19 to 21, 34,
35, 48, 49, 54 to 58, 83 to 88, 100, 111 to 116, 122 to 124, 128, 129, 134 to 140 and 145 to 157. (c) Days 29
(etsu-08-imperialism, merged) and 36 (etsu-10-resistance) adapt ETSU by the source map but their notes do not say so,
though For the lead 4 says every adapted day now names its section.

**Fix (data/plans/world-history-ii/source-map.csv; days.csv rows 29 and 36).** (a) `order_conflict` on etsu-08-russia,
etsu-09-japan and etsu-11-india: "used where the course's time order puts it (Peter before the revolutions; Meiji with
industry's spread; India with decolonization)". (b) "ours" rows for the sections listed. (c) Day 29 note adds "base: ETSU
ch. 8 (imperialism, colonialism) as the terms"; day 36 note adds "base: ETSU ch. 10 (African resistance to European
imperialism)". Every base section is otherwise placed or cut with a reason; the cuts (Korea before 1900, France between
the wars, Australia and Southeast Asia, chapter summaries) are sound.

## The readiness versus retrieval call, and the held look-back days

The writer's call is right for every World History I row (used the year before) and for grade 8's civic-action row (used
in grade 9). The one change is finding 5: the grade 5 and 8 civil rights rows day 117 uses get a readiness check on day
108. Cross-subject leans (chemistry, biology, grade 7 science, grade 6 to 8 math) stay retrieval, the reading I took
for all three courses in this run.

No held look-back day shifts a unit. Day 156's audience adaptation sits inside unit 11's days in calendar.csv; every
unit and check matches days.csv. Nothing to sync. For the lead 2 (assessment on day 155, adaptation on day 156, respond
day 157): accept; the brief puts the adaptation in week 32.

## Checked and found right (do not undo)

- Standards in full: every MA.WHII code from T1.1 to T7.2 with every lettered part is on a teaching day and in its unit's
  assessment, apart from T5.7d's cause (finding 1). T1.2 is a short recall on day 3, right after World History I taught
  it in full. T5.3's and T5.11's one-example rule each has a survey day with every option and an in-depth day; T7.1 has
  an anchor case, a second case and a survey of the rest.
- The shared research brief: source list by the end of week 29 (day 145), draft mid week 30 (day 148), talk taught in
  week 30 (day 150), report and talk in week 31 (days 151, 152), history's adaptation in week 32 (day 156). Exactly the
  brief's calendar.
- ELA 10 leans meet: unit 3's colonial texts (weeks 6 to 8) before ELA's "Under colonial rule" (weeks 10 to 12); unit 4's
  critique of historians before ELA's argument unit (weeks 13 to 17); unit 5's propaganda before ELA's speeches (weeks 23
  to 26).
- Hard history: the Herero and Nama, Armenian, Holocaust, Rwandan and Srebrenica genocides each named as genocide with
  court or scholarly backing (values rules a and b); the Holodomor, Nanjing and its denial, the Gulag, partition and the
  Mau Mau camps named plainly; gay men among the Nazis' victims named with dignity; no simulations; a student with family
  ties may choose another case.
- More than one account wherever an event is contested: the revolutions (day 1), Versailles (two historians), the atomic
  bombs (three countries' views), Tiananmen (official account against survivors), Israel and Palestine (each people's
  own institutions), globalization (evidence on both sides).
- Writing grows: sourced arguments in units 1 and 4, the critique of historians, the research report with counterclaims
  and a second audience.
- No unit over 25 days; response time counted once per unit; informed action once a year, the student's choice.

## Lens checklist, scope and sequence layer

| Line | Met? |
|---|---|
| Unit question answerable without the unit's sources, or one defensible answer | Met: all eleven are open |
| History out of time order with no reason | Met: units 9 to 11 are thematic after 1945, each with its reason |
| A contested event with one telling | Met, once finding 1's wording is fixed |
| Writing from sources once a year or never builds short to long | Met |

## Candidate cells

| Cell | Settled in the draft | My read |
|---|---|---|
| Congress of Vienna; Jamaica Letter (unit 1) | Kept, days 6, 10 | Right |
| Meiji industrialization (unit 2) | Kept, day 18 | Right |
| Taiping and self-strengthening (unit 3) | Kept, day 31 | Right |
| Tanzimat; indentured labour (unit 3) | Dropped with reasons | Right |
| Balfour and Sykes-Picot (unit 4) | Kept, day 51 | Right |
| Three roads to war (unit 5) | Kept as the frame of days 68 to 70 | Right |
| Gandhi and the Salt March (unit 5) | Dropped, India option carries Gandhi | Right; students who do not pick India meet him on day 108's survey pages, which should name the Salt March in one line (item-level, for the unit plan) |
| Forced labour and the "comfort women" system (unit 6) | Kept, day 75 | Right |
| Space race; Chile 1973 (unit 7) | Kept, days 96, 98 | Right |
| Congo and Lumumba; UNDRIP (unit 8) | Kept, days 108, 117 | Right |
| Green Revolution (unit 9) | Kept, day 125 | Right |
| Turkey and Iran modernization; recent pandemics (unit 9) | Dropped with reasons | Right |
| UN Sustainable Development Goals (unit 11) | Kept, days 146 and 147 | Right |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 114 goal names expulsion and flight, with each side's actors | MA.WHII.T5.7d; more than one telling | data/plans/world-history-ii/days.csv row 114 |
| Herero and Nama genocide and Adwa moved from day 32 to day 36 | Day 32 held four topics, two of them mass killing | days.csv rows 32, 36 |
| Day 154 takes the action through an adult; day 157 looks back | Informed action was decided but never taken | days.csv rows 154, 157 |
| Day 38 drops the two-scale map task | Check 1 tests it three days later | days.csv row 39 (day 38) |
| Readiness check on day 108 for the grade 5 and 8 civil rights rows | The settled readiness rule | days.csv rows 108, 117; scope-and-sequence.md |
| Days 146 and 147 double as research time | A school alone had one launch day | days.csv rows 146, 147 |
| Source map order notes, "ours" rows filled, days 29 and 36 name their base | Base order kept unless a reason is given | data/plans/world-history-ii/source-map.csv; days.csv rows 29, 36 |

## For Cory

None.

## Sources

- data/standards/ma-hss-2018.txt (Massachusetts 2018, ids and our words): every WHII code checked against the days by
  script and by reading.
- data/standards/c3-indicators.txt: owned indicator ids.
- ETSU, World History Since 1500 (Rankin and Weise, CC BY 4.0), through the source map; not re-opened.
- The 1948 historiography (expulsion and flight both documented in the archival scholarship): from memory, not
  re-fetched; the unit plan's sources should cite it.
- `plan.py check`, `frame.py calendar`, `stale.py check` output of 2026-11-14.

Confidence: findings 1, 5 and 7 firm; 2, 3 and 4 likely; 6 a judgment call.
