# Art Through Time: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: art-through-time

#### Built
- Offline Timeline and What Changed?, 21 authentic museum works, 12 generated event illustrations and 24 threads.
- Real-pixel compressed timeline, three-row packing, draggable scrolling, mini-map, era travel, zoom, clusters, filters and Spotlight.
- Work frames, zoom, wall labels, contextual lines, the Benin note, session checks and an earned eleven-connection record.
- Tap, keyboard and real drag placement; immediate response, interruptible thread drawing and event settling; Motion, Sound and Read through the kit.
- Build only. No commit, deployment, branch operation, shared-file edit or polish round.

#### Numbers check
- Scratch `numbers.json`: all 11 accepted-event chronologies pass. Japan 1858 does not change Mishima 1833; it accepts Mucha 1897.
- 24 threads, including two lost-wax comparisons. Shared causes each draw both accepted works.
- Differences: 1,512, 567, 172 and 1,230 years, agreeing with the spec's approximate labels.
- Three-row 80-pixel packing minimum was 5,564 pixels, not the spec's estimated 5,750. Required base length remains 6,000 pixels. The post-1000 scale is about 4.54 pixels/year before end margins.
- Contrasts: white/brand 8.58, brand/paper 7.31, ink/paper 13.45, paper/walnut 11.62, muted/paper 5.50; thread colors/walnut 6.32 to 7.97. All meet their specified thresholds.
- Layout exception: the 456-pixel band at 1366 by 768 is about 67 percent of its stage, exceeding the spec's 60 percent so three rows retain their required minimum sizes without overlap. Details are in handoff.md.

#### Feel check
- Best moment: pull the press thread from the authentic Rhinoceros and watch the painted printing press connect to the framed woodcut. The final record then makes the whole session specific to the student's choices.
- Flattest moment 1: isolated works were small inside a large band. Enlarged isolated frames to 124 by 140 pixels while retaining compact frames and three rows in crowded years.
- Flattest moment 2: a correct event initially changed only an outline. It now appears and settles onto the band, draws every accepted connection, and adds the chosen connection to the final record.
- Played the whole explore-to-challenge flow with held mouse input: an intentional earlier-work mistake, all 11 events, and the earned record. Zero runtime errors. Also checked real band dragging, event dragging and keyboard placement.
- Compared `student/pulled-thread.png` beside `bars/bar-beat.png` in Scratch `bar-comparison.jpg`, after opening both required bar tools. The walnut, authentic frames and painted objects have comparable visual finish; this is a contemplative history explorer, not a timed music activity.
- Overview clusters deliberately exchange art detail for navigation; opening a cluster or a work restores the image. That is the least visual state, as specified.

#### Done when
1. PASS: 21 works sorted by numeric year, piecewise 30/70 scale, break mark. Automated rectangle checks found no work or event overlaps anywhere at zoom one, 1366 by 768; smallest work card 73.33 pixels tall.
2. PASS: all 24 threads exercised, with correct endpoints; book/solid, gear/dashed, ship/dotted, and eyes/double styles. Compare and grayscale frames inspected.
3. PASS: all 231 event/work pairs tested against the supplied answer set and earlier-work feedback. All eleven events completed again with native held mouse clicks. Photography accepts either work and draws both.
4. PASS: Compare is excluded from the dealt-event answers; undated lost-wax is never dealt.
5. PASS: Benin note inspected on laptop and preview and included in Read's work context.
6. PASS: real drag and wheel travel, mini-map and keyboard travel, era jumps and zoom; clusters keep 48-pixel targets and cards are at least 44 pixels. Three Show me candidates were measured fully in view in the preview.
7. PASS: five different opens at a 2-second tap pace spoke threadHow once without a cut, then logged four heard/silent entries. Five misses produced five spoken event entries. New actions hush stale speech and leave an empty stale queue.
8. PASS: final bundle about 1.41 MB, below the 2 MB limit.
9. PASS: inspected every STANDARDS size in both modes, including 375 through host port 8785. The band is the largest Timeline region; the dealt picture and band remain visible in the preview. Fixed the phone header and 1000-pixel filter clipping after the full run, then re-shot only affected sizes.
10. PASS: held clicks during thread drawing and travel acted immediately; a real dragged event accepted its target. The next work opened and no stale line remained queued. Motion off had zero running infinite animations.

