# Codex review: untangle

## Played
- Cold play preceded the builder's report, handoff and notes. Adult reviewer using a Grade 3 solo-player lens, then an adult planning lens; no actual child playtest is claimed.
- First fresh standard bundle was unplayable. After the local bundling repair, solved Sky 1 visually in two moves, completed R001, and explored the daily with Undo and Restart before reading builder commentary.
- Then played all 20 First Skies, R001/R025/R162/R550 and the daily to zero with real pointer input. Keyboard-only Sky 1: two moves, three stars. The luminous Kite/Whale reveal is the strongest moment.
- Judged against CODEX-RECESS.md, GAMES.md and the complete spec. Computer opponents, opponent levels, pass-and-play and losing states are not part of Untangle.

## Findings fixed
- **Blocker, general, bundling:** standard `bundle_tool.py` exposed shell JavaScript and threw `Recess is not defined`. Replaced the dangerous script/link example comment in a tool-local shared-shell snapshot; standard bundling now works without a Scratch postprocessor. Executable shell code is unchanged; kit/scripts untouched.
- **Blocker, family:untangle, Undo during a winning slide:** real near-simultaneous drop/U produced `solved=true`, two actual troubles and a move erased. Settle the pending slide before popping history, then re-check solved. Same attack now retains the valid six-move, zero-trouble result.
- **Should fix, family:untangle, resize during reveal:** resizing in the glide cancelled it before bloom, leaving the earned picture invisible. Centralized reveal landing/settling, preserved daily beams, and ignored unrelated shell repaints in the motion callback. Re-test: bloom present, picture opacity .86, zero trouble.
- **Should fix, general, keyboard:** saving initials removed the focused control; Next then lost the new sky's focus. Save now focuses Next after the click completes, and replacing a focused sky restores focus on its first star. Tool-local adapters also name the shell cards and contain Tab within the modal.
- **Should fix, general, notes:** `notes.md` contained only whitespace. Restored the spec's game-specific grown-up explanation, family activities, controls, move-based stars, invented-picture context and device-only privacy. Difficulty is described as a prediction, not a guarantee about each player's moves.
- **Polish, family:untangle, quiet improvement:** a useful drop could feel like a changed number. Added one short warm geometric halo when crossings fall. Calm has no pulse. Kept the existing paintings, palette, sound layer and generous star hit areas.
- **Should fix, general, overview at 1000x625:** the Worlds Back button was clipped despite a clean mechanical fold check. Reserved more header/footer height in the desktop tile formula; kept phone/short-landscape layouts. Targeted screenshot and bounds check: PASS, all 23 tiles and the full 44 px Back button visible; Back ends at y=591.5 inside the dialog ending at y=604.5, with no scrolling (`../../_scratch/untangle/review-overview/`)..

## Findings left
- **Validation gap:** spec Done when 12 requires three children aged 8 to 13 and timing/stall observations. Unavailable unattended; adult role-play and automated solutions do not establish it.
- Shared shell/bundler fixes remain requested in `handoff.md`; local workarounds make this tool reviewable without editing shared files.

## Break it
- **Win gate:** live zero while held remained unsolved; release solved. Each non-shared pair is counted once; 3/6 px gaps count, 8 px does not; shared right/opposite rays clear, narrow angles and overlaps count. Edge clamp and east-first slide checked.
- **Degenerate wins:** stacked stars, straight rows, half-pixel zigzags and tiny clusters all remain troubled on every First Sky. Mirrored valid layouts pass on all 570 skies. These are scripted geometry tests, alongside the real-input paths above.
- **Moves:** eight repeated sub-4 px drops left positions unchanged and moves zero. Rapid Undo stopped at zero; Escape cancelled a lift; resize while held cancelled safely, and release added no move. Winning-slide Undo exploit is closed.
- **Stars/best:** real 2-, 7- and 13-move solves earned 3/2/1 stars; poorer replays preserved the two-move best and three earned stars. Undo exploration and replaying a known sky are expressly allowed by the spec.
- **Initials:** repeated Enter after Save created one entry in that attempt. The fixed Save/Next path stays keyboard-operable. The unchanged shell sorts and caps its local board at ten.
- **Daily:** five independently regenerated dates have 15 stars, 24 lines, six beams and reachable pace-15 witnesses. Two Chrome instances matched today's first three starts. Real daily solve used 14 moves and displayed six beams.
- **Input/access:** real phone touch at 375/390 px gave one move, no page scroll and zoom 1; chart swipes wrapped World 22 to First Skies. All 23 world tiles and 25 sky tiles fit. A 9,999-star total still fits the 375 px toolbar.
- **Motion/sound/offline:** verified Calm has zero running infinite animations; dashed/ringed trouble remains readable in grayscale. Muting stopped active notes; chime calls while muted created none. Game resource checks found no HTTP requests or runtime exceptions.
- Evidence: `../../_scratch/untangle/review-browser/{pre,post}-results.json`, `review-scenes/focus-results.json`, `review-scenes/measurements-record.json` and their frames. The first scenes batch's `calm-loops` row accidentally toggled Motion on; the explicit `calm-loops-verified` row and final audit supersede that test setup.

