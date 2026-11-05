# Codex report: art-through-time

## Built
- Offline Timeline and What Changed?, 21 authentic museum works, 12 generated event illustrations and 24 threads.
- Real-pixel compressed timeline, three-row packing, draggable scrolling, mini-map, era travel, zoom, clusters, filters and Spotlight.
- Work frames, zoom, wall labels, contextual lines, the Benin note, session checks and an earned eleven-connection record.
- Tap, keyboard and real drag placement; immediate response, interruptible thread drawing and event settling; Motion, Sound and Read through the kit.
- Build only. No commit, deployment, branch operation, shared-file edit or polish round.

## Numbers check
- Scratch `numbers.json`: all 11 accepted-event chronologies pass. Japan 1858 does not change Mishima 1833; it accepts Mucha 1897.
- 24 threads, including two lost-wax comparisons. Shared causes each draw both accepted works.
- Differences: 1,512, 567, 172 and 1,230 years, agreeing with the spec's approximate labels.
- Three-row 80-pixel packing minimum was 5,564 pixels, not the spec's estimated 5,750. Required base length remains 6,000 pixels. The post-1000 scale is about 4.54 pixels/year before end margins.
- Contrasts: white/brand 8.58, brand/paper 7.31, ink/paper 13.45, paper/walnut 11.62, muted/paper 5.50; thread colors/walnut 6.32 to 7.97. All meet their specified thresholds.
- Layout exception: the 456-pixel band at 1366 by 768 is about 67 percent of its stage, exceeding the spec's 60 percent so three rows retain their required minimum sizes without overlap. Details are in handoff.md.

## Feel check
- Best moment: pull the press thread from the authentic Rhinoceros and watch the painted printing press connect to the framed woodcut. The final record then makes the whole session specific to the student's choices.
- Flattest moment 1: isolated works were small inside a large band. Enlarged isolated frames to 124 by 140 pixels while retaining compact frames and three rows in crowded years.
- Flattest moment 2: a correct event initially changed only an outline. It now appears and settles onto the band, draws every accepted connection, and adds the chosen connection to the final record.
- Played the whole explore-to-challenge flow with held mouse input: an intentional earlier-work mistake, all 11 events, and the earned record. Zero runtime errors. Also checked real band dragging, event dragging and keyboard placement.
- Compared `student/pulled-thread.png` beside `bars/bar-beat.png` in Scratch `bar-comparison.jpg`, after opening both required bar tools. The walnut, authentic frames and painted objects have comparable visual finish; this is a contemplative history explorer, not a timed music activity.
- Overview clusters deliberately exchange art detail for navigation; opening a cluster or a work restores the image. That is the least visual state, as specified.

## Done when
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

## Wave lessons
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

## Audit leads
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

## Frames looked at
- Both bar frames; all three first frames, all three second frames and all seven focused frames.
- Every full-run PNG: Timeline and What Changed? at 680, 800, 1000, 1280, 1366, 1920, 760 and 375 widths.
- Full-run semantic record, calm, gray, overview, keyboard, five opens, five misses, real band drag, real event drag and tap-during-thread frames. Five specific audit lead frames were inspected; the report does not claim a visual review of every auto-generated audit image.
- Follow-ups: fixed-1000, fixed-phone, fixed-phone-changed, show-me-preview, preview-beninnote and zoom-detail.
- Student run: pulled-thread, six-connections, earned-record. Final event contact sheet and museum contact sheet. Comparison image inspected.

- Every targeted audit-follow-up PNG: three repaired dense layouts, four repaired overviews, phone grid, fade, navigation welcome, Read priority, completed return, solved return, keyboard placement and final preview Benin note.
- Every final PNG: semantic record, two mode quick-taps, same-work quick-taps, five distinct opens, finished fade, overview labels, Spotlight resize and the no-thread work view.

## Art made
- 12 original event images, no generated people, plus 21 supplied authentic works. All 33 finished assets are used.
- Total finished art 978,536 bytes, about 956 KiB; final bundle 1,413,893 bytes.
- Preserved original museum assets in Scratch, compressed each supplied work below 40,000 bytes, and made the labeled 16:9 handscroll section. Fine-detail Rhinoceros and Mihrab needed lower WebP quality to meet that limit; their final displayed images were inspected.
- No image redraws were needed. Rekeyed ship, candle and lost-wax with hole removal and despill to remove magenta remnants. Final contact sheet inspected after those changes.
- Built-in OpenAI gpt-image; exact prompts and drawn_by metadata are in art/prompts.json. Generated originals copied into art/raw/.

## Art still to paint
- None. Authentic museum images containing people were supplied, not generated. Narration recordings were intentionally not made in this build.

## Engine changes wanted
- Missing `kit/art-museum.js` and `docs/families/art-museum.md`. Exact requested functions and behavior are listed in handoff.md. Embedded the existing Art Style Match local adapter; no shared path was written.

## Left open
- Cold review, including cultural framing and the spec's simplified historical causal wording, remains the next stage.
- Museum source-route limits: Met Benin/Chola essays and the NGA slideshow could not be fetched; three AIC work pages returned 403. Supplied metadata and art were retained. Current available essay routes and the Smithsonian return reference are in notes.md.
- No voice recordings: upbeat-guide metadata is ready; kit browser speech is the audible fallback.
- The full audit predates the final repairs. Targeted repaired layouts, narration and semantic checks passed; a fresh cold review is still required.
- Long work views and the final record may scroll in the narrow phone desk. Header, era travel, zoom and the band remain visible.
- The band is larger than the spec's stated 60 percent at the common laptop size, as explained above. The three-row packing and minimum card sizes take precedence in this implementation.
