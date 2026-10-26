FIX (no blockers; five should-fix items, mostly about how clearly the wall teaches the one idea)

Checked cold on 2026-10-25 against spec.md, VERIFY.md and BATCH-G11.md. Draft bundle (CURIO_DRAFT=1, newsprint art still a placeholder, 20 voice clips inlined). I drove it over CDP at 1280x720, 1440x900, 1000x625, 800x500, 680x425, 760x900, and at 375 px wide in an iframe host. I ran real mouse clicks for voice, real Tab and arrow keys for the keyboard, and Motion off. No console errors or exceptions in any of the 56 frames. No network requests: the only URL in the bundle is the SVG namespace.

## Statistics (SAMPLING ENGINE block run in node, default town seed 1936)

- Truth is 44.75 percent (shown as 44.8), the same on every build. Done-when 1 passes. The mail frame is 10,623 people (spec says about 10,500).
- Margin of error is 196 x sqrt(p(1 - p) / n) points, with 0.5 used at p = 0 or 1. Checked: 212 of 400 gives 4.89, and n = 20 at p = 0 gives 21.9. Every method uses this same formula, as the spec says.
- Share of intervals that caught the truth (from 600 to 1,500 repeats):
  - Simple random: 0.94, 0.95, 0.96 and 0.95 at n = 100, 400, 1000 and 2000. That is right.
  - Stratified: 0.96 to 0.975. Slightly above 95, as expected.
  - Systematic: 0.97 to 1.00, with a spread under simple random's. This is correct behavior: the list is ordered by block, so the sample is spread over blocks like a stratified one. Nothing in the tool or notes explains it, so a sharp student may ask.
  - Cluster: 0.68 to 0.73, so 35 of 51 is typical. Done-when 6 passes. notes.md says "67 to 72", which is right; the spec's "about 63" is a little low.
- Cluster design effect: variance ratio 3.5 to 4.2, spread ratio about 1.9 to 2.05. That backs "about twice as spread out".
- Bias at n = 100 / n = 2000, in points:
  - Mall on Saturday: +9.1 / +8.8
  - Online poll: +30.5 / +29.2
  - Daytime phone calls: -11.8 / -11.1
  - Mail to car and phone owners: -16.2 / -15.5
  - Mail's centers are 28.5 / 29.3 and its spread falls from 4.6 to 0.9. Done-when 3 and 4 pass.
  - The center does creep about 1 point toward the truth as n grows. That is because a weighted draw without replacement uses up its high-weight people. It is too small to see on the wall.
- Wording, simple random, n = 1000: Leans yes +8.3, Leans no -8.8. Done-when 5 passes.
- Headline rules: tested at the edges using the printed one-decimal numbers.
  - 54.9 with 4.9 gives split; 55.0 with 4.9 gives backs, 55 to 45.
  - 45.0 with 4.9 gives says no, 45 to 55; 45.1 with 4.9 gives split.
  - 0 percent at n = 20 gives says no, 0 to 100.
  - The two whole numbers always add to 100. Done-when 10 passes.
- Budget desk prices match the spec ($25 / $25 / $8 / $25 / $3 / $0 / $6 / $2). The most a $25 method can afford is n = 400 ($10,000, allowed). n = 600 reads "Over budget by $5,000" and Publish is disabled. Round 3's truth was 51.1.
- Speed: 50 polls at n = 2000 take 15 to 20 ms in node.

## 1936 facts

All of these match Squire (1988), Lohr and Brick (2017) and the standard accounts I checked on the web:
- About 10 million ballots mailed and about 2.4 million returned, drawn from phone, car and subscriber lists.
- The 57 to 43 Landon forecast is a two-way share. Notes correctly gives about 54 percent once minor candidates are counted.
- Roosevelt 60.8 to Landon 36.5, and 523 to 8 electoral votes.
- Gallup's smaller poll called a Roosevelt win.
- The explanation is frame plus nonresponse.