## Voice walk
- None, as required for Recess. Followed the visual instruction, drag/drop, Undo, Restart, chart, daily, solve, initials and Next. No narration, classroom header, Read flow or lesson cards were added. ARIA lift/count announcements remain.

## Facts checked
- Exact First Skies JSON matches the spec. Both ladder SHA-256 checksums reproduced; every recorded intersection count, connected graph, degree bound, start spacing and non-decreasing model D passed.
- All 570 skies re-solved at or below their stated pace on 1300x620, 366x690 and compact 484x401 fields; canonical and mirrored arrangements have zero trouble. No exact minimum is claimed by the spec or this review.
- Counts, clearance thresholds, score tiers, world/page structure and daily sizes checked against the spec's Rules, Content and Modes sections with 11,467 assertions and no failures: `../../_scratch/untangle/review-validation.json` and `review_validate.js`.
- No health, safety, historical or cultural factual claims were introduced. The graph statement is backed constructively by each verified crossing-free drawing. Source/licence declarations retain the original project data and generated-art provenance.
- Class creep: zero specified lesson-word hits or standard codes in `src.html`; no em dashes.
- Text/quiet text contrast against the lightest allowed sky: 13.44:1 and 7.71:1. Line colours exceed 6.5:1, with dashes/rings supplying the non-colour signal: `../../_scratch/untangle/review-contrast.json`.

## Sensitivity
- None requiring cultural review: invented constellations, fantasy creatures and landscapes, with no people, traditional sky stories, real constellation claims, religion, bodies or hard history. Notes state that the pictures are invented.

## Flattest moment left
- Deliberation on a dense late sky is necessarily quiet; the live dashes/rings carry it. The improved-drop halo lifts the small payoff without distracting from planning. Kept the rich painted Whale and world-finale rewards.

## Graphics
- Inspected all 69 existing assets: 23 landscapes, 42 reveals, three painted star sprites and the 1200x750 text-free cover. No painting needed replacing; geometry alone remains code-drawn.
- All 23 backdrops pass the connected bright-region test with the permitted 40% veil. All 230 painted glints fall within 1.10 px of the target star positions, below 12 px: `../../_scratch/untangle/review-scenes/art-checks.json`.
- Opened the art contact sheets; full Whale, R025/R162/R550 and daily frames; before/after race and resize frames; phone opening/held/chart/overview/stress frames; keyboard win, grayscale, shell demo and Beat Lab comparison. Untangle reads as its own world.
- Final bundle: 4,723,605 bytes (4.72 MB), below the 6 MB Recess limit. Cover remains separate.

## Audit
- One complete final audit: `../../_scratch/untangle/review-audit/audit.md`, Chrome 9961, host 8765, 40-minute limit. Its 108 leads were 52 expected SVG halo/hit overlaps, 55 ARIA-only labels mistaken for visible text, and one broken review win-card fixture (missing return in drag bodies).
- Corrected the fixture and re-shot only that state at 1366x768/375x812: solved in two moves, named modal, forward/reverse Tab contained, all controls at least 44 px, Save to Next to new-star focus passes, no exceptions: `../../_scratch/untangle/review-win-state/results.json`.
- Inspected all 35 audit frames. No target, console, Calm or stuck-control fault was confirmed. Visual inspection additionally caught the clipped Worlds Back button at 1000x625; fixed and re-shot that overview only. No second full audit or polish round.

## Left open
- Three-child playtest remains unverified. No outside contact, submission, deployment or shelf edit occurred.
- Ran from `S:\CurioClass-codex`; wrote only `tools/untangle/` and `_scratch/untangle/`; no commits. Bundle/browser/audit command limits were 120/300/2400 s. All started Chrome/server processes closed.
