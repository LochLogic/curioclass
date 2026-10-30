# Hospital Shift

## One idea
Follow one patient through one night in a hospital, 7 p.m. to 7 a.m., stepping into a different job every hour (paramedic, nurse, lab technologist, respiratory therapist, nursing assistant, pharmacist and more), and everyone writes on the same chart in medical words that you can split into their parts (tachy + cardi + ia = fast heart condition), so by morning you can read the whole chart aloud in plain English and name the twelve people it took.

## Not like
- career-cluster-explorer (CTE 6-8, careers, specced): 83 jobs for a minute each across 14 clusters. Here one cluster in depth, one patient, and the jobs pass the work hand to hand.
- path-planner (9-12, careers, this group): years of training. Here one night of work, hour by hour.
- workplace-scenarios (CTE 6-8, story): choices ripple across a camp day on a timeline, with the story card over a full-stage backdrop. Here the record is a medical chart, the choices are about whose job a task is and what to pass on, and the place sits in a framed window beside the card.
- first-aid-responder (health 9-12, specced): what a bystander does in an emergency. Here the hospital team after the ambulance, and no first aid skills are taught.
- interview-simulator (this group): getting hired. Here the job itself.

## Who and how
- Grade 9-12, career and technical education, module "Healthcare and Human Services Careers".
- Topic line: medical terms and careers in a hospital
- Driver: students on laptops; the teacher can project the shift and let the class vote at each choice. 25 to 45 minutes.
- Standards: CTE.Career Clusters (Advance CTE 2024: Healthcare and Human Services cluster, its pathways and occupations; medical terminology).
- Data as of line: "Pay: BLS May 2025. Training: BLS Occupational Outlook Handbook 2025-35. June and Lakeview Hospital are made up."

## Screens and modes
Header: title, topic line, modes (`.seg`): `Shift` (default), `Chart`, `Word parts`; then `Read`, `Motion`, `Sound`.

**Shift.** Focus: the scene card, the largest thing on the stage (at least half its width at 1366x768), with its bold chart words and three option cards. Stage, left: the hour's place as a painted picture in a framed window (Art; no people in the pictures: the story is told in the card), a wall clock drawn in code in its corner; under it a small floor plan of Lakeview Hospital drawn in code (ambulance bay, ER, lab, imaging, pharmacy, medical floor, kitchen) with the current place lit, as the progress map. Stage, right: the scene card shows the hour, the role ("8:30 p.m. You are the phlebotomist."), what is happening (2 to 3 sentences), any chart words in bold, and a choice of 3 option cards. A chart strip runs down the stage's right edge.
- Tap a bold chart word: it splits into colored part tiles (prefix, root, suffix), each with its meaning, and a plain-English line under it. Words decoded this way are marked in the Chart.
- Choose an option: the outcome line appears, and the scene writes its chart note (slides into the chart strip). Choices about scope and handoffs change later scenes (Content).
- `Meet this job` opens the role's career sheet (careers engine): what they do, median pay, training, people doing it, and how to try it now.
- `Next hour` (enabled once an option is chosen) moves on. A row of 13 clock dots at the bottom shows progress; tapping a passed dot revisits that scene read-only.

**Chart.** Focus: June's chart page, centered and full height. A hospital chart page: header (patient, age, room), then every note in time order, each signed by role. A `Plain English` toggle swaps each medical word for its plain meaning in place (both are shown with a dotted underline; tap one to see its parts). A side list "People on June's night" with each role, its emoji and `Meet this job`.

**Word parts.** Focus: the three slots and the built word, centered above the trays. Three trays (Prefixes, Roots, Suffixes, as tiles with meanings). Drag or tap one tile from each tray you need into the three slots (prefix optional). If the parts make a term from the Content list, it lights up with its meaning and the scene where it appears; if not, "Not a word in this chart. Try another part." A tally "Terms built: 6 of 17". `Shuffle` reorders the trays; `Clear` empties the slots.

## Content
**Patient:** June Park, 74, made up. Comes in at 7 p.m. with a cough, a fever and trouble breathing; it turns out to be pneumonia; by morning she is breathing more easily on oxygen and antibiotics. Nothing graphic.

