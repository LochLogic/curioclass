# Untangle: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: untangle (Recess)

#### Built

Built in `S:\CurioClass-codex`, writing only `tools/untangle/` and `_scratch/untangle/`.

One offline Recess game: 20 First Skies, the exact 550-sky ladder in 22 worlds, and a worker-generated daily.

Bundle: **4,720,996 bytes** (4.72 MB, 4.50 MiB), below 6 MB. Cover is separate.

No kit header, voice, classroom flow, accounts, network requests, commits, deployment, shelf edit or polish round.

The report was written last to honor the user's explicit stop condition. Rebuild instructions are in [handoff.md](handoff.md).

#### Rules check

| Edge case | Result | Evidence |
|---|---|---|
| Non-shared segments: 3/6 px gaps count; 8 px does not | PASS | `checks.json` isolated fixtures |
| Shared vertex: right angle and opposite rays clear; under 4 degrees and overlaps count | PASS | Angle/overlap fixtures |
| Star on an unrelated line, exact touches, near-touch rings | PASS | Geometry fixtures and live pointer play |
| Each trouble pair counted once; crowded stars add trouble | PASS | Independent Python evaluator |
| Zero while held waits; zero on release wins | PASS | Real held mouse test, `play/zero-held.png` |
| Clamp to 12 px; slide east first in 2 px steps and 24 directions; only dropped star moves | PASS | Unit fixtures and real neighbour drop |
| Four-pixel threshold; cancel/no-op free; Undo lowers count; Restart exact | PASS | Real mouse, Shift-arrow and Escape tests |
| Resize uses fractions and recounts without adding a move | PASS | Real held-pointer resize |
| Any valid layout wins, without checking the secret picture | PASS | Count-only win gate; 5,130 shape/mirror checks |
| Stacked stars, straight rows and tiny clusters cannot win | PASS | All 20 First Skies tested |

Evidence: [rules/data assertions](../../_scratch/untangle/checks.json), [independent Python](../../_scratch/untangle/independent-results.json), [live play](../../_scratch/untangle/play/results.json).

#### Puzzles and levels

Own relocation solver chooses free destinations before blocked ones and applies the actual slide rule. A separate Python implementation verifies clearance, connectivity and the crossing-free embedding, which constructively proves planarity.

All **1,140 required layouts** solve at or below pace; all **570 compact layouts** also solve at or below pace. Zero failures.

No exact minimum is stated in the spec, and none is invented here. The table records a verified solution length and the reachable three-star pace.

| Sky | Stars / lines | Stated / computed X | Pace | Computed moves, laptop / phone |
|---|---|---|---|---|
| L01 The Kite | 6 / 8 | 3 / 3 | 6 | 5 / 5 |
| L02 The Paper Plane | 6 / 8 | 4 / 4 | 6 | 6 / 6 |
| L03 The Crown | 7 / 9 | 4 / 4 | 7 | 4 / 6 |
| L04 The Fish | 8 / 11 | 5 / 5 | 8 | 8 / 8 |
| L05 The Sailboat | 9 / 13 | 7 / 7 | 9 | 5 / 8 |
| L06 The Bird | 9 / 13 | 8 / 8 | 9 | 9 / 8 |
| L07 The Turtle | 10 / 14 | 8 / 8 | 10 | 10 / 10 |
| L08 The Cat | 11 / 16 | 11 / 11 | 11 | 11 / 11 |
| L09 The Rocket | 11 / 16 | 11 / 11 | 11 | 10 / 10 |
| L10 The Owl | 12 / 18 | 12 / 12 | 12 | 12 / 12 |
| L11 The Fox | 12 / 18 | 14 / 14 | 12 | 12 / 11 |
| L12 The Lighthouse | 13 / 19 | 16 / 16 | 13 | 13 / 13 |
| L13 The Butterfly | 13 / 21 | 18 / 18 | 13 | 13 / 13 |
| L14 The Rabbit | 13 / 21 | 17 / 17 | 13 | 12 / 13 |
| L15 The Ship | 13 / 21 | 19 / 19 | 13 | 13 / 13 |
| L16 The Snail | 13 / 22 | 19 / 19 | 13 | 11 / 11 |
| L17 The Whale | 14 / 24 | 21 / 21 | 14 | 12 / 9 |
| L18 The Stag | 16 / 26 | 23 / 23 | 16 | 16 / 15 |
| L19 The Octopus | 16 / 28 | 27 / 27 | 16 | 16 / 16 |
| L20 The Dragon | 18 / 32 | 34 / 34 | 18 | 17 / 17 |

