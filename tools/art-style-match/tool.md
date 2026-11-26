# Art Style Match: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: art-style-match

#### Built

Look, Match, Make and Album, with 18 authentic museum works, 10 tells, 6 recipes and 4 layered scenes.
Built from the kit starter with Curio.voice. Sources and labels live in content.json. No shared source was changed.
The missing art-museum family engine is handled by a tool-local adapter; see Engine changes wanted.
The offline bundle, teacher notes, lesson plan, voice manifest, art manifest and audit states are included.
Build only. No commit, branch change, upload, deployment or polish round.

#### Numbers check

PASS: all 18 tell sets are subsets of their recipe and identify their own style uniquely.
PASS: gold, tiny, smooth, shadow, dabs, dots and thick each fit one style. Flat, outline and outdoor each fit two.
PASS: no pair of recipes shares two tells. Exactly 6 of the 1,024 toggle mixes name a style.
Contrast ratios: white/brand 7.54; brand/card 7.00; ink/card 14.91; card/felt 10.63; muted/card 6.00; ink/gold 7.37.
Evidence: Scratch/numbers-check.json. These match the spec's rounded values.
Spec inconsistency preserved: the Van Gogh row says late 1880s but includes Irises, 1890. Not silently broadened.

#### Feel check

Best moment: the Bold outlines card fits two recipes, then Thick wavy paint flips up the style choices. The clues visibly stick.
The second payoff is repainting the same scene with dots, then dabs, then raised curving strokes, and comparing it with a collected work.
Flattest moment 1: the first thick-paint treatment looked like wirework. Softened raised edges and cleaned noisy region boundaries.
Flattest moment 2: the artist step crowded the small panel. Its three cards now occupy the hand's space and remain fully visible.
The rendered table has real felt, paper shading, gold card backs, gilt frames and large authentic works. Make uses every generated asset.
Opened both bar tools. Sources were read before building; their Scratch bundles were opened after the first playable version.
The tool and Snowy Mail Route are placed beside each other in the comparison below. Beat Lab was also opened and inspected.
![Art Style Match beside the bar tool](../../../_scratch/art-style-match/bar-comparison.jpg)

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

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

#### Art made

10 generated images: 372.6 KiB. Museum images: 685.3 KiB.
Total art: 1057.9 KiB. Final bundle: 1536.4 KiB.
Bundle SHA-256: 1bfe4509d3d5e37d7d83ba08d878b04288ea93eae26971adc17c0055aaf62b6d.
Ten original people-free images made with OpenAI gpt-image. Willow redrawn twice; the ten final assets are all used.
Eighteen supplied museum images retained, with complete compositions and long sides at most 900 pixels; each is under 45 KiB.
Generated images are each under 60 KiB. The final museum encodings and foliage were inspected at display size.

#### Art still to paint

None. No generated people, placeholder art, downloads of replacement paintings or recorded audio.
The willow's fine leaf edge is more granular than the other cutouts after keying; both permitted redraws were used.

#### Engine changes wanted

Missing kit/art-museum.js and docs/families/art-museum.md: extract/document the local frame, zoom, pins, label and pair API.
Details, exact behavior and the tool-only boundary are in handoff.md. Shared files were not edited.

#### Left open

No known functional blocker in the built tool. The near-final audit and targeted correction evidence are retained for the cold review.
This is a Build handoff, not an independent teaching review or permission to publish.
Lively-host recordings are intentionally not made in Build; browser speech is the fallback. No shared engine files could be added.
The Van Gogh year-range inconsistency and blocked source routes are documented in handoff.md; the specified fallback wording was used.
Teaching concern preserved from the spec: No Outdoor light here can reject an outdoor Japanese scene because the recipe excludes that tell.
The cold teaching review should distinguish a prescribed recipe from the literal absence of a visible feature; see handoff.md.
Phone side-by-side stacks the pictures and uses vertical page space. The long Album grid and occasional Look labels can require scrolling.
The report was deliberately written last because the user required stopping as soon as it exists.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: art-style-match

#### Played
Cold Grade 3 solo play before reading builder notes/source: Look, tells/zoom, wrong/right Match, trade, artist/win, four Make scenes, Album.
Projector lens: the large authentic paintings and felt/gilt card table are strengths; surface transformations invite experimenting.

