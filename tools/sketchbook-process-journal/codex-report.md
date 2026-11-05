# Codex report: sketchbook-process-journal

## Built

- Offline Sample book, My book and Idea map, with the specified issue facts, tradition traits and seven-page Theo sample.
- Mouse, pen-pressure and touch drawing; four thumbnails; studies; revisions referencing earlier thumbnails; plan form; 24 named swatches; optional decision tags.
- Guarded automatic device saving, 20-step Undo, confirmed clearing and deletion, old-source preservation, 12-page limit, keyboard access and Curio.voice.
- Own light desk-and-paper scene, 15 generated illustrations, a quiet light animation and immediate drawing/selection feedback.
- Build only. No commits or polish round. Writes stayed in the two authorized folders. Existing bar bundles were opened without writing to those tools.

## Numbers check

- `numbers-final.json` independently counts the actual sample tags: research 3, borrowed 2, broke 2, own 2, total 9.
- Contrast: brand/paper 6.434:1, white/brand 7.129:1, ink/paper 15.586:1, muted/paper 6.595:1. White node letters: research 6.656:1, broke 7.292:1, own 6.381:1.
- The spec's 1.9 MB storage estimate omits base64. Its conservative 48 drawings at 40 KiB become 2560 KiB as base64, before metadata. The actual book permits at most 40 drawings because pages 1 and 2 are fixed, giving 2133 KiB under that assumption. Storage failure is handled on screen.
- Source dates, Fahrenheit intervals, plastic tonnage and the 5 mm threshold are retained as supplied source inputs. Fahrenheit interval conversions were also recomputed in `numbers.json`; no new converted values were added to the UI.

## Feel check

- Played Theo's complete book, opened every map decision, then made an issue/tradition choice, thumbnails, tags, study, revision and plan.
- Best moment: Theo's final cardboard still life beside its material and microplastic decisions, followed by seeing my own thumbnail enter the same source map.
- Flat moment 1: the raw paper texture competed with the text and art. A translucent cream layer now keeps its tooth without turning every page into visual noise.
- Flat moment 2: the compact drawing grid felt cramped and phone canvases overlapped. The phone now shows full-width boxes in a vertical strip; compact landscape rows keep a usable drawing size and scroll inside the working leaf.
- `comparison.png` places the tool beside Beat Lab. The large original art, paper, spine, desk and source map carry comparable visual weight while fitting this journal's purpose. Snowy Mail Route was also opened for immediate feedback and motion reference.
- This is an investigation studio, not a scored game. Its later depth is the student's studies, deliberate breaks and evidence-backed revisions, culminating in a specific plan and map.

## Done when

1. PASS. The book occupies over 60 percent of the 1366-wide screen; book and map remain the dominant region at 680x425. Full-size frames and compact targeted frames were viewed.
2. PASS. Exactly nine sample nodes. All nine cards were opened with real held clicks and each Open this page reached the expected sample page.
3. PASS. Add page is locked until both choices are confirmed. The hint and narration do not name it while locked. The keyboard and student runs checked this.
4. PASS. Real jittered mouse strokes, CDP pen and touch input, compressed 800x600 saving and reload persistence passed. Undo restored the first drawing after undoing the latest 20 of 21 strokes. Physical pen hardware was not available.
5. PASS. All four tag kinds appear with shape, letter and linked source. Filter classes and visual dimming were checked, including the final old-tag opacity correction.
6. PASS. Changing the issue retained every existing tag and showed the previous research source gray with the old-issue label.
7. PASS. Twelve-page horizontal scrolling and fixed sources passed. Final 760 and 375 layout checks are recorded below.
8. PASS. Five held page adds had gaps of 2037, 2050, 2047 and 2058 ms. tagHow started once, no spoken how line repeated, both new broke-from tags started firstBreak, Read was logged and the post-Read mode change completed without errors.
9. PASS. All 15 final WebPs were opened and inspected; art tokens load. No people, human body parts or fake lettering; WPA bands are blank. The skull-image conflict was resolved as described in the handoff.

## Wave lessons

