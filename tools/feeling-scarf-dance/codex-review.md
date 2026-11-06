# Codex review: feeling-scarf-dance

## Played

Cold as a K-2 child at home, then as a projecting teacher: Build, Watch, Your turn, Share and Swap, before builder notes/source. The flowing cloth is worth copying with a real hand or scarf. Preserved its hilltop, music, patterns and simulation.
## Findings fixed

- Should fix, general, src.html/startRun: Play and Go cut off mode instructions at two-second held-tap pace. A cancellable pending start finishes the fitting introduction before music; Stop, Read, mode changes and opening an editor cancel stale work.
- Should fix, family:dance, choosePart/setMode: an idle edit froze at the first instant of its transition, showing the old pose beneath new labels. Idle edits and mode entry now show the selected start pose; running edits retain their 180 ms transition.
- Should fix, general, Share: removing a chip still praised that observation, and checked observations survived a changed dance. Chips now record observations consistently; Swap or changed feeling/parts clears them. Unique event keys preserve repeat speech; revision checks discard old observation, reflection and Freeze lines.
- Should fix, general, Build: choosing all parts before the feeling left the next step unspoken. Guidance now follows the missing choice in any order, then announces Watch it when the feeling completes the dance. Idle previews label their actual part and clear old count dots.
- Should fix, general, Build: the personal-experience connection lived only in teacher notes. The feeling hint/how-to now invites a remembered experience without asking for disclosure.
- Owner art decision, family:dance: replaced the code figure and its small icons with three painted articulated children, one pose plus reverse per child. Engine joints, clock and right-hand scarf attachment remain authoritative; Again rotates the demonstrator independently of feelings.
- Should fix, family:dance, art integration: fixed atlas leakage with explicit SVG clip paths, preserved head proportions, gave the torso a side-profile width and expanded icon bounds to show whole painted heads. Checked five shapes, six moves, three children and reverse/quarter/side views; repaired cards re-shot at 680, 1366 and 1920 widths.
- Should fix, general, voice: Idea, Watch reflection, Freeze, Share and Swap now name the next control or action; manifest and on-screen hints agree with their purpose.
- Polish, general, Share: replaced the generic visual finish with the actual chosen shapes and movement trace inside its existing four observation chips.
## Findings left

- Should fix, general, voice: 44 authored lines have browser speech but no Enceladus recordings. CODEX-BUILD.md Ground rules says "Do not download anything or record audio", so this pass did not record them. Scheduling is verified; bank timbre/classroom loudness is not.
- Polish, family:dance: the exact side-on instant of Swirl remains a narrow articulated illustration. The quarter and reverse views read more naturally; a future side-profile painting could improve that instant.
## Break it

- Empty dance: pressed Watch, Play, Again, Your turn and Go. Play/Again/Go stayed disabled, no clock started, and the hint named Build. Choosing arbitrary valid parts is expressive creation, not a hidden-answer test.
- Counts/run lifecycle: rapid Play/Again/Again/Again/Stop left no running or pending clock, held the cloth unchanged, and emitted no false completion. Counts measure time, never the child's movement or skill. Live edits, Slow and Mirror were also exercised during an actual run.
- Audience observations: tried all four chips before any on-screen performance and repeatedly tapped one. They only annotate observations, with no score, best, win or pass. Five taps spoke five events, stayed selected, and Swap cleared all four.
- Stale success: selected all four observations, changed feeling and middle move, and returned to Share. Before repair all four stayed checked; afterward all four were clear. Parts-first construction now speaks the missing feeling and its eventual Watch it completion.
- Reflection: Watch's question asks what the scarf expressed; it presumes no mistake and has no answer gate. No guessing, elimination, percent or slider shortcut exists.
- 750 combinations, 12,000 sampled count poses: zero nonfinite values. This is sampled pose validation, not 750 real-time performances. Evidence: combinations-result.json, walk/results.json and final-focused frames in Scratch.
## Voice walk

Real held clicks, default Sound on, two-second gaps between Build and mode actions: Happy, Wide star, Middle, Leap, End, Tall tower, Watch it, Play; wait for the run; Your turn, Go; wait through Freeze; Share and four chips with time for their speech. Read __tool.vlog after the walk; repeated after the audit repairs.
Heard in action order: Happy; middle-selection instruction; end-choice instruction as the End row opened; Watch introduction; Watch reflection; Your turn introduction; Freeze reminder after its quiet hold; Share introduction; clear start; middle move; clear end; felt it.
Build's welcome was correctly skipped by the first feeling event. Superseded Build prompts dropped as their action passed. Watch/Your turn introductions each finished without cuts; older Build/result lines cut on explicit mode changes. No narration started over music.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| Watch introduction | how/welcome | 1 | 1 |
| Your turn introduction | how/welcome | 1 | 1 |
| Share introduction | welcome | 1 | 1 |
| Repeated Middle-row how-to | how | 1 in 5 taps | 1 |
| Repeated clear-start observation | event | 5 in 5 taps | 5 |

Read with Sound off and a subsequent mode change used the current hint. Source allLines and voice/lines.json match exactly, 44 unique lines. Chrome was muted; no claim of listening to recorded takes.
## Facts checked

