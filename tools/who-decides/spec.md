# Who Decides

## One idea
The student picks a local problem (a dangerous crosswalk near school, a library branch closing, a bus route cut) and their state, then follows a decision path board to find who really decides it (city, county, a special district, the state transportation agency, the school board), when that body meets and when public comment opens under the state's open-meetings law, with a checklist for confirming the details in their own town; next the student weighs past policies on the problem by their intended and unintended results (a speed camera program, a lowered speed limit, a branch merger), and compares ways to act alone or together (public comment, a petition, a coalition, a meeting with staff, a letter to the paper, voting) by cost, reach and likely effect before choosing a plan; finally the student drafts a two-minute testimony, a petition and a short letter to a local paper, each adapted for its audience, with an optional rehearsal recorder that plays back on the device only; a mock hearing mode runs the same steps with a meeting agenda, so a twelfth grader learns to evaluate policies by their outcomes, compare means of change, assess individual and collective action, adapt arguments for audiences outside school, and apply democratic procedures to a real civic decision.

## Not like
- causes-web (12, spec): explaining a problem's causes. Here acting on one.
- movement-strategy-room (11, spec): past national campaigns. Here a present local decision.
- jury-room (12, concept): deliberating a verdict. Here addressing a public body.
- levers-of-power (8, spec): who holds power, grade 8. Here the real path in the student's own state.

