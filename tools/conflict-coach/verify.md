Verdict: FIX (1 blocker, 6 should-fix, 7 nits)

Cold verify of the draft bundle (`CURIO_DRAFT=1 python scripts/bundle_tool.py conflict-coach`, 94 KB), 2026-10-26.
Muted headless Chrome over CDP on a private port, real held clicks and keys, a `speechSynthesis` logger for the voice
queue. Art and voice are not generated yet (placeholder discs on the stage, browser TTS); not counted as defects.

## What passed (checked, not assumed)

- Done when 1: all 320 paths (5 scenes x 4 x 4 x 4 picks) driven in the page; every meter value matched my own
  recomputation (start Tense, clamp 0..4), every ending card matched the final stop, every turn showed four
  full-sentence cards. All scene text, replies, endings, hidden reasons and tiles match spec.md word for word
  (only the Partner Cards "Both sides" speaker reasons, `why`, are builder-written; they read fine).
- Done when 2: Rewind on turns 1, 2 and 3 (and from the ending) restores the meter (`before[T]`) and the posture,
  shows the dashed "Last time" bubble and ghost marker, and allows a new pick.
- Done when 3: three strong moves give "Clean run" on stage, clipboard and card check; still Clean after two rewinds
  that ended on strong moves; check survives reload; Clear checks removes it and the key.
- Done when 4: every trap in every scene is caught with its row's explanation; 0 traps open reply, 1 trap guarded,
  2 traps defensive; Say it to them disabled with 0 and with 3 slots filled; empty slots marked "Pick one".
- Done when 5: Swap roles flips (0.5 s flip with Motion on, none with Motion off), Show both sides toggles, Print
  calls `window.print()` and also builds on `beforeprint` (Ctrl+P after a scene change printed the new scene).
  Print PDF: two black-on-white cards, no header, clean.
- Done when 6: no input, textarea, select or contenteditable. localStorage after a full session holds only
  `curio-motion` and `curio-conflict-coach-clean` (`["slides"]`, removed when empty). Zero network requests.
- Done when 7: five postures differ (head turn, brows, mouth, arms); every stop has a word and an icon.
- Done when 10: first held tap on a scene card plays its own hint and skips the welcome unmarked; first tap on a
  mode tab plays that welcome; first tap Read speaks the welcome and marks it said; mode switch mid-line cancels
  and plays the new welcome; Sound off uses nothing, Sound on queues the never-said welcome; Read during a coach
  line cuts it and reads hint plus coach; pick, Rewind, pick replays the coach line; ending plus Clean run lines
  play in order.
- Motion off (stored, and from OS `prefers-reduced-motion` with no stored key): meter jumps, face is instant,
  bubbles do not rise, no card flip.
- No horizontal scroll at any size (680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 760x1000,
  375x812 and 375x667 in an iframe host). No console errors or exceptions in any run.
- No em dashes in src, notes, tool.draft.json, lines.json, prompts.json; "Curio Class" never shortened.
- voice/lines.json matches `allLines()` exactly (25 lines, longest 109 chars); `big-sister` has a ref.wav and no
  other tool uses it.
- SEL rules: fictional ordinary scenes, nothing asks for disclosure, no text box, no score on feelings (moves are
  named, the meter is the talk), notes.md names the school counselor, characters drawn in code with varied skin
  tones, no people in art prompts.
- Contrast, recomputed: every pair in the spec's Look section matches (white on brand 5.47, brand on paper 5.20,
  ink on paper 15.12, muted on paper 6.01, ink on your bubble 13.40, Heated 7.07, Listening 6.84, Working 6.39,
  Tense on paper 5.63). Focus ring on panel and stage: 6.84 on white, 6.50 on paper, 5.44 on #f3e3cf.

## Blocker

