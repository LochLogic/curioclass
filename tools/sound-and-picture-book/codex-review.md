# Codex review: sound-and-picture-book

## Played

Cold K-2 solo/classroom walk: Plan, Sample book, Make, all three Play pages, The end, sound swap and replay before opening the builder's report, handoff, notes or source. Warm, inviting paintings; the sound exchange needed a clearer physical payoff. Also walked original planning with held 120 ms clicks at a two-second pace, and tested it as a projected class activity.

## Findings fixed

- **Blocker, general, Undo:** an old full-book snapshot erased a later picture edit. Actual picture/sound edits now clear earlier swap history with a visible explanation; selecting an unchanged piece retains Undo. Pond survives the original Cave/edit/Undo reproduction; ten consecutive swaps still undo.
- **Blocker, general, capacity:** Who could turn the first prop into an animal when a page held four things. It now leaves the complete book unchanged and asks for room in Make. The four-prop path passed at 680x425, 1366x768 and 375x812.
- **Should fix, general, Make voice:** Plan's character placement caused Make's introduction to be dropped. The introduction now fits the actual page and is heard on the normal planning path.
- **Should fix, general, Read:** a native modal blocked the header Read button. Every choice tray now has its own Read using the same queue. It stops an audition, reads current instructions, and retains Read priority over a new sound assignment.
- **Should fix, general, voice catalog:** fixed Read hints and finite card/sound variants were absent from allLines. Synchronized the 224-line manifest; audition hints also stop claiming Listening when the audition ends.
- **Should fix, general, false changes:** equal sounds and identical pages claimed Swapped and consumed Undo. Both now explain the unchanged result without a history entry. Chip/page selection clears the other selection, and Sample clears pending cards and old change text.
- **Should fix, general, Plan:** compact pages hid the assigned What happens cards, and a modal blocked card drag targets. Page buttons now retain the event icon/word; dragging exposes the pages. Real tap and native drag are rechecked.
- **Should fix, general, suggestions:** custom books were told to swap absent Snap/Snore chips. Suggestions now fit current contents, name the controls to use, and are narrated when shown.
- **Should fix, general, editing:** keyboard limits differed from dragging, and edge/resize positions cropped paintings. Shared limits retain whole pieces. Accessible pose labels now change with the painting.
- **Should fix, general, audit frames/voice:** a Size handle covered the animal's face on compact and phone screens; it now finds nearby clear space while staying 60 x 60 and inside the paper. Plan-slot dialogs were silent; their instructions now speak once. Selection also speaks its matching editing help once.
- **Polish, general, Play/Craft:** chips and pages now travel to their exchanged positions for 420 ms, with immediate state changes and no control lock. Motion off skips/cancels the exchange.
- **Polish, general, art:** redrew the scared turtle to match the happy turtle's warm shell, spotted skin and rounded limbs. Kept the other 22 paintings, paper layers, linen, page curl and scene layout.

## Findings left

No additional confirmed implementation blocker or should-fix remains from this pass. Exact inline card/sound layouts and circular action chips remain the documented spec conflict described under Left open; recorded-voice identity and audible seam verification are still open.

## Break it

- No score, meter, quiz, best score or reflection gate exists. The end is a navigation invitation, with no mastery claim. Blank playback is explicitly allowed by the spec.
- Tried bypassing disabled Make it through mode tabs and racing empty pages to The end: creative blank playback works as specified, with no badge or learning credit. The proper three-place path enables Make it.
- Tried a fifth piece: four remain and the limit is explained. The same check protects every Characters/Things choice.
- Tried Who on a page already holding four props: all three pages remain byte-for-byte unchanged, with an actionable explanation. This closes the alternative route around the capacity check without deleting a prop.
- Tried wrong-kind sound swaps by taps and a real jittered drag: book unchanged, no Undo entry, explanatory feedback.
- Tried identical sounds and identical blank pages: no Swapped praise and no Undo entry after the fix.
- Tried rapid repeated swaps and ten undos after twelve changes: history exhausts cleanly and the tested sound order is restored. Tried switching to Make and editing before Undo: new work survives and old Undo is disabled with an explanation.
- Tried loading Sample while a different Who card was pending: the sample remains Raccoon and the pending card clears.
- Tried blocked storage: editing remains usable with a visit-only status. Persistence and both New book choices are checked in the final targeted batch.
- Choosing every sound is artistic exploration, with no hidden answer or score to farm. All six backgrounds and eight actions are exercised separately; sound-only swaps retain the pictures, while whole-page swaps retain pictures and their sounds together.