All 550 ladder records: expected X equals computed X, canonical and home trouble zero, starts tangled, connected, degree at least two, spacing checks pass, witness at most p moves, D never drops.

The packed table calls X true crossings, but its values include touching/overlapping non-shared pairs. That exact intersection interpretation matches all 550 records; runtime trouble still uses the specified pixel rules.

Both required SHA-256 checksums reproduced:

- Records: `677f292415a7264a81578f4d1cdb36e4d470aaf0a33cccb343d419fabd0e8884`.
- Generated levels: `2be9e60bcfc3865508214b4ac18040ad19fca26c4efadb0d83051e5945b65b49`.

Every stated/computed result: [1,140-row CSV](../../_scratch/untangle/solutions.csv), [compact solves](../../_scratch/untangle/compact-solutions.json), [final size/mirror checks](../../_scratch/untangle/additional-geometry-final.json).

Daily: 55 dates re-generated twice, 15 stars/24 lines, both field sizes solved within 15 moves, six beams; the known 2026-11-8 random draws match. Two separate Chrome instances agree on today's first three starts: `(500,80), (899.4,370.2), (917.7,543.9)`.

#### Computer opponent

Not applicable. Untangle has no opponent, computer ladder, losing state or pass-and-play mode in its spec. No artificial opponent was added.

#### Break it

PASS: 52 end-to-end live-input checks, 10 extra score/input checks, plus final painted-frame solves. Every First Sky and R001/R025/R162/R550 played through with real pointer events; the daily replay, keyboard-only Sky 1, touch, chart pages and overview also passed.

PASS: real two-star/one-star runs used 7/13 moves at pace 6; the better score and stars survived the worse replay. Initials save once; the shell caps its local board at ten entries.

PASS: small-drop abuse cannot accumulate free travel; Undo, Restart during a reveal, changing skies during a win timer, resizing mid-drag, daily replay, sound off and calm mode cannot mint a stale award.

A sub-4 px drop returns to its lift position. This resolves the spec's no-move wording without permitting an unlimited zero-move crawl.

During build, real play exposed stale SVG capture-loss events cancelling a fresh lift. Fixed by following the active pointer through release/cancel. Later complete play passed without exceptions.

The extra test initially assumed an eight-move best; live play legitimately found seven. The assertion was corrected to preserve the observed best and re-run. Both initial and final evidence remain in Scratch.

Largest-sky clearance evaluation measured about 0.5 ms per count in Chrome; real play remained responsive. Daily generation runs in a Web Worker.

The one mechanical audit completed: 102 raw leads, consisting of 40 overlapping SVG halo/hit bounds, 56 ARIA-only star labels mistaken for visible text, and six pointer-focus leads. No overflow, clipped-control, target-size, console, stuck-control or calm-animation blocker was reported.

The first 96 leads are expected for the specified nearest-star hit policy and invisible SVG/ARIA geometry. Pointer focus was fixed locally; a targeted real click returns focus to Star 1. No shared file was edited.

The 680x425 preview initially left 32 dense canonical reveals below pixel clearance. Its controls now form a compact side rail, giving the sky 484x401 actual pixels. All 570 witnesses and all nine final sizes now pass; laptop and phone layouts retain the specified arrangement.

Raw [audit](../../_scratch/untangle/audit/audit.md), [extra checks](../../_scratch/untangle/play/extra-results.json), [final evidence](../../_scratch/untangle/final-checks.json).

#### Look board

One direction was obvious from the world table: an indigo painterly nocturne with warm stars and luminous creature reveals. World art and three static 1366x768 hero frames were painted/assembled before game logic:

