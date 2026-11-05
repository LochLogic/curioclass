# Codex report: act-it-out

## Built

Build only, 2026-10-31. No git commit, branch change, stash, or polish round.
Repository changes are confined to tools/act-it-out/. Test artifacts are in the specified Scratch folder.

Implemented Stories and Trunk: three original folktale retellings, 37 beats, Sun/Moon roles, reversible costumes,
both branches of every choice, Swap, Freeze, eight synthesized effects, six settings, 20 costume pieces,
five character questions, surprise outfits, and role-swapped replay. The children supply the acting.

Files include readable src.html, content.json, tool.draft.json with stage built, notes.md, handoff.md,
voice/lines.json, audit-states.json, art/prompts.json, 32 WebP paintings, preview.svg, and the generated offline HTML.
The source's longest line is 153 characters. No em dashes were introduced.

## Numbers check

Recomputed with the WCAG sRGB formula and equal temperament. Evidence: Scratch/numbers.py and numbers.json.

- White/brand 8.174:1; brand/paper 7.485:1; ink/paper 14.466:1; muted/paper 5.871:1.
- Ink/Sun gold 8.661:1; white/Moon navy 10.110:1; white/curtain 11.763:1.
- TRIP TRAP: 450 and 550 Hz, exactly one octave below 900 and 1100 Hz.
- C6, E6, G6: 1046.502, 1318.510, 1567.982 Hz. Oven ding uses the specified 1320 Hz.
- Data counts: 13 goat beats, 13 gingerbread beats, 11 turnip beats, 20 pieces, 32 paintings.
- No differences from the spec's rounded results. No score, acting tolerance, or countdown was added.

## Feel check

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

## Done when

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

## Wave lessons

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

## Audit leads

Audit not finished. Ran the full default audit once on Chrome port 9991, host 8795, with its dedicated Scratch profile.
It was stopped automatically at 30 minutes. It produced 73 PNGs but no audit.md or completed lead list.
Those frames cover home, Trunk, seven specified story/work states, all required sizes, and calm home.
Do not treat the missing report as a clean audit. All 73 captured frames were reviewed in contact sheets.

Manual review of the compact curtain-call frame found the heading clipping against the beat card.
Fixed with a compact grid and side-by-side action buttons; re-shot only 680x425 and 800x500, both clean.
Read/Sound visual interruption was also completed and checked after the audit stop. The full audit was not rerun.
The final localized drive runs report zero console errors, warnings, or exceptions.

## Frames looked at

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

## Art made

26 new kept paintings made with the built-in OpenAI image tool; six existing painted backdrops retained.
One redraw: icing-buttons initially came back on a garment; replaced with three isolated icing disks.
All new paintings have raw PNGs, prompts, drawn_by codex, and processed WebP assets made with art.py --rekey only.
Reviewed the images and their worn placements. No people, human faces, or human body parts were generated.
Toy faces, badges, lighting, soil, frame, labels, and precise control geometry are drawn in code.

32 final WebPs: 1,060,644 bytes, about 1,035.8 KiB.
Final standalone HTML: 1,502,791 bytes, about 1,467.6 KiB, below 2 MB.
The image credit is present in tool.draft.json and the HTML source comment.

## Art still to paint

None. No people assets are needed. The narration manifest is separate from the painting work.

## Engine changes wanted

Optional: kit/curio.js, init Motion button handler, support rememberMotion:false to skip writing curio-motion.
This would support specs asking for strictly memory-only settings. The current standing kit requirement was followed;
no engine file was changed.

## Left open

- The full audit and systematic resize stress check did not finish within the required limit.
- The 87 fixed narration lines are listed with gentle-storyteller/Vindemiatrix but remain unrecorded, per Build instructions.
  Queue behavior was checked in muted Chrome; this was not an audible listening review. Device voices may differ.
- The Gingerbread ending, body-slot replacement, and cumulative costumes across role changes are explicit handoff decisions.
- The complete costume/puppet/size visual cross-product was not individually photographed.

All test Chrome processes and host servers started for this Build are closed. No allowed test port remains listening.
host.html is absent. No git commit was made. Stop here for the cold review.