**Scenes** (hour, role with careers.json id, place picture, situation, chart words, choice and outcomes with delay minutes; the best option is listed first here only, the tool shuffles them):
1. 7:00 p.m. Paramedic (paramedic). Place: ambulance bay. Bringing June in. Words: dyspnea. Choice, the handoff to the ER nurse: A Short and in order: what's wrong, background, what you found, what you need (the SBAR format). B Every detail of the ride, in the order it happened. C "She's fine, just a cough." Outcomes: A the nurse acts in seconds; B the nurse asks you to start over (note: "handoff repeated", 2 minutes); C the nurse finds the low oxygen herself a few minutes later (note: "dyspnea not reported at handoff", 5 minutes).
2. 7:20 p.m. Patient access representative (new: registration). Place: registration desk. A neighbor calls asking how June is. A Explain you can't share patient information, and take a message for the family. B Tell the neighbor it's pneumonia. C Hang up. Outcomes: A note "message for family"; B a privacy problem is reported (note: "privacy concern reviewed"); C the family never hears the neighbor called. No delay minutes.
3. 7:40 p.m. ER registered nurse (nurse). Place: ER bay. Words: tachycardia, tachypnea, febrile. Choice: A Tell the ER physician now, using the numbers. B Start a full admission form first. C Wait until the doctor walks by. Outcomes: A orders in 5 minutes; B and C orders 30 minutes later (note: "orders delayed", 25 minutes).
4. 8:00 p.m. Emergency medicine physician (new). Place: ER bay. Words: radiograph, hematology, antibiotic. Choice, which order first: A Oxygen now, then the X-ray and blood tests. B Tests first, then decide on oxygen. C Send her home with a cough medicine. Outcomes: A oxygen starts at 8:05; B oxygen at 9:15 (note, 70 minutes); C the nurse questions it and the doctor rethinks (note: "plan revised", 10 minutes).
5. 8:30 p.m. Phlebotomist (new). Place: ER bay. Words: venipuncture. Choice: A Check two identifiers (name and date of birth) against the label before drawing. B Check the room number only. C Ask "Are you June?" Outcomes: A correct; B and C a mislabeled-tube near miss is caught at the lab (note: "sample redrawn", results 40 minutes later).
6. 9:00 p.m. Radiologic technologist (new). Place: imaging room. Words: radiograph, bilateral. Choice: A Explain the X-ray to June and step behind the shield. B Take it fast without explaining. C Ask the family to hold her steady with no shield. Outcomes: A June holds still, clear image; B she moves, one retake (note, 5 minutes); C you stop and use positioning aids instead (note, 5 minutes).
7. 10:00 p.m. Medical laboratory technologist (new). Place: lab. Words: leukocytosis, hematology. Choice: A Call the ER nurse with the result now, because it is outside the normal range. B Post it to the chart and move on. C Wait for the doctor to ask. Outcomes: A the team hears in minutes; B and C it is found an hour later (note, 60 minutes).
8. 11:00 p.m. Respiratory therapist (new). Place: June's room at night. Words: hypoxemia, oximetry. Choice: A Set the oxygen to the doctor's order and recheck in 15 minutes. B Turn it up as high as it goes. C Leave it and check in the morning. Outcomes: A steady; B the order is checked with the doctor (note: "oxygen adjusted to order"); C no recheck (scene 10 changes). No delay minutes here; C's cost shows in scene 10.
9. 12:00 a.m. Pharmacist (pharmacist). Place: pharmacy. Words: intravenous, antibiotic. Choice: A Check June's allergy list before approving the antibiotic: it lists penicillin, so you call the doctor for another one. B Approve as written. C Approve and leave a note for the day shift. Outcomes: A a safe antibiotic at 12:30; B the nurse catches the allergy at the bedside (note: "order changed at bedside", 15 minutes); C same as B.
10. 2:00 a.m. Nursing assistant (new). Place: June's room at night. Words: oximetry. June's oxygen reads 89 percent; the doctor's order says call the nurse if it is under 92. (With 8 C the card adds: "No one has rechecked the oxygen since 11 p.m.") A Tell the nurse right away. B Turn up the oxygen yourself. C Write it down for morning. Outcomes: A the nurse and the respiratory therapist adjust it (note); B in this hospital a nursing assistant doesn't change oxygen, so the nurse checks and fixes it (note: "oxygen changed without order, corrected", 10 minutes); C the morning nurse finds it (note: "reading not reported for 5 hours", 300 minutes).
11. 4:00 a.m. Environmental services technician (new). Place: the empty room next door. Words: none (hand hygiene). Choice, cleaning the empty room: A Clean from the cleanest areas to the dirtiest, high to low, and clean your hands before and after. B Start with the bathroom and work out. C Use one cloth for the whole room. Outcomes: A ready for the next patient; B and C a supervisor's checklist sends you back (note, 20 minutes).
12. 6:00 a.m. Registered dietitian (new). Place: a breakfast tray in June's room at dawn. Words: dysphagia. June coughs when she drinks. A Ask the nurse for a swallowing check before breakfast and hold thin liquids. B Bring the regular tray. C Skip breakfast with no plan. Outcomes: A safe breakfast plan (note); B the nurse stops the tray (note); C June gets hungry and the plan is made at 9 (note, 180 minutes).
13. 7:00 a.m. Night nurse to day nurse handoff (nurse). Place: nurses' station at dawn. Words: pneumonia, afebrile (the night nurse's closing note: "Pneumonia improving. Afebrile since 4 a.m. Breathing easier on oxygen."). No choice: the student reads the night's chart aloud in plain English (the Chart opens with Plain English on), and the closing line names the roles.

