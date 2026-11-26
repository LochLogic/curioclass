# Act It Out: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: act-it-out

#### Built

Build only, 2026-10-31. No git commit, branch change, stash, or polish round.
Repository changes are confined to tools/act-it-out/. Test artifacts are in the specified Scratch folder.

Implemented Stories and Trunk: three original folktale retellings, 37 beats, Sun/Moon roles, reversible costumes,
both branches of every choice, Swap, Freeze, eight synthesized effects, six settings, 20 costume pieces,
five character questions, surprise outfits, and role-swapped replay. The children supply the acting.

Files include readable src.html, content.json, tool.draft.json with stage built, notes.md, handoff.md,
voice/lines.json, audit-states.json, art/prompts.json, 32 WebP paintings, preview.svg, and the generated offline HTML.
The source's longest line is 153 characters. No em dashes were introduced.

#### Numbers check

Recomputed with the WCAG sRGB formula and equal temperament. Evidence: Scratch/numbers.py and numbers.json.

- White/brand 8.174:1; brand/paper 7.485:1; ink/paper 14.466:1; muted/paper 5.871:1.
- Ink/Sun gold 8.661:1; white/Moon navy 10.110:1; white/curtain 11.763:1.
- TRIP TRAP: 450 and 550 Hz, exactly one octave below 900 and 1100 Hz.
- C6, E6, G6: 1046.502, 1318.510, 1567.982 Hz. Oven ding uses the specified 1320 Hz.
- Data counts: 13 goat beats, 13 gingerbread beats, 11 turnip beats, 20 pieces, 32 paintings.
- No differences from the spec's rounded results. No score, acting tolerance, or countdown was added.

#### Feel check

Played through the story paths and Trunk as a desktop rehearsal of the child-facing experience, not a classroom trial.

- Best moment: the turnip becomes enormous, pops free with a soft sound, and the gold frame invites the class's funny frozen heap.
- Flat moment 1: the first story title delayed the actual story narration at a fast tap pace. The beat now starts first;
  its title follows only while that first beat remains open. The 2-second held-click log starts every visited beat.
- Flat moment 2: early dressing feedback was a generic upward movement. New pieces now fly from the actual trunk location
  to their puppet anchors, with a three-note sparkle. The enlarged Trunk puppet makes unusual outfits worth inspecting.
- Corrected stretched puppet proportions, hat anchors that covered faces, and a clipped compact curtain-call heading.
- Compared the final turnip freeze picture beside Snowy Mail Route in Scratch/bar-comparison.png.
  Also bundled and opened Beat Lab before building. The painted settings, costumes, lighting, and readable foreground
  have sufficient visual weight beside the bar tool. This is a theater activity, so the toys do not perform for the class.

#### Done when

1. PASS with the spec's required choice taps: all 37 beats reach their endings; Back restores exact prior costumes.
   functional-results.json has no failures. all-beat-voice.json logs every beat as spoken on its visit.
   Goat beat 1 appears twice because the test starts that story twice. Literal Next-only conflicts with the Choose rule.
2. PASS: role badges, active lighting, swapped text, swapped outfits, and subsequent assignments were checked.
   Evidence: functional run, goat-costume and swap-and-freeze frames at every size.
3. PASS: Next locks before a choice, unlocks after it, and both voice/movement branches match their selection.
   Both bear and mouse paths reach the mouse beat; the bear adds a spoken line without adding a beat.
4. PASS: Freeze and Unfreeze work in both modes, are repeatable event lines, and Next clears Freeze.
   The gold frame and O mouths are visible in the goat and turnip frames.
5. PASS for functionality and reviewed anchors: replacement/removal, 100 surprise outfits without duplicate places,
   all five questions, and all eight sound controls were exercised. All 20 pieces were inspected on both wooden toys
   in recheck/gallery.png; representative multi-piece outfits were inspected at every required size.
   The full 20-piece by two-puppet by eight-size visual cross-product was not individually photographed.
6. PASS: at 1366x768 and 680x425 the active costumed puppet has the spotlight and central visual focus.
   The Trunk puppet is the dominant foreground object; its large-screen height cap was increased to 620 px.
7. PASS in targeted checks: advancing, returning, swapping, and freezing interrupt existing narration and transitions.
   Final Read/Sound checks also report readSettled, soundSettled, finalGrowth, and readLogged all true.
8. PASS for queue behavior: held clicks at 2-second intervals start each visited story line; stale how-to lines drop.
   After the class pauses at Choose, chooseHint speaks once. Freeze and Unfreeze each start their event line.
   Narration uses browser speech fallback; recordings were intentionally not made in this Build.
9. PASS in the size sweep: every measured control is at least 60 px, no horizontal overflow, and main bars stay visible.
   Keyboard Tab, Enter, and Right arrow reach the goat act beat with focus on Next.
   The final compact ending checks confirm its title is below the beat card and Home is above the teacher bar.
