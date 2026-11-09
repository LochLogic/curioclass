# Polish: music-history-radio (Codex fix, round 1)

Evidence paths below are relative to `S:/CurioClass-codex/_scratch/music-history-radio/`. The working folder was verified before edits. The in-progress record is `fix-progress.md`; this report is finalized only after the single audit, per the requested stop rule. No commits, shared-engine changes, refine edits or new topics.

## Blocker

1. FIXED: Gamelan is excluded from scored Mystery sets and their year markers; 482/1,000 baseline sets contained it, 0/2,000 repaired sets did. Its ident, strip, dial explanation and defensive result heading say it is a living tradition heard in Paris in 1889. Before: `fix-before/before-01-gamelan-scored.png`, `before-01.json`. After: `fix-after/after-01-gamelan.png`, `after-01.json`, `final-markers.json` (11 eligible ticks plus axis). It is a side station, not a dated origin.

## Should fix

2. FIXED: Playing modes now queue their how lines, with music ducking, `valid`/`needs` retained and priority over idents. At held-click, two-second pace, dialReady, compareHow, flipHow, deskHow and mysteryHow each start once, versus zero on the original powered path. `before-02.json`, `final-02-main-voice.json`; frames in `fix-before/` and `fix-final/`. Input interruptions are disclosed under Voice walk.
3. FIXED: Dial, Desk and Mystery have independent Power instructions; flipHow requires playing, enabled Flip and no pending switch. Original Mystery/Desk both said generic powerHow, and unpowered Compare spoke flipHow. After: `after-03-mystery.json`, `after-03-desk.json`, `after-03-flip.json` show the correct mode lines and zero unpowered flipHow starts, at 1366x768.
4. FIXED: Idents require a stable 500 ms lock. The rapid station-button sweep originally started and cut ten transient idents; after it starts zero transient idents and the final Disco ident once. `before-04.json`, `after-04.json`, `fix-before/before-04-spin.png`, `fix-after/after-04-spin.png`. Every tuning input resets the lock timer, including movement within a lock.
5. FIXED: Re-locking the same station restarts only after more than 700 ms of lost signal. Twenty lock-edge wobbles caused 20 restarts before, zero after. `before-05.json`, `after-05.json`, matching 1366x768 frames. New stations still restart; signal strength and the eye still follow the actual lock threshold.
6. FIXED: Tool-local output trims reduce the measured twelve-station spread from 14.64 dB to 1.49 dB; static is about -35.04 dBFS, roughly 4 dB below the station mean. Ident ducking was held off during measurements, with the same five-second procedure before and after. Full Renaissance/Baroque loops differ by 2.08 dB. `audio-comparison.json`, `final-06-full.json`, frames in `fix-before-audio/`, `fix-final/`, `fix-cheats/`. No kit change.
7. FIXED: Removed sentence-comparison badges, an allowed option. Five misleading Organum tags become zero; no comparison into or out of gamelan remains. `before-07-08.json`, `after-07-08.json`, matching Organum frames at 1366x768.
8. FIXED: The Harmony row now says "Held D and A; moving intervals include open fifths and octaves." It no longer claims all stressed intervals are open. The original arrangement actually has eight stressed thirds/sixths and one ninth among fourteen starts; retained music now matches the limited wording. `before-08.json`, `after-07-08.json`, `fix-after/after-07-08-organum.png`.
9. FIXED: Modern staff strips use compiled melody onsets/durations and have treble clefs. Ragtime shows offbeats, five eighth flags and tied held notes; Organum separately shows 2:1 long-short motion, seven 3/4 bars for four phrases, and its held D/A lower voice. `fix-before/before-09-ragtime.png`, `fix-before-audio/before-09-organum.png`, `fix-after/after-09-ragtime.png`, `fix-after/after-07-08-organum.png`, `after-09.json` at 1366x768.
10. FIXED: Key skills now promises comparing the estimate with revealed listening clues, without claiming an unavailable revision step. No new revision feature was added. `notes.md`, `before-10.json`, `after-docs.json` (revision claims 1 to 0; five skills retained).
11. FIXED: Desk ranges now use a captured horizontal/vertical knob drag at 32 px per era; native arrow keys remain. The 40 px baseline drag went Baroque to Hip hop, eight steps; the repaired real drag goes Baroque to Classical, one step. `before-11-drag-ready.json`, `after-11.json`, matching 1366x768 frames. The hint and accessible description say arrow keys work; `final-keyboard-fixed.json` confirms real keyboard changes.
12. FIXED: The circulation row and notes name the Dutch colonial exhibit at the 1889 world's fair; notes also name Debussy's listening encounter and Dutch rule. `before-12-13.json`, `after-01.json`, `fix-cheats/final-gamelan-layer-grid.png` at 1366x768. Named museum sources are listed below.
13. FIXED: The row begins with learning by ear in court and village ensembles. A diamond, dashed time tick, SIDE STATION caption and living-tradition wording distinguish gamelan; no predecessor comparisons remain. No uncertain notation date was added. `after-01.json`, `fix-cheats/final-gamelan-layer-grid.png`, `notes.md`.
14. FIXED: The student-facing row names Black bands led by Fletcher Henderson, Count Basie and Duke Ellington, Harlem's Savoy, and Benny Goodman's integrated Carnegie Hall concert using Henderson arrangements. `before-14.json`, `final-swing.json`, `fix-cheats/final-swing-full-credit.png`; panel scrollHeight equals clientHeight, 634 px, at 1366x768.
15. FIXED: Chose the review's explicit keep-people alternative, preserving the respectful community art. Cindy Campbell's organizing role and Jamaican-born DJ Kool Herc are credited on screen; notes explain the deliberate invented 1980s community scene and distinguish it from the 1973 indoor party. `before-15.json`, `after-15-25.json`, `fix-checks/after-15-hiphop.png`, notes section People and places. No answer was requested during this unattended run.