#### Findings fixed
- Blocker, general, Make/export: changing a scene/tell could replace the picture being saved. A separate worker exports the frozen tapped scene/recipe.
- Should fix, family:art-museum, Make: smooth mixed in mean colors instead of blurring. Full-resolution smoothing stays within regions and the subject mask.
- Should fix, general, Make art: fragmented boundaries formed jagged black bands. Continuous 3px contours retain the scene and raised paint detail.
- Should fix, general, phone comparison: return controls were below two pictures. The existing action row stays visible, with space for the captions.
- Should fix, general, Match: Escape after winning prompted unavailable artist cards. Idle/won now name their actual next action.
- Should fix, general, Album: the sixth row clipped at common laptop size. Six compact rows now fit; short previews retain scrolling.
- Should fix, general, art/pond-willow: granular keyed silhouette. Two redraws give denser fronds and a cleaner silhouette while retaining left light.
- Should fix, general, art manifest: authentic paintings containing people lacked people flags. Flags added; no people generated.
- Should fix, general, Save: native disabling dropped focus during export. An aria-disabled busy state and guarded handler retain focus.
- Polish, general, Match: the win was mostly text. A paper collection record shows the actual title, attribution and tells spotted, with a finite count stamp.

#### Findings left
- Blocker, family:art-museum, prescribed rejection: "No outdoor light here" denies an observable feature in Japanese outdoor scenes. The spec requires this wording and restricted tell sets.
- Should fix, general, prescribed artist step: the Van Gogh style name supplies the following artist answer. Changing that name/step requires a spec decision.
- Should fix, general, prescribed Album years: "late 1880s" includes Irises (1890). Preserved under the no-spec-change rule.
- Should fix, general, VA:Cn11 depth: cultural context is mostly read, not actively related to a work's purpose. A stronger task changes the specified activity.
- Polish, general: the finest keyed foliage remains slightly granular at the largest projection size; both review redraws were used.

#### Flattest moment left
Later Match rounds repeat the tell/style/artist sequence. The personal collection record improves the payoff; different progression exceeds this spec.

#### Graphics
All 18 authentic museum paintings and 10 generated assets inspected, including every Look pin frame and all four scenes.
Only willow redrawn, twice with OpenAI gpt-image. Final asset: art/pond-willow.webp; prompt/provenance: art/prompts.json.
Felt, gilt frames, rich palettes, painterly surfaces and the other nine generated assets kept. Motion off stops the new stamp and receipt motion.
Bundle: 1,582,175 bytes, below 2 MB. SHA-256 and closed-port checks: Scratch/review-validation.json.
Text contrast ratios recomputed: white/brand 7.54; brand/card 7.00; ink/card 14.91; card/felt 10.63; muted/card 6.00; ink/gold 7.36.

#### Audit
Completed once within the 40-minute limit, Chrome 9961 and host 8765. Report: Scratch/review-audit/audit.md. Zero runtime errors; 51 leads:
- 13 picture/pin overlaps: intentional pins on the full-picture activation target, not overlapping pin targets.
- 18 resize flags: different shuffled work identities across fresh loads. Fixed-bedroom Look/zoom, Match and artist checks preserved identity and enabled controls.
- 18 skipped gallery welcomes: correctly stale when a work opens; lookOpen immediately names the next action. Mode welcomes and quick/repeated taps passed.
- 1 Album scroll flag: one collected card lies late in the specified long 18-slot grid. Clear confirmation controls remain visible at 680 and 375.
- 1 confirmed Save focus loss: fixed, then re-shot. A held native Save click retained focus while busy and afterward, and downloaded a 1600x1000 PNG.
Only affected flows were checked after the audit; it was not rerun. Evidence: Scratch/review-audit-confirmation.json and review-audit-confirmed/.

| Line | Kind | Expected starts | Observed starts |
|---|---|---:|---:|
| selectHow | how | 1 | 1 |
| playHow | how | 1 | 1 |
| miss | event | 5 | 5 |
| won | event | 5 | 5 |

Held 2-second pace; Read with Sound off and stale mode/reset checks passed. All 61 declared lines match voice/lines.json.