- [Opening](../../_scratch/untangle/look/opening.png).
- [In progress](../../_scratch/untangle/look/in-progress.png).
- [Best moment](../../_scratch/untangle/look/best-moment.png).

Kept this direction for its contrast between the quiet tangled sky and the bright earned reveal. During the build, all backdrops were repainted darker, glass-orb stars became warm light glints, the fox/stag became guide-shaped faces, and Far Galaxy became pure space. No asset exceeded three generations.

#### Grab check

Best moment: the last crossing disappears, threads turn gold, and the whale blooms. [Final real-play Whale](../../_scratch/untangle/play/L17-final-painted.png). [Far Galaxy finale](../../_scratch/untangle/play/R550-final-painted.png).

Flattest moment: the unlit opening sky. Its deliberately quiet landscape protects the thin threads; marching dashes, live rings, warm glints and held-star growth give the first action an immediate response.

The comparison shows a distinct game world beside the shared shell test bench and an existing classroom tool: [Untangle / shell demo / Beat Lab](../../_scratch/untangle/grab-comparison.png).

#### Class creep check

PASS: zero whole-word hits for standard, objective, learn, skill, lesson, correct answer or well done; zero standard-code hits in `src.html`. No voice assets or classroom kit imports. Adult context lives in `notes.md`.

#### Sources

- Puzzle source: the exact original project data in `spec.md`, 20 hand-made skies and 550 packed records. No third-party puzzle set, art, names or code used.
- Daily: original six-line generator implemented from the spec, using the shell daily random stream.
- Wikipedia Planarity and Fary's theorem: CC BY-SA 4.0 text, as recorded in the spec; background/history only, no text copied.
- Simon Tatham Untangle manual: MIT-style licence as recorded in the spec; mechanic reference only, no code/art/levels copied.
- Illustrations generated with OpenAI gpt-image, edited for Curio Class. Individual prompts, redraws and provenance are in `art/prompts.json` and Scratch's generation log.

#### Done when

| Spec item | Result / evidence |
|---|---|
| 1 Exact content and picture geometry | PASS: exact records/hashes, all First Skies data; painted cut-outs fit guide bounds |
| 2 Exact crossing/angle rules | PASS: isolated fixtures plus independent Python |
| 3 Win only on zero drop | PASS: real held-zero test |
| 4 No stack/row/tiny wins | PASS: all First Skies degenerate tests |
| 5 Dashes/rings in calm and grayscale | PASS: calm audit and grayscale frame |
| 6 Moves/Undo/Restart | PASS: live mouse and keyboard tests |
| 7 Move-based stars/readout | PASS: all pace witnesses and real 3/2/1-star runs |
| 8 Deterministic daily, six beams | PASS: 55 dates and two Chrome instances |
| 9 Required sizes, no scroll, chart fits | PASS: audit plus final 390x844 and compact frames |
| 10 Keyboard, Escape, C | PASS: actual key events solve Sky 1 |
| 11 Touch/finger halo/no scroll | PASS: real touch dispatch, one move, scroll zero, scale one |
| 12 Three children, ages 8 to 13 | FAIL / unavailable: unattended session; no human timing or enjoyment claim |
| 13 One offline file, at most 6 MB | PASS: 4,720,996 bytes; HTTP blocked during play; no requests |
| 14 All 550 records, graph checks, witness, monotone D | PASS: both hashes; all required and compact layouts |
| 15 Ladder labels, reveals, finale and Next transitions | PASS: real R001/R025/R162/R550 and both world transitions |
| 16 Paged chart, overview, keys and swipe | PASS: 23 pages and overview; keyboard navigation and real touch swipe |
| 17 Painted art, darkness and glints | PASS: 69 assets; 23 darkness checks; 230 measured glints within 0.88 px, below 12 px |
| 18 Cover 1200x750, no text | PASS: dimensions checked and image inspected |

#### Frames looked at

All three look-board frames; all 33 audit frames through three contact sheets; full laptop Whale and Far Galaxy finale; final compact opening/chart/dense sky, 390x844 phone, focus and daily frames; normal six-beam sweep and calm beams; grayscale; shell demo and Beat Lab; both reveal contact sheets, all backdrops and the cover.

