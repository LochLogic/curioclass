# Codex review: packaging-challenge
## Played
Cold Grade 10 solo path, then a projected-class comparison: Orders, all four Shelf cans and Case, before reading builder reports, handoff, notes or source. The brushed-metal transformation and same-scale shelf are strong; the original reveal was flatter than the build-up.
Evidence: `_scratch/packaging-challenge/` folders cold, play, find, final-sizes, post, post-voice and review-audit. No commits or shared-file edits.
Temporary host.html removed. Owned Chrome and host processes closed; ports 9940, 9941 and 8745 verified closed. Direct process termination succeeded after Windows denied taskkill for two host children.
## Findings fixed
- **Blocker, general, O6 entry:** invalid text produced NaN. Validate in the tool's parser before the kit slider accepts text, retain the prior price, and guard the model API. The first repair protected the model but the kit rewrote the field as NaN; the parser repair addresses that too.
- **Blocker, general, Orders praise:** revealing the answer and typing 3.84 earned "Great build." Replaced achievement praise with a factual comparison, suppressed after Reveal best. Sampled minima describe observations, not demonstrated skill.
- **Should fix, general, O6 voice:** decreasing price said pricier lids. Added the reverse event and interrupt stale price speech. O6 comparisons say cost; actual mass stays unweighted.
- **Should fix, general, graph teaching:** Show curve with no dots credited the student's dots. It now describes the mathematical model, including after identical releases.
- **Should fix, general, O6 record:** weighted cost was called least material. It now says Lowest sampled cost, including after repricing earlier dots.
- **Should fix, general, Shelf facts:** wording implied manufactured metal was measured. It now explicitly compares cylinder-model area at each can's own modeled volume.
- **Should fix, general, graphics:** colored fringes on cutouts. Redrew the weakest glass illustration and rekeyed nine cutouts with despill and holes; retained the coherent painted bench, shelf, cans and kraft.
- **Should fix, general, small graphs:** four-digit y ticks clipped at the smallest width. The margin now allows for their digit count. Moved Shelf's Best label clear of its marker and phone tick.
- **Should fix, general, Case meter:** the empty case's panel could read as already 78.5% filled. Labeled it Full-case fill and Product in 24, separating the planned full-case comparison from the visible packed count.
- **Polish, general, reveal payoff:** best dimensions could be buried in the scrolling readout. They now appear on the bench beside the sampled result, with a brief Motion-aware marker fade. Removed an initial scale animation after frames showed marker displacement.
## Findings left
No blocker or should-fix remains.
- **Polish:** browser speech, no recorded hero-coach performance or headphone review. Recording is outside this pass under CODEX-BUILD.md.
- **Nit:** paper texture repeats on very large flat box faces. It remains warm and readable; no flattening or restyle applied.
## Break it
- **Near-best / sampled record:** copied revealed radius through the number field and real Enter. Before: achievement praise. After: zero best events, truthful sample value, no score, badge or saved achievement. `post-copy.json`.
- **Sweep:** real 100-point slider drag records only its final release; ending at radius 12 gives one poor trial, not the best point crossed. Repeated pre/post in drive.py.
- **Five releases / curve:** identical inputs show the model curve as specified, not five different designs or a pass. Show curve is already an explicit early-reveal aid. Narration no longer invents a discovery.
- **Reveal:** immediately leaves the current design in place and marks the analytic minimum. It is a reference, not an earned gate. Copying does not earn the event.
- **Lid price:** invalid text, decrease, endpoints, all seven prices and repricing a record exercised. Weighted cost, actual area and practice mass remain distinct.
- **Shelf:** tapped all cans and switched quickly. Each uses its own volume and minimum. No quiz, reflection gate, pass or hidden answer exists.
- **Case:** packed all six orders, double-tapped, changed order/mode during packing and used Motion off. Full-case comparisons stay 78.5% for cans and 100.0% for square bases; count matches drawn rows. Repacking earns nothing.
- Independent computation plus 11 browser formula assertions passed; fill/count checks passed for all six orders. `numbers.json`, `post-math.json`.
## Voice walk
Default Sound on, 0.12-second held clicks, two-second pace: package, Radius, Show curve, Reveal best, Shelf, Drink, No. 10, Case, Pack. `voice-main-post.json`.
Spoken order: wOrders, afterBest, wShelf, afterShelf, wCase, afterPack. All three mode instructions started once. Curve became obsolete after Reveal best and dropped; mode changes cut outgoing instructions without late old-mode speech.
Followed the welcome: change width while volume stays locked, then compare the graph. A first release can skip wOrders on the faster path, as BASELINE 16 permits; hint and volume readout retain the premise.
Repeat counts: near-minimum event expected 5, spoken 5 (7-second gaps so each line finishes); curve how-to expected 1, spoken 1 (five taps at 2-second gaps); each mode welcome expected 1, spoken 1. `voice-events.json`, `voice-how.json`.
Read interrupts the current line, reads the current hint even with Sound off, and releases immediately on a mode switch. Rapid switching drops obsolete queued lines. Lid increase/decrease events each start once; reversing the price cuts the old-direction line. `voice-stale.json`, `voice-lid.json`, `read-off.json`. Muted log verification, not a listening review.
## Facts checked
- **Formulas:** cylinder volume and closed area; prism volume and face areas, including the open tray: [OpenStax Prealgebra 2e 9.6](https://openstax.org/books/prealgebra-2e/pages/9-6-solve-geometry-applications-volume-and-surface-area).
- **Minima derived from those formulas, independently recomputed:** O1 r 4.30127, h 8.60254, A 348.73421; O2 r 3.83722, h 7.67443, A 277.54502; O3 r 8.01573, h 16.03145, A 1211.11919. Closed-can h = 2r.
- **Square/weighted models, same source and computation:** cube side 10 gives 600; 20 by 10 by 5 ghost gives 700; tray side 10, h 5 gives 300. O6 at price 3: r 2.66058, h 15.96346, cost 400.28919; h/r = 2k at all seven prices. Price 1 matches O2.
- **Samples/extremes, same formulas:** O2 r 3 gives h 12.56, A 293.22; r 3.84 gives A 277.55 but h 7.66, while exact best rounds to h 7.67. Samples 2.5, 4.5, 5 reproduce. O2 r 1/12 gives h 113.00/0.78; O3 r 1 gives 1030.05. O4 side 2/30 gives h 250/1.11.
- **Units:** 1 mL = 1 cubic centimetre and 1 US fl oz = 29.57353 mL: [NIST Handbook 44, 2026 Appendix C](https://www.nist.gov/document/2026-nist-handbook-44-appendix-c), C-16 and C-24. Spec capacities convert to 354.9, 499.2, 881.0 and 3236.2 mL.
- **Shelf inputs:** food-can inch sizes/capacities match the spec's [Tin can table](https://en.wikipedia.org/wiki/Tin_can#Standard_sizes); nominal-size convention cross-checked against USDA AMS Technical Procedures Manual, February 2013, pages 88-89. Cm inputs are rounded specimen values.
- **Drink:** spec's [Beverage can source](https://en.wikipedia.org/wiki/Beverage_can#United_States) lists 6.60 by 12.3 cm. [Crown's 355 mL specification](https://www.crowncork.com/beverage-packaging/products/beverage-cans/12oz-355ml-standard) confirms 66 mm diameter but gives 122.22 mm height. Retained the spec's approximate specimen, not a universal manufacturing size.
- **Shelf calculations from stated cm inputs:** volumes 420.8, 572.5, 996.2, 3450.9; areas 323.5, 385.8, 553.4, 1266.3; minima 310.9, 381.7, 552.2, 1264.2; excess 4.1%, 1.1%, 0.2%, 0.2%; h/diameter 1.86, 1.37, 1.15, 1.13. OpenStax formulas, full precision. Spec example totals differ slightly through rounding.
- **Packing:** case volume 96 r squared h versus product 24 pi r squared h gives pi/4 = 78.5%; square bases give 100%. Derived from OpenStax volumes. Assumes square grid, bounding volumes, no dividers or case-wall thickness.
- **Mass:** 0.03 g per square cm is the spec's labeled practice factor; O2 best gives 8.33 g; case mass is 24 times unweighted area times 0.03. It is not measured real metal density or cardboard mass.
- **Standards:** [Common Core G-MG.A](https://www.thecorestandards.org/Math/Content/HSG/MG/): Shelf models objects, Orders designs under a volume constraint, Case compares volume density and area-based mass. Notes have the required opening sections and practical home activities.
## Sensitivity
None: unbranded geometric packaging and food/plant objects, no cultural, historical, religious or bodily subject. No people in the art. This object-scale workbench and pantry do not need a person to explain the task.
## Flattest moment left
Repacking the same order repeats its grid. The useful contrast comes from changing circular to square bases. Added no new challenge or score beyond the spec. Reveal is stronger because its exact result stays on the bench.
## Graphics
All 13 assets checked in scenes/contact sheets and final-size cutouts. One glass redraw; nine cutouts rekeyed. Metal package, painted bench, shelf scale, kraft nets and case retain their detail. All art tokens have entries/files; no people or placeholders.
All standard sizes, phone iframe, grayscale, Motion off, keyboard completion and can extremes inspected. The final keyboard run reaches O2 r 3.84 with 17 trials, then reveals best; focus stays on Reveal best. A whole-pixel jittered handle drag records one trial and retains handle focus. Motion off packs 24 instantly and has zero running animations after settling.
BUILD wave checks: synchronous action hints and Read; stable focus/controls; 44 px targets and visible choices; no hidden-answer gate; explicit model assumptions; all three standards practiced; calm motion; resize during action; no late welcome; unknown data stays absent until shown; distinct dot/diamond/ring meanings; truthful labels; hints restore on mode/order changes; no word-matching answer shortcut. Evidence is in the focused logs, source inspection and final audit.
Final art: 222,798 bytes (217.6 KiB); bundle: 426,876 bytes (416.9 KiB), below 2 MB.
## Audit
Completed once within the 40-minute limit, Chrome 9941, host 8745: `review-audit/audit.md`. All 91 audit PNGs inspected, plus focused pre/post frames.
- One fixture lead corrected: the duplicate sidebar `#material` is intentionally below the compact fold. The keep target is now the persistent bench `#liveMaterial`; fixture focus uses preventScroll and the phone size key is corrected. Scoped 680x425 re-shot confirms the live readout in view and invalid price restored.
- Three first-tap welcome leads accepted under BASELINE 16 and the explicit spec: handle release makes wOrders stale; Show curve and Reveal best speak their own instruction. Locked volume stays visible and the main walk hears all three mode how-to lines. No late welcome added.
- All eight first-screen sizes clean; other listed states clean. Motion off has no infinite animations. No runtime errors, stuck disabled controls, lost focus, repeated how-to nagging or quick-tap speech defect. Final resize stress clean.
- No second audit. Only the corrected fixture and the changed graph's remaining extreme-value margins received scoped closure frames.
## Left open
- Unattended choice: retain four real unbranded cans rather than introduce invented box dimensions.
- Retain approximate specimen dimensions and document differences from precise manufacturer sizes; changing inputs needs a spec decision.
- Browser voice fallback remains. No recording, classroom trial or subjective listening validation performed.
- Initial location/document reads returned immediately before the bounded helper was installed. Subsequent commands have explicit limits; no command remains running without a deadline.

- Two manual phone batches logged a parent test-host favicon 404; the offline tool has an inline icon and no remote resources. The audit host is clean.
