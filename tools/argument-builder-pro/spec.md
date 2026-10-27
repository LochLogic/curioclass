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
Header: title "Argument Builder Pro", small line "A fair fight."; mode buttons **Build** (opens first), **Review**, **Outline**; Motion, Sound, Read. The issue card sits under the header: "Should Cedar Bend close Main Street to cars on Saturdays?" with **Read the pack** (opens the evidence drawer) and a note "Cedar Bend and every document in the pack are made up for Curio Class."

### Build (opens first)
Two podiums face each other across the stage: **Your side** on the left, **Their side** on the right. Between them, a step strip: **1 Claim**, **2 Your reasons**, **3 Their side**, **4 Rebuttals**, **5 Close**. Steps can be visited in any order; each shows a ✓ when complete.
1. **Claim**: choose **Close it on Saturdays** or **Keep it open**, then write the claim in your own words (one sentence). The claim check flags a topic-only claim ("Main Street" alone) and a claim that hedges both ways ("maybe sometimes").
2. **Your reasons**: two or three reason cards. Each reason gets one or two evidence chips dragged from the pack drawer (or tapped with **Use for my side**), an **Explain** box (how it supports the reason) and a **Limit** box (what this evidence can't show). The checker notes "Just repeats the evidence" and "Explain it".
3. **Their side**: write the strongest counterclaim, then give it its two best evidence chips with an Explain box each, written as its supporters would. A **Fair fight meter** compares the strength of the best evidence Their side holds with the best still unused in the pack: when stronger evidence for them is left in the drawer, the meter reads **Rigged** with "Their side is missing D5. Would they leave that out?"; when they hold the best available, it reads **Fair**.
4. **Rebuttals**: one rebuttal card per Their-side evidence chip, linked by a line. Each card asks for a move (**Concede and outweigh**, **Question the evidence**, **Answer the cost**) and the rebuttal text. The check asks that the rebuttal name that evidence (its chip id, or at least two of its key words); a rebuttal that only restates your claim gets "This answers your claim, not their evidence."
5. **Close**: a concluding statement box, with transition chips (**However**, **Even so**, **Some residents argue**, **On balance**, **For these reasons**) that insert at the cursor.
The pack drawer lists D1 to D8, each with its kind, its short text, its made-up source line and the sides it can help (shown only after a chip is used once: "Can help either side" and so on, so students judge first).

### Review
- The full outline read-only on the left; the rubric on the right, five rows, each scored **Not yet**, **Getting there**, **Strong**, with one line of what Strong looks like: Claim (precise, takes a side, not a topic); Reasons and evidence (each reason has evidence and an explanation that says how); Fair counterclaim (their best evidence, stated as they would); Rebuttals (each answers its evidence); Style and close (formal words, linked parts, a close that follows).
- **Self check** fills the rubric from the student's own view; beside each row the tool's checks (claim check, explain notes, Fair fight meter, rebuttal links, informal words like "kinda", "stuff", "super") are listed as evidence, never as a score.
- **Swap seats**: hides the student's own rubric answers and hands the screen to a partner, who fills the rubric and one comment per row. **Swap back** shows both ratings side by side.

### Outline
- The outline as clean text: claim, reasons with evidence and explanations, counterclaim with its evidence, rebuttals, close, with the transitions used. **Copy outline**, **Print** (print stylesheet), **Start over** (asks first). Everything stays on this device (localStorage).

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
- Best for Keep it open: D4 and D5 (3 each). Best for Close it: D2 (3), then D1 or D3 (2). A student arguing Keep it open must give Their side D2, and the meter calls Rigged if D2 stays in the drawer; a student arguing Close it must give Their side D4 and D5.
- Informal-word list for the style note: kinda, sorta, gonna, stuff, things like that, super, totally, basically, a lot of (suggest "many"), like (as filler, only flagged before a comma).

## Interactions in detail
- An evidence chip can sit on both sides at once (D3, D5 really do help both); the chip shows a small ⇄ when it does.
- Fair fight meter: compares the highest key strength for Their side among chips they hold against the highest unused; ties count as Fair. It updates on every chip move and never blocks.
- Rebuttal check: content-word overlap with the evidence text of at least two words, or the chip id typed or inserted, counts as "answers it".
- Step ✓ rules: Claim (claim check ok), Reasons (two or more reasons each with evidence and an Explain of six or more words), Their side (counterclaim plus two chips plus explanations), Rebuttals (one per Their-side chip, each "answers it"), Close (a statement of eight or more words).
- Storage `argument-builder-pro:v1` (try/catch). Swap seats ratings are kept until Start over.
- Mode change calls `V.hush()`.
- Sizes: at 760 and below the podiums stack (Your side above Their side) with a sticky step strip; the pack drawer slides over from the bottom at 375. At 680x425 the step strip, the current step's main box and the pack button are visible without scrolling. No horizontal scroll at any listed size.

## Look
- Own light `:root`, a town hall debate stage: `--paper #f3f6f1`, `--panel #ffffff`, `--ink #18221a`, `--muted #4d5a50`, `--line #d3dccf`, accent `--brand #095909` (civic green: header rule, step ticks, active mode, Fair reading), `--btn #095909`, `--btn-line #8a9a8c`, `--head-ink #ffffff`, `--focus #a61b5b`. Your side podium `#0a4f9c` with the word "Your side", Their side podium `#9c2b0a` with "Their side"; the meter shows **Fair** with ✓ and **Rigged** with ⚠ and words.
- Neighbors: research-notebook fountain-pen blue, theme-ledger wine, rhetoric-spotter electric blue, audience-shift-briefing magenta, thesis-workshop slate indigo. Nearest catalog accent habitat-hunt (dE 15.4, grade 3-5 science).
- Contrast (WCAG 2.1): white on brand 8.59:1; brand on paper 7.88:1; ink on paper 15.02:1; muted on paper 6.66:1, on panel 7.26:1; focus on panel 7.17:1, on paper 6.58:1; Your side on panel 8.04:1; Their side on panel 7.60:1 (both carry white text: 8.04:1 and 7.60:1). All pass AA.

## Art
None: drawn in code (two podiums, cards, chips). No people.

## Voice
Bank voice `big-sister` (Leda), style "Say in a friendly, youthful way, like a senior on the debate team helping a freshman." Not used by any 9-12 ELA or evidence sibling specced so far. `Curio.voice`, `scope: () => state.mode`.
- w-build (how): "Start with step one: pick a side and say it in one sentence."
- reasons (how, first time step 2 opens): "Give each reason a piece of evidence, then explain how it helps."
- their (how, first time step 3 opens): "Now argue their side as well as they would. Give them their best evidence."
- rigged (how, first Rigged reading): "That's rigged. Their best evidence is still in the drawer."
- fair (event, when the meter turns Fair; stale if it changes back): "Fair fight."
- rebut (how, first time step 4 opens): "Answer each piece of their evidence, not just their claim."
- w-review (how): "Rate each row honestly. Then press Swap seats and let a partner rate it."
- w-outline (how): "Here's your outline. Copy it into your draft."

## Family engine
`kit/evidence.js`, described in full in tools/theme-ledger/spec.md. This tool uses: Source pack (D1 to D8 as one-paragraph documents with a key by side), Claims with `side`, claim check, Evidence links with `checks` (repeats, unexplained), Sides (`ev.fairFight` for the meter; rebuttal links with `answers`), and the Board view as two podiums. Not Series, Draft or Ledger view.

## Sources
- All documents, numbers and Cedar Bend are made up for this tool (stated on screen). No outside facts are used.
- W.9-10.1 text: Common Core State Standards for English Language Arts, Writing, grades 9-10, standard 1 (a to e), https://www.thecorestandards.org/ELA-Literacy/W/9-10/.

## Done when
- A claim of "Main Street" alone gets the topic note; a one-sentence claim with a side passes.
- Arguing Keep it open with D6 and D8 on Their side reads Rigged naming D2; moving D2 over reads Fair.
- Arguing Close it with D4 and D5 on Their side reads Fair.
- A rebuttal that only restates the claim gets "This answers your claim, not their evidence"; one that names D4 or its key words passes.
- Step ticks follow the rules above; transitions insert at the cursor.
- Swap seats hides the self ratings until Swap back, then shows both.
- Outline copies clean text; everything survives a reload; Start over asks first.
- At 375 wide the podiums stack and the drawer works; no horizontal scroll at any listed size.

## Open questions
- None beyond the group's shared ones.