**Chart terms** (17; parts and meaning): dyspnea (dys- difficult + pnea breathing): hard breathing. tachypnea (tachy- fast + pnea): fast breathing. tachycardia (tachy- + cardi heart + -ia condition): fast heart rate. bradycardia (brady- slow + cardi + -ia): slow heart rate (in Word parts only). febrile (febr fever + -ile pertaining to): has a fever. afebrile (a- without + febrile): no fever. hypoxemia (hypo- low + ox oxygen + -emia blood condition): low oxygen in the blood. oximetry (ox + -metry measuring): measuring oxygen. pneumonia (pneumon lung + -ia): lung infection condition. radiograph (radi X-ray + -graph record): an X-ray image. bilateral (bi- two + later side + -al): both sides. hematology (hemat blood + -logy study of): blood tests. leukocytosis (leuk white + cyt cell + -osis increased condition): high white blood cell count. venipuncture (ven vein + puncture): drawing blood from a vein. intravenous (intra- within + ven + -ous): into a vein. antibiotic (anti- against + bio life + -tic): medicine that fights bacteria. dysphagia (dys- + phag swallowing + -ia): trouble swallowing.

**Roles new to careers.json** (added to the careers builder with O*NET or SOC code; the builder fills pay and jobs): patient access representative (Medical Secretaries and Administrative Assistants, 43-6013), emergency medicine physician (29-1214), phlebotomist (31-9097), radiologic technologist (29-2034), medical laboratory technologist (clinical laboratory technologists and technicians, 29-2010), respiratory therapist (29-1126), nursing assistant (31-1131), environmental services technician (janitors and cleaners, 37-2011), registered dietitian (dietitians and nutritionists, 29-1031). Each gets a plain "does", "path" and "try" line written for grades 9-12 by the builder, in the style of careers_data.py, and the Handbook fields.

## Interactions in detail
- No points, no win state. The night always ends at 7 a.m. with June improving; choices change only the chart notes, the timing lines and the next scenes as listed. The closing card counts "minutes of delay on the chart" as a plain tally of the delay minutes listed in Content (0 to 720), never as a grade.
- Option order is shuffled per visit (seeded per page load); the chart notes always name the role, never the student.
- A scene revisited from a clock dot is read-only; to change a choice, `Restart the shift` (confirm) starts over.
- Word parts accepts only the 17 terms; parts can be used in any slot order but the tool shows them as prefix + root + suffix. "puncture" and "febrile" are whole tiles for their terms.
- A new chart note slides into the strip over 0.4 s (instant with Motion off); a tap on Next hour or a word during the slide finishes it at once and acts. The place picture cross-fades over 0.3 s per hour, never blocking a tap.
- Medical numbers shown are limited to the story's own orders (call if oxygen under 92 percent); the tool gives no medical advice and says so in the footer: "A story for learning about careers. Not medical advice."
- Saves progress on this device (localStorage `hospital-shift-night`, try/catch); `Restart the shift` clears it.
- Esc closes the word split and the career sheet; Tab order: option cards, Next hour, chart words, then the stage.
- Sizes: pictures and card laid out at real pixels; at 680x425 the stage shows the place picture as a short band above the scene card and hides the floor plan; at 375 wide the scene card is full width, the picture a banner, and the chart strip becomes a `Chart` button.

## Look
- Accent `--brand #8fa8ff` (night-ward periwinkle: the lit room on the floor plan, Next hour, active mode), `--brand-ink #0d1633`. Base `kit/theme-912.css`.
- Floor plan: corridor `#0f1726`, rooms `#18233a`, lit room `#2a3b66` with an accent outline; picture frame `#2a3b66`; chart page `#f7f8fb` with ink `#1a2030`; part tiles: prefix `#b8c6ff`, root `#ffd59a`, suffix `#b9f0d2`, each with dark ink `#1a2030` and its label ("prefix") written on it.
- The paintings share a night palette (deep blue shadows, warm pools of lamp light) that brightens at 6 and 7 a.m.
- Contrast: accent on panel 7.59:1, on `--sec-bg` 7.2:1; brand-ink on accent 7.81:1; chart ink on page 15.9:1; tile ink on each tile 11:1 or more.
- Differs from career-cluster-explorer's festival teal, workplace-scenarios' lake blue daylight, first-aid-responder's mint (#3ee0b0) and every accent in this batch.

