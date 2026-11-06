# Illusion Lab

## One idea
You are the subject: you set lines, grays and memories by your own eye and memory first, and only then see that your
own numbers show the same bends the research found, and why the senses and memory build what you experience.

## Not like
- collision-lab (live), gas-law-lab, hand-warmer-lab, prototype-lab (shared lab-bench setting, clusters.md): they
  measure gliders, gases, heat or a design; here the student is what is measured, and the bench is only the home
  screen. Own accent (orchid) and voice (calm-professor).
- go-along: also shows lines, but as a social-pressure pick of A, B or C; Line Lengths is solo and continuous (slide
  one figure with fins). No three-line Asch layout appears here.
- brain-explorer: owns brain regions and cases; Inside the Eye stops at the retina and names the visual cortex only as
  the path's end.
- trait-lab: personality and intelligence measures; this tool measures perception and memory and never labels anyone.
- jury-room: deliberation; Eyewitness here is one short read, no jury, no verdict.
- how-animals-see (live, 3-5) and sign-parameters-lab: animal eyes and ASL; no overlap beyond eyes or the word "lab".

## Who and how
Grade 12, psychology (social studies module social-studies-12-sensation-perception-and-memory). Driver: students
(solo by default; works projected, with the class answering out loud and a show of hands for the Word Lists lure).
30 to 45 minutes for all six stations; each station runs 3 to 6 minutes on its own. Standards: APA.Biological,
APA.Cognition. Prompts are not personal (no feelings, family or health). Privacy line on the Bench and Notebook:
"Your results stay on this device." (localStorage `illusion-lab-v1`, try/catch.)

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| APA.Biological (sensation: receptors, transduction, pathway) | Inside the Eye: tap each stage of the path in turn, then predict Edge or Middle and slide Neighbor inhibition | the signal travels light, rods and cones, bipolar cells, ganglion cells, optic nerve, thalamus, visual cortex; the output curve grows a bright band and a dark band at the edge while the middle of a big patch stays put | after moving the slider to 0.4, the output at the edge cells reads 0.58 and 0.08 against plateaus 0.48 and 0.18, and the "Why" card names lateral inhibition |
| APA.Biological (perception builds on sensation) | Line Lengths and Shadow Squares: set the figure or swatch by eye, 8 and 2 trials, then open Why | own illusion size per fin angle beside the no-fin controls; own A and B swatch settings beside the true gray; then the Bridge reveal | the Line Lengths chart shows three fin angles plus controls and the Why card states fins narrower = stronger (Dewar); Shadow Squares Why names both local contrast and the shadow inference |
| APA.Cognition (encoding needs attention) | Spot the Change: find 6 flicker changes, then 1 with no gap | alternations for each scene, central vs marginal averages, then the no-gap scene popping out | Notebook shows central and marginal averages and the no-gap count; the Why card says attention is needed to see change |
| APA.Cognition (storage and forgetting, interference) | Count Backward: 10 trials of letters, a counting task, then typed recall | own recall by delay, first trial and digit-switch trial marked, beside Peterson's two endpoints | the chart plots trials 2 to 9 by delay, trial 1 and trial 10 as separate marked dots, and the Why card names proactive interference and release |
| APA.Cognition (retrieval is reconstruction) | Word Lists: free recall of list 1, Seen or New plus Picture it or Just know on list 2 | own studied-word recall, whether the never-shown word was typed or called Seen, and how sure | the Notebook shows lure recalled yes or no and lure recognized with its Picture it or Just know tag, beside Roediger and McDermott's 40% and 55%; Eyewitness then links it to Loftus and Palmer |

## Screens and modes
**On load:** the Bench. Nothing plays (the kit speaks nothing before the first tap). Painted bench backdrop
(`il-bench`) with six station cards in code (3 x 2), each with a code-drawn thumbnail of its stimulus (fins, two
squares, a receptor row, a flicker frame outline; Count Backward and Word Lists use the painted stopwatch and blank
index cards, see Art; no thumbnail shows a trigram or a list theme) and a line "about 4 min". Below: Notebook and Eyewitness buttons, and the privacy line. First hint: "Pick a station
card to start. Line Lengths is a good first one." First tap on a station card opens it and queues that station's
how line (so the welcome is skipped; its content lives in the hint and Read). A first tap on Notebook or Eyewitness
queues the welcome after its own line, if it has none.