[Audit contacts](../../_scratch/untangle/audit/contact-1.png), [contact 2](../../_scratch/untangle/audit/contact-2.png), [contact 3](../../_scratch/untangle/audit/contact-3.png), [final contacts](../../_scratch/untangle/final/contact.png), [grayscale](../../_scratch/untangle/play/grayscale.png).

#### Art made

69 WebP assets: 23 backdrops at 1600x1000, 20 First Skies paintings and 22 world paintings at 640x640, three 128x128 transparent light sprites, and a 1200x750 cover. Raw generated originals and prompts are preserved.

True-alpha cut-outs were resized and placed without chroma-keying or destructive trimming of their coordinate canvas. Painted light sprites register every First Skies guide point. Largest measured glint error is 0.88 px at 1366x768.

Every backdrop passes the connected bright-region test after the permitted 40% #0a0b26 veil. Relative-luminance and palette evidence: [art checks](../../_scratch/untangle/art-checks.json), [glints](../../_scratch/untangle/glint-registration.json), [contrast](../../_scratch/untangle/contrast.json).

#### Shell changes wanted

Do not edit the kit in this build. The shell header's literal script/link examples break naive bundling; the local adapter removes only that header comment from the embedded shell. Local styles provide 44 px initials arrows and a phone toolbar that fits. Exact changes wanted are in `handoff.md`.

#### Left open

The three-child playtest and its 30 to 90 second medians remain unverified. No humans were available and nobody was contacted. Visual acceptance remains the owner's decision; the look board and final real-play frames make it reviewable.

All started Chrome processes and the 8795 test server were closed. No commits or polish round were started.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: untangle

#### Played
- Cold play preceded the builder's report, handoff and notes. Adult reviewer using a Grade 3 solo-player lens, then an adult planning lens; no actual child playtest is claimed.
- First fresh standard bundle was unplayable. After the local bundling repair, solved Sky 1 visually in two moves, completed R001, and explored the daily with Undo and Restart before reading builder commentary.
- Then played all 20 First Skies, R001/R025/R162/R550 and the daily to zero with real pointer input. Keyboard-only Sky 1: two moves, three stars. The luminous Kite/Whale reveal is the strongest moment.
- Judged against CODEX-RECESS.md, GAMES.md and the complete spec. Computer opponents, opponent levels, pass-and-play and losing states are not part of Untangle.

#### Findings fixed
- **Blocker, general, bundling:** standard `bundle_tool.py` exposed shell JavaScript and threw `Recess is not defined`. Replaced the dangerous script/link example comment in a tool-local shared-shell snapshot; standard bundling now works without a Scratch postprocessor. Executable shell code is unchanged; kit/scripts untouched.
- **Blocker, family:untangle, Undo during a winning slide:** real near-simultaneous drop/U produced `solved=true`, two actual troubles and a move erased. Settle the pending slide before popping history, then re-check solved. Same attack now retains the valid six-move, zero-trouble result.
- **Should fix, family:untangle, resize during reveal:** resizing in the glide cancelled it before bloom, leaving the earned picture invisible. Centralized reveal landing/settling, preserved daily beams, and ignored unrelated shell repaints in the motion callback. Re-test: bloom present, picture opacity .86, zero trouble.
- **Should fix, general, keyboard:** saving initials removed the focused control; Next then lost the new sky's focus. Save now focuses Next after the click completes, and replacing a focused sky restores focus on its first star. Tool-local adapters also name the shell cards and contain Tab within the modal.
- **Should fix, general, notes:** `notes.md` contained only whitespace. Restored the spec's game-specific grown-up explanation, family activities, controls, move-based stars, invented-picture context and device-only privacy. Difficulty is described as a prediction, not a guarantee about each player's moves.
- **Polish, family:untangle, quiet improvement:** a useful drop could feel like a changed number. Added one short warm geometric halo when crossings fall. Calm has no pulse. Kept the existing paintings, palette, sound layer and generous star hit areas.
- **Should fix, general, overview at 1000x625:** the Worlds Back button was clipped despite a clean mechanical fold check. Reserved more header/footer height in the desktop tile formula; kept phone/short-landscape layouts. Targeted screenshot and bounds check: PASS, all 23 tiles and the full 44 px Back button visible; Back ends at y=591.5 inside the dialog ending at y=604.5, with no scrolling (`../../_scratch/untangle/review-overview/`)..