## Polish accepted

16. FIXED: Baroque Harmony says "Harmony implied by the bass line." `after-music.json`, `fix-cheats/final-06-full-phrases.png`.
17. FIXED: Classical and Ragtime phrase 2 use C rather than F. Alberti pitches are C/G/E/G; stride chord pitches are C/E/G. `after-music.json`. The hip hop keyboard sample bass uses the corrected Classical C chord as well.
18. FIXED: Renaissance phrase 7 holds only G/D under the suspension; B enters at the C-to-B resolution, 1.2 seconds into the 2.4-second phrase. `after-music.json` lists all accompaniment events and times.
19. FIXED: Gamelan gong punctuation is on beat 4 (1.875 of 2.5 seconds), elaborations on half-beats (0.3125-second steps). The layer sketch places gongs at beats 3/7/11/15 in zero-based four-phrase time. `after-music.json`, `fix-cheats/final-gamelan-layer-grid.png`.
20. FIXED: Mixed texture names drums when Beat adds them; Chant Beat explicitly means free phrase lengths while separate accompaniment can pulse. `after-20a.json` has 14 drum events and an explicit Disco-drums row; `after-20b.json` has 16 continuo events and the pulse qualification. Both 1366x768 frames are in `fix-checks/`.
21. FIXED: Closest-station scoring replaces the fixed 50-year window. Exhaustive guesses 800-2000 match at most one of eleven eligible stations; a fixed 1930 no longer covers five styles. Duplicate Tune in does not append history. `after-21.json`, `final-cheat-sweep.json`, `final-cheat-mode.json`; see Cheats tried.
22. FIXED: Chant Rhythm says "Free, unmeasured; each phrase stretches at its end." Visible in `fix-final/final-dial-1366x768.png`, `final-markers.json` line catalog.
23. FIXED: Reveal retains a dim estimate pin and draws a dashed gap to the answer. One guess-pin and one gap path are measured in `after-23.json`; `fix-checks/after-23-reveal.png` at 1366x768.
24. FIXED: Dial labels scale with the radio, 19.75 px at 1920x1080, versus the original 11 px. `after-24.json`, `fix-checks/after-24-large-labels.png`, `fix-sizes/final-27-last-year-1920x1080.png`.
25. FIXED: Tighter panel spacing and 160 px postcards retain all 96 hip hop pads at 1366x768. Pad-strip bottom is 692 px, panel/footer boundary 710 px; clientHeight equals scrollHeight, 634 px. `after-15-25.json`, `fix-checks/after-15-hiphop.png`.
26. FIXED: At 760x900 the visible footer hint and result name Rhythm and Instruments, so the reveal does not depend on off-screen highlighted rows. `after-26.json`, `fix-checks/after-26-760-reveal.png`.
27. FIXED: Shortened the needle and padded the rail. At all seven standalone STANDARDS sizes, the final year is fully visible with at least 6.28 px right padding and at least 6.67 px separation from the needle. First-year frames also show left padding. `final-27-*.json`, `fix-sizes/final-27-last-year-*.png`; the compact dial intentionally scrolls to the tuned year.
28. FIXED: C/F/M and Space shortcuts require Shift outside native button activation. Unmodified M leaves Dial unchanged; Shift+M enters Desk. Real plain Space leaves Power off, real Shift+Space turns it on. `after-28.json`, `final-28-plain-space.json`, `final-28-shift-space.json`, `fix-shortcuts/`. Notes and footer list the modifiers.
29. FIXED: Organum says "was probably sung at Christmas 1198" per the sensitivity guidance. `fix-after/after-07-08-organum.png`, `after-07-08.json`; manifest updated.
30. FIXED: Rock and roll names Black gospel and rhythm and blues roots, Sister Rosetta Tharpe and Chuck Berry in full. `after-30-33.json`, `fix-checks/after-29-33-rock.png`.
31. FIXED: Ragtime names Black composer Scott Joplin; hip hop names Jamaican-born DJ Kool Herc and Black, Latino and Caribbean youth. `fix-after/after-09-ragtime.png`, `after-15-25.json`, matching hip hop frame.
32. FIXED: Repainted the gamelan postcard as a Central Javanese tiled pendopo with a broad joglo roof, bronze instruments and a level garden. Inspected finished 420x315 WebP and live frame: `art/mhr-pc-gamelan.webp`, `fix-cheats/final-gamelan-layer-grid.png`.
33. FIXED: Repainted Swing as an empty Harlem ballroom bandstand with a long wooden dance floor, rock and roll as a neighborhood juke joint with jukebox and low bandstand. Inspected both 420x315 assets and live 1366x768 frames: `fix-cheats/final-swing-full-credit.png`, `fix-checks/after-29-33-rock.png`.

