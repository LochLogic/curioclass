# Art Style Match build handoff

## Cold review changes

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

## Cold review audit closure

The review audit ran once within the 40-minute limit on Chrome 9961 and host 8765. It returned 51 leads and no runtime errors.
Thirteen pin overlays are intentional. Eighteen resize flags compare different shuffled work identities; fixed-bedroom Look/zoom,
Match and artist checks preserved identity and enabled controls across 1366 to 760 to 1366. Eighteen skipped gallery welcomes are
stale by the spec once a work opens; lookOpen names the next action. One Album lead is the specified long 18-slot scrolling grid.
The remaining lead, Save losing focus, was fixed with aria-disabled and the busy guard. A held native Save click retained focus
both while saving and after completion, and wrote a 1600 by 1000 PNG in Scratch. Only affected flows were rechecked afterward.
Evidence: `review-audit/audit.md`, `review-audit-confirmation.json`, `review-audit-confirmed/` and `review-downloads/` in Scratch.

## Spec corrections still wanted

These are left unchanged under CODEX-REVIEW.md's rule against changing the spec during a cold review.
- Literal "No outdoor light here" can deny an observable feature of an outdoor Japanese print. Keep the selected recipe
  sets, but revise rejection wording to describe the card's chosen tells, not the absence of a visible property.
- The specified Van Gogh style name supplies the answer to the following artist question. It needs a spec decision.
- The specified "late 1880s" Album range includes Irises dated 1890.
- VA:Cn11 currently rests on reading contextual card lines and connecting works with artists. A stronger active
  connection with cultural purpose would require a changed activity, outside this pass's scope.

## Structure

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

## Decisions and source checks

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

## Engine changes wanted

- Missing `kit/art-museum.js`: add `frame`, `zoomTo`, `unzoom`, `pins`, `label` and `pair` using the API in spec.md.
  A fitted frame must recalculate on resize, preserve aspect ratio, use 44-pixel pins and finish a running zoom on
  the next input. Extract the local adapter only after comparing its needs with the other family tools.
- Missing `docs/families/art-museum.md`: document the work record, fractional image coordinates, fitted viewports,
  keyboard behavior and Motion behavior. This build cannot edit either shared path.

## Narration

`Curio.voice` owns the queue, stale scope checks, Read and heard-line tracking. The tool updates its hint immediately.
How-to lines speak once per page load; misses and wins are event lines. `voice/lines.json` selects lively-host. No
recordings were made, as requested by the build brief; the browser voice is the current audible fallback.

## Review focus

The cold review should inspect cultural framing, each tell pin on the authentic work, transfer from Match to Make,
and visual fidelity of combinations. Recipes are deliberately simple. Screen effects are not faithful material
simulations of gold leaf, woodblock printing or an artist's full practice. Check the report for measured limits and
any remaining mechanical leads. Nothing outside this tool should be changed to finish a local issue.

One teaching concern comes from the specified content rule: Match rejects every tell outside the card's supplied
set with “No ... here.” Red Fuji visibly depicts an outdoor scene, yet Outdoor light is excluded from its recipe.
The build preserves the specified tell sets and fixed feedback. The teaching review should decide whether that
wording should describe the card's recipe rather than claiming the visible feature is absent.

## Builder final check notes

The single full audit completed with 80 repeated mechanical leads. The report groups and answers every lead class.
Focused follow-ups fixed small targets, focus after opening/dealing, header movement and same-tab speech cuts.
Fixed-work resizes preserved Look, Match and artist state. Make observes its displayed canvas size and re-renders
a stale backing buffer after layout settles; the final buffer and display both measured 690 by 424 pixels.
The post-fix PNG export remained 1600 by 1000. All started Chrome instances and host servers were closed.