**Layout at 1366x768 (every station):** header 48 px (title, Motion, Sound, Read). Left rail 168 px: Bench, the six
stations (icon plus name, a check mark once done), Notebook, Eyewitness. Stage in the center (about 870 x 700) holds
the stimulus, always the biggest thing. Right panel 320 px: hint, the station's controls, a small progress row
("Trial 3 of 8"). All controls a station needs sit above the fold. At 680x425 the rail becomes 48 px icon buttons
(names as aria-label and title), the panel narrows to 220 px with controls first and the hint second, and the
stimulus re-lays out at real pixel size (no scaled-down text under 10 px). Below 1000 wide the panel never stacks
under the stage; it stays beside it, compact.

**Every station has three steps, in order:** Do (the task, no results shown), Compare (own numbers beside typical or
true values), Why (the explanation card, 4 to 6 short paragraphs, on screen, with a diagram where named). Step tabs
"Do", "Compare", "Why" sit above the stage; Compare and Why are disabled until Do is finished once. "Run again" in
Compare starts a new run; the Notebook keeps the first complete run and the latest, both labeled.

**Line Lengths.** Focus: two figures stacked on the neutral stage. Top: the reference figure. Bottom: the adjustable
one, centered on its own random horizontal offset (plus or minus 60 units) so end alignment cannot be used. Controls:
Shorter, Longer (hold to repeat, 1 unit per step, 25 steps per second), Left and Right arrow keys, dragging either
end of the bottom shaft (both ends move together, symmetric), Lock it in. 8 trials: fin angles (angle between the two
fins) 45, 90 and 135 degrees, each once with the fins-in figure adjustable and once with the fins-out figure
adjustable, plus 2 plain-line control trials (no fins), in shuffled order. Reference shaft random 260 to 340 units;
fins 50 units long; lines 3 px #e6e6e6 on #26262a. Start length random in 0.70 to 0.95 or 1.05 to 1.30 times the
reference. Range limits 0.5 to 1.6 times. No grid, no ruler, no numbers, no feedback until all 8 are locked.
Compare: a dot chart of "illusion size" (percent, in the direction the illusion pushes) for 45, 90, 135 and Controls,
with a 0 line labeled "perfect match". Why: Müller-Lyer (1889), the fin-angle result, practice shrinking it, and the
culture debate card (Content).

