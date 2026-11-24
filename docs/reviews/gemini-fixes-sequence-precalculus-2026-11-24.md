# Gemini fixes: scope and sequence of precalculus, 2026-11-24

Outside cold read: S:\CurioClass-gemini\reports\sequence-precalculus-gemini-read.md. Checked against the files, the expert read docs/reviews/sequence-precalculus-2026-11-24.md, its fix pass docs/reviews/sequence-precalculus-fixes-2026-11-24.md, sequence-write.md, the lead calls of 2026-11-15 (docs/reviews/sequence-lead-calls-2026-11-15.md) and DESK-ANSWERS.md. Every finding was checked in the files before any change.

## Findings

- **G1, earlier-grade ids in `skills` on 28 days** (37 ids): wrong. Rule 2's line ("named by id in that day's note, never in its `skills` column") covers the rows a **readiness check** samples (DESK-ANSWERS 2026-11-15, the same words). Retrieval rows are a separate settled call: lead call 4 of 2026-11-15 (sequence-lead-calls-2026-11-15.md, line 90) says earlier-grade retrievals carry the row id in the skills column. scripts/unit_skeleton.py reads them that way (earlier_rows: "math lead call 4 puts its id in the skills column"; such an id counts as an earlier row, not an owned one). The expert fix pass moved days 20 and 34 onto this practice on purpose. Checked all 28 days: every earlier-grade id in `skills` is a retrieval named in the note; the three readiness checks (days 49, 101, 132) name their rows in the note only, with none in `skills`. No change. Gemini's Calculus finding 1, which it calls the same kind, falls under the same call.
- **G2a, day 46 split 25/25 between response and report revision**: partly. The frame allows it ("revised in part of a later day (never the end day or a day that first teaches a topic)"), and rule 2 sets no minimum response time. The two alternatives fail: day 44 is a Fluency day, which revises no writing, and one evening is too short for feedback on 30 reports (the expert fix pass set two evenings for unit 8's draft on day 128 and revision on day 130). The gap Gemini names is real but unexplained, so I added it: the unit 3 Assessment line now says why unit 3 splits its respond day where units 6 to 8 do not, and that the first 25 minutes cover day 45's most-missed items, a reteach by group and a parallel retry. No day, kind or count changed.
- **G2b, stale "(For the lead 4)" and "(For the lead 3)" pointers**: holds. The For the lead section now has items 1 and 2 only. I removed both pointers (unit 3 prose, unit 6 Assessment line). The facts they pointed to are already in the text: day 43 draft and day 46 revision, and the single response on day 98.
- **G3, "the base text has no..." on ours days 24, 29, 95, 107, 125, 134**: partly. Rule 8 is about the "Base" label that marks an adapted day, and a lowercase "the base text has no section" says the opposite. No gate or skeleton parse misreads it. Still, the reword is cheap and leaves no doubt, so all six notes now read "no OSP section ..." (OSP is the source id the notes already use). I kept product names out of the wording on purpose.

Totals: 4 findings: 1 holds, 2 partly, 1 wrong, 0 already fixed.

## Facts and figures checked

- Carbon-14 half-life about 5,730 years (day 39): holds. [Britannica](https://britannica.com/science/carbon-14-dating) and [NOAA GML](https://gml.noaa.gov/infodata/isotopes/decay.html) give 5,730 plus or minus 40 years. Newer evaluations give about 5,700 plus or minus 30 ([Wikipedia](https://www.wikipedia.org/wiki/14C_date)). "About 5,730" stands.
- Yellowstone gray wolves, NPS reports 1995 to 2004 (day 43): holds. The [1995 and 1996 biennial report](https://www.nps.gov/yell/learn/nature/upload/wolfreport_95-96_508.pdf) covers the January 1995 releases, and the [2004 annual report](https://www.nps.gov/yell/learn/nature/upload/wolfrpt04.pdf) counts at least 171 wolves at the end of 2004. One note for the unit plan, already its job on day 43: the [2005 report](https://www.nps.gov/yell/learn/nature/upload/wolfrpt05.pdf) shows a fall to at least 118, so the 1995 to 2004 window must stay fixed as the day sets it.
- Mathematics: (-1 + sqrt(3) i)^3 = 8 (modulus 2, angle 120 degrees, so 8 at 360 degrees); r = 4 cos(theta) is the circle with center (2, 0) and radius 2; ln(y / (L - y)) is linear in time for a logistic. All exact, no change.

## Changed

- docs/courses/precalculus/scope-and-sequence.md: two stale pointers removed; unit 3 Assessment line explains the day 46 split.
- data/plans/precalculus/days.csv: notes of days 24, 29, 95, 107, 125, 134 reworded.

## For Cory

Nothing. Settled fixes and Desk decisions kept: lead call 4 (retrievals in `skills`) and the 2026-11-15 readiness-in-note call.

## Gates

- `python -X utf8 scripts/sequence.py check precalculus`: 0 failures (sequence and frame).
- `python -X utf8 scripts/frame.py check precalculus`: 0 failures (10 units, 160 days).
- `python -X utf8 scripts/frame.py calendar`: exit 0.