- Hint and voice: PASS. Hints update with state, Read uses the visible current hint, compact instructions name Tags, disabled Add and final-page Next are not named. The five-add pace run passed.
- Focus and layout: PASS. No load focus; page picker focus after adding, deleting or clearing; dialogs restore focus. Keyboard-only journey passed eleven checks, including delayed Clear persistence. Compact modal/choice action fixes received targeted checks.
- Sizes: PASS for primary controls, with the phone secondary-panel limitation below. One full STANDARDS run, then only affected compact and phone states. Targets are 44 px; long editors deliberately scroll. See Left open for strict short-choice audit leads.
- No giveaways: PASS, not applicable to a scored puzzle. The student authors choices; there is no hidden correct answer or success meter.
- Honest numbers: PASS. Research dates remain visible, historical estimates are not represented as current totals, plan dimensions are labeled in cm and sample counts are computed from tags.
- Standards: PASS. Solo students generate alternatives, investigate contextual traditions, study and revise, and explain research/history connections in a final plan. No family engine is specified.
- Motion off: PASS. The decorative light stops, while drawing and navigation remain immediate. Calm and grayscale frames were viewed.
- Short choices in view: FAIL under the literal audit rule for map nodes; the spec requires a scrollable map. Issue/tradition pickers show all three cards. Choice confirmation and modal actions stay outside their scrolling content. Long page, palette and tag editors retain scrolling rather than shrinking type.
- Resize mid-animation: PASS. The final audit reported no exceptions or stuck controls. No moving simulation owns a stale geometry reference; canvas coordinates use current rectangles.
- First-tap welcome: PASS. Curio.voice owns first-tap ordering with mode scope and stale checks, without welcomeAfter. Sample navigation and page additions were exercised with held clicks.
- Unknown stays unknown: PASS. Empty drawings are blank, untagged working pages say Not tagged yet, and a Revision without earlier thumbnails says so.
- One look, one meaning: PASS. R square, T triangle, B split diamond and O circle remain distinct in grayscale. Old-source gray is labeled separately.
- Truthful badges: PASS. Saved reflects a successful write or the specified warning; chosen issue/tradition labels match committed choices. Plan completion checks title, medium, palette and statement.
- Hints change back: PASS. Page and mode navigation recompute the hint; the last sample page points to Prev page and See the map. Compact Tags returns to the current page instruction.
- No answer by copied wording: PASS, not applicable to a quiz. Research wording supplies evidence; students must draw, select an aspect and explain its relationship.

## Audit leads

The one audit finished with 45 leads and 54 frames. It reported no console errors, infinite motion, resize exceptions or stuck controls.
The responses below cover all 35 size/state rows and the 10 counted walk findings. Full wording is in Scratch/audit-responses.md.
Navigation controls now retain DOM identity; the final stable-navigation.json check passed. The full audit was not rerun after repairs.

- 1. 375x812 (iframe host), control below the fold: #seeMap "See the map ↗" top 842: Left open: duplicate phone panel button is below the fold; the equivalent Idea map header control is visible.
- 2. 375x812 (iframe host), control below the fold: #startOwn "Start my own book" top 893: Left open: duplicate phone panel button is below the fold; the equivalent My book header control is visible.
- 3. mode My book, Choose this issue below its scroll view: Fixed: issue/tradition confirmation stays outside the scrolling detail. Compact button bottom is 400 px within 425 px.
- 4. mode My book, compact panel hid Delete/Clear: Fixed: compact My book panel removes introductory text so all four action buttons stay visible; targeted 680 frames checked.
- 5. mode My book, control below the fold: #seeMap "See the map ↗" top 849: Left open: duplicate phone panel button is below the fold; the equivalent Idea map header control is visible.
- 6. mode My book, control below the fold: #deletePage "Delete page" top 900: Left open: occasional phone Delete/Clear actions follow the book; primary drawing, Add and mode controls remain visible.
- 7. mode My book, control below the fold: #clearBook "Clear book" top 951: Left open: occasional phone Delete/Clear actions follow the book; primary drawing, Add and mode controls remain visible.
- 8. mode Idea map, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 9. mode Idea map, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 10. mode Idea map, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 11. mode Idea map, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 12. mode Idea map, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 13. node-card, focus fell to the page after clicking #seeMap (click 1): Fixed: mode transitions focus the visible mode button with preventScroll; final map-focus.json passes.
- 14. node-card, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 15. node-card, modal actions outside its scroll view: Fixed: dialog actions have their own reserved row and the body scrolls; 680 and phone frames show both actions.
- 16. node-card, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 17. node-card, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 18. node-card, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 19. node-card, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 20. thumbnails, small target: #pad-0 "Thumbnail 1. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 21. thumbnails, small target: #pad-1 "Thumbnail 2. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 22. thumbnails, small target: #pad-2 "Thumbnail 3. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 23. thumbnails, small target: #pad-3 "Thumbnail 4. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 24. thumbnails, compact panel hid Delete/Clear: Fixed: compact My book panel removes introductory text so all four action buttons stay visible; targeted 680 frames checked.
- 25. tagged-map, focus fell to the page after clicking #seeMap (click 1): Fixed: mode transitions focus the visible mode button with preventScroll; final map-focus.json passes.
- 26. study, compact panel hid Delete/Clear: Fixed: compact My book panel removes introductory text so all four action buttons stay visible; targeted 680 frames checked.
- 27. plan-form, control with no name: #planTitle: Fixed: explicit aria-label added in addition to the wrapping label; final plan-accessible.json passes.
- 28. plan-form, control with no name: #planStatement: Fixed: explicit aria-label added in addition to the wrapping label; final plan-accessible.json passes.
- 29. plan-form, compact panel hid Delete/Clear: Fixed: compact My book panel removes introductory text so all four action buttons stay visible; targeted 680 frames checked.
- 30. clear-confirm, small target: #pad-0 "Thumbnail 1. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 31. clear-confirm, small target: #pad-1 "Thumbnail 2. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 32. clear-confirm, small target: #pad-2 "Thumbnail 3. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 33. clear-confirm, small target: #pad-3 "Thumbnail 4. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 34. clear-confirm, tagHow dropped during Clear confirmation: Intentional stale drop: a confirmation dialog replaces the drawing instruction. It is not marked heard; Read and later page entry remain available.
- 35. compact-tagged-map, focus fell to the page after clicking #seeMap (click 1): Fixed: mode transitions focus the visible mode button with preventScroll; final map-focus.json passes.
- 36. Control walk, Sample See the map lost focus: Fixed: the arriving mode button receives focus; stable navigation DOM and map focus were verified.
- 37. Control walk, Sample Start my own book lost focus: Fixed: the arriving mode button receives focus; stable navigation DOM and map focus were verified.
- 38. Control walk, My book See the map lost focus: Fixed: the arriving mode button receives focus; stable navigation DOM and map focus were verified.
- 39. Control walk, Next page skipped welcome: Intentional per spec: welcomeSample is stale after a tab or Next page. It stays unmarked and can play on a later mode entry.
- 40. Control walk, 2 Tradition skipped welcome: Intentional per spec: welcomeSample is stale after a tab or Next page. It stays unmarked and can play on a later mode entry.
- 41. Control walk, 3 Thumbnails skipped welcome: Intentional per spec: welcomeSample is stale after a tab or Next page. It stays unmarked and can play on a later mode entry.
- 42. Control walk, 4 Study skipped welcome: Intentional per spec: welcomeSample is stale after a tab or Next page. It stays unmarked and can play on a later mode entry.
- 43. Control walk, 5 Revision skipped welcome: Intentional per spec: welcomeSample is stale after a tab or Next page. It stays unmarked and can play on a later mode entry.
- 44. Control walk, 6 Revision skipped welcome: Intentional per spec: welcomeSample is stale after a tab or Next page. It stays unmarked and can play on a later mode entry.
- 45. Control walk, 7 Plan skipped welcome: Intentional per spec: welcomeSample is stale after a tab or Next page. It stays unmarked and can play on a later mode entry.

