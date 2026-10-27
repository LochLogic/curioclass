# Path Planner

## One idea
Build your own route from 18 to 28 to one real career by laying training blocks (college, community college, a certificate, a paid apprenticeship, military service, a job) on a ten-year trail map, then press Walk it: a ledger walks the trail year by year and shows when you first earn that career's pay, what school cost, what you earned along the way, and how two routes to the same job end up side by side at 28.

## Not like
- career-cluster-explorer (CTE 6-8, careers, specced): meets 83 careers at a festival; its Clusters view only shows that ways in exist at each education level. Here one career and the years, costs and pay of each way in, built and tested.
- career-match-quiz (CTE 6-8, careers, built): starts from your interests. Here you start from a goal and plan how to get there.
- hospital-shift (9-12, careers, this group): a night inside one workplace. Here years of training, never a workday.
- first-apartment-budget (9-12, money, built): one year of spending. Here ten years of earning and school costs, no budget.
- compound-interest-head-start (9-12, this group): money growing at a rate. Here no interest; the comparison is time and cost.

## Who and how
- Grade 9-12, career and technical education, module "Education and Training Paths".
- Topic line: college, apprenticeships, certificates and military
- Driver: students on laptops; pairs compare routes. 20 to 40 minutes.
- Standards: CTE.Career Clusters (Advance CTE Career Clusters framework 2024: pathways and the education and training each needs).
- Data as of line: "Pay: BLS May 2025. Tuition: College Board 2025-26. Military pay: 2026 tables. Grants: 2025-26."

## Screens and modes
Header: title, topic line, modes (`.seg`): `Build` (default), `Compare`, `Explore paths`; then `Read`, `Motion`, `Sound`.

**Build.** Top of the stage: `Goal` picker, eight career chips with emoji (Content). Stage: a trail map drawn in code on light topographic paper: a winding trail with ten year markers (ages 18 to 28), and a block shelf beside it (Content blocks as rounded tiles, each with an icon and its length in years). Drag a block onto the trail, or select it and press `Add to trail` (keyboard path); blocks snap end to end from age 18. A block can be dragged off, or selected and removed with `Remove`.
- The goal's flag sits at the end of the trail. As blocks go down, a checklist under the map shows the goal's requirements (for nurse: "A nursing degree (associate or bachelor's)", "Pass the licensing exam") and ticks each one the trail meets. When every one is met, the flag moves to the age where the career starts and the remaining years fill with Career years automatically.
- `Walk it` animates a hiker along the trail (about 4 seconds; instant with Motion off) while the ledger fills, one column per year: what you did, school cost after grants, what you earned, and running totals. Final readouts at 28: Earned, Paid for school, Net (earned minus school costs), Age you start the career, and "If you borrowed for all of school: $x" (school costs after grants).
- Panel toggles that change the ledger: `Pell grant` (off by default; on: up to $7,395 a year off tuition, never below $0), `Work part-time while in school` (on: $9,000 a year in school years, "15 hours a week at $15 for 40 weeks"), `Live at home` (a note only: living costs are not counted on any route; the military block notes housing and food are provided).
- `Save as Route A` and `Save as Route B` keep two routes for Compare.
- The career sheet opens from the goal chip (`About this career`).

**Compare.** Route A and Route B as two trails, one above the other, with their ledgers as two lines on one chart (running Net by age, A solid, B dashed, each labeled) and a table of the five readouts. A note names where the lines cross ("Route B catches up at 26"). If either route is missing: "Save two routes in Build to compare them."

**Explore paths.** A table view for looking around without building: rows are the eight careers, columns are the block types, and each cell says whether that block is a way in for that career and how long it takes ("Apprenticeship, 4 years, paid"). Tap a cell: `Build this route` drops the route on the Build trail.

## Content
**Goals** (careers from careers.json; median pay May 2025 from careers.json; requirements and routes):
- Electrician (63,190): a registered apprenticeship (4 years; OOH says 4 to 5) and a license. Routes: apprenticeship; certificate then apprenticeship; military (4) then apprenticeship.
- HVAC technician (61,010): a certificate (1 year; OOH 6 months to 2 years) or an apprenticeship (4 years). Routes: certificate; apprenticeship.
- Registered nurse (97,550): a nursing associate degree (2 years at a community college) or bachelor's (4 years), then the licensing exam. Routes: community college; university; military then university.
- Dental hygienist (98,100): an associate degree in dental hygiene (3 years, counting prerequisites) and a license. Route: community college 3 years.
- Software developer (135,980): a bachelor's degree. Routes: university; community college 2 then university 2 (transfer); military then university.
- Accountant (83,680): a bachelor's degree. Routes: university; community college 2 then university 2.
- Aircraft mechanic (79,870): an FAA-approved school (2 years; OOH 18 to 24 months) or military aircraft maintenance experience, then FAA certification. Routes: certificate 2 years; military 4 years.
- Paramedic (60,600): EMT training then a paramedic program (2 years together). Route: certificate 2 years.