## Who and how
- Grade 12, Social Studies (Civics), module "Civic Action". Standards: D2.Civ.13.9-12 (evaluate public policies in terms of intended and unintended outcomes, and related consequences), D2.Civ.14.9-12 (analyze historical, contemporary, and emerging means of changing societies, promoting the common good, and protecting rights), D4.7.9-12 (assess options for individual and collective action to address local, regional, and global problems by engaging in self-reflection, strategy identification, and complex causal reasoning), D4.3.9-12 (present adaptations of arguments and explanations that feature evocative ideas and perspectives on issues and topics to reach a range of audiences and venues outside the classroom using print and oral technologies and digital technologies), D4.8.9-12 (apply a range of deliberative and democratic strategies and procedures to make decisions and take action in their classrooms, schools, and out-of-school civic contexts).
- Format: builder. Driver: one student alone, or the class running a mock hearing (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Three problem cards, a decision path for each of the 50 states and DC, three past-policy cases, six action options, three drafts, the optional recorder. Extra: Mock hearing (the class runs a public hearing with an agenda, a chair, sign-up for comment and a time limit). tool.json `modes: ["Plan", "Mock hearing"]`, `minutes: "45-60"`, `grades_label: "Grade 12"`. Five codes in one tool; each step teaches one or two so it can be run as separate class periods.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.13.9-12 | Rate a past policy's intended and unintended results from its evaluation | the policy case with before and after figures | 2 |
| D2.Civ.14.9-12, D4.7.9-12 | Compare the six action options by cost, reach and likely effect, and choose a plan with a reason | the options table; the plan card | 3 |
| D4.3.9-12 | Write the testimony, petition and letter, each fitted to its audience | the three drafts with audience checks | 4 |
| D4.8.9-12 | Follow the decision path and run the mock hearing's procedures | the path board; the hearing agenda | 5 |

## Screens and modes
Header (kit): title "Who Decides"; `Plan`, `Mock hearing`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A street corner near a school with a faded crosswalk. Three problem cards: the crosswalk, a library branch closing, a bus route cut. A state picker. The welcome is queued (`welcomeAfter: true`): "Something in your town needs fixing. Before you can change it, you have to find who decides. Pick a problem card." First hint: "Tap a problem card."

**The decision path (D4.8.9-12).** At 1366x768 the path board fills the left with the office card right; at 680x425 the card is a sheet. The board shows city, county, special district, state agency and school board. From the state's written guide (who owns which roads, how library boards are chosen, the open-meetings rules on notice and public comment), the path lights the likely office. A checklist tells the student how to confirm it for their own town (the city website's agendas, the clerk's office, the state road map). Every state guide names its law and when it was checked.

**Past policies (D2.Civ.13.9-12).** Three cases with published evaluations:
- Speed cameras in Montgomery County, Maryland: after several years, the chance a driver was speeding more than 10 mph over the limit fell by about 59 percent, and the chance a crash caused a serious or fatal injury fell by about 39 percent; unintended results the student weighs too (complaints about fines, drivers shifting routes).
- Why speed matters: a pedestrian's average risk of death is about 10 percent when hit at 23 mph and about 50 percent at 42 mph.
- A library branch merger with its reported results (visits, travel time, savings), from a real city's audit, checked at build.
- The student marks each result intended or unintended and good or bad for whom.

**Action options (D2.Civ.14.9-12, D4.7.9-12).** Six options in a table: public comment, a petition, a coalition with neighbors or a club, a meeting with staff, a letter to the paper, voting in the next local election. Columns: cost in time, reach, likely effect, who you need. The student picks a plan of two or three and writes why, including one reflection: "What I'd find hard is ___."

**Drafts (the aha, D4.3.9-12).** Three drafts from one argument: a two-minute testimony (a timer shows the read-aloud length), a petition (a clear ask in one sentence), a letter to the editor (under 200 words). Audience checks: does the testimony name the body and the ask; does the petition fit one line; does the letter speak to neighbors. A line on screen: "Your drafts stay on this device." The optional recorder plays the testimony back locally; nothing leaves the device and there is no speech recognition. Narrator: "The same idea, said three ways, reaches three different rooms."

**The end.** The path, the policy ratings, the plan and the drafts. `Print` prints them.

**Mock hearing (extra, D4.8.9-12).** An agenda with a chair, sign-up for comment, a two-minute limit and a vote by the class acting as the board; students read their testimonies.

## Content
- Three problem cards, 51 state guides (50 states and DC) with laws named and dates checked, three past-policy cases with published figures, the options table, draft templates and checks, the hearing agenda.
- No real officials are named; the student fills in their own town's names from the checklist.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Drafts and recordings stay on the device and the screen says so; recording only starts on a tap and shows a clear on-air sign.
- Keyboard: Tab to the cards, the picker, the path, the policy cases, the options, the drafts and the recorder; Enter to choose.
- With Motion off the path lights without moving.

## Look
- Accent `--brand` #3949ab civic blue (header, the path, the options table); gold #f4c542 (the lit office, the chosen option); paper #f1f2fb; ink #0f1433; muted #54576c.
- Contrast (WCAG 2.1, computed): white on brand 7.73:1; brand on paper 6.94:1; ink on paper 16.12:1; muted on paper 6.37:1; ink on gold 11.05:1.
- Never color alone: offices carry names and icons; results carry words.
- Different from this batch (Senate rust, olive drab, brain magenta, web teal).

## Art
- Local FLUX (`scripts/localart.py`): the crosswalk (1, 16:9), a library branch (1, 16:9), a bus stop (1, 16:9), a council chamber (1, 16:9).
- People (illustrated) for residents at the hearing, labeled "illustration" (Gemini, `people: true`, 3; cutout yes).
- Drawn in code: the path board, the table, the timer.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `big-sister` as the guide and hints; `warm-teacher` as the reader of state guides and policy cases. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `state`: "Pick your state."
- event, whole, the decision path result.
- event, whole, each policy case.
- how `rate`: "Mark each result intended or not, and good for whom."
- how `options`: "Choose two or three actions and say why."
- how `draft`: "Write the testimony, the petition and the letter."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the path board, state guide lookup, policy cases, the options table, drafts with checks, the local recorder, the hearing agenda. State guides sit in a marked block `/* WHO-DECIDES STATES: begin */ ... /* end */` with one entry per state and DC, each naming its law and check date.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Policy ratings | Mark everything intended | Each result checks against the case. |
| Plan | Pick all six options | The plan takes two or three, with a reason and a reflection. |
| Drafts | Paste one draft three times | Each draft has its own audience check (length, ask, reader). |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `state`; path result (whole).
2. Policy case (whole), waits; `rate`.
3. `options`.
4. `draft`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.13.9-12, D2.Civ.14.9-12, D4.7.9-12, D4.3.9-12 and D4.8.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Every state has an open-meetings law with notice and public-access rules | Reporters Committee for Freedom of the Press, "Open Government Guide" | National Freedom of Information Coalition, state laws | yes |
| Montgomery County speed cameras: about 59 percent fewer drivers 10 mph over; about 39 percent lower chance of a serious or fatal crash | Hu and McCartt, Traffic Injury Prevention (2016) | Insurance Institute for Highway Safety, Status Report (2015) | yes |
| Pedestrian death risk about 10 percent at 23 mph, about 50 percent at 42 mph | Tefft, AAA Foundation for Traffic Safety (2011) | National Highway Traffic Safety Administration, pedestrian safety | yes |
| Who owns roads and how library and school boards are chosen, by state | U.S. Federal Highway Administration, "Highway Statistics" (public road ownership) | each state's statutes, checked at build | yes |
| Speed safety cameras as a proven countermeasure | Federal Highway Administration, "Proven Safety Countermeasures" | National Transportation Safety Board, "Reducing Speeding-Related Crashes" (2017) | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r21, 2026-11-09): 51 state entries (50 states and DC); death risk at 42 mph is five times that at 23 mph; a two-minute testimony at 130 words a minute is about 260 words; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 path and card; at 680x425 sheet.
2. Past-policy results are rated intended or unintended, and for whom. (D2.Civ.13.9-12)
3. The plan picks two or three actions with a reason and a reflection. (D2.Civ.14.9-12, D4.7.9-12)
4. Three drafts each pass their audience check. (D4.3.9-12)
5. The decision path and mock hearing apply real procedures. (D4.8.9-12)
6. Drafts and recordings stay on the device, stated on screen; no speech recognition.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: path lights without moving; no network requests.

## Open questions
- The idea card flags five codes as too big (default used: one tool whose steps each teach one or two codes, so it can run across class periods; not split).
- The idea card flags a data source (default used: a 51-entry state guide, each entry naming its law and check date, checked before build; a state that can't be confirmed shows only the general checklist).
