# Polish: moon-base-drama (Codex fix, round 1)

Evidence paths are relative to `_scratch/moon-base-drama/`. Claimed frames were inspected. The reported rewind bug is repaired, but the prescribed option wording still permits a longest-text shortcut. Under the user's stronger no-skill-pass rule, the meter blocker is conservatively NOT FIXED. No questions were asked in this unattended session; scope decisions preserve the spec and settled calls.

## Blocker

1. **NOT FIXED under the additional no-skill-pass condition; the reported rewind corruption is repaired.** Before: `fix-before/double-rewind.png`, `back-rewind.png`, `skip-to-warmth.png` and their `before-*.json` files show visited 8 at beat 3, every target enabled, and an invalid 1,1,3 ending under three live-looking old icons. Invalidation now drops the frontier; eligibility and the rewind handler both require a genuinely past/current-chosen node; old icons fade independently of beat position. After: matching `fix-after/` frames show frontier 3, meters 1,1,1, and all targets disabled on unanswered Batteries. Back plus Rewind, three initial targets, repeated earlier rewinds, and Next spam are checked in `fix-cheats.json` and `fix-exploits.json`. None skips a required choice. Longest-text selection still fills resources 8/8, however. See Cheats tried and Left open.

## Should fix

1. **FIXED.** Before `fix-before/choice-read.png` and `before-choice-read.json` read the Batteries fact alone. Mission Control now voices the fact and both crew lines in displayed order on choice entry, Read, Radio again and Rewind. `fix-read-choices.json` checks 3 beats x 2 orders, 6/6 matching the buttons. Held-click main/side logs start every named transmission. `fix-after/choice-read.png` shows its Read caption. Ada's questions/reactions remain excluded; runtime and manifest contain the same 93 lines.
2. **FIXED for the picture defect.** Before `fix-before/night-000.png`, `night-010.png`, `night-111.png` show the same thriving background and squashed foreground. After `fix-paths/path-000.png`, `path-001.png`, `path-010.png`, `path-100.png`, `path-111.png` distinguish healthy, cold, thirsty and dark states at 1366x768. Leaves hang from bent stems, with shaded yellow blades and veins; cold alone has green drooping leaves and blue frost. Final Motion-off frames `fix-night-final/path-000.png`, `path-100.png`, `path-111.png` show immediate states: Light 3 versus 1 gives background brightness 0.90 versus 0.56 and saturation 0.85 versus 0.45; low Water lowers it further to 0.099 plus sepia; cold overlay is 0.8 versus 0. All eight meters/endings match independent arithmetic in `fix-path-validation.json`. The shared longest-text shortcut is not claimed fixed.
3. **FIXED.** Before: `fix-before/warm-680.png`, the 1366 map frames, `fix-before-phone/phone-map.png`. Six shared SVGs replace the battery/sun, moon, ice, wave, blanket and door glyphs in buttons, diamonds and Rewind. After: `fix-checks/warm-680.png`, `rewind-680.png`, `fix-after/double-rewind.png`, `fix-phone/phone-map.png`, `phone-warm.png` at 680x425, 1366x768 and a true 375x812 iframe. Map SVGs are 15x15. Choice icons and map dots are decorative; the path has list/listitem roles and accessible choice/rewind names carry the words.
4. **FIXED.** `before-job-first-sound.json` has only the job event after badge, Sound off/on and Crew re-entry. `after-job-first-sound.json` recovers the valid premise once. `fix-premise-at-start.json`, `fix-mission-first.json`, and `fix-main-voice.json` carry it into Start mission on badge-first and Mission-first routes. Frames: `fix-final/mission-final.png`, `fix-phone/phone-intro.png`. Crew Read also includes the premise without the stale badge instruction.
5. **FIXED.** Actual Audio fixture before: `before-clip-read.json`, glow false and stale caption. After: `after-clip-read.json`, glow true with exact Read text during playback and false after its 3-second clip completes. `fix-clip-event.json` proves the same event lifecycle. `fix-clip-interrupted.json` proves Sound-off Read stops on Motion and leaves glow false. Events follow V.playing; a small Read adapter follows the actual completion promise of kit playback, without an estimated glow timer. Silent WAV fixtures exercise clip control flow; no narration was recorded. Frames: `fix-final/`.

