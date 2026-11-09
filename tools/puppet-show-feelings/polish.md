# Polish: puppet-show-feelings (Codex fix, round 1)

Verified: both blockers, seven should-fix items and nine accepted polish items. Two items remain NOT FIXED as detailed below.

Evidence paths below are relative to `_scratch/puppet-show-feelings/`. Before frames and JSON were captured from the incoming bundle, before repairs. Failed iframe-selector shots were replaced by `phone-before/` captures inside the 375x812 host.

## Blocker
1. FIXED: All first Show actions open scene 1, including Next, right arrow, Show me, Again and theater. The waiting hint says "Tap Pom to start the show." `before-first-next.json` reached state.scene=1 (the second scene) with only Whoosh; first reveal left started false. Every `after-first-*.json` stays at state.scene=0 and logs welcome, baseline, six 150 ms syllables, question, without cuts. Frames: `before/before-first-next.png`, `after-behavior/after-first-next.png` and the four other first-action frames.
2. FIXED: Backstage Line now cycles four speaking scenes plus the selected ending, with the label and picture following. Before Line 5 was the choice prompt with n=0. `after-line5.json` has the Dot ending and n=8 on change and Say it. Frames: `before/before-line5.png`, `after-behavior/after-line5.png`. `check-line-cycle.json` wraps 2, 3, 4, 5, 1, 2, 3 with syllable counts 8, 7, 5, 8, 6, 8, 7; no choice prompt appears.

## Should fix
1. FIXED: Every change hushes the narrator and starts babble in its handler; the full how-to follows babble. The flip explanation waits for a completed audience result and is remembered only after completion. Before: `before-flip.json` had no babble at the audience tap. After: babble 3535 ms, how 4539 ms, audience 5686 ms, flip 10758 ms (`after-flip.json`). `check-flip-retry.json` shows a Read-cut flip at 10758 ms and a complete retry at 25983 ms; `check-voice-back.json` has the complete how, result, flip in order. Frames in `after-voice1/`.
2. FIXED: A textured foreground shelf ledge hides the cuff, with the puppet base raised enough to remain visible at tall narrow sizes. Before: `before/before-like-1366.png`, `before/before-like-680.png`, `phone-before/before-phone-like.png`. Final: `after-placement-final/after-like-{680,800,1000,1280,1366,1920,760,375}.png`, all viewed. No scrolling or controls below 60 px in their JSON probes.
3. FIXED: Dot sits at left 15% inside the opening beside Pom; the stick points up toward the tree behind both puppets. The rescued kite was also moved clear of Pom's face. Before: `before/before-dot-{1366,1920}.png`, `phone-before/before-phone-dot.png`. After: `after-placement-final/after-dot-{1366,1920,375}.png`, all viewed.
4. FIXED: All six faces have two dot eyes. Worried has raised pinched brows and a wavy mouth; sad has drooping outer brows and a frown; calm has awake dot eyes and a small smile. Compared at actual 27 px phone/compact and 38 px laptop sizes in the before and final Like me frames above.
5. FIXED: All six Like me prompts name Pom's matching story moment first and retain "Tell Pom, or pass." Worried is visible and voiced in final Like me frames. `check-like-all.json` logs happy, excited, worried, sad, proud and calm once each, all complete; `after-voice2-small/check-like-all.png` was viewed.
6. FIXED: A first vote asks "Why do you like that ending? How did it make you feel?" A second tap on the selected tile supplies the preserved example reason; the hint names that tap. Before: `before-vote.json`. After: `after-vote-first.json`, `after-vote-second.json`, and `after-behavior/after-vote-{first,second}.png`. `check-voice-votes.json` logs all three original reasons after their reason-first prompts; `after-voice2-small/check-voice-votes.png` was viewed.
7. FIXED: Notes now say to model a small everyday example, keep it light, speak privately after a worrying disclosure and follow school procedure. `before-notes.txt` lacked that advice; `static-check.txt` confirms the new procedure text. This is teacher guidance, not a student gate.
8. NOT FIXED (full voice proof incomplete): The code, manifest and live allLines now use "Yes! Pom looks X!" and "The audience sees a/an X Pom." `check-voices-0.json` and `check-voices-3.json` prove all six audience lines and five praise lines, including "an excited Pom". Happy praise was not triggered: that probe began with matching settings, and the no-op guard correctly withheld praise. Its revised literal is present in the live manifest, but I did not hear it, so I am not marking this item fully verified. No recordings existed before this repair, and none were made under CODEX-BUILD's no-recording rule.

