# Hospital Shift

## One idea
Follow one patient through one night in a hospital, 7 p.m. to 7 a.m., stepping into a different job every hour (paramedic, nurse, lab technologist, respiratory therapist, nursing assistant, pharmacist and more), and everyone writes on the same chart in medical words that you can split into their parts (tachy + cardi + ia = fast heart condition), so by morning you can read the whole chart aloud in plain English and name the twelve people it took.

## Not like
- career-cluster-explorer (CTE 6-8, careers, specced): 83 jobs for a minute each across 14 clusters. Here one cluster in depth, one patient, and the jobs pass the work hand to hand.
- path-planner (9-12, careers, this group): years of training. Here one night of work, hour by hour.
- workplace-scenarios (CTE 6-8, story): choices ripple across a camp day on a timeline. Here the record is a medical chart and the choices are about whose job a task is and what to pass on.
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

**Shift.** Stage: a night hospital drawn in code as a cutaway (ambulance bay, ER, lab, imaging, pharmacy, a medical floor room, a hallway), with a clock and the patient's room light. The current scene's place is lit. A scene card shows the hour, the role ("8:30 p.m. You are the phlebotomist."), what is happening (2 to 3 sentences), any chart words in bold, and a choice of 3 option cards.
- Tap a bold chart word: it splits into colored part tiles (prefix, root, suffix), each with its meaning, and a plain-English line under it. Words decoded this way are marked in the Chart.
- Choose an option: the outcome line appears, and the scene writes its chart note (slides into a small chart strip at the right edge of the stage). Choices about scope and handoffs change later scenes (Content).
- `Meet this job` opens the role's career sheet (careers engine): what they do, median pay, training, people doing it, and how to try it now.
- `Next hour` moves on. A row of 13 clock dots at the bottom shows progress; tapping a passed dot revisits that scene read-only.

**Chart.** June's chart full size, as a hospital chart page: header (patient, age, room), then every note in time order, each signed by role. A `Plain English` toggle swaps each medical word for its plain meaning in place (both are shown with a dotted underline; tap one to see its parts). A side list "People on June's night" with each role, its emoji and `Meet this job`.

**Word parts.** A builder for the terms in the tool: three trays (Prefixes, Roots, Suffixes, as tiles with meanings). Drag or tap one tile from each tray you need into the three slots (prefix optional). If the parts make a term from the Content list, it lights up with its meaning and the scene where it appears; if not, "Not a word in this chart. Try another part." A tally "Terms built: 6 of 17". `Shuffle` reorders the trays; `Clear` empties the slots.

## Content
**Patient:** June Park, 74, made up. Comes in at 7 p.m. with a cough, a fever and trouble breathing; it turns out to be pneumonia; by morning she is breathing more easily on oxygen and antibiotics. Nothing graphic.