**Shadow Squares.** Focus: a code-drawn checkerboard floor (8 x 6 checks in mild perspective) with a code-drawn
cylinder casting a soft shadow, squares labeled A (outside the shadow) and B (inside). A separate swatch sits on a
plain #808080 strip at the right of the stage. Controls: Darker, Lighter (2 sRGB steps, hold to repeat), Up and Down
keys, Lock it in. Order per trial: match A, then match B. 2 trials (gray sets in Content). Compare: two bars per trial,
"your A" and "your B", beside a line at the true gray they share, and "B minus A" in steps. Then two buttons: Bridge
(a bar of the exact shared gray, #6e6e6e on trial 1 and #797979 on trial 2, joins A and B) and Hide the scene (everything but A and B goes to
#808080). Why: lightness constancy and local contrast (Content).

**Inside the Eye.** Focus, top half: the path diagram (seven stage boxes left to right, in code); tapping a stage
sends a pulse to it and opens its two-line card. Bottom half: a row of 24 receptor cells under a light pattern, the
input curve in gray and the output curve in the accent. Controls: Pattern (Step edge, Patch on dark, Patch on light),
Neighbor inhibition slider 0 to 0.4 in 0.05 steps (starts at 0), Predict buttons Edge and Middle (shown before the
slider unlocks on the first visit: "Where will the output change most?"). Rule: output(i) = input(i) minus k times
the average of its two neighbors (end cells reuse themselves). Values: Step edge 0.8 then 0.3; patches are 0.5 on 0.2
or on 0.8. What it shows: k 0, output equals input; k 0.2, edge cells 0.69 and 0.19 against plateaus 0.64 and 0.24;
k 0.4, 0.58 and 0.08 against 0.48 and 0.18. Patch interior reads 0.30 at k 0.4 on both surrounds; only its edge
cells differ (0.36 on dark, 0.24 on light). The Why card uses that: inhibition sharpens edges but cannot by itself
make a big patch look lighter, so Shadow Squares also needs the brain's guess about the light.

**Spot the Change.** Focus: the painted scene, 16:10, as large as the stage allows. Flicker notice above it the
first time: "This station flashes a gray screen about once a second. Choose Flip by hand to step through instead."
Cycle: image 560 ms, gray blank 160 ms (the scene's average color), other image 560 ms, blank, and so on: 1.39 blanks
per second, under 3 flashes per second. Count alternations. Controls: Start (begins the next scene), Spotted it (or Space), Flip by hand toggle (Flip
button then shows the blank 160 ms and the other image; flips counted the same), Next scene. Spotted it freezes the
current image; the student taps where. Right spot (inside the change box plus 4% padding): pick the kind of change,
three picture buttons Color, Appeared or vanished, Moved. Wrong spot or wrong kind: counted as a miss and the cycle
resumes. Three misses or 83 alternations (60 s): "Not found", the change is outlined and both frames shown side by
side. 6 scored scenes (3 central interest, 3 marginal) in shuffled order, then scene 7 with no blank (marked "No
gap"). Motion off: Flip by hand is on by default. Every control stays live while flicker runs; Spotted it freezes at
once, never at the next beat. Compare: alternations per scene, central and marginal averages, the no-gap count.

**Count Backward.** Focus: one big center box. Start (one per trial; between trials it reads Next trial) shows three letters for 1.5 s, then a three-digit number and
three choice buttons (the number minus 3, minus 2, minus 4, shuffled positions); every tap shows the next number and
new choices; a 3 s step with no tap counts as missed and moves on. After the delay, the box asks "Type the three
letters" (text box, autocomplete, autocorrect and spellcheck off, uppercase shown) and Enter or Submit. Trial 1 delay
18 s; trials 2 to 9 delays 3, 6, 9, 12, 15, 18, 3, 18 shuffled; trial 10 shows three digits instead of letters,
delay 18 s, with "Type the three digits". The student sets the pace.
Compare: recall (all three in order) by delay for trials 2 to 9 as dots, trial 1 and trial 10 as their own marked
dots ("First trial", "Switched to digits"), and Peterson's two endpoints as hollow diamonds joined by a dashed line
labeled "Peterson and Peterson 1959, approximate".

**Word Lists.** Focus: one word at a time, 56 px, center. Start begins list 1. List 1 (15 words, 1.5 s each, then a 1 s blank) then a
recall box: type a word, Enter adds it as a chip (delete by tapping the chip's x), Done when finished (2 min cap, a
quiet countdown bar). Then list 2, then the recognition test: 12 words one at a time, buttons Seen and New; after
Seen, Picture it ("I can picture it on the screen") or Just know ("It feels familiar"). Start over appears during a
list; using it marks that list "seen twice" and Compare greys it out. No voice and no hint changes while a list plays.
Compare: list 1 studied words recalled out of 15, and the lure row "Typed a word that was never shown: yes or no (the
word)"; list 2 Seen rate for studied words, for unrelated new words, and the lure's answer and tag; Roediger and
McDermott's 40% and 55% as reference bars. The lures are named only in Compare.

**Notebook.** A table: one row per station, your key number, the comparison, and Go to station. Run counts. Reset
all (confirm: "Clear every result on this device?" Yes, Cancel).

**Eyewitness.** On-screen read: your Word Lists lure result at the top (or "Run Word Lists to see your own result
here" with a Go button), then the Loftus and Palmer card, the exoneration figure, and a closing question to discuss:
"Your false word felt real. What should a jury hear before trusting a confident witness?" No answer box.

## Content
Line Lengths illusion size: fins-in adjustable: (set minus reference) / reference x 100. Fins-out adjustable:
(reference minus set) / reference x 100. Controls: the fins-in formula, with the plain line in the fins-in slot.
Station value = mean of the six fin trials; per angle = mean of its two. A trial where the student moved less than 3
units in total is not locked: "Move the bottom line until it looks equal first." A trial locked at a range limit
plays once more at the end, new start length.

Line Lengths Why text: "Franz Müller-Lyer published this figure in 1889. Fins pointing out make a shaft look longer;
fins pointing in make it look shorter. The illusion is stronger when the fins form a narrower angle. With practice,
and especially with feedback, it often shrinks, which is why you saw no numbers until the end. Your control trials
show your eye's own error with no fins." Culture card: "In the 1960s, Segall, Campbell and Herskovits measured the
illusion in many societies and found its size differed. One proposed reason: people raised among right-angled
buildings learn to read the fins as corners. A 2025 review by Amir and Firestone argues the evidence does not show a
cultural cause. Researchers still disagree."

Shadow Squares gray sets (sRGB gray, same value on all three channels): trial 1 light checks 200, dark checks 110,
shadow multiplies by 0.55 with a 24 px soft edge, so A (dark, lit) = 110 and B (light, shaded) = 200 x 0.55 = 110.
Trial 2: light 220, dark 121, B = 121. Swatch starts random 60 to 180. Why text: "A and B are the same gray on your
screen. Your eye has two reasons to call B lighter. Cells compare each spot with its neighbors, and B sits among
darker checks. And your brain reads the shadow as less light falling on the floor, so it decides B must be a light
check. Edward Adelson, who made the first version of this illusion in 1995, calls it a success of vision: in a real
room, B would be the lighter tile."

Inside the Eye path cards (two lines each): Light (enters through the cornea and lens and lands on the retina); Rods
and cones (photoreceptors; they turn light into electrical signals, called transduction; an eye has about 92 million
rods for dim light and about 4.6 million cones for color and detail, roughly 20 to 1, and counts vary between people);
Bipolar cells (pass signals on and begin comparing neighbors); Ganglion cells (their axons bundle into the optic
nerve); Optic nerve (carries the signal out of the eye); Thalamus (a relay station); Visual cortex (at the back of the
brain, in the occipital lobe, where seeing edges and shapes begins). Why text: "Each cell's signal is turned down by
its neighbors: lateral inhibition, first measured by Haldan Keffer Hartline in the horseshoe crab eye. It makes
edges stand out, as the bright and dark bands showed. It barely changes the middle of a big patch, so Shadow Squares
needs more than your retina: your brain's guess about the light."

Spot the Change scenes (art in Art; change box in scene fractions x, y, w, h):
1 kitchen, central, color: the red kettle on the stove turns blue (0.42, 0.40, 0.14, 0.18).
2 street corner, marginal, appeared or vanished: a small blue mailbox at the far right curb (0.86, 0.62, 0.06, 0.12).
3 park pond, central, moved: the rowboat shifts left by 0.12 of the width (0.40, 0.55, 0.20, 0.12).
4 classroom, marginal, appeared or vanished: a small potted plant on the back shelf (0.08, 0.22, 0.06, 0.09).
5 market stall, central, appeared or vanished: the big basket of oranges in front (0.38, 0.60, 0.22, 0.20).
6 harbor, marginal, color: a far buoy turns from red to green (0.80, 0.58, 0.04, 0.06).
7 living room, marginal, moved, No gap: a framed painting on the side wall shifts up by 0.08 (0.12, 0.20, 0.10, 0.12).
Why text: "With a gray blank between the pictures, the flash hides the change's own motion signal, so you must find
it by attention, one place at a time. Changes to things a scene is about (central interest) are found faster than
changes to background things (marginal interest). With no gap, the change pops out."

Count Backward trigrams, in order: TLV, PGQ, LSK, WBG, SPH, NJC, VKD, RSF, NWH (no two in a row share a letter, no
vowels, no common acronyms); trial 10 digits 582. Start numbers: random 300 to 999. A trial counts as "rehearsal
possible" when fewer than 70% of its counting steps were answered right; it is plotted hollow and left out of the
by-delay dots. Why text: "Peterson and Peterson (1959) had people count backward to stop rehearsal. Recall fell from
about 80% after 3 seconds to about 10% after 18. They called it decay. Keppel and Underwood (1962) found the very first
trial was recalled almost perfectly even at 18 seconds: earlier letters crowd out new ones, proactive interference.
Switching to digits on your last trial gives memory a fresh category, and recall often comes back. Hermann Ebbinghaus
described the long-term forgetting curve in 1885: fast loss at first, then slower."

Word Lists (original lists, built the way Deese, Roediger and McDermott built theirs: the strongest associates of one
word that is never shown, strongest first).
List 1 (lure winter): snow, cold, ice, sled, mittens, frost, scarf, December, freezing, coat, shovel, blizzard, boots,
chilly, snowman.
List 2 (lure beach): sand, waves, shore, ocean, towel, sun, surf, shells, tide, swim, umbrella, salt, coast,
sunscreen, seagull.
Recognition test (12, shuffled, the lure never in the first or last two slots): studied sand, waves, towel, tide,
sunscreen, seagull; lure beach; unrelated pencil, garden, candle, ladder, violin. Recall matching: lowercase, trimmed,
a trailing "s" ignored. Why text: "Your memory stored the list's meaning, then rebuilt it when you recalled it, and
the theme word came along. In Roediger and McDermott's 1995 study, with lists read aloud, people recalled the
never-said word on 40% of lists, and on 55% with longer lists. Most who later called it old said they could
remember hearing it. Memory works in three steps, encoding, storage and retrieval, and retrieval is a rebuild, not a
replay. Their lists differ from these, so compare loosely."

Eyewitness text: "Loftus and Palmer (1974) showed students a film of a car crash and asked how fast the cars were
going when they hit or smashed each other. 'Smashed' got estimates of about 40 mph, 'hit' about 34 mph. A week
later, 32% of the 'smashed' group remembered broken glass, against 14% of the 'hit' group. There was no broken glass.
The Innocence Project found that mistaken eyewitness identification played a part in 69% of the 375 DNA exonerations
it tracked in the United States from 1989 to 2020."

## Interactions in detail
- Leaving a station mid-run (rail tap) keeps nothing from the unfinished run and says so in a toast: "That run was
  not finished, so it was not saved." Finished steps and the Notebook are kept.
- Do-step controls never show numbers. Compare is the first place any number appears for that run.
- Line Lengths and Shadow Squares: hold-to-repeat stops on pointerup, pointercancel and blur. Lock it in is disabled
  until the figure or swatch has moved 3 units; its hint then names the move ("Press Longer or Shorter first.").
- Spot the Change: a tap on the image with no Spotted it does nothing (hint: "Press Spotted it first, then tap.").
  Spotted it during the blank freezes on the image that comes next. Resize mid-run keeps the alternation count.
  Preload all 14 frames before the first scene starts (a "Loading pictures" line); no frame shows a load flash.
- Count Backward: typing in the recall box before the prompt is impossible (box hidden). Submit with an empty box
  counts as 0 letters. Letters are scored in place (shown as 0 to 3 right) and as all-three-in-order (plotted).
- Word Lists: Done with no words: "Nothing typed. That's a result too." Words typed twice count once.
- Run again on any station replaces "latest" only. Reset all clears both, after the confirm.
- Sound off: nothing speaks; hints still update. Motion off: no pulse animation on the path (the stage just lights),
  flicker becomes Flip by hand by default, timing of lists and counting unchanged.

## Look
9-12 theme (`kit:theme-912`). Accent `--brand #f28fc4` (orchid), `--brand-ink #1f0a16`; no neighbor uses it
(collision-lab cyan, gas-law-lab #9ec9e8, hand-warmer-lab #d28279, prototype-lab #ff9f43). Stimulus stage is neutral
`#26262a` with no tint, because color around a gray changes how it looks; the accent never touches a stimulus. Data
charts use theme graph colors: own data accent filled dots, typical values hollow diamonds in `--gr-1`, true values a
`--ink` line, each with its own shape and a text label, so color is never the only signal. Contrast (computed):
accent on panel 7.83:1, on sec-bg 7.42:1, on paper 8.50:1, on stage 6.82:1; brand-ink on accent 8.53:1; stimulus
lines #e6e6e6 on stage 12.08:1; ink on stage 12.81:1; muted on stage 7.08:1. No confetti, no mascot.

## Art
- il-bench: a tidy psychology lab tabletop seen from slightly above, warm desk lamp, a blank clipboard, a stopwatch,
  a stack of blank index cards, a small eye model, soft evening light, painterly; 16:9; cutout no; people no; Bench
  backdrop under the code cards (darkened 35% so card text stays AA).
- il-cards: a stack of blank white index cards with a pencil, on a dark desk; 1:1; cutout yes; people no; Word Lists
  thumbnail (shows no words and no theme).
- il-stopwatch: a silver stopwatch, plain face with tick marks only; 1:1; cutout yes; people no; Count Backward
  thumbnail.
- Seven scenes, each 16:10, people no, painted base WITHOUT the changing object, plus one cutout (yes) of the object
  with matching light, feathered edge, placed by code at the change box: il-kitchen (sunny kitchen, stove, counter,
  window; cutout il-kettle, a red kettle, 1:1, color changed in code by hue rotation to blue); il-street (city corner,
  shops with blank signs, trees; cutout il-mailbox, a blue mailbox, 3:4); il-pond (park pond, trees, bench; cutout
  il-boat, a wooden rowboat, 16:9); il-classroom (empty classroom, desks, a back shelf, blank board; cutout il-plant, a
  small potted plant, 3:4); il-market (outdoor fruit stall, crates; cutout il-oranges, a woven basket of oranges, 4:3);
  il-harbor (harbor, moored boats, far water; cutout il-buoy, a red buoy, 3:4, hue rotated to green); il-living (living
  room, sofa, side wall; cutout il-frame, a framed landscape painting, 4:3). Text surfaces blank.
- Drawn in code: every illusion figure, the checkerboard and cylinder (exact gray values are the experiment), the
  eye path and receptor row (a diagram that moves), charts, thumbnails for the other stations.

## Voice
Bank voice `calm-professor` (Schedar), style "Say evenly and clearly, like a calm, friendly college professor running
a lab." No neighbor tool uses it (collision-lab hs-narrator, hand-warmer-lab news-reader, prototype-lab
science-narrator, gas-law-lab bright-teacher; the grade 12 psychology neighbors are unbuilt). `Curio.voice`, `scope: ()
=> state.station + ':' + state.step`. No line plays during a measurement (a list, a flicker run, a counting trial, a
Do trial being adjusted): starting one calls `V.hush()`, and lines queued in that scope are dropped stale.
- welcome (how; first tap on Bench, Notebook or Eyewitness that queued nothing; stale when a station opens):
  "Welcome to Illusion Lab. Here, you are the subject. Pick a station card, do the task first, then compare your
  results with the research."
- llHow (how; entering Line Lengths Do; stale when trial 1 is locked): "Make the bottom shaft look as long as the top
  one. Use Longer and Shorter, then press Lock it in."
- llDone (event; all 8 locked): "Done. Your settings are on the chart beside a perfect match."
- ssHow (how; entering Shadow Squares Do; stale when the first match is locked): "Make the swatch match square A. Use
  Lighter and Darker, then press Lock it in."
- ssB (how; after A is locked on trial 1; stale when B is locked): "Now match square B the same way."
- ssBridge (how; first Bridge press): "One bar, one gray. Square A and square B were the same all along."
- eyeHow (how; entering Inside the Eye; stale when a prediction is tapped): "Tap a stage to follow the signal. Then
  tap Edge or Middle to predict where the output will change most."
- eyeSlide (how; after the prediction; stale when the slider moves): "Now slide Neighbor inhibition up and watch the
  output line."
- eyeBands (how; first time k reaches 0.3 on Step edge): "A bright band and a dark band at the edge. The light did not
  change there. The cells did that."
- scHow (how; entering Spot the Change, before Start; stale when Start is pressed): "Press Start. When you see what
  changes, press Spotted it, then tap the spot."
- scKind (how; first correct spot; stale when a kind is chosen): "Right spot. Tap the kind of change."
- scNoGap (how; before scene 7 starts, plays before Start enables, whole): "Last scene, with no gray gap. Watch how
  fast you find this one."
- cbHow (how; entering Count Backward; stale when Start is pressed): "Read the three letters. Then tap the next number,
  counting back by threes, until the box asks for the letters. Press Start."
- wlHow (how; entering Word Lists; stale when Start is pressed): "Words will show one at a time. Just read them. Then
  type every one you remember. Press Start."
- wlTest (how; recognition test opens; stale on the first answer): "For each word, tap Seen or New. After Seen, tap
  Picture it or Just know."
- ewHow (how; entering Eyewitness): "Your own memory result is at the top. Read down to see why it matters in court."
- nbHow (how; entering Notebook): "Your results stay on this device. Tap Go to station to run one again."
Repeats: how lines once per page load, then hint only. llDone repeats per finished set. No line speaks a number.

## Family engine
none. Charts use `kit/graphing.js` only for axes and dots if the builder finds it fits; no family.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails (or the design change made here) |
|---|---|---|
| Line Lengths illusion size (a measure, no pass) | guessing; aligning ends; a ruler or pixel readout on screen; a chart of earlier trials to calibrate on; doing nothing; mashing Longer; knowing the trick and over-correcting; position or size cue | random reference length and offset kill end alignment and a fixed target size; no grid, ruler or number until Compare; no per-trial feedback; do-nothing is refused (3 unit move rule; simulated unmoved trials average 0% with SD 19, which is why they are refused); mashing hits the range limit, and limit trials replay; adjustable side and fin direction flip across trials, so one habit ("always longer") cancels out; a known-trick student still has the controls as the baseline, and Compare shows fins vs controls side by side |
| Shadow Squares match | set A and B the same on purpose; read a value off the swatch; doing nothing; mashing | no value shown; start value random per match; Lock it in needs a 3 step move; mashing ends at 0 or 255, labeled "at the limit, run again"; a student who sets them equal on purpose sees "B minus A: 0" and the Why card still teaches; nothing rewards it (no score) |
| Inside the Eye prediction (Edge or Middle) | guessing (1 of 2); answer on screen (input and output curves visible) | the output curve is hidden behind "Predict first" until a choice is made, and the slider is locked; a guess wins nothing: the next step is the same for both answers, with a one-line reply either way; it is a commit-then-see, not a score |
| Spot the Change found | mashing Spotted it then tapping anywhere; position (changes always central); size (changes always big); a halo or crispness edge on the cutout; a load flash; replaying a solved scene | a correct find needs the padded box (0.8% to 6.2% of the frame, computed) AND the kind (1 of 3): three random tries succeed 0.8% to 6.1% of the time per scene, and each miss resumes the clock; boxes sit in center and edges, small and large; cutouts feathered and lit to match; all frames preloaded; replays are marked practice and not stored |
| Spot the Change kind | elimination (kinds repeat) | each kind appears 2 or 3 times in shuffled scenes; the three buttons are always all live, in fixed order, unrelated to the scene |
| Count Backward recall | rehearsing instead of counting; writing letters down; mashing the count choices; doing nothing in the count | count steps must be tapped; under 70% right marks the trial "rehearsal possible" and hollow; mashing scores about 33% (1 of 3); no tap for 3 s is a missed step; paper cannot be blocked, so the hint says "No writing. Keep it in your head." |
| Count Backward choices | the correct answer's position; the common wrong answer (minus 2 or 4) | positions shuffled each step; both near misses always offered |
| Word Lists lure recall | the lure shown anywhere (station name, art, thumbnail, list title); autocomplete; doing nothing | no title, art or thumbnail shows a theme; the lure appears only in Compare; autocomplete off; typing nothing is a valid result, not rewarded |
| Word Lists recognition | answering New to everything; Seen to everything; the lure's position | Compare shows Seen rate for studied AND unrelated words beside the lure, so "all New" shows 0 of 6 studied and "all Seen" shows 5 of 5 unrelated; the lure is never in the first or last two slots and is styled like every word |
| Compare lines vs typical | a verdict to chase ("stronger than typical") | no verdicts or praise: Compare shows numbers beside the reference and the Why card; nothing on screen ranks the student |

## Heard in order
Grade 12: none required by grade. One rule must hold: lines never play during a measurement, and scNoGap plays whole
before scene 7's Start enables (Start waits for it; Sound off waits its estimated time). Station entry order: hint set
at once, then the how line; Start (or the first Do control) hushes it and never waits for it.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| Müller-Lyer figure published 1889 | Wikipedia, Müller-Lyer illusion | Amir and Firestone 2025, Psychological Review (doi 10.1037/rev0000549) | yes |
| Narrower fin angle makes it stronger | Dewar 1967, Perceptual and Motor Skills 24 (abstract) | Dewar 1965 McMaster thesis, "Stimulus determinants of the M-L illusion and its decrement" | yes |
| Practice and feedback shrink it | Dewar 1965 thesis (decrement) | a 1995 study on feedback and the Müller-Lyer illusion (PubMed 7567409: accurate feedback substantially reduced magnitude) | yes; builder confirms the author line before citing it in notes |
| Segall et al. found size differs across societies; carpentered-world idea | Segall, Campbell, Herskovits 1963 Science 139 | Henrich, Heine, Norenzayan 2010 | yes |
| A 2025 review disputes a cultural cause | Amir and Firestone 2025 | cognitionandculture.net "Culture and Perception part II" | yes (on screen as a disagreement) |
| Checker shadow: A and B identical; lightness constancy plus local contrast; Adelson 1995; "success" framing | illusionsindex.org/ir/20-checkershadow | Adelson 2000, "Lightness perception and lightness illusions" | yes |
| About 92 million rods, 4.6 million cones, about 20 to 1, varies | Curcio et al. 1990, J Comp Neurol (PubMed 2324310) | USMF repository abstract (same averages, 20 to 1) | yes; an older study is lower, hence "counts vary" |
| Path: photoreceptors, bipolar, ganglion, optic nerve, thalamus, occipital visual cortex; transduction | OpenStax Psychology 2e, 5.3 Vision | Purves et al., Neuroscience, NCBI Bookshelf | yes |
| Lateral inhibition, Hartline, horseshoe crab, edge enhancement | nobelprize.org, Hartline 1967 | Purves, Neuroscience (contrast and receptive field surrounds) | yes |
| Flicker: blank of about 80 ms or more hides change; no blank, easy; on-times 200 to 600 ms typical; results in alternations | Rensink, "Change blindness" chapter in Vision and Attention (cs.ubc.ca PDF) | Millisecond flicker paradigm manual (80 ms blank) | yes |
| Central interest changes found faster than marginal | Rensink chapter, Fig 9.2 | O'Regan et al. ARVO 1997 abstract (ubc) | yes |
| Peterson 1959: about 80% at 3 s, about 10% at 18 s | simplypsychology.org Peterson and Peterson | studymind.co.uk Peterson and Peterson | yes (middle points disagree between sources, so cut) |
| Keppel and Underwood 1962: first trial near perfect, proactive interference | simplypsychology.org | tutor2u.net | yes |
| Switching category releases interference | simplypsychology.org (Wickens 1963) | Wikipedia Brown-Peterson task (letters to numbers) | yes |
| Ebbinghaus 1885 forgetting curve, fast then slower | Murre and Dros 2015, PLOS ONE | Wikipedia, Forgetting curve | yes (his numbers cut, a different measure) |
| DRM: lure recalled 40% (12-word lists), 55% (15-word); most called it remembered | Roediger and McDermott 1995 (personality-project.org copy) | Wikipedia, DRM paradigm | yes |
| Encoding, storage, retrieval; reconstruction | OpenStax Psychology 2e, 8.1 | Roediger and McDermott 1995 | yes |
| Loftus and Palmer: about 40 vs 34 mph; broken glass 32% vs 14% | themantic-education.com (40.5, 34.0; 32%, 14%) | simplypsychology.org (40.8, 34.0; "more than twice as likely") | yes for "about 40" and the ratio; exact 40.5 vs 40.8 disagree, so "about 40" |
| 69% of 375 DNA exonerations, 1989 to 2020 | innocenceproject.org DNA exonerations page | deathpenaltyinfo.org (reports the Innocence Project's count) | yes; both rest on one count |
Cut: a typical Müller-Lyer percent (no two sources agree), a published Shadow Squares magnitude, Rensink's exact
seconds, Peterson's middle points, Ebbinghaus's savings numbers, DRM recognition rates (.84, .76 disagree), and
lineup reform claims. The DRM published lists themselves (two copies disagree), so original lists are used.
Number checks run (Python, scratchpad il.py): contrast ratios above; lateral inhibition at k 0, 0.2, 0.4 (values in
Screens, edge bands appear, patch interior 0.30 on both surrounds); flicker 720 ms cycle, 1.39 blanks per second, 83
alternations in 60 s; illusion size formula (fins-in 360 on 300 = +20%, fins-out 255 on 300 = +15%); do-nothing over
100,000 simulated trials averages 0.07% with SD 18.9 (so unmoved trials must be refused, not scored); trigram list
checked for shared letters and acronyms; shadow grays 200 x 0.55 = 110, 220 x 0.55 = 121.

## Done when
1. Focus: on every station's Do step the stimulus is the largest thing on screen at 1366x768, and every control the
   step needs is above the fold with no page scroll; at 680x425 controls come before the hint and nothing is clipped.
2. Line Lengths: 8 trials, no number anywhere before Compare; an unmoved Lock it in is refused; Compare shows 45, 90,
   135 and Controls against the 0 line.
3. Shadow Squares: A and B pixels read the same value (110, then 121) in the canvas; Bridge and Hide the scene work.
4. Inside the Eye: output hidden until a prediction; at k 0.4 Step edge reads 0.58 and 0.08 against 0.48 and 0.18;
   patch interior 0.30 on both surrounds.
5. Spot the Change: blanks run at no more than 1.4 per second; Spotted it freezes at once during flicker (a tap while
   it plays changes the screen immediately); a wrong kind counts as a miss; Motion off starts in Flip by hand.
6. Count Backward: 10 trials, counting taps required, low-count trials hollow; chart shows trial 1 and 10 marked and
   Peterson's two endpoints labeled approximate.
7. Word Lists: lures never visible before Compare; recognition Compare shows studied, unrelated and lure together.
8. No line plays during any measurement; scNoGap is heard whole before scene 7 starts.
9. Notebook keeps first and latest runs across a reload, says results stay on this device, and Reset all confirms.
10. Standards map rows: each check in its Done when column passes.
11. Every on-screen fact matches the Sources table; no em dashes; "Curio Class" never shortened.

## Open questions
- Sensitivity review (rule 5): the culture card in Line Lengths (cross-cultural illusion research, framed as an open
  disagreement) and the Eyewitness card (wrongful convictions). Neither names a people or group.
