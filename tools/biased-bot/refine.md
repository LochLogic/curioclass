PASS
Counts: blockers 0 (general 0, family 0), should fix 9 (general 8, family 1), polish accepted 11

# biased-bot: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C), refine/sensitivity.md (SE, PASS).
All 8 Done-when pass in every lens. The Teaching lens rebuilt the results from the spec in Python (all 1,330 jar
settings swept) and Craft's `checkTable` reproduces the whole table: no number is wrong. The sensitivity agent
passed the Room 9 framing and the Gender Shades note.

## Should fix
1. **The Room 9 jar is empty when the tool sends students to it** (T-S1, P-1, SE1; general). After a run the line and
   hint say "Tap a room's jar to see how its students write" (notes step 3: "Tap the Room 9 jar"), but Room 9 starts
   at 0 cards, so the viewer shows "This jar is empty" and the long-flag sentence ("Lots of people learn to write 1
   with a long flag...") never shows. Show each room's writing from its students (the lunch line), not only from the
   jar's cards, so Room 9's writing and that sentence are always reachable from the first run; keep the "normal way
   to write" sentence wherever Room 9's writing first shows. The same goes for any room whose jar is empty.
2. **The hint after a run never names the next experiment** (T-S2, P-2; general, BR1 lesson). It returns to "Press Run
   the lunch line. Predict..." while the voice points at the jars. The hint follows the state: after the first run,
   look at the jars; after looking, try more Room 12 cards; after that, try Room 9 cards. Pick by `V.heard`.
3. **One taught card changes nothing, with no reason given** (T-S3, P polish; family:ml-lab). One card is one of three
   votes, so the first "It's a 1" leaves the read wrong after "Bitsy learned your card". Keep kNN honest: say why on
   screen ("Bitsy looks at the 3 closest cards. Yours is 1 of 3 votes. Teach it once more.") and show the three
   nearest cards for that read. Note it in docs/families/ml-lab.md if the vote view is an engine part.
4. **"Every room got the right lunch. Bitsy learned from everyone." is false where it plays** (T-S4, P-4; general).
   It plays at 15/6/0 with Room 3's jar empty, and with only the student's own cards. Say what is true ("Every room
   got the right lunch this time.") and keep "learned from everyone" for when every room has cards. Change the
   spec's line to match.
5. **A first tap on Run skips the welcome and story for good** (P-3; general). The likeliest first tap leaves ~27 s
   of silence and a non-reader never hears the premise. Use `welcomeAfter` (or an equivalent) so the story comes
   once the run's own line is done.
6. **Results below the fold in small windows** (P-5; general, BR1 lesson). After a run the room bars are below the
   fold at 680x425 and 800x500 (Room 9's bar hidden at 800x500); at 375 they sit in a nested scroll with no cue.
   Keep the results, Room 9 first, in view after a run at every size.
7. **Writing mode stacks at preview sizes** (P-6; general). At 680x425 and 800x500 the pad and "What Bitsy sees"
   stack and a read scrolls the drawing out of view; at 375 the look-alikes the hint names are below the fold. Side
   by side in short landscape boxes (STANDARDS), and the look-alikes in view.
8. **Focus lost at a jar's limit** (C-1; general, BR1 lesson). src.html:85 sets the real `disabled` on the focused
   Fewer or More at 0 or 30; use `aria-disabled` as Train and Run do.
9. **Re-tapping the current mode cuts the welcome for good** (C-2; general). src.html:101 `setMode` hushes even when
   the mode doesn't change. Do nothing when the mode is unchanged.

## Polish accepted
10. **Engine fix in kit/ml-lab.js** (C polish, the builder's own engine request; family:ml-lab). Approved: `host()`
    skips drawing at zero size and draws on the first real size; groupBars clamps widths at 0, takes an empty-state
    text (no "0 of 0 right lunches" three times before a run) and a size option. Then drop the off-screen parking and
    the `font-size:11px!important` override. Update docs/families/ml-lab.md (or the family section in
    tools/teach-the-robot/spec.md) in the same change, and confirm teach-the-robot and leaf-sorter-ai look and behave
    the same (bundle each and compare frames).
11. Teaching a card shows which jar it went into (T-N2).
12. The empty-jar viewer doesn't say the same thing twice (T-N1).
13. notes.md: "one Room 9 card isn't enough, two are" holds only with Room 12 at 15 and the others empty; say so (T-P2).
14. notes.md: the long-flag 1 is standard in much of Europe and Latin America, so some students may write it; invite
    them to teach Bitsy, never ask who writes like Room 9 (SE2).
15. notes.md: the Gender Shades numbers (up to 34.7% vs at most 0.8% error) and the PMLR link (SE3).
16. notes.md: a talk question for the 0 / 15 / 0 run, "Does Room 12 write wrong now?" (SE4).
17. spec Sources: Gender Shades measured the gaps between groups; it did not see the companies' training data (SE5).
18. art/prompts.json: the cafeteria-counter entry says no people and `"people": false` (SE6).
19. The tray and sticker don't sit on Bitsy mid-run, and "− Fewer" doesn't wrap (C).
20. The Play lens's other polish items that touch only what the student sees, as the builder judges (list them in
    the handoff).

## Spec open questions (not for the builder)
- Predict: a way to record the class's guess before a run (T-P1). Adds to the spec.

## Settled calls
- The spec's lines 4 and the Try Your Writing welcome name a control that is disabled at that moment (the builder's
  own flag). BR1 lesson wins: reword them so the line names the step that enables the control first ("Pick the
  cards, then press Train Bitsy"), and change the spec's wording to match.

## Exit check, round 1

Cold check, 2026-10-28. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py biased-bot`, 194 KB (no clips recorded
yet; browser voice). All driving with `scripts/drive.py`, held clicks (0.12 s), Chrome on ports 9930 and 9932, 375
through `drive.py --host 9931` (host.html deleted after). Frames and logs are in the exit-check scratch folder (s1 to
s10). No console errors, warnings or exceptions in any shot (the only log line was the host page's own favicon 404).

### Items
1. PASS. Run, Skip, tap the Room 9 jar (`i1-room9-after-run`; `i12-empty9` before any run; `h375-view9`): the viewer
   shows Room 9's ten lunch cards grouped 1, 4, 7 and "Lots of people learn to write 1 with a long flag and 7 with a
   line through it." with the jar at 0.
2. PASS for the path the item names (`i2-hint-path`, hint log): after the run "Room 9 got wrong lunches. Tap the Room 9
   jar...", after Close "Try more of the same writing. Press More under Room 12...", after the 30 / 0 / 0 run "More of
   the same did not help. Try More under Room 9, then Train Bitsy.", at all 10 "Every room got the right lunch. Use
   Fewer and More...". The hint changes at once on each step. New item 21 below covers the step after Room 9 at 3.
3. PASS. A flagged 1 at the start reads 4; after one "It's a 1" the look-alikes show My cards (vote 1) and two Room 12
   cards (vote 4), the note says "Yours is 1 of 3 votes. The other two votes still win." and the hint "Press It's a 1
   once more." (`i3-teach-once`); a second teach reads 1 (`i3-teach-twice`). Same at 375 (`h375-wrteach`). The family
   doc notes it.
4. PASS. 15 / 6 / 0 speaks "all" and not "represented" (`dw3` log); 15 / 15 / 15 speaks both (`i4-represented`). Spec
   line 6 matches.
5. PASS. First tap on Run (`v3-run`): the story is spoken at once, then "Watch the lunch cards, or press Stop or Skip to
   results." When the run is skipped first, the running line drops as stale and the results follow (`dw1`).
6. PASS. After Run and Skip the Room 9 first score strip is fully in view at 680x425, 800x500, 1000x625, 1280x720,
   1366x768, 1920x1080, 760x1000 (`res-*`) and 375 (`h375-res`), with no page scroll.
7. PASS. After a read the pad and "What Bitsy sees" sit side by side and the three look-alikes are in view at every
   size (`wr-*`: the grid's left edge is right of the pad at all seven sizes; `h375-wrread`).
8. PASS. Six held clicks on Room 12's Fewer down to 0: focus stays on `fewer-12`, `aria-disabled="true"`, not
   `disabled`; six Enter presses on More up to 30: focus stays on `more-12` (`i8-focus-limit-click`, `-keys`).
9. PASS. Three taps on Lunch Line 1.5 s apart: the story and the welcome are both spoken, nothing hushed
   (`i9-retap-mode`).
10. PASS. Engine: `host()` returns without drawing and resets W and H at a zero box, and draws on the next real size
    (bars redraw after Lunch, Writing, Lunch: `panel-1366`, aria-label with the numbers); groupBars clamps `bw` and the
    fill share at 0, shows `empty` ("Room scores appear here.", `def-1366x768`) and takes `size`; the off-screen
    parking and `font-size:11px!important` are gone from src.html. Doc against code, line by line: the signature
    `{names, glyphs, order, unit, empty, size}` matches; "empty ... when no group has tested items" matches
    `!keys.some(k => G[k] && G[k].n > 0)`; "size ... minimum 10, scales captions and row spacing" matches
    `Math.max(10, O.size)`, `factor` on rowH, the glyph radius and the caption offset, caption `size - 1` (minimum
    10); "omitted options preserve the original 13 px labels, 12 px captions and layout" holds (size 13, factor 1,
    `lab` is the old formula, caption 12, offset 14); the host bullet matches. Models, seeds and ties are untouched
    (`checkTable` reproduces the spec table exactly, `dw-table`). teach-the-robot: bundled from two scratch copies,
    one with HEAD's ml-lab.js and one with the current one (its own files untouched; the two bundles differ only in
    the engine); first screen, three teaches, a Mystery read and a parade at 1366x768 and 680x425 give identical hint,
    state and panel text, and identical frames except one card's glow caught at a different animation phase (parade
    frame). It calls only `knn` and no views, so the change cannot reach it. leaf-sorter-ai has only a spec here.
11. PASS. "Added to My cards: 1. Label: 1." under the look-alikes, and the My cards line pulses (`i3-teach-once`).
12. PASS. The empty Room 9 viewer says "The jar has 0 training cards." and "Close this view and use More to add
    training cards." (`i12-empty9`), no repeat.
13. PASS. notes.md says the one-versus-two claim assumes Room 12 at 15 and Room 3 at 0.
14. PASS. notes.md: Europe and Latin America, invite students to teach Bitsy, never ask who writes like Room 9.
15. PASS. notes.md: 34.7% against at most 0.8%, with the PMLR link.
16. PASS. notes.md talk question "Does Room 12 write wrong now?" after training only on Room 9.
17. PASS. Spec Sources: Gender Shades measured the gaps without access to the companies' training data.
18. PASS. prompts.json says "no people" and `"people": false`.
19. PASS. Mid-run on a mix-up card (card 3, Room 9): the tray and the "Wanted pasta" sticker do not overlap Bitsy at
    680x425, 800x500, 1366x768 and 1920x1080 (`i19-midrun-*`, bounding boxes); Fewer is one line at every size.
20. PASS on what the Play lens list asked: story first then the short welcome, a larger sticker and x marks on wrong
    queue cards, mix-up wording "Room 9: 4 cards wrote 1 (pasta), got tacos.", no "0 of 0" bars, bigger numbers at
    1920, art kept to its aspect (`xMidYMax slice`), a Bitsy in Writing, the keyboard ring only after a key.
Settled call: PASS. Line 4 is "Pick the cards, then press Train Bitsy." (Train is enabled at that moment) and the
Writing welcome no longer names a disabled control; the spec's wording matches.

### Done when
1 PASS (10 / 10 / 6, Mix-ups "Room 9: 4 cards wrote 1 (pasta), got tacos.", `dw1`). 2 PASS (30 / 0 / 0 gives 6,
"same" spoken, `dw2`). 3 PASS (15 / 3 / 0 gives 6, 15 / 6 / 0 gives 10 everywhere, "all" spoken, `dw3`). 4 PASS
(0 / 15 / 0 gives 6 / 6 / 10 with 1s read as 7, "flip" spoken, `dw4`). 5 PASS (Run `aria-disabled` after More,
results grey with "(old)", `dw5`). 6 PASS (a stick 1 reads 1, `v1-stick1`; the grid matches the drawing; look-alikes
carry badges; teaching changes later reads). 7 PASS (`dw7-gray`: circle, square, triangle with names). 8 PASS (Run,
Train and the jars on screen at 680x425, 1366x768, 760 wide and 375, no scroll).

### New finding
21. **should fix, general.** src.html:116, `includeHow`. After a run where Room 9 has some cards and is still at 6,
    the hint reads "Try examples from the other rooms. Use More under a room whose jar is empty." The only empty jar
    is then Room 3, which never helps Room 9 (spec table: 15 / 0 / 30 gives 6), and at 15 / 3 / 3 no jar is empty but
    the hint still says so (`f-includeHow`: counts 15 / 3 / 3, scores 10 / 10 / 6, that hint). A solo student who
    follows the hint goes the wrong way at the tool's key step (BR1 lesson: the hint names the next control and
    matches the state). Better: while Room 9 is under 8 and has cards, "Room 9 still got wrong lunches. Press More
    under Room 9 again, then Train Bitsy."; keep `includeHow` for the 0 / 15 / 0 case, worded for the rooms that are
    actually empty.

### Polish and nits noticed (not blocking)
22. **polish, general.** An event line waits behind a how line already playing: draw then Read at once, and "Bitsy
    read a 4." is spoken about 4 s after the tap, behind "Press Bitsy, read it!..." (`v1-read5`, `v1-stick1`); the
    fifth "Your card went into My cards." came 5.4 s late behind the `taught` line (`v1-teach5`). The screen updates at
    once and nothing is stale, but cutting a how line when its own control is pressed would keep the voice in step.
23. **nit, family:ml-lab.** docs/families/ml-lab.md: the biased-bot row leaves out `MLLab.glyph` and `train('knn')`,
    which the tool also calls.

### Regressions looked for
- Sizes (`def-`, `res-`, `wr-` at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000; `h375-def`,
  `h375-res`, `h375-view9`, `h375-wrread`, `h375-wrteach`): no button under 44 px; Run, Train, the jars, their buttons
  and the hint on screen; hint never clipped; no page scroll; nothing focused on load. At 1366x768 the panel's last
  privacy line sits inside the panel's own scroll (it scrolls).
- allLines() against voice/lines.json: 69 and 69, identical in order and wording.
- Motion off (`calm-midrun`, `calm-train`): no running animations, training still takes 0.6 s and cards 0.9 s each;
  Motion on: no infinite animations (`motion-inf`).
- Saving and reset (`reset`, `reset-reload`): after teaching, a run and the viewer, Start over gives jars 15 / 0 / 0,
  My cards 0, a clear pad, "No run yet.", the strip hidden, focus kept on Start over; storage holds only the kit's
  `curio-motion`; no cookies; a reload has no My cards.
- Focus when controls rebuild (`focus-rebuild`): More, Train, Run, the teach buttons and Clear keep focus; Skip hands
  focus to Run; the viewer takes focus to Close and Escape returns it to the jar.
- Network: no resource requests in a full session (PerformanceObserver); no http URLs in the bundle besides the SVG
  namespace. Console clean in every shot.
- Words: no em dashes in src, notes, spec, lines, tool.draft.json, the family doc or the engine; "Curio Class" never
  shortened.

### Voice check (browser voice, Sound on, Motion on, held clicks)
| Line | Kind | Expected | Spoken |
|---|---|---|---|
| story (welcome) | how | once | 1 (stage tap, Tab, Run, Sound back on) |
| lunchWelcome | how | once | 1 |
| running | how | once in 5 runs | 1 |
| Room 12 / Room 3 / Room 9 totals | event | 5 in 5 runs | 5 / 5 / 5 |
| under | event | 5 | 5 |
| lookHow, moreSame | how | once each | 1, 1 |
| change (5 More) | how | once | 1 |
| ready (5 trains) | how | once | 1 |
| inspect (5 jar opens) | how | once | 1 |
| Bitsy read a 4 (5 reads) | event | 5 | 5 |
| readHow, teachHow | how | once each | 1, 1 |
| Your card went into My cards (5 teaches) | event | 5 | 5 |
| taught | how | once | 1 |
| same / all / represented / flip | event | once in their runs | 1 / 1 / 1 / 1 |
| writingWelcome | how | once | 1 |
| Read (5 taps) | read | 5, the hint | 5, each the current hint |

- Stale (`v2-stale`, `v2-stale2`, taps 0.2 s apart): the results and lookHow drop on the jar change or mode switch,
  writingWelcome plays only in Writing, no line plays after its moment.
- First tap: stage and Tab give the story within 0.15 s; Run gives the story then the running line; Lunch Line gives
  the welcome; Try Your Writing gives its welcome; Read speaks the hint only; Sound says nothing, and Sound off then on
  brings the story once (`v3-soundoffon`); More and a jar speak only their own line (the story comes with the first
  Run).
- Read: cuts the story and speaks the hint, with Sound off too; a mode change or Run right after Read starts its line
  at once (`v4-*`).
- Order: spoken lines follow the actions in every log.

### Gate
1 Done when: all 8 pass. 2 Standards: each code is taught by a solo action (changing sources and retraining; reading
results by room and inspecting Room 9; comparing outcomes by source; labeling a drawing and seeing the neighbors
change), as notes.md maps them. 3 Solo defaults: story card and welcome, hints name the next control, except item 21.
4 Sensitivity: refine/sensitivity.md PASS; nothing in its scope changed against it. 5 Open should fix: item 21.
6 Bundle clean, 194 KB, no console errors, no network. 7 Voice counts right. Gate fails on 5 only.

### Left open
- 21 (should fix, general): the `includeHow` hint once Room 9 has some cards. Narrow; the integrator may fix it and
  send this check back.
- 22 (polish) and 23 (nit): known, not done unless taken.

## Exit check, round 2

Cold check, 2026-10-28, the last round. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py biased-bot`, 190 KB
(194,636 bytes; no clips recorded, browser voice). All driving with `scripts/drive.py`, held clicks (0.12 s), Chrome on
ports 9930 and 9932, 375 through `drive.py --host 9931` (host.html deleted after). Frames and logs are in the exit-check
scratch folder exit-bb2 (`s1` sweep, `s21`, `s22`, `s22b`, `sz`, `h375`, `vc`, `dw`). Logs pair each held click's time
with the voice log and with each utterance's real start and end (a wrapper on `speechSynthesis.speak`). No console
errors, warnings or exceptions in any shot (the only log line was the host page's own favicon 404).

### Round 1 open items
21. PASS on the three named states. 15 / 3 / 0 (Room 12 / Room 9 / Room 3; scores 10 / 10 / 6): "Room 9 still got
    wrong lunches. Press More under Room 9 again, then Train Bitsy." (`h21-15-3-0`); following it (More under Room 9,
    Train, Run, Skip) gives 10 / 10 / 10 and "Every room got the right lunch..." (`h21-15-3-0-follow`). 15 / 3 / 3: the
    same hint, and following it gives 10 / 10 / 10 (`h21-15-3-3`, `-follow`). 0 / 15 / 0 (6 / 6 / 10): "Try examples
    from the other rooms. Use More under Room 12 or Room 3, then Train Bitsy.", both empty there; one More under Room
    12 lifts Room 12 to 8 and Room 3 to 7 (`h21-0-15-0`, `-follow`). The spec's hint paragraph matches. But the sweep
    of all 1,330 jar settings (`s1/sweep`) finds the same fault one step away: new item 24.
22. PASS. Draw, then Read at once: "Bitsy read a 1." takes the voice 2 ms after the tap and starts 0.2 s later,
    cutting "Press Bitsy, read it!" (`e22-read`). Five teaches at a 2 s pace: each "Your card went into My cards." is
    queued at its tap and cuts the how line playing (`e22-teach5`, `teach5-r0` to `-r2`). After a Skip during "Watch
    the lunch cards..." the first result starts 0.14 s after the tap (`runskip9`). Read still wins: a teach tapped while
    Read speaks waits behind Read and plays after it (`e22-readwins`, `e22-readwins2`: Read at 3.26 s, the card line at
    12.48 s; nothing cut Read). Events never cut events (a queued event keeps `cutHow` off). Items 25 and 26 are what
    the cut-in costs.
23. PASS. docs/families/ml-lab.md's biased-bot row now lists `rng`, `uni`, `MLLab.glyph`, `train('knn')`, `knn`,
    `evaluate` and `groupBars`.

### Round 1 items spot-checked
1 PASS (`h-view9` at 375 and `view9-*` at every size: Room 9's lunch cards and the long-flag sentence with the jar at
0). 2 PASS (log `vc/lunch`: lookHow after the first run, moreSame after Close, moreMissing after the 30 / 0 / 0 run,
moreRoom9 once Room 9 has cards, allHow at 10). 3 PASS (`wrread-*`, `h-wr`: one teach shows My cards vote 1 and two
Room 12 votes 4, "Yours is 1 of 3 votes. The other two votes still win.", hint "Press It's a 1 once more."). 4 PASS
(30 / 6 / 0 speaks "Every room got the right lunch this time." and not "represented"; 30 / 6 / 3 speaks "Every room has
cards in the training jars...", `vc/lunch`). 5 PASS when the story is left to finish (`e22-runwait`: story, then "Watch
the lunch cards..."); see 25. 6 PASS (`res-*` and `h-res`: the Room 9 first strip on screen at every size). 7 PASS
(`wrread-*` and `h-wr`: pad and "What Bitsy sees" side by side, the three look-alikes in view). 8 PASS (six held
clicks on Room 12 Fewer: focus stays on `fewer-12`, `aria-disabled="true"`, `disabled` false). 9 PASS (three taps on
Lunch Line 1.5 s apart: story and welcome both spoken, `vc/retap`). 10 PASS on the doc against kit/ml-lab.js: `host()`
returns at a zero box and resets W and H; groupBars takes `{names, glyphs, order, unit, empty, size}`; `empty` shows
when no group has `n > 0`; `size` has a minimum of 10 with `factor` on rows, glyphs and captions, caption `size - 1`;
omitted options give 13 px labels and 12 px captions. `checkTable` still reproduces the spec table exactly (`dw`).

### Done when
1 to 4 PASS (`dw`: checkTable gives 10/10/6, 10/10/6, 10/10/6, 10/10/6, 10/10/10, 10/10/10, 6/6/10 for the spec rows;
Mix-ups "Room 9: 4 cards wrote 1 (pasta), got tacos."; "same", "all" and "represented" spoken in `vc/lunch`). 5 PASS
(More after a run: Run `aria-disabled`, strip "(old)", "Old results. Pick cards and press Train Bitsy."). 6 PASS (a stick
1 reads 1; look-alikes and teaching as in 3). 7 not re-shot (badges and names unchanged). 8 PASS (sizes below).

### New findings
24. **should fix, general.** src.html:113 to 119, `nextHint`. Room 9 under 8 goes to `moreRoom9`, but Room 9 at 8 or 9
    falls through to `includeHow`. Swept: 22 jar settings, every one with Room 9 at 3 cards and either Room 12 at 6 or fewer or Room 3 at 6 or 9 (for
    example 15 / 3 / 6 gives 10 / 10 / 9 and 15 / 3 / 9 gives 10 / 10 / 8). There the hint says "Try examples from the
    other rooms. Use More under Room 12 or Room 3, then Train Bitsy." while Room 9 is the room still wrong; no amount of
    Room 12 or Room 3 fixes it, and one More under Room 9 does (15 / 6 / 6 and 15 / 6 / 9 give 10 everywhere). Reached
    in two taps from item 21's own 15 / 3 / 3 by trying More under Room 3 (`h21-15-3-6`: strip "Room 9 9 of 10", that
    hint; `h21-15-3-6-follow`: following it, 18 / 3 / 9, leaves Room 9 at 8). "under" is not spoken there either (it
    waits for under 8). Same fault as 21 (BR1: the hint matches the state). Better: send any Room 9 score under 10
    with Room 9 cards to `moreRoom9`, and keep `includeHow` for the states where Room 12 or Room 3 is the low room; the
    spec's "below 8" wording moves with it.
25. **should fix, general.** src.html:131 and 173, `cutHow` in `finish()`. The 22 fix cuts any how line playing, and
    the story welcome counts as one. Tap Run (the story starts, about 7 s), then Skip within those 7 s: the first
    result cuts the story, the story is already marked said and never comes back, and the story card left the stage at
    Run (`e22-runskip`: story from 1.34 s, Skip at 4.50 s, results at 4.51 s; same in `vc/lunch` and `vc/runs5`). This
    brings back round 1's item 5 (a non-reader never hears the premise) on a likely path, and BR1 says no line is lost
    at a 2 s tap pace. Better: never cut `story` (let results wait behind it, or queue it again), or cut only the how
    line whose step the tap just did.
26. **polish, general (kit voice).** When a how line was already speaking and an event cut it, headless Chrome left the
    event's utterance pending in 3 of 5 such runs: no start event, the queue held to the 4.8 s cap, then "interrupted"
    (`teach5`, `teach5-r0`, `-r1`; `-r2` and `runskip9` started at once). In those runs the first "Your card went into
    My cards." was logged spoken but stayed silent, and the next came 4.8 s after its tap. The cut (`cur.cut(); stop()`)
    followed at once by `say0()`'s own `stop()` and `speak()` may be the trigger; it may be headless only. Worth one
    check on a real Chrome with the browser voice before clips land.

### Regressions looked for
- Sizes (`def-`, `res-`, `wrpre-`, `wrread-`, `view9-` at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080,
  760x1000; `h-def`, `h-res`, `h-view9`, `h-wr`, `h-reset` at 375 through the host): no button or pad under 44 px, no
  page scroll, the hint never clipped; Run, Train, the jars and their buttons, the strip, the pad, Read and the teach
  buttons all inside the window; no overlapping controls (only the modal viewer over the header at 375); smallest text
  10 px (680x425 writing), 11 px elsewhere; nothing focused on load.
- allLines() against voice/lines.json: 70 and 70, identical in order and wording (moreRoom9 is the new line); longest
  118 characters.
- Motion off (`motionoff-midrun`, `motionoff-train`): no running animations mid-run or while training; cards still
  0.9 s each. Motion on: no infinite animations in any session.
- Reset (`reset-desk`, `h-reset`): after teaching, a run and the viewer, Start over gives 15 / 0 / 0, My cards 0, a
  clear pad, "No run yet.", the strip hidden, focus kept on Start over; storage holds only `curio-motion`; no cookies.
- Focus when controls rebuild: Train keeps focus through training, More keeps it, Skip hands it to Run, the viewer
  takes it to Close, a teach keeps it, Fewer at 0 keeps it.
- Network: no resource entries in any session; no http URLs in the bundle besides the SVG namespace.
- Words: no em dashes in src, notes, spec, lines, tool.draft.json, the family doc, the engine or this file.

### Voice check (browser voice, Sound on, Motion on, held clicks)
| Line | Kind | Expected | Spoken |
|---|---|---|---|
| story (welcome) | how | once | 1 per session (cut by an early Skip, item 25) |
| lunchWelcome | how | once | 1 (`vc/retap`) |
| running | how | once in 5 runs | 1 (`vc/runs5`) |
| Room 12 / Room 3 / Room 9 totals | event | 5 in 5 runs | 5 / 5 / 5 (`vc/runs5`) |
| under | event | 5 | 5 |
| lookHow, moreSame | how | once each | 0 (dropped as stale: the jar was tapped first), 1 in `vc/lunch`; lookHow 1 in `vc/runs5` |
| change (5 More) | how | once | 1 |
| ready (after Train) | how | once | 1 |
| inspect (5 jar opens) | how | once | 1 |
| Bitsy read a 4 (5 reads) | event | 5 | 5 |
| readHow, teachHow | how | once each | 1, 1 |
| Your card went into My cards (5 teaches) | event | 5 | 5 (logged; see 26) |
| same / all / represented | event | once in their runs | 1 / 1 / 1 |
| writingWelcome (Writing tab) | how | once | 1 (`vc/wwelcome`) |
| Read (5 taps) | read | 5, the hint | 5, each the current hint |

At a 2 s pace a jar change hushes the result lines still queued (stale, `vc/lunch`), as in round 1; given time to
finish, all five runs' results play in full.

### Gate
1 Done when: all pass. 2 Standards: unchanged since round 1, each code taught by a solo action. 3 Solo defaults: the
hints name the next control, except in item 24's states. 4 Sensitivity: refine/sensitivity.md PASS; nothing in its
scope changed. 5 Open should fix: 24 and 25. 6 Bundle clean, 190 KB, no console errors, no network. 7 Voice counts
right except the story lost to an early Skip (25). Gate fails on 5.

### Left open (to the integrator)
- 24 (should fix, general): `nextHint` sends Room 9 at 8 or 9 to `includeHow`. One condition.
- 25 (should fix, general): `cutHow` cuts the story welcome. One condition.
- 26 (polish): a speech engine stall after a cut, seen headless; known, not done unless taken.

## Integrator fix (24, 25) and close

Narrow check, 2026-10-28. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py biased-bot`, 189 KB (194,834 bytes; no
clips, browser voice). Driving with `scripts/drive.py`, held clicks (0.12 s), Chrome on ports 9930 to 9938 with its own
profile, 375 through `drive.py --host 9931` (host.html deleted after). Frames and logs are in the scratch folder exit-bb3
(`s1` sweep, `d24`, `s25`, `sz`, `h375`). No console errors, warnings or exceptions in any shot (the only log line was
the host page's own favicon 404).

24. **PASS.** Sweep in the page (`s1/sweep`): all 1,330 jar settings (0 to 30 by 3 per room, not all empty), scored with
    the page's own `training`, `LINE` and `MLLab.train('knn')` / `evaluate` (agrees with `checkTable` on all 8 spec
    rows), each hint read from the page's own `#hint` after setting the state and re-rendering. Hints: allHow 1,065,
    lookHow 120 (all Room 9 at 0), moreRoom9 117, includeHow 28; no other hint and no unknown text. Every includeHow
    setting has Room 9 at 10 (the 22 round 2 states, Room 9 at 8 or 9, now all give moreRoom9: 15 / 3 / 6, 15 / 3 / 3
    and 15 / 3 / 9 give moreRoom9). For all 117 moreRoom9 settings, pressing More under Room 9 repeatedly reaches Room 9
    = 10 before the jar is full, and never drops Room 12 or Room 3 from 10 on the way; from there the hint path ends at
    allHow in all 117. Following the hint from every one of the 1,330 settings (moreRoom9 and moreMissing: More under
    Room 9; lookHow: open the jar; moreSame: More under Room 12; includeHow: More under Room 12 or Room 3) reaches
    "Every room got the right lunch" in all 1,330: no setting points to a hint whose action cannot help.
    Driven with held clicks at a 2 s pace (`d24`): 15 / 3 / 6 (More 9, More 3, More 3, Train, Run, Skip) gives 10 / 10 / 9
    and "Room 9 still got wrong lunches. Press More under Room 9 again, then Train Bitsy." (`h24-15-3-6`); following it
    (More 9, Train, Run, Skip) gives 15 / 6 / 6 at 10 / 10 / 10 and "Every room got the right lunch this time." spoken
    (`h24-15-3-6-follow`). 15 / 3 / 3 gives 10 / 10 / 6 and the same hint (`h24-15-3-3`); one More under Room 9 gives
    10 / 10 / 10, "all" and "represented" spoken (`h24-15-3-3-follow`); a second More 9 keeps 10 / 10 / 10
    (`-follow2`). Focus ends on Run each time. Doc nit (not behaviour): spec.md:105 still says "still scores below 8";
    the code now sends any Room 9 score under 10 with Room 9 cards and a jar under 30 to this hint.
25. **PASS.** Fresh page, story not yet said (`s25`, utterance start and end from a wrapper on `speechSynthesis.speak`):
    - 2 s pace, Run at 1.33 s, Skip at 3.49 s: story 1.55 to 8.70 s in full, then "Room 12 got 10 right..." from 8.97 s,
      the other totals, "Some students got...", the lookHow hint (`r25-skip2`).
    - 0.5 s pace, Run at 1.35 s, Skip at 1.99 s: story 1.52 to 8.64 s in full, results from 8.91 s (`r25-skip05`).
    - The same in the item 21 / 24 drives (`d24`): Skip 2.1 s after Run, results wait for the story's end (7.4 s).
    Round 1 item 5 holds: Run left alone gives the story (1.45 to 8.53 s), then "Watch the lunch cards..." (8.87 to
    12.82 s), then the results (`r25-item5-runwait`). Item 22 holds: Draw then Read, "Bitsy read a 1." queued 2 ms
    after the tap and started 0.24 s later, the "Press Bitsy, read it!" how line cut (`r25-e22-read`); five teaches at a
    2 s pace, each "Your card went into My cards." queued at its tap and the how lines cut (`r25-e22-teach5`); Skip
    during "Watch the lunch cards..." (after the story) cuts it, first result 0.12 s after the tap (`r25-runskip9`); Read
    wins: Read at 3.25 s, the teach tapped during it waits and plays at 12.48 s, Read not cut (`r25-e22-readwins2`).
    Item 26 still seen headless: the first teach event in `r25-e22-teach5` was logged spoken but never started.
- allLines() against voice/lines.json: 70 and 70, identical in order and wording (`sz/lines`).
- Sizes: 1366x768 and 680x425 (`def-`, `res-`, `wr-`) and 375 through the host (`h-def`, `h-res`, `h-view9`, `h-wr`,
  `h-reset`): no page scroll, nothing under 44 px, nothing off screen, the hint never clipped, no overlaps (only the
  viewer over the header at 375, as before), smallest text 10 px (680x425 writing), nothing focused on load, no running
  animations at rest.

### New observation (outside 24 and 25)
27. **polish or should fix, integrator's call.** A second Run within the story still loses it: Run, Skip, Run, Skip at
    a 2 s pace (`r25-4tap2`: Run 1.34 s, Skip 3.49 s, Run 5.64 s) and at a 0.65 s pace (`r25-skip05b`). The second Run's
    `V.hush()` (src.html:177, `run()`) stops the story at about 4 s in; it is marked said and never comes back, and the
    new run speaks "Watch the lunch cards..." instead. Not the `cutHow` path that 25 fixed, and less likely than Run then
    Skip, but the same cost (the premise lost). Possible fix: let the welcome survive a Run hush, or queue it again if it
    was cut before its end.

### Gate
24 PASS, 25 PASS. Items 5 and 22 still hold. No should fix left open from rounds 1 and 2; 26 (polish, headless stall)
and the spec.md:105 wording nit are left to the integrator, with 27 above. Bundle clean, 189 KB, no console errors, no
network. **PASS.**

### Left open after close (integrator)
- 27 (polish, general): Run, Skip, Run inside the story's first 4 s hushes the story for good (`V.hush()` in `run()`). Three taps in 4 s; left for Final look.
- 26 (polish, kit voice): the headless speech stall (an event cutting a how line sometimes never starts); check once in a real Chrome.
- spec.md line 105 changed to "below 10" to match the code (integrator).
