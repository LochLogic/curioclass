PASS (round 2 re-check, 2026-10-29: the 3 should fix items and polish item 6 are fixed; polish 4, 5 and the line over dog pictures are known, not done)

# teach-the-robot: Final look (round 1, 2026-10-29, fresh cold agent)

Read handoff.md and refine.md (Refine PASS, round 2) first. Bundle rebuilt with `CURIO_DRAFT=1` (634 KB on disk 652 KB,
byte-identical to the committed bundle). 41 lines in voice/lines.json, 41 clips; every line's `clip_name()` file exists,
and every clip is under the kit's hold cap (2.5 s + 80 ms per character; the longest, the Teach welcome, is 7.34 s
against 9.38 s). Drawn in code, no `art:` tokens, no people.

Tools: `scripts/audit_tool.py` on ports 9231/9232 with host port 8814 (audit.md: 4 leads, all "welcome not heard" after
a first tap on Pet Parade, Next pet, Mystery pet or Start over; every size, state, Motion off, resize, five-click and
quick-tap row clean). Then `scripts/drive.py` on 9231 (voice) and 9232 (frames), host on 8814 for 375 wide (host.html
deleted after). Voice runs wrapped `window.Audio` to log each clip's start, end or cut, and matched each played clip's
data back to its mp3 file, so every played clip is identified by its content, not by the log's text. Scratch:
`S:/CurioClass-codex-scratch/final/teach-the-robot/` (audit/, frames/, vframes/, work/). Every Chrome and server
closed; nothing left listening on 9231, 9232 or 8814.

## Should fix