## Voice walk

Default Sound on; Who > Fox > Beginning > Where/Forest/Beginning > Where/Cave/Middle > Where/Campsite/End > Make it > Background/Rain/Close > Action/Splash/Close > Play book > Next > Next > Next > Swap. Held clicks, two-second gaps. Repeated after the audit repairs. Evidence: Scratch/main-post-audit.json.

Spoken in order: card instruction, Fox, Where instruction, Forest card, Beginning: Forest path, Cave card, Middle: Cave, Campsite card, End: Campsite, That's a plan, prepared-picture Make instruction, sound-tray instruction, Rain, Splash, Play instruction, The end, Swap instruction, applicable Thunder suggestion. No dropped how-to in the final walk. First-tap Plan welcome is legitimately skipped for the card tray's own instruction; its premise remains in the initial hint and Read.

| Line | Kind | Expected starts | Observed starts |
|---|---|---:|---:|
| Card-tray instruction, four openings | how | 1 | 1 |
| Make / Play / Swap introductions | how/welcome | 1 each | 1 each |
| Sound-tray instruction | how | 1 | 1 |
| Rain / Birds, five assignments | event | 3 / 2 | 3 / 2 |
| Plan-slot instruction, three openings | how | 1 | 1 |
| Editing instruction, five selections | how | 1 | 1 |

Side path: Make > Action > Snore audition > tray Read > Thunder assignment. Read starts, stops Snore, and Thunder waits until Read finishes. Header Read also works with Sound off. All logged spoken/read texts match the manifest. No queued mode how-to failed to start on the tested main path. Later actions can cut a started introduction; its full instruction stays in the hint/Read. Chrome is muted as required; this establishes queue/timing behavior, not a listening-quality verdict.

## Facts checked