#### Left open
The spec conflicts above remain under CODEX-REVIEW.md's explicit rule against changing the spec or adding an activity during this pass.
Missing shared art-museum engine/document remains in handoff.md; the existing tool-local adapter is retained. Browser narration remains the fallback.
Recipe checks: all 18 tell sets identify their own style; shared clues fit two; exactly 6 of 1,024 toggle mixes name styles.
All 18 paintings won and restored after reload; 1,080 trades preserved useful, duplicate-free hands; Clear/Keep confirmation passed.
Native jittered drag, a full keyboard win, grayscale and Motion off passed. Affected large-screen renders stayed below 300ms.
The frozen 1600x1000 export matched the tapped picture after rapid scene/dot changes, leaving the live buffer at display resolution.
Scratch evidence: review-numbers.json, review-game.json, review-trades.json, review-render.json, review-export.json and review-voice-*.json.
Frames inspected: cold-frames/, review-pins/, review-sizes/ (32 frames, eight sizes), review-fixed/, review-final-render/ and review-narrow-final/.
The temporary iframe host requested a missing favicon; offline tool resource checks showed no HTTP requests or tool runtime errors.
No commits. Repository writes stayed within tools/art-style-match/ and _scratch/art-style-match/. All started browsers/servers are closed; host.html removed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Art Style Match build handoff

#### Cold review changes

- The win now replaces the inactive hand with a paper collection record: title, attribution and the student's played tells.
  The album count receives a finite stamp; both are still with Motion off. Existing gilt frames, felt and art remain.
- Escape in Match now gives the right next action for idle and won states instead of naming unavailable artist cards.
- The six Album rows fit the common laptop layout; shorter previews and narrow screens retain the specified scrolling grid.
- PNG export freezes its scene and effects in a separate StyleBrush worker, independent of rapid scene/tell changes.
  It downloads the frozen 1600 by 1000 bitmap and does not replace the live canvas buffer.
  Save uses aria-disabled and a guarded handler while busy, keeping keyboard focus on the same button throughout export.
- In the stacked phone comparison, the existing Save picture, Side by side and Reset row stays on screen so the
  student can return without searching below the two paintings.
- Smooth blending now averages only neighboring pixels in the same region and subject mask, rather than mixing in a mean color.
  Region outlines use continuous curves and omit tiny isolated contour specks, keeping 3-pixel lines readable on small canvases.
- Willow was redrawn twice during cold review with OpenAI gpt-image. The selected dense-frond version is rekeyed at 380 pixels,
  quality 40, about 58 KiB; other nine generated images and all eighteen authentic paintings are retained.
- Authentic museum assets containing people are marked as such in prompts.json; no people were generated.
- Evidence is in `_scratch/art-style-match/review-*`; the cold report is `codex-review.md` when the pass is finished.

#### Cold review audit closure

The review audit ran once within the 40-minute limit on Chrome 9961 and host 8765. It returned 51 leads and no runtime errors.
Thirteen pin overlays are intentional. Eighteen resize flags compare different shuffled work identities; fixed-bedroom Look/zoom,
Match and artist checks preserved identity and enabled controls across 1366 to 760 to 1366. Eighteen skipped gallery welcomes are
stale by the spec once a work opens; lookOpen names the next action. One Album lead is the specified long 18-slot scrolling grid.
The remaining lead, Save losing focus, was fixed with aria-disabled and the busy guard. A held native Save click retained focus
both while saving and after completion, and wrote a 1600 by 1000 PNG in Scratch. Only affected flows were rechecked afterward.
Evidence: `review-audit/audit.md`, `review-audit-confirmation.json`, `review-audit-confirmed/` and `review-downloads/` in Scratch.

#### Spec corrections still wanted

These are left unchanged under CODEX-REVIEW.md's rule against changing the spec during a cold review.
- Literal "No outdoor light here" can deny an observable feature of an outdoor Japanese print. Keep the selected recipe
  sets, but revise rejection wording to describe the card's chosen tells, not the absence of a visible property.
- The specified Van Gogh style name supplies the answer to the following artist question. It needs a spec decision.
- The specified "late 1880s" Album range includes Irises dated 1890.
- VA:Cn11 currently rests on reading contextual card lines and connecting works with artists. A stronger active
  connection with cultural purpose would require a changed activity, outside this pass's scope.

#### Structure

`src.html` starts from the kit starter and holds the responsive table, controls and game state. `content.json` holds
all eighteen work records, tell pins, six recipes and ten tells. `lib/museum.min.js` is a readable local adapter for
the missing family engine. `lib/brush.min.js` is a readable worker renderer, despite the bundler's required suffix.
Both scripts are inlined by the standard bundler. No shared files were changed.

The renderer composes a background and a separate subject. It prepares an eight-color k-means map at 320 pixels,
cleans isolated region specks, and renders the effect stack at the canvas's displayed size. Random brushwork uses a
fixed scene seed. A newer render terminates the busy worker; stale results never overwrite a newer picture.
Prepared region maps survive worker replacement. Frame ResizeObservers refit comparisons after their boxes settle.