**Scenes** (hour, role with careers.json id, situation, chart words, choice and outcomes; the best option is listed first here only, the tool shuffles them):
1. 7:00 p.m. Paramedic (paramedic). Bringing June in. Words: dyspnea. Choice, the handoff to the ER nurse: A Short and in order: what's wrong, background, what you found, what you need (the SBAR format). B Every detail of the ride, in the order it happened. C "She's fine, just a cough." Outcomes: A the nurse acts in seconds; B the nurse asks you to start over, two minutes lost (note: "handoff repeated"); C the nurse finds the low oxygen herself a few minutes later (note: "dyspnea not reported at handoff").
2. 7:20 p.m. Patient access representative (new: registration). A neighbor calls asking how June is. A Explain you can't share patient information, and take a message for the family. B Tell the neighbor it's pneumonia. C Hang up. Outcomes: A note "message for family"; B a privacy problem is reported (note: "privacy concern reviewed"); C the family never hears the neighbor called.
3. 7:40 p.m. ER registered nurse (nurse). Words: tachycardia, tachypnea, febrile. Choice: A Tell the ER physician now, using the numbers. B Start a full admission form first. C Wait until the doctor walks by. Outcomes: A orders in 5 minutes; B and C orders 30 minutes later (later scenes note the delay).
4. 8:00 p.m. Emergency medicine physician (new). Words: radiograph, hematology, antibiotic. Choice, which order first: A Oxygen now, then the X-ray and blood tests. B Tests first, then decide on oxygen. C Send her home with a cough medicine. Outcomes: A oxygen starts at 8:05; B oxygen at 9:15 (note); C the nurse questions it and the doctor rethinks (note: "plan revised").
5. 8:30 p.m. Phlebotomist (new). Words: venipuncture. Choice: A Check two identifiers (name and date of birth) against the label before drawing. B Check the room number only. C Ask "Are you June?" Outcomes: A correct; B and C a mislabeled-tube near miss is caught at the lab (note: "sample redrawn"), results 40 minutes later.
6. 9:00 p.m. Radiologic technologist (new). Words: radiograph, bilateral. Choice: A Explain the X-ray to June and step behind the shield. B Take it fast without explaining. C Ask the family to hold her steady with no shield. Outcomes: A June holds still, clear image; B she moves, one retake (note); C you stop and use positioning aids instead (note).
7. 10:00 p.m. Medical laboratory technologist (new). Words: leukocytosis, hematology. Choice: A Call the ER nurse with the result now, because it is outside the normal range. B Post it to the chart and move on. C Wait for the doctor to ask. Outcomes: A the team hears in minutes; B and C it is found an hour later (note).
8. 11:00 p.m. Respiratory therapist (new). Words: hypoxemia, oximetry. Choice: A Set the oxygen to the doctor's order and recheck in 15 minutes. B Turn it up as high as it goes. C Leave it and check in the morning. Outcomes: A steady; B the order is checked with the doctor (note: "oxygen adjusted to order"); C the nursing assistant finds a low reading later (scene 10 changes).
9. 12:00 a.m. Pharmacist (pharmacist). Words: intravenous, antibiotic. Choice: A Check June's allergy list before approving the antibiotic: it lists penicillin, so you call the doctor for another one. B Approve as written. C Approve and leave a note for the day shift. Outcomes: A a safe antibiotic at 12:30; B the nurse catches the allergy at the bedside (note: "order changed at bedside"); C same as B.
10. 2:00 a.m. Nursing assistant (new). Words: oximetry. June's oxygen reads 89 percent; the doctor's order says call the nurse if it is under 92. A Tell the nurse right away. B Turn up the oxygen yourself. C Write it down for morning. Outcomes: A the nurse and the respiratory therapist adjust it (note); B in this hospital a nursing assistant doesn't change oxygen, so the nurse checks and fixes it (note: "oxygen changed without order, corrected"); C the morning nurse finds it (note: "reading not reported for 5 hours").
11. 4:00 a.m. Environmental services technician (new). Words: none (hand hygiene). Choice, cleaning the empty room next door: A Clean from the cleanest areas to the dirtiest, high to low, and clean your hands before and after. B Start with the bathroom and work out. C Use one cloth for the whole room. Outcomes: A ready for the next patient; B and C a supervisor's checklist sends you back (note).
12. 6:00 a.m. Registered dietitian (new). Words: dysphagia. June coughs when she drinks. A Ask the nurse for a swallowing check before breakfast and hold thin liquids. B Bring the regular tray. C Skip breakfast with no plan. Outcomes: A safe breakfast plan (note); B the nurse stops the tray (note); C June gets hungry and the plan is made at 9 (note).
13. 7:00 a.m. Night nurse to day nurse handoff (nurse). No choice: the student reads the night's chart aloud in plain English (the Chart opens with Plain English on), and the closing line names the roles.

**Chart terms** (17; parts and meaning): dyspnea (dys- difficult + pnea breathing): hard breathing. tachypnea (tachy- fast + pnea): fast breathing. tachycardia (tachy- + cardi heart + -ia condition): fast heart rate. bradycardia (brady- slow + cardi + -ia): slow heart rate (in Word parts only). febrile (febr fever + -ile pertaining to): has a fever. afebrile (a- without + febrile): no fever. hypoxemia (hypo- low + ox oxygen + -emia blood condition): low oxygen in the blood. oximetry (ox + -metry measuring): measuring oxygen. pneumonia (pneumon lung + -ia): lung infection condition. radiograph (radi X-ray + -graph record): an X-ray image. bilateral (bi- two + later side + -al): both sides. hematology (hemat blood + -logy study of): blood tests. leukocytosis (leuk white + cyt cell + -osis increased condition): high white blood cell count. venipuncture (ven vein + puncture): drawing blood from a vein. intravenous (intra- within + ven + -ous): into a vein. antibiotic (anti- against + bio life + -tic): medicine that fights bacteria. dysphagia (dys- + phag swallowing + -ia): trouble swallowing.

**Roles new to careers.json** (added to the careers builder with O*NET or SOC code; the builder fills pay and jobs): patient access representative (Medical Secretaries and Administrative Assistants, 43-6013), emergency medicine physician (29-1214), phlebotomist (31-9097), radiologic technologist (29-2034), medical laboratory technologist (clinical laboratory technologists and technicians, 29-2010), respiratory therapist (29-1126), nursing assistant (31-1131), environmental services technician (janitors and cleaners, 37-2011), registered dietitian (dietitians and nutritionists, 29-1031). Each gets a plain "does", "path" and "try" line written for grades 9-12 by the builder, in the style of careers_data.py, and the Handbook fields.

