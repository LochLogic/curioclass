1. [Header; missing merged U6 and U8] This one-section unit lacks the required section day rows and returning-practice schedule; the generated day list does not replace them | Teaching, practice and retrieval repairs cannot be traced within the available periods | Add U6 rows with opening times, carried materials, paper work, tool entries and evidence references, plus U8’s daily retrieval schedule, within existing 50-minute days.
2. [2, Teaching] Sahara reading moves to day 7 and day 8 is reserved for the claim, although days.csv assigns day 8 Understanding of Sahara change | The prose changes the scheduled day’s teaching purpose | Keep day 7 focused on ice and coastlines; explicitly teach Sahara change on day 8, then fit the claim and out-of-Africa handoff into that period.
3. [3, Returns] Day 39 is named as a chronology return, but its calendar goal is floods, irrigation and the Fertile Crescent | The return schedule points teachers to a day without planned timeline practice | Replace “days 39 and 52” with “day 52,” whose goal explicitly revisits the class timeline.

Check: `unitplan.py check` passes s01.md; notes at reported lines 87 and 90 flag multiple error letters, `(B, G)` and `(F, H)`, for the assessment reader.
Read limit: required `source-map.csv` was absent from the named folder and other checked course locations, so base-lesson “keep” alignment could not be verified.
Count: 3 findings (lens sequence).

## Files changed outside the allowed set

- build/lessons/math-4/u03-3/d018-key.html
- build/lessons/math-4/u03-4/d023-key.html
- data/media-manifest.txt
- docs/COURSES-STATUS.md
