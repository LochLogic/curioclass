# Decades Explorer

## One idea
A hallway runs through four rooms, the 1980s, 1990s, 2000s and 2010s, each styled after its decade with a shelf of everyday objects (a corded phone, a pager, a flip phone, a smartphone); in each room the student opens drawers by theme (technology, economy, events, culture, politics), and every item pairs a "then" source from the decade (a headline, a poll, an ad, a government photograph) with a "now" view (a later poll, a retrospective, how the event is taught today); charts along the hallway track real measures across all four decades (internet use, smartphone ownership, real median household income, the cost of college, who votes); for each decade the student marks where today's view differs from the view at the time and why (hindsight, nostalgia, new evidence, new values); at the end the student picks one thread through all four rooms and writes what changed, what stayed the same, and how the present shapes the way we tell it, so an eleventh grader learns to analyze change and continuity across recent decades and how present perspectives shape interpretations of the past.

## Not like
- two-space-races (11, spec): two nations' accounts of 1957 to 1969. Here four decades then and now.
- missing-voices-archive (11, spec): an archive's gaps. Here memory against the record.
- behind-the-podcast (11, spec): one secondary work checked. Here a shelf of then-and-now pairs.
- historians-disagree (7, spec): two historians. Here then versus now.

## Who and how
- Grade 11, Social Studies (U.S. History), module "Modern America". Standards: D2.His.2.9-12 (analyze change and continuity in historical eras), D2.His.7.9-12 (explain how the perspectives of people in the present shape interpretations of the past).
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every item. Controls 44 px or more.
- Four rooms with five drawers each (twenty then-and-now pairs), five hallway charts, the memory check, the thread write-up. Extra: Add the 2020s (students build a fifth room's drawers from sources they find, with a then column only, since "now" hasn't happened yet). tool.json `modes: ["Hallway", "Add the 2020s"]`, `minutes: "30-40"`, `grades_label: "Grade 11"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.2.9-12 | Read the hallway charts and pick one thread through all four rooms | the five charts; the thread write-up | 2, 4 |
| D2.His.7.9-12 | For each pair, mark where now differs from then and why | the then-and-now pair; the memory check with four reasons | 3 |

## Screens and modes
Header (kit): title "Decades Explorer"; `Hallway`, `Add the 2020s`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A long hallway with four doors labeled 1980s, 1990s, 2000s, 2010s. On a shelf by the first door: a corded phone, a pager, a flip phone, a smartphone (drawn generically, no brands). The welcome is queued (`welcomeAfter: true`): "Each decade had a story about itself. We tell it differently now. Open the 1980s door." First hint: "Tap the 1980s door."

**Rooms (focus: the pair).** At 1366x768 the room fills the left with the then-and-now pair right; at 680x425 the pair is a sheet. Five drawers per room: technology, economy, events, culture, politics. Each item pairs a then source (quoted under 15 words, or public domain) with a now view (a later poll, retrospective or how textbooks teach it). Examples:
- 1980s, events: the fall of the Berlin Wall (November 9, 1989); then, surprise in the news; now, taught as the end of the Cold War.
- 1990s, technology: the World Wide Web opens to the public (1991); a 1995 survey finds about 14 percent of adults online; now, taught as the start of a new era.
- 2000s, events: September 11, 2001; then, the day's reporting; now, how it is taught to students born after it.
- 2000s, economy: the 2008 financial crisis (Lehman Brothers fails September 15, 2008); then, headlines; now, research on its long effects.
- 2010s, technology: smartphone ownership rises from about 35 percent of adults in 2011 to about 81 percent in 2019.
- Politics drawers follow one balanced shape in every decade: each president's approval polls at the time beside later retrospective polls of the same president, with no commentary on parties.

**Hallway charts (D2.His.2.9-12).** Five lines across 1980 to 2019 from public data: share of adults online, smartphone ownership (from 2011), real median household income, average cost of a four-year college, and voter turnout in presidential years. Each chart shows its source and marks where its series starts.

**Memory check (D2.His.7.9-12).** For each pair the student marks whether now differs from then and picks a reason: hindsight (we know what came next), nostalgia, new evidence, or new values. A short note per decade explains the reason chosen.

**The thread (the aha).** The student picks one thread (technology, money, events, culture or voting) through all four rooms and writes: "From the 1980s to the 2010s, ___ changed. ___ stayed the same. Today we tell it as ___ because ___." Narrator: "The past doesn't change. The people looking back at it do."

**The end.** The marked pairs, the charts and the thread. `Print` prints them.

**Add the 2020s (extra).** Students build a fifth room with then sources only; the now column stays empty with a note: "Ask again in twenty years."

## Content
- Twenty then-and-now pairs from public sources (government records, Pew, Gallup, Census, NCES, Library of Congress), five charts, the memory check, the thread template.
- Politics items use the same structure for every president; a fresh-agent read checks balance before build.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Rooms open in any order; the thread opens after all four rooms have at least three marked pairs.
- Keyboard: Tab to doors, drawers, the pair, the memory check, the charts and the thread; Enter to open and mark.
- With Motion off doors open without swinging.

## Look
- Accent `--brand` #7a1f8a decade violet (header, doors, charts); gold #f4c542 (the drawer open, a marked pair); paper #f8f0fa; ink #240829; muted #5e5262.
- Contrast (WCAG 2.1, computed): white on brand 8.78:1; brand on paper 7.88:1; ink on paper 16.50:1; muted on paper 6.59:1; ink on gold 11.31:1.
- Never color alone: chart lines carry labels and markers; reasons carry words.
- Different from this batch (gilded bronze, archive teal, suburb green, press red).

## Art
- Local FLUX (`scripts/localart.py`): four decade rooms (4, 16:9) and the shelf of objects (1, 16:9), with no brands, logos, copyrighted characters or music.
- Public domain government photographs where an item needs one (National Archives, NASA, Library of Congress, ids checked at build), each with credit.
- Drawn in code: the charts, doors and drawers.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as the guide walking the hallway and hints; `news-reader` as the reader of then sources. `Curio.voice` with `scope: () => state.mode + ':' + state.room + ':' + state.drawer + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each then source.
- event, whole, each now view.
- how `mark`: "Mark whether now differs from then, and why."
- how `chart`: "Read the hallway chart for this thread."
- how `thread`: "Pick one thread and write what changed."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the hallway, rooms and drawers, then-and-now pairs, the memory check, the thread. Charts may use kit/data-desk.js `Chart` (line) with fixed `xDomain` 1980 to 2019.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Memory check | Mark "hindsight" every time | Each decade's note must explain the reason with a detail from the pair. |
| Thread | Write about one decade | It needs all four decades named. |
| Charts | Skip them | The thread asks for one number from its chart. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Then source (whole), waits; now view (whole); `mark`.
2. `chart`.
3. `thread`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.2.9-12 and D2.His.7.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The Berlin Wall opened November 9, 1989 | Office of the Historian, U.S. Department of State | National Archives, Reagan and Bush libraries | yes |
| The Web opened to the public in 1991; about 14 percent of U.S. adults online in 1995 | CERN, "A short history of the Web" | Pew Research Center, "Internet/Broadband Fact Sheet" | yes |
| Smartphone ownership about 35 percent (2011) to about 81 percent (2019) | Pew Research Center, "Mobile Fact Sheet" | Pew Research Center, "Smartphone Ownership 2011" | yes |
| Lehman Brothers failed September 15, 2008 | Federal Reserve History, "The Great Recession" | Financial Crisis Inquiry Commission Report (2011) | yes |
| Real median household income series | U.S. Census Bureau, Historical Income Tables | Federal Reserve Bank of St. Louis, FRED (MEHOINUSA672N) | yes |
| College cost series | National Center for Education Statistics, Digest of Education Statistics | College Board, "Trends in College Pricing" | yes |
| Turnout in presidential years | U.S. Census Bureau, Voting and Registration tables | University of Florida Election Lab | yes |
| Presidential approval at the time and in later retrospective polls | Gallup, Presidential Job Approval Center | Gallup, retrospective approval polls | yes |
Backed twice: 9. Cut: 0.

Sensitivity note: recent politics and September 11 are present. Politics drawers use one structure for every president (approval then and later, no commentary); September 11 uses government sources without images of victims or the moment of impact. A fresh-agent read for balance is needed before build.

Checks run (Python, scratchpad r20, 2026-11-09): four rooms of five drawers is twenty pairs; every drawer item's then date falls inside its decade; smartphone ownership more than doubled 2011 to 2019; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 room and pair; at 680x425 sheet.
2. Five hallway charts show their sources and start years. (D2.His.2.9-12)
3. Each pair is marked with a reason, and each decade has a note. (D2.His.7.9-12)
4. The thread names all four decades, a change, a continuity and a now. (D2.His.2.9-12)
5. Politics drawers share one structure for every president.
6. No brands, logos or copyrighted music or photos.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no swinging; no network requests.

## Open questions
- Sensitivity flag: recent politics and September 11 (default used: one balanced structure for every president, no commentary on parties, September 11 from government sources without images of victims or impact, fresh-agent read before build).