**Blocks** (length, school cost a year, earnings a year while in it):
- Community college (1 to 3 years, set by the goal): $4,150 tuition and fees; earnings $0, or $9,000 with part-time.
- University, public in-state (4 years, or 2 after transfer): $11,950; $0 or $9,000.
- Certificate program (1 or 2 years): $4,150 a year (a community college program); $0 or $9,000.
- Registered apprenticeship (4 years): $0 tuition (most programs are employer paid); pay is a percent of the career's median that rises each year: 50, 60, 70, 80 percent ("an example step schedule; each program sets its own").
- Military enlistment (4 years active duty): $0; pay year 1 at E-1 ($2,407.20 a month), years 2 to 4 at E-4 with 2 years or less ($3,142.20 a month) ("promotion speed varies"); housing and food provided. Afterward the Post-9/11 GI Bill pays in-state tuition at public schools in full (after 36 months of service), so school blocks after it cost $0. Card: "Enlisting is a contract: usually 4 years of active duty within an 8-year total service obligation. You also take the ASVAB test to qualify for jobs."
- Job, no training (any length): $31,200 a year ("full time at $15 an hour, an example").
- Career years (filled automatically after the requirements are met): year 1 at the career's 25th-percentile pay (p25), rising in equal steps to the median by the fifth year, then flat; never below the last apprenticeship year's pay.
- Licensing exams as zero-length milestones on the trail: nursing licensing exam, dental hygiene board exam, FAA mechanic certification, electrician license.

## Interactions in detail
- Rules check: a career starts only when its requirement checklist is all ticked, in order (a license milestone comes after its training). A route that never qualifies by 28 shows "Not qualified by 28" and fills the rest with whatever blocks are on the trail; it never fails silently.
- The trail is exactly 10 years; a block that would pass 28 is refused with "Only (n) years left on the trail."
- School cost a year = max(0, tuition - Pell if on); GI Bill sets it to $0 for school blocks after a military block (the GI Bill card says the benefit also includes a housing allowance, not counted here).
- Earned = sum of earnings in all years; Paid for school = sum of school costs; Net = Earned - Paid for school. Whole dollars; cents in military pay kept until the totals, then rounded.
- Worked values: apprenticeship years for electrician are $31,595, $37,914, $44,233, $50,552 ($164,294 in 4 years); military years are $28,886.40 then $37,706.40 ($142,005.60 in 4 years); university tuition 4 years $47,800, with Pell $18,220; community college 2 years $8,300, with Pell $0.
- p25 comes from the careers engine (`p25` field). If a career's p25 is missing, career year 1 uses 80 percent of the median and the ledger says "estimated".
- Undo (`Ctrl+Z` and an `Undo` button) steps back one block change; `Clear trail` empties it after a confirm.
- Saved routes live on this device (localStorage `path-planner-routes`, try/catch); `Clear saved` removes them.
- Drag uses pointer events with whole-pixel jitter tolerance; every drag has the keyboard path (select, Add to trail).
- Sizes: the trail map is drawn at real pixels per size (a gentle S-curve at wide sizes, a straight vertical trail under 760 px); the block shelf and Walk it stay visible without scrolling at 1366x768; at 680x425 the ledger collapses to the five readouts.

## Look
- Own light `:root` (a trail map): `--paper #f3efe4`, `--panel #fffdf7`, `--ink #23261f`, `--muted #5d6355`, `--line #ddd5c2`, `--btn #2e6b34`, `--head-ink #ffffff`, `--focus #1d4ed8`. Accent `--brand #2e6b34` (trail-marker green). Topographic lines `#e2dac6`; trail `#8a6a3e` dashed; block colors by type with an icon and a label each (school blue `#2f5e9e`, apprenticeship rust `#9a4a1c`, military olive `#55602a`, job gray `#555b63`, career green `#2e6b34`), white text on each at 4.5:1 or more.
- Contrast: accent on paper 5.59:1, on panel 6.32:1; white on accent 6.42:1; ink on paper 14.0:1; muted on panel 6.0:1.
- Differs from career-cluster-explorer (dusk festival, teal), career-match-quiz (cream, navy, coral), workplace-scenarios (lake blue) and the rest of this group.

## Art
none: drawn in code (trail map, blocks, hiker as a simple shape, ledger).

