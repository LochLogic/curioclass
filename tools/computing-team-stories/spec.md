# Computing Team Stories

## One idea
Five computing teams each cracked one stubborn problem because of who was in the room (a color-blind game tester, a community health worker who grew up in the neighborhood, a tribal water office's 30 years of creek logs, a copy editor who lives up the canyon, a prosthetic user who said "I have one hand when I'm holding something"), and you can take any person off the team and watch the story change, then match your own interests to the people you met and sketch three next steps.

## Not like
- industry-device-tour (6-8, gap fill, not specced) and job-shadow-day (3-5, gap fill): computing at work, by device or job. Here the unit is a team and one problem, and the point is how a mix of people solved it.
- career-cluster-explorer and career-match-quiz (careers family): browse or match careers by cluster and interests. Here careers are reached through people on teams; the career data is reused, not a second engine.
- data-policy-council (9-12 CS): council members argue a policy. Here nobody argues; you remove a person and read what the team would have missed.
- sprint-board (this group): your real team runs a project. Here you study other teams.
- emerging-tech-pitch, cloud-through-time (this group): technology's reach and history. This tool is about the people who make computing work.

## Who and how
- Grades 9 to 12, computer science. Module: Computing Teams and Careers (Computing and Society), "How diverse teams use computing, and where your goals meet computer science". Topic line: "computing teams and careers".
- Driver: students on laptops, alone. 20 to 35 minutes.
- Standards (module codes, CSTA 2026): HS-SOC-CE-45 (how diverse teams use computing: Teams and the "Take off the team" switch), HS-SOC-CE-46 (connect computing to your own career goals: You and Next steps). CSTA 2017 crosswalk: 3A-IC-27 (use collaboration tools to connect people in different cultures and career fields), 3B-IC-25 (evaluate artifacts to maximize benefits), 3A-IC-24 (computing's impact on practices).
- tool.json: driver "students", minutes "20-35", modes ["You", "Teams", "Next steps"], grades_label "Grades 9-12". Kit starter, `kit:theme-912`.

## Screens and modes
Header (kit): "Computing Team Stories", small line "Five teams, five problems". Modes: **You** (first, can be skipped with **Skip to the teams**), **Teams**, **Next steps**. Motion, Sound, Read.

### You
Stage: two chip clouds. **I'm into** (pick any): Art, Music, Games, Health, Sports, Nature and weather, News and writing, Building things, Math puzzles, Helping people, Languages, Military service, Business. **I want work that** (pick up to three): Helps my community, Makes things people use, Solves hard puzzles, Gets me outdoors sometimes, Pays well, Is steady, Is on a team, Is creative. Panel: "People like you" count, **Meet the teams**. Picks live in the page; Save is in Next steps.

### Teams
Stage left: five team cards in a column (scene image, team name, one-line problem). Stage main, for the open team: the **story strip**, four beats side by side (stacked under 760 px): **Problem**, **Stuck**, **Turn**, **Shipped**, each two or three sentences. Under it the **team row**: five member badges (initials in a circle, a role icon, the role name). Badges of members who match two or more of the student's picks have a small "like you" ribbon.
Tap a badge: the **member card** in the panel: name and role, "What I do on a normal day", "How I got here", "Tools I use", "What I brought to this problem", a **Career** line (career name, median pay with year and source, typical entry-level education, from the careers data) with **Open career sheet** (the shared careers sheet). At the bottom of the card, the switch **Take off the team**.
Taking a member off: their badge greys with a dashed outline; the beats that depend on them rewrite to the "without" version, marked with a ⟲ and the line "Without [name]: ..."; beats that don't change stay and a note says "The team would miss [name]'s [skill], but this story ends the same way." **Put everyone back** restores the team. Only one member can be off at a time (taking another off puts the first back), so each change reads clearly.
Panel footer: "These teams and people are made up. The kinds of work, careers and facts are real (Sources)."

### Next steps
Stage: the **career shelf**: every career from the five teams as a card (name, median pay, education, the member who does it); cards for careers that match the student's picks come first. Below: **My next three steps**: twelve step cards (Content); pick up to three; they fill a "My path card" with the picked interests, goals, two careers the student stars on the shelf, and the three steps. Panel: **Copy my path card**, **Save on this device**, **Clear saved**.

## Content
Each team: problem; beats; five members (name, role, path, tools, what they brought, career id, interest and goal tags); the two "without" members and their rewritten beats. The other three members show the "ends the same way" note.

**1. Lantern Bay Games** (a 14-person game studio). Problem: "Beta players kept quitting on level 3 of their co-op puzzle game."
Beats. Problem: "Half the beta players quit on level 3." Stuck: "The designers made the puzzle easier twice. Players still quit." Turn: "Ollie, a tester, noticed level 3 is the first puzzle where you match red and green switches. He has red-green color blindness and couldn't tell them apart, and about 1 in 12 men can't either. The team added shapes to every switch, and Priya added a different sound to each." Shipped: "Quitting on level 3 dropped to the same rate as other levels."
Members: Mara Quinn, game designer (art school, then small games at night; Figma, the game engine's level editor; tags Art, Games / creative, makes things; career game-design). Dev Patel, gameplay programmer (associate degree at a community college, then a transfer to a four-year school; C#, version control; Games, Math puzzles / hard puzzles, pays well; software-dev). Ollie Brandt, QA tester (retail job, then a software testing certificate; bug tracker, test plans; Games, Helping people / on a team, steady; software-dev, shown as "Software quality assurance analysts and testers" inside the Handbook's software developers profile). Priya Nair, sound designer (music degree; audio workstation, field recorder; Music, Games / creative; sound-tech). Teo Alvarez, community manager (bilingual, ran player forums as a teen; community tools, surveys; Languages, Games / helps community, on a team; market-research).
Without Ollie: Turn "Nobody on the team has trouble with red and green. They keep making the puzzle easier." Shipped "Players who can't tell red from green still quit."
Without Priya: Turn "Shapes go on every switch." Shipped "Most players are fine, but players with low vision still struggle with the small shapes."

**2. Pine County Public Health, data team.** Problem: "Flu shot sign-ups were low in the Eastgate neighborhood, even with free clinics."
Beats. Problem: "Eastgate had the county's lowest sign-up rate." Stuck: "The dashboard made it look like Eastgate wasn't interested." Turn: "Luz, a community health worker who grew up in Eastgate, pointed out that the sign-up form required an email address and was only in English. Many families there use a phone with no email. Ken built text-message sign-up in English and Spanish, and Sam re-ran the map." Shipped: "Eastgate sign-ups caught up with the county average by the second clinic."
Members: Ruth Okafor, epidemiologist (master of public health; statistics software, disease reports; Health, Math puzzles / helps community, steady; epidemiologist). Sam Lee, data analyst (statistics degree; SQL, Python, maps; Math puzzles / hard puzzles, steady; data-sci). Luz Ramírez, community health worker (grew up in Eastgate; state community health worker certificate; phone, clinic calendars; Helping people, Languages / helps community, on a team; chw). Ken Morrison, web developer (Army signal specialist, then a coding bootcamp; JavaScript, text-message service; Military service, Building things / makes things, steady; web-dev). Ada Nwosu, nurse who runs the clinics (nursing degree, license; scheduling, health records; Health, Helping people / helps community; nurse).
Without Luz: Stuck "The team decides Eastgate isn't interested." Turn "The clinic budget moves to other neighborhoods." Shipped "Eastgate's rate stays the lowest."
Without Ken: Turn "The team knows the form is the problem, but an outside company can't change it until next season." Shipped "This year's sign-ups stay low."

**3. River Basin Lab** (a state university climate modeling group). Problem: "Their flood model missed flash floods in small mountain towns."
Beats. Problem: "Two towns flooded on days the model called safe." Stuck: "The model only had one rain gauge for every 100 km. Storms between gauges vanished." Turn: "Ray, who runs a tribal nation's water office, had 30 years of creek-level logs written by hand at canyon stations. Joy turned them into data, and Marcus added them to the model's checks." Shipped: "With the logs, the model caught the flash floods in its test years, and the water office got the cleaned data back."
Members: Hana Sato, atmospheric scientist (PhD; climate model code, supercomputer jobs; Nature and weather, Math puzzles / hard puzzles; atmo-sci). Marcus Bell, research software engineer (physics degree, learned to code in research; Fortran, Python, version control; Math puzzles, Building things / makes things; software-dev). Joy Kim, data engineer (self-taught, then an associate degree; databases, scanning and data entry tools; Building things / steady, on a team; data-sci). Ray Whitehorse, water resources manager for a tribal nation (forestry degree, decades of field work; creek gauges, field logs; Nature and weather, Helping people / outdoors, helps community; hydrologist). Lin Zhou, graduate student (computer science; Python, plots; Math puzzles, Nature and weather / hard puzzles; comp-research).
Without Ray: Turn "Nobody knows the old logs exist. The model looks fine on the data it has." Shipped "The next flash flood is missed again."
Without Joy: Turn "The logs stay on paper. Typing them in would take longer than the grant." Shipped "The fix waits a year."

**4. The Valley Ledger, graphics desk** (a regional newspaper). Problem: "During a wildfire, the evacuation map wouldn't load for readers with weak signal."
Beats. Problem: "Readers in the canyon saw a blank page." Stuck: "The map was a big interactive page, about 6 megabytes." Turn: "Ivy, a copy editor who lives up the canyon, read the readers' messages: 'Just tell me if my street is in the zone.' Omar built a text-only list by street that loads almost at once, and Carl made a printable version for the shelters." Shipped: "The light version was the most-read page that week."
Members: Nia Brooks, graphics reporter (journalism degree; mapping tools, charts; News and writing, Art / creative, helps community; reporter). Omar Haddad, newsroom developer (computer science degree; JavaScript, servers; Building things, News and writing / makes things; web-dev). Bea Santos, data reporter (political science degree, taught herself code; spreadsheets, Python; News and writing, Math puzzles / hard puzzles; reporter). Carl Jensen, designer (graphic design degree; layout software; Art / creative; graphic-design). Ivy Two Rivers, copy editor (English degree; style guide, headline tools; News and writing, Languages / helps community; editor).
Without Ivy: Turn "Nobody links the complaints to the page size. The team keeps polishing the map." Shipped "Readers in the canyon still see a blank page."
Without Omar: Turn "The list goes out as a slow PDF." Shipped "It helps, but loads too slowly on weak signal."

**5. Kestrel Limb Lab** (a small prosthetics startup). Problem: "Their app for switching a prosthetic hand's grips needed two hands."
Beats. Problem: "Users almost never switched grips." Stuck: "The engineers added more grip modes." Turn: "Andre, a paid user-advisor who has used a prosthetic arm for 12 years, said: 'I have one hand when I'm holding something. I can't open an app.' Wen built a switch you trigger with a double squeeze of the arm muscles, and Grace adjusted the socket so it didn't trigger by accident." Shipped: "Users switched grips through the day."
Members: Tomás Vega, biomedical engineer (bioengineering degree; CAD, test rigs; Health, Building things / makes things, hard puzzles; biomed-eng). Wen Li, embedded software engineer (electrical engineering degree; C, signal tools; Building things, Math puzzles / hard puzzles, pays well; software-dev). Grace Mensah, certified prosthetist (master's in orthotics and prosthetics; scanning, fitting tools; Health, Helping people / helps community; prosthetist). Andre Lewis, user-advisor and peer mentor (Army veteran, prosthetic user for 12 years; his own arm and a notebook; Military service, Sports / helps community, on a team; no career card: "Paid advisors bring lived experience; it is a role, not a job title."). Sofia Russo, industrial designer (industrial design degree; sketching, 3D printing; Art, Building things / creative, makes things; ind-design).
Without Andre: Turn "The team adds a ninth grip mode." Shipped "Nobody uses it either."
Without Grace: Turn "The double squeeze works on the bench but triggers by accident when the socket shifts." Shipped "Users turn the feature off."

Careers (ids): from `careers.json` already: game-design, software-dev, market-research, data-sci, web-dev, nurse, graphic-design. Added for this tool through the careers builder (BLS Handbook profile and OEWS May 2025 median pay, same fields as the siblings): sound-tech (Broadcast, sound and video technicians), epidemiologist (Epidemiologists), chw (Community health workers), atmo-sci (Atmospheric scientists, including meteorologists), hydrologist (Hydrologists), comp-research (Computer and information research scientists), reporter (News analysts, reporters and journalists), editor (Editors), biomed-eng (Bioengineers and biomedical engineers), prosthetist (Orthotists and prosthetists), ind-design (Industrial designers). Pay and education on screen come only from that data, with "May 2025" and the source.

Fact in team 1: "About 1 in 12 men and 1 in 200 women have color vision deficiency" (NEI).

Next steps cards: Take AP Computer Science Principles or AP Computer Science A. Join or start a coding, robotics or game club. Build a small project for someone you know. Try a game jam or a hackathon. Take a dual-credit class at a community college. Volunteer with a group that uses data (a food bank, a park, a clinic). Shadow someone at work for a day. Look up apprenticeships in computing. Learn about technical jobs in the military. Make a simple portfolio page of what you've built. Learn a second language, spoken or programming. Ask a teacher about summer programs.

## Interactions in detail
- Every team is open from the start; order doesn't matter. Opening a team puts everyone back.
- Matching: a member is "like you" when two or more of their tags are among the student's picks. With no picks, no ribbons and the shelf keeps its default order (team order). Nothing is scored.
- Take off the team: the changed beats crossfade (no motion with Motion off); a screen reader hears "Story changed: Turn, Shipped".
- Career sheet: the shared careers sheet (career-cluster-explorer's Family engine part), opened read-only.
- Next steps: a fourth pick replaces the oldest with a note. Copy my path card copies plain text. Save on this device stores picks, stars and steps; Clear saved removes them. No names or free text anywhere.
- Keyboard: modes, chips, team list, beats, badges (arrow keys), then the panel. Visible focus.
- Sizes: at 1366x768 and 1280x720 the four beats and the team row fit without scrolling beside the panel; at 760 wide the beats stack and the team list becomes a picker; at 680x425 the story shows one beat at a time with Previous and Next. Beat text at least 14 px.

## Look
- Accent `--brand #ef8bff` (orchid: badges' rings, "like you" ribbons, the header rule, Take off the team) with `--brand-ink #2a0a30`, on `kit:theme-912`.
- Team cards each get a scene image tinted toward the dark theme; beats on `--sec-bg` cards; rewritten beats get a dashed orchid left border and ⟲.
- Contrast (computed): brand on `--panel` 8.08:1, on `--sec-bg` 7.66:1; brand-ink on brand 8.28:1; theme ink on `--sec-bg` 13.9:1. All pass AA.
- Neighbors: capture-the-flag pink #ff7ac8 and ai-evaluator pink #f472b6 (orchid here is bluer and lighter), sorting-showdown violet #c39bff, api-playground lemon, network-architect sky blue, simulation-studio orange; group siblings coral, cyan, lime and light pages.

## Art
Five scenes, Cloudflare FLUX.2 (`scripts/cfart.py`), 16:9, cutout no, people no; shown as the team card thumbnail (cropped) and a faint backdrop behind the story strip. Prompts describe empty workspaces with blank screens and blank surfaces:
- cts-game-studio: "an empty indie game studio at dusk, two desks with dark blank monitors, sketchbooks with doodled creatures, a game controller, warm desk lamps, soft illustrated style"
- cts-health-office: "an empty county health office, a large paper map of a town pinned to a corkboard with colored pins, a laptop with a dark blank screen, a clinic cooler box, daylight, soft illustrated style"
- cts-river-lab: "an empty university lab, a tall server rack with small lights, a table model of a mountain river valley, stacks of old paper logbooks tied with string, soft illustrated style"
- cts-newsroom: "an empty newsroom desk at night, three dark blank monitors, a police scanner, a coffee mug, a printed map with blank labels, soft illustrated style"
- cts-limb-lab: "an empty workshop bench, a white 3D-printed robotic hand, a small 3D printer, calipers and wires, a sketch of a hand, soft illustrated style"

## Voice
Bank voice `smooth-narrator`, style "Say smoothly and warmly, like an audiobook narrator": the teams' stories told like short chapters. Not used by a 9-12 CS tool or a group sibling. Light narration:
1. how, welcome (You): "Pick what you're into and what you want from work. Or skip ahead and meet the teams."
2. how, first team opened: "Read the four beats. Then tap a person and try taking them off the team."
3. event, a story-changing member is taken off (every time; stale if put back first): "Without [name], the story changes. Read the new ending."
4. event, a member with no story change is taken off (every time; stale if put back): "The team would miss them, but this story ends the same way."
5. how, welcome (Next steps): "Star two careers and pick three next steps. They make your path card."
Line 3 has one recording per story-changing member (10). Read speaks the hint. Beats are read on screen, not spoken.

## Family engine
careers (from career-cluster-explorer's spec): the shared `careers.json` and its career sheet. This tool reads `name`, `pay`, `edu`, `ooh` and the source line, and asks the builder (`scripts/careers_data.py`) for the eleven careers listed in Content, with the same fields as the siblings. It adds no new fields.

## Sources
- CSTA 2026 PK-12 Computer Science Standards: https://csteachers.org/2026-csta-pk-12-computer-science-standards/ ; CSTA 2017: https://csteachers.org/k12standards/
- Career pay and jobs: BLS Occupational Employment and Wage Statistics, May 2025, through `careers.json`; education and profiles: BLS Occupational Outlook Handbook, https://www.bls.gov/ooh/ (profiles: software developers, quality assurance analysts and testers; web developers and digital designers; data scientists; epidemiologists; community health workers; atmospheric scientists; hydrologists; computer and information research scientists; news analysts, reporters and journalists; editors; bioengineers and biomedical engineers; orthotists and prosthetists; industrial designers; broadcast, sound and video technicians; graphic designers; registered nurses; market research analysts; special effects artists and animators for game design as listed in `careers.json`).
- Color vision deficiency, about 1 in 12 men and 1 in 200 women: National Eye Institute, "Color Blindness": https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/color-blindness
- Community health workers bridge health services and communities: CDC, "Community Health Workers": https://www.cdc.gov/chronic-disease/php/community-health-workers/
- Diverse teams and lived experience in design: W3C Web Accessibility Initiative, "Involving Users in Web Projects for Better, Easier Accessibility": https://www.w3.org/WAI/planning/involving-users/
- AP Computer Science Principles and AP Computer Science A: College Board, https://apstudents.collegeboard.org/courses
- The teams, people and story outcomes are made up, inspired by real kinds of work.

## Done when
1. You: picking Games and Is creative puts "like you" ribbons on Mara and Priya (two tag matches each) and on no one else at Lantern Bay.
2. Lantern Bay: taking Ollie off rewrites Turn and Shipped with ⟲ and "Without Ollie"; taking Dev off leaves all beats and shows the "ends the same way" note.
3. Only one member is off at a time; Put everyone back restores the original beats.
4. Every member card shows a career line with pay labeled May 2025 and a source, except Andre's role note.
5. Next steps lists every career from the five teams; starred careers and three steps fill the path card; Copy gives plain text with no names.
6. Save, reload: picks return; Clear saved removes them.
7. Beats and the team row fit beside the panel at 1366x768; at 680x425 one beat shows at a time.
8. Voice: line 3 plays each time a story-changing member is taken off and is dropped if they are put back first.

## Open questions
- [computing-team-stories] Eleven careers are added to the shared careers.json through the builder. OK to extend it, as hospital-shift also asks?
- [computing-team-stories] Team 3 includes a tribal nation's water manager and team 4 a copy editor named Ivy Two Rivers. Should a Native educator review those two portrayals before build?
