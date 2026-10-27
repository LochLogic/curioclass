# CS gap fill (CSTA 2026): notes

Written 2026-10-27 for the gap-fill merge. Checker: `python scripts/overlap/stage_check.py docs/agents/gapfill/cs --missing`
reports 0 errors and 0 warnings, and CSTA at 196 of 196 (all planned): K-2 48/48, 3-5 57/57, 6-8 45/45, 9-12 46/46.
Live plus specced is 98/196 (K-2 23, 3-5 27, 6-8 21, 9-12 27); live alone is 16/196.

## Where the wording came from

The repo holds only the ids (data/standards/csta-2026-ids.txt has no header and no wording). I read every statement and
boundary statement in the official PDF, "2026 CSTA PK-12 Computer Science Standards" (download page
https://csteachers.org/2026-csta-pk-12-computer-science-standards/, CC BY-NC-SA 4.0, DOI 10.1145/3820482). All 196 ids
were found with their statements; every code below was matched to its statement and boundary statement, not to its
prefix. The interactive viewer (csteachers.org/pk12standards/view/) blocks scripted reads; the PDF did not.

No id was left unread, so there are no ids with unconfirmed wording.

## 1. Codes added to existing modules (codes.txt, 11 lines, 14 codes)

| Module | Tool | Added | Why the tool already does it |
|---|---|---|---|
| computer-science-k-step-by-step | robot-dance (live) | EK-PRO-RD-06 | the class says what Bolt will do as each card runs |
| computer-science-k-count-and-decide | me-vs-the-counter | EK-DAT-IM-10 | the computer's counts decide the bounciest ball |
| math-k-sort-and-count | toy-box-sort (planned, no spec) | EK-ALG-ML-02 | sort by color, shape or size: the boundary statement's own activity |
| computer-science-1-code-a-path | snowy-mail-route | E1-ALG-IM-03 | Mixed Up level: swapped cards send Pip somewhere else |
| computer-science-3-how-we-use-the-internet | internet-journey | E3-SYS-IM-15 | Where copies live: who a widely used message app affects, and how |
| computer-science-4-wired-wireless-and-login | network-help-desk | E4-SYS-HW-12 | ask, diagnose, fix, test ping ("no network access" is the CSTA example) |
| computer-science-4-training-data-matters | biased-bot | E4-DAT-IM-11, E3-ALG-ML-02 | data from one room harms another room; adding Room 9 cards fixes it |
| computer-science-6-8-algorithms-and-fairness | algorithm-audit | MS-SOC-HU-43 | human choices in the formula decide who gets seats |
| computer-science-6-8-machine-learning-models | model-mechanic | MS-DAT-IM-29 | collection and labeling decisions compromise the model |
| computer-science-9-12-ethics-law-and-data-policy | data-policy-council | HS-SOC-HI-39, HS-DAT-IM-27 | revise a proposed policy past legal flags; the ads clause is CSTA's example |
| computer-science-9-12-building-and-evaluating-ai | ai-evaluator | HS-SOC-HU-43, HS-ALG-IM-11 | test set, threshold and ship verdict decide who the AI fails; the threshold trades values |

The nine specced, not-live tools above had the codes appended to their `- Standards` line. robot-dance is live, so only
codes.txt changes; toy-box-sort has no spec yet.

Asked for but not added:
- **secret-keeper (K):** no EK SOC code fits. EK-SOC-HI-14 (tech changed over time), EK-SOC-HU-15 (people design
  tech) and EK-SOC-CE-16 (devices at home, school, work) are not privacy. Its privacy and responsible-use work is
  already coded (EK-SYS-SE-12, EK-SYS-IM-13). The K SOC codes go to new K-2 tools instead.
- **simulation-studio:** HS-DAT-DC-24 (verifying types, values, ranges) is only touched by its night-code flag, so it
  went to the new data dictionary tool, where checking rows against rules is the whole job.

## 2. New modules and tools (32: K-2 7, 3-5 9, 6-8 8, 9-12 8)

Every module is a band span with each spanned grade's code; the tool has a grade switch that changes the task, not just
the wording. K-2 tools use the grade `k-2` (the catalog already has 22 k-2 modules; see questions).

| Band | Tool (module) | Codes | What the grade switch changes |
|---|---|---|---|
| K-2 | Attic Gadget Box (Computing Then and Now) | EK-SOC-HI-14, EK-SOC-HU-15, E1-SOC-HI-14, E2-SOC-HI-14, E2-SOC-HU-15 | K: old and new look; 1: how the task changed; 2: who designed it, from many places and abilities, and the problem |
| K-2 | Question Jar (Asking With Data) | EK-DAT-DI-09, EK-DAT-DC-08, E1-DAT-DI-09, E1-DAT-DC-08, E1-DAT-IM-10, E2-DAT-DI-09, E2-DAT-DC-08, E2-DAT-IM-10 | K: can we count it?; 1: data question or opinion, numbers or words; 2: refine the question, who the plan leaves out |
| K-2 | Who Uses This Device? (Devices at Home, School and Work) | EK-SOC-CE-16, EK-SYS-HW-11, E1-SOC-CE-16, E2-SOC-CE-16 | K: tools for different people; 1: home, school, community; 2: hobby to computing job |
| K-2 | Tablet Buddy (Using Tech Well) | EK-SYS-IM-13, E1-SYS-IM-13, E2-SYS-IM-13 | K: responsible choices; 1: why the class rules exist; 2: benefits and harms to how you feel |
| K-2 | Line Leader Picker (Fair Rules for Turns) | EK-ALG-IM-03, E1-ALG-IM-03, E2-ALG-IM-03 | K: people write the rule; 1: change a step, new result; 2: is it fair to everyone? |
| K-2 | Morning Meeting Board (Signs and Changing Values) | EK-PRO-VD-05, E1-PRO-VD-05, E2-PRO-VD-05 | K: read picture signs; 1: what changes; 2: name each box, constant or changing |
| K-2 | Tap-to-Start Puppets (What the Code Does) | EK-PRO-RD-06, E1-PRO-RD-06, E2-PRO-RD-06 | K: what happened; 1: which tap started it; 2: retell how it was built and who helped |
| 3-5 | Inventors Hall (Computing Inventions and Inventors) | E3-SOC-HI-16, E3-SOC-HU-18, E4-SOC-HI-16, E4-SOC-ET-17, E5-SOC-HI-16 | 3: how life changed, why built; 4: overlooked inventors, old limits to new tech; 5: who was included or left out |
| 3-5 | Job Shadow Day (Computing on the Job) | E3-SOC-CE-19, E4-SOC-CE-19, E5-SOC-CE-19, E5-SYS-IM-15 | 3: computing at work; 4: learning a new tool; 5: teamwork and how work changed |
| 3-5 | Family Tech Vote (New Tech: Yes or No?) | E3-SOC-ET-17, E4-DAT-IM-11, E4-SYS-IM-15, E5-SOC-ET-17, E5-DAT-IM-11 | 3: benefits and risks; 4: data about people, the planet; 5: how a family decides |
| 3-5 | Fair Survey Kit (Fair Surveys) | E3-DAT-IM-11, E3-DAT-DC-09, E4-DAT-DC-09, E5-DAT-DC-09 | 3: plan for every group, check answers; 4: rows and columns; 5: sort and group with the tool |
| 3-5 | Marble Ramp Trials (Why Data Varies) | E3-DAT-DI-10, E4-DAT-DI-10, E5-DAT-DI-10 | 3: two attributes; 4: explain with a chart; 5: variability and outliers |
| 3-5 | Team Code Relay (Code as a Team) | E3-PRO-PD-05, E3-PRO-RD-07, E4-PRO-PD-04, E4-PRO-PD-05, E5-PRO-PD-05, E5-PRO-RD-07 | 3: feedback, what a part does; 4: compare two fixes, contribute; 5: build a component, comment it |
| 3-5 | Adventure Outline Cards (Plan It Before You Code It) | E3-ALG-PS-01, E4-ALG-PS-01, E5-ALG-PS-01 | 3: plan with a fork; 4: written outline; 5: card diagram with a variable |
| 3-5 | Three Route Rules (Algorithms That Help Some More) | E3-ALG-IM-03, E4-ALG-IM-03, E5-ALG-IM-03 | 3: compare outcomes; 4: who benefits or loses; 5: design the app's options for users |
| 3-5 | Inside the Keypress (Hardware and Software Together) | E3-SYS-HW-12, E4-SYS-HW-12, E5-SYS-HW-12 | 3: what software does; 4: fix the stuck step; 5: input, memory, processing, output |
| 6-8 | Metadata X-Ray (Data, Metadata and You) | MS-DAT-DC-21, MS-DAT-DC-22, MS-DAT-IM-28 | |
| 6-8 | Lunch Survey Cleanup (Cleaning Data Honestly) | MS-DAT-DC-24, MS-DAT-DI-27 | |
| 6-8 | Accessibility Test Team (Design for Every User) | MS-ALG-IM-09, MS-PRO-TR-20, MS-SYS-IM-36, MS-PRO-PD-15 | |
| 6-8 | County Connection Grant (Who Gets Connected) | MS-SYS-HW-30, MS-SYS-IM-37, MS-SOC-ET-41 | |
| 6-8 | AI Fit Check (Choosing AI or Not) | MS-ALG-PS-04, MS-ALG-PS-05, MS-SOC-ET-40 | |
| 6-8 | AI Code Inspector (Code You Did Not Write) | MS-PRO-RD-18, MS-PRO-TR-19, MS-PRO-PD-13, MS-PRO-PD-14 | |
| 6-8 | Industry Device Tour (Computing in Industry) | MS-SOC-CE-44, MS-SYS-HW-31 | |
| 6-8 | Eras of Computing (Computing History and Impact) | MS-SOC-HI-38, MS-SOC-HI-39, MS-SOC-ET-42 | |
| 9-12 | Emerging Tech Pitch (Emerging Technology Review) | HS-SOC-ET-40, HS-SOC-ET-41, HS-SOC-ET-42 | |
| 9-12 | Cloud Through Time (A Technology's Long Story) | HS-SOC-HI-38, HS-SYS-IM-37 | |
| 9-12 | Dice in the Chatbot (Minds and Machines) | HS-ALG-PS-04, HS-SOC-HU-44 | |
| 9-12 | Pull Request Review (Reviewing AI-Written Code) | HS-PRO-RD-18, HS-PRO-PD-14 | |
| 9-12 | Sprint Board (Design, Test and Refine) | HS-ALG-IM-09, HS-PRO-TR-19, HS-PRO-TR-20, HS-PRO-PD-15 | |
| 9-12 | Catalog Column Rules (Data Dictionaries and Validation) | HS-DAT-DC-22, HS-DAT-DC-24 | |
| 9-12 | Computing Team Stories (Computing Teams and Careers) | HS-SOC-CE-45, HS-SOC-CE-46 | |
| 9-12 | Coin Cell Greenhouse (Device Limits and Optimization) | HS-SYS-HW-30, HS-ALG-PS-02 | |

Some span modules also carry a code another tool already covers (EK-DAT-DI-09, EK-DAT-DC-08, EK-SYS-IM-13,
E1-ALG-IM-03, E3-ALG-PS-01, E4-DAT-DC-09, E4-DAT-DI-10, E4-DAT-IM-11, E4-SYS-HW-12, E5-ALG-IM-03) so the span has a
code for every grade it switches to. Each is practiced by that grade's level, not listed for the count.

Choices worth knowing:
- **Computing and society** (34 empty) now has a tool per band for history (Attic Gadget Box, Inventors Hall, Eras of
  Computing, Cloud Through Time), for jobs (Who Uses This Device?, Job Shadow Day, Industry Device Tour, Computing Team
  Stories), for emerging tech (Family Tech Vote, AI Fit Check, Emerging Tech Pitch) and for ethics and equity (Three
  Route Rules, County Connection Grant, Dice in the Chatbot). Accessibility is its own 6-8 tool and part of Sprint Board.
- **Data** (23 empty) is now a K-2 question tool, a 3-5 survey and a 3-5 measurement lab, two 6-8 tools (metadata,
  cleaning) and a 9-12 data dictionary.
- **AI-written code** (MS-PRO-RD-18, HS-PRO-RD-18, new in CSTA 2026) gets a tool in 6-8 and 9-12. Both use a made-up AI
  helper with fixed output, so no live model is needed and nothing is sent anywhere.
- **Collaboration codes** (E4/E5-PRO-PD-05, MS-PRO-PD-15, HS-PRO-PD-15) are on tools that real students use together
  (Team Code Relay splits the screen between partners; Accessibility Test Team and Sprint Board rotate roles), not a
  simulation of teammates.
- **Settings avoided:** no new K-2 robot, machine or town; no 9-12 lab setting, business or council; no new cyber or
  network world. Dice in the Chatbot is format lab but its setting is two chat windows (generic).
- Where's My Phone From? (social studies 10) already traces a phone's supply chain, so Cloud Through Time follows data
  centers instead of phones.

## 3. Checker warnings

None remain. The first run flagged Tablet Buddy against three K-2 creature tools (letter-lanterns, habit-hero,
terrarium-pal: care-for in a creature world) and a cross-band triple between Inventors Hall and Eras of Computing.
Tablet Buddy became a story (choose-path, school day); Eras of Computing got its own skill key (tech-impact-history) and
an archive setting.

## 4. By-design exclusions

None. All 196 CSTA 2026 ids are claimed after this folder.

## 5. Questions for Cory

1. **K-2 spans.** The seven K-2 tools use module grade `k-2` with EK, E1 and E2 codes, as the arts, ELA and other k-2
   modules do. The brief listed 3-5, 6-8 and 9-12 spans. If CS should stay one grade per module in K-2, each splits
   into a K, 1 or 2 tool (about 17 tools instead of 7).
2. **E3-ALG-ML-02 on biased-bot (grade 4).** Its boundary statement ("adding missing or underrepresented examples helps
   the model") is biased-bot's whole story, but the module is grade 4. The alternative is a grade 3 ML tool, which
   would crowd the ml-lab family (five tools already).
3. **EK-ALG-ML-02 on math-k-sort-and-count.** A CS code on a math module (toy-box-sort, planned). It matches the
   statement exactly; say if CS codes should stay on CS modules.
4. **input-or-output (grade 2)** says in its own spec that it does not teach E2-SYS-SE-12 ("online actions have real-world
   consequences"), though its module carries the code. Coverage counts it. It may want a home elsewhere (Tablet Buddy
   could take it) or an edit to that spec.
5. **Five busy modules.** data-policy-council and ai-evaluator now carry 5 and 6 codes. Each added code matches the tool's
   core activity, but if module pages should stay at about 3 codes, HS-DAT-IM-27 and HS-ALG-IM-11 can move to new
   9-12 tools instead.