10. PASS for calm behavior and tool state: zero running animations; turnip scales step through .25, .6, then full size.
    Story/outfit progress is memory-only and resource checks show no tool network requests.
    The required kit still remembers the shared Motion preference; this spec conflict is recorded in handoff.md.

#### Wave lessons

- PASS, Hint and voice: hints update synchronously, Read uses the current beat/hint, how-to selection uses V.heard,
  and the choice hint names the choice controls while Next is disabled. Muted voice logs are preserved.
- PASS, Focus and layout: permanent button nodes, no focus on load, intentional preventScroll focus transfers
  to choices/replay when Next becomes disabled, and a successful keyboard-only path.
- PASS, Sizes: all eight required sizes, including the real 375x812 iframe host, plus localized compact-ending rechecks.
- PASS, No giveaways: both creative interpretations are valid; there is no hidden-answer quiz or score to reveal.
- PASS, Honest numbers: only exact beat counts are displayed; no unsupported performance or learning estimate.
- PASS, Standards: actual child actions use body, expression, voice, imaginary costumes, sound, choices, and performance.
  Teacher notes distinguish Kindergarten modeling, grade 1 characterization, and grade 2 intentional interpretation.
- PASS, Motion off: explicit animation:none for doll sway; no running animation in the calm checks; discrete growth steps.
- PASS, Short choices visible: both story choices remain visible together at the smallest preview and phone sizes.
- FAIL, Resize mid-animation audit: the automated resize/stress phase did not finish before the audit deadline.
  Responsive snapshots passed, but a completed systematic resize stress result is not claimed.
- PASS, Welcome timing: the kit decides after the first action; a story's own line suppresses a stale home welcome.
- PASS, Unknown as unknown: no hidden diagnostic state or undisclosed factual clue is used in this activity.
- PASS, One look, one meaning: Sun/Moon retain their icon, word, and side; active light indicates who acts.
- PASS, Badge truth: actor labels and spoken side names follow the same swapped-role mapping as costumes.
- PASS, Hint changes back: Back, Home, Stories, Trunk, and choice changes update the applicable hint immediately.
- PASS, No answer by copying: the choices intentionally name alternative acting interpretations, not a factual answer.

#### Audit leads

Audit not finished. Ran the full default audit once on Chrome port 9991, host 8795, with its dedicated Scratch profile.
It was stopped automatically at 30 minutes. It produced 73 PNGs but no audit.md or completed lead list.
Those frames cover home, Trunk, seven specified story/work states, all required sizes, and calm home.
Do not treat the missing report as a clean audit. All 73 captured frames were reviewed in contact sheets.

Manual review of the compact curtain-call frame found the heading clipping against the beat card.
Fixed with a compact grid and side-by-side action buttons; re-shot only 680x425 and 800x500, both clean.
Read/Sound visual interruption was also completed and checked after the audit stop. The full audit was not rerun.
The final localized drive runs report zero console errors, warnings, or exceptions.

#### Frames looked at

Scratch root: S:/CurioClass-codex/_scratch/act-it-out.

- bars/: Snowy Mail Route and Beat Lab; bar-comparison.png.
- early/, fit/, functional/: first play, corrected proportions, Trunk, and story costume checks.
- sizes/: all three views at all eight sizes; sizes-sheet.png.
- phone-final/: corrected iframe measurements and final phone proportions, all three views.
- detail/: choices, goat Freeze, gingerbread fox, growing/grown/popped turnip, curtain call, calm, grayscale, keyboard,
  voice pace, and costume gallery; detail-sheet.png.
- recheck/: all 20 pieces on both puppets, large-screen Trunk, voice pace, and discrete calm growth.
- voice-check/: every beat event, then a pause allowing the first choice how-to to finish.
- audit/: all 73 PNGs, reviewed in audit-sheet-0.png through audit-sheet-6.png; compact ending also inspected full size.
- final-check/: Read/Sound interruption and the final crown outfit.
- ending-fix/: both corrected compact endings, inspected full size with positive geometry checks.
- art-sheet.png: all paintings. The incorrect initial icing garment is visible in older frames and was replaced.

The first phone harness attempt addressed the host document instead of its iframe and requested a host favicon.
Corrected the test harness, suppressed that host-only favicon request, and re-shot only the phone states.
Final phone measurements: 375x812, no small controls, no off-screen main bar, no horizontal scroll, no tool requests.

#### Art made

26 new kept paintings made with the built-in OpenAI image tool; six existing painted backdrops retained.
One redraw: icing-buttons initially came back on a garment; replaced with three isolated icing disks.
All new paintings have raw PNGs, prompts, drawn_by codex, and processed WebP assets made with art.py --rekey only.
Reviewed the images and their worn placements. No people, human faces, or human body parts were generated.
Toy faces, badges, lighting, soil, frame, labels, and precise control geometry are drawn in code.

