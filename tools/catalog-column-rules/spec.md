# Catalog Column Rules

## One idea
Write the data dictionary for a real public library's checkout records (what each column means, its type, its allowed values or range, and the rules that tie columns together), then send a new branch's 40-row batch with 14 hidden problems through three checks built from your own dictionary, rules at entry, an overnight cleaning script, and a librarian reading a sample, and find that each one catches problems the others miss: entry rules stop "twelve" and month 13 but let a duplicate and a swapped title and author through, the script catches the duplicate and flags the 400, and only a person notices that "Douglass, Frederick" is in the title column.

## Not like
- data-table-builder (grade 4, data desk): picks a column type for class survey answers. Here each column gets a full definition and the definitions are run as checks.
- simulation-studio (9-12, data desk): one shifted column found, then a cleaning recipe. Here nothing is cleaned by hand; the dictionary is the product and the question is which way of checking catches what.
- lunch-survey-cleanup (6-8, data desk): pick drop, reformat or keep for each messy answer. Here the problems are found by rules you wrote, and comparing three checking methods is the point.
- api-playground (9-12 CS): reading a town's JSON responses. Here you define what valid data looks like before it arrives.
- data-policy-council (9-12 CS): what data should be kept. This tool takes the data as given and asks whether each value is right.
- pull-request-review, sprint-board (this group): checking code and running a team. This one checks data.

## Who and how
- Grades 9 to 12, computer science. Module: Data Dictionaries and Validation (Data and Analysis), "Describe each attribute and check data against its types, values and ranges". Topic line: "data dictionaries and checking data".
- Driver: students on laptops, alone or in pairs. 30 to 45 minutes.
- Standards (module codes, CSTA 2026): HS-DAT-DC-22 (describe each attribute of a dataset: Describe), HS-DAT-DC-24 (check data against types, values and ranges, and compare ways to do it: Check, Compare). CSTA 2017 crosswalk: 3A-DA-10 (evaluate the tradeoffs in how data elements are organized and where data is stored), 3B-DA-06 (select data collection tools and techniques to generate data sets that support a claim).
- tool.json: driver "students", minutes "30-45", modes ["Describe", "Check", "Compare"], grades_label "Grades 9-12". Kit starter, `kit:theme-912` with this tool's light palette (Look), `kit:data-desk`.

## Screens and modes
Header (kit): "Catalog Column Rules", small line "Say what good data looks like". Modes: **Describe** (first), **Check**, **Compare**. Motion, Sound, Read.

### Describe
Stage top: the **real sample** (about 120 rows of Seattle Public Library checkout records, Content) in the engine's table, read-only, scrolling inside its box, with a source line and the date pulled. Stage below: the **dictionary**, one card per column (nine). Each card:
- **Meaning**: pick one of three or four plain descriptions (one right, the others plausible: for Checkouts, "how many times this title was checked out that month" vs "how many copies the library owns" vs "how many people borrowed it ever").
- **Type**: whole number, decimal, text, year (4 digits), code from a list.
- **Required**: yes or no.
- **Allowed**: by type: a list of codes (chips, add or remove), a minimum and maximum, or a pattern from a short menu (for ISBN: "10 or 13 digits", "blank or 10 or 13 digits, several allowed with commas", "any text").
- **Example**: a value from the real sample, shown automatically.
Under the cards, **Link rules** (checkboxes with editable parts): "If MaterialType is EBOOK or AUDIOBOOK, UsageClass must be Digital"; "If MaterialType is BOOK or VIDEODISC, UsageClass must be Physical"; "PublicationYear is not after CheckoutYear"; "No two rows share Title + Creator + CheckoutYear + CheckoutMonth + MaterialType"; "ISBN-13 check digit must be valid". Each is off until ticked.
Every change runs the dictionary on the real sample at once; each card shows a strip "Real rows that break this rule: 0" or a count with the first three values ("PublicationYear: 23 rows, like 'c2015.', '[2019]'"). This is where the student learns the real catalog is messy and decides: tighten, loosen, or keep the rule and note it. A **Note** line on each card (pick from "Real data breaks this; clean before use", "Rule is strict on purpose", or none) carries that decision into Compare.
Panel: "Columns described: 6 of 9", and **Check a new batch** (enabled once every card has a Meaning and a Type).

