# Expert read: unit plans of Kindergarten: Living and Learning Together

Course `social-studies-kindergarten`, units 1 to 6 (s01.md to s06.md). Cold read, 2026-11-14, per
docs/pipeline/briefs/plan-read.md. I did not write these plans and did not open the Codex write notes beyond the
s01 note's "expert attention" line.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, docs/GLOSSARY.md,
  docs/pipeline/briefs/plan-read.md, docs/courses/UNIT-PLAN.md, the social studies part of
  docs/ADOPTION-BAR-SUBJECTS.md (items 1 to 14 and "Fails if"), the Tennessee row of
  docs/courses/social-studies/STANDARD.md.
- In full: docs/courses/social-studies-kindergarten/frame.md, scope-and-sequence.md, s01.md to s06.md;
  data/plans/social-studies-kindergarten/days.csv (64 rows); the MA.K lines of data/standards/ma-hss-2018.txt;
  scripts/unit_skeleton.py (header and build()).
- Earlier reads, for REPEAT tags: docs/reviews/sequence-social-studies-kindergarten-2026-11-14.md.
- Gates: `plan.py check` passes the course (0 failures); `unitplan.py check` passes s02 to s06 (s01 above the tail,
  no failure listed). Prose word counts outside fields 4 to 6, skeleton blocks and the day list: 1,088, 1,273, 1,247,
  1,224, 1,128, 1,209, all under the 1,800 cap. No em dashes in any plan.