- Beginning/middle/end, movement choices expressing a feeling: [National Core Arts Standards Dance, DA:Cr2 K-2](https://www.nationalartsstandards.org/customize-handbook?discipline=Dance&grade_level=PK-2%2CPK%2CK%2C1st%2C2nd%2C3+-+5%2C3rd%2C4th%2C5th&process=Creating%2CPerforming%2FPresenting%2FProducing%2CResponding%2CConnecting). Children compose the three parts.
- Perform for an audience and link a dance to lived experience: the same NCAS handbook, DA:Pr6 and DA:Cn10. Your turn performs; Share supports observation; Build now makes the life connection on screen. A solo child can use a toy or imagined audience as notes suggest.
- Movement energy, space, time and individual variation: [NDEO, organization of its Early Childhood Standards](https://www.ndeo.org/Learn/Dance-Education-Standards/Early-Childhood-Dance-Standards/How-the-Standards-are-Organized). The six move names are accessible tool labels, not a claim of a complete Laban taxonomy.
- Scarves as creative/sensory props and room for safe movement: [NDEO Opportunity-to-Learn Standards](https://www.ndeo.org/Portals/NDEO/Standards%20Documents/NDEO_Opportunity_to_Learn_Standards_2-22-18%281%29.pdf). Notes retain own-space, seated/small-motion and empty-hand options.
- Gilbert, Anne Green, second edition, 2015: [Human Kinetics publisher catalog](https://www.humankinetics.com/AcuCustom/Sitename/DAM/158/Human_Kinetics_2017_Product_Guide.pdf). Full book pages were unavailable; its specific wording was not independently verified or quoted.
- Counts and tempo, recomputed in Scratch/recompute_numbers.py: 16 = 4+8+4; with four-count introduction, Happy 10.714 s, Sad 18.182 s, Calm 16.667 s, Mad 12 s, Surprised 12.5 s. Slow = 70%, observed Sad 46.2 bpm; slow Sad exceeds 20 s.
- Scarf geometry, spec plus computation: 24 points, 23 segments, each 1.1/23 = 0.047826 engine body units. The spec's 0.046 assumes 24 links; total length stays 1.1. Contrast recomputation: white/brand 7.155, brand/paper 6.713, ink/paper 15.873, muted/paper 6.428; these match spec rounding.
- Music tracks/patterns are original authored choices, checked in trackFor and Dance.music: Happy's claps on 2/4, Calm's triple meter, Mad's stamps on 1/3, Surprised's fourth-count stop. Colors, tempos and suggested moves are not universal facts about feelings.
## Sensitivity

No named cultural tradition, religion or hard history. Bodies are represented: a fresh reviewer should inspect skin/body variation, the right lower-leg prosthesis through turns, articulated low poses and access through seated/small-motion options. People are not assigned to feelings. Keep the invitation to personal meaning optional; a face or movement does not diagnose a child's feelings.
## Flattest moment left

The first Your turn setup waits for its spoken instruction to finish. That time lets the class find its start shape, but it is still the least active screen moment. The final audience discussion is strongest with a partner; personalized pose chips now give it something specific to discuss.
## Graphics

Preserved hilltop and silk. Generated one dancers-rig atlas with the built-in imagegen tool; people:true and drawn_by:codex. Full prompt, cast and registration are in art/prompts.json; source PNG is art/raw/dancers-rig.png; processed WebP is art/dancers-rig.webp. Three children, six front/reverse tiles replace eleven proposed separate pose assets; prior plan preserved in Scratch. Engine motion and scarf remain live code.
Inspected the art in actual scenes, all moves/shapes, grayscale, Motion off, phone and all eight STANDARDS sizes. Beat Lab and Snowy Mail Route were opened without modifying their folders; final comparison is in Scratch. Bundle: 702,164 bytes, about 686 KiB; all art tokens resolve. No art still to paint.
## Audit

One audit completed within its 40-minute limit on Chrome 9941, host 8745. Its 44 frames were opened. It reported 20 mechanical leads: 16 suppressed first-tap welcomes (correct replacement by an action's line or incomplete-dance guidance under STANDARDS); one obsolete Start prompt after Feeling idea (correct stale drop); one hint under the native modal backdrop (legible, intentionally inert; modal Read speaks it); two phone-host context/hint failures (harness coverage failure).
Seven desktop sizes, Motion off, resize stress, held-control/keyboard checks and sampled repeated/quick taps were mechanically clean otherwise. Automatic mode discovery saw zero kit-header modes; eight explicit audit states and manual four-mode runs supplied coverage. The actual 375x812 iframe was separately driven through all four modes plus its editor, then rechecked after repairs, with zero errors.
Frame inspection confirmed clipped painted icon heads; fixed and re-shot. Audit voice inspection led to clearer next-control lines, then the stale-observation and parts-first repairs above. Only those paths, their affected frames, rapid run cancellation and the main voice walk were repeated afterward, with zero errors. No second full audit. Evidence: review-audit/audit.md, audit-repair/, walk/results.json, phone/ and verification-summary.json in Scratch.
## Left open

- Recorded voice and the narrow side-profile polish above. Fresh people/sensitivity review remains part of the normal release workflow.
- Full Gilbert page-level attribution was unavailable; official NCAS/NDEO sources independently support the actual teaching claims.
- Shared dance.md table/platform/Motion-persistence suggestions remain in handoff.md because this run cannot edit shared files.
- No questions were asked in this unattended run. Kept the spec's three silent Freeze seconds before its spoken reminder; used an articulated atlas to minimize poses; interpreted observation chips as teacher annotations.
- No git commits. Writes confined to tools/feeling-scarf-dance/ and _scratch/feeling-scarf-dance/.
