# Art Through Time build handoff

## Cold review changes, November 3, 2026
- Played all 21 works and all 11 events before reading this handoff or the source. Kept the walnut gallery, authentic art, thread styling and challenge content.
- Learned from labels now respect direction: an earlier source says Influenced, while the recipient says Learned from. Thread data is unchanged.
- Native timeline buttons retain their button semantics. Overview clusters and individual cards follow date order in the DOM; Left and Right include clusters, and opening a cluster places keyboard focus on a visible work.
- The eleventh placement immediately opens the illustrated record of the student's choices. Record entries replay their thread and explanation; Read no longer prefixes a stale dealt event. Fixed compact record rows and prevented the hint from shrinking over progress.
- Added fixed no-thread, candidate, record and Benin context lines to the voice inventory. Five native opens speak threadHow once; five native misses each start their event line.
- Redrew rail.png/rail.webp with the built-in image tool: an open 1840s footplate replaces the enclosed cab. Full prompt is in art/prompts.json. Final asset was rekeyed with holes and despill, then inspected at its displayed size on parchment.
- Phone opens centered on the Rhinoceros instead of leaving its only work card at the clipped right edge. No shared files changed, no commits, no downloaded art or recorded voice.
- Recomputed chronology, scale and contrast in Scratch review-numbers.json. Browser recheck passed 231 pairings, all 24 thread endpoints and base card overlap checks. Real event dragging and keyboard Enter both place photography and draw both accepted threads.
- Fresh sensitivity review passed respectful representation and Benin framing. Source-bound spec disagreements remain: Hatshepsut's current Met date starts 1473 BCE, Mihrab's design includes sacred inscriptions, and Cannons is not entirely object-free. Photography/Monet causal wording and press/woodcut distinctions also remain specification concerns. Notes now explain these limits with primary source links.
- Final cold-review audit completed once, exit 0, with 42 leads and no runtime errors. Evidence is in Scratch review-audit. Fixed the confirmed Maya/break overlap, hidden Benin thread controls and five quick-tap welcome cuts. Benin's note stays visible beside its fixed thread rack; only longer work context scrolls. Focus survives overview resize and closing a work into a cluster.
- Targeted follow-ups passed the repaired laptop, preview and phone layouts, all five quick-tap cases, native selections of Whalers/Courbet/Mucha, and actual 1366 to 760 to 1366 resize. The Spotlight resize lead compared different random works; a fixed-work check preserved Courbet, Close focus and both enabled threads. No second full audit was run.
- Expected audit leads: the deliberately scrollable time axis and eleven-entry optional browsing record; Close over an empty frame-mount corner; a card's current thread instruction replacing its stale welcome; coordinates reused across independently shuffled challenge deals. Kept the full art and record instead of reducing them to clear those leads. The opened-work keep region now targets the actual image viewport.
- This is one review pass, not a second build or a new polish round. Specification-level issues are disclosed in codex-review.md and notes.md; the tool is not being represented as free of those content concerns.

## Structure
`src.html` starts from the kit starter, with responsive museum-desk CSS, an embedded family adapter, then the timeline and challenge logic. `content.json` is actually loaded by the source and supplies all 21 works, 12 events and 24 threads. Art tokens resolve through one image map so each image is bundled once. The tool has no runtime requests.

The timeline uses the representative numeric years and a piecewise compressed scale. The base band length is 6,000 pixels; zoom ranges from whole-band overview to two times. Work and event packing is separate. Isolated works receive larger frames; close works use 80-pixel slots in up to three rows. Compact previews start at zoom two and use two work rows, three event rows, and 56-pixel work cards. Clusters represent crowded overview regions. The timeline redraws at real CSS pixels on resize.

`Curio.voice` owns speech, Read, once-only how lines, and scope checks. Every new action interrupts stale narration and completes thread drawing. Result lines are events, and the fixed lines select bank voice upbeat-guide. No recordings were made. The browser voice is the current fallback.

The challenge retains its order, placed-event set and chosen connections for the session. Photography, Cezanne and abstraction each draw both correct threads after either is placed. Japan accepts Mucha only. The lost-wax card has no year and is compare-only. The final record lists the student's own connections.

