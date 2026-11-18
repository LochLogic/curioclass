# Fix report: english-language-arts-grade-3 unit 3 (s03), 2026-11-17

Findings merged: 26 (27 across the lenses; assessment 3 and sequence 3 are one fault on RL.3.2). Fixed: 23. Rejected: 2. Lead: 6 lines.
Held up per lens: assessment 14 of 15, sources 5 of 6, sequence 6 of 6 (sequence 6 and parts of others are lead items).
Gate: `unitplan.py check english-language-arts-grade-3` PASS for s03.md (word cap 1800 held by keeping field 2, 3, 7 and 10 additions short and putting the day-list notes in U6).

Fixed: blank lines removed so the 99, 106 and 113 rows join their tables; 99 RL.3.2 scope and revision-in-preparation wording; exits E100 to E103, E109, E110 rewritten as read-and-explain on new models; exits E83, E85, E86, E89, E112, E113, E117, E118 cut to two parts; E112 intended order added; 106 L.3.2a key now uses small words (new letter AM); E114 theme key matched to the stimulus; F118 gains the noise sentence (80 words kept) and its key; 92 RL.3.3 and RL.3.10 keys use sample words only; 85 L.3.5a has its own phrase (fallen flat added to P85); 85 and 92 RL.3.1 ask the student to write the question; new letter AN for report pace (116, 119, E116, E119); owners set by day; 114 RL.3.6 and RL.3.9 use new passages P114v, P114c and P114d; "invented for practice" printed on the panels and exit table header; field 3 pipeline remarks reworded; 107 split and no-spoken-report note; 110 and 99 retrieval and practice lines (in U6); safety link and company name dropped; Oz "only opening was read" line removed from the plan; P85 and P92 verbatim note; text 04 line.

REJECTED: assessment 4 | E85 repeats P85 and E92 repeats P92 with new nouns, so the exits should test a different skill | An exit is the same error on a new story, which is exactly what UNIT-PLAN rule 4 asks ("Same error, new numbers"); the stimuli share no story or wording with P85 or P92, so the exits add fresh evidence of the same skill (E85 was cut to two parts under another finding) | UNIT-PLAN rule 4.
REJECTED: sources 5 | Name a source for the Peter Pan stereotype claim or reword it as a flagged concern with no claim of fact | The claim sits in the generated frame line between skel markers (field 10), which cannot be edited by hand, and a prose rewording did not fit the 1800-word cap; the line already says "Flagged for the sensitivity read" | AGENTS.md (generated tables) and UNIT-PLAN Length cap.

LEAD:
- days.csv: rows exist in field 5 for codes days.csv does not list: RL.3.2 on 99; RF.3.3d, L.3.2e, L.3.2f, W.3.10, W.3.4 on 106; L.3.2c on 113. Add the codes to those days or drop the rows (the plan keeps the rows, tables repaired).
- days.csv 107 lists SL.3.4, SL.3.6, L.3.3b but they are taught on 108; the plan now gives 107 a read-aloud-only job, or drop the three codes from 107.
- source-map.csv shows "order conflict" on all 39 unit 3 rows and the header section titles are missing.
- Name a US classroom drama and movement safety source (state department or district guide, or Educational Theatre Association) once the safety read confirms it.
- Oz library file (library/wizard-oz/text.md): record its transcription source and a second free link that opens; the plan states the lead does this. Hand-off note: only the opening of Oz was read.
- Name one or two free sources text 04's facts are checked against, or confirm the "no claim about real publishers" line is enough; a cited source for the Peter Pan portrayal concern.
