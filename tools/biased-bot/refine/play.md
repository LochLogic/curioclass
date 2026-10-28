# Play lens: biased-bot

Played cold twice: as a grade 4 student alone at home (no teacher, can't read the screen well), and as a teacher
projecting Lunch Line to a class at 1366x768 and 1920x1080. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py
biased-bot` (177 KB, clean). Frames via `scripts/drive.py` (port 9972) and `--host` for 375; audit via
`scripts/audit_tool.py` (ports 9970-9971). No console errors in any shot (the only log line was the host page's own
favicon 404).

Frames looked at: default, end of a full run, mid-run (4 of 30), Writing default, Writing after a read, Room 9 viewer,
at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900; 375x812 (host) default, results, results
scrolled, Writing, Writing after a read, viewer; plus at 1366x768 a mix-up mid-run, Room 9 viewer at the start (empty
jar), all jars empty, all jars at 30, old results, stopped, grayscale results, Motion off run, a jittered mouse drag of
a flagged 1, the keyboard pen.

Checked and fine: Done when 1 (10/10/6, four "wrote 1, got tacos"), 2 ("same" spoken after Room 12 to 30), 3 (Room 9 at
3 still 6; at 6 all 10 and "all" spoken), 4 (Room 12 and Room 3 to 6 with 1s read as 7, "flip" spoken), 5 (Run
disabled and results greyed "Old results" after a jar change), 6 (a stick 1 reads 1, grid matches, look-alikes show
badges; a flagged 1 reads 4, two teaches flip it to 1, and three taught flagged 1s bring Room 9 to 10 in the lunch
line), 7 (panel badges and bars by shape and name in grayscale), 8 (Run, Train and jars on screen at every size). How
lines are spoken once ("change" once, then silent); event lines repeat per run. Keyboard pen draws. No sideways
scroll at any size.

## Blockers

None.

## Should fix

1. **The jar the voice sends you to is empty.** Lunch Line, `openViewer` (src.html:117) with the start jars. After the
   first run the voice says "Some students got the wrong lunch. Tap a room's jar to see how its students write." (it
   `needs` `#jar-9`). Room 9's jar starts at 0, so tapping it shows "This jar has no training cards yet. / This jar is
   empty. Press Close, then More to add cards." and nothing else: no Room 9 handwriting, and the one line that names
   the style ("Lots of people learn to write 1 with a long flag...") is replaced. The central discovery step dead-ends
   for the solo student in the room it matters for. Better: when a jar is empty, still show that room's writing (for
   example its 10 lunch-line cards, labeled "Room 9's lunch cards, not in the jar yet") with the flag sentence, then
   "Press More under Room 9 to put some in the jar." Seen: frame `view9-start` (1366x768); audit walk row 11.
   general.
