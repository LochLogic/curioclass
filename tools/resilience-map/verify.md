# Verify: resilience-map (cold, 2026-10-26)

**Verdict: FIX** (no blockers; 5 should-fix, 5 nits)

Checked against spec.md, BATCH-SEL.md, STANDARDS.md, TOOL-CONTRACT.md and VERIFY.md. Bundle rebuilt with
`CURIO_DRAFT=1 python scripts/bundle_tool.py resilience-map` (322 KB, 8 voice clips inside). Driven in muted headless
Chrome over CDP (a copy of drive.py on private port 9791, iframe host on 9071, both in the temp dir) with held clicks and
real keys at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 760x600 and 375x812 (iframe). No
console errors or exceptions in any shot. No horizontal scroll at any size.

## What passes

- **988 wording.** I checked 988lifeline.org today. It gives the name "988 Suicide & Crisis Lifeline", Call / Text / Chat,
  "available 24/7/365", "free and confidential" and "The 988 Lifeline is for everyone." The footer line, the More help
  dialog, the Lighthouse card and the plan's Any time box match the spec word for word. Every 988lifeline.org link goes
  to `https://988lifeline.org` with target _blank and rel noopener. 911 is sourced to 911.gov.
- **No disclosure, no labels.** No input, textarea or contenteditable anywhere (checked: 0). All eight situations are
  fictional and ordinary. Nothing asks what is stressing the student. There are no scores, counts, badges, confetti or
  "complete" states. The only number is "Box full (4)", which the spec calls for. The dialog line "It can't tell you
  what you feel or diagnose anything" is there. The tone is calm and plain and fits grades 9-12.
- **Plan storage (Done 5, 6).** With a fresh load there is no `curio-resilience-plan`. Picks stay in page memory until
  Save, which writes ids only (`{"signs":["heart",...],"change":[],...}`) and shows "Saved on this computer." A reload
  restores it without a message. Clear asks first ("Keep it" changes nothing). "Yes, clear" empties all four boxes and
  removes the key, and focus goes back to Clear. A fifth chip is refused with "Four is plenty. Remove one to add
  another." and the plan does not change. Add-from-card reads "Box full (4)" and is disabled when the box is full.
- **Print.** Print media hides header, main, footer and dialog and shows only the plan card plus Any time, in black on
  white (frame print-full.png). With nothing picked, only Any time is filled in.
- **Routes (Done 2).** All 8 situations x 2 halves light exactly the spec's pins, in order. The path is solid for "can
  change" and dashed 14/9 for "can't". The wrench and wave glyphs differ, so the halves read apart in gray. The
  Lighthouse is never dimmed.
- **Content (Done 4).** I script-compared all 20 landmark cards (what / try it small / fits / sources), the 7 hotspot
  texts, all 8 situation labels and the 46 route "how it fits" lines with the spec Content. All match.
- **Help reachable.** The footer and More help are on screen in every mode at every non-stack size, and the short line
  shows under 500 px tall. The dialog traps Tab (link and Close), Esc and Close both close it, and focus returns to
  More help.
- **Voice (Done 8), held clicks.** One welcome per mode, never repeated. Read stops other speech and speaks the current
  hint. Lines that come in during Read wait for it. Sound off is silent, and turning Sound back on speaks the current
  mode's unsaid welcome. All 8 lines match voice/lines.json word for word.
- **Motion off (Done 9).** The beam has `animation-name: none` and holds at opacity .3. The route swaps instantly (one
  route group, no fade). Content is the same.
- **Keyboard (Done 10).** Tab order is: mode buttons, Motion/Sound/Read, the 8 situations, the pins west to east, the
  footer link, More help. Enter opens pins and hotspots. Focus rings show on the header, the segmented buttons (inset
  ring), chips and hotspots.
- **Contrast I computed** (WCAG 2.1): brand on panel 8.65:1, brand-ink on brand 8.89:1, ink on footer 15.31:1, focus
  #8fe3ff on panel 12.0:1, legend 10.8:1, chart axis 8.25:1. All pass.

## Builder's calls

- **Read as the first tap skips the welcome:** right. STANDARDS.md "Voice behavior" says exactly this.
- **h-sit narrated on the first situation pick:** fine. It is a recorded hint, said once. On a first tap it replaces
  the welcome (unmarked), as the standard says.