## Interactions in detail
- No points, no win state. The night always ends at 7 a.m. with June improving; choices change only the chart notes, the timing lines and the next scenes as listed. The closing card counts "minutes saved by clear handoffs" only as a plain tally of the delays in the notes (0 to about 180), never as a grade.
- Option order is shuffled per visit (seeded per page load); the chart notes always name the role, never the student.
- A scene revisited from a clock dot is read-only; to change a choice, `Restart the shift` (confirm) starts over.
- Word parts accepts only the 17 terms; parts can be used in any slot order but the tool shows them as prefix + root + suffix. "puncture" and "febrile" are whole tiles for their terms.
- Medical numbers shown are limited to the story's own orders (call if oxygen under 92 percent); the tool gives no medical advice and says so in the footer: "A story for learning about careers. Not medical advice."
- Saves progress on this device (localStorage `hospital-shift-night`, try/catch); `Restart the shift` clears it.
- Esc closes the word split and the career sheet; Tab order: option cards, Next hour, chart words, then the stage.
- Sizes: the cutaway is drawn at real pixels; at 680x425 the stage shows only the lit room and the scene card; at 375 wide the scene card is full width and the chart strip becomes a `Chart` button.

## Look
- Accent `--brand #8fa8ff` (night-ward periwinkle: the lit room, Next hour, active mode), `--brand-ink #0d1633`. Base `kit/theme-912.css`.
- Scene: night corridor `#0f1726`, rooms `#18233a`, lit room glow `#2a3b66`, monitor line `#7ee3c8`; chart page `#f7f8fb` with ink `#1a2030`; part tiles: prefix `#b8c6ff`, root `#ffd59a`, suffix `#b9f0d2`, each with dark ink `#1a2030` and its label ("prefix") written on it.
- Contrast: accent on panel 7.59:1, on `--sec-bg` 7.2:1; brand-ink on accent 7.81:1; chart ink on page 15.9:1; tile ink on each tile 11:1 or more.
- Differs from career-cluster-explorer's festival teal, workplace-scenarios' lake blue, first-aid-responder's mint (#3ee0b0) and every accent in this group.

## Art
none: drawn in code (hospital cutaway, clock, chart page, part tiles; roles shown by emoji as in career-match-quiz).

## Voice
Bank voice `wise-mentor` (Gacrux), "Say thoughtfully and warmly, like a wise high school mentor": the charge nurse walking you through the night. Not used by another tool in this group or a 9-12 CTE tool (it speaks for ai-evaluator, virtual-gallery and captain-s-choices in other subjects). `Curio.voice`, `scope: () => state.mode`. Scene texts are voiced as story beats (13, each under 200 characters, written by the builder from the Content); chart notes are on screen only.
- welcomeShift (how): "It's seven at night. Read the card, then tap a bold word to split it into parts."
- chooseHow (how, first word split): "Now pick what you would do. Then tap Next hour."
- scene1 to scene13 (event, when each scene opens; stale if Next hour is tapped first): the scene text.
- delay (event, a choice that adds a delay note; stale on Next hour): "That choice added a delay. It's on the chart now."
- morning (event, scene 13): "Seven in the morning. Read June's chart in plain English. Twelve jobs got her through the night."
- welcomeChart (how): "Turn on Plain English to read the chart without the medical words."
- welcomeParts (how): "Pick a part from each tray to build a word from June's chart."
- built (event, each new term built; stale on the next tap): "(term): (meaning)."

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

## Done when
1. All 13 scenes play in order 7 p.m. to 7 a.m., each with its role, words and three options; every role opens a career sheet with 2025 pay and training.
2. Each of the 17 terms splits into the listed parts and meanings, in Shift, Chart and Word parts.
3. Word parts builds all 17 and rejects other combinations with the hint; bradycardia appears only there.
4. Scene 8 C changes scene 10's reading story; scene 4 B moves oxygen to 9:15 in the notes; every listed outcome writes its note.
5. Chart with Plain English on reads every note with no medical word left unexplained.
6. No score, timer or win screen anywhere; the delay tally is plain minutes from the notes.
7. Option order changes between visits; a revisited scene is read-only.
8. Scene card, options and Next hour are visible without scrolling at every STANDARDS.md size; the preview is readable.
9. How lines once each in five actions in a row; scene lines, delay, morning and built every time, dropped when stale.

## Open questions
- Nine roles are new to careers.json (listed in Content). Add them to the shared builder (they would also appear in career-match-quiz's Explore view and career-cluster-explorer's counts unless filtered), or keep them in this tool's own data?
- Scene 2 touches patient privacy with a nosy neighbor, and scene 10 shows a nursing assistant noticing a low oxygen reading. Both are calm and non-graphic. Anything a health teacher or parent might want changed?
