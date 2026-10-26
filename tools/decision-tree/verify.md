# Verify: decision-tree

**Verdict: FIX** (1 blocker, 7 should fix, 8 nits). The math, content and voice queue are right; the problems are
layout at the preview and laptop sizes, focus loss, and two first-screen states in Side by side and Make a call.

Checked cold on the draft bundle (`CURIO_DRAFT=1 python scripts/bundle_tool.py decision-tree`, 142 KB, art in, no voice
clips yet so speech fell back to the browser voice) in muted headless Chrome on private ports, with real held clicks
and real keys, at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 760x600 and 375x812 (iframe host).

## What passed

- **Content (Done 1):** every setup, sign, option, leaf text, who tag, mark code, graft pair and look-back question
  read out of the page matches spec.md exactly (parsed the spec and diffed field by field: no differences).
- **Standings (Done 2):** recomputed in Python from the spec codes and read from the tool's own `tally`/`bestOf`; both
  match the spec's worked check at R/W/M for all four dilemmas, ties included (Booking C,G / G / D; Quiz G / B / B;
  Tablet C,G / B,C / B; Game G / B,C,G / C). Badge tallies on screen match (e.g. Booking A at Next month "2 up, 6 down").
- **Quiz Photo cheating:** over all 15 non-empty goal sets, with or without the graft, A is never best or tied at
  Next month. (See nit 7 for partial plantings.)