## Art
Local FLUX (`scripts/localart.py`), one session, no people (June and the staff are told in the card and the voice, never painted). Shared style line: "quiet realistic digital painting of a hospital at night, deep blue shadows, warm pools of lamp light, calm and clean". Blank surfaces on every sign, screen and label. All 4:3, cutout no, people no, webp 1000 px wide, shown in the framed window on the Shift stage.
- hs-bay: "an ambulance parked in a covered hospital ambulance bay at night, its back doors open and an empty stretcher beside it, (style)" (scene 1).
- hs-desk: "a hospital registration desk at night with a desk phone, a computer with a dark screen and a clipboard, (style)" (scene 2).
- hs-er: "an emergency room treatment bay with a made bed, a heart monitor showing a green line, an oxygen outlet on the wall and a privacy curtain half open, (style)" (scenes 3 to 5).
- hs-xray: "a hospital X-ray room with a large ceiling-mounted X-ray machine, a padded table and a lead apron on a hook beside a shield wall, (style)" (scene 6).
- hs-lab: "a hospital laboratory at night with a blood analyzer, racks of capped sample tubes and a microscope on a bright counter, (style)" (scene 7).
- hs-room: "a calm hospital patient room at night, the bed with its blanket and pillow, an oxygen tube coiled on the bedside, a pulse oximeter clip on the table, a small lamp on, (style)" (scenes 8 and 10).
- hs-pharmacy: "a hospital pharmacy at night with shelves of medicine boxes, a counter with IV bags and a computer, (style)" (scene 9).
- hs-clean: "an empty freshly cleaned hospital room with a stripped bed, a housekeeping cart with spray bottles and colored cloths, a hand sanitizer on the wall, (style)" (scene 11).
- hs-tray: "a hospital breakfast tray on an overbed table at dawn, a covered plate, a cup of thickened juice and a spoon, early light through blinds, (style, early morning light)" (scene 12).
- hs-station: "a hospital nurses' station at dawn with computer screens, a coffee mug and a stack of charts, morning light at the end of the hall, (style, early morning light)" (scene 13).
- 10 images, none with people. Drawn in code: the floor plan, clock, chart strip and page, part tiles, option cards and role emoji (from careers.json, as in its siblings).

## Voice
Bank voice `wise-mentor` (Gacrux), "Say thoughtfully and warmly, like a wise high school mentor": the charge nurse walking you through the night. Not used by another tool `neighbors.py` lists or by this batch (it speaks for ai-evaluator, virtual-gallery and captain-s-choices in other subjects). `Curio.voice`, `scope: () => state.mode`. Scene texts are voiced as story beats (13, each under 200 characters, written by the builder from the Content); chart notes are on screen only.
- welcomeShift (how; on entering Shift before the first word or choice; stale when a word or option is tapped): "It's seven at night. Read the card, then tap a bold word to split it into parts."
- chooseHow (how; after the first word split; stale when an option is tapped): "Now tap the option card you would choose."
- nextHow (how; after the first outcome; stale when Next hour is tapped): "Tap Next hour to move to the next job."
- scene1 to scene13 (event; when each scene opens; stale if Next hour is tapped first): the scene text.
- delay (event; a choice that adds delay minutes; stale on Next hour): "That choice added a delay. It's on the chart now."
- morning (event; scene 13; stale when the mode changes): "Seven in the morning. Read June's chart in plain English. Twelve jobs got her through the night."
- welcomeChart (how; on entering Chart; stale when Plain English is tapped): "Tap Plain English to read the chart without the medical words."
- welcomeParts (how; on entering Word parts; stale when a tile is tapped): "Tap a part from each tray to build a word from June's chart."
- built (event; each new term built; stale on the next tap): "(term): (meaning)."
- notWord (event; a combination that is not a term; stale on the next tap): "Not a word in this chart. Try another part."

## Family engine
The careers family engine, described in full in career-cluster-explorer's spec. This tool uses the shared career sheet (opened from `Meet this job` and the Chart's people list) with `payText` and `jobsText`, and the Handbook fields. It feeds it nine new healthcare careers (listed in Content, added to `scripts/careers_data.py` so every sibling gets them) and the 13 scenes, 17 terms and chart notes.

