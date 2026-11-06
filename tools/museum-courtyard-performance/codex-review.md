# Codex review: museum-courtyard-performance
## Played
Cold grade 9-12 play before builder reports or source: Site, seat inset, Week bookings, six weeks, complete show and program sheet.
Then walked the default rehearsal path with voice and tested budget/floor plans, injury, rain, empty weeks, keyboard and projector views.
It feels like a production desk with real tradeoffs; the audience comparison is its strongest idea. Kept the limestone world and twelve-card board.
Evidence below is relative to `_scratch/museum-courtyard-performance/`. Review stays one pass, with targeted rechecks.
## Findings fixed
- **Blocker, general, weekLoad:** center-only floor credit let landings beyond a sprung edge claim load 72. Checks all six planned landings, hardest surface wins. Same real arrow-key exploit now returns 216 (`review-before/`, `review-after/`).
- **Should fix, general, load preview:** green low load could read as medical clearance. Labels now say model; visible advice distinguishes grip, cushioning and warm-up. Fictional numerical rules stay intact.
- **Should fix, general, narration:** soreness delayed the first injury announcement until it could go stale. Injury now starts first and includes its two-sore-week cause. Seat view and rehearsal booking speak their current how-to once.
- **Should fix, general, dialog speech:** leaving the sheet let the old event occupy speech; repeated openings lost one event. Sheet entry/exit now stop stale speech; five openings produce five events.
- **Should fix, family:dance, graphics:** temporary same-body code figures and unsupported floating lifts. Painted six varied dancers in five essential poses, plus supported pair lifts; all assets people:true. A small adapter keeps the cast swappable.
- **Should fix, general, pathway:** arcade weaving passed through column centers. The pathway bends around their coordinates.
- **Should fix, general, small screens:** gave phone status an extra row and restored keyboard-accessible opening-night seat menus in the scrolling secondary panel.
- **Should fix, general, compact Week:** the load estimate was below the fold. Plan and load now share the top row; all four section choices remain visible, and historical reports replace disabled rehearsal inputs.
- **Should fix, general, pointer stability:** opening Seat view moved its own button. Site actions are anchored after the secondary controls; exact before/open/close positions match in the targeted laptop and compact tests.
- **Should fix, general, duplicate state:** a Site map seat tap moved the camera but left its seat menu stale. The menu now follows the rendered viewpoint; a real row-three tap confirmed menu g40 and the row-three caption in the same pointer event.
- **Should fix, family:dance, cast assignment:** the sixth painted person always rested after injury. The rest slot is now selected independently of appearance; lifts use two complete remaining pairs. All six rest cases still show five people.
- **Polish, general, flat show:** live audience-average receipts now connect the performance to Seen, Heard and Lit. The sheet leads with this production's most limited view. Figures have more space to read.
- **Should fix, general, source credits:** the brief's precise IADMS Dance Floors title could not be verified. Public flooring credit now names the directly checked Ausdance guidance; notes preserve the source uncertainty.
## Findings left
- **Should fix, specification:** spray examples and sunset chronology are inconsistent with the spec's own rule/times. Computed geometry and the required scripted light model remain; notes name both conflicts. See Left open.
- **Polish:** painted people are three-quarter billboards, with discrete key poses, rather than articulated rear views. Deliberate few-pose compromise, documented for swapping.
- **Polish:** the requested narrator timbre and final music mix need listening with headphones. No recordings were made under the build rules; browser speech remains the fallback.
## Break it
- **Budget / crew / one-time cards:** spammed purchases, spent exactly 10 h, attempted unaffordable additions, then changed weeks. No overspend, negative money or repeat purchase; $300 remained in the tested $2,700 floor plan.
- **Adaptation dots / undo:** booked and unbooked repeatedly, ended, undid and ended again. Only actual rehearsals earn dots; undo removes the previous result and spending. Six empty weeks unlock a low-readiness sheet, with no score or success badge.
- **Load / injury:** slid Rise's center onto a panel edge with a real key. Exploit blocked after repair. Full stone 216, warm stone 172.8, half stone 108, marley 144 / 115.2 warm, sprung 72, marked stone 64.8. Two sore weeks injure; undo reverses the injury.
- **Rain:** tried no backup, backup, Rise first and Rise second. No backup gives zero dots/load; backup gives one dot, only the first section. Rise-first lobby full-jump load is 72; Rise-second is zero.
- **Seen / Heard / Lit / patterns / site use:** swept Pool adaptations and fountain modes, tested risers, lamps and unadapted spacing. Independent rays and all six sound-table cases agree. Open-floor Columns cannot claim weaving; running-only water cannot claim score use.
- These are exposed planning consequences, not a hidden-answer quiz: moving a zone to a better view is the intended skill, not a sweep-to-win gate. No best score or reflection gate exists.
- `review-functional.json`: 45 assertions passed; adversarial real-input paths in `review-after/` have zero console errors.
## Voice walk
Final main path: real zone drag, Seat view, Plan week, default rehearsal selection, End week/current week through six Mondays, Opening night, Begin, all forty seconds, sheet.
Held clicks 0.12 s, gaps 2 s, default sound/motion. Heard order (`review-main-voice-final.json`):
`seatHow`, `chooseSeat`, `welcomeWeek`, `rehearsalHow`, `sore`, `injured`, `sore`, `sore`, `sore`, `rain`, `welcomeNight`.
The drag's first-tap instruction may replace the Site welcome under BASELINE 16; the welcome remains in hint/Read. No mode how-to is lost.
Later report-only how lines drop when the student has already opened another week, as required. Injury is heard before that transition.