2. **The hint doesn't change when a run ends.** `nextHint()` (src.html:72) returns `ready` after a finished run, so
   the panel and Read keep saying "Press Run the lunch line. Predict how many right lunches each room will get." on
   top of a 10/10/6 result, while the voice says to tap a jar. A student who presses Read after the run hears
   "predict" for a run that already happened, and the waiting moment never names the next real step. Better: an
   after-run hint keyed on the result ("Room 9 got wrong lunches. Tap a jar to see how each room writes, or change
   the jars and press Train Bitsy."; once all are 10: "Try training on just one room."). Seen: snapshot hint in every
   `res-*` shot; `v-seq-same` log. BR1 lesson "hint and voice". general.
3. **Tapping Run first means the story is never heard and nothing is said for 27 s.** `speaks:'#run'` (src.html:71)
   skips the welcome on a Run first tap, `run()` never queues the `running` how line, and the `story` line's `valid`
   (`!state.results`) is false from the first card on. Run is the big gold button the hint points at, so it is the
   most likely first tap: a non-reader gets no premise ("Room 12 trained Bitsy with their own handwriting") and no
   word until the results. Seen: `v-firstrun` held click on `#run`, `vlog` empty after 5 s; audit walk row 5 spoken
   blank. Better: on the first run speak the story (short) and "Watch the cards. Press Skip to results to jump ahead."
   once. general.
4. **"Bitsy learned from everyone" is said when it didn't.** `all` (src.html:52, 107) plays the first time all rooms
   reach 10. The usual route (notes step 4, Done when 3) is Room 12 15, Room 9 6, Room 3 0: Room 3 has no cards in
   the jar, so the line is untrue on screen (the jar says "0 cards") and blurs the talk point that Room 3's messy
   writing was never the problem. Seen: `v-seq-all-flip` log with jars 15/6/0. Better: "Every room got the right
   lunch. Bitsy needed to see Room 9's way of writing." (the line is from the spec, so the spec line changes too).
   general.
5. **The result of a run is below the fold in the preview and on a phone.** At 680x425 the panel ends at "Full run:
   10 cards per room." with no bars; at 800x500 only Room 12's bar shows (Room 9, the one that changed, is hidden);
   at 375 the results sit inside a 350 px panel that scrolls on its own inside the page scroll. Nothing tells the
   student to scroll. Seen: `res-680x425`, `res-800x500`, `h375-res` (and `h375-res-scroll` shows they exist).
   Better: in compact sizes put a one-line score strip on the stage after a run ("Room 12 10/10, Room 3 10/10,
   Room 9 6/10" with badges), or scroll the panel to the results when a run ends. general.
6. **Writing mode stacks pad and "What Bitsy sees" in short windows, so you can't compare them.** At 680x425 and
   800x500 the pad (300 px) and the grid stack in the stage; after "Bitsy, read it!" `readPad` scrolls the stage to
   the grid and the drawing goes off screen. At 375 the look-alikes the hint asks you to "compare" are below the
   page fold. STANDARDS: keep side by side with a compact layout in short landscape boxes. Seen: `wrread-680x425`,
   `wrread-800x500`, `h375-wrread`. Better: shrink the pad (about 200 px) and grid to sit side by side under 900 px
   wide. general.

## Polish

1. **Welcome and story say the same thing twice, and the action isn't last.** On a stage tap: "Good morning. Room 12
   trained Bitsy to read lunch cards with their own handwriting. Press Run the lunch line..." then 8 s later "Room 12
   built Bitsy to read lunch cards, and they trained it with their own handwriting. Now the whole school uses it."
   (`v-firststage` log). Better: story first, then one short "Press Run the lunch line to see how it does." general.
2. **One teach often changes nothing, and nobody says why.** A flagged 1 reads 4; after one "It's a 1" it still reads
   4 (k = 3), after two it reads 1 (`w-drag`: reads 4, 4, 1, 1, 1). A solo student thinks teaching failed. The hint
   after teaching ("Press Clear pad to try another, or Bitsy, read it! to compare.") could say, when the read didn't
   change: "Bitsy still sees more look-alikes that say 4. Teach it one more card." This is also the tool's best
   moment for "one example is not enough; two are". family:ml-lab.
3. **The mix-up moment is small and quiet.** The "Wanted pasta" sticker is 11 px text tucked under Bitsy, partly over
   its wheels, with no sound (`lunch-mixup`). It is the harm the tool is about. Better: a larger sticker beside the
   tray, a soft "wrong" cue from the kit, and mark wrong cards in the queue (a small tray icon or X) so after the run
   the stage shows which four cards went wrong, not only the text list. general.
4. **Every run speaks all three room totals (about 9 s) before the line that matters.** After five runs a student has
   heard "Room 12 got 10 right lunches out of 10" five times (`v-seq-same`, `v-seq-all-flip`). They are event lines
   per the spec, so this is a spec question: after the first run, speak only the rooms whose total changed, or lead
   with "same"/"flip". general.
5. **Teacher projection: the numbers are small.** Bar captions are forced to 11 px (`#bars text{font-size:11px!important}`,
   src.html:16) and Mix-ups is 13 px, so at 1920x1080 on a projector "6 of 10 right lunches" can't be read from the
   back (`res-1920x1080`). Better: scale captions with the panel at large sizes, and show the room totals on the stage
   too (see should fix 5). general.
6. **Mix-up wording.** "Room 9: wrote 1, got tacos (4), 4 cards" puts two different 4s side by side. Better: "Room 9:
   4 cards wrote 1 (pasta), got tacos." general.
7. **Empty bars say "0 of 0 right lunches"** before any run (`def-1366x768`, `jars-empty`); "No run yet" is already
   above. Better: leave the captions blank until a run. family:ml-lab (the `groupBars` empty state).
8. **Room badges on the lunch-line cards are about 8 px.** Circle and square read as the same dot in grayscale and on
   a projector (`gray-res`, zoomed). The 30 cards are where a class first spots Room 9's flagged 1s. Better: badges
   about 14 px, or a room-colored strip with the shape on each card. general.
9. **The cafeteria art is stretched to the stage** (`preserveAspectRatio:'none'`, src.html:124): at 760x900 the counter
   and trays are pulled tall (`def-760x900`). Real art will show this more. Better: `xMidYMax slice` and place the menu
   board from the image's own box. general.
10. **Writing mode is a plain form.** No Bitsy, no cafeteria: a blank pad and a grid on flat mint (`wr-1366x768`). A
    small Bitsy beside "What Bitsy sees" holding the guess on its screen would tie the two modes together. general.

## Nits

1. Mid-run the room label ("Room 12") above the feeding card stays after the card has slid and faded (`mid-1366x768`):
   the label is outside the animated group. general.
2. Drawing with the mouse leaves the keyboard pen's blue ring at its last keyboard spot on the pad (`w-drag`). Show the
   ring only after a key press. general.
3. "− Fewer" wraps to a lone minus over "Fewer" at most sizes (`def-1366x768`). general.
4. The empty-jar viewer says it is empty twice in two different sentences (`view9-start`). general.

## Audit pilot

- Leads confirmed: none needed fixing; the sizes, Motion off and five-click rows matched my frames (targets, fold for
  Run/Train/jars, how lines once). Leads that were wrong: all 11 overlaps at 375 are panel text hidden by the
  panel's own scroll box, measured against the stage SVG below it; nothing overlaps on screen (`h375-def`).
- It missed: the empty Room 9 viewer (row 11 only shows the line), the stale hint after a run, results below the fold
  after a run, Writing's stacked layout after a read, and the silent Run first tap (row 5 shows "spoken" blank but
  doesn't flag it); it can't see past one click, so none of the run-end or teach states.

Teaching lens (read after the above): agree on the empty Room 9 jar (its S1 = my should fix 1), the post-run hint
(S2 = 2), "learned from everyone" (S4 = 4) and the doubled empty-jar text; differ only in level on the one-teach
moment (its S3 should fix, my polish 2: I'd accept its level, since the screen says "learned" then gets it wrong); it
also caught `teach` training untrained jar changes (N2), which I missed; my silent Run first tap and the compact-size
results and Writing layout (should fix 3, 5, 6) are not in its list.