## Polish accepted
1. FIXED: Show me speaks and displays Head, Voice and Bounce clues. `after-voice2-small/check-clue-card-{1366,680,375}.png` were viewed; each shows "Head up, middle voice, small bounce." The six reveal lines follow each scene's preset.
2. FIXED: Reveal hushes only narration; it no longer changes the babble serial or stops running syllables. `check-reveal-mid-babble.json`: mouth talking before=true and immediately after reveal=true, same six-syllable run. `after-voice3/check-reveal-mid-babble.png` viewed.
3. FIXED: Head controls use drawn sock poses and Bounce uses visibly low/high SVG arcs. `after-layout2/after-back-{1366,680}.png` viewed.
4. FIXED: What changed is 18 px in every layout and includes the old and new icons beside the arrow. Final layout JSON reports 18 px; compact and laptop Backstage frames show both icons.
5. NOT FIXED (phone extreme still clips): Pom is enlarged and all nine controls remain visible at 1366x768 and 680x425. Final frames `after-voice3/after-back-{1366,680}.png` and `fix-audit/state-backstage-big-up-{1366x768,680x425}.png` were viewed. CSS height grew from 88% to 104%, laptop width from 26% to 38%. However, the final full-size `fix-audit/state-backstage-big-up-375x812.png` shows the top of Pom's head clipped at the phone stage edge. The main-size improvement is real, but this regression leaves the item open. The mechanical audit does not detect painted-character clipping.
6. FIXED: Sign typography follows theater width, clamped to at least 10 px and kept on one line. `after-layout2/after-ending-680.png` and `after-placement-final/after-dot-375.png` show text inside the painted sign.
7. FIXED: Try it and Ending vote display a check when on. `after-layout2/after-back-680.png`, `after-vote-1366.png`, `after-vote-680.png` viewed.
8. FIXED: Chosen mode is nowrap with reduced compact padding. Backstage stays on one line in `after-layout2/after-back-680.png`.
9. FIXED: Phone audience card has a 3% right inset and is lower so it clears Pom's face. `after-voice3/after-back-375.png` viewed: the card has space from the stage edge and does not cover the eyes.
10. FIXED: Scene strip now has role img and its current scene label; all three mode icon spans are aria-hidden. `static-check.txt`: 1 scene role and 3 hidden mode icons.

## Settled calls
- Applied both blocker severities: opening skip and silent Line 5.
- Flip follows the audience reading, not the change; interrupted explanations can return.
- Line skips the no-babble ending-choice scene and cycles five lines.
- Applied the sad/worried should-fix priority with visibly different faces.
- Applied the Dot should-fix priority with placement inside the opening.
- Kept "Tell Pom, or pass." and optional disclosure.
- Kept Try it as exploration that can be swept, with no score or mastery claim, as expressly settled. Handoff's older open-blocker wording now records that settlement.
- Kept quick Next interruption behavior and the separate mode navigation.
- No new painted art. The spec's open questions were left untouched.

## Cheats tried
- Blind Down, Slow, Still sweep: Try it check earned. This is the specifically accepted exploration behavior, not an assessment pass. Notes and handoff say so.
- Eight taps on the already selected Still button: zero extra praise.
- Toggle Try it off/on while matching: zero extra praise.
- Cycle all six targets without changing settings: zero extra praise.
- Sweep settings, leave audience hidden, tap Read: reads only Head, Voice and Bounce plus the instruction, with no hidden feeling answer. `check-cheaps.json`.
- Tap Show me without watching: first tap starts the baseline; a later reveal intentionally supplies word and clues. There is no score, check or saved result for naming it.
- Tap every ending or double tap for the narrator's reason without explaining: preferences and example reasons remain available, with no reflection grade, gate, count or saved result. First tap still requests the child's own reason.
- Read while flip is playing, then Audience says again: the interrupted explanation returns and completes. `check-flip-retry.json`.
- Read first, then Back: starts scene 1 without skipping (`check-extra-start.json`). Seven rapid Line/Say it pairs: every line babbles, no silent scene (`check-line-cycle.json`). The original five startup patterns and these extra paths all ran through the tool handlers.

## Voice walk
Held clicks were 120 ms with 2 s gaps; listening waits were added for the long story/question beats. All five opening paths log welcome, baseline, babble, question once with no cuts. Backstage change starts babble before the how-to, then Audience says supplies result and flip. The strict 2 s audience tap cuts the how-to, as its log states; a listening walk completes it (`check-voice-back.json`). The flip is not consumed by an interruption. Six life prompts play once each, in happy, excited, worried, sad, proud, calm order, with no cuts. All six audience wordings and five praise wordings were heard in the smaller probes; happy praise lacks an individual voice proof. All three vote reasons played fully on repeated tile taps. The first rapid repeat can cut the reason-first question by design; the separate first-vote listening frame/log shows it completing before a second tap. Logs: `check-like-all.json`, `check-voices-{0,3}.json`, `check-voice-votes.json`.