- Planning ideas, organizing a model, revising content, and combining media: [NCAS Media Arts at a Glance, K-2 Cr1, Cr2, Cr3, Pr4](https://www.nationalartsstandards.org/sites/default/files/Media%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf). These are practiced in Plan, page order, Make/Swap revision, and playback respectively. This tool teaches selected practices, not every performance standard in each family.
- Sound can affect a picture's perceived meaning: Michel Chion, [Audio-Vision, Projections of Sound on Image](https://pzacad.pitzer.edu/~mma/teaching/ms52/readings/audio-vision3-13.pdf), added value. The scan identifies Columbia University Press, 1994, translated/edited by Claudia Gorbman. No universal emotional response is claimed.
- Beginning/middle/end: the three-part design of this book, not a claim that every good story follows that order. Corrected the welcome accordingly.
- Contrast, recomputed with [W3C WCAG 2.1 contrast/luminance definitions](https://www.w3.org/TR/WCAG21/#dfn-contrast-ratio): white/brand 10.358:1, brand/paper 9.335:1, ink/paper 14.574:1, muted/paper 5.994:1. All meet AA for normal text.
- Spec timing/counts independently recomputed: 1000/625 = 16/10; 6 + 12 + 5 = 23 assets; Snore 2 x 1.6 = 3.2 s, beginning at .8 s ends at 4.0 s before a 6 s Auto turn. The .20 + .40 = .60 calculation is a bus-gain sum, not a measured waveform guarantee. Evidence: Scratch/review-numbers.json and audio logs.
- Offline/save/sound provenance: source inspection finds embedded original illustrations, synthesized Web Audio, localStorage in try/catch, and no fetch, socket, upload, camera, microphone or external runtime URL. The sample's named pieces, poses and sounds were checked against spec Content. No biology, health, safety, legal or financial lesson is presented.

## Sensitivity

None: an invented animal story with unnamed woodland settings; no people, cultures, religion, Indigenous content, hard history or human-body teaching. All 23 assets are marked people:false. The campground belongs to the fictional animal story and does not require a missing human cast.

## Flattest moment left

Planning several cards still takes repeated tray openings. The complete trays preserve large targets and all choices; Sample book remains a vivid first-tap entry. The weaker swap payoff was lifted without reducing the art or play.

## Graphics

Inspected all six backdrops at 1000 x 625, all twelve animal poses and five props, cutout edges, actual Make/Play/Swap frames, Motion off and grayscale. One style, no placeholders or people. Redraw: art/raw/turtle-scared.png > art/turtle-scared.webp, built-in imagegen with turtle-happy reference, finished through art.py --rekey only; full prompt/provenance in art/prompts.json. Bundle 1557.43 KiB; finished art 1099.28 KiB. Opened both snowy-mail-route and beat-lab bar frames; comparison in Scratch/review-bar-comparison.png. Kept the book's rich finish.

## Audit

The one full audit completed within 40 minutes: 33 reported leads, 68 inspected PNGs, all eight STANDARDS sizes, all modes, populated/selected/end/dialog/extreme states. Chrome 9961, host 8765; targeted checks used 9960. No small targets, horizontal scroll, application exceptions, unintended control shifts, failed Enter-twice paths, repeated how-to faults, quick-tap faults or resize-stress failures. Motion off had no infinite animation.

Disposition: transparent animal/lantern hit-box overlap and native-modal coverage of inactive art are intentional. Play's actual how-to is classified as how rather than welcome; Sample, New book and card trays use their own first-tap lines under BASELINE 16. The three genuinely silent page-slot paths and the obscuring Size handle were fixed afterward. The original audit is preserved; targeted frames at 680x425, 1366x768 and 375x812 verify the repairs. Real resizing reached 460; keyboard resizing reached 80 and 460. Main voice path repeated, with no unspoken queued how-to. The final Who guard also received a separate three-size check. No second full audit. Detailed disposition: Scratch/review-audit-disposition.md; measurements: Scratch/review-postfix-measurements.md.

Wave lessons checked: current hint/Read, first-tap timing, focus retention, all-size targets/fold, full short choice sets, calm timing, resize during actions, unknown empty pages, distinct chip meanings, truthful labels and restored hints. Hidden-answer/giveaway/copied-answer and misleading-estimate cases are inapplicable: no assessment or estimate exists. Standards map to actual planning, arranging, revising and playback activities.

An early reload-inside-evaluation fixture failed and was retried successfully with a state-reset fixture. Final drive batches reported zero application console errors. The temporary phone host emitted connection-reset messages when tabs closed; this was host cleanup, not a bundled-tool request or browser exception. All owned browser/server ports were verified closed; tools/sound-and-picture-book/host.html is absent.

## Left open

- Complete choice trays and pill-shaped action chips remain intentional deviations from exact inline selectors/circles. The 60 px K-2 targets, complete short choice sets, substantial picture and 425 px preview cannot all support fourteen permanently inline sound choices. STANDARDS sizing/readability wins; no kit or spec was changed.
- Recorded Algenib/gravel-ranger clips are absent. Browser narration remains the fallback because CODEX-BUILD.md forbids recording audio in this work. A production voice pass and headphone loop-seam/timbre listening remain open; muted automation cannot honestly certify them.
- No questions were asked in the unattended session. Kept the spec's defaults, existing compact-layout compromise and six-second timing. No git commits. Writes confined to this tool and Scratch; the restarted session continued the same evidence and fix pass.