#### Findings left
- **Validation gap:** spec Done when 12 requires three children aged 8 to 13 and timing/stall observations. Unavailable unattended; adult role-play and automated solutions do not establish it.
- Shared shell/bundler fixes remain requested in `handoff.md`; local workarounds make this tool reviewable without editing shared files.

#### Break it
- **Win gate:** live zero while held remained unsolved; release solved. Each non-shared pair is counted once; 3/6 px gaps count, 8 px does not; shared right/opposite rays clear, narrow angles and overlaps count. Edge clamp and east-first slide checked.
- **Degenerate wins:** stacked stars, straight rows, half-pixel zigzags and tiny clusters all remain troubled on every First Sky. Mirrored valid layouts pass on all 570 skies. These are scripted geometry tests, alongside the real-input paths above.
- **Moves:** eight repeated sub-4 px drops left positions unchanged and moves zero. Rapid Undo stopped at zero; Escape cancelled a lift; resize while held cancelled safely, and release added no move. Winning-slide Undo exploit is closed.
- **Stars/best:** real 2-, 7- and 13-move solves earned 3/2/1 stars; poorer replays preserved the two-move best and three earned stars. Undo exploration and replaying a known sky are expressly allowed by the spec.
- **Initials:** repeated Enter after Save created one entry in that attempt. The fixed Save/Next path stays keyboard-operable. The unchanged shell sorts and caps its local board at ten.
- **Daily:** five independently regenerated dates have 15 stars, 24 lines, six beams and reachable pace-15 witnesses. Two Chrome instances matched today's first three starts. Real daily solve used 14 moves and displayed six beams.
- **Input/access:** real phone touch at 375/390 px gave one move, no page scroll and zoom 1; chart swipes wrapped World 22 to First Skies. All 23 world tiles and 25 sky tiles fit. A 9,999-star total still fits the 375 px toolbar.
- **Motion/sound/offline:** verified Calm has zero running infinite animations; dashed/ringed trouble remains readable in grayscale. Muting stopped active notes; chime calls while muted created none. Game resource checks found no HTTP requests or runtime exceptions.
- Evidence: `../../_scratch/untangle/review-browser/{pre,post}-results.json`, `review-scenes/focus-results.json`, `review-scenes/measurements-record.json` and their frames. The first scenes batch's `calm-loops` row accidentally toggled Motion on; the explicit `calm-loops-verified` row and final audit supersede that test setup.

#### Voice walk
- None, as required for Recess. Followed the visual instruction, drag/drop, Undo, Restart, chart, daily, solve, initials and Next. No narration, classroom header, Read flow or lesson cards were added. ARIA lift/count announcements remain.

#### Facts checked
- Exact First Skies JSON matches the spec. Both ladder SHA-256 checksums reproduced; every recorded intersection count, connected graph, degree bound, start spacing and non-decreasing model D passed.
- All 570 skies re-solved at or below their stated pace on 1300x620, 366x690 and compact 484x401 fields; canonical and mirrored arrangements have zero trouble. No exact minimum is claimed by the spec or this review.
- Counts, clearance thresholds, score tiers, world/page structure and daily sizes checked against the spec's Rules, Content and Modes sections with 11,467 assertions and no failures: `../../_scratch/untangle/review-validation.json` and `review_validate.js`.
- No health, safety, historical or cultural factual claims were introduced. The graph statement is backed constructively by each verified crossing-free drawing. Source/licence declarations retain the original project data and generated-art provenance.
- Class creep: zero specified lesson-word hits or standard codes in `src.html`; no em dashes.
- Text/quiet text contrast against the lightest allowed sky: 13.44:1 and 7.71:1. Line colours exceed 6.5:1, with dashes/rings supplying the non-colour signal: `../../_scratch/untangle/review-contrast.json`.

