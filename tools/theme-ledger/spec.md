# Theme Ledger

## One idea
Keep a story's two themes like a bookkeeper keeps two accounts: every entry is an exact quoted line, a weight and what it shows, the ledger's chart then shows where in the story each theme rises and where the two cross, and the strongest entries become the evidence in a paragraph you draft.

## Not like
- idea-threads (ela 9-12, literature group, not built): pulls threads through a speech or essay to show where two central ideas twist together. Here the texts are short stories (RL, not RI), entries are weighted and filtered like data, the chart measures rise and crossing by paragraph, and the end product is a drafted paragraph.
- theme-evidence-ladder (ela 6-8, evidence family, not built): ranks given passages for one theme against a rival theme. Here the student finds every passage, keeps two themes at once and reads their shape across the whole story.
- argument-builder-pro (ela 9, evidence family): builds an argument outline from an evidence pack. Here the claim is about literature and comes last, out of the ledger.
- tension-meter (ela 9, literature group, not built): graphs suspense across a plot. Here the graph is of themes, built only from the student's quoted entries.
- source-mixer (ela 11, data, research group): mixes sources at a desk. Here there is one story and the ledger book is the instrument.
- claim-quote-comment (ela 6-8, evidence family, not built): one analysis paragraph about an article. This tool's Draft step uses the same checks, but only after a whole story's ledger is kept.