| Line / kind | Expected | Spoken |
|---|---:|---:|
| Week welcome / how, five weeks | 1 | 1 |
| Rehearsal / how, five bookings | 1 | 1 |
| Seat selection / how, repeated toggles | 1 | 1 |
| Five sore-week results | 5 total | 4 sore + 1 injury/cause |
| New injury / event | 1 | 1 |
| Rain / event, main path | 1 | 1 |
| Site use / event, five sheet openings | 5 | 5 |

Read interrupted speech, worked with Sound off, and mode changes released it. Fourteen source lines match fourteen manifest lines exactly.
Main show reached position 64 and saved showFinished:true; injured lift frame contains five people, including the two-person painted pair.
The mid-show real seat tap updated its caption inside the same pointer event while running; real Skip and Stop then acted immediately (`review-midshow-seat.json`).
## Facts checked
- **Venue dimensions, seats, piece, prices, crew, weather and all percentages/load rules:** fictional spec Content/Model, explicitly labeled. Independent `review-numbers.json`: all purchases $6,300 / 45 h; sample $2,900 / 25 h; 49 ellipse samples; 60 ground / 40 balcony seats.
- **Sightlines:** own independent 60-seat rays against the specified 0.3 m columns and 1.5 m spray. Arcade 78.50%; balcony 100%, 59.18%, 26.53%. Behind spray 33.54%, not printed 37%; (10,8) 83.13% with spray / 97.96% without.
- **Surface grip versus shock absorption and hard-floor caution:** [Ausdance National, Safe dance floors](https://ausdance.org.au/articles/details/safe-dance-floors), live checked 2026-11-06. Fictional floor multipliers do not imply measured cushioning.
- **Warm-up/cool-down preparation, authors and date:** [Human Kinetics, Safe Dance Practice](https://us.humankinetics.com/products/safe-dance-practice) and [publisher excerpt](https://us.humankinetics.com/blogs/excerpt/structure-and-content-of-individual-dance-sessions), Quin, Rafferty, Tomlinson, 2015. No guidance supports the invented 20% reduction or 120 threshold; these remain clearly identified model choices.
- **Site-specific form and credit:** [Kloetzel and Pavlik, Site Dance, 2009](https://doi.org/10.5744/florida/9780813034003.001.0001), publisher-hosted record. Original Water Over Stone is credited to Curio Class, not represented as a traditional dance.
- **Standards:** [NCAS Dance performing standards](https://www.nationalartsstandards.org/customize-handbook). Students adapt levels/pathways (Pr4), compare rehearsal/floors/load (Pr5), and allocate sound, light and audience production (Pr6). The simulator does not assess physical technique.
- **Contrast:** independent WCAG computation gives brand/paper 5.34:1, white/brand 6.12:1, ink/paper 14.01:1, muted/paper 5.98:1.
## Sensitivity
Bodies and injury require fresh sensitivity review. Check that the cast's skin tones, apparent ages and body shapes read naturally, the supported lifts remain clear, and injury is treated as care rather than a score penalty. No named cultural tradition is represented.
All people images are tagged people:true; the contact sheet is `review-art-contact.jpg`. Check partner-lift role assignments as well as cast variety. No actual disability, health or dance competence is inferred from appearance. Images are illustrative, not a lift tutorial.
## Flattest moment left
Late quiet weeks can be short if the production is already planned. The spec explicitly permits quiet weeks; no extra event or topic was invented. The lifted show now gives an immediate audience comparison and a specific final result.
## Graphics
Kept all nine architectural paintings; inspected every finished asset, both painted atlases, cutouts on a contrasting sheet, and final-size ground/balcony poses. Added 30 individual pose cells plus three paired lifts in two swappable assets, not 33 separate files.
Eleven WebPs total 589,396 bytes. Final bundle: 1,379,345 bytes (1,347.0 KiB). Artwork, source and voice are embedded; no tool network references. Original limestone palette and layered production board remain.
Compared fresh Beat Lab and Snowy Mail Route frames; `review-painted/`, `review-phone/`, `review-after/`, `review-checks/` and contact sheets hold the targeted evidence. Keyboard-only plan movement, grayscale and calm frames were opened and inspected.
## Audit
Completed once in 1,670.98 s (27 min 51 s), exit 0, under the 2,400 s cap. Chrome 9961, host 8765; 52 saved frames opened through contact sheets 00-08. No full audit repeated.
All 25 reported leads are accounted for:
- Ten map/warning/instruction overlaps and two inset-caption overlaps are intentional nonblocking labels on the canvas; inspected at each reported size.
- Two phone leads came from a failed iframe attachment, not a missing tool hint. Leftover localhost helpers may have interfered. Targeted 375 iframe checks covered Site, seat inset, Week booking/report, Opening night and sheet: no small targets, page overflow, clipped text or console errors.
- One grouped Opening night focus lead clicks the locked fresh-page tab. The unlocked six-week route, Begin, Stop, Skip and seat controls were tested separately.
- Three Model-dialog background/keep leads and one sheet keep lead are deliberate modal coverage of the inactive background.
- Four receipt keep leads are hit-testing artifacts from passive overlays; the audience receipts are visibly present in both views at 680 and 1366.
- Two first-tap welcome leads are permitted by BASELINE 16: Seat view speaks its own action; Model opens its text. The premise remains in Site hint/Read.
The frame review additionally found the compact load/report fold fault and the Site action-button shift. Fixed and re-shot only those layouts. Phone sideways action cards follow the explicit spec; keyboard focus deliberately scrolls secondary night seat menus into view.
Motion off, held-click focus/Enter, five repeats, quick taps and resize recovery were clean. Final targeted frame/measurement files are `review-post-audit/`, `review-extra-checks/` and `review-final-phone-status/`.
Final socket preflight found four orphan host children from this review. Their exact tool/port command lines were verified and all four closed; no unrelated process was stopped. Evidence: `review-owned-processes.json` and final validation.
Done when: layout, spending/undo, injury/load, rain, forty-second show and sheet checks pass. Printed sightline examples remain a spec discrepancy. The injury event combines its sore-week cause. The owner's painted-people direction overrides the old no-people art item.
## Left open
- Correct the spec's spray worked examples and dusk timetable. Six minutes starting thirty before sunset ends twenty-four before sunset, not after dusk. The required scripted dusk rule is retained, with the conflict visible in teacher notes.
- Exact IADMS Dance Floors paper/title was not located; old IADMS media URLs redirect. Checked public flooring credit uses Ausdance instead.
- Unattended choices retain the brief's direction: 0.75 m assumed basin radius, later-week warm-up, 75% kneeling factor, first-selected lobby section and inherited sprung-lobby assumption. None is presented as a real venue rule.
- Headphone listening, named recorded timbre and the fresh sensitivity/owner people contact-sheet review remain pre-publication work. No outside contact, upload, commit or shared-file change was made.

Final cleanup: all assigned Chrome/host ports closed, temporary host removed, source lines at most 160 characters. No commits.
