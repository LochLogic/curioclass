# Codex review: safety-sweep-house

## Played
Cold full-house play as a grade 4 student, before reading the builder's report, handoff, notes or source. Inviting search, useful consequences, satisfying final lamps; the repeated decision cards are the slowest stretch.
Then walked the teaching, play and craft lenses, including projection-size frames, all six look-alikes and twelve physical fixes. No commits or shared source edits.

## Findings fixed
- **Blocker, general, chat controls:** Block and Report inherited white text on white buttons. Explicit ink color makes both readable; `review-matrix/review-chat-contrast.png`.
- **Blocker, general, heater ruler:** the picture included an unmoved second blanket and its zero did not mark the heater edge. A separate heater and blanket now share the ruler's geometry; distance measures the nearest blanket edge. Display rounds down, so 2.999 feet cannot read as three. `review-targets/heater-final-680.png` and `heater-final-1366.png`.
- **Blocker, general, backyard art:** a baked-open gate stayed visible behind the repaired gate. Redrew the backdrop without gate leaves and aligned the changing gate across its opening; full-size and phone fixed-room frames checked.
- **Should fix, general, Read:** Think explanations, reflection reasons, half the wide Safety card and its emergency instructions were omitted. Read now follows the visible card and includes both emergency instructions; wide-card log contains all twelve habits.
- **Should fix, general, voice:** room navigation could hush the completion line; a delayed welcome could start over a look-alike card. Preserve room completion, constrain the welcome, and validate state-specific narration. Repeated the main and side paths.
- **Should fix, general, card reopening:** a click Event was treated as the `earned` argument and replayed the house-completion announcement. Wrap the handler; reopening now uses only the emergency how-to, once heard.
- **Should fix, general, online room:** inline message plaques overpainted wrapped lines. Block layout and bounded type now keep the messages distinct at 680 and 375 widths.
- **Should fix, general, scene fixes:** moving a bucket or cooled towel could leave another copy in the scene. Removed the duplicate during the action. The Think explanation now explicitly distinguishes moving a cool blanket from touching the heater.
- **Should fix, general, reset dialog:** underlying room controls remained active, and Escape lost focus. Make background content inert while confirming and restore focus to Sweep again.
- **Should fix, general, audit layout:** moved compact Rooms navigation into the header; separated the kitchen pot/towel hit areas; made the portrait Safety card a viewport overlay with inactive background content. These address below-fold controls and overlapping targets without shrinking the art.
- **Polish, general, weakest art:** redrew the magenta-stained cleaner cutout and the look-alike pot that included a miniature stove. Preserved the painted style; improved alarm and block-bin keying.
- **Polish, general, flattest action:** tap-target fixes jumped straight to the finished painting. They now show the object traveling to the target, with immediate feedback and live next controls. Motion off swaps directly and clears any flight in progress.

## Findings left
- **Nit, general:** some furniture cutouts retain a slightly different perspective from the room painting. Kept their texture and detail; no additional restyling pass.
- Browser speech remains the kit fallback. No recording was made because CODEX-BUILD.md forbids recording audio; the intended friendly-dad delivery is not an authored clip yet.

## Break it
`review-break/checks.json`: 145 checks passed with held real clicks, jittered drags and keys, including a complete twelve-case run and reset. The reviewed input script was reused as a baseline, then extended; its old PASS was not accepted as evidence.
- Room count: opening rooms, tapping look-alikes and peeking never lights a room. Both hazards need safe choice, action, adult contact and reflection completion. No score, accuracy badge, saved best or timer exists.
- Think: picked the wrong help answer first in all twelve cases. It corrects the answer before Choose, with no accuracy reward. Six adult-first and six act-then-tell cases confirmed.
- Choose: peeked all cards, tried both unsafe options, and tried fixed-index choices. Unsafe choices never expose Check; safe picks show all three outcomes. Safe positions are 4/4/4. Every-option exploration is explicitly permitted by the unscored spec.
- Adult-first fixes: attempted progression before Tell. No actionable object or hold control is available until the adult arrives.
- Move fixes: target alone does nothing; real drags and select-then-target work. Action without the required Tell still cannot complete.
- Candle and alarm: four short holds do not accumulate; one continuous one- or two-second hold works. Leaving the step cancels a hold.
- Heater: Enter at one foot, 2.5 feet and 2.999 feet fails; three feet succeeds. Nearest-edge geometry, six-inch keys, singular foot and conservative display checked at 680 and 1366.
- Chat: Report before Block fails. Block, Report and Tell are required in order. Pop-up needs Close and Tell.
- Reflection: Done starts disabled. Always Everyone or any single person still reveals the actual safer set and reason, as the spec requires; it makes no claim of correct independent mastery.
- Reset: No keeps the completed house, Yes clears it; Escape returns focus. Leaving and returning preserves the unfinished decision.
- Keyboard-only real key sequence completed the entire cleaner case; `review-keyboard-complete.json` records done:true. Grayscale retains words and symbols; calm frames retain meaningful states.

