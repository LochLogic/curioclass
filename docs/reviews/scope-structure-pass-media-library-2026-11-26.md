# Scope structure pass: media arts K to 5 and library K to 2 (2026-11-26)

The lead's structure pass on two decided items: A, the media arts K to 5 year-end check week (docs/reviews/scope-group-media-arts-2026-11-26.md
finding 1, option (a)); B, the online-safety brand name in the library K to 2 frames. days.csv was edited with the csv
module (a round trip was checked byte for byte first; minimal quoting and CRLF line endings kept). No git, no stash.

## A. Media arts K to 5: the year-end check moves to week 32

**days.csv (media-arts-grades-k-to-2, media-arts-grades-3-to-5).** In each year the year-end check and its respond day
move to the end of the year, after the screening unit; every other day keeps its order. Each day keeps its goal,
skills, codes, assess, retrieves and kind (checked by script); `school_day` slots stay in order, so the moved check
takes the year's last two slots and the screening unit moves two slots earlier.

| Course | Year | Year-end check, respond (was) | Now | Screening unit (was) | Now |
|---|---|---|---|---|---|
| K to 2 | K | 53, 54 (week 27) | 63, 64 (week 32) | 55 to 64 (weeks 28 to 32) | 53 to 62 (weeks 27 to 31) |
| K to 2 | 1 | 117, 118 | 127, 128 | 119 to 128 | 117 to 126 |
| K to 2 | 2 | 181, 182 | 191, 192 | 183 to 192 | 181 to 190 |
| 3 to 5 | 3 | 51, 52 (week 26) | 63, 64 (week 32) | 53 to 64 (weeks 27 to 32) | 51 to 62 (weeks 26 to 31) |
| 3 to 5 | 4 | 113, 114 (week 25) | 127, 128 (week 32) | 115 to 128 (weeks 26 to 32) | 113 to 126 (weeks 25 to 31) |
| 3 to 5 | 5 | 177, 178 (week 25) | 191, 192 (week 32) | 179 to 192 (weeks 26 to 32) | 177 to 190 (weeks 25 to 31) |

Day references inside the notes and goals were renumbered (for example "Response time: day 64" on the old day 63 is
now "day 62" on day 61).

**Frames.** Checks table: After unit 3, 7, 11 to 4, 8, 12, week 32 and the new days; "Unit 4 (8, 12), just before, is
assessed by its own screening (showing)". Course-level checks bullet rewritten (arts are specials, CALENDAR.md rule 1;
year-end week 32 after the screening unit). The 3 to 5 frame's "CALENDAR.md stagger tool c" reason is withdrawn there,
and its year-end labels now read "Samples units 1 and 2 and carries unit 3" (years 4 and 5 the same), which settles
the 3 to 5 scope's For the lead item 2. Units-table rows 4, 8, 12: "ends the year after the year-end check" became
"comes just before the year-end check (week 32)". Once-a-week path: the screening unit's six sessions run in weeks 25
to 30, the year-end check session in week 31, its respond session in week 32 (as media arts 6 to 8 does, since a
once-a-week year has one session in week 32); no unit pauses for it. For the lead items on check weeks updated
(K to 2 item 3; 3 to 5 item 2): the week 27, 26 and 25 clash lists went with the move. Seam day ranges renumbered.

**Scopes.** Each year-end check section now follows its screening unit, with its new days and week 32; unit headings
and spans carry the new days and weeks; the checks tables, the codes-not-sampled reasons, the once-a-week weeks and
tables, and the For the lead items (K to 2 item 1; 3 to 5 items 2 and 5) updated. Every day reference was renumbered
by script and the diff read line by line; the year spans (1 to 64, 65 to 128, 129 to 192) and the 3 to 5 frame's
K to 2 unit 11 range (171 to 180), which the script first moved by mistake, were set back.

**Outside the two courses.** One stale seam reference in docs/courses/media-arts-grades-6-to-8/frame.md (3 to 5 unit 12
"days 179 to 192") now reads "days 177 to 190". No other course cites these days.

**CALENDAR.md.** The "Target weeks, K to 8" table has no arts columns, so the cells named in the read ("21, 27" and
"17, 26 / 17, 25 / 18, 25") are not in it; the media arts weeks live only in the generated `gen:calendar` table, which
`frame.py sync` rewrote: only the six media arts K to 5 rows changed (year-end weeks 27, 26, 25 to 32; last unit week
32 to 31).

**Sync.** `frame.py check` passed for both courses first. The first `frame.py sync` wrote calendar.csv and stopped
on an OSError writing CALENDAR.md; a second run finished. Both runs also changed about 40 rows of other courses in
data/plans/calendar.csv (labels taken from other workers' frame edits: computer science grade 9, health K to 2 and
3 to 5, SEL 6 to 8 and others). Those rows were put back to their pre-sync text, so calendar.csv now differs from
before only in the media arts K to 2 and 3 to 5 rows. frames.csv did not change. CALENDAR.md changed only in the six
media arts rows. A later sync will bring in the other courses' label changes.

## Left open for the lead

- **What the year-end check samples.** The lead set "each day keeps its content and codes", so the checks still sample
  the same ids as before (units 1 and 2, 5 and 6, 9 and 10), with the third unit's record carried unscored. The read's
  wider sample (adding the third unit's judge row, MA:Re8.1.K, 1, 2 and MA:Re8.1.3, 4, 5, as media arts 6 to 8 does)
  would change the check days' goals and codes. Each scope now names this as open.
- The 3 to 5 scope's For the lead item 6 (once-a-week rebalance for units 4, 8 and 12) is untouched.

## B. Library K to 2 frames: the online-safety brand

docs/courses/library-and-research-skills-kindergarten, -grade-1 and -grade-2 frame.md named the National Center for
Missing and Exploited Children's presentation "Be Safer Online with NetSmartz: Grades K-2". Each now reads "a free
K to 2 online-safety presentation from a national child-safety nonprofit", following the grade 2 scope's wording ("the
free K to 2 online-safety presentation"). The listing url stays as the source record the lead opens at grade close
(browser check); the url itself carries the organization's address.

## Defect ledger

Ten rows, `plan.py defect --status=fixed --made-at=scope`: media arts K to 2 days.csv, scope-and-sequence.md and
frame.md; media arts 3 to 5 days.csv, scope-and-sequence.md and frame.md; media arts 6 to 8 frame.md; library K, 1 and
2 frame.md.

## Checks

| Course | sequence.py check | frame.py check |
|---|---|---|
| media-arts-grades-k-to-2 | 0 failures | 0 failures |
| media-arts-grades-3-to-5 | 0 failures | 0 failures |
| media-arts-grades-6-to-8 | 0 failures | 0 failures |
| library-and-research-skills-kindergarten | 0 failures | 0 failures |
| library-and-research-skills-grade-1 | 0 failures | 0 failures |
| library-and-research-skills-grade-2 | 0 failures | 0 failures |