## Decisions and open questions
- There is no separate Open questions section in this spec. The specified leaned choices were retained: all eleven events, no Compare questions, Japan to Mucha only, and the left-edge undated lost-wax card.
- The user's image-tool instruction takes precedence over the spec's FLUX production suggestion. Twelve people-free event illustrations were made with the built-in OpenAI gpt-image tool. The lost-wax model is a geometric vessel rather than a human figure. Pure magenta keys were processed only with the authorized free `art.py --rekey` form. Original generated files are in `art/raw/`; exact prompts are in `art/prompts.json`.
- All authentic works were already supplied. They were preserved, resized and compressed locally. A 16:9 mountainous section of Summer Mountains is labeled as a section. Original supplied versions were backed up in Scratch. No art was downloaded.
- Recomputed contrast is in Scratch `numbers.json`: white/brand 8.58, brand/paper 7.31, ink/paper 13.45, parchment/walnut 11.62, muted/paper 5.50, thread colors/walnut 6.32 to 7.97.
- The numerical minimum for three-row, 80-pixel greedy packing was 5,564 pixels in the computation, rather than the spec's estimate of 5,750. The required 6,000-pixel base is retained, with 50-pixel end margins. The dates and all eleven accepted-event chronologies agree with the spec.
- At 1366 by 768, the band is about 456 pixels tall, roughly 67 percent of the stage rather than the spec's 60 percent. Three 72-pixel work rows, three 44-pixel event rows, spacing and the axis need more than a 409-pixel band. The larger band preserves the specified card sizes and no-overlap check. The compact preview retains its separate 56-pixel layout.
- The filter rack is available on the closed-work museum desk. Closing a work returns to those controls; thread buttons remain with the opened work. Long contextual work views and the final connection record can scroll in the phone desk while header, travel controls and band stay in view.
- Source-route failures and the current Smithsonian return statement are documented in notes.md. The Met's supplied Benin and Chola short routes returned 404. AIC denied three requested pages with 403. Supplied work metadata was retained.
- The user explicitly says to stop when codex-report.md is written. The working report therefore stays in Scratch until all build checks finish. The final report is written once at the end. This overrides the generic brief's early-report instruction.
- The bar tools were bundled into Scratch by redirecting only the bundler's output. Neither reference folder was written.

## Engine changes wanted
- `kit/art-museum.js`, missing: add `frame`, `label`, `zoomTo`, `unzoom`, `pins`, `pair`, `finish`, and `dispose` using the work API in Art Style Match's spec. Frames need resize fitting, preserved aspect ratio, interruptible zoom, 44-pixel controls, and object mounts distinct from flat frames. This tool embeds the already built Art Style Match adapter, rather than creating a competing shared implementation.
- `docs/families/art-museum.md`, missing: document the record fields, fractional detail coordinates, frame fitting, Motion behavior, and keyboard behavior. No shared files were edited.

## Cold review focus
Inspect cultural framing, the handscroll crop, the Benin note, and the simplified historical explanations. In particular, the spec's photography-to-Monet wording and its use of printing presses as the event behind a woodcut deserve a teaching review. Compare never claims influence. The detailed mechanical outcomes and any remaining limits are in codex-report.md.

This is Build only. No commit, deployment, branch change, shared engine change, or polish round was started.

## Build audit and repairs
The full audit ran once on Chrome 9981 with host 8785 and completed with 86 leads and no runtime errors. Its original report stays in Scratch. Targeted follow-ups fixed medium-height packing, cluster boundaries, axis-label collisions, phone work-view geometry, real-sized zoom glyphs, Spotlight focus, navigation welcomes and repeated-tap speech cuts. The complete audit was not rerun after these repairs.

Read now retains priority while a later action draws a thread and queues its explanation. Completed and already-solved challenge states do not queue the opening drag instruction when revisited. Repeated taps on the same work or mode do not cut a still-applicable instruction. Old threads fade at the eight-thread limit, and crowded overview tick labels wait for zoom rather than colliding.

The final semantic check again tested every one of the 231 event/work pairings and all eleven placements with zero failures. The final native checks include keyboard placement, five different work opens at two-second intervals, quick taps, a fixed-work Spotlight resize and real mouse event dragging. Final bundle: 1,413,893 bytes, with 978,536 bytes of finished art.

The built neighbor's source and handoff were read. Its refine.md did not exist in this checkout. The shared family adapter and its source spec supplied the missing engine contract.