## Voice walk
Default Sound on, 120 ms held clicks, two-second gaps: Kitchen, cleaners Stop, Think, Choose, peek, unsafe pick, safe pick, Check, move, Tell, reflection; repeat for towel, House, next room.
Started in order: roomIn, stop, think, choose, tried, safe, fix, who, safe, roomDone. The second case's how-to lines are hint-only. Room completion was not cut during the House/next-room transition.
Game-room side path: Read, roomIn, lookalike, stop, think, choose, safe, fix, who. Read with Sound off speaks the current explanation; leaving clears stale speech.
Finale: roomIn, stop, think, choose, safe, fix, who, houseDone, poison. The last two finish uncut; queue empty. Eleven cases were precompleted for this timing fixture, after the separate complete input run.
At a two-second pace some earlier instructions are cut when the student advances; the logs disclose this. No unstarted required step was lost, no instruction later names an old state, and Read remains available.

| Line / kind | Expected starts | Observed |
|---|---:|---:|
| stop, think, choose, fix, who / how, two hazards | 1 each | 1 each |
| safe / event, two hazards | 2 | 2 |
| lookalike / how, five visits | 1 | 1 |
| tried / event, five unsafe taps in one hazard | 1 by spec | 1 |
| houseDone and poison / earned finale | 1 each, whole | 1 each, whole |