#### Sensitivity
- None requiring cultural review: invented constellations, fantasy creatures and landscapes, with no people, traditional sky stories, real constellation claims, religion, bodies or hard history. Notes state that the pictures are invented.

#### Flattest moment left
- Deliberation on a dense late sky is necessarily quiet; the live dashes/rings carry it. The improved-drop halo lifts the small payoff without distracting from planning. Kept the rich painted Whale and world-finale rewards.

#### Graphics
- Inspected all 69 existing assets: 23 landscapes, 42 reveals, three painted star sprites and the 1200x750 text-free cover. No painting needed replacing; geometry alone remains code-drawn.
- All 23 backdrops pass the connected bright-region test with the permitted 40% veil. All 230 painted glints fall within 1.10 px of the target star positions, below 12 px: `../../_scratch/untangle/review-scenes/art-checks.json`.
- Opened the art contact sheets; full Whale, R025/R162/R550 and daily frames; before/after race and resize frames; phone opening/held/chart/overview/stress frames; keyboard win, grayscale, shell demo and Beat Lab comparison. Untangle reads as its own world.
- Final bundle: 4,723,605 bytes (4.72 MB), below the 6 MB Recess limit. Cover remains separate.

#### Audit
- One complete final audit: `../../_scratch/untangle/review-audit/audit.md`, Chrome 9961, host 8765, 40-minute limit. Its 108 leads were 52 expected SVG halo/hit overlaps, 55 ARIA-only labels mistaken for visible text, and one broken review win-card fixture (missing return in drag bodies).
- Corrected the fixture and re-shot only that state at 1366x768/375x812: solved in two moves, named modal, forward/reverse Tab contained, all controls at least 44 px, Save to Next to new-star focus passes, no exceptions: `../../_scratch/untangle/review-win-state/results.json`.
- Inspected all 35 audit frames. No target, console, Calm or stuck-control fault was confirmed. Visual inspection additionally caught the clipped Worlds Back button at 1000x625; fixed and re-shot that overview only. No second full audit or polish round.

#### Left open
- Three-child playtest remains unverified. No outside contact, submission, deployment or shelf edit occurred.
- Ran from `S:\CurioClass-codex`; wrote only `tools/untangle/` and `_scratch/untangle/`; no commits. Bundle/browser/audit command limits were 120/300/2400 s. All started Chrome/server processes closed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Untangle build handoff

Build only. No commits, deployment, shelf edits, or polish round.

`src.html` is the canonical readable source. `untangle.html` is the generated, offline game.
The game uses the shared Recess stylesheet and a tool-local snapshot of the shared Recess script; it has no classroom header, voice, lesson cards or standards UI.
All 20 First Skies and the exact 550-record ladder are embedded, with a worker-generated daily sky.

#### Rebuild

Run from `S:\CurioClass-codex`:

```powershell
$env:CURIO_DRAFT=1
python _scratch/untangle/review_run.py 120 python scripts/bundle_tool.py untangle
```

The standard shared bundler now works directly. `lib/recess.min.js` is a readable snapshot of `kit/recess.js`,
with only its header's inline script/link example comment replaced. The original header both closes the inline
script and triggers stylesheet substitution. No executable shell code was changed. The source uses `lib:recess`
so this workaround survives bundling and does not depend on a Scratch-only postprocessor. Do not overwrite it
with an unsanitized copy. No shared kit or bundler file was edited.

The older Scratch `bundle.py` adapter is build history; do not use it for the reviewed source.

`_scratch/untangle/assemble.py` was the build-time assembler. It refreshes script sections from the build-time
Scratch modules, so do not use it after editing the canonical source unless those modules are synchronized.

#### Evidence

