# Data Policy Council

## One idea
You hold the pen on a school district's data policy for a new hall-pass app: every clause you set (location, how long data is kept, who sees it, ads, an early-warning AI, family rights) redraws one 12-year-old's school day as the data trail it leaves, five council members lean toward yes or no, and the district's lawyer refuses to send a draft to a vote while any clause breaks FERPA, COPPA or the state's student privacy law.

## Not like
- algorithm-audit (6-8 CS, roleplay): audits one algorithm's outcomes for bias. Here you write the rules for collecting and sharing data, and the early-warning AI is one clause among six.
- ai-evaluator (9-12 CS): tests a model's accuracy on chosen photos. Here no model is tested; the question is whether to collect and use the data at all, and on what terms.
- sorting-showdown, api-playground (9-12, same group): measuring algorithms, and building with APIs. Here there is no code, only a policy and the people it affects.
- capture-the-flag, data-defenders (security): protect data from attackers. Here the threat is ordinary use: what a legitimate app keeps, shows and sells.
- secret-keeper (K), internet-journey (grade 3): what one person should share. Here an institution decides what it collects about everyone.

## Who and how
- Grades 9 to 12, computer science (also civics and government). Module: Ethics, Law and Data Policy (Computing and Society), "Algorithmic bias, data policy and computing law". Topic line: "student data privacy policy and law".
- Driver: students in pairs or small groups on one laptop (one drafts, the others argue as members), or a teacher on a projector running the vote while the class debates each clause.
- 25 to 45 minutes: read the vendor's proposal and its flags (5 min), draft to a passing vote (15 min), pin and compare three drafts and defend one (15 min).
- Standards (CSTA 2026, as listed): HS-ALG-IM-10, HS-DAT-IM-28, HS-SYS-IM-36. CSTA 2017 crosswalk (matched by topic): 3A-IC-29 (explain privacy concerns related to the collection and generation of data through automated processes that may not be evident to users), 3A-IC-30 (evaluate the social and economic implications of privacy in the context of safety, law or ethics), 3A-IC-24 (evaluate the ways computing impacts personal, ethical, social, economic and cultural practices).
- tool.json: driver "students or teacher", minutes "25-45", modes ["Draft", "Compare"], grades_label "Grades 9-12". Kit starter (own light `:root`, see Look).

## Screens and modes
Header (kit): "Data Policy Council", small line "Linden Valley Unified". Mode buttons: **Draft** (opens first), **Compare**. Motion, Sound, Read. Footer line on the stage: "A classroom model, not legal advice."

### Mode 1: Draft
Stage, three bands laid out at real pixel size:
1. **The dais** (top): six nameplates in an arc, five voting members and Counsel (non-voting, at the end). Each voting nameplate: portrait, name, role, a lean bar from no to yes with a marked **Yes line**, and the words "Leaning yes" or "Leaning no". A member's latest line appears in a speech card under the plate when a clause they care about changes.
2. **A day in the data** (middle): Jordan's day (age 12, grade 7) as a timeline from 7:35 am to 9:00 pm with eight events (Content). An event the policy collects is lit, with chips for who can see it, how long it is kept, and ad or sale use; an unlit event shows "not collected". Readout: "Collected today: 4 of 8 moments" (the vendor proposal).
3. **The draft** (bottom left on wide screens): the policy as a short document, one numbered section per clause in plain sentences, rebuilt from the choices. A flagged section has a red margin bar, "Flag" and Counsel's note.

