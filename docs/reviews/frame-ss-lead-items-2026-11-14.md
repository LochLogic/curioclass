# Social studies frame reads: the lead's items, 2026-11-14

The "For the lead" lists in the five social studies frame fix reports (K to 2, 3 to 5, 6 to 8, 9 to 11, 12), worked
by the lead's helper. Items the lead had already done were spot-checked and left alone.

## 1. Standards paraphrases (data/standards/ma-hss-2018.txt)

Each checked against the official framework PDF (on disk, reference only); our own words kept, the framework's
sentences not copied. Header note dated 2026-11-14 lists the codes.

| Code | Done | PDF page |
|---|---|---|
| MA.7.T4b.3: 3a and 3b became five parts, 3a to 3e (polis, citizen participation and voting rights, law-making bodies, writing a constitution, rule of law) | Done | 101 |
| MA.7.T1b.2d: Ashoka's missionaries, the Gupta Empire's Sanskrit literature and art | Done | 97 |
| MA.8.T3.2: committees, hearings and votes; the executive branch's Cabinet, departments, agencies and armed services | Done | 106 to 107 |
| MA.8.T3.4: terms of office and the limit on presidential terms | Done; the Electoral College, also in the PDF, was not added (not asked; a row change is the frame writers' call) | 107 |
| MA.USII.T1.2: adds equity | Done | 130 |
| MA.GOV.T1.6: adds constitutionalism and republicanism | Done | 163 |
| MA.WHI.T3.9: repeated outbreaks into the 15th century | Done | 144 |
| MA.WHII.T3.2c and 3.2d | Done, with one change: the reader's 3.2c spoke of "European imperialism"; the PDF names the Spanish and Portuguese empires in the Americas (missionary conversion, language, imposed government), so 3.2c says that | 152 |
| MA.WHII.T5.5: Asia, Africa, the Middle East, Central and South America; decolonization after 1950 | Done | 157 to 158 |
| MA.WHII.T6.2: youth population, Kurdish autonomy, Gulf states; "such as" became "including", as the PDF has it | Done | 160 |

None rejected. The progression CSV was not changed: ss7-athenian-democracy owns the parent MA.7.T4b.3, which carries
its lettered parts (the same convention as MA.7.T4b.7); wh2-imperialism-causes likewise owns MA.WHII.T3.2. The grade 7
frame (world-geography-and-ancient-civilizations-ii) now says "61 codes" and "MA.7.T4b.3 carries 3a to 3e (unit 8...)",
and unit 8's row says "7.T4b.3a to 3e". The file header's literacy note (it said the ELA file covers the literacy
standards) was corrected to match STANDARD.md.

## 2. Stale notes

- docs/ROADMAP.md, "Subjects outside the core": superseded line added. Done.
- docs/PRODUCTION-PATH.md, the ELA and math paragraph's last sentence: the 9 to 11 wording. Done.
- docs/APPROACH.md introduction: already says APPROACH-MATH and APPROACH-ELA exist and science and social studies
  pages are still to be written; true, left as is.
- docs/ADOPTION-BAR-SUBJECTS.md: "Decided" wording; social studies row "confirm the C3 edition" replaced by the
  edition line; the standards paragraph's literacy parenthesis corrected. Done.
- progression-social-studies-codex: finding 6 update line, and the limits bullet's resolved note. Done.
- progression-social-studies-fixes, Codex 6: within-year note added. Done.
- social-studies-open-material (the source-scouting report): settled note on the partial bases; open items for Oak,
  US Courts, c3teachers and the Library of Congress, LibreTexts and Louisiana closed with the addendum's results.
  Science-second lines: the grade 12 report's wording applied ("governed by PRODUCTION-PATH, social studies first").
  **Not applied:** the 9 to 11 report's wording that "availability of a complete base text no longer determines that
  order". PRODUCTION-PATH (P2, and step 5) still puts science second because no whole-course base text was found, so
  that sentence would be false.
- frame-world-geography-and-ancient-civilizations-ii and frame-us-history-ii reviews: "Since written" lines. Done.
- data/plans/flow-status.csv rows for the six high school frames: already updated by the lead.

## 3. Source list

docs/APPROACH-SOURCES.md, new section "Social studies frame reads, 2026-11-13": the framework and C3 PDF routes, grade 3
and 5 sources, the five nations' pages, Investigating History routes, Oak's /programmes/ route, the democracy roadmap,
Since Time Immemorial routes, Tennessee and New York (working and failed), the college-level frameworks, the economics
and personal finance standards, the insurance activity, Civic Online Reasoning, Yick Wo, the 1924 Act and the Mussolini
entry, each with how far it was read. Done.

## Gates

`stale.py check`, `progression.py check social-studies` and `frame.py check world-geography-and-ancient-civilizations-ii`:
0 failures each.