## Settled calls

- Preserved 15 illustration tokens, all drawn by Codex, with only the hip hop asset marked people. Three disputed settings were repainted using the built-in imagegen skill and `art.py --rekey`, no paid art API. Prompts/provenance are in `art/prompts.json`; raw files are in `art/raw/`.
- New saved assets: `art/raw/mhr-pc-gamelan.png`, `art/raw/mhr-pc-swing.png`, `art/raw/mhr-pc-rocknroll.png` and their matching `art/*.webp` files inside the tool folder. The full house style and each final prompt are in `art/prompts.json`; generation used the built-in tool mode.
- Kept the rich radio, room, tuning eye and play. `fix-feel-comparison.png` puts the repaired radio beside the existing Beat Lab bar frame. Best moment is the reveal's two pins and gap; the two flattest moments were missing mode guidance and uncontrollable knobs, both repaired.
- Left the open-question proposal for two pre-reveal clue choices alone. It is not part of this fix.
- Optional touched nits: a 20 ms audio fade replaces the single-sample cut, and the redundant scrollable-dial Tab stop is removed. Other optional nits remain outside this pass.

## Cheats tried

- Fixed year: exhaustively checked all 1,201 integer guesses against the eleven eligible years. Maximum is one matching station, hence at most 1/6 for a constant guess across six distinct stations, rather than five styles under the old 50-year rule. 1930 matches Swing only; 1889 matches Ragtime only. `after-21.json`.
- Slider sweep: traversed 800-2000 in ten-year steps before one reveal. Final estimate 2000 against Swing scored false; the sweep did not bank intermediate matches. `final-cheat-sweep.json`.
- Repeated answer: twenty additional Tune in calls after reveal leave history length at one; six-round duplicate-reveal test leaves exactly six records. `final-cheat-sweep.json`, `after-21.json`.
- Mode/elimination attempt: switched out of and back into Mystery six times. Same target, no history, station still masked; the visible panel contained only generic listening prompts. `final-cheat-mode.json`.
- Signal check: tested five offsets at each of twelve marks. 0.15 gap locks with strength 0.7; 0.151 does not (0.698). Edge wobble cannot manufacture restarts or consume transient idents. `final-lock-boundaries.json`, `after-05.json`, `after-04.json`. The signal eye is a tuning indicator, not an achievement score.
- Audio meter: measured the actual post-limiter graph, not event counts or a visual badge. Voice ducking was disabled only in the measurement harness; both before and after used the same procedure. Level matching does not award a student score.

