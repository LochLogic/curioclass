# Codex report: art-style-match

## Built

Look, Match, Make and Album, with 18 authentic museum works, 10 tells, 6 recipes and 4 layered scenes.
Built from the kit starter with Curio.voice. Sources and labels live in content.json. No shared source was changed.
The missing art-museum family engine is handled by a tool-local adapter; see Engine changes wanted.
The offline bundle, teacher notes, lesson plan, voice manifest, art manifest and audit states are included.
Build only. No commit, branch change, upload, deployment or polish round.

## Numbers check

PASS: all 18 tell sets are subsets of their recipe and identify their own style uniquely.
PASS: gold, tiny, smooth, shadow, dabs, dots and thick each fit one style. Flat, outline and outdoor each fit two.
PASS: no pair of recipes shares two tells. Exactly 6 of the 1,024 toggle mixes name a style.
Contrast ratios: white/brand 7.54; brand/card 7.00; ink/card 14.91; card/felt 10.63; muted/card 6.00; ink/gold 7.37.
Evidence: Scratch/numbers-check.json. These match the spec's rounded values.
Spec inconsistency preserved: the Van Gogh row says late 1880s but includes Irises, 1890. Not silently broadened.

## Feel check

Best moment: the Bold outlines card fits two recipes, then Thick wavy paint flips up the style choices. The clues visibly stick.
The second payoff is repainting the same scene with dots, then dabs, then raised curving strokes, and comparing it with a collected work.
Flattest moment 1: the first thick-paint treatment looked like wirework. Softened raised edges and cleaned noisy region boundaries.
Flattest moment 2: the artist step crowded the small panel. Its three cards now occupy the hand's space and remain fully visible.
The rendered table has real felt, paper shading, gold card backs, gilt frames and large authentic works. Make uses every generated asset.
Opened both bar tools. Sources were read before building; their Scratch bundles were opened after the first playable version.
The tool and Snowy Mail Route are placed beside each other in the comparison below. Beat Lab was also opened and inspected.
![Art Style Match beside the bar tool](../../../_scratch/art-style-match/bar-comparison.jpg)

## Done when

1. PASS: 18 complete work records, correct classroom labels, images and tell spots reviewed. Pins and zoom driven in Look.
   All works were also opened as Match frames; the final museum contact sheet and pin sheets were inspected.
2. PASS: held clicks on bedroom, outline alone gives two styles; thick then reveals all six choices. held/held-shared-680.png.
3. PASS: all 18 matched from deals. 1,440 further trades kept a useful tell and a ten-card partition with no duplicates.
   New painting visited 18 distinct unmatched works. Evidence: game-evidence.json, input/trade-deck.png, skip-evidence.json.
4. PASS: 18 collected, 18 restored on reload, Clear confirmation emptied storage and showed albumEmpty. deep/ frames.
5. PASS: 24 scene/recipe combinations named the exact recipe. Non-recipes named Your own style. Every effect is implemented.
   Measured warm renders 29-105 ms; the final willow's thick recipe took 131 ms at 1920x1080. First scene preparation is separate.
   Rapid changes completed with the newest mix. Export decoded as a 1600x1000 PNG; three native downloads also verified at that size.
   Evidence: brush-evidence.json, Scratch/downloads/ and final/ frames.
6. PASS: painting and canvas remain the central, largest stage objects. Final Match image is 47.26% of the stage height at 1366x768.
   Artist choices fit at 680x425 and 375x812. Evidence: final-match-evidence.json, last/artist-680.png, last/phone-artist.png.
7. PASS: held taps during zoom changed to the next work without a stale zoom or hint; rapid Make toggles canceled the prior worker.
8. PASS: how-to lines started once across five repeats; miss started 5 times; won started 5 times. Stale lines were dropped.
   Read retained priority. Anonymous wins now say Into the album first. Evidence: voice-how.json, voice-miss.json, won-five.json.