## Polish accepted

1. **FIXED.** All three ending transmissions speak the story first, then their first reflection instruction, naming New mission or Rewind. `fix-paths/path-000.png`, `path-010.png`, `path-111.png` and the two held-click logs prove the order. Later endings omit the repeated how-to.
2. **FIXED.** Shared choice content says "Wrap the greenhouse in a blanket" in the button, accessible map/rewind name and spoken options. `fix-checks/warm-680.png`, `fix-phone/phone-warm.png`, `fix-read-choices.json`.
3. **FIXED.** `fix-six-reactions.json` records all 6 distinct in-role card reactions after their results. None enters runtime allLines or the voice manifest.
4. **FIXED.** A revisited unanswered choice adds "Say the new line in your own words. What will you tell me?" on Ada's card, unspoken. `fix-checks/rewind-680.png`, `fix-after/double-rewind.png`, `fix-phone/phone-rewind.png`, `fix-exploits.json`. Choosing replaces it with the result reaction.
5. **FIXED.** Notes explicitly name the three responding asks: choose a job prop, explain how the crew met the Moon problems, and judge which choice mattered with a reason. Talk about it includes the doors question. The revision invitation is also explained.
6. **FIXED.** Dialog return and corresponding fixed narration say "Back to the story". `fix-after/double-rewind.png`, `fix-phone/phone-map.png`; the phone label fits its 60 px target.
7. **FIXED.** `fix-after/crew-1920.png` and `fix-crew-spacing.json` at 1920x1080 show a 15 px prop/label gap and 14 px subtitle/badge gap. The grid starts lower; props retain label space while selected.

## Settled calls

- Mission Control voices the crew options, never Ada. The broader solo-role question and Warmth B rewrite remain untouched.
- Ending pictures are stronger. How-to-before-story stays on beats 2 to 7; only endings change order.
- Immediate interruption, replayable job events and card/Motion interruption remain. Moon fact wording and all eight resource rules are unchanged.
- No new assessment, paid generation, uploads, commits or shared-file changes. Only the named tool and Scratch were written. `refine.md` and `refine/` were untouched.

## Cheats tried

- Rewind Batteries, then try Water/Warmth without a new Batteries choice: formerly reached the invalid 1,1,3 ending; now blocked by eligibility and handler guards. Current unanswered Batteries is disabled too. Before/after rewind frames and JSONs prove it.
- Back from the ending to Batteries, then Rewind to any choice, or spam Next: remains blocked on the unanswered choice. `fix-cheats.json`, `fix-exploits.json`.
- Start a rewind at each of 3,4,6, then attempt later and earlier targets. Later skips fail; earlier targets restore and reduce the frontier again. First restored meters are 1,1,1; 3,1,1; 3,3,1. `fix-exploits.json`.
- Repeat the poor choice 10 times and alternate both buttons 10 times at each choice. Resources remain 1,1,1; 1,2,1; 1,2,1, never stack, and the other committed choice asks for Rewind. `fix-cheats.json`.
- Always left across all 8 shuffle configurations: full ending 1/8. Every meter matches the semantic choice. `fix-exploits.json`.
- **NOT FIXED: always choose the longest line without Moon science.** Full ending 8/8 across shuffle configurations. This is not learning evidence. The spec prescribes those lines and a revisable story with no mastery assessment; settled calls retain the content/resource rules. I did not add an assessment gate or rewrite choices beyond this Refine. This is why the meter blocker is not certified FIXED under the user's stronger condition.
- Badges assign replayable crew roles, not scores. No saved/best score, reward or mastery claim was added. Read and rewind openly provide teaching content as specified.

## Voice walk

- Held 120 ms presses, 2 s gaps, default Sound: ready + Plant Keeper; premise + long night; next + greenhouse; choose + solar fact/options; Batteries A; water fact/options; Water A; lift ice; warmth fact/options; Warmth A; dust; full ending + reflection. All 12 transmissions start in order; each how-to starts once. `fix-main-voice.json`.
- Side path: corresponding B results; low ending + reflection; map; old story + warmth rewind + fact/options; Warmth A; dust; low ending without repeated reflection. All 17 transmissions start in order. `fix-side-voice.json`.
- Separate premise recovery and six Read-order cases pass. No Ada question, reaction or own-words invitation appears in the 93-line runtime/manifest set. Exact equality checked with `fix-final-lines.json`.
- A spoken log means the kit started the transmission; a subsequent tap may cut it, as Done when 5 requires. Browser voice quality is not certified. Actual clip control flow was tested with silent fixtures.