## Voice walk

- Main path, default Sound/Motion, held 120 ms clicks at two-second intervals: Power, Station, Compare, Station, Flip, Desk, Random mix, Mystery, Tune in, Next. Spoken-start order: dialReady; Organum ident; compareHow; flipHow; deskHow; mysteryHow; result. Each of the five named how lines starts once. `final-02-main-voice.json`.
- Side path, two-second held clicks: Mystery, Power, Tune in. mysteryPower, mysteryHow and a result start in that order. Slow seven-second version also lets mysteryHow and the result finish. `final-voice-side-two.json`, `final-voice-side.json`.
- Fast inputs cut some already-started lines, as the log explicitly records; no named how line is left queued and unspoken as before. Mode changes, pause and reveal drop stale speech. Muted automated starts are not an independent certification of narration by ear, and browser fallback cannot guarantee the recorded news-reader character.
- Gamelan path, Power then six Station taps at two-second pace: the corrected ident starts once after the stable lock, with the full living-tradition sentence, and is not cut. `final-gamelan-ident.json`, `fix-gamelan-voice/final-gamelan-ident.png`. Gamelan result speech is unreachable in normal Mystery sets because this station is excluded.
- `voice/lines.json` equals the 1,997 unique runtime `allLines()` strings, including all mixed row text. UTF-8 comparison is exact. No audio was recorded.

## Engine changes wanted

- No new kit change is needed for these repairs. Existing `handoff.md` requests remain: explicit audio-clock start/variable phrase boundary hooks and a documented cancellable custom-instrument bus in `kit/music-studio.js`. No engine file was edited.

## Audit