- **Graft (Done 4):** only the listed pairs work; A+B and A+C give the miss line, then the "Look for two options" line;
  pulling up C removes G. Planting G plants both parents (judgment call: fine, it keeps "a graft grows from both
  parents" true and nothing in the spec forbids it).
- **Make a call (Done 5):** hit, miss, tie hit and tie miss all correct ("Surprise: B and D are standing best by next
  month." for a tie; judgment call on the tie wording: fine, clear and grammatical). Moving back below Next month
  clears the line and keeps the flag. Works through Play too, with one chime and one spoken line.
- **Choose a branch (Done 7):** card shows "{name} chose: {option}.", the three leaves and the look-back question; no
  grade; focus lands on "Back to the tree"; Escape returns focus to "Choose a branch".
- **Side by side (Done 6):** two trees, ghost bud "Graft not found yet" until found in Grow, line updates, Swap swaps.
- **Storage, input, network (Done 8):** only `curio-motion` in localStorage after a full session; the only input is the
  range slider; no resource requests; no console errors or exceptions in any shot. Print is clean black on white.
- **Keys (Done 10):** 1 to 4, 5 (ignored until found), G, Escape, W, P and the arrows all work from the body.
- **Voice queue:** first tap on an option skips the welcome unmarked and speaks its own line; a blank first tap gets
  the welcome; Read speaks the current hint and later lines wait for it; mode and dilemma changes cut speech; Sound off
  queues nothing and Sound on queues the never-said welcome. `voice/lines.json` equals `allLines()` word for word.
- **Motion off:** leaves and branches appear at once; Play still steps at 1.2 s.
- **Contrast:** recomputed the spec pairs and the ones it left out (muted who tag on leaf/bloom/wilt fills 4.56 to 4.69,
  arrows on fills 4.26 to 4.61, focus ring on the hill 3.74): all pass.
- **SEL rules:** no text box, fictional ordinary dilemmas, no feelings scored, Blooming/Wilting describe branches only,
  notes.md names the school counselor. The notes' CASEL wording ("identifying solutions for personal and social
  problems", "anticipating and evaluating the consequences of one's actions") matches CASEL's listed examples;
  paraphrasing them is fine. No em dashes; "Curio Class" never shortened.

## Blocker

1. **Leaf text is not readable in the 680x425 preview with four or more branches (Done 9).**
   Repro: 680x425, plant A to D, all goals on, Next month. Every leaf is 64 px wide, 11 px, clamped to one line:
   "The ar...", "Coach...", "Ana...", "Bowling..." (frame full-680x425). With three branches it is two readable lines;
   four is the normal state. The spec asks for "a short title" at narrow sizes, and these are not titles.
   Fix: give each leaf a short title (two to four words, e.g. "Bowling is a blast", "Arm jams at the meet") and show it
   when the leaf is narrow, or drop the goal-mark row to a single summary arrow in tiny leaves so two lines fit. The
   same collapse happens at 375 wide.

## Should fix

1. **Focus drops to the body after five actions** (all repro'd with real keys at 1280x720):
   - graft found from the option cards (Enter on C, Tab, Enter on D): `buildOpts()` (src.html:878) rebuilds the cards;
   - "Next dilemma" on the choose card: the card hides with focus in it (src.html:780);
   - a focused Next month leaf, then ArrowLeft: the leaf becomes `visibility:hidden` (src.html:648-651);
   - the detail box close button (src.html:767);
   - a focused leaf, then key 1 pulls its branch up (the leaf is removed).
   Fix: after `buildOpts()` refocus the card with the same letter (or the new G card); after Next dilemma focus the
   new dilemma's picker card; when a focused leaf hides or is removed, move focus to that branch's crown or option
   card; after closing the detail, return focus to the leaf that opened it.

2. **The tool row falls below the fold at 1280x720 and 1366x768 once branches are planted.** Repro: Double Booking or
   Tablet Fund, plant A to D. At 1280x720 the row starts at y=720 (Make a call and Choose a branch fully off screen);
   at 1366x768 the second row (Choose a branch, Print, Clear) is at 770 to 814. With the graft found it is lower still.
   The "Planted · Pull up" tags add a line to every card in the wide layout. A real click on Make a call missed at
   1280x720 in my first run for this reason. Fix: in the `short` wide layout use the compact tag (absolute, top right,
   as body.compact .opt .tag already does), or move the tool row above the options.

3. **680x425 preview: the time slider and Play leave the screen once the graft is found** (5 option cards), and Play is
   cut off at the bottom even with 3 or 4 cards (frames full-680x425, p3). Tapping a leaf inserts the detail box at the
   top of the panel and pushes them further. STANDARDS "main controls visible without scrolling at every size".
   Fix: put the time box above the options in compact, and show the leaf detail as an overlay on the stage (or below
   the tools) rather than at the top of the panel.

4. **Side by side opens with both goal sets off, and the line then claims agreement.** Repro: enter Side by side. Line:
   "Standing best at Right away: A: A, B, C, D. B: A, B, C, D. Both goal sets agree here." and the "agree" clip is
   spoken on the first toggle. With one set empty it reads "B: A, B, C, G, D. ... different best branch." Judgment
   call: starting empty is defensible for a class that calls out goals, but the line must not draw a conclusion from
   no goals. Fix: until a set has a goal, show "Pick at least one goal for Goals A and Goals B." (and do not narrate
   agree/differ); or start A and B with one contrasting goal each so the first screen already shows the point.

5. **Make a call with no goals on always says "You called it."** Repro: plant A to D, no goals, Make a call, flag A,
   Next month: "You called it." plus the chime (every branch ties at 0). Fix: disable Make a call while no goals are on,
   or report "Turn on a goal to see which branch stands best." instead of a result.

6. **The Tablet Fund look-back gives the graft away.** "Option D cost Nia the fair. What did combining it with C
   change?" shows on the choose card whichever branch was chosen, including before the graft is found, so it names the
   graft pair. Repro: Tablet Fund, plant A to D, Next month, Choose a branch, pick B. This is spec content, so flag it
   to the integrator: reword so it works for any branch and spoils nothing (e.g. "What did the branch you chose cost
   Nia, and was it worth it?"), and re-record the line.

7. **At 760 and 375 wide no control is on screen with the tree, and a tapped leaf's text appears off screen.** At
   760x900 the stage is 720 px tall and the whole panel is below it; at 375 the panel starts about 630 px down. Leaves
   collapse to two words there, and tapping one writes the full text into the panel, out of sight. This follows the
   collision-lab stack pattern, so it is not a blocker, but for this tool the leaf tap is the only way to read the
   text. Fix: shorter stack stage (about 0.9 x width), show the leaf detail as a sheet over the stage in stack, and put
   the time box first in the stacked panel.

## Nits

1. The hint stays "Now slide time forward..." at Next month and after a call result, so Read speaks a stale line.
   Use a Next month hint (e.g. the choose nudge, or the result line) when t = 2.
2. In the short wide layout the setup paragraph is moved below the slider (src.html:93); the spec puts it under the
   picker, and it is the first thing to read for a new dilemma. Consider a one-line setup under the picker.
3. The detail close button is 32x32 (src.html:149) and the slider track 30 px (24 px compact): under 44 px.
4. The choose card sits over the chosen branch's own Next week leaf (frame ch1). Nudge it off the chosen column.
5. At 680 and 800 wide in Side by side the "Graft" knot label touches the sign, and the Swap button is below the fold.
6. At 375 wide the crown badges ("Blooming") overlap their neighbors (frame n375-full).
7. Partial plantings: with only A and D (or A and B, A and G) planted and "Stay in with the group" alone, A ties for
   best at Next month, so a call on A reports "You called it." The spec's guarantee is about the full tree, so this is
   within spec; worth knowing if a teacher asks.
8. The spoken Surprise line says "A different branch is" even when the screen names two tied branches. Fine as is;
   "A different branch is standing best" could become "Other branches are..." for ties if a second clip is cheap.

## Not checked

- Recorded clips (none yet in this draft); re-check clip timing after the voice lands. `$80`, `$150`, `$35` and "at 2"
  are in spoken setups: listen that the casual-peer clone reads them as dollars and a time.
- Real Chrome print dialog (checked with print media emulation and the built print block only).

## Re-verify

**Verdict: FIX** (0 blockers, 1 should fix, 4 nits). Every earlier finding is fixed except nits 2 and 7 (left on
purpose, still present, accepted), and nothing that passed before has regressed. One state the first pass did not try
still shows the old blocker's symptom: Who it touches in the preview.

Checked cold on a fresh draft bundle (`CURIO_DRAFT=1 python scripts/bundle_tool.py decision-tree`, 562 KB, art and all
28 clips in, under 2 MB) in muted headless Chrome on private ports (9971 devtools, 9191 for the 375 iframe host), with
real held clicks and real keys, at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 760x600 and
375x812 (iframe host), in all four dilemmas with four branches and with the graft.

### Earlier findings, re-checked

- **Blocker 1 (leaf text at 680x425 and 375): fixed.** With A to D planted, all goals on, Next month, every leaf shows
  its short title or its full text, at 11 px or more, in every dilemma at 680x425 and 375 (and with the graft). Measured
  the clamp on every leaf: one clipped title in 64 frames (nit 2). The short titles match spec.md word for word and are
  all two to four words.
- **Should fix 1 (focus to body): fixed.** With real keys: graft found from the option cards lands on the new G card;
  Next dilemma lands on the new picker card; a focused Next month leaf plus ArrowLeft lands on its crown; the detail
  close (now 44x44) returns focus to the leaf that opened it; key 1 on a focused leaf, key 2 on a focused crown and key
  3 on the focused G card land on an option card; Choose a branch and Make a call turning disabled hand focus to the
  next tool; Escape and Back to the tree land on Choose a branch; Clear tree and mode switches keep focus. A 60-key Tab
  walk never reaches body, and panel controls come before the leaves.
- **Should fix 2 (tool row at 1280x720 and 1366x768): fixed.** Every option card, chip, the slider, Play and all six
  tools are on screen in all four dilemmas, with and without the graft, at 1280x720, 1366x768 and 1920x1080 (Tablet
  Fund with graft and Who on at 1366x768: lowest tool at 624 of 768).
- **Should fix 3 (680x425 slider and Play): fixed.** The time box now sits first in the compact panel and the leaf
  detail is a card over the stage (measured: it never covers the tapped leaf at 680, 800, 1000 or 1280; in the panel at
  1920x1080). See nit 1 for what moved below instead.
- **Should fix 4 (Side by side empty goal sets): fixed.** Opens with "Pick at least one goal for Goals A and for Goals
  B." in the line and the hint; with one set on, the same line and the sbspick clip, no agree or differ; with both on,
  "Same choices, different goals, different best branch." and the differ clip; Swap swaps.
- **Should fix 5 (Make a call with no goals): fixed.** The button is disabled with no goal on (and `callBtn` does
  nothing); turning every goal off after the flag gives "Turn on a goal to see which branch stands best." at Next month.
- **Should fix 6 (Tablet look-back spoiler): fixed.** Spec, src and lines all read "What did the branch you chose cost
  Nia, and was it worth it?", newly recorded.
- **Should fix 7 (760 and 375 stack): fixed.** At 760x900 the stage is 640 px and the slider and Play show with the
  tree; at 375 the stage is 380 px with the time box right under it; a tapped leaf opens a card over the stage, next to
  the leaf and not covering it.
- **Nits:** 1 fixed (at Next month the hint is "That's next month. Choose the branch you'd go with.", after the call
  result when there is one); 3 fixed (44 px close and slider); 4 mostly fixed (nit 3 below); 5 fixed (Swap joins the
  time row at 680 and 800, the Graft label clears the sign); 6 fixed (375 crowns fit, no overlaps measured); 8 fixed
  (tied misses say "Surprise. Other branches are standing best by next month."). 2 and 7 are still there, on purpose.

### Done when, re-run

1. Setups, signs, goals, options, every leaf's text, who, code and short title, the graft pairs and the look-back
   questions read out of the page equal spec.md (parsed and diffed: no differences).
2. Standings recomputed in Python from the spec codes: all four goals on, R/W/M equal the worked check (Booking C,G / G /
   D; Quiz G / B / B; Tablet C,G / B,C / B; Game G / B,C,G / C). The tool's own tally and best lists equal mine for all
   16 goal sets x 3 times x 4 dilemmas, with and without G (192 cases, 0 mismatches). Quiz Photo A is never best or tied
   at Next month under any of the 15 goal sets, with or without the graft.
3. No goals: every badge reads "Pick a goal" and no marks show; one goal on gives one mark per leaf at once.
4. In each dilemma every wrong pair gives the miss line (the clue line after two misses), only the listed pair grows G,
   and pulling up a parent removes G.
5. 240 calls (4 dilemmas x 15 goal sets x 4 flags) all report the right line, ties counted as called.
6. Side by side: two trees, ghost bud until the graft is found, the line updates, Swap swaps.
7. "Dev chose: Go to practice. Don't say anything to Ana.", the three leaves and the look-back, no grade.
8. The only input is the range slider; after a session that toggles Motion, Sound, Who and both modes, localStorage
   holds only `curio-motion`; no external `src`, `href` or `url(http`. Print (print media): black on white, goals on,
   each branch with its standing, leaves, who and marks.
9. Sizes: above, plus the should fix below.
10. Keys 1 to 5, G, W, P, arrows and Escape work; voice below.

### Voice, Motion, console, art, words

- All 28 `allLines()` entries equal `voice/lines.json` and have a clip; durations are sane (0.83 s to 9.68 s, 45 to 71
  ms per character). Transcribed every clip locally (facebook/mms-1b-all): the Tablet setup says "eighty dollars", "one
  hundred and fifty dollar", "thirty five dollars"; the Booking setup says "Saturday at two"; the five new clips
  (surprise2, callgoal, month, sbspick, the Tablet look-back) say their lines. Only real clips played, never the browser
  voice.
- Queue, with held clicks and a play/pause log: a blank first tap plays the Grow welcome; Side by side its welcome once;
  back to Grow, no repeat; a first tap on an option skips the welcome and plays its own line; Read restarts the current
  hint, and a chip line queued during Read waits for it to end; Kai then Nia cuts Kai's setup and plays Nia's in full
  (9.7 s); Sound off speaks nothing and Sound on queues the never-said welcome; Read as the first tap reads the hint
  with no welcome after; a call through Play speaks one result line.
- Motion off: transitions at 0, Play still steps at about 1.2 s (1209 and 2407 ms; 1219 and 2412 with Motion on).
- Console: no errors, warnings or exceptions in any frame (the only 404 was my own host page's favicon).
- bg-hillside: the bundled webp is candidate c2 (mean pixel difference 1.8 of 255): open sky, rolling hills, a tree line
  at the right edge, no people, animals, buildings or lettering. It sits under the paper overlay and the bands; leaves,
  crowns and the sign read clearly over it at every size.
- Words: no em dashes in src, notes, lines or the bundle; "Curio Class" only. The short titles carry their leaf's
  meaning (nit 4 for two that lose the downside).

### Should fix

1. **Who it touches in the 680x425 preview and at 375 cuts most short titles to one word.** Repro: 680x425 (or the 375
   host), any dilemma, plant A to D, all goals on, Next month, press W. The who line takes the title's second line: 9 of
   12 leaves clipped in The Double Booking, 11 of 12 in The Quiz Photo and The Tablet Fund, 8 of 12 in The New Game
   ("Never...", "Everyone...", "Caught...", "Kids guess..."). Same counts at 375. Fine at 800x500 and up and at
   760x600. This is the old blocker's symptom in a state the first pass did not try, and Who it touches is one of the
   notes' talk prompts. Fix idea: when Who is on in a narrow leaf, use the one-row arrow marks (the `ao` layout) to free
   a line, or shorten the who line to its first name plus "+1", so the title keeps two lines.

### Nits

1. 680x425: option cards C and D are cut by the bottom edge in The Double Booking and The New Game (bottoms 436 to 451
   in a 425 box, G at 484 to 499 once found); about 30 px of each stays visible and clickable. The tool row (Graft, Make
   a call, Who it touches) is below the fold at 680x425 and 800x500, and partly at 760x600 and 1000x625 with the graft.
   Done 9 does not ask for the tools, and the G and W keys reach them.
2. 680x425, The New Game, four branches: A's Right away title "Great gaming night" clamps to "Great gaming..." (Who off).
3. The choose card now sits beside the chosen branch at 1280 and 1366 but still overlaps a sliver of it (largest at
   1366x768: about 1100 square px of B's Next week leaf). At 800 and 680 it is centered over the chosen column.
4. Two short titles keep only the upside of a mixed leaf: The Double Booking A Right away "Bowling is a blast" (the team
   waits) and B Right away "Practice goes well" (Ana keeps looking at the door). With no goals on, the title alone reads
   as a clean win; the tap shows the full text. Something like "Team waits for you" and "Ana waits at the door" would
   keep the point.

## Re-verify 2

Checked cold on a fresh draft bundle (`CURIO_DRAFT=1 python scripts/bundle_tool.py decision-tree`, 563 KB) served on a
private port (8967) in muted headless Chrome (devtools 9631, own profile), at 680x425, 800x500, 1000x625, 1280x720,
1366x768, 1920x1080, 760x900, 760x600 and 375x812 (iframe host): every dilemma, four branches and with the graft, Who
off and on, Next month (144 measured frames), plus the choose card for every branch in every dilemma at every size
(410 frames) and real held clicks for the choose flow. Every leaf's title was measured for clamping (visible text vs
full title), every leaf for content cut by its height, and every leaf and crown pair for overlap.

### Claimed fixes

- **Should fix 1 (Who it touches at 680x425 and 375): fixed for four branches.** With A to D, all goals, Who on, Next
  month: 0 clamped titles in all four dilemmas at 680x425 and at 375 (was 8 to 11 of 12). The who line shows the first
  name plus a count in narrow leaves ("Ms. Ortiz +2").
- **Nit 1 (cards C and D cut at 680x425): fixed.** Every A to D card is fully on screen at 680x425 in all four dilemmas
  (lowest bottom 415). The G card is still partly cut once found (see nit 2 below). The tool row stays below the fold
  at 680 and 800, as accepted before.
- **Nit 2 (New Game A Right away title): fixed.** The title is now "Gaming night" and shows in full at every size.
- **Nit 3 (choose card over the chosen branch): fixed, but see should fix 1.** Over 288 frames (8 sizes, 4 dilemmas,
  every branch incl. G) the card never overlaps the chosen branch's crown or leaves (0 square px in every frame).
- **Nit 4 (Booking titles): fixed.** A Right away "Team waits for you", B Right away "Ana waits at the door". All 60
  short titles and who tags read out of the page equal spec.md (0 differences).

### No regressions found

- 1000x625 and up, 760x900 and 760x600: 0 clamped titles, 0 cut leaves, 0 leaf or crown overlaps in every frame,
  Who on or off, with or without the graft; smallest leaf text 11 px (680, 375), 12 to 15.5 px elsewhere.
- Option cards, chips, slider and Play on screen at 1280x720, 1366x768 and 1920x1080 in every state, and all six tools
  too.
- Side by side (Quiz Photo, graft found, Goals A and B differ): the line reads "Standing best at Next month: A: D. B:
  B, G. Same choices, different goals, different best branch." at 680, 800, 1366 and 375; Swap on screen at 680 and
  800.
- `allLines()` equals `voice/lines.json` (28 lines, all with clips). No em dashes in src, spec or the bundle; "Curio
  Class" never shortened. No console errors or exceptions in any frame (only my server's favicon 404).

### Who it touches plus the graft (the state the builder says still clips)

Confirmed, and judged acceptable as a nit, not a should fix. It needs both an opt-in toggle and the found graft, at
the preview or phone size only; the title keeps its first words with an ellipsis, at 11 px, and a tap shows the full
text. Counts of 15 leaves at 680x425: Booking 2, Quiz 5, Tablet 5, New Game 4 (375: 2, 5, 7, 4). Nit 1 says where it
hurts most.

### Should fix

1. **The choose card is a narrow scrolling column at 680x425 and 375, with its buttons and often its question out of
   sight.** The card now sits in the free side beside the chosen branch, so when the chosen branch is in the middle it
   is only 156 to 192 px wide. Measured content vs box height at 680x425: Booking B 524/343, Quiz G 621/343, Tablet B
   470/343; "Back to the tree" and "Next dilemma" are both below the card's visible area in 13 of 20 cases at 680x425
   and 10 of 20 at 375 ("Next dilemma" alone in most of the rest), and the look-back question is cut mid-sentence (frames c3-680-d1-G: "Kai chose: Study / like
   normal, and / tell Ms. Ortiz / without naming / anyone." at three or four words a line; c3-375-d0-B). Also at
   800x500 and 760x600 with the Quiz Photo graft chosen. The question also shows in the hint and focus lands on "Back
   to the tree" (which scrolls the card), so it works, but a touch user has to scroll inside a 160 px box to find the
   buttons. Done 7 card at two of the standard sizes. Fix idea: when the free side is under about 260 px, let the
   card cover the dimmed columns on the wider side (and at most the chosen branch's Right away leaf), or fall back to
   the old centered card there; keep the side placement where it fits (1000 and up, where it never scrolls).

### Nits

1. Who on plus the graft at 680x425 and 375 (above): the cut word is sometimes the point of the leaf. Tablet Fund B
   shows "Fund reaches..." for both Next week and Next month (the $90 and $110 are lost), New Game B and C both show
   "Good grade,..." at Next month, Quiz D Right away "Kids guess it's...". If cheap: in a tiny leaf with Who on, drop
   the who line to the tap only, or move the person count into the crown, so the title keeps its lines.
2. 680x425 with the graft found: the G card sits at 388 to 432 (Quiz, Tablet), 402 to 446 (New Game), and 417 to 461
   in The Double Booking, where only its "Planted · Pull up" tag (8 px) is on screen. Key 5 and the panel scroll reach
   it.
3. 375, The Tablet Fund, four branches, Who off: B Next month clamps to "Fund reaches..." (the only clamp with Who off
   in 144 frames).

**Verdict: FIX** (0 blockers, 1 should fix: 1. the choose card is a narrow scrolling column with its buttons out of
sight at 680x425 and 375 when the chosen branch is in the middle).

## Integrator fix (Re-verify 2 should-fix 1)

The choose card now sits beside the chosen branch only when the free side is at least 300 px wide; otherwise it is centered (it lists the chosen branch's three leaves itself). Its button row is sticky at the card's bottom edge, so both buttons stay in view when a short card scrolls. Rechecked with the re-verify's own 100-frame choose-card sweep (all dilemmas, every branch with the graft, at 680x425, 375 in the host, 800x500, 760x600 and 1280x720): 0 frames with a button out of view, narrowest card 312 px. At 375 the look-back question can scroll under the buttons; it is also shown in full below the stage. Nits left as they are.
