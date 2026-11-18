# Fix: social-studies-grade-3 unit 2 (s02.md), 2026-11-17

Findings merged: 29 (assessment 13, sources 10, sequence 6). Fixed: 25, some in part. Rejected: 4. Lead: 5. Held up: assessment 13 of 13, sources 9 of 10, sequence 4 of 6 (two only in part). Gate: `unitplan.py check social-studies-grade-3` gives PASS for s02.md (1,250 words, at the cap, so three fixes were shortened and two rejected for it).

Notes for the lead:
- Assessment 11: the response groups are one sentence in field 7, not a table, because table pipes count as words against the cap. The sheet now says nothing is self-marked.
- Two letters added after AB: AC (mocking or ignoring another view) and AD (the Constitution was always there). Both are in the day 48 groups.
- Packets renamed Local record, Town model, Funding model, Rule record, State card, Class record. Exits 29 to 31, 33, 35 and 38 to 40 were rewritten with fresh structures. A Minutes column (4, 4, 3, 3, 3, 3, 3, 7 = 30) and an Owner column from days.csv were added.
- Sources 1: the plan now says Menominee carries only the constitutional-structure comparison here and unit 4 uses it for homeland, treaty and oral history. Sources 2: a dated line records what was read; the 24-month news search was not run.
- The file had mixed CRLF and LF endings; it is now LF throughout.

REJECTED: sources 7 | Pair each government page with its form and add the class's own state education page on local boards as the general source | over the word cap (field 10 is at 1,250 words and nothing existing may be cut); the pairing is a short edit once room exists | the writer's brief (general form first)
REJECTED: sequence 4 | Move the source maker, date and purpose model from day 27 to day 32 | day 32 is marked compressible and the finding itself calls it overloaded, so the move trades one overloaded day for another; day 27 is relieved by the small-group repairs of sequence 1 | UNIT-PLAN rule 6 (social studies) and days.csv day 32 note
REJECTED: sequence 5 | Name the unit 1 days for the biography (day 1) and the two-source claim (days 19 to 21) in the hand-offs | over the word cap (about 11 words in field 3, which has no room) | none
REJECTED: sequence 6 | List printed office, place and symbol cards, nested outline sheet, official-page printouts and passage, with printing before days 27, 32 and 42 | over the word cap for all but ballot slips (field 8 has no room); ballot slips were added | none

LEAD:
- Sources 1: Cory or the lead decides whether day 43 should use a nation other than the Menominee Indian Tribe of Wisconsin (the frame names it as a worked case in more than one unit); a swap needs new constitution pages read and unit 4 checked.
- Sources 2: run the news search of the last 24 months for the Menominee, Boston, Boulder and Lexington forms and replace the "not yet run" clause in the field 6 background line.
- Sequence 5 and 6 (above) need about 40 words of room in fields 3 and 8, for example by moving text out of the counted fields.
- days.csv day 47 codes omit D1.1.3-5, D1.2.3-5 and D1.4.3-5, and day 26 omits D1.1.3-5.
- scope-and-sequence.md readiness line names ss1-elected-leaders, ss1-citizens, ss1-voting and ss1-group-roles, while days.csv day 24 and the plan name ss1-leaders, ss1-voting and ss1-group-roles; data/plans/social-studies-grade-3/ has no source-map.csv.