Artist choices occupy the hand's place during the artist step, keeping all three cards visible in compact layouts.
They follow the painting and style choices in DOM order. A shuffled circular deal cursor lets New painting visit
all eighteen unmatched works. The tell hand and draw pile partition the ten-card deck without duplicate cards;
the useful-tell guarantee swaps a useful card in when a trade would otherwise strand the player.

`window.__tool` exposes state, content, actions, recipe matching, render timing and the kit voice log for checking.
Storage is limited to `art-style-match-album` and the kit's shared Motion preference. Storage access is guarded.

#### Decisions and source checks

- The spec contains no separate Open questions section. Its source-check alternatives lean toward short verified
  fallbacks: use “Ter Borch painted fine clothes in careful detail” and “Pissarro painted many views of busy Paris
  streets.” The Met Margaretha page supports detailed attire but does not explicitly support the proposed satin
  wording; the Art Institute page returned 403. The spec is unchanged.
- The Met Feast of Sada page explicitly identifies Sultan Muhammad as the attributed painter and Firdausi as author.
  The supplied public-domain metadata's author field is not used as the artist answer.
- The specified Van Gogh recipe year label says “late 1880s”, while Irises is dated 1890. Both are retained exactly
  from the spec. A later spec decision can extend that year label; this build does not change the historical scope.
- The two Met essays opened successfully. The supplied Van Gogh Museum story routes could not be fetched; the
  Rijksmuseum corroborates the self-portrait/model-cost statement. These routes and outcomes are documented in notes.
- Authentic museum images were already supplied. None was generated, replaced with a lookalike or downloaded.
- The user's image-tool instruction takes precedence over the spec's local-FLUX production suggestion. Ten original
  people-free assets were made with OpenAI gpt-image. The willow was redrawn after its edge looked rough.
- All ten generated assets are used: felt, gold and all four separate scene/background pairs.
- The user permits writing only this tool. The two reference tools were bundled directly into Scratch using the
  original bundler with only its output destination redirected. Their source and folders were not changed.
- The user says to stop when codex-report.md is written. It is therefore written once, at the end, rather than
  created early as the generic brief suggests. This is Build only; no polish round or git commit was started.
- Python initially created two incidental bytecode cache files under scripts. Those exact files were removed;
  subsequent commands use `-B` and `PYTHONDONTWRITEBYTECODE=1`. Final status should contain this tool only.

#### Engine changes wanted

- Missing `kit/art-museum.js`: add `frame`, `zoomTo`, `unzoom`, `pins`, `label` and `pair` using the API in spec.md.
  A fitted frame must recalculate on resize, preserve aspect ratio, use 44-pixel pins and finish a running zoom on
  the next input. Extract the local adapter only after comparing its needs with the other family tools.
- Missing `docs/families/art-museum.md`: document the work record, fractional image coordinates, fitted viewports,
  keyboard behavior and Motion behavior. This build cannot edit either shared path.

#### Narration

`Curio.voice` owns the queue, stale scope checks, Read and heard-line tracking. The tool updates its hint immediately.
How-to lines speak once per page load; misses and wins are event lines. `voice/lines.json` selects lively-host. No
recordings were made, as requested by the build brief; the browser voice is the current audible fallback.

#### Review focus

The cold review should inspect cultural framing, each tell pin on the authentic work, transfer from Match to Make,
and visual fidelity of combinations. Recipes are deliberately simple. Screen effects are not faithful material
simulations of gold leaf, woodblock printing or an artist's full practice. Check the report for measured limits and
any remaining mechanical leads. Nothing outside this tool should be changed to finish a local issue.

One teaching concern comes from the specified content rule: Match rejects every tell outside the card's supplied
set with “No ... here.” Red Fuji visibly depicts an outdoor scene, yet Outdoor light is excluded from its recipe.
The build preserves the specified tell sets and fixed feedback. The teaching review should decide whether that
wording should describe the card's recipe rather than claiming the visible feature is absent.

#### Builder final check notes

The single full audit completed with 80 repeated mechanical leads. The report groups and answers every lead class.
Focused follow-ups fixed small targets, focus after opening/dealing, header movement and same-tab speech cuts.
Fixed-work resizes preserved Look, Match and artist state. Make observes its displayed canvas size and re-renders
a stale backing buffer after layout settles; the final buffer and display both measured 690 by 424 pixels.
The post-fix PNG export remained 1600 by 1000. All started Chrome instances and host servers were closed.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
