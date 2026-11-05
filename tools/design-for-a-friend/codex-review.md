# Codex review: design-for-a-friend

## Played
Grade 5 solo walkthrough of all three interviews, evidence boards, failed and successful prototypes, Polite yes, and shared design before reading the builder's files. Replayed the class/projector path. Listening and testing feel purposeful; the garden and portraits are strong.

## Findings fixed
- **Should fix, general, src.html avatar:** fallback silhouettes showed behind loaded portraits, giving Kofi an extra head/shoulder. Hide the SVG after the painting loads; preserve it for missing images.
- **Should fix, general, src.html updateHint:** live test-shelf selection still said to start testing; full phones named nonexistent empty slots; shared results omitted the next action. Hints now describe placement, making room, and Back to design immediately.
- **Should fix, general, shared Test drive:** only colored cells changed, hiding the person and their snag. The existing table now shows the active portrait, step, words, and a current-cell outline; snag descriptions have accessible labels.
- **Should fix, general, phone preview:** missed Save, tapped Delete, and a missed reminder looked much like success. The mock screen now shows those actual outcomes with words and symbols, retaining the five-step rule and timing. Compact controls wrap inside the phone.
- **Should fix, general, evidence overlay:** a running test and narration continued behind the board. Opening evidence now cancels them and keeps the next-action hint stable.
- **Should fix, general, voice:** Read hints were absent from the manifest. Centralized hints and their named variants now match allLines and all 58 entries in voice/lines.json.
- **Should fix, general, initial navigation:** revealing Reset moved Ask under a double tap, so the second tap hit Test and cut the instruction. Reserved the Reset footprint; all three tab rectangles now remain identical before/after entry at 1366 and 680. Real fixed-point double taps stay in Ask with one uncut instruction.
- **Should fix, general, direct Test entry:** the hint named Start but no instruction spoke. The existing Start hint now speaks once with current-state validity; five held taps produced exactly one start.
- **Should fix, general, quote dialog:** a real background click spent a question and left the sheet stale. Background work areas are now inert while it is open. Held clicks stay blocked on laptop/phone; Back and Escape restore controls and focus, and Read still speaks the board hint with Sound off.
- **Polish, general, restored results:** returning to a completed drive reset the marker and mock screen to step 1. Restored results now show step 5.
- **Polish, general, art:** redrew the weakest plant, kohlrabi, with a clear botanical silhouette; cleaned magenta fringes and gaps in all six plant cutouts. Preserved the garden and portraits.
- A null-state regression in the preview repair was caught and fixed before the final audit. The affected functional and held-input checks then passed without console errors.

## Findings left
- No confirmed blocker or should-fix remains open.
- **Polish, general:** recorded narration is unavailable; this review obeyed the instruction not to record audio. Browser speech remains the fallback.

## Flattest moment left
After all four shared features work, another identical run has little surprise. The shared portrait/quote makes the first test more human; further depth would require changing the fixed scenario, so none was added.

## Graphics
Checked all ten images in their actual scenes and the finished plant/people contact sheet. One built-in OpenAI imagegen redraw, plant-kohlrabi; raw art saved at tools/design-for-a-friend/art/raw/plant-kohlrabi.png, full prompt in art/prompts.json. Six plant cutouts rekeyed using art.py --rekey only. All three people assets retain people:true and their existing pending owner-review metadata. No missing art tokens. Art: 479.3 KiB. Bundle: 1180.2 KiB, about 1.21 MB. Compared the existing Snowy Mail Route and Beat Lab frames (review-bar-comparison.jpg); retained the rich studio finish.

## Audit
Finished once with exit 0 within the 40-minute limit, Chrome 9961 and host 8765. All eight sizes, the nine states in its frozen plan, Motion off, control walks, repeats, rapid taps, and resize stress completed. No application errors or stuck controls. Opened all audit PNGs directly or in labeled contact sheets; compact result and phone frames also inspected directly.

All 32 leads answered in Scratch/review-audit-dispositions.md: 22 tilted-card rectangle false positives; nine welcome warnings where the introduction correctly becomes stale; one real fixed-point Ask interruption, repaired. The Test row also exposed missing first-entry speech; the quote frames prompted the confirmed background-click repair. Only affected paths were re-shot afterward at 1366x768, 680x425, and hosted 375x812. The full audit was not repeated after these final narrow repairs.

Independent checks: 6,144 friend/subset outcomes; exactly one successful four-feature set, none of three, eight of five; empty snags and all ten contrast ratios match the spec (lowest 5.02:1). All 22 functional assertions pass. Keyboard Enter placement keeps slot focus; whole-pixel jittered drag places a feature; grayscale keeps checks, exclamation marks, and words; Motion off preserves the 4.074-second test.

| Voice line | Kind | Expected starts | Actual starts |
|---|---|---:|---:|
| ask, open-q, closed-q, design | how | 1 each | 1 each |
| lou-done | event, five drives | 5 | 5 |
| lou-snag | event, five drives | 5 | 5 |
| direct Test instruction | how, five taps | 1 | 1 |

Held clicks used 0.12 seconds; the five-action run used two-second gaps. Results were deliberately restarted while their narration played; obsolete speech stopped. Read matched the current hint with Sound off. All 58 possible Read/narration lines match the manifest exactly.

## Left open
Existing owner review of Lou, Ana, and Kofi remains pending; the review-art.png contact sheet in Scratch includes them. No kit or spec changes. No commits. All owned browsers and host servers closed; no host.html remains. No actual classroom or audible headphone test. The initial read-only rules command lacked a hard timeout; every subsequent shell command used a deadline.