- Web checks (this run): the bald eagle national bird law, December 2024
  ([ABC News](https://abcnews.go.com/US/wireStory/biden-signs-bill-officially-making-bald-eagle-national-117097174));
  the 2025 federal proclamation of Columbus Day only ([NPR](https://npr.org/2025/10/11/nx-s1-5570093/columbus-day-trump-proclamation));
  the Russell Lee bakery photograph, "Making pie crusts. Bakery, San Angelo, Texas," November 1939
  ([Library of Congress blog](https://blogs.loc.gov/picturethis/2021/11/a-slice-of-american-life-from-the-fsa-owi-photograph-collection/));
  [The Lion & the Mouse](https://read.gov/aesop/007.html) at read.gov; the
  [Great Seal Hand Press](https://diplomacy.state.gov/items/great-seal-hand-press/) record (accession 2015.0028.01,
  about 1900, public-domain image, eagle on the coat of arms on its exterior); the
  [Cambridgeport School contact page](https://cambridgeport.cpsd.us/explore-cport/contact-cambridgeport-school)
  (89 Elm St.). Not reachable: loc.gov item pages (403), so the three unit 4 Russell Lee titles and contents are
  unverified; the Tennessee 2024 standards PDF on tn.gov (403 to WebFetch and curl).

## Course verdict

The six plans are honest, careful and to the standard on coverage: every lettered part of every Massachusetts code
and every C3 indicator has an observation item with look-fors and a meets and does-not sample, every unit has a
fresh source, the informed action is the class's own, and the sensitivity cautions are mostly right. The biggest risk
is time: the daily two-minute exit tickets ask thirty pre-readers for individual spoken reasons, and in units 1, 4
and 5 the observation slots eat the only teaching minutes of a new skill, so a section writer would build days no
kindergarten room can run. The one change that matters most is a kindergarten exit and observation format (a
picture mark from every child, spoken reasons from a rotating group) applied to all six units; after it, unit 5's
sensitivity study list must be completed to the frame's list before the sensitivity agent runs.

Finding counts: unit 1, 1 serious, 1 moderate, 1 minor; unit 2, 2 minor; unit 3, 1 serious (the course-wide exit
format, sharpest here), 1 minor; unit 4, 1 serious, 2 moderate, 1 minor; unit 5, 1 serious, 5 moderate, 3 minor;
unit 6, 1 moderate, 2 minor; course-wide, 1 serious, 1 moderate, 2 minor, plus 3 skeleton or process findings.

## Course-wide findings

### C1. Exit tickets cannot be run as written in kindergarten (serious)

LAYER plan. REPEAT new.
- **What is wrong.** Every unit reserves "the final two minutes" for an exit ticket and asks to "save each child's
  response, not a group chorus", with most exits asking for a spoken reason ("Why does our big question matter to
  you?", s01 day 1; "How are their ideas alike or different?", s01 day 7; "Explain liberty and justice for all. Does
  everyone have to say the Pledge?", s05 day 47, three questions). Thirty pre-readers cannot each give a spoken
  answer in two minutes, and s03 days 25 and 26 ask each child to make a new block model or a drawn map with a key
  in those two minutes.
- **Why it matters.** The section writer copies these into U3 and the days; the teacher either skips them or
  hears four children, and the next-opening responses (field 6) fire on no evidence.
- **Fix** (s01 to s06, field 5, the paragraph before each exit table; I settle it, see the table below). Replace
  the paragraph's timing sentence with: "Each exit has two parts. Every child marks a picture on paper (point,
  circle, place a token or draw one mark) in the last two minutes; the teacher reads the prompt aloud. The spoken
  'why' is heard from a rotating group of six children a day during supported work, so each child is heard about
  once a week; the record sheet shows the rotation." Then each exit row's first sentence names its mark task. For
  s03 days 25 and 26, the mark tasks are: day 25, "On a new card of a window view beside a photo of a block model of
  it, circle the block that stands for the tree"; day 26, "On a new drawn map with a key, circle the key picture for
  the tree and point to the tree on the map".

### C2. Tennessee is compared in no unit (moderate)

LAYER process. REPEAT new.
- **What is wrong.** All six comparison tables read "Tennessee 2024: blocked, not retried". Bar item 10 asks each
  unit plan to compare California, Tennessee and New York. tn.gov does return 403 to WebFetch and curl (confirmed
  this run), so the writer could not reach it.
- **Why it matters.** "Fails if 10: a unit plan has no comparison table" is not met, but one of three check states
  is missing from every kindergarten unit, and the same block will hit every social studies course.
- **Fix.** Not the plan writer's to fix. The structure pass loads Tennessee's kindergarten lines once (ids and own
  words, as STANDARD.md allows) by a route that works, for one the lead's logged-in browser, and the fixer then
  adds one Tennessee line to each unit's comparison table. Until then each table's Tennessee row should say
  "not yet compared; the 2024 PDF on tn.gov refuses automated reading" instead of "not retried".

### C3. The voice is clipped and abstract in the teaching and carried fields (minor)

LAYER plan. REPEAT new.
- **What is wrong.** Field 2's teaching and carried bullets are strings of short commands with unstated objects:
  "Withdraw teacher-supplied reasons on 9; keep picture references and communication supports" (s01); "Retain unit
  3's source comparison and claim-and-because routine; set aside its map-key" (s04); "access observations",
  "content-prompted", "supplied comparisons". A teacher reading quickly has to decode them.
- **Why it matters.** Small: the readers now are section writers, but the plan's own words become the teacher page.
- **Fix.** For the section writer and any later edit: write each teaching move as one plain sentence with who does
  what ("On day 9 the teacher stops giving reasons; children give their own, and picture cards stay up"). No edit to
  the unit plans now.

### C4. The plans hold only the unit fields of a one-section unit (minor)

LAYER skeleton. REPEAT new.
- **What is wrong.** UNIT-PLAN.md: "A unit with one section has one merged document: the unit fields, then section
  fields 3 to 11." Every kindergarten unit has one section, but the skeleton writes fields 1 to 10 only, and the
  writers parked the exit tickets in field 5 "for the section writer" (U3's place).
- **Why it matters.** A later writer may make a separate u0N-1.md, against the template, or miss the exits.
- **Fix.** See "For the structure pass", item 2.

## Unit 1. Learning together (days 1 to 10)

### 1.1 Day 8 loses its teaching to the observation (serious)

LAYER plan and data. REPEAT yes (the sequence read's finding 3 was the same kind: a day carries more than it holds).
- **What is wrong.** Field 5 gives day 8 "three minutes to model the claim routine ..., fifteen for observation and
  two for the exit ticket". Day 8 is the only teaching day for D4.1.K-2 and D4.4.K-2 (the claim and "Why do you think
  that?"); day 5 only shows the frame once. The days.csv note on day 8 says "The observation task starts here", which
  invited this.
- **Why it matters.** Children are observed on a skill they were taught for three minutes; most will be "not yet",
  and day 10 becomes the real teaching day.
- **Fix.** s01 field 5, "Administration for thirty children": replace "On day 8 use three minutes to model the claim
  routine on a separate teaching card, fifteen for observation and two for the exit ticket;" with "On day 8 teach:
  five minutes to model the claim and a why-question on a separate teaching card, eleven for partner practice while
  the teacher notes talk rules (item 5) for the day's rotating group, two for the exit ticket;". Day 9 then holds
  the fresh-source items for every child in five groups of six (three minutes a group), and day 10's fresh-try
  minutes finish unheard parts, as the plan already says. days.csv day 8 note: replace "The observation task starts
  here" with "The teacher's notes on talk rules (D2.Civ.9) continue; the claim items are heard on day 9".

### 1.2 The start-of-year check cannot run as defined (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** Field 4 uses "ten minutes of the existing start-of-year check on school day 1 or 2". No such
  check exists for this course (the frame: "no unit opens with a readiness check"; unit 1 is asked to define it),
  and the three items are one-to-one exchanges ("Exchange turns twice"), which cannot reach thirty children in ten
  minutes on the first days of kindergarten.
- **Why it matters.** The check either does not happen or eats days 1 and 2; the bridges it selects then fire on
  nothing.
- **Fix.** s01 field 4, replace the paragraph after "**Given:**" with: "Kindergarten assumes no earlier social
  studies row, so the start-of-year check is not a separate sitting. It is the three access look-fors below, noted
  by the teacher during the ordinary work of days 1 to 3 (each child asks or shows a wonder, gives any reason about
  sharing, takes one turn in an exchange), recorded on the record sheet by the end of day 3. Read aloud, demonstrate
  the response choices and record each child's preferred way to communicate. No score bars entry." Keep the table
  and the bridges; in the bridges, item 3's bridge moves from "day 2's opening" to "day 3's opening, before the
  rule cards".

### 1.3 "Following an agreed class rule" is looked for before the rules exist (minor)

LAYER plan. REPEAT new.
- **What is wrong.** Item 2 records following "an agreed class rule" during "days 3 to 9"; the class makes its rules
  on day 5.
- **Fix.** s01 field 5, item 2: "During days 3 to 9" becomes "During days 5 to 9 (and the room's existing routines
  before then)".

## Unit 2. Doing our part (days 11 to 19)

Sound. The informed action is the class's own, has a tie rule, records dissent, and the look-back has evidence.

### 2.1 Day 16's fable and day 16's goal do not match (minor)

LAYER plan and data. REPEAT new.
- **What is wrong.** Day 16's goal is responsible or in-charge characters and "a moment when a rule is made or
  followed". The plan puts the rule moment in The Paper Workshop on day 15 and uses The Lion & the Mouse on day 16,
  which has no rule and whose lion the plan itself says is not legitimate authority. The plan does not say which
  fable character shows responsibility.
- **Fix.** s02 field 10, "Day 16" bullet, add: "The mouse keeps her promise (responsibility) and acts with courage;
  the in-charge and rule moments come from The Paper Workshop of day 15, revisited." days.csv day 16 goal: "Characters
  who are responsible or in charge in an open folktale of honesty or courage, beside our read-aloud, where the rule
  made and followed on day 15 is revisited".

### 2.2 The sensitivity study list is off target (minor)

LAYER plan. REPEAT new.
- **What is wrong.** It lists a Greek-language Aesop library as a "community voice" (a fable has no living community
  at risk here) and omits what the frame names for units 1 to 3 and 2: children without a stable home, and home
  jobs.
- **Fix.** s02 field 10, sensitivity paragraph: replace the Greek-language Aesop link with
  [a youth's account of school and housing](https://schoolhouseconnection.org/article/on-being-noticed-feeling-safe-and-finding-strength-in-community),
  and change "the Greek fable's telling" to "home circumstances and home jobs".

## Unit 3. Where things are (days 20 to 30)

Sound geography; the graph part of D2.Geo.1 is caught (rule 19), the world-map exposure stays exposure, and the
own-state method has two worked states plus the class's own.

### 3.1 Days 25 and 26 hold a model, a graph, observation and an impossible exit (serious, with C1)

LAYER plan and data. REPEAT yes (sequence read finding 3, load).
- **What is wrong.** Day 25 must hold the block model, the picture graph that field 5 adds ("Each child makes a
  simple picture graph"), eight minutes of group observation and an exit that is a second block model. Day 26 holds a
  drawn map with key plus an exit that is another drawn map with key. The graph is not in days.csv, so the section
  writer may not plan it.
- **Fix.** Exits as in C1. days.csv day 25 goal: "Build a block model of the classroom or playground with a hill, a
  pond or trees, and a picture graph of the trees and rocks we counted". s03 field 5, first administration paragraph:
  "reserve eight minutes within supported making" becomes "note the rotating group during supported making; the
  products themselves are the evidence".

### 3.2 Real elementary schools as the address examples (minor)

LAYER plan. REPEAT new.
- **What is wrong.** Field 10 uses Cambridgeport School (address verified this run) and Madison Elementary,
  Olympia (not verified) as the worked addresses. A public curriculum that sends classes to a named school's address
  ties itself to a building that may move, and to a place with children in it.
- **Fix.** Settled below: use each example state's capitol building, a stable public address that also names the
  state.

## Unit 4. Long ago and today (days 34 to 40)

### 4.1 Observation slots take the teaching of the unit's two models (serious)

LAYER plan. REPEAT yes (sequence read finding 3).
- **What is wrong.** Field 5 gives days 36 to 38 "two minutes to reopen, five to teach, five for supported inquiry,
  six for individual observation tasks and two for the exit ticket". Day 36 introduces the timeline and day 37 the
  continuity-change model and the first sourcing of a photograph; each gets five minutes of teaching in a seven-day
  unit. Day 37's observation is a calendar log of time words, a different skill from the day's goal.
- **Why it matters.** The unit's two models, carried to unit 5, unit 6 and grade 1, are taught in ten minutes in all.
- **Fix.** s04 field 5, first "Administration" sentence becomes: "On day 36 use two minutes to reopen, ten to
  teach, six for supported work in which the teacher notes the rotating group's time words, and two for the exit.
  Day 37 holds no observation: two to reopen, twelve to teach sourcing and the two columns, four supported, two exit.
  On day 38 the four-domain comparison uses the teaching and supported minutes, and the rotating group's time words
  are noted during it." Item 2's day 37 calendar record moves to day 38's supported minutes.

### 4.2 The "then" sources may show one community only (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** All three primary photographs (Washing at El Indio, Washing in San Antonio, Water at School) are
  Russell Lee Farm Security Administration pictures from south Texas, the first two plainly of Mexican American
  households in poverty, and every "today" side is an original drawing. The images were not inspected (loc.gov
  refuses automated reading, confirmed this run). A five-year-old comparing documentary photographs of one community's
  hardship with clean drawings of "today" can learn that "long ago" means "those people", which is the whole-era
  judgment the frame forbids.
- **Fix.** s04 field 10, "Primary photographs": add "Choose the three 'then' photographs from at least two
  communities and regions, and confirm each image before keys are written." s04 field 5, the fresh source pairs: the
  "today" sides become photographs, not drawings (settled below), so both columns are real evidence. The sensitivity
  agent's checks already name outsider framing; keep them.

### 4.3 The assessment logs contradict themselves (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** "School Library shows this class arriving at a library session", then "All assessment logs ...
  describe invented school events ... do not present them as records of what this class did."
- **Fix.** s04 field 5, "Fresh materials": "School Library shows this class arriving" becomes "School Library shows
  a pictured class arriving".

### 4.4 Wrong day in "Returns" (minor)

LAYER plan. REPEAT new.
- **Fix.** s04 field 3, "Unit 6, day 52 revisits work then and now" becomes "Unit 6, day 53 revisits work then and
  now" (days.csv day 53).

## Unit 5. Days we remember (days 41 to 51)

### 5.1 The sensitivity study list falls short of the frame (serious)

LAYER plan. REPEAT new.
- **What is wrong.** The frame tells the sensitivity agent to study, for unit 5: both Wampanoag nations' own pages,
  scholarship by Wampanoag and other Native historians, a Native journalists' association style guide, the King
  Center's own materials, a published framework for teaching hard history in the early grades, and each faith or
  cultural community's own pages. s05 lists Aquinnah, Mashpee (which "returned navigation only"), Paula Peters, two
  museum pages, the King Center biography and the two tradition accounts. It has no style guide, no hard-history
  framework and no voice for Columbus Day's other community (5.3), and it lowers the bar to "at least five substantive
  sources".
- **Why it matters.** This is the course's Native and hard-history unit; the agent studies what the plan names.
- **Fix.** s05 field 10, "Sensitivity study required": replace "Study at least five substantive sources, including
  two community voices." with "Study every source the frame names for unit 5: add the
  [Native American Journalists Association reporting guide](https://najanewsroom.com/reporting-guides/), the
  [Teaching Hard History K to 5 framework](https://www.learningforjustice.org/frameworks/teaching-hard-history/american-slavery/k-5-framework)
  for day 43, an Italian American community page on Columbus Day (5.3), and, if Mashpee's pages still return
  navigation only, the tribe's public statements or news pages, recorded as reached or not." (Addresses from memory;
  the agent confirms them.)

### 5.2 The flag's colors are "explained" with no reason (moderate)

LAYER plan. REPEAT new (the sequence read's flag finding was the stars).
- **What is wrong.** Item 4 meets with "The law chose those colors." MA.K.T1.4a asks why the flag has its colors.
  The record answer is: the 1777 resolution sets the colors without a reason; in 1782 Charles Thomson's report gave
  the same colors meanings for the Great Seal (white purity and innocence, red hardiness and valor, blue vigilance,
  perseverance and justice), and people say the flag's colors mean these. The plan has the Thomson report in hand
  and the frame's two bins ("the record says", "people say it means") fit this exactly.
- **Why it matters.** As written, children learn that the colors have no reason, and the standard's "why" is not
  taught.
- **Fix.** s05 field 5, item 4 look-fors: replace "the 1777 law specified the colors but did not explain their
  meanings" and the sample with "colors: the flag law gives no reason; the same colors were given meanings for the
  country's seal, and people say they mean courage, purity and justice. 'The law does not say why. People say red
  is for being brave.'" Keep error C as it is.

### 5.3 Columbus Day is given one side only (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** Exit 41 says Columbus Day "recalls Columbus's 1492 voyage; it does not mark discovery of an
  empty land". Accurate, but for a community that observes Columbus Day the plan gives no meaning the community gives
  it: many Italian American communities keep it as a day of heritage pride. The federal holiday's legal name is
  Columbus Day, and in 2025 the federal proclamation named Columbus Day only, while many states and towns keep
  Indigenous Peoples' Day.
- **Why it matters.** Values rule (c), dignity and openness; a child from a family that celebrates Columbus Day hears
  only a correction.
- **Fix.** s05 field 5, exit 41 answer, add after "empty land.": "Many Italian American families keep it as a day to
  be proud of their heritage." s05 field 10 teacher notes, add: "The federal law names the day Columbus Day; many
  states and towns observe Indigenous Peoples' Day instead or as well."

### 5.4 Day 41 posts the unit's question mid unit 2, and anchors on Aquinnah everywhere (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** The hook posts unit 5's compelling question in week 7, while unit 2's question is live on the
  wonder wall, and pairs it with Aquinnah's account in every state. Bar item 13 (own-state method) and the frame
  ("Native nations named by their own names") point to the nations of the school's own region for Indigenous
  Peoples' Day; Wampanoag belongs on day 42 (the 1621 meal).
- **Fix.** s05 field 2, hook: "show an original calendar card beside Aquinnah's account of its living community. Who
  can a day help us remember? Post the compelling question. Reopen it on 44 with saved holiday cards." becomes "show
  an original calendar card and a picture of a Native nation of our own region today, from that nation's own pages
  (the Wampanoag nations as the worked example where the school has no nearby nation's pages). Ask 'Who does this day
  help us remember?' as the day's question. The unit's compelling question is posted on day 44, with the saved
  holiday cards." (Settled below.)

### 5.5 The Pledge look-for asks a five-year-old to explain every phrase (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** Item 6 requires plain meanings of each phrase, including "republic" and "indivisible", "before
  marking complete". Rule (d), grade level, and the 20-minute day 47 that also holds the anthem.
- **Fix.** s05 field 5, item 6: replace "Add the remaining phrase explanations before marking complete." with "Meets:
  the gist in the child's words (a promise to be loyal to one country, with freedom and fairness for everyone). The
  teacher explains each phrase while teaching; the child is not asked for each one." Exit 47: drop "Ask remaining
  Pledge phrases individually over 47 to 50." (Settled below.)

### 5.6 The traditions items never ask the reason behind a tradition (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** Unit 5 carries the perspective model out ("people do things differently for reasons that matter
  to them"), but items 7 and exits 48 and 49 compare only foods, games and music. No item asks why a family keeps the
  tradition (Hanukkah remembers the Temple lit again; the New Year festival welcomes a fresh year), so model_out is
  not checked.
- **Fix.** s05 field 5, item 7 prompt, add: "Why do these families do this?" Look-fors, add: "one reason from the
  source notes ('They light candles to remember a story of light')."

### 5.7 The bald eagle line is out of date (minor)

LAYER plan. REPEAT new.
- **What is wrong.** Day 46 and item 3 stop at the 1782 seal. Since December 2024 a federal law also names the bald
  eagle the national bird (web, this run).
- **Fix.** s05 field 5, item 3 look-fors, add: "Teacher note: since 2024 a law also names it the national bird." No
  change to what a child must say.

### 5.8 Presidents' Day is a common name, not the law's (minor)

LAYER plan. REPEAT new.
- **What is wrong.** Item 1's sample says the day "remembers Washington and Lincoln". Federal law names the holiday
  Washington's Birthday; many places call it Presidents' Day and remember Washington and Lincoln, or all presidents.
  This is the unit's own "the record says / people say" distinction.
- **Fix.** s05 field 5, item 1 look-fors, add: "Teacher note: the law calls it Washington's Birthday; many people call
  it Presidents' Day and remember Washington and Lincoln."

### 5.9 Juneteenth, a federal civic holiday since 2021, is missing (minor)

LAYER plan and data. REPEAT new.
- **What is wrong.** Day 44 adds Independence Day and Memorial Day as one-sentence picture cards but not Juneteenth,
  a federal holiday since 2021 (the anchor dates from 2018). A current course on "days we remember" names it.
- **Fix.** Settled below: a fourth picture card on day 44, one sentence ("Juneteenth remembers the day in 1865 when
  enslaved people in Texas learned they were free"), flagged for the sensitivity read with day 43.

## Unit 6. Work and trade (days 52 to 61)

Sound and careful on money and means; the bakery source is real and is what the caption says (a commercial bakery,
San Angelo, Texas, November 1939).

### 6.1 Store day cannot run in its minutes (moderate)

LAYER plan. REPEAT yes (sequence read finding 3, load).
- **What is wrong.** Day 58 gives "four to organize exchange, twelve for store work and individual observation",
  hearing every child "about twenty seconds". Thirty children rotating buyer and seller, trading stickers and saving
  a token, plus every child heard, in twelve minutes.
- **Fix.** s06 field 5, "Administration": "On 58 use two minutes to reopen the question, four to organize exchange,
  twelve for store work and individual observation" becomes "On 58 use two minutes to reopen, three to organize, fifteen
  for store work in which the teacher hears the rotating group of six; the rest of the class's choices and reasons are
  heard on day 60". On the thirty-minute route the extra ten minutes go to the store.

### 6.2 "Saving for later" happens inside the same lesson (minor)

LAYER plan. REPEAT new.
- **Fix.** Settled below. s06 field 5, "A saved token permits a later choice within 58, with no extra lesson" becomes
  "A saved token goes in the child's named envelope and buys one item in the first two minutes of day 59".

### 6.3 Bakery caption should carry its place (minor)

LAYER plan. REPEAT new.
- **Fix.** s06 field 5: "Reserve Russell Lee's Making pie crusts, November 1939" becomes "Reserve Russell Lee's
  'Making pie crusts. Bakery, San Angelo, Texas,' November 1939".

## Settled by the expert

| Choice | Reason, in one line | File it touches |
|---|---|---|
| Kindergarten exit format: every child marks a picture; spoken reasons from a rotating group of six a day | Two minutes cannot hear thirty pre-readers | s01 to s06, field 5 exit paragraphs and rows |
| Start-of-year check = three access look-fors noted in days 1 to 3, no separate sitting | No earlier row; one-to-one items cannot fit ten minutes | s01, field 4 |
| Day 8 teaches (5 model, 11 practice); claim items heard on day 9 | Day 8 is D4.1 and D4.4's only teaching day | s01, field 5; days.csv day 8 note |
| Address worked examples: each example state's capitol (Massachusetts State House, 24 Beacon Street, Boston; Washington State Capitol, Olympia, address to verify) | Stable public address that names its state | s03, field 10 and item 5 sample |
| "Today" side of each then-and-now pair is a photograph (the school's own drinking fountain taken by the teacher; a plain washing-machine photograph) | Both columns become evidence, not photo against drawing | s04, fields 5 and 10 |
| Day 41 asks a day question; unit 5's compelling question is posted on day 44 | One compelling question on the wall at a time | s05, field 2 |
| Pledge item meets on the gist | Phrase-by-phrase is above kindergarten | s05, field 5 item 6 and exit 47 |
| Juneteenth picture card on day 44, one sentence, sensitivity-read flag | Current federal civic holiday | days.csv day 44 goal and note; s05 field 2 |
| Saved token spent in the first two minutes of day 59 | "Later" must be a later day | s06, field 5 |
| Day 16 fable stays (the mouse keeps her promise); the rule moment is day 15's read-aloud | Swap inside the unit, no change of standard | days.csv day 16 goal; s02 field 10 |

## For the fixer (exact edits, in order)

1. s01 to s06, field 5: the exit paragraph and each exit row's first sentence, per C1 (s03 days 25 and 26 mark tasks
   as given).
2. s01, field 4: the start-of-year paragraph and item 3's bridge day (1.2).
3. s01, field 5: day 8 timing (1.1); item 2 "days 3 to 9" to "days 5 to 9 (and the room's existing routines before
   then)" (1.3).
4. days.csv day 8 note (1.1); day 16 goal (2.1); day 25 goal (3.1); day 44 goal and note, add "Juneteenth" to the
   picture cards and "Sensitivity read: Juneteenth card" to the note (5.9). Then bring each changed row into the
   plan's "Day list" table so it matches days.csv again (do not rerun the whole skeleton over the written plans).
5. s02, field 10: day 16 bullet (2.1); sensitivity list (2.2).
6. s03, field 5: day 25 and 26 administration sentence (3.1); field 10 and item 5 and 6 samples: capitol buildings
   (3.2).
7. s04, field 5: administration (4.1); "this class" (4.3); fresh source pairs' "today" side to photographs (4.2);
   field 10, the "two communities" sentence (4.2); field 3, day 52 to day 53 (4.4).
8. s05, field 10: sensitivity study list (5.1) and teacher note on the federal name (5.3); field 2 hook (5.4); field
   5 items 1, 3, 4, 6, 7 and exits 41 and 47 (5.2, 5.3, 5.5, 5.6, 5.7, 5.8).
9. s06, field 5: day 58 timing (6.1); saved token (6.2); bakery caption (6.3).
10. Each comparison table's Tennessee row: "not yet compared; the 2024 PDF on tn.gov refuses automated reading" (C2).

## For the structure pass

1. scripts/unit_skeleton.py, field 5: `ass = [r for r in rows if r['assess'] in ('end', 'mid')]` misses the
   kindergarten to grade 2 `observe` value, so the skeleton printed "days.csv marks no end-of-unit assessment day" and
   the writer patched it by hand (Codex's s01 note says so). Add `'observe'` and label it "End-of-unit assessment
   (observation)". REPEAT: every K to 2 social studies course.
2. UNIT-PLAN.md against the skeleton: a one-section unit is one merged document with U3 to U11, but the skeleton
   writes fields 1 to 10 only. Either the skeleton writes U3 (exit questions) and empty U4 to U11 headings for a
   one-section unit, or UNIT-PLAN.md says social studies one-section units get their U fields at PRODUCTION-PATH step 7
   in the same file. Then field 5's "exit tickets for the section writer" tables move to U3.
3. A kindergarten to grade 2 exit and observation format, written once (a course DEFAULTS.md for each K to 2 course,
   or a line in UNIT-PLAN.md rule 11's subject fill): mark part from every child, spoken part from a rotating group,
   observation inside supported work, never inside the only teaching minutes of a new skill. All six plans say "No
   course defaults ... exists"; this is the default they needed.
4. Tennessee: load the kindergarten to grade 12 lines (ids and own words) by a route that works, and record it in
   STANDARD.md, so no unit plan has to try tn.gov again.
5. The skeleton's "Builds on (progression, assumes): none listed" is true across grades but reads as "nothing" for
   units 2 to 6, which build on earlier units of the same year. Add a mechanical line from days.csv: "Earlier units
   in this course whose skills this unit's days cite: ...".
6. Cosmetic: the header's school-day text "34 and 58 and 94 and 102 to 120" should read "34, 58, 94 and 102 to 120"
   (runs_text joins every run with "and").

## For Cory

None.

## What is right and should not be touched

- Every lettered part of MA.K.T1.4 and MA.K.T3.3 and every owned C3 indicator has an item with a meets and a
  does-not sample; the home part of MA.K.T1.2 is checked through a fictional case, never a child's home.
- The informed action in unit 2: two safe proposals from the children, a tie rule, dissent recorded, a look-back
  that may find the change failed.
- Thanksgiving from two accounts (Winslow and Paula Peters), King's work named plainly, the Pledge as a choice under
  Barnette, no costume play, no family disclosure anywhere, equal tokens never earned by compliance.
- Every source invented by the plans is labelled invented; real sources carry rights lines and "image uninspected"
  where true.

## What I could not judge

- The three unit 4 Russell Lee photographs and the Great Seal Hand Press image (loc.gov refused; the hand press page
  confirms an eagle on the object but I could not see the photograph).
- Madison Elementary's address in Olympia (not fetched; moot if the capitol fix is taken).
- Tennessee's kindergarten lines (blocked).

## Sources

- [ABC News, bald eagle national bird law, December 2024](https://abcnews.go.com/US/wireStory/biden-signs-bill-officially-making-bald-eagle-national-117097174): finding 5.7.
- [NPR, 2025 Columbus Day proclamation](https://npr.org/2025/10/11/nx-s1-5570093/columbus-day-trump-proclamation): finding 5.3.
- [Library of Congress, "A slice of American life"](https://blogs.loc.gov/picturethis/2021/11/a-slice-of-american-life-from-the-fsa-owi-photograph-collection/): the bakery caption, 6.3.
- [read.gov, The Lion & the Mouse](https://read.gov/aesop/007.html): 2.1.
- [National Museum of American Diplomacy, Great Seal Hand Press](https://diplomacy.state.gov/items/great-seal-hand-press/): item 3 of unit 5.
- [Cambridgeport School contact page](https://cambridgeport.cpsd.us/explore-cport/contact-cambridgeport-school): 3.2.
- From memory, not fetched this run: the 1777 flag resolution and Thomson's 1782 report on the seal's colors (5.2;
  the plan cites both), the C3 K-2 indicator wordings, Washington's Birthday as the federal holiday's legal name
  (5.8), Juneteenth's federal status since 2021 (5.9).

Confidence: 5.2, 5.7 firm; 5.3 and 5.8 firm on the facts, judgment on the wording; C1, 1.1, 3.1, 4.1, 6.1 likely
(classroom arithmetic); 4.2, 5.4, 5.9 judgment calls.

## For the source list

- tn.gov refuses WebFetch and curl (403) for the 2024 social studies standards PDF
  (tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN Academic Social Studies Standards_25.pdf);
  a kindergarten crosswalk PDF dated June 2024 sits in the same folder. A logged-in browser is the likely way past.
- loc.gov/item and loc.gov/pictures pages refuse WebFetch (403); blogs.loc.gov pages work and often quote the full
  captions.
- diplomacy.state.gov/items/ pages are readable and state their image rights.
