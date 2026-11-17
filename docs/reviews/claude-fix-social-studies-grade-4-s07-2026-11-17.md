# Fix report: social-studies-grade-4 unit 7 (s07.md), 2026-11-17

Findings merged: 32 (assessment 14, sources 11, sequence 9, less overlaps: assessment 5 and sequence 3 on exit 148; assessment 14 and sources 9 on day 144; assessment 12 and 4 on exit 152). Fixed: 26 (some in part). Rejected: 4. Lead: 8.
Held up: assessment 14 of 14 (13 fixed fully, 13 adds minutes without cutting tasks); sources 6 of 11 fixed or marked inside the cap (2, 3, 4, 6, 7, 8, 9, 10, 11 marked or reworded; 1 and 5 rejected); sequence 6 of 9 (1, 2, 3 in part, 4, 6; 5, 7, 8, 9 not the plan's to change or over the cap).
Gate: `unitplan.py check social-studies-grade-4` PASS for s07.md (1245 words counted of 1250). Line endings were mixed CRLF and LF; the file is now all LF.

What changed: field 7 rewritten for social studies (nothing self-marked, teacher scoring after class, component-to-move list, day 160 in four groups, day 159 5 minutes for collecting, not marking); C4 look-for says Southwest; wrong answers refiled under letters that describe them (C2, C5, H1, C3, C4); letters no answer could produce removed (exits 152, 155, 156); M2 key matches the stimulus; S technological case changed from a reservoir wall to a flood wall so it no longer retells Johnstown; exits 145, 147, 148, 149, 152, 153, 154, 158 rewritten (stories no longer repeat an end item, one question of at most two parts); A2 added for D1.1.3-5; owners set by section; minutes listed by item (35 in all); Filipino named on 143 with V; J wording says to check which body asked residents; claim-to-source table marks the weak or missing sources; day 144 marks its cards "to write with section 7.2"; both retrieval repairs now sit in the warm-up and a small group; supplies add printed current advice for day 155.

REJECTED: sources 1 | Seventeen strip statements have no free source, so add one for each or drop them | Sourcing them needs reading many pages and is not a plan edit; dropping them would remove most of the scored strips, and the plan already marks them "from memory" and "still to make" | UNIT-PLAN rule 16 (from memory marked) and field 10 "what is still to make"
REJECTED: sources 5 | Days 146 to 148 and 152 name no hazard agency pages in field 10 | Naming pages not yet read would invent sources, and field 10 is at the word cap (1245 of 1250); the day 152 and 155 teacher lines already require checking current official pages | UNIT-PLAN field 10 (verified or none), Length
REJECTED: sequence 7 | Field 3 should say what earlier units (science 4-ESS3-2, units 2, 4, 6) taught and on which days | The day numbers cannot be checked from this file and field 3 is at the word cap | UNIT-PLAN Length
REJECTED: sequence 8 | Carried should name the days where two-source claims are taught and practised before 158 | No day in days.csv teaches or practises it before 158, so naming days would be invented; the gap belongs to the section plans | UNIT-PLAN field 2 and days.csv

LEAD:
- days.csv day 159 codes omit D1.1.3-5 although A2 now tests it; add it, and change "marking 5" in the day 159 note to "collecting 5; teacher scores after class".
- days.csv day 148 goal omits Southwest hurricanes (MA.4.T4d.4 names hurricanes and drought) although exit 148 uses a Southwest hurricane card; add them or move that card.
- days.csv kinds: days 145 and 153 are Application but first teach D2.Geo.7.3-5 and policy tracing; consider Understanding.
- Section titles are missing from the header; fix in the skeleton generator.
- Where two-source claims are taught and practised before day 158 (D3.4.3-5, D4.1.3-5); decide in section 7.6.
- Free sources to find: 17 strip statements, exit captions on 138, 140 to 143 (141 reworded to "served at army posts and helped build them"), Chinese levee-building, Japanese farm associations, Eastern Band of Cherokee page, Somali organization page, Gold Rush on 142, day 144 alternatives.
- Hazard days 146 to 148 and 152: name and read agency pages; cite the official FEMA review report and agency page in the teacher background.
- Sensitivity study: name each unnamed source (Hmong center, Somali organization, Chinese descendant scholarship, survivor testimony, California Native nation) and mark reached or not.
