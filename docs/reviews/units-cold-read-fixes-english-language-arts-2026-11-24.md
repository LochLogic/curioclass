# Fixes: ELA units cold read, 2026-11-24

Fix pass on docs/reviews/units-cold-read-english-language-arts-2026-11-24.md. Scope: ELA courses K, 1 to 5 and 7 to 12,
data/plans/ela-texts.csv and the ELA ledger. Written days (K to 3) were not edited; changes they need are rows in
data/plans/defects.csv (found_by "cold-read fix 2026-11-24"). Grade 6 was not opened.

## Findings and what was done

1. **ELA ledger had no unit-level rows.** Fixed. Seeded 3,081 planned rows with `ledger.py seed`: 345 skill (from each
   plan's "Progression skills owned" line), 2,036 term (progression words, first unit that owns them), 148 model (frame
   models "introduced or first used here"), 552 text (one per ela-texts.csv row). `ledger.py check ela --all` exit 0;
   the remaining citation notes (planned-only, unmatched) are pre-existing K to 3 section rows.
2. **K to 3 exits on invented cards marked needs_text yes.** Fixed in the records, logged for the days. Root cause:
   each ELA DEFAULTS.md carried a math-style exit line ("a new case"). The exit line in DEFAULTS.md for K, 1 to 5 and
   7 to 12 now asks for a transfer on the day's text (a reserved passage or an unread part of the unit's texts, never a
   card invented for the exit) and says an item on an invented card has needs_text no. In items.csv, grade 2 had 207
   exits and grade 3 had 209 items (176 exits, 33 practice) set to needs_text no where text_ref said the content is not
   in the text. Defects rows log both for the day pages. This makes grades 2 and 3 fail plan.py's 80 percent text gate
   (48 and 52 percent): honest counting until the days are fixed.
3. **Twain clash (grade 11 day 33 and grade 12 unit 1).** Fixed. Grade 12 keeps Life on the Mississippi chapter 9.
   Grade 11 day 33's cold text is now John Muir, "A Wind-Storm in the Forests" (The Mountains of California, 1894,
   chapter 10; public domain). Its four item rows were rewritten around the new text; the three assessed words are to be
   named at section 2.4 from the checked text. The source page could not be fetched this pass (Gutenberg 503), so the
   ela-texts row says source still to check.
4. **Texts repeated across grades (Gettysburg, Second Inaugural).** The read said no other text repeats; that was
   wrong. Grade 9 day 93 assesses the closing lines cold, so grade 11 exit 45 moved to the second paragraph ("Both
   parties deprecated war...") and grade 12 exit 108 and T3 moved to other sentences. Grade 9 frame Seams notes the reuse.
5. **Stale generated lines and day kinds.** Fixed. Regenerated the days.csv-derived lines (header, day list, owned codes,
   writing types, earlier-grade rows) from fresh skeletons in g4 s04, g5 s03, g7 s02 to s04, g8 s03 to s05, g9 s04,
   g10 s01 and s07, g12 s01 and s02; removed stale earlier-grade lines in g7 s02 and s04, g8 s03, g10 s05 and s07,
   g11 s03, g12 s01. Earlier-grade tags with no reason were removed (g7 days 31, 87; g8 day 66; g10 days 95, 150;
   g11 day 43; g12 day 3). Days whose goal is understanding relabeled (g5 119, g7 76, g8 98 and 148, g10 5).
6. **Grade 4 anchor measures above the band.** Fixed. Unit targets lowered (u2 740 to 870, u3 770 to 900, u4 800 to 930)
   in ela-texts, frame, s02 to s04 and scope-and-sequence.
7. **Grade 5 had no receiver for the grade 4 portfolio (day 160).** Fixed in g5 s01.
8. **Grade 2 source-map harms_learning held prose.** Fixed: 313 values set to yes, no or unclear, prose moved to why.
9. **K to 3 items that need written days changed.** Logged (see Defects).
10. **Grade 11 day 1 retrieval of e10-ri-evidence-central-idea.** Kept on day 3 by judgment: day 1 is RL, RI starts day 3.

## Cory's calls applied

1. Grade 1 L.1.5/L.1.6 return with two spaced touches in units 3 and 4; sentence conventions continue after unit 2.
   Frame rows 3 and 4 updated; days are written, so a defects row carries it.
2. Grade 2 text 04 is now "The Old Man Who Made Withered Trees to Flower" (Japan), retold from Yei Theodora Ozaki's
   public-domain edition (1903/1908); sensitivity read is a todo on the ela-texts row. Frame and s04 updated; the six
   written days that use it are a defects row.
3. Grade 4 keeps 30/35/35; day 155 is now a short narrative scene in place of an informative drafting day (s04 minutes,
   exit and Goal map rows, source-map L14 cut). Its partner talk stays so grade 5's last-use table holds.
4. Grade 7 novella audio is made at the Art and voice step (s01, ela-texts).
5. Grade 7 keeps real Klamath River places with an invented family and town; sensitivity read before the novella is
   written (s01, ela-texts todo).
6. Grade 9 choice book may go home; anchors stay in class (scope-and-sequence).
7. Grade 11 Occom is now the 1772 Moses Paul sermon: page 13 excerpt on day 43 (fits; day 48's log may cite it), pages
   16 to 17 and the page 17 exit kept for day 109 (s03, s06, frame, scope-and-sequence, days.csv, ela-texts).
8. Grade 12 keeps the 1921 film; audio and live staging are the other two versions; the new-film plan is removed
   (s02, days.csv day 24, scope-and-sequence).

## Defects logged (7 rows)

g1 L.1.5/L.1.6 spacing; g1 e1-revise-publish Understanding day; g1 day 21 tag; g2 folktale swap (days 124, 125, 129,
131, 153, 155); g2 207 invented-card exits; g3 209 invented-card items; g3 day 98 kind.

## For Cory

- **80 percent text gate for K and grade 1 foundational items.** Options: (a) exempt decoding and phonics items from
  the count, (b) count them like any item. Pick (a): decoding work is on decodable text, not the unit's texts.
- For the lead: scripts/defaults.py line 96 still emits the math exit line for ELA; regenerating DEFAULTS.md would undo
  the fix until the script changes. UNIT-PLAN.md could state the invented-card needs_text rule.
- Checks still owed: the Muir source page and the Ozaki edition details (both from memory); the g4 day 155 dialogue is
  marked invented.

## Gates

- `unitplan.py check ela`: no FAIL (one pre-existing note on g7 s06).
- `sequence.py check` for all 12 touched courses: 0 failures each.
- `goalmap.py audit`: exit 0 for all 12 courses.
- `ledger.py check ela --all`: exit 0.
- Not a named gate: plan.py still fails stage 5 in K, 1, 2, 3 and 11 for pre-existing reasons; grades 2 and 3 now also
  fail the 80 percent text gate (see finding 2).