- `../../_scratch/untangle/checks.json`: 1,799 assertions, both required hashes, all 1,140 required layouts.
- `../../_scratch/untangle/solutions.csv`: every stated crossing count, computed count, pace and witness move count.
- `../../_scratch/untangle/independent-results.json`: separate Python geometry and constructive planarity checks.
- `../../_scratch/untangle/compact-checks.json`: all 570 skies solved in the 680x425 preview's 484x401 field.
- `../../_scratch/untangle/additional-geometry-final.json`: 5,130 shape/mirror checks at nine final field sizes.
- `../../_scratch/untangle/daily-checks.json`: 55 dates, deterministic generation, both required field sizes.
- `../../_scratch/untangle/play/results.json`: real pointer, keyboard, touch and offline play.
- `../../_scratch/untangle/play/extra-results.json`: score tiers, best preservation, clearance slide and restart races.
- `../../_scratch/untangle/art-checks.json`: all 23 backdrop darkness checks and painted glint registration.
- `../../_scratch/untangle/audit/audit.md`: the one complete mechanical audit, including its raw leads.
- `../../_scratch/untangle/final/`: targeted checks after compact-layout and pointer-focus fixes, plus comparison frames.

#### Implementation choices

- The spec's packed X values count non-shared line intersections including exact touches and overlaps.
  This interpretation matches every record and both hashes; runtime trouble follows the separate 7 px/4 degree rules.
- A drop shorter than 4 px returns to its lift position. It cannot accumulate free movement or a zero-move best.
- The 680x425 preview uses a compact control rail to preserve actual pixel clearance. The specified laptop and
  390x844 phone arrangements retain their top shell controls and bottom strip.
- Transparent generated paintings are resized without chroma-keying or trimming their coordinate canvas.
  First Skies painted cut-outs fit their guide bounds; glints use the painted gold sprite registered at the exact guide coordinates.
- Asset filenames use lowercase `sky-l01` through `sky-l20`, matching the bundler's lowercase token grammar.
- The move pace is verified reachable. Neither the spec nor this build claims an exact global minimum.
- There is no opponent, losing state, or pass-and-play mode in this game's spec.
- Cold review: Undo now settles a pending slide and checks for a solve before removing history. This prevents a
  rapid Undo from minting a lower score while putting a crossing back into an already solved sky.
- Cold review: `revealLanded` and `settleReveal` preserve the painted reveal and daily beams on resize or a
  motion-mode change during the glide. The motion callback ignores unrelated shell repaints.
- Cold review: drops that reduce crossings get a brief geometric gold halo; Calm keeps the still appearance.
- Cold review: the effectively empty notes file has been restored with game-specific grown-up guidance.
- Cold review: saving initials focuses the shell's Next button; Next preserves keyboard focus on the new sky.
  Tool-local adapters also name the shell's modal cards and keep Tab inside them. No executable shell code changed.
- Cold review: the desktop Worlds overview reserves extra header/footer space when sizing tiles, so its Back
  button stays fully visible in the 1000x625 preview. Phone and short-landscape overrides keep their layouts.

#### Engine changes wanted

- `kit/recess.js`, header: escape or remove literal `<script>`/`</script>` and `<link>` examples in the header comment.
  `bundle_tool.py` currently interprets those examples as tokens and produces invalid inline JavaScript.
- `kit/recess.css`, `.rc-arr`: use a 44 px minimum height for initials arrows. This game supplies a local style override.
- `kit/recess.css`, phone toolbar: allow the title and four-digit total to fit beside five controls at 375 px.
  This game supplies local font and spacing overrides.
- `kit/recess.js`, `card` and `initials`: label the dialog from its heading, contain Tab inside it, and move
  focus to Next after saving removes the initials form. This game supplies tool-local accessibility adapters.

#### Left open

The requested three-child playtest, ages 8 to 13, was unavailable in this unattended session. The 30 to 90 second
human median and enjoyment/stall criteria are not claimed. All automated play and geometry evidence is separate.
The owner's decision on the visual bar remains the owner's decision; the painted look board and final frames are provided.

#### Live early

Live early for Cory to see, 2026-11-12, process not exempted. tool.draft.json was renamed to tool.json only so the site lists the game; Refine, Exit check, Art and voice, Finish check and Sign-off are still owed.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-09)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-09)
- 2026-11-25: handoff.md folded in (last changed 2026-11-11)