The case card matches the spec word for word.

## Findings

1. **Workshop wall, "Plus or minus caught the truth"** counts every dot shown, across all methods. After the notes' 5-minute start it reads "45 of 100" and in Case file "18 of 40". That hides the key contrast, which is 0 of 20 for the Digest's method against 18 of 20 for the fair one. Seen in the mail_* and case_* frames and the truthBody text. **Should fix.** When Show is "All methods", give one count per method on the wall, or per pile in Case file.
2. **Wall does not show n.** n = 100 and n = 2000 dots of the same method are the same color and stack in one pile. The comparison the hint asks for ("Try n = 2000 and see") shows up only as a wide base under a spike, and you can tell which is which only by hovering. The normal curve then fits that mix. With "All methods" it fits two methods at once: the mail_1440x900 frame reads "mean 37.2, sd 8.0" across Random plus Mail, a bimodal mix. **Should fix**, because this is the tool's one idea. Options: a Show choice for "this design" (method, wording and n), or different dot sizes or labels by n. At minimum, fit the curve only to one design. The note "Run at least 10 polls of this design" already implies that.
3. **Methods on the wall differ only by color.** Under deuteranopia, Stratified (#5fd39a), Mall (#ff8a8a) and Mail (#d9c27a) all come out about beige (Machado simulation). Case file's two piles are Stratified against Mail. Position, the tooltip and the screen-reader list help, but the key works by color alone. **Should fix:** label each pile, or give the key and dots shapes.
4. **First-tap voice order** (src.html, the first pointerdown handler and narrate). If a student's first click is Run poll, "One poll can be lucky..." plays first, then "Welcome to Millbrook...", then the how-to. Seen in the real-click run vA_runfirst. The 350 ms welcome timer queues after the click's own line. **Should fix:** queue the mode welcome ahead of any line triggered by the first tap.
5. **Budget desk verdict check works against the lesson** (spec rule, implemented as written). Over 150 random towns, Cluster at n = 1000 is "verdict right" 76 percent of the time, against 73 percent for Simple random at n = 400. That is despite Cluster's plus or minus catching the truth only 68 percent of the time. The three biased methods still score "right" 52 percent of the time. An honest "split" from the best affordable fair poll is marked wrong whenever the truth is 52 to 55 percent. **Should fix (design call for Cory):** for example, count "split" as right when the truth is inside the plus or minus, or reword the check.
6. **16:10 preview (680x425, 800x500):** the controls are all visible. But after Run poll the result and headline card sit below the fold of the panel, and at 680x425 the wall's plot is only about 50 px tall. Seen in run_800x500 and reveal_680x425. **Nit.** Full screen is fine.
7. **Curve label collides with the newest dot.** "mean 37.2, sd 8.0; shaded: middle 95 percent" is overlapped by the newest dot's ring and bar when that dot is the top of a tall pile (mail_1000x625). In Budget desk the "R1" label sits under the truth line (budpub_800x500). **Nit.**
8. **Clear wall leaves the Case file flags set.** Afterward both buttons still say "ran 20", and running either one alone reveals the truth at once. Also, a truth already revealed in Workshop shows in Case file before any case run. **Nit.**
9. **"biased" hint** says "Try n = 2000 and see" even when n is already 2000. **Nit.**
10. **notes.md wording:**
    - "with everyone answering, the Digest would still have picked Roosevelt": "still" reads as if the Digest picked Roosevelt. It should say "would have picked Roosevelt".
    - Step 2, "about 48 of 51 plus-or-minus bars reach it": only the newest bar is drawn, so this should refer to the "caught the truth" readout.
    - **Nit.**

## Passed with no finding

- Every spec mode, button and label is present.
- Done-when items 1 to 10, apart from the teaching concerns above.
- Supporter and opposer marks differ in shape (filled with a check, hollow with an x), and the map key matches.
- Tab order: the header, then Show, Curve and the wall (one tab stop), then the design panel. Arrow keys, Home and End move between dots. The live region reads "43 of 50. Simple random, Neutral, n = 400: 47.0 percent...". The tooltip shows the dot's bar.
- No visible control is under 44 px at 1280x720 or 680x425.
- Motion off: 50 dots appear at once.
- allLines() matches voice/lines.json exactly (20 lines, 20 clips in the bundle).
- Voice, tested with real clicks:
  - Read cuts off a welcome and speaks the hint.
  - Lines dropped by a stop are not marked as said.
  - Case file's "Same town..." line plays after its welcome.
  - In Budget desk, the welcome, publish and close-race lines queue in order.
  - Read works with Sound off.
  - A mode switch stops speech.
- No em dashes. "Curio Class" is never shortened to "Curio". prompts.json has newsprint with people: false. The theme link is in place. There is no score or celebration.

Unsure of: the newsprint art was still a placeholder, so I did not judge its legibility under the headline. I did not test real speech timing against clip lengths beyond the 2.5 s plus 80 ms per character timeout. I am judging findings 2 and 5 on teaching grounds, not against the spec text.

## Re-verify

PASS (all five should-fix items are fixed; four small nits below)

Checked cold on 2026-10-25. I rebuilt the draft bundle with CURIO_DRAFT=1; it came out byte-identical to the one on disk. I drove it over CDP at 680x425, 800x500, 1000x625, 1280x720 and 1400x900, and at 760 and 375 wide in an http-served iframe host, with Motion off. There were no console errors or exceptions in any tool frame. The only 404s were the host page's favicon and one probe of mine. I re-ran the SAMPLING ENGINE through the verdict rule in node.

### Prior findings

1. **Per-design catch counts: fixed.** Each row's caption and the truth panel now count by design. After the notes' 5-minute start they read "Simple random, n = 400: 45 of 51" and "Mail to car and phone owners, n = 2,000: 0 of 50". In Case file they read "Mail, n = 2,000: 0 of 20" and "Stratified, n = 2,000: 18 of 20".
2. **Wall shows n, one row per design: fixed.** Each design (method, wording, n) gets its own labeled row, and the curve is fitted to one row only. With Mail run at n = 100 and at n = 2000 the rows read "mean 29.4, sd 4.2" and "mean 29.3, sd 0.7", with the white truth line at 44.8 well clear of both. Without the curve, the wide pile and the narrow spike still sit in the same place, labeled "caught 4 of 50" and "caught 0 of 50". "Bias does not shrink with sample size" is now unmistakable on the default view once both n have been run. Even at 680x425 three rows fit (the wall is now 142 px, not about 50). When there are more designs than rows fit, the most recent rows show, with an "older designs not shown" note.
3. **Color-only methods: fixed.** Every row caption starts with the method's shape and name, and the truth list repeats the shape. At the small dot sizes of a 50-dot pile the shapes themselves are hard to tell apart, but the row label carries the meaning.
4. **First-tap voice order: fixed.** I held each click (press, 120 ms, release) and logged every clip play and stop:
   - First tap on Run poll: welcome, then how-to, then "One poll can be lucky".
   - First tap on Reveal: welcome, how-to, reveal, moe.
   - First tap on Case file plays its welcome only; Budget desk the same. A Tab key as the first input plays the Workshop welcome.
   - Read as the first tap speaks the hint first, then the welcome.
   - Read 1.1 to 1.8 s into a welcome cuts it off and speaks the hint. A Run poll after that queues "One poll can be lucky" behind Read, once, even after two clicks. The dropped how-to is not replayed.
   - Case file, both buttons clicked during the welcome: "Same town..." plays after the welcome. In Budget desk the order is welcome, publish, publish, close.
   - A mode switch stops speech. Read works with Sound off.
5. **Budget verdict rule: fixed.** "split" now counts as right when the truth is inside the plus or minus. The screen and notes.md explain the rule. Node, with the best affordable n:
   - Over 300 random towns: Simple random, Stratified and Systematic (n = 400) are right 98 to 99 percent of the time and Cluster (n = 1000) 89 percent. The biased methods are right 34 to 66 percent of the time, and their plus or minus never covers the truth.
   - Over 150 close-race towns (48 to 52): the three fair $25 methods are right 97 to 100 percent of the time, Cluster 83, and the biased methods 49 to 51.
   - This matches notes.md and now rewards the lesson.
   - Edges: split with the truth inside gives yes, split with the truth outside gives no, and "backs" with the truth at 50.1 gives yes.
6. **16:10 preview: improved; acceptable.** In compact layout the wall title now carries the newest result (for example "28.0% ± 2.0: says no"). The newsprint card is still below the fold at 680x425 and 800x500, but the panel scrolls to it.
7. **Curve label collisions: fixed.** Curve stats and the Budget round label moved into the row captions, which sit on a plate. The truth line is dimmed where it crosses a caption, so the text stays readable.
8. **Clear wall and Case file: fixed.** Clear wall resets both "ran 20" flags and hides the truth. A truth revealed in Workshop stays hidden in Case file until both case runs are done.
9. **"Try n = 2000" at n = 2000: fixed.** At n = 2000 a biased method gets the moe line as its hint instead.
10. **notes.md wording: fixed.** It now says "would have picked Roosevelt", and step 2 points at the truth panel.

### Engine and assets

- Fresh-load numbers are unchanged from the first verify:
  - Truth is 44.75 (shown as 44.8) and the mail frame is 10,623.
  - Margin of error: 4.89 for 212 of 400, and 21.9 for n = 20 at p = 0.
  - Bias at n = 100 / 2000, in points: mall +9.6 / +8.7, online +31.3 / +29.3, phone -11.7 / -11.1, mail -16.0 / -15.4.
  - Wording: Leans yes +8.3, Leans no -8.9.
  - Headline edge cases are the same as before.
- The notes' fresh-load figures check out:
  - Simple random n = 1000 x 51: 44.8, sd 1.7, 48 of 51.
  - Cluster: 43.6, sd 3.05, 35 of 51.
  - Mail n = 2000: 29.6, plus or minus 2.0, 0 of 51.
- Newsprint art is inlined: one webp data URI, 1200x300. It is real art, no longer a placeholder, but very flat (pixel sd about 2), as prompted. The headline stays easy to read on it.
- All 20 clips are inlined as audio data URIs. Their text keys match voice/lines.json exactly, and allLines() matches too: 20 lines with the same character count.
- No URLs other than the SVG namespace. No em dashes. Nothing under 44 px at any size, and no horizontal scroll.

### New nits

1. **notes.md, 5-minute start step 2:** it says "about 48 of 51". On a fresh load, following the steps exactly (n = 400), the truth panel reads 45 of 51. (48 of 51 is the n = 1000 figure.) **Nit.**
2. **notes.md, 5-minute start step 3:** it runs Mail only at n = 2000. The class sees fair against biased, but never the same biased method at two sizes, which is the pair that shows bias not shrinking. That pair appears only if Talk prompt 3 is used. Suggest running Mail at n = 100 first, then sliding to 2000. **Nit.**
3. **spec.md:65-66** still gives the old 52/48 verdict rule, so it now disagrees with the tool and notes. notes.md, "Good to know", says "fair designs stay at 99 percent" in close races, but Cluster is about 83 there. **Nit.**
4. **Case file after the Workshop start:** the walls are shared, so the Digest row merges with Workshop's own Mail n = 2000 polls ("70 polls · caught 0 of 70"), and the Random n = 400 row stays as a third row. Meanwhile the hint says "two piles" and "each button runs 20 polls". The contrast still reads clearly. **Nit.**