## Voice
Bank voice `knowing-guide` (Sadaltager), "Say in a knowledgeable, friendly way, like a museum curator": a calm guide who knows every route. Different from career-cluster-explorer (upbeat-guide), workplace-scenarios (casual-peer) and every tool in this group. `Curio.voice`, `scope: () => state.mode`. Ledger numbers are on screen only.
- welcomeBuild (how): "Pick a career at the top. Then drag training blocks onto the trail, starting at eighteen."
- walkHow (how, first time the checklist is all ticked): "Your route qualifies. Tap Walk it to see the ten years."
- qualified (event, each time a route becomes qualified; stale if a block changes first): "You start as a (career) at (age)."
- notQualified (event, Walk it on a route that never qualifies): "This route doesn't reach the career by twenty-eight. Check the list under the map."
- saveHow (how, after the first Walk it): "Save it as Route A, then try another way in."
- welcomeCompare (how): "Two routes to compare. Look for where the lines cross."
- welcomeExplore (how): "Tap any cell to build that route."

## Family engine
The careers family engine, described in full in career-cluster-explorer's spec (careers.json from `scripts/careers_data.py`, the shared career sheet, `payText`, `jobsText`, `money`, cluster names). This tool uses the career sheet and helpers for its eight goals, and the Handbook fields `edu` and `ooh` that career-cluster-explorer adds. It adds one field to the same builder: `p25`, the BLS OEWS national annual 25th-percentile wage, May 2025 (data type 12 through `scripts/bls.py`, already supported there), as the early-career stand-in first-apartment-budget uses. It feeds the engine the eight goals, their routes and requirement checklists above.

## Sources
- Median pay May 2025 and 25th-percentile pay: BLS Occupational Employment and Wage Statistics, May 2025, national, via careers.json (https://www.bls.gov/oes/).
- Training lengths and requirements: BLS Occupational Outlook Handbook, 2025-35 edition: Electricians, Heating Air Conditioning and Refrigeration Mechanics, Registered Nurses, Dental Hygienists, Software Developers, Accountants and Auditors, Aircraft and Avionics Equipment Mechanics, EMTs and Paramedics (https://www.bls.gov/ooh/).
- Tuition and fees 2025-26 (public two-year in-district $4,150; public four-year in-state $11,950): College Board, Trends in College Pricing and Student Aid 2025 (https://research.collegeboard.org/trends/college-pricing/highlights).
- Maximum Pell grant 2025-26 $7,395: Federal Student Aid (https://studentaid.gov/understand-aid/types/grants/pell).
- 2026 military basic pay (E-1 over 4 months $2,407.20; E-4 two years or less $3,142.20): Defense Finance and Accounting Service, 2026 military pay tables (https://www.dfas.mil/MilitaryMembers/payentitlements/Pay-Tables/).
- Post-9/11 GI Bill pays full in-state public tuition after 36 months of service: U.S. Department of Veterans Affairs (https://www.va.gov/education/about-gi-bill-benefits/post-9-11/).
- 8-year total military service obligation: 10 U.S.C. 651 (https://www.law.cornell.edu/uscode/text/10/651); the ASVAB: official ASVAB site, U.S. Department of Defense (https://www.officialasvab.com/).
- Registered apprenticeships are paid jobs with wage increases as skills grow: U.S. Department of Labor, Apprenticeship.gov (https://www.apprenticeship.gov/).
- Nursing licensing exam requirement: NCSBN, NCLEX (https://www.nclex.com/).
- Part-time and no-training job pay, the apprenticeship step schedule and career pay ramp: examples made up for this tool and labeled as examples on screen.

## Done when
1. Electrician by apprenticeship: years 18 to 21 show $31,595, $37,914, $44,233, $50,552; career starts at 22; career year 1 is max(p25, $50,552).
2. Nurse by university without Pell: Paid for school $47,800; with Pell $18,220; by community college with Pell $0.
3. Military then university (software developer): years 18 to 21 earn $142,005.60 in total, school after it costs $0, and the career starts at 26.
4. Every goal's checklist ticks only when its blocks and milestones are in order; a route that misses shows "Not qualified by 28".
5. A block that passes 28 is refused with the years-left message; Undo restores the previous trail.
6. Compare draws both Net lines and names the crossing age correctly (recompute from the two ledgers).
7. Every block can be placed and removed by keyboard; drag works with jittered real pointer input.
8. Trail, block shelf and Walk it are visible without scrolling at every STANDARDS.md size; the preview is readable.
9. Saved routes survive a reload and `Clear saved` removes them.
10. How lines once each in five actions in a row; qualified and notQualified every time, dropped when stale.

## Open questions
- The military block is presented as one route among others, with pay, the service commitment card ("enlistment contracts are usually 4 active years within an 8-year total obligation") and the GI Bill, and no recruiting language. Is that the framing you want, or should the military block carry more detail (or less)?
- `p25` is a new field in the shared careers.json (the same question career-cluster-explorer raised for its Handbook fields): extend the live file in place?