1. **Focus is not visible on the header controls (Done when 8).** `--focus #1f5f8b` against the header: 1.25:1 on
   `--brand #b3471d`, 1.02:1 on `--btn #9a3b16` (WCAG 1.4.11 needs 3:1). Worse, on the three mode tabs the ring is
   clipped by the kit's `.seg{overflow:hidden}`: Tab to "Line Builder" and only a 4 px blue sliver shows at its left
   edge, nothing else changes. Repro: 1366x768, press Tab twice, look at the header (frames focus-1, focus-3).
   Fix (tool CSS only, no kit change): `header :focus-visible{outline-color:#fff}` (white on brand 5.47, on btn
   6.97) and `.seg button:focus-visible{outline:3px solid #fff;outline-offset:-6px;box-shadow:inset 0 0 0 2px #26211f}`
   so the inset ring reads on both the brown tabs and the yellow pressed tab.

## Should fix

2. **Keyboard focus is dropped to `<body>` after every Scenes action.** Tab to a move card, press Enter: focus is on
   `body` 0.3 s later (`renderScenesPanel()` replaces the move buttons in `pick()` and again at stage 3). Enter on
   Rewind or Next: also `body`, because the button hides itself before the `setTimeout` in `rewind()`/`next()`
   checks `document.activeElement.id`, so that hand-off code never runs. Keyboard users lose the ring and must
   re-find their place (Chrome resumes near the old node, but nothing is shown focused). Fix: remember the action
   before re-rendering (`const wasKey = document.activeElement`), then after render focus by role: after a pick,
   the picked card (or `#next` once stage 3 shows it); after Rewind, the first move card; after Next, the first move
   card; at the ending, `#nextScene`. The 1 to 4 / A to D keys already refocus; the Enter path does not.