9. PASS: hand, painting and Deal fit all eight standards sizes, including the 375-pixel iframe host. Full size sweep plus targeted fixes.
10. PASS: 1,573,256 bytes, below 2 MB. Bundles cleanly with CURIO_DRAFT=1; no placeholder assets.

## Wave lessons

- Hint and voice: PASS. Hints change synchronously, Read uses the hint or wall label, and the kit tracks heard how-to lines.
- Focus and layout: PASS after follow-up fixes. Open moves focus to Tells; Show style moves to Next; zoom preserves a painting target.
  No focus on initial load. Header labels reserve their width, so toggling does not shift controls. Rebuilt artist choices receive focus intentionally. All programmatic focus uses preventScroll.
- Sizes: PASS for primary controls. 44-pixel minimums, stable hint space, all eight sizes inspected. Album's long grid scrolls.
- No giveaways: PASS against the spec. Style names stay hidden until tells identify one recipe; Match hides artist labels.
  Van Gogh's name is part of the specified style name. Other artist choices are shuffled and drawn from different styles.
- Honest numbers: PASS. No score, timer or fabricated estimate. The six recipes are identified as classroom simplifications in notes.
- Standards: PASS for the requested solo activities. Students locate evidence and connect works with book, painting and print contexts.
  The recipe-feedback wording concern remains for the cold teaching review, as noted below.
- Motion off: PASS. The waiting-card loop is explicitly stopped; the browser reported zero infinite animations in calm mode.
- Short choice sets: PASS after fixes. Four tells, six style cards and three artist choices fit. Make controls use compact rows when needed.
- Resize mid-animation: PASS after a real backing-buffer fix. Fixed-work CDP resizes preserved all four tested states with zero exceptions.
  Final Make buffer equals its displayed 690x424 size; see resize-followup.json and followups/resize-*.png.
- Deferred welcome: PASS. No welcomeAfter; welcomes are scoped to modes and the applicable waiting state.
- Unknown shown as unknown: PASS. Face-down style cards, hidden Look styles and empty Album slots disclose no guessed identity.
- One look, one meaning: PASS. The same tell icons are used in Look pins, hand cards, recipes and Make toggles.
- Badge truth: PASS. Exact recipes alone receive a style label; other mixes receive Your own style. Album count follows storage state.
- Hint changes back: PASS. Modes, deselection, zoom-out, reset and cleared Album update the next-action hint immediately.
- No answer by copying words: PASS for the visible-tell task. The student chooses a tell from the image before the style names appear.

## Audit leads

Completed once with exit 0 on port 9981 and host 8785. Original audit: 80 repeated leads, zero runtime errors.
The original report is retained at ../../../_scratch/art-style-match/audit/audit.md. Every lead class is answered here:
- Read/Tells/Next/Close small targets: FIXED. Header, mode and control minimum widths are 44 pixels. Final 680 scan: no small targets.
- Focus lost opening a painting: FIXED. Opening focuses Tells, Show style focuses Next, and a zoomed pin transfers focus to the painting.
  Replacing a gallery card with an opened view is intentional navigation; its former DOM node is necessarily replaced.
- Deal/New painting rebuilt and lost focus: FIXED. The rebuilt control with the same id retains focus. Follow-up ended on new-painting.
- Picture-target/tell-pin overlap: INTENTIONAL. Pins overlay the painting at the required fractional spots and intercept their own taps.
  The audit reports each pin's overlap with the full-picture zoom button. Pin-to-pin positions were spaced and edge targets clamped.
- Seventeen resize identity leads: NOT DISABLED CONTROLS. Separate randomized loads show different paintings, so labels do not match.
  Same-work 1366 to 760 to 1366 tests kept picture controls enabled, the work ids unchanged, and all three artist choices available.
  That follow-up found a separate Make backing-buffer issue; it was fixed and rechecked at matching display resolution.
