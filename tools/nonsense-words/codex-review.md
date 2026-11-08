# Codex review: nonsense-words

## Played
Simulated a grade 2 reader and projector teacher: Explore, flags, mixed Practice, review, perfect Challenge and a real one-minute timeout. Played before reading builder reports, notes or source. The quiet reading space fits the brief.

## Findings fixed
- **Should fix, general, Explore:** the opening hint and welcome named disabled Back. Instructions now name available controls at the first, last and single-review-word boundaries.
- **Should fix, general, compact controls:** Sound, Motion and Read were 44 px tall. All now retain the grade-band 60 px target.
- **Should fix, general, perfect result:** the 680x425 panel clipped the personal best. Short previews keep the wide banner, score and best; a redundant heading yields room, with tighter paragraph spacing. Larger results retain their headings. Added #best to that audit state's keep list.
- **Should fix, general, Read:** four fixed hints were absent from the narration catalog. All 12 instruction lines now match allLines and voice/lines.json. Marking hints use words without spoken check/cross glyphs.
- **Should fix, general, Flagged:** reopening the picker while its closing welcome played cut that instruction permanently. Only an interrupted welcome is rearmed; the next Close plays it whole. Fully heard instructions stay quiet.
- **Polish, general, mode navigation:** added the control-group role, so the audit discovers and walks both timed modes.
- **Polish, general, Practice ending:** replaced generic encouragement with the actual attempt count and specific review count.
- **Polish, general, parchment:** visible repeating squares weakened the otherwise appropriate art. Rendered the existing paper once at cover size, removing seams while retaining texture.
- **Polish, general, notes:** added a concrete supportive response to Not yet: blend taught sounds together and retry in Practice these.

## Findings left
No in-scope blocker or should-fix remains. The unchanged bank still needs the owner's specified approval before shipping.

## Flattest moment left
Ordinary Next remains a quiet, repeated action, as the owner's Look requires. The listening partner supplies reading feedback. The formerly generic Practice ending now points to this reader's specific review set.

## Graphics
Both finished assets inspected: 640 px parchment and 80 px quill, including their displayed sizes. Retained both, 5,450 bytes total; no missing art or people. Improved the weakest rendering, the tiled paper, without adding illustrations.
Final bundle: 71,692 bytes, about 70 KiB. Blue border, centered word, still header flourish and Sight Words sibling structure preserved. Viewed both bar tools' existing bundles; the owner's plain Look takes precedence.

## Audit
One full audit completed with exit 0 under the 40-minute limit, Chrome 9961 and host 8765. Evidence: _scratch/nonsense-words/review-audit/audit.md. All 87 PNGs inspected in the 15 review-audit-contact sheets, with important frames opened individually.
Its one mechanical lead was the Flagged welcome interruption, confirmed and repaired. Sizes, mode/state layouts, Motion off, control/Enter paths, five-click checks, quick taps and resize stress otherwise passed.
The audit snapshot precedes the final compact-result, Read-catalog and modal-recovery repairs. Only affected states were re-shot afterward; no second full audit or polish round. Evidence: review-exit.log, review-exit-frames, review-compact-final.log and review-compact-final-frames in Scratch.
All 36 independent functional checks passed: exact bank/order/kind counts, every Practice length, 2-second green plus 2-second yellow thresholds, no automatic Practice advance, review subsets, skips, late Challenge input rejection and perfect scoring.
Bank recomputation: 114 + 50 + 36 = 200 unique lowercase entries. Smallest kind has 36 words, enough for a 30-word Challenge. A real 61-second wait ended Challenge; a keyboard-only 20-word run finished with focus on Again.
All eight STANDARDS sizes were checked, including the 375x812 iframe. Grayscale, Sound off with Read and Motion off were checked. Nominal contrast: ink/paper 12.06:1, muted/paper 5.82:1, white/blue 8.75:1, Right 6.90:1, Not yet 6.38:1.

| Voice check | Kind | Expected | Observed |
|---|---|---|---|
| Explore after five held Next taps, 2 s apart | welcome | 1 | 1 |
| Marking, review, Again and kind-guard Read hints | Read | 1 each | 1 each |
| Interrupted picker welcome after Close | welcome | 1 complete retry | 1 complete retry |
| Five perfect sessions | event | 5 complete cheers | 5 complete cheers |

Focused product checks had no console errors. The earlier phone host favicon 404 and a corrected test toggle-order assertion were harness issues, preserved in Scratch. The final hosted checks were clean.

## Left open
- Owner bank approval, as the spec requires. Handoff preserves the builder's concerns and adds nog, fid, neg, dob and nesh as candidates for the owner's real-word/sound-alike review. No words were changed.
- Browser speech remains the spec-approved temporary voice. Muted Chrome verifies scheduling and text, not listening quality; no classroom trial was performed.
- Unattended decisions followed the owner's quiet Look and sibling direction over generic art/gameplay instructions. No questions, new topics, features or kit changes.
- Final report written last to honor the explicit stop instruction; the working draft was saved in Scratch throughout. No git commits. Drive cleanup completed; used ports are closed and temporary host.html is absent.
- System process inventory was denied by Windows. Browser cleanup used the prescribed drive.py routine; ports 9960, 9961 and 8765 were independently confirmed closed.