3. **"Could we [4]?" breaks on several ask tiles (builder's flag confirmed), and the demand traps stop reading as
   demands inside "Could we".** Read in the frame: "Could we ask me first?", "Could we include me next time?",
   "Could we text me about plans?", "Could we let me do everything?", "Could we always ask me first?", "Could we
   never touch them again?", "Could we check before you share?"; and the Slides trap "Could we do it right now?"
   sounds like a polite ask, so "That's a demand" is a hard sell. Keep the frame (it matches the Scenes I-statements
   and the Partner Card) and reword tiles (spec Content change, same for the bubble since it uses `lbSentence`):
   - The Markers: `ask me first` -> `ask before borrowing`; `put the caps back on` -> `both put the caps back on`;
     T `never touch them again` -> `agree you never touch them again`.
   - The Tryout: `check before you share` -> `check before sharing`; T `never tell anyone anything` ->
     `agree you never tell anyone anything`.
   - The Lab Controls: T `let me do everything` -> `agree I do every step from now on`.
   - The Weekend Plan: `include me next time` -> `all go together next time`; `text me about plans` ->
     `start a group chat for plans`; T `always ask me first` -> `agree you always ask me first`.
   - The Slides: T `do it right now` -> `agree you finish them all tonight`.
   The "agree you..." traps read as orders dressed as questions, which fits the explanation "Ask for something you
   could both agree to." Good asks for Slides (`make a plan today`, `split the slides`, `work on it after school`)
   and Lab (`switch jobs halfway`, `take turns each lab`, `run it together`) already read well.
4. **Two tiles contradict their row's coach rule.** Weekend feeling trap `that you don't like me` gets the
   explanation "Feel like you... is a thought about them", which no longer matches the words on the tile; change the
   tile to `like you don't want me around`. Weekend because-row good tile `you're my friends` starts with "you" and
   is marked "About you" while the row's trap rule says "That's about them. Say why it matters to you"; change it to
   `our friendship matters to me`.
5. **The "Last time" bubble text is hard to read.** The whole bubble is at `opacity:.55`, so its text drops to about
   3.5:1 (computed: #827970 on #f4e8d6) and the bench planks show straight through the words (frames
   rewound-repick-1366 and rw-1920x1080: a plank line crosses "You always hog everything"). This side by side is the
   point of the tool and it is read on projectors. Fix: keep the faded look on the box only: `.bub.last{opacity:1;
   background:#fbf3e8;border:2px dashed #8a6d4f}` and `.bub.last` text in `--muted` (#6b5d55 on #fbf3e8 is about
   5.8:1), label "Last time" in ink.
6. **760 wide: no move card is visible without scrolling.** 760x900 Scenes turn 1: the stage is about 600 px tall,
   the picker chips follow, and the first card starts at y 885 (all four below the fold); at 760x1000 cards C and D
   and Rewind/Next are below. STANDARDS says the main controls are visible without scrolling at every size. Fix: in
   `relayout()` for `stack`, size the stage to the space left after the header and about 260 px of panel (for
   example `clamp(innerHeight - headerH - 300, 320, w * .95)`), or move `#scenesSec` above the picker chips in stack.
   375 wide works (scrolls), acceptable for phones.
7. **Partner Cards at the 680x425 preview: text drops to 8.8 px and "Show both sides" opens below the fold.** The
   fit loop shrinks to 11 px and the `.lab`/`.who` labels (0.8 em) end at about 9 px; the Both sides box sits 81 px
   below the stage bottom and needs an inner scroll. Fix: in compact Partner mode show the Both sides text in the
   panel under the buttons (there is room) instead of under the cards, and floor labels at 11 px.

## Nits

8. The meter marker's pointer triangle sits on the active stop's icon, so the icon you most need (flame at Heated,
   ear at Listening, hands at Working it out) is half covered; the dashed ghost does the same. Draw the marker on the
   bar only (drop the triangle or point it up from below the bar).
9. Line Builder frame has a space before the punctuation: "...for people to know . Could we" and "anything ?"
   (inline slot margins). Wrap each slot with its following punctuation in a `white-space:nowrap` span and drop the
   right margin.
10. Heated and Tense postures differ mainly in the head; both have the same crossed arms and a small lean
    difference, hard to tell apart at 680x425. Lean Heated further back (lean 7 -> 12) and turn the body more.
11. Partner Cards "Both sides" box uses second person for the Listener ("Listener (Jordan): Your house is
    crowded..."), confusing when both partners read it. Third person: "Jordan: their house was crowded and loud this
    week, and they were embarrassed to say so."
12. Partner Cards: the Listener's "Only you know this" reason sits beside the Speaker card on the same screen, so
    on one shared laptop the Speaker sees it too. Consider covering it until tapped (a "Listener, tap to see your
    secret" face-down card). Spec question for Cory, not a build error.
13. Shared reply "See, this is why I didn't say anything." fits four scenes but not The Tryout, where Mateo did say
    something. A generic alternative that fits all five: "See, you're not even listening."
14. Copy polish: Lab reflective listen has a double "so" ("So you're nervous about our grade, so you want..."): use
    "...our grade, and you want to make sure the steps are right." Line Builder when-tiles mix tenses after "I feel"
    ("when other kids asked", "when I heard about the movie after"); present tense reads better ("when kids ask about
    the tryout", "when I hear about plans after"). At 1280x720 and 1366x768 the picker's welcome hint is just below
    the panel fold (panel 711 px for 640/688 px); harmless.

Copy and tone otherwise good: plain sentences at about a grade 3 to 5 reading level (Flesch-Kincaid estimate on
the narration about 1.5, short setups), warm, never preachy, "usually" and "easier to hear" kept as the spec
requires.

## Re-verify

Verdict: FIX (0 blockers, 4 should-fix, 5 nits)

Cold re-verify, 2026-10-26, of the rebuilt draft (`CURIO_DRAFT=1 python scripts/bundle_tool.py conflict-coach`, 946 KB,
under 2 MB; five real webp backdrops and 25 real mp3 clips inlined, no placeholders). Muted headless Chrome over CDP on
private port 9733 (real held clicks and keys), iframe host on 9031 for 375 wide. Everything started was closed.

### Earlier findings, re-checked

- 1 (blocker, header focus): fixed. White 3 px ring on header buttons (6.97:1 on btn), inset white plus ink ring on the
  three tabs, fully visible on all six header controls.
- 2 (focus to body in Scenes): fixed. Enter on a move card focuses the picked card, then Next at stage 3; Enter on
  Rewind, Next, end Rewind and Replay lands on the first move card; the ending lands on Next scene; Pick a scene lands
  on the first scene card; the 1-4 / A-D / R / N keys keep focus. (New focus drops in Line Builder: see 3 below.)
- 3 (Could we tiles): fixed. All 80 tiles read in the frame across the five scenes; every good line is grammatical and
  every "agree you..." trap reads as an order. Tiles match the updated spec word for word.
- 4 (contradicting tiles): fixed (`like you don't want me around`, `our friendship matters to me`).
- 5 (Last time bubble): fixed. Opaque box, dashed border, text 5.75:1, label in ink 14.46:1; no planks through text.
- 6 (760 wide fold): fixed. 760x900 and 760x1000 show all four move cards, and Rewind/Next after a pick, without
  scrolling.
- 7 (Partner Cards in the preview): fixed. At 680x425 to 1000x625, Show both sides goes in the panel under the buttons
  and is fully visible; labels floor at 11 px.
- 8 (meter marker over icons): fixed. The marker and the dashed ghost sit on the bar, icons clear.
- 9 (space before punctuation): fixed. The period and question mark sit inside slots 3 and 4.
- 10 (Heated vs Tense): fixed. The five postures differ clearly (arms crossed and leaning back, hands gripped in the
  lap, hands on knees, head tilt, open hand), checked for Jordan and Sam. But see should-fix 1: the bigger lean clips.
- 11 (Both sides person): fixed, third person now. Tense mix: see nit 7.
- 12 (Listener secret on a shared screen): still open on purpose, for Cory.
- 13 (shared reply): fixed ("See, you're not even listening.").
- 14 (copy polish): fixed (Lab reflect has no double "so"; when-tiles are present tense; the picker hint now sits above
  the cards and is in view at 1280x720 and 1366x768).

### Regression checks that passed

- Done when 1: all 320 paths (5 scenes x 4 x 4 x 4) match my own meter recomputation (start Tense, clamp 0..4), every
  ending matches the final stop, every turn shows four full-sentence cards.
- Done when 2 and 3: Rewind restores meter and posture, shows the Last time bubble and ghost; Clean run still counts
  after rewinds (a demand, then a rewind to ask what works, gave Clean); the check survives reload; Clear checks
  removes it and the key.
- Done when 4: in every scene each trap gets its own explanation; 0, 1 and 2+ traps get the open, guarded and defensive
  replies; Say it to them is disabled with 0 to 3 slots filled.
- Done when 5: Swap flips (no flip with Motion off), Show both sides toggles, Print calls `window.print()` once and
  `beforeprint` rebuilds for the current scene; the PDF is two clean black-on-white cards, no header.
- Done when 6: no input, textarea, select or contenteditable; localStorage holds only `curio-motion` and
  `curio-conflict-coach-clean`. Zero network requests, zero console errors or exceptions in every run.
- Done when 7 and 8: postures distinct, every stop has a word and icon; every control reachable by Tab with a visible
  ring (except the drops in should-fix 3).
- Done when 9: cards and Rewind/Next in view at 1366x768, 1280x720, 800x500 (and 680x425, 1000x625, 1920x1080);
  no horizontal scroll at any size, including 375x812 and 375x667 in the iframe host.
- Done when 10, with the real clips and held clicks: a first tap on a scene card plays only its own hint and leaves the
  welcome unmarked; a first tap on Line Builder plays its welcome; a first Read reads the welcome and marks it said; a
  mode switch cuts the playing welcome and starts the new one at once; Sound off plays nothing and Sound on queues the
  unsaid welcome; Read cuts a coach line and reads hint plus coach; a line triggered during Read waits for it; Read then
  a mode switch starts the new welcome within 25 ms (hush resolves Read); pick then Rewind drops the coach line for the
  rewind hint; the ending and Clean run clips play in order. All 25 lines map to a clip; clip lengths look sane (12 to
  21 characters a second, none truncated). Not listened to for pronunciation.
- Motion off (stored "calm", OS reduced motion with no key, and the Motion button): meter jumps, face is instant,
  bubbles do not move, no card flip; Motion on animates.
- Backdrops: all five are empty rooms, no people, faces, hands or animals. Under the 0.32 paper overlay they sit well
  behind the code-drawn bench and kids, and bubbles stay readable on the busy courtyard brick.
- No em dashes in any tool file; "Curio Class" never shortened; copy reads at a grade 6-8 level or below.

### Should fix

1. **Heated posture pushes the kid off the right edge of the stage (regression from nit 10's bigger lean).** At every
   size the kid extends 10 to 29 px past the stage edge in Heated (Mateo's curls worst): at 1366x768 the face and hair
   are cut at the edge, at 760x900 the back of the head is gone. Same in Line Builder with 2+ traps. Repro: any scene,
   turn 1, pick the blame card. Measured as the `#kidG` box against `#stage`: 680x425 +10 to 17, 1366x768 +18 to 29,
   760x900 +5 to 12. Fix: in `drawStage()` leave more room on the right, for example `kidX = W - pad - 90 * k` (or
   lean Heated about a point further left), then re-check that bubbles still clear the kid.
2. **The reply bubble is hidden under the "Last time" bubble in small boxes.** After a rewind and a new pick,
   `fitColumn()` runs out of room at 11 px and stacks the boxes on top of each other. 680x425 (the preview), The
   Markers and The Tryout turn 1: 10 px overlap, the last line of Priya's reply ("...ask the teacher again.") is
   covered. 375 wide: 13 to 59 px in every scene, Sam's whole second sentence is hidden. This is the compare moment the
   tool is built around. Fix: when `fitColumn()` returns false, drop the `who` line on the Last time bubble and move
   "Last time: <line>" into the panel under the coach box, or in stack let the stage grow until the column fits.
3. **Keyboard focus drops to `<body>` in Line Builder.** (a) In the tabbed layout (680x425 to 1000x625, 1280x720, 760,
   375), Enter on a row tab (`1 Feeling` ... `4 Your ask`) rebuilds the tabs in `buildLB()` and focus goes to body.
   (b) Enter on a filled slot in the stage frame empties it, `drawStage()` replaces the slot buttons, and focus goes to
   body (any size). Repro: 1280x720, Line Builder, Tab to "3 Why it matters", Enter; or pick a tile, focus its slot,
   Enter. Fix: after `buildLB()` from a tab, focus `#rowTabs button[aria-pressed="true"]`; after emptying a slot, focus
   the same `.slot[data-slot=i]` in the new frame (or the first tile of that row).
4. **The Line Builder "Coach check" explanations are cut off by the stage bottom in the preview and narrow sizes.**
   The check card is placed under the frame and overflows the stage, so the per-trap sentences, the point of Check my
   line, cannot be read. Measured overflow: 680x425 one trap 2 to 41 px, four traps 131 to 204 px; 800x500 four traps
   8 to 74 px (only explanation 1 and half of 2 show); 760x900 and 760x1000 four traps 10 to 35 px; 375 wide up to
   253 px (the frame itself is clipped too). Repro: 800x500, Line Builder, The Tryout, pick the four trap tiles, Check
   my line. Fix: as with Both sides, in compact and stack put the Coach check text in the panel under the Check / Say /
   Clear buttons when it does not fit, and keep only the badges on the frame.

### Nits

5. 760 wide: the kid's name label sits right under the strip title, reading "The Tryout, with Mateo / Mateo" at the top
   right. Hide the strip title when the stage is under about 800 px wide, or skip the name label when the title shows.
6. Two-line slot tiles in the Line Builder frame get the frame's 2.05 line height ("agree you never tell anyone /
   anything?" has a wide gap at 800x500): `.slot{... font:inherit}` resets the `line-height:1.2` set earlier in the
   same rule. Put `line-height:1.2` after `font:inherit`.
7. Both sides tense and wording: The Slides mixes "The Speaker wants..." with "Jordan's house was crowded and loud this
   week, and they were embarrassed" (try "is crowded ... they're embarrassed"). The Weekend Plan's "The Speaker likes
   hanging out with them" has no clear "them", and the reason starts "There wasn't room" instead of with Sam's name
   like the other four (try "...likes hanging out with Sam's group, and heard about the movie after. Sam's mom only had
   room for three, and Sam felt bad but didn't know how to say it.").
8. Line Builder copy: "Could we ask before borrowing?" (The Markers) reads oddly, since only Priya borrows; "agree to
   ask before borrowing" fits the frame. "I feel surprised when kids bring it up in class because I wanted to tell
   people myself" has a past tense in the present frame ("I want to tell people myself").
9. Backdrops: a few faint fake-text scribbles remain (classroom notice board, hallway door papers, courtyard notices).
   Small and soft under the overlay; flag for Cory's art review (prompts.json "review": "pending").

Also noted, outside this tool's checks: there is no `plan.md` yet (TOOL-CONTRACT says one is expected for every tool).

## Re-verify 2

Verdict: FIX (0 blockers, 1 should-fix, 1 nit)

Cold re-verify, 2026-10-26, of fix round 2 (`CURIO_DRAFT=1 python scripts/bundle_tool.py conflict-coach`, 948 KB, under
2 MB). Muted headless Chrome over CDP on private port 9881 (real held clicks and real keys), an iframe host on 9131 for
375 wide (375x812 and 375x667). Every Chrome and server I started was closed. Nit 9 (backdrop scribbles) and original
nit 12 (Listener secret) left for Cory, as agreed.

### Round 2 items, re-checked

- Should-fix 1 (Heated kid cut off): fixed. `#kidG` against `#stage` for all five kids, Heated, Listening and Working it
  out, in Scenes and in Line Builder with 2+ traps: the kid now sits 9 to 26 px inside the right edge at every size
  (Mateo's curls the closest, 9 px at 680x425 and 800x500), no other edge crossed. By eye at 680x425, 1000x625,
  1366x768 and 760x900: head and hair whole.
- Should-fix 2 (reply under Last time): fixed. All 240 rewind cases per size (5 scenes x 3 turns x 4 first picks x 4
  second picks) at all eight sizes plus 375x812 and 375x667: zero overlaps between bubbles and captions, nothing past
  the stage, smallest bubble text 11 px. When the column does not fit (31 cases at 680x425, about 175 at 375) the Last
  time line moves to the panel; at 680x425 it shows under Rewind and Next, in view (frame last-680x425).
- Should-fix 3 (Line Builder focus to body): fixed. Real Enter at 680x425, 760x900, 1280x720, 1366x768 and 1920x1080 on
  each row tab, each tile (tabbed and untabbed), filled and empty slots, Check, Say, Clear and the scene chips: focus
  always lands on a visible control with `:focus-visible`, never on body.
- Should-fix 4 (Coach check clipped): the text no longer overflows the stage (405 tile combinations per size, every
  size, nothing past the stage edge), but the move to the panel does not work. See the should-fix below.
- Nit 5 (760 name label): fixed. The strip title is hidden under 800 px; at 760x900 and 760x1000 only the kid's name
  shows, above the hair, clear of everything (frames heat-760x900, last-760x1000, say-760x900).
- Nit 6 (two-line slot gap): fixed. "agree you never tell anyone / anything?" now has normal line spacing at 800x500.
- Nit 7 (Both sides wording): fixed. The Slides is present tense throughout; The Weekend Plan names "Sam's group" and
  starts the reason with "Sam's mom".
- Nit 8 (Line Builder copy): fixed. "agree to ask before borrowing" and "I want to tell people myself", in src and spec.

### Should fix

1. **The Coach check box escapes the panel, and in the 16:10 preview it makes the whole page scroll.** `#checkPanel` has
   the classes `cap capp`, and `.cap{position:absolute}` (src.html line 160) comes after `.capp{position:static}`
   (line 131) with the same specificity, so the box is absolutely positioned at its static spot and hangs out of the
   panel. The panel's own scroll never sees it (panel scrollHeight 369 = clientHeight 369 at 680x425); instead the
   document grows. 680x425, The Tryout, four traps, Check my line: only "Coach check" and the first line show, the box
   ends 185 px below the window, and a wheel over the panel scrolls the whole page 185 px: the header and meter leave
   the top, the stage is cut and blank paper fills under it (frames lb4-680x425, wheel-680). The document grows for 0,
   1 and 4 traps at 680x425 (9, 46, 185 px) and for 4 traps at 800x500 (110 px). At 760 wide the box also ignores the
   panel padding (16 px to the window edge at 760x900 with four traps, shrink-wrapped to 560 px in the Say state).
   Repro: 680x425 or 800x500, Line Builder, The Tryout, pick the four trap tiles, Check my line, scroll over the panel.
   Fix (CSS only): `#checkPanel{position:static}` (or `.cap.capp{position:static}`), then the compact panel scrolls
   inside itself; consider `checkPanel.scrollIntoView({block:'nearest'})` after Check so the first explanation is in view.

### Nit

2. At 375 wide the Last time box sits in the panel under Rewind and Next, below the fold (frame last-375x812), so on a
   phone the compare needs a scroll. Acceptable for phones; only if it is cheap, put it right under the hint.

### Regression sweep that passed

- Done when 1: all 320 paths match my own meter recomputation (start Tense, clamp 0..4), posture equals the stop, each
  ending card matches the final stop, every turn shows four full-sentence cards, Clean flag right on every path.
- Done when 2 and 3: Rewind on turn 2 put the meter back (2 to 3) and the posture, showed the Last time line and the
  dashed ghost, and allowed a new pick. Fresh storage: a blame then rewind to I-statement, reflect, demand then rewind
  to ask what works gave Clean run (end card, clipboard) and saved `["lab"]`; after a reload the Lab card reads "clean
  run done"; Clear checks removed the key and the check, focus on the first scene card.
- Done when 4: each trap in each scene gets its own explanation; 0, 1, 2+ traps give the open, guarded and defensive
  replies and postures 4, 1, 0; Say it to them is disabled with 0 to 3 slots and enabled at 4, in every scene.
- Done when 5: Swap flips (0.5 s with Motion on, none with Motion off), Show both sides toggles (in the panel at
  680x425, under the cards at 375), Print calls `window.print()` once; the PDF is two black-on-white cards for the
  current scene, no header.
- Done when 6: no input, textarea, select or contenteditable; localStorage holds only `curio-motion` and
  `curio-conflict-coach-clean`; zero network requests.
- Done when 7 and 8: postures distinct by eye; every stop has word and icon; full Tab order reaches every control
  with a visible ring; Enter on every Scenes control (move card, Rewind, Next, end Rewind, Replay, scene card) and
  keys 1, B, R, N keep focus on a visible control; Partner Cards buttons and mode tabs keep focus. Never body.
- Done when 9: all four cards before a pick, and Rewind and Next after it (also after a rewind), and the four end
  buttons, are in view at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 760x1000 (60 turns per
  size). No horizontal scroll in any mode at any size, 375 included. Outside the Line Builder check above, the compact
  layouts never scroll vertically.
- Done when 10, real clips, held clicks: first tap on a scene card plays only h-say, welcome unmarked; first tap on
  Line Builder plays its welcome, and Partner Cards 1.2 s later cuts it and starts its own within 20 ms; first tap Read
  reads the welcome and marks it said; Sound off cuts the clip and plays nothing on a mode switch, Sound on queues the
  unsaid builder welcome; Read during a coach line cuts it and reads hint then coach; a pick during Read waits for Read
  to end; Read then a mode switch starts the new welcome 6 ms after the cut; pick then Rewind cuts the coach line for
  h-rewind; a clean run plays each turn's hint and coach line, then "You worked it out." and the Clean run line in order.
  All 25 lines in `allLines()` match voice/lines.json and each maps to a real clip (none falls back to browser speech),
  12 to 20 characters a second, none cut short.
- Motion off from the OS setting with no key, from a stored "calm", and from the Motion button: marker jumps, no rising
  bubbles, no card flip; Motion on animates.
- Zero console errors, warnings or exceptions in every run.
- Copy: no em dashes in src, notes, spec, tool.draft.json, lines.json or prompts.json; "Curio Class" never shortened;
  the new wording reads at grade 6-8 or below.

Still outside this tool's checks: no `plan.md` yet.

## Integrator fix (after Re-verify 2)

The one should-fix (Coach check box escaping the panel) was a specificity clash: `.cap` came after `.capp`. Fixed with `.capp,.cap.capp{position:static}`. Checked in muted headless Chrome at 680x425 and 800x500 with four traps: the box is static inside the panel and the document no longer grows (scrollHeight equals the viewport). Fix rounds were used up, so no further re-verify.