## Sources
- Medical word parts and meanings: MedlinePlus (NIH, National Library of Medicine), "Understanding Medical Words" tutorial (https://medlineplus.gov/medicalwords.html) and its word-part lists.
- Pneumonia symptoms (cough, fever, trouble breathing), oxygen and antibiotic treatment: MedlinePlus, Pneumonia (https://medlineplus.gov/pneumonia.html).
- SBAR handoff format: AHRQ, TeamSTEPPS, "SBAR" (https://www.ahrq.gov/teamstepps-program/index.html).
- Two patient identifiers: The Joint Commission, National Patient Safety Goals, NPSG.01.01.01 (https://www.jointcommission.org/standards/national-patient-safety-goals/).
- Patient privacy (sharing information with others): HHS, HIPAA for Individuals (https://www.hhs.gov/hipaa/for-individuals/index.html).
- Hand hygiene and clean-to-dirty room cleaning: CDC, Hand Hygiene in Healthcare Settings (https://www.cdc.gov/clean-hands/hcp/) and CDC, Environmental Cleaning in Healthcare (https://www.cdc.gov/healthcare-associated-infections/hcp/cleaning-global/).
- Allergy checks before medicines: AHRQ PSNet, Medication Errors and Adverse Drug Events (https://psnet.ahrq.gov/primer/medication-errors-and-adverse-drug-events).
- Swallowing trouble (dysphagia): MedlinePlus, Swallowing Disorders (https://medlineplus.gov/swallowingdisorders.html).
- Roles, pay and training: BLS OEWS May 2025 and Occupational Outlook Handbook 2025-35 profiles for each role (https://www.bls.gov/ooh/healthcare/), via careers.json.
- Healthcare and Human Services cluster: Advance CTE, Career Clusters Framework 2024 (https://careertech.org/career-clusters/).
- June, Lakeview Hospital, the orders and the scenes: made up for this tool; "in this hospital" scope rules are the story's, since real scope varies by state and employer.
- Checks run (Python, 2026-10-29): all 531,441 choice paths over the 12 scenes with choices; the delay tally runs from 0 to 720 minutes (288 different totals). The old spec said "0 to about 180", which scene 10 C alone (300 minutes) breaks, so each outcome now carries its minutes and the range is 0 to 720. Terms: 17 listed; the scenes used 14, so pneumonia and afebrile were never split in Shift (Done when 2 failed); scene 13's closing note now carries them, and bradycardia stays Word parts only. Roles: 13 scenes, 12 different jobs (the nurse appears at 7:40 p.m. and 7 a.m.), matching "twelve people".

## Done when
1. All 13 scenes play in order 7 p.m. to 7 a.m., each with its role, place picture, words and three options; every role opens a career sheet with 2025 pay and training.
2. Each of the 17 terms splits into the listed parts and meanings, in Shift (all but bradycardia), Chart and Word parts.
3. Word parts builds all 17 and rejects other combinations with the hint; bradycardia appears only there.
4. Scene 8 C adds the "not rechecked" line to scene 10; scene 4 B moves oxygen to 9:15 in the notes; every listed outcome writes its note.
5. Chart with Plain English on reads every note with no medical word left unexplained.
6. No score, timer or win screen anywhere; the delay tally is plain minutes from the notes, 0 for all best options and 720 for the worst path.
7. Option order changes between visits; a revisited scene is read-only.
8. Focus: at 1366x768 and 680x425 the scene card is the largest thing in Shift, the chart page in Chart and the slots in Word parts.
9. Tap while it plays: a tap on Next hour or a bold word while a note slides or a scene line is spoken acts at once and the old line stops.
10. All 10 place pictures load; none shows a person or fake lettering.
11. Scene card, options and Next hour are visible without scrolling at every STANDARDS.md size; the preview is readable.
12. How lines once each in five actions in a row; scene lines, delay, morning, built and notWord every time, dropped when stale.

## Open questions
- Nine roles are new to careers.json (listed in Content). Add them to the shared builder (they would also appear in career-match-quiz's Explore view and career-cluster-explorer's counts unless filtered), or keep them in this tool's own data?
- Scene 2 touches patient privacy with a nosy neighbor, and scene 10 shows a nursing assistant noticing a low oxygen reading. Both are calm and non-graphic. Anything a health teacher or parent might want changed?
- The places are painted empty (no June, no staff), so nothing waits on Gemini. Fine, or should a few scenes show the team at work later (images with people for Cory's review)?