- Sound moved six other header controls: FIXED. Sound and Motion reserve their widths. Held toggle follow-up: zero header controls moved.
- Eighteen gallery-first welcomes not heard: EXPECTED. The spec makes welcomeLook stale once a card opens; lookOpen speaks the next action.
  No old gallery welcome is replayed over the opened work. Make's welcome likewise expires after a recipe/tell action.
- Four active-mode double taps cut welcomes: FIXED. Re-selecting the active mode does not hush its speech or rebuild the mode.
  Held taps 0.7 seconds apart recorded one welcome and zero cuts in each mode.
- Clean audit rows confirmed: all other size/mode states, infinite-motion check, per-control console checks, and five-click mode tests.
Only affected flows were rechecked after corrections; the full audit was not run a second time, as instructed.

## Frames looked at

Scratch is S:/CurioClass-codex/_scratch/art-style-match. Every builder PNG was opened directly or in a native-size contact sheet.
- early/: gallery 1366, compact bedroom, first thick recipe.
- fix/: corrected thick recipe, Make 680, Look pins 680, Snowy Mail Route and Beat Lab.
- held/: shared tell, revealed styles, gold recipe. The first full-round selector failed in the test driver and was corrected.
- deep/: full Album, reload, clear and all-effect brush run.
- full/: Look, Match, Make and Album at 680, 800, 1000, 1280, 1366, 1920, 760 and 375 widths.
  A host-context test error was corrected; only phone and changed Make layouts were re-shot.
- input/: held full round, keyboard win, five misses, five how-to repeats, Read, real drag, grayscale, calm, compare, interrupted zoom, trades.
- final/: final phone Make/Match/stacked comparison and final willow at 1920.
- last/: artist cards at 680, 1366 and 375; skip through all 18 works.
- final-source/: focus, minimum targets, pin zoom and final Match dominance. diagnostic/: finite flip geometry inspected.
- voice-final/: five successive wins. Art contact sheets, all pin sheets and the final museum sheet were also inspected.
- Audit frames inspected: state-look-pins-1366x768, state-match-dealt-375x812, state-make-recipe-680x425 and calm-1366x768.
- followups/: four rapid modes, fixed header, Deal focus, phone header, fixed-work resizes and final export. All were inspected.

## Art made

10 generated images: 372.6 KiB. Museum images: 685.3 KiB.
Total art: 1057.9 KiB. Final bundle: 1536.4 KiB.
Bundle SHA-256: 1bfe4509d3d5e37d7d83ba08d878b04288ea93eae26971adc17c0055aaf62b6d.
Ten original people-free images made with OpenAI gpt-image. Willow redrawn twice; the ten final assets are all used.
Eighteen supplied museum images retained, with complete compositions and long sides at most 900 pixels; each is under 45 KiB.
Generated images are each under 60 KiB. The final museum encodings and foliage were inspected at display size.

## Art still to paint

None. No generated people, placeholder art, downloads of replacement paintings or recorded audio.
The willow's fine leaf edge is more granular than the other cutouts after keying; both permitted redraws were used.

## Engine changes wanted

Missing kit/art-museum.js and docs/families/art-museum.md: extract/document the local frame, zoom, pins, label and pair API.
Details, exact behavior and the tool-only boundary are in handoff.md. Shared files were not edited.

## Left open

No known functional blocker in the built tool. The near-final audit and targeted correction evidence are retained for the cold review.
This is a Build handoff, not an independent teaching review or permission to publish.
Lively-host recordings are intentionally not made in Build; browser speech is the fallback. No shared engine files could be added.
The Van Gogh year-range inconsistency and blocked source routes are documented in handoff.md; the specified fallback wording was used.
Teaching concern preserved from the spec: No Outdoor light here can reject an outdoor Japanese scene because the recipe excludes that tell.
The cold teaching review should distinguish a prescribed recipe from the literal absence of a visible feature; see handoff.md.
Phone side-by-side stacks the pictures and uses vertical page space. The long Album grid and occasional Look labels can require scrolling.
The report was deliberately written last because the user required stopping as soon as it exists.