The manifest equals allLines(): 117 unique fixed lines (`static-check.txt`). Narration remains the existing browser fallback; there are no MP3 recordings to synchronize.

## Engine changes wanted
No runtime engine change. Existing audit helper request retained in handoff: `scripts/audit_tool.py`, `MODES_JS`, include `nav .seg button` so the separate mode bar is discovered. Authored states and explicit three-mode frames supply coverage here.

## Audit
The single final audit completed with exit 0 within its 40-minute limit. Report: `fix-audit/audit.md`. All eight sizes and eleven authored states are mechanically clean, Motion off has no infinite animation, resize stress has no exceptions or controls left disabled, and console/error columns are empty. No runtime changes followed the audit.

All 97 audit PNGs were inspected on seven contact sheets (`audit-sheets/`); the 1366, 680 and phone Up/Fast/Big frames and phone Dot ending were also opened full size. That visual review found the phone head crop reported under Polish accepted 5. Default Show and all three modes have current 1366 frames. The separate navigation bar is still missed by automatic mode discovery, as documented under Engine changes wanted; authored states and explicit walks cover it.

Four mechanical leads, each answered:
- Quick `#reveal` twice cuts the welcome when the second tap reveals the feeling. Expected: first tap starts the opening, second acts on the reveal. Full first-tap opening was separately proved.
- Quick `#back` twice cuts the welcome while replaying scene 1. Expected responsive navigation; the new scene line proceeds.
- Quick `#next` twice cuts the welcome while moving to scene 2. Expected newest-scene behavior, as settled in refine.md.
- Quick `#again` twice cuts the welcome while replaying the baseline. Expected immediate replay.
These welcome cuts are permitted by `docs/agents/decisions/BASELINE.md` rule 16 and the unlocked story controls. No input lock or forced listening was added. All five-click checks at a 2 s pace are mechanically clean.

Bundle: 1,162 KB, no bundler failure. No console errors in final targeted batches. The first phone host favicon 404 was a harness request; subsequent host runs use a data favicon. A combined six-example voice probe hit drive's 60 s evaluation limit and was retried once as two smaller probes; both completed. No new recordings exist, so the bundle uses the established browser fallback.

## Left open
- Should fix 8: happy praise's revised literal exists, but its individual spoken proof is incomplete. Exact follow-up: Backstage, Try it on, Next target three times to happy, Head Down then Up, inspect vlog for "Yes! Pom looks happy!". The other five praise lines and all six audience lines have complete spoken entries.
- Polish accepted 5: Up/Fast/Big clips the top of Pom's head on the phone. Bound phone puppet size/base against its full bounce and recheck Up/Big and Down/Big at 375x812. No post-audit runtime repair was made.
- The spec's explicit open questions stay with the integrator. No recordings were made under CODEX-BUILD's rule. Try it stays sweepable exploration by the settled call.

## Feel check
Best moment: Dot is now visibly beside Pom while the stick reaches into the tree. The two flat moments were a first instruction that skipped the opening and the silent Line 5; both now play. The original painted theater, texture and mouth frames are retained. `fix-bar-comparison.png` puts the repaired scene beside the current Beat Lab frame; the K-2 theater retains comparable visual care. `fix-grayscale.png` preserves legible labels and selected checks. Both were viewed. The existing Beat Lab bundle was opened read-only because writes outside this tool and Scratch are forbidden.

## Numbers and coverage
All 27 results match the spec table: sad 4, worried 7, calm 3, proud 3, happy 5, excited 5. Immediate change-to-babble-call latency is 0.1 ms in `check-immediate.json`. The final live allLines array equals the 117-line manifest. No art was generated or rekeyed. Default Show and every mode were re-shot at 1366x768. All named phone checks use an actual 375x812 iframe on host port 8715; Chrome used 9910 and audit 9911. Motion-off frames, keyboard opening and grayscale were checked. Existing files and pre-existing work were preserved; no commits or spec/refine edits.

## Assumptions made unattended
Followed the explicit settled choices: five Backstage lines, flip after a reading, optional passing, original vote reasons on request, and sweepable Try it as exploration. The existing browser narrator stays because CODEX-BUILD prohibits recording; no incompatible clips exist. The spec's open questions remain for the integrator.

Offline static check: zero external src/href resource attributes, zero remote CSS references, zero fetch calls in the bundled HTML (`final-numbers.json`).

## To the spec's open questions
Left the spec unchanged. Its five-line cycle, revised voice copy and art-route text drift remain assigned to the integrator, as refine.md requests.

## Not taken
- Kept "all by herself" in the original new-kite ending.
- Did not add a spec-drift note to notes.md; that belongs to the spec's open questions.

Cleanup verified: Chrome ports 9910 and 9911 and host port 8715 are closed; temporary host.html is removed. No git commits were made.