### Check
Stage top: the **incoming batch**, 40 rows from the made-up Lakeside branch (Content), in the engine's table. Stage below: three method tabs, each run with one button:
- **Rules at entry**: the clerk types each row and the form refuses a value that breaks a single-row rule (type, required, allowed, range, pattern, link rules within the row). Rows refused are shown with the cell and the message, as the clerk would see it ("Checkouts must be a whole number"). Cost line: "Adds about 5 seconds per row for the clerk: 3 min 20 s for 40 rows."
- **Cleaning script**: runs overnight on the whole batch with the same rules plus the rules that need many rows (duplicates, and outliers by the 1.5 IQR rule on Checkouts). It can fix two kinds of problem by itself if allowed (switches): **Fix capital letters in codes** ("Book" to BOOK) and **Pull a year out of text** ("c2015." to 2015); fixed cells show the old and new value. Cost line: "Under 1 second to run, about 10 minutes for someone to read the flags."
- **Librarian review**: a librarian reads 10 rows chosen at random from the batch (fixed seed for the class: rows 2, 5, 9, 14, 19, 23, 27, 33, 36, 39; **New sample** draws another set) and flags what looks wrong, by knowledge, not rules. Each flag has the librarian's note ("Douglass is the author; the title and author are swapped"). Cost line: "About 2 minutes per row: 20 minutes for 10."
Each method's result: a list of flagged rows (row number, column, reason) and the batch table with those cells marked (icon plus tint).

### Compare
Stage: the **catch grid**: 14 problem rows (revealed now, with what each problem is) down the side, three methods across, each cell caught (check icon), fixed (wrench), or missed (empty circle). Below: a bar chart from the engine (catches per method and all three together) and a histogram of the batch's Checkouts with the outlier marked. A **Reference dictionary** drawer shows the librarian's sheet beside the student's, column by column, with differences highlighted. Panel: **Which would you run?** (pick one, two or all three; the panel shows the combined catches and combined time) and **Copy my dictionary** (plain text, one block per column, plus notes).

## Content
**Real sample.** Seattle Public Library, "Checkouts by Title" (data.seattle.gov, dataset tmmm-ytt6), public domain. Pulled by a builder script (`scripts/spl_checkouts.py`, written at build time) into `tools/catalog-column-rules/data/spl-sample.json` with the date pulled: CheckoutYear 2025, CheckoutMonth 4, 30 rows for each MaterialType BOOK, EBOOK, AUDIOBOOK and VIDEODISC, taken in the API's row order from a fixed offset so the pull repeats. Columns kept: UsageClass, MaterialType, CheckoutYear, CheckoutMonth, Checkouts, Title, Creator, ISBN, PublicationYear. Dropped: CheckoutType (vendor names), Subjects and Publisher (long text). The dataset counts checkouts per title per month; it has no column about who borrowed, and the panel says so ("Libraries keep counts, not borrowers").
Real values the builder must check and the spec relies on: PublicationYear is stored as text and includes forms like "c2015." and "[2019]"; ISBN is blank on many physical items and can hold several ISBNs separated by commas on digital ones. The build records the real counts for the reference dictionary in the data file; this spec does not promise them.

