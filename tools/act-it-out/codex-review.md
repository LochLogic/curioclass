# Codex review: act-it-out

## Played

Played as a K-2 child and a projecting teacher: all three tales to their endings, choices and Trunk, before reading builder notes or source.
The painted theater and dressing are strong; children supply the performance. This was a desktop rehearsal, not a classroom trial.

## Findings fixed

- Should fix, general, Story/Home/Trunk hints: the only shared hint was visually hidden. One visible hint now follows the current mode, with reserved footer height in Stories.
- Should fix, general, first screen: solo parts, classroom side assignment and personal-space mime were only in notes. The opening hint and Read now explain them.
- Should fix, general, turnip bear choice: a bear event spoke over the old choice question, and Read repeated the question. The card, actor badge, Read and next-action cue now match the bear branch.
- Should fix, general, Trunk Ask: questions ended without a next action. Added a visible action cue, spoken once, while the five questions remain repeatable events.
- Should fix, general, Trunk costumes: nonreaders got no spoken selection feedback. Every put-on/take-off action now names its piece, with exact manifest entries.
- Should fix, general, Trunk welcome: a skipped welcome became permanently ineligible after any costume tap. Fresh mode entry and Sound on after silent dressing can deliver an unheard welcome.
- Should fix, general, dimming: inactive and choosing puppets became transparent over busy paintings. They now dim without showing the scenery through their bodies.
- Should fix, general, puppet face/buttons: walnut expressions were hard to see, and icing buttons stretched into narrow ovals. Added a subtle warm face halo and preserved button aspect ratio.
- Should fix, general, calm interaction: story sound-effect taps had no visible response with Motion off. A brief button flash now confirms them in both motion settings.
- Should fix, general, turnip: the root floated above the soil and calm growth finished early. A deeper textured soil band hides its lower half; calm growth finishes at four seconds.
- Blocker, general, turnip Swap during growth: a nonmoving repaint reset the giant root to invisible without restarting growth. It now retains the settled giant; Swap, Freeze and Read interruptions were rechecked.
- Should fix, general, audit-confirmed overlaps: moved the garden dress-up trunk away from the turnip, cleared the phone Trunk puppet's foot, and hid background side badges during curtain call.
- Polish, general, flattest moment: the stuck-to-pop transition now reveals the whole root above a shaded empty hole. Trunk has gentle idle life; Freeze and Motion off stop it.
- Should fix, general, mouse-ears art: the original added a large unrequested polka-dot bow. Redrew plain grey felt ears in the existing painted style and inspected the keyed asset and both worn placements.

## Findings left

- Should fix, spec conflict, Gingerbread beat 2: the script requests icing buttons AND candy bow tie, but both occupy the single body slot, so the bow replaces the buttons. A second slot or a special pairing would contradict the explicit costume rule; left under CODEX-REVIEW step 3.
- Should fix, spec conflict, character changes: cumulative costume places leave the pig snout/apron on the fox and earlier pieces on the mouse. Automatic clearing would contradict the supplied cumulative rule; no new costume rule was invented.
- Should fix, instruction conflict, narration: 128 fixed lines have exact manifests but no recordings. CODEX-BUILD explicitly forbids recording audio. Browser speech remains; the requested named recorded voice is not delivered.

## Flattest moment left

The curtain call is the same generic end card for every tale. The class's own performance supplies the earned ending; no new reward system was added.

## Graphics

Inspected all 32 paintings, all 20 costume pieces on both toys at useful stage scale, representative outfits at all required sizes, and the redrawn mouse ears at final asset size.
Retained all six backgrounds and 26 cutout assets; replaced one painting. Every asset explicitly says people:false; no humans or stereotyped portrayals are present.
Art 1,035.3 KiB; standalone bundle 1,471.0 KiB (bundler display 1,469 KB). No missing art tokens. Original paintings and rich stage styling kept.
Compared existing Snowy Mail Route and Beat Lab bundles without regenerating or writing either tool; the side-by-side frame is review-bar-comparison.png in Scratch.

## Audit

Completed once in about 35 minutes, within the 40-minute limit: 14 machine leads and 89 inspected frames. Resize stress finished cleanly, with no exceptions or controls left disabled.
Confirmed visual leads fixed: turnip/trunk overlap at all sizes, both background badge/end-heading overlaps on phones, and the phone Trunk chest covering a foot. Targeted rechecks found zero covered sample points on all eight buried-turnip sizes and on the phone Trunk puppet; end badges hide correctly.
Expected/false-positive voice flags: a story tile's own beat suppresses the home welcome, Sound off stops speech, and rapid mode/Motion taps hush a welcome. STANDARDS says to mark it heard at its start and avoid repeating it; forcing it back would nag or play after its moment.
The shawl/cape "nothing changed" rows and off-screen/covered wardrobe targets were unscrolled long-tray targets. Scrolling the tray, then using real held clicks, selects each piece and speaks its name. Both scrolled controls passed.
The full audit preceded the final narrow repairs. Only affected frames and growth/Sound interruption cases were re-shot; no second full audit or review round was run. The specified story-start title events remain.

Independent checks: all 37 beats and both branches; exact Back costumes; Swap; Freeze; 100 valid 3/4-piece surprises; replacement/removal; five-question cycle; memory-only outfit retention; growth interruption; keyboard; grayscale; real 375x812 iframe.
All seven contrast ratios independently match the spec (5.87:1 to 14.47:1); octave frequencies 450/550 Hz and sparkle pitches match. Three tales have 13/13/11 beats; 20 pieces and 32 images.
Motion-off samples are scale .25, .6, then full at four seconds, with zero running infinite animations. No tool resource requests or console errors in the targeted drive batches.

| Voice line | Kind | Expected starts | Observed |
| --- | --- | --- | --- |
| Freeze / Unfreeze | event | 5 / 5 | 5 / 5 |
| Ask questions over 6 taps | event | 2,1,1,1,1 | 2,1,1,1,1 |
| Ask next-action cue | how | 1 | 1 |
| Story beats at 2-second taps | event | 6 | 6 |
| Trunk welcome after silent dressing | welcome | 1 | 1 |

Read interruption, Sound off Read, rapid mode changes and stale-queue clearing were checked with held input. Spoken starts were logged in muted Chrome; this is not an audible quality review.
Wave checks: immediate hints/Read, permanent control identities, focus transfer and keyboard path, 60 px targets, no hidden-answer quiz, honest beat counts, all five theater standards through acting/choices/voice/performance, Motion off, visible short choices, and state-restored hints were checked.
Evidence: _scratch/act-it-out/review-*-frames, review-*-sheet-*.jpg, review-functional-result.json, review-numbers.json, review-static-result.json and review-audit/.

## Left open

Literal Next-only completion conflicts with the required choice gate; the gate is retained. Nothing-stored wording conflicts with required kit Motion settings; progress/outfits are memory-only and notes state the kit preference behavior.
The traditional gentle Gingerbread ending is retained pending the spec's open question. No new topics, scoring or automatic acting were added.
The complete 20-piece by two-puppet by eight-size visual cross-product was not individually photographed. No classroom or audible narration trial is claimed.
Final source stays readable (longest line 153 characters). No em dashes, commits, kit edits, or writes outside the two allowed folders. All review Chrome/server processes were closed and host.html removed.