## Engine changes wanted

- Existing: `kit/curio.js`, init Motion handler, optional memory-only preferences for literal no-storage tools.
- Optional: `kit/curio.js`, voice/read and speakOne, expose native Read's text and completion/playback callbacks for Audio and speech. That removes the local Read adapter; the current tool already follows kit playback completion.
- Existing audit issue: `scripts/audit_tool.py`, size iframe context discovery, add a same-origin iframe-window fallback. Separate actual phone-host checks succeeded. No shared source was changed.

## Audit

Completed once, exit 0, within the 2400-second cap, Chrome 9911 and host 8715. Evidence: `fix-audit/audit.md`, `fix-audit-console.log`. All 68 audit frames were inspected. The audit was not repeated.

- **2 phone-probe leads:** iframe context discovery failed and therefore could not find the hint. Separate true 375x812 host frames in `fix-phone/` verify map, Warmth, revision, night and the long introduction; radio/card gap is 14 px and card/choice gap is 22 px in both choice states. Read speaks the actual context. Shared audit change is listed under Engine changes wanted.
- **1 real layout lead, FIXED:** the long Warmth rewind caption covered 3/9 choice sample points at 1366x768. Before: `fix-audit/state-warmth-revision-1366x768.png`. All choice layouts now reserve actual radio height. After: `fix-audit-followup/warmth-revision-1366.png` and `warmth-revision-680.png`; respective gaps 14 and 9 px, both centers unobstructed, full words visible. Coupled widths 1280, 1920 and 760 also have 14 px gaps and unobstructed centers. The matching `fix-warmth-revision-*-followup.json` files retain the numbers.
- **7 first-tap welcome leads:** Mission and the six job badges intentionally speak their own first action. The premise recovers at Start mission, Sound on or Crew re-entry, verified by the focused premise logs and main/side paths. No late, stale job-badge welcome was added.
- **9 quick-tap leads:** Crew, Mission, Motion and six job badges cut the preceding transmission. This is required by Done when 5 and the settled calls. Job events replay; their first combined how-to need not repeat. The five-held-click checks are clean for all 10 tested speaking controls, and Read is clean on quick taps.
- Final resize stress is clean: no exceptions or controls left disabled. The automatic Mission walk cannot enter without a job; the separate real-input paths supply Mission coverage.
- The audit snapshot predates the targeted spacing follow-up and an accessibility correction found during frame review: ordinary past nodes now say visited, rather than future/old. The final follow-up records all eight labels accurately. This changes no story resources or narration. The final default Crew and actual Mission were also re-shot at 1366x768 in `fix-audit-followup/`.

## Left open

- Longest-choice shortcut. A full greenhouse cannot certify science understanding. Resolving the stronger condition needs a content/assessment decision outside this Refine's permitted scope.
- Both spec open questions remain untouched. Recording narration and shared Motion storage remain at their existing later-stage/engine boundaries.
- Corrected Scratch test errors: selector quoting in two voice shots and a duplicate local declaration in the first after-phone batch. Successful reruns provide the evidence. A targeted night batch and the first post-audit batch lost Chrome connections; smaller/allowed-port reruns passed. An optional interpreter lookup hit its 30-second cap and was abandoned; no dependency installation was needed.
- Bundle: 1,519,271 bytes. Standalone exploit run made zero external HTTP(S) resource requests. Successful drive batches had no tool-console errors. Authored files contain no em dashes. Final default Crew and actual Mission at 1366x768 are in `fix-final/`; final night Motion-off comparisons are in `fix-night-final/`.

All task Chrome debugging ports and host port 8715 were closed before report publication. Validation hashes, path data and final gaps are in `fix-validation.json`.
The shell cleanup had left three test hosts. `fix-process-cleanup.json` records their verified commands; `fix_cleanup.py` checked creation time and workspace before native termination. Final port checks confirm closure. The Scratch host helper now terminates its own process handle directly.