#### Wave lessons
- PASS, hint and voice: immediate state hints name the next control. Read uses the current context. How lines use Curio.voice's heard set; results are events with state validity checks. Held-click evidence is in `voice-opens.json` and `voice-misses.json`.
- PASS, focus and layout: no focus on load; card focus restored on timeline redraw, explicit focus uses preventScroll, and Next event restores a stable mode control. Keyboard frame retained card-benin focus after opening.
- PASS, sizes: every required size viewed; 44-pixel controls, 56-pixel preview work cards, phone host test. Fixed only affected follow-up sizes.
- PASS, no giveaways: event text is historical context; candidate frames appear only after two misses and Show me. Compare never supplies a challenge answer. No points, timer or hidden answer label.
- PASS, honest numbers: approximate dates retain their ranges on wall labels; the representative timeline years and compressed scale are explained in notes. Count is placed events out of 11.
- PASS, standards: a solo student inspects authentic art and makes historical connections; both named NCAS standards are practiced.
- PASS, Motion off: zero running infinite animations; direct state and full feedback remain available.
- PASS, short choices: filter choices and challenge controls fit the desk; the timeline is intentionally a long scrolling list. Show me brings its three candidates into view.
- PASS, resize mid-animation: resize rebuilds positions from current state; no object references are retained by a timeline mover. No input locks or runtime exceptions in the checked flows.
- PASS, welcome pacing: no welcomeAfter option; welcomes belong to their modes. Card and event actions invalidate their old moment.
- PASS, unknown stays unknown: no correct-work highlight before a hint or result. An unplaced event is absent from the band until accepted.
- PASS, one look/one meaning: each thread kind keeps its icon and stroke in the band, buttons and legend; Compare is explicitly not influence.
- PASS, badges say what is true: opened checks, placed checks, and the 11-event strip are driven from their session sets.
- PASS, hint returns with state: switching modes or dealing a new event immediately restores the correct action hint.
- PASS, no word-copy answer: the event names the historical change, while the works retain their authentic titles and visual evidence.

#### Audit leads
- Full audit completed once, exit 0, with 86 mechanical leads and no runtime errors. Original evidence remains in Scratch `audit/audit.md`. Only affected cases were rechecked afterward; the complete audit was not rerun.
- Fixed all dense-card overlap leads at 1000 by 625 and 1280 by 720: three 56-pixel rows now fit medium-height bands; the laptop retains cards at least 72 pixels tall. Rectangle checks found zero overlaps in both repaired layouts and the preview.
- Fixed every cluster/card collision class by grouping consecutive close neighbors, rather than measuring from a bucket's first item. Checked 680, 760, 1000 and 1920 overview layouts: zero card/cluster overlaps.
- Fixed event/tick and break/tick collisions by separating the axis label rail from event rows and moving the break above the rail. Colliding overview tick labels wait for zoom. Kept the oldest frame inside the whole-band end margin; inspected the 1920 overview.
- Fixed the zero-font zoom leads: actual 16-pixel plus/minus glyphs replace hidden-size text with pseudo-elements. Full labels remain visible where space allows, with accessible names at every size.
- Fixed the phone work-view overlap class with explicit grid areas for frame, label, Close and context. Inspected the repaired 375-pixel work view. The compact keep-region flags sample the Close control over an empty corner of the mount; the actual artwork viewport is clear, so that intentional corner placement remains.
- Fixed Spotlight's real focus loss by focusing Close with preventScroll after opening. The resize lead compared different randomly chosen works across independent runs. A fixed-random native click followed by 1366 to 760 to 1366 resize preserved the same work, its thread controls and Close focus, with zero exceptions.
- Fixed lost welcomes after All, filters, era, zoom and mini-map navigation: those actions leave the opening instruction valid. Card/Event/Spotlight first taps deliberately replace it with the current thread instruction, as the spec requires. A held All click now starts welcomeTimeline.
- Fixed both same-mode quick-tap speech cuts by leaving the active mode intact. Fixed same-work quick-tap cuts and preserved a still-applicable threadHow across different work opens. Two quick taps per mode and work, plus five different opens two seconds apart, logged one spoken instruction without a cut.
- Fixed two additional state cases: Read continues while a later thread explanation waits in the queue; completed or solved challenge re-entry speaks the correct current action instead of the opening drag instruction. Keyboard Enter also placed an event correctly.
- Retained every sideways-scroll lead: this is the specified long timeline, not a short hidden choice set. Mini-map, eras, zoom, drag and arrow keys provide travel. Optional Show me candidates were separately measured fully in view.
- The three What Changed? “nothing changed” leads use coordinates captured from one shuffled deal on a fresh independently shuffled deal. Actual work selection and Place were checked in the native eleven-event session and the final 231-pair check. No dead work handler was found.
- Audit five-click checks were clean; Motion off was clean. The original host favicon 404 was a harness request; a data favicon was added to the tool and the Scratch host, and follow-up console checks were clean.
- Added and checked the specified oldest-thread fade while retaining eight active thread groups. After 500 milliseconds the retiring group's opacity was zero. No input waits for it.