## Who and how
- Grades 9 to 12 ELA. Module: Developing Themes with Evidence (Reading Literature).
- Driver: students on laptops, alone or in pairs. 35 to 50 minutes for one story (reading and logging 20 to 30, chart 5 to 10, draft 10 to 15); the second story suits another day.
- Standards: RL.9-10.1 and RL.11-12.1 (cite strong and thorough textual evidence; at 11-12, including where the text leaves matters uncertain): Ledger entries with weights and the "says or suggests" tag. RL.9-10.2 (a theme's development over the text, shaped by details) and RL.11-12.2 (two or more themes, how they interact and build on one another): Chart's rise lines, crossings and "Both" entries. W.9-10.9 and W.11-12.9 (draw evidence from literary texts to support analysis): Draft.
- Grade setting in the panel: **9-10** or **11-12**. At 11-12 the ledger adds the "Leaves it open" weight tag and Draft asks for how the two themes build on each other.
- tool.json: driver "students", minutes "35-50", modes ["Ledger", "Chart", "Draft"], grades_label "Grades 9-12". Kit starter plus `kit:evidence`.

## Screens and modes
Header: title "Theme Ledger", small line "Two themes, every entry quoted."; story picker **The Gift of the Magi** / **The Story of an Hour**, each with a small painted picture (art: story-magi, story-hour) that also heads its About this story card; mode buttons **Ledger** (opens first), **Chart**, **Draft**; Motion, Sound, Read.

### Ledger (opens first)
- Focus: the story text and the open ledger book side by side, the story the wider of the two, with the lit span and the Log it bar between them.
- Left: the story, with paragraph numbers in the margin (M1 to M45, H1 to H23). Right: the open ledger book, its pages a painted aged-paper texture (art: ledger-paper) with the columns and rules drawn in code over it. Its two columns carry the story's two theme topics (Content), each with its glyph: Theme A ◆, Theme B ●. Under each topic, a line "Your theme statement (write it when you're ready)" stays editable all session.
- Making an entry: tap the first word of a passage, then the last (or select with the keyboard: Shift and arrows). The span lights. The **Log it** bar appears with: column **A**, **B** or **Both**; weight **Faint**, **Clear**, **Strong** (1, 2, 3 marks on the ledger's tally edge); at 11-12 a tag **Says it** / **Suggests it** / **Leaves it open**; and **What it shows** (a text box). **Enter in ledger** writes the row.
- A ledger row: paragraph number, the quote (exact, with "..." only where the student skipped words inside one paragraph using **Trim**), weight marks, tag, and the comment. Rows sit in story order. **Edit** and **Strike** (struck rows stay visible with a line through, as in a real ledger, until **Remove struck rows**).
- The evidence checker writes small margin notes on a row when it applies (engine rules): "Just repeats the quote: say what it shows", "Explain it: a few more words", "Long quote: which words matter most? Try Trim". Notes never block an entry.
- Footer totals: entries per column, Both entries, and "Covered: 9 of 45 paragraphs".

### Chart
- Focus: the two theme lines, the biggest thing on the stage; filters and readouts sit beside and below.
- Stage: a line chart across the story, x = paragraph number (labelled Beginning, Middle, End along the axis too), y = the summed weight of entries in a window centered on each paragraph (three paragraphs: the one before, it and the one after). Theme A is a solid line with ◆ markers, Theme B a dashed line with ● markers. Every crossing is marked ✕ with its paragraph ("cross at H15"). Both entries show as small rings on both lines.
- Filters (panel): **Show** A, B, both; **Weight** at least Faint / Clear / Strong; **Tag** (11-12) Says, Suggests, Leaves open; **Part** Beginning, Middle, End, Whole.
- **One reading** toggle draws the tool's key (Content) as thin grey lines behind the student's, with the caption "One reader's ledger. Yours can differ."
- Readouts, shown here as they read with the key's own entries for Magi (window 3): "Theme A peaks at M44 to M45", "Theme B peaks at M2, M33 and M34", "Crossings: 5", "Longest quiet stretch for Theme A: M1 to M4". A peak names every paragraph at the top value, up to three, else the first and "and n more". Tapping a point lists the entries behind it, each with **Go to text**.
- **Notice** box (private): "Where do the two themes meet, and what happens to each after?"

### Draft
- Focus: the three evidence slots with their quotes, in the middle of the stage; the Claim box above them.
- The paragraph frame, top to bottom: **Claim** (pre-filled with the student's theme statement for the chosen column, or both at 11-12), then three evidence slots filled from the ledger's strongest entries (highest weight, then spread across the story; the student can swap any slot for any row with **Swap**), each with **Lead-in** (who says it or when it happens), the quote (read only), and **Analysis** (how it supports the claim). At 11-12 a fourth box: **How the themes build on each other**.
- **Check my paragraph** runs the engine rules on each slot: lead-in missing ("Drop-in quote: say where it comes from"), analysis missing or only repeating ("Explain it"), claim is only a topic ("A theme is a statement: what does the story say about it?"). Each note links to its box.
- **Assemble** shows the paragraph as one block of text. **Copy paragraph**. **Clear draft**. Everything stays on this device.

## Content
Exact texts from the named editions (Sources). Source em dashes are shown as "--". Paragraph ids are fixed; spans are word ranges inside one paragraph.

### The Gift of the Magi (O. Henry), 45 paragraphs, M1 to M45
- Theme topics: A "Sacrifice in love" (◆): what each one gives up for the other. B "What things are worth" (●): price set against value.
- The tool's reading (key): weight 1 to 3 per paragraph per theme, with its key quote.
  - M1 B3 "One dollar and eighty-seven cents. That was all."
  - M2 B1 "life is made up of sobs, sniffles, and smiles, with sniffles predominating"
  - M3 B1 "A furnished flat at $8 per week."
  - M5 B1 "Now, when the income was shrunk to $20"
  - M6 A1, B2 "Something fine and rare and sterling--something just a little bit near to being worthy of the honor of being owned by Jim."
  - M9 A2, B2 "two possessions of the James Dillingham Youngs in which they both took a mighty pride"
  - M10 A2 "Once she faltered for a minute and stood still while a tear or two splashed on the worn red carpet."
  - M11 A1 "with the brilliant sparkle still in her eyes, she fluttered out the door"
  - M16 B2 "Twenty dollars"
  - M17 A2 "Give it to me quick"
  - M19 B3 "properly proclaiming its value by substance alone and not by meretricious ornamentation--as all good things should do"
  - M22 A1, B1 "what could I do with a dollar and eighty-seven cents?"
  - M24 A1 "Please God, make him think I am still pretty."
  - M28 A3 "I couldn't have lived through Christmas without giving you a present."
  - M30 A1 "I'm me without my hair, ain't I?"
  - M33 A3, B2 "Maybe the hairs of my head were numbered... but nobody could ever count my love for you."
  - M34 B3 "Eight dollars a week or a million a year--what is the difference?"
  - M36 A2 "I don't think there's anything in the way of a haircut or a shave or a shampoo that could make me like my girl any less."
  - M38 A1, B2 "They were expensive combs, she knew"
  - M39 A2 "My hair grows so fast, Jim!"
  - M44 A3, B1 "I sold the watch to get the money to buy your combs."
  - M45 A3, B3 "of all who give gifts these two were the wisest"
  - With the key (window 3): Theme B leads M1 to M7; the lines cross 5 times (at M9, M15, M23, M33 and M36); Theme A peaks at 6 in M44 to M45, Theme B at 5 in M2, M33 and M34; Theme B is quiet (0) from M24 to M31, its longest gap.

### The Story of an Hour (Kate Chopin), 23 paragraphs, H1 to H23
- Theme topics: A "Freedom and selfhood" (◆). B "Love and marriage" (●).
- Key:
  - H1 B1 "the news of her husband's death"
  - H3 B2 "She wept at once, with sudden, wild abandonment"
  - H5 A1 "the tops of trees that were all aquiver with the new spring life"
  - H8 A1 "whose lines bespoke repression and even a certain strength"
  - H9 A2 "There was something coming to her and she was waiting for it, fearfully."
  - H10 A1 "striving to beat it back with her will"
  - H11 A3 "free, free, free!"
  - H13 A2, B2 "the face that had never looked save with love upon her" / "a long procession of years to come that would belong to her absolutely"
  - H14 A3, B3 "There would be no one to live for her during those coming years; she would live for herself."
  - H15 A3, B3 "And yet she had loved him--sometimes. Often she had not."
  - H16 A3 "Free! Body and soul free!"
  - H18 A2 "she was drinking in a very elixir of life through that open window"
  - H19 A3 "She breathed a quick prayer that life might be long."
  - H20 A2 "she carried herself unwittingly like a goddess of Victory"
  - H21 B2 "It was Brently Mallard who entered"
  - H23 A2, B2 "she had died of heart disease--of joy that kills" (at 11-12 the key tags this "Leaves it open": whose joy, and what killed her, the story does not say)
  - Key reading (window 3): Theme B leads H1 to H4; Theme A overtakes at H5 and climbs from H9; the lines tie at H13 and H14, where love is weighed against selfhood, and Theme A peaks at 9 in H15 (Theme B at 8 in H14); Theme A carries H15 to H20; Theme B leads again at H22 and they tie at H23. Crossings: 2 (at H5 and H22).

### Context cards (one per story, from **About this story**)
- Magi: "First printed in a New York newspaper in 1905 and collected in The Four Million (1906). Della and Jim live on $20 a week. The magi are the wise men who, in the Bible story, brought gifts to the infant Jesus."
- Hour: "Published in Vogue on December 6, 1894, as 'The Dream of an Hour'. In the 1890s a married woman in most states had limited control over her property and wages, and divorce was hard to get. Chopin never says whether Brently was cruel; the story says 'A kind intention or a cruel intention made the act seem no less a crime.'"
- Students write their own theme statements; the tool never offers one.

## Interactions in detail
- A span stays inside one paragraph. **Trim** lets the student drop words from the middle of a span, shown as "..."; at least 3 words must remain. A span over 40 words gets the "Long quote" note.
- The same words can sit in two rows (one per column) or one Both row; the chart counts a Both row on both lines.
- Weight changes or struck rows update the chart at once. A story with fewer than 3 entries shows the chart axes with "Log at least 3 entries to see a line."
- The window is 3 paragraphs for Magi and 3 for Hour; a slider at 11-12 sets 1, 3 or 5 ("Smooth"), always centered, cut off at the story's first and last paragraph. Crossings are counted where the leading line changes; a tie (equal values) is not a crossing, and the crossing is placed at the first paragraph where the other line leads.
- A tap while the chart redraws after a filter change (300 ms) acts at once on the new chart.
- Draft's strongest-three pick: sort by weight, then prefer rows at least 5 paragraphs apart; ties go to story order.
- Storage per story in localStorage `theme-ledger:v1` (try/catch): rows, theme statements, notes, draft. **Clear this story** asks first. Nothing leaves the page.
- Sizes: at 760 wide and below the story and ledger become two tabs (**Story**, **Ledger**) with the Log it bar pinned to the bottom; at 375 the chart's filters fold into a **Filters** drawer. No horizontal scroll at any listed size; at 680x425 the Log it bar and the current paragraph are visible together.

## Look
- Paintings in warm sepia and muted ochre, like old bookkeeping, kept clear of the wine accent. Own light `:root`, an accounting ledger: `--paper #f7f3e8` with faint green column rules, `--panel #fffdf6`, `--ink #22191c`, `--muted #5e5357`, `--line #d8cfbd`, accent `--brand #592439` (ledger wine: header rule, ruled double line under totals, Enter in ledger, active mode), `--btn #592439`, `--btn-line #a38f8f`, `--head-ink #ffffff`, `--focus #0b6e75`. Theme A ink `#1d4f91` (◆, solid line), Theme B ink `#8a4b00` (●, dashed line); glyphs and dash patterns carry the difference. Weights are tally marks, not colors.
- Neighbors: research-notebook fountain-pen blue, satire-decoder oxblood (dark; this is a light page and a wine closer to purple, dE well over 20 from any catalog accent, nearest two-trains at 24.3), usage-panel ink red (dark), fallacy-field-guide olive, founding-words-explorer rust.
- Contrast (WCAG 2.1): white on brand 12.10:1; brand on paper 10.91:1, on panel 11.88:1; ink on paper 15.48:1; muted on paper 6.64:1, on panel 7.24:1; focus on paper 5.41:1; Theme A on paper 7.34:1; Theme B on paper 6.14:1. All pass AA.

## Art
Local FLUX (`scripts/localart.py`), one warm sepia still-life style, asked in one session. No people. The ledger's columns, rules, rows and tally marks stay in code because they hold the student's entries.
- ledger-paper: "A full-frame close view of aged cream ledger paper, soft fibers and faint foxing, evenly lit, plain, warm sepia still life"; 4:3; cutout no; people no; full-frame texture clipped to the ledger book's pages, with rules drawn over it.
- story-magi: "A pair of tortoiseshell hair combs with jeweled rims and a platinum pocket-watch fob chain lying on a worn wooden table by a window, warm sepia still life"; 4:3; cutout no; people no; the Magi picker button and its About this story card.
- story-hour: "An open window seen from inside a quiet room, white curtains moving, the tops of spring trees with new leaves and patches of blue sky between clouds, warm sepia still life"; 4:3; cutout no; people no; the Hour picker button and its About this story card.
3 images, none with people. Drawn in code: the ledger's columns, rules and tally marks, the chart, markers, crossings and every label.

## Voice
Bank voice `smooth-narrator` (Algieba), style "Say smoothly and warmly, like an audiobook narrator who keeps careful books." Not used by any neighbor or another tool in this batch. `Curio.voice`, `scope: () => state.mode + state.story`. The story itself is never read by the voice; Read speaks the hint. Event line ids: checked.
- w-ledger (how, welcome on Ledger; stale when a word is tapped): "Tap the first word of a line that shows a theme, then tap the last."
- logit (how, the first span; stale when Enter in ledger is tapped): "Tap a column and a weight, type what it shows, then tap Enter in ledger."
- statement (how, after the fifth entry; stale when a theme statement is typed): "When you're ready, write each theme as a sentence at the top of its column."
- w-chart (how, welcome on Chart; stale when a filter or point is tapped): "Each line is one theme. Look for the crossing marks, then tap a point to see its entries."
- reading (how, first One reading; stale when it is turned off): "That grey line is one reader's ledger. Yours can differ."
- w-draft (how, welcome on Draft; stale when a box is typed in): "Your strongest entries are in place. Type a lead-in and say how each one supports your claim."
- checked (event, Check my paragraph; stale on any edit): "{n} notes to look at." or "No notes. Read it aloud once."
- With fewer than 3 entries, Chart's hint reads "Log at least 3 entries in Ledger to see a line." and w-chart waits until there are 3.

## Family engine
`kit/evidence.js` (the evidence family). No family doc exists; this spec holds the full description, written so the lower grades can reuse it. Siblings: because-bridge (K-2), main-idea-pinboard (3-5), quote-picker (4), claim-court (5), argument-x-ray (6), debate-prep-desk (6), cer-builder (6-8), claim-quote-comment (6-8), theme-evidence-ladder (6-8), argument-builder-pro (9), theme-ledger (9-12). Pure parts in one marked block, exposed as `__tool.ev`.
- **Source pack**: `{id, title, author, edition, paras:[{id, text, sents:[[start,end]]}], key}`. Text exactly as in the edition. Sentence and word offsets are computed once (`ev.index(pack)`), so spans are word ranges `{para, from, to, skips:[[a,b]]}`.
- **Spans**: `ev.quote(pack, span)` returns the exact words with "..." for skips; `ev.words(span)` counts.
- **Claims**: `{id, text, side}`; `ev.claimCheck(text)` returns `topic` when the text has fewer than 5 words or no verb from a small built-in verb list, else `ok`.
- **Evidence links**: `{id, span, claim, weight 1-3, tag, comment, leadIn}`. `ev.checks(link, opts)` returns flags: `repeats` (the comment shares 60 percent or more of the quote's content words, or 5 or more consecutive words), `unexplained` (comment under `opts.minWords`, default 6), `long` (quote over `opts.maxWords`, default 40), `dropped` (no lead-in, Draft only), `offKey` (the pack's key gives this paragraph 0 for this claim; shown only as "One reading doesn't see this here"). A built-in stoplist defines content words. Checks are advice; nothing is refused.
- **Strength**: a pack's key may rate spans or paragraphs 0 to 3 per claim; `ev.coverage(links, key)` returns the share of key-strong paragraphs the student covered; `ev.compare(links, key)` gives same, also, different per link.
- **Ledger view**: columns per claim, rows in text order, strike and remove, totals. **Board view**: a claim card with pinned evidence cards and a coverage meter (for the younger siblings).
- **Series**: `ev.series(links, nParas, window, filter)` returns per-paragraph summed weights per claim and `ev.crossings(seriesA, seriesB)`.
- **Draft**: `ev.pickStrong(links, n, minGap)`; `ev.draftChecks(frame)` applies `topic`, `dropped`, `unexplained`, `repeats` per slot.
- **Sides** (for argument-builder-pro and debate-prep-desk): claims carry `side: 'claim'|'counter'`; rebuttal links `{rebuttal, answers: linkId}`; `ev.fairFight(links, key)` compares the key strength of the best evidence on each side.
This tool uses: Source pack (two stories with keys), Spans with skips, Evidence links, checks, Ledger view, Series and crossings, Draft. Not Board view or Sides.

## Sources
- "The Gift of the Magi": O. Henry, The Four Million (1906), Project Gutenberg eBook #7256, https://www.gutenberg.org/ebooks/7256 (45 paragraphs; $1.87, $8 flat, $20 a week, $21 chain, $20 for the hair: from the text).
- First printed in the New York Sunday World, December 10, 1905: confirm at build against the O. Henry Museum or the Library of Congress "Today in History"; if not confirmed, say "first printed in 1905".
- "The Story of an Hour": Kate Chopin International Society, https://www.katechopin.org/story-hour/ (text and its note: Vogue, December 6, 1894, as "The Dream of an Hour").
- Married women's limited property and wage rights and hard divorce in the 1890s: confirm a plain one-line statement against the Library of Congress "Women's History" research guide or the National Women's History Museum at build; cut it if no source fits.
- Magi in the Bible story: Matthew 2:1-12 (King James Version).
- Checks run (Python, 2026-10-29) on both keys with a centered window of 1, 3 and 5. Magi, window 3: crossings at M9, M15, M23, M33 and M36 (5); Theme A peaks at 6 in M44 and M45; Theme B at 5 in M2, M33 and M34; Theme A quiet M1 to M4. The old text said Theme B leads M1 to M19 and A from M24 on, and its sample readouts gave 2 crossings, peaks at M45 and M34 and a quiet stretch M11 to M16; none of that matched the key, so the key readings and samples now carry the computed values. Hour, window 3: B leads H1 to H4, A from H5; ties at H13, H14, H21 and H23; crossings at H5 and H22 (2); Theme A peaks at 9 in H15. The old "Theme A rises from H9 and overtakes it" was late by four paragraphs. The slider now steps 1, 3, 5, because an even window has no center. Contrast ratios in Look recomputed with the WCAG 2.1 formula; all match to 0.01.

## Done when
- Both stories show every paragraph with its id; texts match the editions.
- An entry needs a span, a column, a weight and a comment; the "Just repeats the quote" note appears when the comment copies the quote.
- Trim makes a quote with "..." and keeps at least 3 words.
- The chart draws two lines with different markers and dash styles, marks every crossing with its paragraph, and filters change it at once.
- One reading draws the key behind the student's lines; with the key's own entries logged, the lines match it.
- Draft picks three entries spread across the story, and Check my paragraph flags a missing lead-in and a topic-only claim.
- Rows, statements and draft survive a reload; Clear this story asks first.
- At 375 wide Story and Ledger are tabs with the Log it bar visible; no horizontal scroll at any listed size.
- With every key entry logged at window 3, Magi reads "Crossings: 5" with marks at M9, M15, M23, M33 and M36, and Hour reads "Crossings: 2" at H5 and H22.
- Focus: at 1366x768 and 680x425 the story text and the ledger are side by side in Ledger, and the two theme lines are the largest thing in Chart.
- Tap while it plays: changing a filter or weight while the chart redraws acts at once, with no stale line.

## Open questions
- "The Story of an Hour" ends with a woman's sudden death and treats her husband's reported death as a release. Fine for grade 9 as the second story, or offer it only at the 11-12 setting?