- **Help line spoken when More help opens:** I disagree. See should-fix 1.
- **The added "kind" line on landmark cards** ("Action Ridge · Works on the problem"): good. It ties each card to the
  two kinds of coping the switch teaches, it is not a label on the student, and the Lighthouse card leaves it out.
  Keep it.
- **Solid vs dashed routes instead of dotted:** right. The spec contradicts itself ("dotted path" in What responds,
  "solid" and "long-dash" in Route styles and the legend). The builder followed the specific rule. Fix the spec's
  "dotted" wording so a later re-verify doesn't flag it.

## Blockers

None.

## Should fix

1. **More help reads the help line out loud on open** (src.html:924-927, `cue([L.help], 250, () => dlg.open)`).
   - Repro: click More help with Sound on. The clip "If you need to talk, a trusted adult at school can help..." starts
     at about 250 ms, every time the dialog opens (v-firsthelp shot).
   - Why it matters: on a laptop in a classroom, speakers announce to the room that this student just opened the help
     dialog. That is an involuntary disclosure, the very thing BATCH-SEL.md guards against. The text is already on
     screen.
   - Fix: don't speak it on open. Let the student choose: a small "Read this" button inside the dialog (Read in the
     header is behind the modal), or simply no narration there. Keep the recording for that button.
2. **Clicking a pin or a route item scrolls the switch and situation buttons out of view** at every compact size and at
   1280x720 and 1366x768 (src.html:824, `scrollIntoView` on `#lmSec`).
   - Repro: pick Priya, then click the Talk it through pin. The panel scrolls about 420 to 650 px. The switch sits at
     y=-346..-302 at 680x425, -5..39 at 1280x720 (clipped), and the situation buttons are off screen (sitpin-* shots).
     A route-item click does the same at 1000x625 and up (sitroute-*).
   - Why it matters: the core loop is flip, look, flip. After one pin the student has to scroll back up to flip.
     STANDARDS.md says main controls stay visible at every size.
   - Fix: make the switch (and the selected situation's name) sticky at the top of the panel while a situation is
     picked, or show the landmark card in a fixed slot above the route list in compact, or don't auto-scroll on a pin
     click when the card's top is already within reach.
3. **Clear situation drops focus to `<body>`** (src.html:794 and 806).
   - Repro: pick Dev, focus Clear situation, press Enter or click it. `document.activeElement` is BODY (k-clearsit,
     k-clearsit-click).
   - Cause: `renderSit()` disables the button that has focus.
   - Fix: after clearing, focus the situation button that was selected (or the first situation button).
4. **The focus ring on a dimmed pin fails contrast** (`.pin.dim{opacity:.32}` covers `.fring` too).
   - Repro: pick Dev, Tab to Unwind. The white dashed ring renders at about 2.1 to 2.8:1 on village, land, woods, ridge
     and sea (computed; zoom frame z1.png). That is under the 3:1 WCAG 1.4.11 minimum, and these pins are still
     working buttons.
   - Fix: `.pin.dim:focus-visible{opacity:1}` (or put the ring outside the dimmed group). Dimmed pin labels (`.lbl.dim`,
     about 2.5:1) are also low for clickable items; .55 opacity would read as "off the route" and still be legible.
5. **Stack layout (760 wide, 375 wide): More help and the main controls are below the fold.**
   - Repro, 760x900 map: the 620 px map comes first, the situation buttons start at y=846 and More help is at
     y=1231..1275 on a 1285 px page.
   - Repro, 375x812 iframe: More help is at y=1004 (map), 1378 (situation picked) and 2304 (plan). In My plan the chips
     and Save/Clear/Print sit under the whole card (h375-plan).
   - The Lighthouse pin on the map is visible and opens the same help lines, which softens this. The footer is still
     not "always reachable" without scrolling on a phone or a narrow window.
   - Fix: in stack, cap the map height at about 55% of the viewport, and keep a slim sticky footer (the short line plus
     More help) at the bottom of the viewport, or add a More help button to the header in stack. In stack My plan, put
     the chip groups and actions before the card, or collapse the card behind a "See my plan" toggle.

## Nits

1. **notes.md, step 2**: calls the switch "I can change it" / "I can't change it". The tool says "The part they can
   change" / "The part they can't". Use the tool's words so the teacher's script matches the screen.
2. **"Get help" label hidden in compact** (680x425, 800x500, 760x600): only open and route pins get labels, so the
   Lighthouse shows no "Get help" name (only the area label "The Lighthouse"). Always label the help pin.
3. **Route path order is hard to read**: the harbor-to-first-pin curve often runs under the second pin (Dev's change
   route goes harbor to Small steps right through Plan with times, then doubles back), so it reads as the wrong order.
   Add small order numbers (1, 2, 3) on the route badges, or start the curve from the nearest-to-harbor pin.
4. **Printout has no Curio Class credit line**, but the on-screen card has "Made with Resilience Map, Curio Class."
   Add the same line to `#printPlan` for consistency.
5. **Verb mix**: hints say "Click a pin" in the map and body but "Tap chips" in My plan. Pick one ("Click" fits
   laptops).

## Re-verify (cold, 2026-10-26)

**Verdict: FIX** (no blockers; 2 should-fix, 6 nits)

Bundle rebuilt with `CURIO_DRAFT=1 python scripts/bundle_tool.py resilience-map` (333 KB; the old bundle predated the
h-plan re-record). Driven in muted headless Chrome over CDP (own driver, devtools 9911, http 9151, all in my temp
dir) with held clicks and real keys at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 760x600,
and 375x812 and 375x667 in an iframe host. No console errors or exceptions (the only log line is the test server's
favicon 404). No horizontal scroll at any size. The only URLs in the bundle are the SVG namespace and the
988lifeline.org links.

### The 5 should-fix from the first verify

1. **More help no longer speaks on open: fixed.** Opening it starts no clip (with a Read clip playing, the clip stops
   at once). Nothing queued plays while it is open. "Read this" plays the help clip only on a press, Close and Esc
   stop it, and focus returns to More help. More help as the first tap queues no welcome.
2. **Switch scrolled out of view: fixed.** With Priya picked, a pin click and a route-item click leave the sticky bar
   (name, Clear situation, both halves of the switch) on screen and unobstructed at every size: y=108..152 in compact,
   140..184 at 1280x720 and 1366x768, and at the bottom edge above the footer in stack. On the builder's note: the eight
   situation buttons do scroll away after a pin click in compact and at 1280/1366 (about -300 px). I find that
   acceptable. Switching situation is rarer than flipping, the picked name and Clear situation stay on screen, and Clear
   puts focus (and scroll) back on that situation's button. All eight are on screen on load at 680x425 and 1366x768, so
   Done-when 1 holds.
3. **Clear situation focus: fixed.** Enter on Clear focuses the Dev button that was picked. A mouse click focuses Lena's
   button with no ring, which is right for a pointer.
4. **Dimmed pin focus and label contrast: fixed.** A dimmed pin reached by Tab goes to opacity 1 with the white ring
   (6.9 to 15.4:1 on village, land, woods, ridge and sea). Dimmed labels at .62: 6.2 to 6.4:1 against their own halo,
   3.1 to 5.9:1 against the ground.
5. **Stack layout: fixed.** At 760x900, 375x812 and 375x667 the footer (short line plus More help) is sticky at the
   bottom in all three modes and never covers the sticky situation bar. In stack My plan the chips come first (panel at
   y=151, card at 1690).

### Nits from the first verify

All five are fixed: notes.md uses the tool's switch words; "Get help" is labeled at every size and in all 16 route
states; route pins carry 1, 2, 3 badges; the printout ends with "Made with Resilience Map, Curio Class."; the plan hint
says "Click chips" and its new clip plays.

### Regression checks that pass

- **Routes (Done 2):** all 8 situations x 2 halves at all 8 desktop sizes light exactly the spec's pins, in order, with
  numbered badges; solid with wrench for "can change", dashes 14/9 with wave for "can't". The Lighthouse is never
  dimmed.
- **988 and help (Done 3):** footer, short line, More help dialog, Lighthouse card and Any time box match the spec word
  for word. I checked 988lifeline.org today: "988 Suicide & Crisis Lifeline", call, text or chat, "available
  24/7/365", "free and confidential", "The 988 Lifeline is for everyone." Both links go to https://988lifeline.org,
  target _blank, rel noopener. The dialog traps Tab (link, Read this, Close, both ways); Esc and Close return focus.
- **Content (Done 4):** all 20 landmark texts, 8 situation labels, stories and halves, 46 route lines, 7 hotspot texts,
  the note and the legend are found verbatim in spec.md.
- **No disclosure, chips only (Done 5, 7):** 0 input, textarea, select or contenteditable. No scores, badges or
  "complete" states. Nothing asks about the student.
- **Storage and plan (Done 5, 6):** no key on a fresh load; picks stay in memory; Save writes ids only and shows "Saved
  on this computer." for 3 s; reload restores silently; Clear asks (focus to "Keep it"), Keep changes nothing, "Yes,
  clear" empties all boxes and removes the key; a failing setItem shows "Couldn't save here. Print it instead." A fifth
  chip is refused with the message; card and hotspot Add buttons read "Box full (4)" and are disabled; "both" landmarks
  go to box 3; the help card has no Add button.
- **Print:** only #printPlan shows, black on white; zero picks prints blank lines plus Any time.
- **Voice (Done 8), held clicks, clips logged as they started:** `allLines()` equals voice/lines.json (8 lines), and
  every line has a clip in the bundle (h-plan is the new c530670a846e.mp3). No browser-voice fallback ran. One welcome
  per mode, never repeated. A situation or Read as the first tap skips the welcome. Read stops other speech and plays
  the current hint's clip in all three modes. With Sound off nothing plays; Sound back on plays w-map.
- **Motion off (Done 9):** beam `animation-name: none` at opacity .3, one route group swapped instantly, pin
  transitions at 0.01 ms. Turning Motion on brings back the 4 s beam.
- **Copy:** no em or en dashes in the bundle, notes, spec or tool.draft.json; "Curio Class" on screen, "Curio" alone
  only as code identifiers.

### Should fix

1. **In My plan, keyboard focus goes under the sticky Save/Clear/Print bar** (src.html:125-127, `.acts` sticky, nothing
   reserves room for it when focus scrolls the panel).
   - Repro: My plan, Tab through the chips. At 1366x768, 15 chips end up fully covered (44 of 44 px) by the bar at
     y=612..719: Keep a sleep routine, Move more, Question an unhelpful thought, Notice something good, Get outside, and
     School counselor through A faith or community leader (frame planfocus-counselor-1366: "A friend" has focus and
     can't be seen). The same happens at 1280x720 (10 chips) and 680x425 (17 chips).
   - This fails Done-when 10 ("every chip reachable with visible focus") and WCAG 2.4.11. A mouse click aimed at a
     chip there hits the bar instead.
   - Fix: give the panel `scroll-padding-bottom` equal to the bar height (it has `--barh` for the top bar already), or
     scroll the focused chip clear of the bar in a focusin handler.
2. **Map labels overlap in the 680x425 preview and at 375 wide** (placeLabels non-strict fallback, src.html:647, and
   area labels placed with `bad: true`, src.html:621).
   - Checked with getBBox in all 16 route states. 680x425: "Mind Woods" covers the Notice good pin in every state;
     "Join a group" sits under "Plan with times" (Sam, change; frame c680-sam-change reads "Join a Plan with times");
     "Unplug" overlaps "Mind Woods" (Lena and Grace, can't; frame c680-lena-cant); "Talk to someone" overlaps "People
     Village"; "Talk it through" overlaps "The Lighthouse" (Priya and Lena, change). Pin labels also run onto
     neighboring pins (Small steps onto Plan with times, Sleep routine onto Move more). At 375x812 and 375x667, "The
     Lighthouse" overlaps "Talk it through" in all 16 states. 800x500 and up have no overlaps.
   - The 680x425 box is the site's preview, the first frame a teacher sees.
   - Fix: when a route label has no free spot, try more candidate spots or a smaller font before falling back, and drop
     or move an area label that collides (the area name can shift, or hide while a route pin needs that space).

### Nits

1. **spec.md:137** still says "Tap chips to add them." The tool, lines.json and the clip say "Click chips". Update the
   spec so a later verify doesn't flag it. spec.md:17 says "(see open questions)", but the spec has no such section.
2. **Stale voice files:** voice/local.json still lists the old "Tap chips" line, and voice/raw/6d8c00d82fd0.pcm (the old
   take) is still there. They don't reach the bundle.
3. **The route path runs across the Get help pin** whenever the first stop is east of the harbor (Priya and Lena change,
   which start at Talk it through), at every size (frames 1366x768-pin, 760x900-priya). The numbered badges make the
   order clear, but the line through the Lighthouse can read as a stop. Bend the first leg above it, or start the path
   behind it.
4. **680x425 with a situation picked:** the sticky bar at the panel's bottom covers about half of Tomás and Grace
   (24 of 44 px), including when they have keyboard focus. They still work, and they are clear on load.
5. **375 wide, Stress in the body:** the short burst / keeps going switch is at y=833 under a 600 px figure, below the
   fold on a phone. That's acceptable in stack, but a slightly shorter body stage would bring it up.
6. **Dimmed pins on Tab:** the dim-to-full opacity uses the .3 s pin transition, so the ring fades in rather than
   appearing at once. It's harmless and instant with Motion off.

## Re-verify 2 (cold, 2026-10-26)

**Verdict: PASS** (no blockers, no should-fix; 6 nits)

Bundle rebuilt with `CURIO_DRAFT=1 python scripts/bundle_tool.py resilience-map` (328 KB, 8 clips inside). Driven in my
own muted headless Chrome (devtools 10041, http 9251, profile and iframe host in my temp dir) with real keys and held
clicks at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 760x600, and 375x812 and 375x667 in an
iframe host. No console errors, warnings or exceptions in any run. No horizontal scroll at any size. No network URLs
except the 988lifeline.org links.

### The fix-round-2 items

1. **Focus clear of sticky bars: fixed.** I Tabbed forward through the whole page and back again (Shift+Tab) in the map
   with no situation, with Priya, Tomás and Grace picked, in Stress in the body and in My plan, at 1366x768, 1280x720,
   680x425, 760x900, 760x600, 375x812 and 375x667. For every focus stop I sampled the element (a pin's disc, a hotspot's
   pill) with elementFromPoint. Every situation button, switch button, route item, Add button, chip, Save, Clear, Print,
   pin, hotspot and More help was 100% uncovered and on screen at every size. The 15 chips that were under the
   Save/Clear/Print bar at 1366x768 are now scrolled clear, and so are Tomás and Grace at 680x425 when they have focus.
2. **Labels re-placed per state: fixed for overlaps.** I checked 17 states (none plus 8 situations x 2 halves), each with
   no pin open, each route pin open, and Unplug, Regular meals and Get help open (115 states per size), at all 10 sizes
   with getBBox. I found no label-label overlaps, no label on a pin or its badges and nothing off the stage. "Get help"
   and "The Lighthouse" show in all 115 states at every size. 1000x625 and up (and 760x900) show all 20 pin names and
   all five area names. What is dropped at small sizes is in nit 1.
3. **Route path bends around Get help: fixed.** In all 16 route states at all 10 sizes, the path stays at least 12 px
   clear of the Get help disc (at least 15 px at the desktop sizes, 22 px at 680x425).
4. **Instant focus on dimmed pins: fixed.** A dimmed pin that gets Tab focus reads opacity 1 with transition 0s right
   away.
5. **Spec wording: fixed.** No "dotted", "Tap chips" or "open questions" left in spec.md. All 8 lines.json lines are in
   the spec word for word.

### Regression sweep (all pass)

- **Done 1:** all three modes open at every size. At 1366x768 and 680x425 the 8 situation buttons are on screen on load,
  and the switch, Clear situation and More help stay on screen after a pick. More help is fully visible in every mode
  at every size (sticky footer in stack). In stack, Save/Clear/Print come after the chips (as accepted last round).
- **Done 2:** all 8 situations x 2 halves light exactly the spec's pins plus the Lighthouse, numbered 1, 2, 3 in the
  spec's order. Solid path with wrench for "can change", dash 14 9 with wave for "can't". The route ids and every
  "how it fits" line, story and half text match the spec Situations. With no situation, all 20 pins are lit and the
  path is gone once the 300 ms fade ends.
- **Done 3, 988 wording:** the footer line, the short line, the four More help lines, the Lighthouse card and both Any
  time lines are found word for word in spec.md. All three links go to https://988lifeline.org/ with target _blank and
  rel noopener.
- **Done 4:** all 20 landmark texts and all 7 hotspot texts match spec Content.
- **No disclosure (Done 5, 7):** 0 input, textarea, select or contenteditable elements. No scores, badges or "complete"
  states. Nothing asks about the student.
- **More help never speaks on open:** opening it as the first tap plays nothing. Opening it during a welcome pauses the
  clip at once and nothing else starts. "Read this" plays the help clip only when pressed. Close and Esc stop it. The
  dialog traps Tab both ways (link, Read this, Close), and Esc returns focus to More help.
- **Plan and storage (Done 5, 6):** fresh load has no key. Picks stay in memory. Save writes ids only
  (`{"signs":["heart","edge"],"change":["steps"],...}`) and the "Saved on this computer." message clears after 3 s.
  A reload restores the plan silently. Clear asks first and focuses Keep it. Keep changes nothing. "Yes, clear" empties
  the plan, removes the key and returns focus to Clear. A fifth chip is refused with the message. A full box makes the
  card's button read "Box full (4)", disabled. The help card has no Add button. A throwing setItem shows "Couldn't save
  here. Print it instead."
- **Print:** header, main and footer are hidden. Only #printPlan shows, on white, with the Any time box and "Made with
  Resilience Map, Curio Class."
- **Voice (Done 8), held clicks, clips logged as they started:** the 8 clips in the bundle are exactly the 8 lines.json
  lines. No browser voice ran. A pin as the first tap plays w-map once. Each mode's welcome plays once and never again.
  Read as the first tap plays h-map only. Read plays h-body and h-plan in those modes. A situation as the first tap
  plays h-sit and no welcome. h-sit queued during Read waits for it. With Sound off nothing plays on its own, and Sound
  back on plays w-map. Read and "Read this" still speak with Sound off, which is the kit's rule for Read
  (`say(..., true)`).
- **Motion off (Done 9):** beam `animation-name: none` at opacity .3, one route group swapped with no fade, pin
  transitions at 0.01 ms. With Motion on: the 4 s beam and the route cross-fade.
- **Keyboard (Done 10):** Tab order is mode buttons, Motion, Sound, Read, the 8 situations, the 20 pins west to east,
  the footer link, then More help.
- **Copy:** no em or en dashes in the bundle, src, notes, spec, tool.draft.json or verify.md. On screen and in the
  dialog, "Curio" never appears without "Class".

### Nits

1. **Dropped labels at 680x425, 800x500 and 375 wide.** Nothing overlaps now, but the placer drops more than the spec
   says.
   - The "Mind Woods" area name is missing in all 115 states at 680x425, 800x500, 375x812 and 375x667. "Body Coast" is
     missing in all of them at 375 and in 21 at 680x425. Spec line 23 asks for "Five areas, each with a label".
   - Route-pin names are dropped in 13 of 16 route states at 680x425 and 12 of 16 at 375. Ana's "can't" and Lena's
     "can't" show only 1 of 3 names at 680x425 (frames lab-680-ana-cant, lab-680-lena-cant).
   - The open pin often gets no label even though it is placed first. That happens in about 45 of 115 open states at
     680x425 and 375. Unplug and Regular meals never get one when opened, and Plan with times never does when it is on
     a route (it is also dropped at 760x600). Spec lines 34 and 117 say the open pin's label shows (bold).
   - My judgment is that nothing important is lost. The numbered badges, wrench and wave glyphs, the panel's route list
     and the open card all name the same things. Get help and The Lighthouse are always labeled. Everything is labeled
     at 1000x625 and up. It is only thinner in the preview and on a phone.
   - Fix if wanted: give Mind Woods candidate spots in the gap between the two pin rows, and let the open pin's label
     try a few more spots. Otherwise, reword spec 23 and 117 to describe the priority-and-drop rule.
2. **Pin labels at 9.5 px in the 680x425 preview** (and 375, 800x500, 760x600): the fallback font is `fs - 1.5` with fs 11
   (for example "Ask early" and "Good friends" at 680x425). Spec line 124 asks for 10 px or more in the preview.
3. **The route path still crosses dimmed non-route pins**, now that it bends around Get help. Examples: Tomás "can't"
   passes through Easy on caffeine, Rethink a thought and Notice good at every size (frame tomas-cant-1366), and Dev
   "can't" through Move more and Easy on caffeine. The numbered badges make the real stops clear, so this is cosmetic.
4. **680x425 with a situation picked:** Tomás and Grace are still partly under the sticky situation bar until they get
   focus (then they scroll clear). Same as last round's nit 4.
5. **375x667, Stress in the body:** the burst switch is below the fold under the figure. Same as last round's nit 5.
6. **Carried over:** voice/local.json still lists the old "Tap chips" line and voice/raw/6d8c00d82fd0.pcm is still
   there. Neither reaches the bundle.