## Frames looked at

- `bar/`: Beat Lab and Snowy Mail Route; `comparison.png`: side-by-side with Beat Lab.
- `early/`: three initial book/map frames, used to correct texture and compact sizing.
- `student/`: all seven workflow frames, including tagged thumbnails, revision, plan fields, old-source map and twelve-page map.
- `full/`: all 11 frames, including every desktop STANDARDS size, sample Plan, compact map, My book and grayscale.
- `phone/`: all three final 375x812 host frames, after the phone grid fix; the earlier affected frames were also inspected.
- `keyboard/keyboard-map.png`: final keyboard focus and filtered map. The first harness attempt required the driver's Enter event character, not a tool repair.
- `audit/`: all 54 PNGs viewed in seven QA sheets, with affected compact states also opened individually.
- `targeted/`: all eight frames; `final-checks/`: all five frames; `phone-final/`: all six frames; `last-hints/`: both limit-choice frames.

- `first-card/first-card.png`: final first-tap issue-card welcome suppression; zero stale welcome starts and no console errors.

## Art made

- Fifteen finished illustrations made with the built-in OpenAI image tool. House style, prompts, drawn_by and provenance are in `art/prompts.json`; raw PNGs are in `art/raw/`.
- Total art: 1015.4 KiB. Every finished image is below 80 KiB; long side is 1000 pixels. Bundle: 1450.4 KiB, below 2 MB.
- One redraw: the monarch scene's misleading snowy alpine background became a close central Mexican oyamel fir-forest interior.

## Art still to paint

None. The prohibited human skull imagery has intentional object substitutions; it is not waiting for generated people. Historical skull symbols remain in the text.

## Engine changes wanted

None.

## Left open

- Clear-teacher/Iapetus remains the planned bank voice. No audio was recorded or listened to. Runtime speech uses the browser voice. A grown-up bank voice is an owner-side follow-up, as noted in the spec.
- The full map scrolls horizontally, and compact layouts also scroll its lanes vertically. The source column stays fixed during horizontal scrolling. Long tag and plan fields scroll inside their leaf.
- Environmental source claims follow the supplied spec; no external source-verification pass was performed.
- The full audit predates the final targeted corrections and was not rerun. Six authored phone states used an incorrect size name in that audit configuration and were skipped; the file is corrected for cold review, and targeted phone frames cover issue, tradition, drawing, study, plan, dialog and the twelve-page map.
- Temporary host.html was removed and every Chrome/server started by these checks was closed. No git operation changed the checkout.