**Reference dictionary** (the librarian's sheet; the student never has to match it):
| Column | Meaning | Type | Required | Allowed |
|---|---|---|---|---|
| UsageClass | physical item or digital | code | yes | Physical, Digital |
| MaterialType | kind of item | code | yes | BOOK, EBOOK, AUDIOBOOK, VIDEODISC (plus others in the full catalog) |
| CheckoutYear | year of the checkouts | year | yes | 2005 to 2025 |
| CheckoutMonth | month of the checkouts | whole number | yes | 1 to 12 |
| Checkouts | times checked out that month | whole number | yes | 0 or more (the sheet says 0 to 10,000) |
| Title | title as cataloged | text | yes | any text |
| Creator | author or maker, "Last, First" | text | no | any text |
| ISBN | book number | text | no | blank, or 10 or 13 digits; several with commas |
| PublicationYear | year published | year | no | 4 digits, not after CheckoutYear (note: real data stores text like "c2015."; clean before use) |
Link rules: both MaterialType to UsageClass rules, PublicationYear not after CheckoutYear, no duplicate Title + Creator + CheckoutYear + CheckoutMonth + MaterialType. Check digit: on.

**Incoming batch** (made up, Lakeside branch, April 2025, public domain classics; every clean ISBN has a valid check digit). Columns: UsageClass, MaterialType, CheckoutYear, CheckoutMonth, Checkouts, Title, Creator, ISBN, PublicationYear.
1 Physical, BOOK, 2025, 4, 6, Pride and Prejudice, Austen, Jane, 9780141439518, 2003
2 Physical, BOOK, 2025, 4, 3, Frankenstein, Shelley, Mary, 9780486282114, 1994
3 Physical, BOOK, 2025, 4, **twelve**, Little Women, Alcott, Louisa May, 9780147514011, 2014
4 Digital, EBOOK, 2025, 4, 9, The Time Machine, Wells, H. G., 9781627930031, 2013
5 Physical, VIDEODISC, 2025, 4, 4, The General, Keaton, Buster, (blank), 2009
6 Digital, AUDIOBOOK, 2025, 4, 7, Treasure Island, Stevenson, Robert Louis, 9781400108237, 2008
7 Physical, BOOK, 2025, 4, **-2**, Moby-Dick, Melville, Herman, 9780142437247, 2003
8 Physical, BOOK, 2025, 4, 5, Dracula, Stoker, Bram, 9780486411095, 2000
9 Physical, **Book**, 2025, 4, 2, Jane Eyre, Bronte, Charlotte, 9780141441146, 2006
10 Digital, EBOOK, 2025, 4, 11, The Call of the Wild, London, Jack, 9781627931823, 2014
11 Physical, BOOK, 2025, 4, 1, Walden, Thoreau, Henry David, 9780486284958, 1995
12 Physical, **DVD**, 2025, 4, 3, Nosferatu, Murnau, F. W., (blank), 2007
13 Digital, AUDIOBOOK, 2025, 4, 8, The Secret Garden, Burnett, Frances Hodgson, 9781400100651, 2005
14 Physical, BOOK, 2025, 4, 4, Anne of Green Gables, Montgomery, L. M., 9780141321592, 2008
15 Physical, BOOK, 2025, 4, 2, **(blank title)**, Twain, Mark, 9780486280615, 1994
16 Digital, EBOOK, 2025, 4, 6, A Christmas Carol, Dickens, Charles, 9781627930116, 2013
17 Physical, BOOK, 2025, 4, 3, The Jungle Book, Kipling, Rudyard, 9780141325293, 2013
18 Physical, BOOK, 2025, **13**, 2, Heidi, Spyri, Johanna, 9780141322568, 2009
19 Digital, AUDIOBOOK, 2025, 4, 5, Alice's Adventures in Wonderland, Carroll, Lewis, 9781400110278, 2009
20 Physical, BOOK, 2025, 4, 7, The Wonderful Wizard of Oz, Baum, L. Frank, 9780486291161, 1996
21 Physical, BOOK, 2025, 4, 1, Emma, Austen, Jane, 9780141439587, **2031**
22 Digital, EBOOK, 2025, 4, 4, Peter Pan, Barrie, J. M., 9781627931038, 2014
23 **Physical, EBOOK**, 2025, 4, 3, Black Beauty, Sewell, Anna, 9781627930543, 2013
24 Physical, BOOK, 2025, 4, 2, The Odyssey, Homer, 9780140268867, 1997
25 Physical, VIDEODISC, 2025, 4, 5, The Kid, Chaplin, Charlie, (blank), 2016
26 Physical, BOOK, 2025, 4, 3, Great Expectations, Dickens, Charles, **978014143956**, 2002
27 Digital, EBOOK, 2025, 4, 10, Sherlock Holmes Stories, Doyle, Arthur Conan, 9781627932486, 2015
28 Physical, BOOK, 2025, 4, 2, The Scarlet Letter, Hawthorne, Nathaniel, 9780142437261, 2003
29 Physical, BOOK, 2025, 4, 6, Robinson Crusoe, Defoe, Daniel, 9780141439822, 2003
30 **(same as row 29)**
31 Digital, AUDIOBOOK, 2025, 4, 4, Around the World in Eighty Days, Verne, Jules, 9781400113460, 2009
32 Physical, BOOK, 2025, 4, 3, Grimm's Fairy Tales, Grimm, Jacob, 9780486282749, 1993
33 Physical, BOOK, 2025, 4, 2, **Douglass, Frederick**, **Narrative of the Life of Frederick Douglass**, 9780486284996, 1995
34 Digital, EBOOK, 2025, 4, 5, The Adventures of Tom Sawyer, Twain, Mark, 9781627930185, 2013
35 Physical, BOOK, 2025, 4, 1, Uncle Tom's Cabin, Stowe, Harriet Beecher, 9780486440286, 2005
36 Physical, BOOK, 2025, 4, **400**, The Boston Cooking-School Cook Book, Farmer, Fannie Merritt, 9780486283234, 1997
37 Physical, BOOK, 2025, 4, 2, The Count of Monte Cristo, Dumas, Alexandre, 9780140449266, 2003
38 Physical, BOOK, **24**, 4, 4, Les Miserables, Hugo, Victor, 9780451419439, 2013
39 Digital, AUDIOBOOK, 2025, 4, 6, Kidnapped, Stevenson, Robert Louis, 9781400101771, 2006
40 Physical, BOOK, 2025, 4, 3, The Hound of the Baskervilles, Doyle, Arthur Conan, 9780141034324, **c2015.**
(Bold marks the problem for this spec only; on screen nothing is marked until Compare.)

The 14 problems: 3 text in a number column; 7 negative count; 9 code in the wrong case; 12 code not in the list; 15 required value blank; 18 month out of range; 21 published after it was checked out; 23 ebook marked Physical; 26 ISBN 12 digits; 30 duplicate row; 33 title and author swapped; 36 a count far above the rest (Checkouts quartiles 2 and 6, upper fence 12, the only outlier); 38 two-digit year; 40 year stored as text.

Reference results (checked with the reference dictionary):
- Rules at entry: 11 caught (3, 7, 9, 12, 15, 18, 21, 23, 26, 38, 40); missed 30, 33, 36.
- Cleaning script: 13 (the 11 plus 30 and the outlier flag on 36), with fixes allowed: 9 and 40 fixed, not just flagged; missed 33.
- Librarian review of rows 2, 5, 9, 14, 19, 23, 27, 33, 36, 39: 4 caught (9, 23, 33, 36).
- All three together: 14 of 14. Entry plus script: 13. Script plus librarian: 14.

## Interactions in detail
- The three checks run the student's dictionary, not the reference: a student who left Checkouts as "text" sees "twelve" pass, and Compare shows the reason in the cell ("Your dictionary: Checkouts is text").
- Librarian review never depends on the dictionary; it is fixed knowledge for the fixed sample and for any New sample (each of the 14 rows has a librarian note if it is in a sample; problems 3, 7, 12, 15, 18, 21, 26, 30, 38, 40 are also noticed by the librarian when sampled, so a lucky sample can do better).
- Fix switches in the script change values only in the script's copy; the batch table shows both values.
- Compare's combined line counts a problem once, whichever method caught it, and adds the times.
- Engine: checks call `t.validate(dictionary)` (Family engine), which returns every violation with row, column and rule; Rules at entry filters to single-row rules.
- Save on this device: the dictionary and notes stay in localStorage; **Clear saved** removes them. No student data.
- Keyboard: modes, cards (Tab), chips and fields inside a card, tables (engine's keyboard table), method tabs, grid cells. Every marked cell is announced with its reason.
- Sizes: at 1366x768 and 1280x720 Describe shows the sample table (8 rows visible) above two rows of cards with the panel; Check shows the batch and one method's results; at 760 wide cards stack; at 680x425 one card at a time with Previous and Next. Table text at least 13 px, cards 14 px.

## Look
- Own light palette over `kit:theme-912` (a card catalog drawer): paper `#f6efe0`, cards `#fffdf7`, ink `#2a2118`, muted `#5f5446`, accent `--brand #5b3a8c` (catalog purple: Check buttons, chip outlines, the header rule) with white text on it, error red `#a3261b` with an X icon, caught green `#1d6b3a` with a check icon, highlight for marked cells `#fff3c4`.
- Contrast (computed): brand on paper 7.55:1, on cards 8.50:1; white on brand 8.65:1; ink on paper 13.8:1; muted on paper 6.45:1; error red on paper 7.24:1; caught green on paper 6.42:1. All pass AA.
- Engine charts use `--dd-1` to `--dd-6` with shapes, set for the light background.
- Neighbors: the dark 9-12 CS tools (pinks, violet, lemon, sky blue, orange) and data-policy-council's light navy page; group siblings: pull-request-review wine on grey-white, sprint-board blue on whiteboard, cloud-through-time teal on parchment. Purple on manila differs from each.

## Art
None. Cards, table and a small drawn card-catalog drawer in the header are code.

## Voice
Bank voice `curious-librarian` (Aoede), style "Say curiously and warmly, like a friendly school librarian": the branch's catalog librarian who asked you to write the sheet. Not used by a 9-12 CS tool or a group sibling. Light narration:
1. how, welcome (Describe): "Pick a column card. Say what it means and what values belong in it."
2. event, first time a rule turns up real rows that break it: "The real catalog breaks your rule. Tighten it, loosen it, or add a note."
3. how, welcome (Check): "Run each check. Watch what it catches and what slips by."
4. event, first time all three checks have run: "Now open Compare. No single check caught everything."
5. event, a combined pick in Compare reaches 14 of 14 (once): "All fourteen. Now look at what that costs in time."
Read speaks the hint. Rows, values and reasons are on screen only.

## Family engine
data-desk (`kit/data-desk.js`): DataTable for the sample and the batch, `renderTable` (read-only), `t.stats('Checkouts')` for the outlier rule, Chart bar (catches per method) and histogram (Checkouts with the outlier highlighted).
New engine feature, added to the engine and to `docs/families/data-desk.md` in the same change, existing calls unchanged:
```js
t.validate({
  columns: {Checkouts: {type: 'int', required: true, min: 0, max: 10000}, MaterialType: {type: 'code', values: [...]},
            ISBN: {type: 'text', pattern: 'isbn', checkDigit: true}, ...},
  links: [{if: {col: 'MaterialType', in: ['EBOOK', 'AUDIOBOOK']}, then: {col: 'UsageClass', is: 'Digital'}},
          {col: 'PublicationYear', notAfter: 'CheckoutYear'}],
  unique: [['Title', 'Creator', 'CheckoutYear', 'CheckoutMonth', 'MaterialType']],
  outliers: ['Checkouts'],
}) -> [{row, col, rule, message}]
```
Types: int, number, text, year, code. Patterns: isbn (10 or 13 digits, comma list allowed by a flag). Outliers use the engine's 1.5 IQR rule. Other siblings (simulation-studio, lunch-survey-cleanup) can call it later.
Dataset: Seattle Public Library checkouts, used by no other sibling.

## Sources
- CSTA 2026 PK-12 Computer Science Standards: https://csteachers.org/2026-csta-pk-12-computer-science-standards/ ; CSTA 2017: https://csteachers.org/k12standards/
- Seattle Public Library, "Checkouts by Title", City of Seattle Open Data, dataset tmmm-ytt6: https://data.seattle.gov/Community-and-Culture/Checkouts-by-Title/tmmm-ytt6 (public domain; date pulled recorded in the data file).
- ISBN-13 check digit rule: International ISBN Agency, ISBN Users' Manual: https://www.isbn-international.org/content/isbn-users-manual
- Outlier rule, 1.5 times the interquartile range: NIST/SEMATECH e-Handbook of Statistical Methods, 7.1.6 "What are outliers in the data?": https://www.itl.nist.gov/div898/handbook/prc/section1/prc16.htm
- Data dictionaries: USGS, "Data Dictionaries" (Data Management): https://www.usgs.gov/data-management/data-dictionaries
- The Lakeside branch batch is made up; its titles are public domain classics.

## Done when
1. Describe shows the real sample with source and date pulled, and nine cards; each change recounts "real rows that break this rule" at once.
2. Setting PublicationYear to "year, 4 digits" shows real breaking rows with their values (like "c2015.").
3. With the reference dictionary: Rules at entry flags exactly rows 3, 7, 9, 12, 15, 18, 21, 23, 26, 38, 40; the script adds 30 and 36; with fixes on, rows 9 and 40 show old and new values.
4. Librarian review of the fixed sample flags 9, 23, 33, 36 with notes; New sample draws ten other rows.
5. With Checkouts set to "text", Rules at entry does not flag row 3, and Compare says why.
6. Compare's grid shows all 14 problems; picking all three methods reads 14 of 14 with the summed time.
7. `t.validate` is in the engine and in `data-desk.md`, and the other siblings' calls still work.
8. Fits at 1366x768; every marked cell has an icon and a spoken reason.

## Open questions
- [catalog-column-rules] Adds `t.validate` to the shared data-desk engine (and its family doc). OK to grow the engine in this tool's build?
- [catalog-column-rules] The real sample is pulled from Seattle's open data at build time; the counts of real rows breaking each rule will only be known then. OK that the spec does not fix those numbers?
