# Argument Builder Pro

## One idea
A fair fight: you build your argument and the other side's at the same time, the other side must get the strongest evidence in the pack (the tool calls the outline "rigged" if you hand it the weak stuff), and every rebuttal has to answer that specific evidence, not just repeat your claim louder.

## Not like
- debate-prep-desk (ela 6, evidence family, not built): builds a claim with reasons and faces practice counterarguments the tool supplies. Here the student builds the counterclaim, must make it as strong as the evidence allows, and the issue is a different one (not school start times).
- argument-frames-pro (eld 9-12, eld-talk family, not built): sentence frames for academic argument language at a proficiency level. Here there are no frames by level; the work is choosing and weighing evidence for both sides.
- argument-map (ela 12, rhetoric family): analyzes a published essay's structure. Here the student writes their own outline.
- theme-ledger (ela 9-12, evidence family): collects literary evidence for themes. Here the evidence is a civic pack and it is split between two sides.
- audience-shift-briefing (ela 9): presents one finding to three rooms. Here there is one reader and two opposing sides.
- claim-court (ela 5, evidence family, not built): sorts given reasons into strong, weak and irrelevant. Here strength decides who gets what, and the student must give away strength.

## Who and how
- Grade 9 ELA. Module: Writing arguments.
- Driver: students on laptops; a partner joins for Swap seats. 40 to 50 minutes (build 25 to 30, review 10, outline 5).
- Standards: W.9-10.1 (arguments to support claims, using valid reasoning and relevant and sufficient evidence): 1a precise claim distinguished from alternate claims (Claim step and claim check); 1b develop claim and counterclaims fairly, supplying evidence for each and pointing out strengths and limitations of both (Their side, the rigged check, the Limits fields); 1c words and clauses that link the parts (transition chips); 1d formal style (the rubric's style row and the informal-word note); 1e a concluding statement (Close step).
- tool.json: driver "students", minutes "40-50", modes ["Build", "Review", "Outline"], grades_label "Grade 9". Kit starter plus `kit:evidence`.

## Screens and modes
Header: title "Argument Builder Pro", small line "A fair fight."; mode buttons **Build** (opens first), **Review**, **Outline**; Motion, Sound, Read. The issue card sits under the header: the painted Main Street picture (Art) as a thumbnail beside "Should Cedar Bend close Main Street to cars on Saturdays?" with **Read the pack** (opens the evidence drawer) and a note "Cedar Bend and every document in the pack are made up for Curio Class."

### Build (opens first)
Focus: the current step's work card, center stage and the biggest thing on screen. The painted town square bandstand (Art) is the backdrop; two painted podiums frame the card at the left and right edges, **Your side** on the left, **Their side** on the right, each holding its evidence chips (painted document icons) along its top. Above the card, a step strip: **1 Claim**, **2 Your reasons**, **3 Their side**, **4 Rebuttals**, **5 Close**. Steps can be visited in any order; each shows a ✓ when complete.
1. **Claim**: choose **Close it on Saturdays** or **Keep it open**, then write the claim in your own words (one sentence). The claim check flags a topic-only claim ("Main Street" alone) and a claim that hedges both ways ("maybe sometimes").
2. **Your reasons**: two or three reason cards. Each reason gets one or two evidence chips dragged from the pack drawer (or tapped with **Use for my side**), an **Explain** box (how it supports the reason) and a **Limit** box (what this evidence can't show). The checker notes "Just repeats the evidence" and "Explain it".
3. **Their side**: write the strongest counterclaim, then give it its two best evidence chips (dragged from the drawer onto Their side's podium, or tapped with **Use for their side**) with an Explain box each, written as its supporters would. A **Fair fight meter** sits at the top of the step card and compares the two strongest chips Their side holds with the two strongest in the whole pack for that side: when stronger evidence for them is left in the drawer, the meter reads **Rigged** with "Their side is missing D5. Would they leave that out?" (naming the strongest chip they don't hold); when their two hold as much strength as the pack's best two, it reads **Fair**.
4. **Rebuttals**: one rebuttal card per Their-side evidence chip, linked by a line. Each card asks for a move (**Concede and outweigh**, **Question the evidence**, **Answer the cost**) and the rebuttal text. The check asks that the rebuttal name that evidence (its chip id, or at least two of its key words); a rebuttal that only restates your claim gets "This answers your claim, not their evidence."
5. **Close**: a concluding statement box, with transition chips (**However**, **Even so**, **Some residents argue**, **On balance**, **For these reasons**) that insert at the cursor.
The pack drawer lists D1 to D8, each with its painted icon, its kind, its short text, its made-up source line and the sides it can help (shown only after a chip is used once: "Can help either side" and so on, so students judge first).

### Review
Focus: the rubric, the larger right column.
- The full outline read-only on the left; the rubric on the right, five rows, each scored **Not yet**, **Getting there**, **Strong**, with one line of what Strong looks like: Claim (precise, takes a side, not a topic); Reasons and evidence (each reason has evidence and an explanation that says how); Fair counterclaim (their best evidence, stated as they would); Rebuttals (each answers its evidence); Style and close (formal words, linked parts, a close that follows).
- **Self check** fills the rubric from the student's own view; beside each row the tool's checks (claim check, explain notes, Fair fight meter, rebuttal links, informal words like "kinda", "stuff", "super") are listed as evidence, never as a score.
- **Swap seats**: hides the student's own rubric answers and hands the screen to a partner, who fills the rubric and one comment per row. **Swap back** shows both ratings side by side.

### Outline
Focus: the outline text, centered and full width.
- The outline as clean text: claim, reasons with evidence and explanations, counterclaim with its evidence, rebuttals, close, with the transitions used. **Copy outline** (to paste into the student's own draft on this device), **Start over** (asks first). Everything stays on this device (localStorage).

## Content
All documents are original, written for this tool, about a made-up town; the numbers are invented for the exercise and labelled so. Strength (0 to 3) per side is the tool's key, used by the Fair fight meter; it is shown only in Review.
- D1 Merchant survey (Main Street Business Association, made up): "Of 62 shops on Main Street, 40 answered. 23 support Saturday closing, 12 oppose it, 5 are unsure." Close 2, Keep 1. Limit: 22 shops did not answer.
- D2 Pilot day counts (city planning office, made up): "On two trial Saturdays in June, volunteers counted people passing the corner of Elm and 3rd between 10 a.m. and 4 p.m.: about 3,400 each day, compared with about 1,900 on two ordinary Saturdays in May." Close 3, Keep 0. Limit: two days, one corner, June weather.
- D3 Sales report (city finance office, made up): "Total Main Street sales on the two trial Saturdays were 6 percent higher than on the same Saturdays last year. The hardware store reported sales down 18 percent and the pharmacy down 11 percent." Close 2, Keep 2. Limit: two days; stores that sell heavy or urgent items may lose out.
- D4 Fire department memo (made up): "The plan keeps a 20-foot emergency lane open on Main Street. During the trials, ambulances going to homes east of Main took about one minute longer on average because of detours on side streets." Close 1, Keep 3. Limit: two days of data.
- D5 Letter from the Cedar Bend Disability Council (made up): "Closing Main Street moves the nearest accessible parking two blocks away. Some of our members cannot walk two blocks. We ask for drop-off zones at both ends before any closing." Close 0, Keep 3. Limit: it names a fix, so it can also support closing with drop-off zones.
- D6 Bus notice (Cedar Bend Transit, made up): "Route 4 will detour on Saturdays, adding about 6 minutes to each trip." Close 0, Keep 2. Limit: 6 minutes, once a week.
- D7 Resident letter to the paper (made up): "Saturday is the only day I can walk downtown with my kids without worrying about cars." Close 1, Keep 0. Limit: one person's experience.
- D8 Online poll (a community page, made up): "81 percent of 230 voters said they loved car-free Saturdays." Close 0 (anyone could vote, more than once), Keep 0. Limit: self-selected; the drawer shows "Who could vote?" after it is used.
- Best for Keep it open: D4 and D5 (3 each, best two total 6). Best for Close it: D2 (3), then D1 or D3 (2), best two total 5. A student arguing Keep it open must give Their side D2 plus D1 or D3, and the meter calls Rigged if D2 stays in the drawer; a student arguing Close it must give Their side D4 and D5.
- Issue words (never count toward a rebuttal match, because a restated claim always contains them): main, street, streets, saturday, saturdays, close, closing, closed, open, car, cars, cedar, bend, town, downtown.
- Informal-word list for the style note: kinda, sorta, gonna, stuff, things like that, super, totally, basically, a lot of (suggest "many"), like (as filler, only flagged before a comma).

## Interactions in detail
- An evidence chip can sit on both sides at once (D3, D5 really do help both); the chip shows a small ⇄ when it does.
- Fair fight meter: sums the key strengths (for Their side's position) of the two strongest chips Their side holds, and compares that with the sum of the two strongest chips in the whole pack for that side; equal counts as Fair. When Rigged it names the strongest chip Their side does not hold (ties by lowest id). It updates on every chip move and never blocks. Their side may hold more than two chips; only the top two count.
- Rebuttal check: the chip id typed or inserted, or at least two shared content words with the evidence text, counts as "answers it". Content words: lowercase, split on anything that is not a letter or digit (so "one-minute" gives "one" and "minute"), drop a short stop-word list and the issue words in Content, drop words under 3 letters, and strip a final -s, -es, -ed or -ing from words over 4 letters before comparing.
- Step ✓ rules: Claim (claim check ok), Reasons (two or more reasons each with evidence and an Explain of six or more words), Their side (counterclaim plus two chips plus explanations), Rebuttals (one per Their-side chip, each "answers it"), Close (a statement of eight or more words).
- Storage `argument-builder-pro:v1` (try/catch). Swap seats ratings are kept until Start over.
- Mode change calls `V.hush()`; the hint changes at once.
- Nothing plays on its own. Chip moves ease over 200 ms (instant with Motion off); a tap or drag during an ease lands at once and the meter updates on that same tap.
- Sizes: at 760 and below the podiums stack (Your side above Their side) with a sticky step strip; the pack drawer slides over from the bottom at 375. At 680x425 the step strip, the current step's main box and the pack button are visible without scrolling. No horizontal scroll at any listed size.

## Look
- Own light `:root`, a town square debate (the painted backdrop sits behind a `--paper` card at 92 percent opacity, so text contrast is measured on `--paper`): `--paper #f3f6f1`, `--panel #ffffff`, `--ink #18221a`, `--muted #4d5a50`, `--line #d3dccf`, accent `--brand #095909` (civic green: header rule, step ticks, active mode, Fair reading), `--btn #095909`, `--btn-line #8a9a8c`, `--head-ink #ffffff`, `--focus #a61b5b`. Your side podium's blank front panel gets a `#0a4f9c` band with the word "Your side", Their side's a `#9c2b0a` band with "Their side" (text in code); the meter shows **Fair** with ✓ and **Rigged** with ⚠ and words.
- Neighbors: research-notebook fountain-pen blue, theme-ledger wine, rhetoric-spotter electric blue, audience-shift-briefing magenta, thesis-workshop slate indigo. Nearest catalog accent habitat-hunt (dE 15.4, grade 3-5 science).
- Contrast (WCAG 2.1): white on brand 8.59:1; brand on paper 7.88:1; ink on paper 15.02:1; muted on paper 6.66:1, on panel 7.26:1; focus on panel 7.17:1, on paper 6.58:1; Your side on panel 8.04:1; Their side on panel 7.60:1 (both carry white text: 8.04:1 and 7.60:1). All pass AA.

## Art
Eleven painted images, all local FLUX (`scripts/localart.py`), people: false. No people are needed: the sides are podiums and the evidence is documents.
- `square`: "A white wooden gazebo bandstand on a park lawn in a small-town square, oak trees and empty park benches, warm afternoon light". 16:9; cutout no; people: false. Build's stage backdrop (an outdoor debate, so it differs from the indoor rooms in audience-shift-briefing), dimmed behind the step card; cover-fit, re-cropped per size.
- `podium`: "One wooden lectern with a wide blank front panel, front view, soft studio light, plain light backdrop". 3:4; cutout yes; people: false. Drawn twice (the right one mirrored); code puts the side's color band and name on the blank panel and its chips along the top edge.
- `main-street`: "Brick main street of a small Midwestern town on a sunny morning, shop awnings with blank signboards, string lights across the street, empty pavement, trees in planters". 16:9; cutout no; people: false. Issue card thumbnail (about 160 px wide; 96 px at 375 wide). Signs stay blank.
- Document kit (8 cutouts, one per pack document). Shared prompt: "single object, three-quarter view, soft studio light, plain light backdrop, painted, blank paper and blank screens". Pieces: `d1-clipboard` a clipboard holding a blank survey sheet; `d2-tally` a metal hand tally counter; `d3-receipt` a long curling paper sales receipt; `d4-helmet` a red firefighter's helmet; `d5-envelope` an opened envelope with a folded blank letter; `d6-busstop` a bus stop sign on a short pole with a blank plate; `d7-newspaper` a folded newspaper with blank columns; `d8-phone` a smartphone with a blank glowing screen. 1:1; cutout yes; people: false. Sizing rule: each object fills about 80 percent of its square, centered; shown at 28 px in chips and on podiums, 72 px on drawer cards. The chip's id (D1 to D8) stays in code beside the icon.
Drawn in code: the step strip, cards, chip frames, rebuttal link lines, the Fair fight meter and the rubric.

## Voice
Bank voice `big-sister` (Leda), style "Say in a friendly, youthful way, like a senior on the debate team helping a freshman." Not used by any 9-12 ELA or evidence sibling specced so far, nor by another spec in this batch. `Curio.voice`, `scope: () => state.mode`.
- w-build (how, Build welcome; stale once a side is chosen): "Tap Close it on Saturdays or Keep it open. Then write your claim in one sentence."
- reasons (how, first time step 2 opens; stale when step 2 closes): "Drag a card from the pack onto a reason, or tap Use for my side. Then explain how it helps."
- their (how, first time step 3 opens; stale when step 3 closes): "Now argue their side. Give their podium its best evidence with Use for their side."
- rigged (how, first Rigged reading; stale when the meter reads Fair): "That's rigged. Their best evidence is still in the drawer. Tap Read the pack and give it to them."
- fair (event, each time the meter turns Fair; stale if it changes back): "Fair fight."
- rebut (how, first time step 4 opens; stale when step 4 closes): "Pick a move on each card, then write a rebuttal that names their evidence."
- close (how, first time step 5 opens; stale when step 5 closes): "Write your closing sentence. Tap a transition chip to add it at the cursor."
- w-review (how, Review welcome; stale after the first rating): "Tap Not yet, Getting there or Strong on each row. Then tap Swap seats for your partner."
- w-outline (how, Outline welcome; stale on mode change): "Here's your outline. Tap Copy outline and paste it into your draft."

## Family engine
`kit/evidence.js`, described in full in tools/theme-ledger/spec.md. This tool uses: Source pack (D1 to D8 as one-paragraph documents with a key by side), Claims with `side`, claim check, Evidence links with `checks` (repeats, unexplained), Sides (`ev.fairFight` for the meter; rebuttal links with `answers`), and the Board view as two podiums. Not Series, Draft or Ledger view.

## Sources
- All documents, numbers and Cedar Bend are made up for this tool (stated on screen). No outside facts are used.
- W.9-10.1 text: Common Core State Standards for English Language Arts, Writing, grades 9-10, standard 1 (a to e), https://www.thecorestandards.org/ELA-Literacy/W/9-10/.
- Checks run in Python (2026-10-29) on the D1 to D8 texts:
  - Rebuttal check, old rule (any two shared words): restated claims such as "Main Street should close to cars on Saturdays." passed against D4 and D5 (shared "main" and "street"); 3 of 5 restated claims wrongly counted as answers. With the issue words and stems in Interactions: 0 of 7 restated claims pass, and 5 of 5 real rebuttals pass ("A one-minute delay for ambulances matters less than safer sidewalks." matches D4 on minute and ambulance; "Two June days at one corner don't prove crowds all year." matches D2 on june and corner).
  - Fair fight meter, old rule (best chip only): Their side holding D4 and D6 read Fair, contradicting "must give Their side D4 and D5". With the top-two rule: Keep side D6 + D8 Rigged naming D2; D2 + D1 Fair; D2 + D6 Rigged naming D1; Close side D4 + D5 Fair; D4 + D6 Rigged naming D5; nothing held, Rigged naming D4.

## Done when
- Focus: in Build at 1366x768 and 680x425, the current step's card is the largest thing on screen, centered between the two painted podiums, with the step strip and the pack button visible without scrolling.
- A claim of "Main Street" alone gets the topic note; a one-sentence claim with a side passes.
- Arguing Keep it open with D6 and D8 on Their side reads Rigged naming D2; with D2 and D1 it reads Fair; with D2 and D6 it reads Rigged naming D1.
- Arguing Close it with D4 and D5 on Their side reads Fair; with D4 and D6 it reads Rigged naming D5.
- A rebuttal that only restates the claim ("Main Street should close to cars on Saturdays.") gets "This answers your claim, not their evidence" against D4; one that names D4 or two of its key words (minute, ambulance, detour, lane) passes.
- A tap or drag during a chip's ease lands at once and the meter changes on that same tap; no voice line names a control that is hidden or disabled.
- Step ticks follow the rules above; transitions insert at the cursor.
- Swap seats hides the self ratings until Swap back, then shows both.
- Outline copies clean text; there is no Print button; everything survives a reload; Start over asks first.
- At 375 wide the podiums stack and the drawer works; no horizontal scroll at any listed size; every painted icon has its D number beside it in code.

## Open questions
- None beyond the group's shared ones. (Changed in revision: Print was removed under the scope rule; the Fair fight meter now compares the top two chips and the rebuttal check ignores issue words, after checks showed the old rules gave wrong answers.)
