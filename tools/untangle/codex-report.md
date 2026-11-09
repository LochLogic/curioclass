# Codex report: untangle (Recess)

## Built

Built in `S:\CurioClass-codex`, writing only `tools/untangle/` and `_scratch/untangle/`.

One offline Recess game: 20 First Skies, the exact 550-sky ladder in 22 worlds, and a worker-generated daily.

Bundle: **4,720,996 bytes** (4.72 MB, 4.50 MiB), below 6 MB. Cover is separate.

No kit header, voice, classroom flow, accounts, network requests, commits, deployment, shelf edit or polish round.

The report was written last to honor the user's explicit stop condition. Rebuild instructions are in [handoff.md](handoff.md).

## Rules check

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

## Puzzles and levels

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

## Computer opponent

Not applicable. Untangle has no opponent, computer ladder, losing state or pass-and-play mode in its spec. No artificial opponent was added.

## Break it

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

## Look board

One direction was obvious from the world table: an indigo painterly nocturne with warm stars and luminous creature reveals. World art and three static 1366x768 hero frames were painted/assembled before game logic:

- [Opening](../../_scratch/untangle/look/opening.png).
- [In progress](../../_scratch/untangle/look/in-progress.png).
- [Best moment](../../_scratch/untangle/look/best-moment.png).

Kept this direction for its contrast between the quiet tangled sky and the bright earned reveal. During the build, all backdrops were repainted darker, glass-orb stars became warm light glints, the fox/stag became guide-shaped faces, and Far Galaxy became pure space. No asset exceeded three generations.

## Grab check

Best moment: the last crossing disappears, threads turn gold, and the whale blooms. [Final real-play Whale](../../_scratch/untangle/play/L17-final-painted.png). [Far Galaxy finale](../../_scratch/untangle/play/R550-final-painted.png).

Flattest moment: the unlit opening sky. Its deliberately quiet landscape protects the thin threads; marching dashes, live rings, warm glints and held-star growth give the first action an immediate response.

The comparison shows a distinct game world beside the shared shell test bench and an existing classroom tool: [Untangle / shell demo / Beat Lab](../../_scratch/untangle/grab-comparison.png).

## Class creep check

PASS: zero whole-word hits for standard, objective, learn, skill, lesson, correct answer or well done; zero standard-code hits in `src.html`. No voice assets or classroom kit imports. Adult context lives in `notes.md`.

## Sources

- Puzzle source: the exact original project data in `spec.md`, 20 hand-made skies and 550 packed records. No third-party puzzle set, art, names or code used.
- Daily: original six-line generator implemented from the spec, using the shell daily random stream.
- Wikipedia Planarity and Fary's theorem: CC BY-SA 4.0 text, as recorded in the spec; background/history only, no text copied.
- Simon Tatham Untangle manual: MIT-style licence as recorded in the spec; mechanic reference only, no code/art/levels copied.
- Illustrations generated with OpenAI gpt-image, edited for Curio Class. Individual prompts, redraws and provenance are in `art/prompts.json` and Scratch's generation log.

## Done when

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

## Frames looked at

All three look-board frames; all 33 audit frames through three contact sheets; full laptop Whale and Far Galaxy finale; final compact opening/chart/dense sky, 390x844 phone, focus and daily frames; normal six-beam sweep and calm beams; grayscale; shell demo and Beat Lab; both reveal contact sheets, all backdrops and the cover.

[Audit contacts](../../_scratch/untangle/audit/contact-1.png), [contact 2](../../_scratch/untangle/audit/contact-2.png), [contact 3](../../_scratch/untangle/audit/contact-3.png), [final contacts](../../_scratch/untangle/final/contact.png), [grayscale](../../_scratch/untangle/play/grayscale.png).

## Art made

69 WebP assets: 23 backdrops at 1600x1000, 20 First Skies paintings and 22 world paintings at 640x640, three 128x128 transparent light sprites, and a 1200x750 cover. Raw generated originals and prompts are preserved.

True-alpha cut-outs were resized and placed without chroma-keying or destructive trimming of their coordinate canvas. Painted light sprites register every First Skies guide point. Largest measured glint error is 0.88 px at 1366x768.

Every backdrop passes the connected bright-region test after the permitted 40% #0a0b26 veil. Relative-luminance and palette evidence: [art checks](../../_scratch/untangle/art-checks.json), [glints](../../_scratch/untangle/glint-registration.json), [contrast](../../_scratch/untangle/contrast.json).

## Shell changes wanted

Do not edit the kit in this build. The shell header's literal script/link examples break naive bundling; the local adapter removes only that header comment from the embedded shell. Local styles provide 44 px initials arrows and a phone toolbar that fits. Exact changes wanted are in `handoff.md`.

## Left open

The three-child playtest and its 30 to 90 second medians remain unverified. No humans were available and nobody was contacted. Visual acceptance remains the owner's decision; the look board and final real-play frames make it reviewable.

All started Chrome processes and the 8795 test server were closed. No commits or polish round were started.