#### Frames looked at
- Both bar frames; all three first frames, all three second frames and all seven focused frames.
- Every full-run PNG: Timeline and What Changed? at 680, 800, 1000, 1280, 1366, 1920, 760 and 375 widths.
- Full-run semantic record, calm, gray, overview, keyboard, five opens, five misses, real band drag, real event drag and tap-during-thread frames. Five specific audit lead frames were inspected; the report does not claim a visual review of every auto-generated audit image.
- Follow-ups: fixed-1000, fixed-phone, fixed-phone-changed, show-me-preview, preview-beninnote and zoom-detail.
- Student run: pulled-thread, six-connections, earned-record. Final event contact sheet and museum contact sheet. Comparison image inspected.

- Every targeted audit-follow-up PNG: three repaired dense layouts, four repaired overviews, phone grid, fade, navigation welcome, Read priority, completed return, solved return, keyboard placement and final preview Benin note.
- Every final PNG: semantic record, two mode quick-taps, same-work quick-taps, five distinct opens, finished fade, overview labels, Spotlight resize and the no-thread work view.

#### Art made
- 12 original event images, no generated people, plus 21 supplied authentic works. All 33 finished assets are used.
- Total finished art 978,536 bytes, about 956 KiB; final bundle 1,413,893 bytes.
- Preserved original museum assets in Scratch, compressed each supplied work below 40,000 bytes, and made the labeled 16:9 handscroll section. Fine-detail Rhinoceros and Mihrab needed lower WebP quality to meet that limit; their final displayed images were inspected.
- No image redraws were needed. Rekeyed ship, candle and lost-wax with hole removal and despill to remove magenta remnants. Final contact sheet inspected after those changes.
- Built-in OpenAI gpt-image; exact prompts and drawn_by metadata are in art/prompts.json. Generated originals copied into art/raw/.

#### Art still to paint
- None. Authentic museum images containing people were supplied, not generated. Narration recordings were intentionally not made in this build.

#### Engine changes wanted
- Missing `kit/art-museum.js` and `docs/families/art-museum.md`. Exact requested functions and behavior are listed in handoff.md. Embedded the existing Art Style Match local adapter; no shared path was written.

#### Left open
- Cold review, including cultural framing and the spec's simplified historical causal wording, remains the next stage.
- Museum source-route limits: Met Benin/Chola essays and the NGA slideshow could not be fetched; three AIC work pages returned 403. Supplied metadata and art were retained. Current available essay routes and the Smithsonian return reference are in notes.md.
- No voice recordings: upbeat-guide metadata is ready; kit browser speech is the audible fallback.
- The full audit predates the final repairs. Targeted repaired layouts, narration and semantic checks passed; a fresh cold review is still required.
- Long work views and the final record may scroll in the narrow phone desk. Header, era travel, zoom and the band remain visible.
- The band is larger than the spec's stated 60 percent at the common laptop size, as explained above. The three-row packing and minimum card sizes take precedence in this implementation.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: art-through-time


#### Played

- Cold Grade 7 solo run before builder notes/source: all 21 works, all 11 events, earlier-work misses, invention and Compare threads, overview and preview. Played the projection flow too. The authentic works and walnut gallery reward exploring; the original finish hid its record behind an unnecessary Next event.

#### Findings fixed

