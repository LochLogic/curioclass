# Codex review: weekend-drawing-share

## Played
Cold play before builder notes: as a K-2 artist, drew a place, chose an art word, added a person, and saved; then retold Pip's seven-part sample and tried compact drawers. The warm room and paper invite drawing; the final whole picture is worth sharing. Also checked the teacher's projected workflow. One review pass, with focused rechecks only.

## Findings fixed
- **Should fix, general, src.html keyboard Size:** growing a sticker near an edge clipped it outside the sheet. Clamp its center after keyboard resizing, matching pointer behavior. Before/after frames and a keyboard-only placement/move/resize run confirm the repair.
- **Should fix, general, src.html Save:** a successful retry after blocked storage left the failure message on the question card. Refresh the card on successful Save; the original question returns and the saved hint agrees.
- **Should fix, general, src.html picker speech:** queued colors, brushes, and widths could name obsolete choices. Interrupt ordinary picker speech and validate the selected value. Read remains protected; red/orange were dropped and only current yellow followed Read.
- **Should fix, general, src.html and voice/lines.json:** Read used short chip names and waiting text absent from allLines/lines.json. Register the exact phrases and read the registered confirmation instruction. The two line sets now match exactly.
- **Polish, general, replay payoff:** badges and the invitation to speak waited behind long narration while the picture sat still. Reveal reasons one by one as drawing finishes and show the speaking invitation immediately; retain question-then-chip speech and revision guards. Added audit states for this and keyboard edge resizing.
- **Polish, general, art:** the dog looked photographic beside wax stickers. Repainted it with rich crayon grain using built-in imagegen, saved the prompt in art/prompts.json and raw PNG in art/raw/dog.png, then ran art.py --rekey dog with despill. Kept all other art and the studio's finish. Updated notes and handoff.

## Findings left
- **Polish, general:** New drawing, Save and the saved shelf need page scrolling in short previews and the 760-wide portrait layout. Core drawing/replay actions, hints, and all ten art words remain visible. This preserves the 4:3 paper and 60-pixel controls.
- No known blocker or should-fix remains from this pass.

## Flattest moment left
Opening Tools, choosing a color and closing it adds a pause in the smallest preview. The full classroom view keeps the tray open. Squeezing the controls would weaken the drawing space.

## Graphics
Checked all 18 processed assets on a fresh contact sheet and in their final contexts, including the dog at drawer, normal, and maximum sizes. Four Pip poses remain consistent. Verified Pip's complete sprite on contrasting magenta. The quiet unoccupied backdrop follows the explicit spec; people stamps are editable code-drawn figures, with no generated people assets to mark or stereotype. One dog redrawn; no assets removed. Bundle 1505 KB. Beat Lab reference frame inspected without writing in its folder.

## Audit
The single final audit completed in about 33 minutes, within its 2400-second limit, on Chrome 9941 and host 8745. All 92 frames were opened. Its 109 leads were reviewed: 76 size/state leads for intentional overlays, modal occlusion, pointer-transparent badges, the Size handle, disabled empty Tell it, and compact auxiliary shelf placement; 33 welcome leads follow the standing skip-on-own-action-line rule. Full dispositions: _scratch/weekend-drawing-share/review-audit-dispositions.md. No further source repair was warranted by the audit.

All 68 held-click rows retained control identity and focus, with no errors or control jumps. All ten five-click cases and ten quick-tap cases were clean. Final resize stress found no exceptions or controls left disabled. Motion off had no endless animations. The automatic mode walk starts empty, so actual Tell it behavior is covered by the separate sample/replay states and cold play. No second audit or polish round. Owned Chrome/server listeners are closed; host.html is absent.

Focused checks passed with zero console errors: identical 1920-to-760 stroke coordinates after reload, six saves and explicit replacement/Cancel, polite storage failure and successful retry, 20,000-point cap, 4000ms maximum replay, exact seven sample chip pairs, rapid replay navigation, keyboard-only drawing via stamps, grayscale, Motion off, and Read priority. All focused frames were opened. The corrected reload fixture scrolls the saved card into view before clicking it.

| Voice line | Kind | Expected starts | Observed |
|---|---|---:|---:|
| Five successive questions | event | 5 | 5 |
| Big, selected five times | event | 5 | 5 |
| Next question how-to | how | 1 | 1 |

Recomputed white/brand 6.3088:1, brand/paper 5.9668:1, ink/paper 14.8800:1, muted/paper 6.0990:1. Replay examples match 0.5, 2, 4, 4 seconds. The spec's 11-character point storage estimate is optimistic: the tested integer triple uses about 19 characters. Save failure remains non-destructive. Both standards are practiced by making, revising, explaining and retelling the child's own experience; there is no scored wrong answer or hidden answer to give away. Notes open with the three required sections and accept the child's own reasons. Wave checks cover current hints, stable focus, sizes, honest counts, visible choices, motion, resize, and state-matched speech.

## Left open
- Recorded curious-librarian narration remains absent; browser speech is the fallback. Recording is outside this task's rules.
- Keep the builder's documented welcomeAfter:false choice: the multi-mode wave lesson overrides the spec's true flag. No late welcome was introduced.
- No classroom trial, new features, engine changes, or commits. Authored project changes stayed in the two authorized folders. The report draft stayed in Scratch until completion to obey the explicit stop-on-report instruction.