1. **Read on a two-part hint plays the browser voice, not a clip** (should fix, general; K-2 rule "every fixed line has
   its clip"). Most hints are two lines joined (`both()`: "Kip remembers: that one is a cat! Now tap Mystery pet. Kip
   will guess!", every Mystery result, Forget, Start over, every parade end). Read speaks `#hint` as one string, which
   has no clip, so the kit falls back to speechSynthesis: a different, robotic voice in a tool that otherwise speaks
   only Laomedeia. Seen: v-read-pend (Read after a parade end: no clip started, `speechSynthesis.speak` called with
   "Kip got six out of ten right. Tap Teach and show Kip more pets. Then run the parade again."). Single-line hints
   (v-first-read, v-read-off, v-read-mid) play their clip. Fix: pass `read: () => [...]` to `Curio.voice` returning
   the hint's lines as a list (the kit plays a list part by part, each with its clip); keep the hint text as is.
2. **The skipped Teach welcome arrives late and is cut, so the premise is lost** (should fix, general; audit lead
   confirmed). The natural first tap is Next pet (the screen says "Tap Next pet"). Its own line plays, the welcome is
   skipped, and it is queued again when the first card lands, after "Kip remembers" (about 8 s into the lesson). The
   recorded welcome is 7.3 s, so the next Next pet hushes it: v-teach5 (6 s pace) played 3.05 of 7.34 s; v-read-combined
   1.04 s (cut by Read). It is marked said when it starts, so "Kip is a robot that learns from examples" is never heard
   whole, and it plays after the class has already started, the late-welcome case the audit warns about. With the
   browser voice this passed; the real clip's length is what breaks it. Fix: on a first tap of Next pet, play the
   premise first (a short welcome line before "Is it a cat or a dog?", recorded), or drop the late welcome after a
   landing and leave it for Read; either way, no welcome after the class has begun.
3. **The look-alike line crosses the next card's name** (should fix, general; BUILD "Labels and badges never
   overlap"). When the deciding card is first on its shelf and the pet is down and to the right, the line leaves the
   card's lower right corner and runs straight through the name of the card beside it: "Bear" reads "?ear" in
   mtruth-1366x768, mtruth-800x500, mtruth-1000x625, mtruth-760x900 (zoom: work/z1.png). Not seen at 680x425 or 375
   (no names). Fix: end the line at the card's bottom edge centre when a name sits to the side, or route the last
   segment below the name row.

## Polish

4. **First Mystery pet: 10 s of back-to-back talk before the truth** (polish, general). Tap at 1.4 s, prediction
   2.2 to 4.9 s, "Kip looks for..." 5.0 to 9.3 s, guess 9.4 s, truth 11.4 s, then "Yes!" and the how line to 17.9 s
   (v-mystery5). It works and is spoken once, but it is the slowest moment in the tool; a class sits through 9 s of
   narration after its own guess. Better: let the prediction beat end when its clip ends (it already waits), and start
   "Kip looks..." while the line draws instead of after, so the guess lands about 2 s sooner.
5. **How lines cut at a teacher's pace and never heard whole** (polish, general). "Now tap Mystery pet. Kip will
   guess!" starts about 3 s after Cat (after "Kip remembers" ends) and needs 3.5 s; the next Next pet cut it at 3.15 s
   (v-teach5). "Tap Mystery pet again, or Next pet to teach Kip more." starts 2.3 s after the truth and was cut at
   0.79 s by the next Mystery pet (v-mystery5). Both stay in the hint, so nothing is lost for Read, but the spoken
   once-only instruction is usually clipped. Better: start the how line right after the event line with no extra gap,
   or let a cut how line come back once on the next idle moment.
6. **Kip's Chart memory counts collide at two digits** (polish, general). Under the bars, "12" runs into the next paw
   icon (the "12" touches the paw before "16") at 1366x768 (work/z3.png), 1280x720 and 1920x1080. Better: center the paw and number as one group
   under each bar, and shrink or drop the paw when the slot is narrow.
7. **The late welcome replaces the two-part hint** (polish, general). After the first card lands, the welcome sets the
   hint to "This is Kip... Tap Next pet to show Kip a pet." while one card is on the wall (v-read-combined frame). It
   still names Next pet, so it is not wrong; fixing item 2 removes it.

Known and left (from refine, still true): truth badge over the pet's small name at 680x425; wall card hit area 47 px at
680x425; Teach panel scrolls 24 px with a card selected at 680x425; Forget sits at the bottom edge at 760x900 (the
page scrolls).

## 1. Frames (all looked at)

audit/: size-* at all 8 sizes, state-mode-pet-parade-* at all 8, calm-1366x768. frames/: default, waiting, mguess,
mtruth (wrong label), selected, deckdone, pmid, pend (three runs 6, 10, 8), pempty at 1366x768, 680x425 and 375x812
(host); default, mtruth, pend, deckdone, selected at 800x500, 1000x625, 1280x720, 1920x1080, 760x900; default, mtruth,
pmid at 1366x768 with Motion off. vframes/: the end frame of each voice run. No horizontal scroll at any size, main
controls on screen, every hint whole, no placeholders. Pets: every dog reads as a dog (snout, nose pad, collar) and
every cat as a cat (whiskers, slit eyes); Marmalade on the Dog shelf in the wrong-label state is the intended lesson.
Text is drawn on flat scene color, not on pictures: no contrast issue on art. Only item 3 and item 6 seen.

## 2. Art against the spec

No `art:` tokens and no art files (art/prompts.json has none); everything is drawn in code, one consistent flat style.
Nothing to check against an art spec; no people.

## 3. Voice with the real clips

Every played clip matched its line (by content); played length = file length + 50 to 100 ms in every uncut case, so
nothing is truncated in the files. No clip ran into another line: the kit stops one before the next starts, and the
only cuts are hushes from a newer tap or Read (items 2 and 5). The browser voice was never used except Read on a
two-part hint (item 1). Clips never played in these runs (wrongLabel, afterMysteryAll, empty, allCards, the other
score lines, more, fewer, better, againAllHow) exist, match their text by hash and fit their cap.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| catOrDog (Next pet x5) | how | 1 | 1 |
| remCat (Cat x5) | event | 5 | 5 |
| tryMystery | how | 1 | 1 (cut at 3.15 of 3.53 s) |
| teachWelcome (after first-tap Next pet) | welcome | 1 whole | 1, cut at 3.05 of 7.34 s (item 2) |
| predict (Mystery x5) | how | 1 | 1 |
| looks | how | 1 | 1 |
| thinkCat / thinkDog | event | 5 | 5 (3 + 2) |
| right / wrong | event | 5 | 5 (4 + 1) |
| afterMystery | how | 1 | 1 (cut at 0.79 s) |
| forgetHow (select x5) | how | 1 | 1 |
| forgot (Forget x5) | event | 5 | 5 |
| forgotHow | how | 1 | 1 |
| paradeWelcome, startHow | welcome, how | 1, 1 | 1, 1 |
| score line (parade x5) | event | 5 | 5 |
| same as last time | event | 4 | 4 |
| againHow | how | 1 | 1 |

First taps (fresh page each): stage tap, welcome clip at 1341 ms right after the tap; Tab key, welcome; Pet Parade
with an empty wall, only "Tap Teach first!"; Read, the hint (welcome text) by clip; Sound, nothing, then Sound on
brings the welcome once; Next pet, only its own line (then item 2). Stale (0.2 s taps through Next pet, Cat, Next pet,
Mystery pet, Pet Parade, Teach, Start over): each line cut at its moment, only "Starting over!" and "Tap Next pet"
play to the end, in order. Read cuts a playing line and plays the hint, works with Sound off; after Read a mode change
speaks at once. Liveliness: no take flagged flat by the reading; timing gives no take a reason to redo.

## 4. Full run, solo student and teacher projecting

Solo student: the first screen and the welcome say Tap Next pet; Cat or Dog is asked out loud; every waiting moment
names its control in the hint and once by voice. A student who starts with Next pet never hears what Kip is (item 2).
Teacher projecting at 1366x768 and 1920x1080: cards, names, slots and the score box read from the back; the chart
numbers are readable apart from item 6; the parade's 3.5 s per pet gives time to call out each guess. The flattest
spot is the first Mystery pet (item 4). Scores in the page: 2 cards 6 of 10 (five runs), 12 cards 10, 16 cards with
Marmalade as dog 8: as the spec table.

## 5. Contract

One file, 634 KB with all 41 clips (under 2 MB). No console errors or exceptions in any audit or drive run (the only
log line is the host page's favicon 404). The only http string in the bundle is the SVG namespace; clips are data URIs;
no network requests.

## Re-check (round 2, 2026-10-29, same agent)

I treated final-fix.md as claims and checked each one. Rebundled with `CURIO_DRAFT=1` (638 KB; the working kit/curio.js
now has a `hold` option this tool does not use). drive.py on 9231 (voice, 18 runs) and 9232 (frames), host on 8814
for 375 wide (host.html deleted after). No console errors or exceptions in any run (the only log line is the host
favicon 404). Nothing left listening; every Chrome closed. Frames: frames2/ (r2-mguess, r2-mtruth, r2-mguess10 with 10
cards, r2-pend at 1366x768, 680x425, 800x500, 1000x625, 1280x720, 1920x1080, 760x900 and 375x812, r2-pend1 at
1366x768 and 1920x1080) and vframes2/ (the end frame of each voice run), all looked at.

1. **Read on two-part hints: fixed.** Read after Cat, a right and a wrong-label Mystery result, Forget, Start over,
   a parade end and a parade end with the deck used up (v-read-cat, -myst, -wrong, -forget, -over, -pend, -pendall):
   each plays two clips, the event line, then the how line, matched by audio content. `speechSynthesis.speak` was
   never called in any of the 18 runs. Read with a single-line hint and with Sound off still plays its one clip.
2. **Teach welcome: fixed.** It no longer plays after a card lands: a first tap on Next pet, then five Next pet and
   Cat pairs at a 6 s pace, never brings it (v-first-next, v-teach5). A plain first tap plays it whole at 1.34 s
   (v-first-stage). Cut at 2.63 s by Next pet, it plays again whole (7.42 s) at the next Teach entry (v-cut-mode). Cut
   by Sound off, it plays whole when Sound comes back on (v-cut-sound). Cut by Read at 1.63 s, it plays whole at the
   next Teach entry (v-cut-read). The cut Pet Parade welcome gets the same treatment. One trade-off, which I accept: a
   class that starts with Next pet now hears the premise only by Read or on its first return to Teach, never cut
   mid-sentence. The hint and the first how line still say what to do.
3. **Look-alike line over a name: fixed.** With names shown, the line now ends just under the deciding card's own
   name, and any name it still crosses is redrawn whole on top: "Bear" (mtruth) and "Pebble" and "Rocket" (mguess,
   mguess10) read whole at every size; at 680x425 and 375 there are no names and the line ends on the card corner.
   **Cat card line over Dog card pictures (polish, general, known, not done).** From a Cat card the line crosses the
   Dog shelf, through Pebble's face (mguess, every size) or Pebble and Rocket (mguess10). I judge this acceptable: the
   gold glow and the end dot sit on the deciding card, so the line reads as ending there, and no name or label is
   hidden. Still, a child could take the dog it passes over as the match. Better: draw the line under the cards (or
   fade it where it crosses a card) so only the deciding card has it on top.
4. **Chart memory counts (polish item 6): fixed.** Counts are centered under each bar. When two-digit counts leave no
   room, one paw sits at the left of the row (1366x768, 1280x720, 1920x1080, 760x900); otherwise each bar gets its own
   paw (680x425, 800x500, 1000x625, 375). No count touches a paw or another count. With one paw at the row's left, the
   link between paw and pets remembered is a little weaker, but still readable.

**Regressions (voice counts, real clips):** Next pet x5: catOrDog 1, remCat 5, tryMystery 1. Mystery x5: predict 1,
looks 1, guess 5, result 5, afterMystery 1. Select and Forget x5: forgetHow 1, forgot 5, forgotHow 1. Parade x3: score 3,
same 2, againHow 1, paradeWelcome and startHow 1 each. Stale 0.2 s taps: each line cut at its moment, the order follows
the actions. No played clip ran past its moment; every uncut clip played its full length. Scores: 6 (2 cards), 10
(12), 8 (16 with Marmalade as dog), 10 (16), as the spec. No horizontal scroll and no hint clipped in any re-shot frame.

Still open as polish (known, not done): item 4 (the first Mystery pet's 10 s of narration) and item 5 (how lines cut at
a teacher's pace; tryMystery cut at 3.15 of 3.53 s and afterMystery at 0.8 s, as in round 1). Item 7 is gone with
item 2: the hint after Cat now stays "Kip remembers... Tap Next pet to show Kip a pet."