- Completed once, exit 0, within the 40-minute cap: `fix-audit/audit.md`, debugging port 9911, iframe host 8715. All 76 audit frames were inspected; `fix-audit-seen.json` records them. There were no runtime, resize, disabled-control, target-size, overflow, focus or Motion-off failures. All five-click repetition checks passed.
- Leads 1-2, compact footer text below 10 px at 680x425 and 800x500: FIXED, restored the label to 10 px. `post-audit-final-680x425.json`, `post-audit-final-800x500.json`, matching frames in `fix-audit-leads-final/`.
- Leads 3-9, Organum 3/4 text-box overlap in locked-second, compare-ready and a reveal: FIXED, increased the vertical separation without reducing digit size. At all affected sizes, 800x500, 1280x720, 1366x768 and 1920x1080, the text boxes now have a positive gap; including the extra 680 preview check, gaps range from 1.96 to 4.87 px. `post-audit-final-*.json`, `fix-audit-leads-final/`. The first narrower adjustment still touched, so it was rejected and its frames/numbers were retained separately.
- Leads 10-13, generic welcome classified as not heard after first Desk, Mystery, Power or Compare: the same audit table records the correct action-owned mode instruction on every one of those taps. Desk says Power plus knobs; Mystery says Power plus year pin; Power says tune with knob/Station; unpowered Compare speaks the complete Power/tuning instruction as a how line. These deliberately replace the generic welcome and match the repaired path; `after-03-*.json` and `final-02-main-voice.json` independently confirm them. No welcome is queued late behind the action.
- Lead 14, Reset changes nothing at the initial Baroque/Baroque/Baroque mix: expected unchanged starting value, already an optional nit in Refine. Random and Reset remain working; no change made.
- Lead 15, two quick Power taps cut dialReady: the second tap is Pause, which deliberately stops speech/music and changes the hint to Resume. This is a state-valid interruption; the five-click Power check is clean. The instruction remains in the live hint/Read after resuming. The fast-path log discloses the cut rather than claiming every syllable finished.
- The single audit is the snapshot before the two follow-up typesetting repairs. Only their affected frames/numbers were rechecked afterward; no second audit or lens run was made.

## Facts and sources

- Colonial display, Sundanese/Javanese performers and Debussy: [Smithsonian NMAA, Sumarsam](https://asia-archive.si.edu/essays/article-sumarsam/), [NMAA, Gillitt](https://asia.si.edu/research/essays/gillitt/), [Museo Reina Sofia, MadGamelan](https://www.museoreinasofia.es/en/activity/madgamelan/). Local transmission uses the named Smithsonian Folkways/UNESCO references in notes; no unverified notation date was introduced.
- Black swing bands, the Savoy and Henderson's arrangements: [Smithsonian Savoy account](https://americanhistory.si.edu/blog/2012/07/its-getting-hot-in-here.html), [Henderson archive](https://americanhistory.si.edu/collections/archival-collection/sova-nmah-ac-0797), [NEA interview](https://www.arts.gov/honors/jazz/gary-giddins).
- Cindy Campbell and Jamaican heritage: [GRAMMY interview with the siblings](https://qa.grammy.com/news/dj-kool-herc-cindy-campbell-50th-anniversary-of-hip-hop-interview-jamaican-roots). Gospel roots: [Smithsonian Sister Rosetta Tharpe](https://www.si.edu/spotlight/sister-rosetta-tharpe). Joplin: the supplied Library of Congress source. Perotin's uncertainty follows the named sensitivity item 6. Arrangement claims are proved from the compiled events in `after-music.json`, not treated as historical recordings.

## Checks

- Bundle succeeds, about 893 KB, all images load, zero remote resource requests in the file-loaded runtime. Browser-voice fallback notices are expected because no recordings were supplied. Runtime batches reported zero console errors/warnings/exceptions.
- All 1,728 mixes compile through eight phrases, 234,208 finite events. Every loop remains under 30 seconds. Motion off has zero infinite animations; grayscale and real keyboard frames were inspected.
- Standalone sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900. Phone 375x812 is checked inside the final audit's iframe host on 8715.

## Left open

- The fresh sensitivity exit check is still required by the pipeline; this run does not claim that PASS or run the three lenses again. By-ear timbre certification and a guaranteed recorded narrator remain unavailable. Optional nits not touched remain open.
- Remaining optional nits include Classical's generic phrase-balance wording, the extra hip hop Harmony/sample mismatch, passing-chord/stab/walking-bass details, Tune in before Power, the compact Power/dial edge, initial Reset styling, ident wording variants, dead maker/overridden CSS, the covered-round volume control and Guido wording. The accepted fixes do not claim those nits were resolved.
- Commands use 30-second read/static checks, 120-second bundles/rekey, 300-second drive batches and a 2,400-second audit cap. One Chrome connection reset was retried with a smaller two-shot batch. Initial rekey lacked NumPy; the existing read-only Python site-packages supplied it, with bytecode writes disabled.