- Should fix, family:art-museum, Timeline: source-side Learned from buttons reversed history. Source now says Influenced; recipient keeps Learned from. Verified Duccio/Carnevale in both directions.
- Should fix, general, completion: eleventh placement now opens the earned record immediately. Illustrated event/work entries replay the student's exact connections. Read no longer prefixes the previous event. Fixed compact record clipping and the hint shrinking over progress.
- Should fix, family:art-museum, keyboard: removed role=listitem from native buttons, sorted clusters and cards in time order, included clusters in Left/Right navigation, and restored visible focus after cluster zoom. Native keys verified.
- Should fix, general, audit-confirmed craft: fixed the wide-overview Maya/break overlap, kept Benin's full history note and thread controls visible, and preserved a still-valid welcome during quick navigation taps. Targeted frames and voice logs passed. Cluster focus also survives resize and closing a work at overview zoom.
- Should fix, general, phone opening: centered its first artwork, previously clipped at the right edge. Header, main controls and band remain in view.
- Should fix, general, voice inventory: added no-thread, candidate, recap and Benin context lines; lines.json and allLines agree. Held-click checks: threadHow 1 spoken/5 opens; miss events 5 spoken/5 attempts. Read on the completed record speaks the current state.
- Polish, art: replaced the later enclosed-cab railway illustration with an early open-footplate locomotive, retaining the painted museum-catalog style. Final keyed image checked on parchment and in the dealt card.

#### Findings left

- Should fix, general, prescribed content: current Met Hatshepsut date, Mihrab's sacred inscriptions, and partly figurative Cannons conflict with the supplied wording. Kept spec text under the explicit spec-disagreement rule; explained in notes and Left open.
- Polish, general: longer work contexts and the eleven-entry record scroll inside the desk. Short thread, placement and filter choices stay visible; Benin's history note remains visible too.

#### Flattest moment left

- Overview clusters temporarily replace pictures with counts. This specified navigation state remains less involving than opening authentic work. The formerly flat finish now reveals the student's illustrated connection record immediately.

#### Graphics

- Inspected all 21 authentic works and all 12 event images on final-size contact sheets; all are present and used. Correct seated Hatshepsut image confirmed. No generated people; authentic people assets are conservatively marked people:true.
- Redrawn: art/rail.webp, 360 by 178, about 19 KB; original saved in Scratch. Built-in image tool, complete prompt in art/prompts.json, rekey with holes/despill. No downloads or audio recordings.
- Bundle: 1,416,541 bytes, below 2 MB. Museum frames, detail zoom, threaded arcs and rich materials retained. Looked at both supplied bar tools without writing their folders.

#### Audit

- Completed once, exit 0, within the 40-minute limit: 42 leads, no runtime errors. Ports 9961 and 8765. Original evidence: _scratch/art-through-time/review-audit/audit.md. Re-shot only repaired views; no second full audit.
- Confirmed leads fixed: Maya/break overlap, Benin's hidden two-button thread rack, and five welcome cuts on quick All/filter taps. Repaired 1000, 680 and 375 views, five quick-tap logs and focused resize checks passed.
- Answered remaining groups: horizontal timeline travel is required; the complete eleven-entry record is optional browsing, not a hidden short answer set. Close covers only an empty mount corner, not artwork. Nine opening taps correctly substitute the current thread instruction for the stale welcome. Native Whalers/Courbet/Mucha clicks all selected correctly with a fixed deal. Fixed-work Spotlight resize preserved selection, focus and enabled threads; the original lead compared different random works.
- Focused evidence: all required STANDARDS sizes in both modes, 375 iframe, grayscale, Motion off, keyboard, real band/event drags; inspected every shot produced. Zero tool runtime errors. First phone host favicon 404 was removed in the Scratch harness; follow-up was clean.
- Browser checks passed all 231 event/work pairings, shared-cause connections, all 24 thread endpoints, and base card overlaps at 1366 by 768. Chronology and contrast recomputed independently: text ratios 5.50 to 13.45, thread/walnut ratios 6.32 to 7.97.
- Fresh sensitivity evidence: Scratch sensitivity.md. Respectful representation and Benin handling pass; specification-level accuracy concerns remain disclosed below.

#### Left open