32 final WebPs: 1,060,644 bytes, about 1,035.8 KiB.
Final standalone HTML: 1,502,791 bytes, about 1,467.6 KiB, below 2 MB.
The image credit is present in tool.draft.json and the HTML source comment.

#### Art still to paint

None. No people assets are needed. The narration manifest is separate from the painting work.

#### Engine changes wanted

Optional: kit/curio.js, init Motion button handler, support rememberMotion:false to skip writing curio-motion.
This would support specs asking for strictly memory-only settings. The current standing kit requirement was followed;
no engine file was changed.

#### Left open

- The full audit and systematic resize stress check did not finish within the required limit.
- The 87 fixed narration lines are listed with gentle-storyteller/Vindemiatrix but remain unrecorded, per Build instructions.
  Queue behavior was checked in muted Chrome; this was not an audible listening review. Device voices may differ.
- The Gingerbread ending, body-slot replacement, and cumulative costumes across role changes are explicit handoff decisions.
- The complete costume/puppet/size visual cross-product was not individually photographed.

All test Chrome processes and host servers started for this Build are closed. No allowed test port remains listening.
host.html is absent. No git commit was made. Stop here for the cold review.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: act-it-out

#### Played

Played as a K-2 child and a projecting teacher: all three tales to their endings, choices and Trunk, before reading builder notes or source.
The painted theater and dressing are strong; children supply the performance. This was a desktop rehearsal, not a classroom trial.

#### Findings fixed

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

#### Findings left

- Should fix, spec conflict, Gingerbread beat 2: the script requests icing buttons AND candy bow tie, but both occupy the single body slot, so the bow replaces the buttons. A second slot or a special pairing would contradict the explicit costume rule; left under CODEX-REVIEW step 3.
- Should fix, spec conflict, character changes: cumulative costume places leave the pig snout/apron on the fox and earlier pieces on the mouse. Automatic clearing would contradict the supplied cumulative rule; no new costume rule was invented.
- Should fix, instruction conflict, narration: 128 fixed lines have exact manifests but no recordings. CODEX-BUILD explicitly forbids recording audio. Browser speech remains; the requested named recorded voice is not delivered.

#### Flattest moment left

The curtain call is the same generic end card for every tale. The class's own performance supplies the earned ending; no new reward system was added.

#### Graphics

Inspected all 32 paintings, all 20 costume pieces on both toys at useful stage scale, representative outfits at all required sizes, and the redrawn mouse ears at final asset size.
Retained all six backgrounds and 26 cutout assets; replaced one painting. Every asset explicitly says people:false; no humans or stereotyped portrayals are present.
Art 1,035.3 KiB; standalone bundle 1,471.0 KiB (bundler display 1,469 KB). No missing art tokens. Original paintings and rich stage styling kept.
Compared existing Snowy Mail Route and Beat Lab bundles without regenerating or writing either tool; the side-by-side frame is review-bar-comparison.png in Scratch.

#### Audit

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

#### Left open

Literal Next-only completion conflicts with the required choice gate; the gate is retained. Nothing-stored wording conflicts with required kit Motion settings; progress/outfits are memory-only and notes state the kit preference behavior.
The traditional gentle Gingerbread ending is retained pending the spec's open question. No new topics, scoring or automatic acting were added.
The complete 20-piece by two-puppet by eight-size visual cross-product was not individually photographed. No classroom or audible narration trial is claimed.
Final source stays readable (longest line 153 characters). No em dashes, commits, kit edits, or writes outside the two allowed folders. All review Chrome/server processes were closed and host.html removed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Act It Out build handoff

#### Files and structure

`src.html` starts from the kit starter and uses kit CSS, controls, audio context, and Curio.voice.
The page has permanent home, story, and Trunk containers. Buttons retain their DOM identities and focus.
`content.json` holds the three exact retellings, beat metadata, costume places, questions, sound names, and every voice line.
`art/prompts.json` retains the six existing backdrops and adds the missing 26 painted assets.
All image tokens occur once in the ART table; static image elements use data-art so the bundle does not duplicate paintings.

`state.outfits` is rebuilt by folding costume assignments from beat 1 through the current beat.
Swapping XORs the role-to-side mapping, including line names, active badges, and later costumes.
Choices are keyed by beat index, retained on Back, and may be changed there.
Trunk outfit and backdrop are independent of story state and persist across mode changes in memory.

#### Narration and interruption