Panel:
- `#hint`.
- **Start from**: **Vendor proposal** (default), **Most private**, **Blank**.
- Six **clause** groups, each a set of option buttons (`aria-pressed`): Location, Keep for, Who can see, Ads and selling, Early warning, Family rights (Content). A flagged option carries a small "Flag" tag once chosen.
- **Ask the room**, **Call the vote** (big), **Pin draft** (to Compare, up to three, labeled A, B, C), **Show the math** toggle (adds each member's points per clause under the lean bars).

### Mode 2: Compare
Stage: up to three pinned drafts as columns: the six choices, flags, the vote forecast (five Yes or No marks with names), and each draft's day-in-the-data strip, stacked so the lit moments line up. Panel: `#hint`, **Unpin** per draft, **Load into Draft** per draft, **Clear pins**.

## Content
Setting (all made up): Linden Valley Unified, a California school district of 900 students, is choosing whether to adopt the Aldermark Pass app (digital hall passes, a lunch account, bus times). The vendor, Aldermark Learning, offers extra features and a free ad-supported version. Hall pass times and lunch purchases are always collected (they are the app).

Clauses (option, then points for Parent, Student, Teacher, Principal, Budget):
- **Location**: L1 No location data (+1, +2, 0, -2, 0). L2 Door check-ins on school grounds only (+1, +1, +1, +1, 0). L3 Phone location during school hours, 8:00 to 3:15 (-1, -2, 0, +2, 0). L4 Phone location all the time (-3, -3, -1, +1, 0).
- **Keep for**: R1 30 days (+1, +1, -1, -1, +1). R2 To the end of the school year (+1, +1, +1, +1, 0). R3 Until graduation (-1, -1, +1, +1, 0). R4 No limit (-2, -2, 0, 0, -1).
- **Who can see**: A1 The student, the family and staff who need it for their job (+2, +2, +1, 0, 0). A2 All district staff (-1, -1, +1, +1, 0). A3 Also the vendor's analysts, under contract, for the district's purposes only (-1, -1, 0, 0, +1). A4 Also the vendor's partner companies (-3, -3, -1, -1, +2) FLAG.
- **Ads and selling**: S1 No ads, never sold, full price (+2, +2, 0, 0, -2). S2 No ads; the vendor may use de-identified data to improve the app, for a discount (0, 0, 0, 0, +1). S3 Targeted ads in the free version (-3, -2, -1, 0, +3) FLAG. S4 Data may be sold (-3, -3, -2, -1, +3) FLAG.
- **Early warning** (an AI that flags students "at risk" from grades and attendance): E1 Off (0, +1, -1, -1, +1). E2 On; a counselor reviews every flag first, and families can see a flag and its reasons (+1, 0, +2, +2, -1). E3 On; flags go automatically to all the student's teachers (-2, -3, -1, +1, 0).
- **Family rights**: F1 See, correct and get a copy of the data, and opt out of optional features (+2, +2, 0, -1, -1). F2 See it and ask for corrections (0, 0, 0, 0, 0). F3 No access (-3, -2, -1, 0, +1) FLAG.

Vote rule (this tool's own model): a member votes yes when their points total 2 or more; a draft passes with 3 of 5. Any flag blocks the vote. Of the 576 flag-free drafts, 156 pass and none is unanimous (computed in Python).

Counsel's flags:
- A4: "FERPA: the district needs a parent's written consent, or the student's once they turn 18, before sharing personal information from education records with outside companies."
- S3: "COPPA: for children under 13, targeted ads need a parent's verifiable consent, and a school can only consent for school use. California's SOPIPA bans targeted ads based on student data."
- S4: "California's SOPIPA bans selling student information, and FERPA limits sharing education records without consent."
- F3: "FERPA gives parents, and students once they turn 18, the right to inspect education records and ask for corrections."
- Blocked vote: "I can't send this to a vote. Fix the flagged sections first."

Members (portraits), and their line for a clause where their points are below 0:
- **Dana Ruiz, parent and PTA representative.** L "Tracking a child's phone is a line I won't cross." R "Why keep it longer than the school year?" A "Only the people who need it should see it." S "My child's data isn't for sale, and it isn't for ads." E "No label should follow a kid without a person checking it." F "Families have to be able to see what's kept." Yes: "I can support this."
- **Malik Owens, student representative, grade 11.** L "Students aren't suspects. Don't track our phones." R "One bad year shouldn't follow us to graduation." A "Not every staff member needs my hall passes." S "We're not the product." E "Automatic flags with no counselor? That's how kids get labeled." F "We should see and fix our own records." Yes: "Students can live with this."
- **Priya Natarajan, grade 7 science teacher.** L "All-day tracking isn't our job, and families won't trust it." R "Thirty days is too short to spot a pattern." A "Partner companies have no business with this." S "I won't put ads in front of my class." E "Early warning should exist, and a counselor should check every flag." F "Families need some way to see this." Yes: "This helps me teach."
- **Tom Becker, principal, Linden Valley Middle School.** L "During the school day I need to know students are safe in the building." R "Thirty days won't cover a full investigation." A "Sharing with partners puts the district at risk." S "Selling data would end this app in a week." E "Early warning helps us reach kids sooner." F "Opt-outs for every feature will be hard to run." Yes: "I can run a school with this."
- **Grace Lee, district budget officer.** R "Keeping everything forever costs storage money." S "Full price breaks my budget." E "The early-warning add-on costs extra." F "Copies and opt-outs take staff time." Yes: "The numbers work."
- **Ana Sorensen, district counsel** (non-voting): the flag lines above, and "No legal flags. It can go to a vote." when clear.

A day in the data (Jordan, 12, grade 7): 7:35 at the bus stop (L4); 8:02 walks in the main door (L2, L3, L4); 10:14 hall pass to the nurse, back 10:26 (always); 11:48 buys lunch (always); 1:30 a quiz grade and attendance reach the early-warning AI (E2, E3; chip "counselor reviews" or "sent to all teachers"); 3:20 leaves school (L4); 4:30 at a friend's house (L4); 9:00 pm at home (L4). Chips: Who can see (A1 "family and staff who need it", A2 "all staff", A3 "plus vendor analysts", A4 "plus partner companies"); Kept (30 days, to June, to graduation, forever); S3 "used for ads", S4 "may be sold"; F3 adds "family can't see this".

Draft text: each section is one sentence built from the option ("2. Keep for: The district deletes app data at the end of each school year.").

## Interactions in detail
- Opens on the vendor proposal (L3, R4, A3, S3, E3, F2): Counsel flags section 4 and Call the vote is replaced by the blocked line. The lean totals then are Parent -9, Student -10, Teacher -2, Principal 3, Budget 3.
- Changing an option updates lean bars (300 ms ease), the day strip, the draft section, and queues the line of the member whose points for that clause changed most (one line at a time; a newer change replaces a waiting line).
- Ask the room: each member leaning no names the one option change that raises their total most, in clause order on ties: "Change Location to Door check-ins and I'm a yes." or, if no single change reaches the Yes line, "Even with No limit changed to the school year, I'm still a no." Flagged options are never suggested.
- Call the vote: the clerk reads the motion, then each plate flips to Yes or No in order with its line (600 ms apart), then "The motion passes, 4 to 1." or "fails, 2 to 3." Changing any option after a vote clears the result.
- Blank start: options unset, lean bars at 0, Call the vote disabled until all six are set (the hint says which are left).
- Pins are for this page load only; nothing is saved. No text entry anywhere.
- Motion off: bars and plates change at once; the vote keeps its 600 ms pacing so the voice stays in step.
- Sizes: at 1366x768 the dais, the day strip and the panel's clause groups (scrolling in the panel) fit, with Call the vote pinned at the panel's bottom. Under about 900 px tall the draft document folds behind a **Read the draft** button. At 760 wide the panel goes below with the clause groups first. At 375 wide the dais becomes a row of five small plates (tap one to see its card) and the day strip scrolls sideways.
- Keyboard: Tab order is Start from, clause groups, Ask the room, Call the vote, Pin, then the dais plates; option groups use arrow keys (radio group).
- `window.__tool = {state, setDraft({L, R, A, S, E, F}), totals(), flags(), vote(), ask(), countPassing()}` for tests.

## Look
- Accent `--brand #1f4e79` (civic navy: header, Call the vote, nameplate rules). Own light `:root`, not the dark 9-12 theme: a daylit council chamber and a printed draft, set apart from its two dark group siblings on purpose (theme-912 class names kept, with light values).
- `--paper #f3f1ec`, `--panel #ffffff`, `--ink #1c2330`, `--muted #555e6e`, `--line #d9d4c8`, `--btn #1c2330`, `--head-ink #ffffff`, `--focus #b45309`. Day strip on `#e3ecf5`. Flags `#9f1239` with the word "Flag" and a margin bar; Yes `#166534` with ✓, No `#9f1239` with ✗.
- Contrast (computed): white on brand 8.66:1; brand on paper 7.67:1; ink on paper 13.96:1; muted on paper 5.79:1 (on white 6.54:1); ink on the day strip 13.20:1; flag red on paper 7.10:1 (on white 8.02:1); yes green on paper 6.32:1 (on white 7.13:1); focus ring 4.45:1 (non-text, needs 3:1). All pass AA.
- Neighbors: sorting-showdown violet and api-playground lemon (both dark), ai-evaluator pink. No celebration: the clerk reads the result.

## Art
Six portraits, Codex (`scripts/gptart.py`), `people: true`, Cory reviews each. One shared style: head and shoulders, flat editorial illustration, plain warm grey background, 1:1, cutout no, shown 72 px in the nameplates and 160 px on a member's card.
- member-dana-ruiz: a Latina mother in her forties in a cardigan, warm, attentive; people: true.
- member-malik-owens: a Black high school junior in a hoodie with a lanyard, thoughtful; people: true.
- member-priya-natarajan: a South Asian woman teacher in her thirties with glasses and a lanyard, lively; people: true.
- member-tom-becker: a white middle school principal in his fifties in a shirt and tie, calm; people: true.
- member-grace-lee: an East Asian woman in her forties in a blazer holding a folder, practical; people: true.
- member-ana-sorensen: a woman lawyer in her sixties with grey hair and a dark suit, serious and kind; people: true.
Jordan is never drawn: the day strip uses icons (bus stop, door, nurse's cross, tray, quiz sheet, house).

## Voice
Bank voice `news-reader` (Rasalgethi), "Say clearly and steadily, like a trusted radio news reader", here the council clerk. Not used by any group sibling or 9-12 CS neighbor. Members' lines are on screen in speech cards (not voiced, so one voice never plays six people). `Curio.voice`, `scope: () => state.mode`.
- w-draft (how, Draft welcome): "The vendor's proposal is on the table. Change any section, and watch the council and the day in the data respond."
- flag (event, a flag appears; stale when that section changes): "Counsel has flagged a section. It must be fixed before a vote."
- clear (event, the last flag is fixed): "No legal flags. The draft can go to a vote."
- ask (how, first Ask the room): "Members who lean no have each named one change that would win them over."
- motion (event, Call the vote): "The council will now vote on the draft."
- passes (event; stale on any change): "The motion passes."
- fails (event; stale on any change): "The motion fails. Ask the room, or change a section."
- w-compare (how, Compare welcome): "Pinned drafts sit side by side. Compare who each one wins over, and what each one collects."

## Family engine
none

## Sources
- CSTA 2026 ids HS-ALG-IM-10, HS-DAT-IM-28, HS-SYS-IM-36 (`data/standards/csta-2026-ids.txt`); CSTA K-12 CS Standards (2017) 3A-IC-24, 3A-IC-29, 3A-IC-30: https://csteachers.org/k12standards/
- FERPA consent before disclosure, the right to inspect and seek amendment, rights passing to the student at 18, the school-official exception for contractors: 20 U.S.C. 1232g and 34 CFR Part 99; U.S. Department of Education, Student Privacy Policy Office, https://studentprivacy.ed.gov/faq/what-ferpa
- COPPA parental consent for children under 13, and schools consenting only for educational use: FTC, "Complying with COPPA: Frequently Asked Questions", section N, https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions
- SOPIPA bans targeted ads based on student data, profiles for non-school purposes and selling student information: California Business and Professions Code 22584, https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=22584
- Data minimization and limited retention as privacy principles: NIST Privacy Framework 1.0 (2020), https://www.nist.gov/privacy-framework ; FTC, "Protecting Consumer Privacy in an Era of Rapid Change" (2012), https://www.ftc.gov/reports/protecting-consumer-privacy-era-rapid-change-recommendations-businesses-policymakers
- Early-warning systems that flag students from grades and attendance: U.S. Department of Education, Office of Planning, Evaluation and Policy Development, "Issue Brief: Early Warning Systems" (2016), https://www2.ed.gov/rschstat/eval/high-school/early-warning-systems-brief.pdf
- The district, app, vendor, members, Jordan, the points and the vote rule are original to Curio Class; pass counts computed in Python (2026-10-27).

## Done when
1. The vendor proposal shows one flag (section 4), a blocked vote, and totals -9, -10, -2, 3, 3.
2. Changing only Ads to S2 clears the flag; totals -6, -8, -1, 3, 1; the vote fails 1 to 4.
3. Then E2, R2, L2: totals 2, 1, 4, 4, 1; passes 3 to 2. Then A1: 5, 4, 5, 4, 0; passes 4 to 1.
4. Most private (L1 R1 A1 S1 E1 F1) totals 8, 10, -1, -5, -1 and fails 2 to 3.
5. Each of A4, S3, S4, F3 raises its own flag text; `countPassing()` returns 156 of 576.
6. Ask the room never suggests a flagged option, and each suggestion it calls a yes really reaches 2.
7. The day strip lights 4 of 8 moments for the vendor proposal, 8 of 8 for L4 with E2, 7 of 8 for L4 with E1, and 2 of 8 for L1 with E1; chips follow the clauses.
8. Pin three drafts; Compare lines up their strips and forecasts; Load into Draft restores one.
9. Every size in STANDARDS.md: the clause groups and Call the vote reachable without page scrolling; 375 wide shows the small plates.
10. Voice: welcome once per mode, ask once, events each time while fresh; members' lines never voiced; Read speaks the hint; console clean; no network requests; the name only as "Curio Class".

## Open questions
- The tool names real laws (FERPA, COPPA, California's SOPIPA) and places the made-up district in California so SOPIPA applies. Keep the real laws, or make the state law generic ("a state student privacy law")?
- Six portraits (five adults, one teen; Codex, for your review). Keep portraits, or use nameplates with icons only?