- Spec correction: Hatshepsut wall label says about 1479 to 1458 BCE; the current [Met record](https://www.metmuseum.org/art/collection/search/544450) says about 1473 to 1458. Representative -1470 still fits.
- Spec correction: Mihrab to Mondrian says geometry is the whole design, although the [Met record](https://www.metmuseum.org/art/collection/search/449537) explains sacred inscriptions and prayer function too.
- Spec correction: the object-free abstraction event accepts Cannons; [AIC's owning archive](https://archive.artic.edu/modernwing/8991) identifies figures, buildings and a cannon in this work.
- Spec simplifications: photography does not record a scene exactly or single-handedly explain Monet; the press event should distinguish woodblock printing from movable type. The prescribed claims remain unchanged.
- Missing shared art-museum engine/document and the larger-than-60-percent laptop band remain documented in handoff.md; no kit or spec changes authorized.
- Narration remains browser fallback; no recordings were made. No classroom test or audible recording review. No commits, branch changes, publication, or writes to other tools.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Art Through Time build handoff

#### Cold review changes, November 3, 2026
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

#### Structure
`src.html` starts from the kit starter, with responsive museum-desk CSS, an embedded family adapter, then the timeline and challenge logic. `content.json` is actually loaded by the source and supplies all 21 works, 12 events and 24 threads. Art tokens resolve through one image map so each image is bundled once. The tool has no runtime requests.

The timeline uses the representative numeric years and a piecewise compressed scale. The base band length is 6,000 pixels; zoom ranges from whole-band overview to two times. Work and event packing is separate. Isolated works receive larger frames; close works use 80-pixel slots in up to three rows. Compact previews start at zoom two and use two work rows, three event rows, and 56-pixel work cards. Clusters represent crowded overview regions. The timeline redraws at real CSS pixels on resize.

`Curio.voice` owns speech, Read, once-only how lines, and scope checks. Every new action interrupts stale narration and completes thread drawing. Result lines are events, and the fixed lines select bank voice upbeat-guide. No recordings were made. The browser voice is the current fallback.

The challenge retains its order, placed-event set and chosen connections for the session. Photography, Cezanne and abstraction each draw both correct threads after either is placed. Japan accepts Mucha only. The lost-wax card has no year and is compare-only. The final record lists the student's own connections.

#### Decisions and open questions
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

#### Engine changes wanted
- `kit/art-museum.js`, missing: add `frame`, `label`, `zoomTo`, `unzoom`, `pins`, `pair`, `finish`, and `dispose` using the work API in Art Style Match's spec. Frames need resize fitting, preserved aspect ratio, interruptible zoom, 44-pixel controls, and object mounts distinct from flat frames. This tool embeds the already built Art Style Match adapter, rather than creating a competing shared implementation.
- `docs/families/art-museum.md`, missing: document the record fields, fractional detail coordinates, frame fitting, Motion behavior, and keyboard behavior. No shared files were edited.

#### Cold review focus
Inspect cultural framing, the handscroll crop, the Benin note, and the simplified historical explanations. In particular, the spec's photography-to-Monet wording and its use of printing presses as the event behind a woodcut deserve a teaching review. Compare never claims influence. The detailed mechanical outcomes and any remaining limits are in codex-report.md.

This is Build only. No commit, deployment, branch change, shared engine change, or polish round was started.

#### Build audit and repairs
The full audit ran once on Chrome 9981 with host 8785 and completed with 86 leads and no runtime errors. Its original report stays in Scratch. Targeted follow-ups fixed medium-height packing, cluster boundaries, axis-label collisions, phone work-view geometry, real-sized zoom glyphs, Spotlight focus, navigation welcomes and repeated-tap speech cuts. The complete audit was not rerun after these repairs.

Read now retains priority while a later action draws a thread and queues its explanation. Completed and already-solved challenge states do not queue the opening drag instruction when revisited. Repeated taps on the same work or mode do not cut a still-applicable instruction. Old threads fade at the eight-thread limit, and crowded overview tick labels wait for zoom rather than colliding.

The final semantic check again tested every one of the 231 event/work pairings and all eleven placements with zero failures. The final native checks include keyboard placement, five different work opens at two-second intervals, quick taps, a fixed-work Spotlight resize and real mouse event dragging. Final bundle: 1,413,893 bytes, with 978,536 bytes of finished art.

The built neighbor's source and handoff were read. Its refine.md did not exist in this checkout. The shared family adapter and its source spec supplied the missing engine contract.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