## Facts checked
Checked current named guidance on 2026-11-06, independently of the builder's source claims.
- Decision and practice indicators 5.5.1-5 and 7.5.1-2: [SHAPE America, NHES 2024](https://shapeamerica.org/standards/health/new-he-standards/). Each is exercised by search, help decision, comparison, choice, reflection or scene action.
- Never mix cleaners; bleach plus ammonia produces irritating gases and breathing symptoms: [Washington DOH](https://doh.wa.gov/community-and-environment/contaminants/bleach-mixing-dangers) and [CDC cleaning guidance](https://www.cdc.gov/hygiene/about/cleaning-and-disinfecting-with-bleach.html). Outdoor mixing still producing gas follows the same reaction; it is not a safe exception.
- Medicine, vitamins and gummies belong above children's reach and out of sight; excess ingestion can harm children: [CDC Up and Away](https://www.cdc.gov/medication-safety/php/toolkit/index.html). Medicine is given by a grown-up, not sampled as candy.
- Child-resistant caps are not childproof: [National Capital Poison Center, prevention card](https://www.poison.org/-/media/files/poisonorg/public-ed-materials/pdfs/tip-card-to-prevent-poisonings-in-children.pdf).
- Towel/heat/fire-spread risks, staying with cooking and pot handles toward the back: [USFA cooking safety](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/cooking/) and [USFA home safety handout](https://www.usfa.fema.gov/downloads/pdf/publications/home-fire-safety-poster-brochure.pdf).
- Candle separation of one foot, extinguishing when leaving, and flameless alternatives: [USFA candle safety](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/candle/).
- Missing battery prevents this alarm's warning; monthly Test-button check: [USFA smoke alarms](https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/smoke-alarms/). No universal battery replacement interval is taught.
- Three-foot clearance from things that burn: [USFA heating safety](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/heating/). Three feet equals 36 inches; the keyboard moves six inches per press.
- Two exits per room and an outside meeting place: [USFA escape planning](https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/home-fire-escape-plans/).
- Shallow-water drowning can be quick and silent; empty unused tubs and keep young children supervised: [CPSC in-home drowning](https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/In-Home-Drowning-Safety-Information-Center) and [AAP bathroom safety](https://www.healthychildren.org/English/safety-prevention/at-home/pages/Bathroom-Safety.aspx).
- Pool barriers need self-closing, self-latching gates; do not prop them open: [CPSC Pool Safely](https://www.poolsafely.gov/parents/safety-tips/) and its [barrier guidance](https://www.poolsafely.gov/wp-content/uploads/2023/05/Safety-Barrier-Guidelines-Pub-362_0423.pdf).
- Children leave matches/lighters alone and tell an adult: [USFA youth fire safety](https://www.usfa.fema.gov/prevention/arson/prevent-youth-firesetting/) and [Utah State Fire Marshal](https://firemarshal.utah.gov/services/cigarette-fire-safety/match-and-lighter-safety/).
- Protect school/contact details; block/report unwanted game contact and involve a trusted grown-up: [FTC kids and video games](https://consumer.ftc.gov/articles/kids-and-video-games).
- Prize/password pop-ups can steal account access; close without entering details: [FTC phishing guidance](https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams). The tool's password claim is about the unsolicited prize message in this scene.
- Poison Help 1-800-222-1222, US, free and available at any time: [HRSA](https://poisonhelp.hrsa.gov/faq/calling-poison-help) and [National Capital Poison Center](https://www.poison.org/need-immediate-assistance).
- Fire: leave, stay out, then call 911 outside: [American Red Cross](https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/fire/if-a-fire-starts.html) and USFA escape guidance above.
- The six look-alike explanations use the corresponding guidance above. Maya's identity and the family are fictional premises; Theo's benefit never assumes that all young children cannot swim.
- Recomputed all twelve contrast ratios, minimum 4.67:1; safe positions 4/4/4, help 6/6, beneficiary sets 6/4/2. The full tap-target/keyboard route is 155 inputs, not the spec's 72: 72 decisions + 36 fixing/help inputs + 36 reflection inputs + 11 room-navigation inputs.

## Sensitivity
No cultural tradition, religion or hard history is represented. Fire, poisoning, drowning and online solicitation may connect with lived trauma; notes and plan retain school disclosure procedures and never ask for a child's experience.
Reviewed all five marked people assets: fully clothed Theo, warm Dad and Grandma June, natural skin tones and ages, no mocking or stereotyped roles. A later reviewer should check the small Theo age/identity variation and avoid treating this family structure as universal.

## Flattest moment left
The later Think cards repeat the same decision framework. The spec deliberately asks for that practice; shortening it or adding a new game would change scope. The moving fixes, alarm hold and ordered online actions now provide the variation.

## Graphics
46 images checked on four contact sheets and room/action frames. Three redraws: cleaner group, backyard backdrop and isolated pot; alarm and block-bin key cleanup. No missing art tokens. People flags preserved.
Finished art about 1603 KB; offline bundle about 2231 KB. Rich backgrounds, material detail, family, porch glow and lamp payoff retained. Compared the existing Snowy Mail Route and Beat Lab reference frames; no plain substitute art introduced.
Opened all review PNGs from cold-frames, cold-play, review-break, review-matrix, review-voice, review-targets and review-last. Size matrix: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and a real 375x812 iframe.

## Audit
Completed once with the required 40-minute limit, port 9961 and host 8765. `review-audit/audit.md` contains 27 lead rows on the audited bundle. Confirmed three root causes: kitchen target overlap, compact Rooms navigation below the fold, and phone Safety-card controls below the fold. Fixed all three and re-shot the affected room state at all eight sizes plus narrow Safe, Who and Safety-card states. Scoped checks show zero pot/towel intersection, visible header navigation and all three Safety-card buttons inside the phone viewport.
Two background-label occlusion rows are intentional card overlay, not missing teaching text; background content is now inert. The late welcome rows are permitted by the one-mode `welcomeAfter` spec. Console, focus, Motion off, held-click/Read stress and mid-action resize checks passed. The full audit was not repeated after repairs, as required by the one-pass brief.

## Left open
No confirmed blocker or should-fix remains open. Audit lead resolutions and scoped frames are preserved in Scratch.
No publishing, outreach, recording, commits or engine changes. Voice listening quality and authored friendly-dad recordings remain outside this recording-prohibited pass.
Unattended choices followed the spec: unscored correction and exploration, six/six help split, short-landscape side-by-side layout, and the existing family. The spec was left unchanged.