The Curio.voice scope is mode plus story. Each beat has a visit revision used by valid checks.
The first story beat starts speaking immediately; its title follows only if that first beat remains open.
Read and Sound also settle any visual transition immediately while preserving their kit handlers.
Every new action stops speech, finishes and cancels transient animations, clears pending visual timers,
and stops tool sound nodes before applying the next state. No UI action waits for a line or animation.
How-to lines use V.heard; story visits and action lines are events. Read speaks the current beat plus its hint.
`voice/lines.json` contains the requested voice and both role-name variants. No narration was recorded, per Build instructions.

#### Spec decisions and ambiguities

- Open question: keep the classic Gingerbread Boy ending, gently told, as the supplied beat list leans toward.
- The first Done when says Next only, while Choose explicitly disables Next until a choice. Choose takes precedence:
  all stories finish with Next plus their required choice tap. There is no automatic choice.
- Icing buttons and candy bow tie share the body place. The spec's one-piece-per-place rule means the bow replaces
  the buttons in Gingerbread beat 2. Both are painted and usable individually in Trunk. A separate neck slot would
  require an owner-approved content change; the builder did not introduce one.
- Costume assignments persist in the other places when a role changes. For example, the fox's new head and tail
  do not implicitly remove the earlier apron or pig snout. This follows the cumulative per-place rule; review the
  intended combination before changing it.
- The art list calls the six settings kitchen, road, river, and garden in the beat shorthand. Content uses the exact
  art names cottage-kitchen, country-road, wide-river, and veggie-garden.
- Puppet cutouts are narrow lathe-turned toys. Their natural aspect ratio and face coordinate system are used,
  rather than stretching them into the requested image canvas aspect.
- Nothing saves story progress or outfits. The required shared kit still remembers the Motion preference.
- The six pre-existing backdrop images remain. New cutouts were made with the built-in image tool, per the user's request.
- The report is written last because the user's explicit stop-on-report instruction overrides the brief's early-report advice.

#### Engine changes wanted

`kit/curio.js`, init Motion handler: optionally support an in-memory preference for tools whose spec requests no storage.
The current kit always writes curio-motion. This tool follows the standing kit requirement and makes no kit change.

#### Validation and remaining work

##### Cold review, 2026-11-03

The cold reviewer played all stories and Trunk before reading this handoff or the source.
Review commands use Chrome 9960 to 9967 and host 8765, superseding the builder's ports below.
The one-pass review keeps all changes in tools/act-it-out and _scratch/act-it-out; no commits.

Changes: the current hint is a single visible node moved between home, story footer, and Trunk.
The home hint explains solo parts, classroom sides, and personal-space mime. Acting/dressing use the acting hint.
The selected bear branch now owns the visible card and Read, rather than narrating over a conflicting Choose card.
Piece taps speak on/off event lines; Ask includes a once-per-load next-action cue. All are in both line manifests.
Trunk welcomes may return on a fresh mode entry if an earlier welcome never started.
Inactive toys dim with brightness rather than becoming transparent. Trunk has the same gentle idle sway, stopped by Freeze/Motion.
Mouse ears were redrawn as a plain grey felt headband, without the unrequested bow, and rekeyed through art.py.
The turnip soil now hides its lower half and leaves a dark hole after the pop; calm growth uses the full four seconds.
Sound-effect taps have a visible flash with Motion off. The specified story-start title event follows the immediate first beat.
Sound on after silent dressing can deliver an unheard Trunk welcome. Swap on the growing turnip keeps the settled giant visible.
Garden dressing places the decorative trunk in spare foreground space; the phone Trunk chest clears the puppet's feet.
Background side badges hide during the curtain call, preventing the phone heading overlap.

Still governed by the spec ambiguities above: no extra body slot or automatic costume clearing was introduced.
Those changes would contradict the explicit one-piece-per-place/cumulative rules, so the cold review leaves them open.
The narration manifest is complete but no recordings were made, because CODEX-BUILD forbids recording audio.
Final review evidence and the single audit outcome are in codex-review.md when completed.

The review audit completed once within its 40-minute limit, with 14 machine leads and 89 frames.
The resize stress stage finished without exceptions or controls left disabled. Visual overlap leads were confirmed and fixed.
Welcome suppression after a story's own first-tap line, intentional rapid-tap speech cuts, and unscrolled wardrobe targets
are interpreted against the actual interaction rules, not treated as missing narration or dead buttons.
Only the affected states and voice interruption cases were re-shot afterward; no second full audit was run.

##### Original build validation (historical)

The audit reached its 30-minute cap without producing audit.md. Its 73 frames are preserved in Scratch.
After that stop, Read/Sound interruption was checked separately. A clipped compact curtain-call heading was
fixed with a two-column button row and re-shot at 680x425 and 800x500. The full audit was not rerun.
See codex-report.md for the Build evidence, frame paths, and honest limits. Scratch is
S:/CurioClass-codex/_scratch/act-it-out. Only ports 9990 to 9997 and host 8795 are allowed for this work.
Build only. No commit and no polish round. A cold review is the next workflow step.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
