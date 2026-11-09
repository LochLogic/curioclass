# Craft lens: moon-base-drama (round 1)

Cold lens on the bundle as built (`moon-base-drama.html`, 1,509,808 bytes). Not re-bundled. Frames and logs in
`S:/CurioClass-codex-scratch/moon-base-drama/craft/out/` (mine) and `S:/CurioClass-codex-scratch/moon-base-drama/audit-r1/` (shared audit).

## Contract (clean)

- One file, 1.51 MB: under the 2 MB goal.
- No network requests: `performance.getEntriesByType('resource')` empty after a full walk to the ending (perf-night).
- No console errors or exceptions in any of my 20 shots or in the audit.
- Kit used: `Curio.voice`, `Curio.init`, kit Motion, Sound, Read and `.calm`; nothing re-implemented except the radio caption and glow loop (finding 1).
- Frame times at 1366x768 (rAF, 180 to 240 frames): Crew idle median 16.7 ms, p95 16.7; rover drive 16.7 / 16.7;
  night scene 16.7 / 16.8. Only the idle beacon and the drive or ice float run, all killed by Motion off (calm-rover, calm-ice: zero animations, rover transform none).
- Keyboard: Tab reaches the badges with a 4 px #ffcf45 outline (kbd-tab); Right and Left step beats, Right stops on an unanswered choice, A toggles the card, R opens the map with focus on its first choice (kbd-letters).
- Targets: the audit's 60 px rows are clean at every size; I cite them.
- Art: all 14 `art:` tokens have prompts.json entries; no people in any asset (airlock suits hang empty, checked on the frame). Credit line matches CODEX-BUILD.
- Words: no em dashes in src.html or notes.md; "Curio Class" only; privacy stated in notes (story in memory, Motion preference on this device).
- Lines: voice/lines.json holds all 59 strings, including the 24 guided "how + event" joins, word for word with `allLines()`.

## Findings

1. **should fix, general.** `src.html:847-853` (radioState). The radio glow and the Read caption follow
   `speechSynthesis.speaking` only. The tool ships no clips yet (voice/ has only lines.json), but sibling tools ship
   mp3 clips and `Curio.init({clips:"voice:*"})` plays them through `Audio`, not speechSynthesis. Once this tool's
   recordings land, the radio will never glow while Mission Control talks, and a Read line will not show in the caption
   (spec: "The radio glows only while Mission Control speaks"). How seen: the code against `kit/curio.js` speakOne
   (clips first, then speechSynthesis). Better: glow on `V.playing` or an active Read, not on the synth.

2. **should fix, general.** `src.html:467` (welcome valid only while no job is checked). A first tap on a job badge
   skips the welcome (kit rule, fine), but it never comes back: Sound off then on, and Crew re-entry, bring nothing
   (log v-job-first-then-sound: only the job line, then the beat 1 line). Standard voice check item 3 fails, and the
   most natural first tap means the teacher never hears "Teacher, you are Commander Ada." Better: a welcome that stays
   true once jobs exist (the premise without "Tap a job badge"), brought by Sound on or the next Crew entry, once.

3. **should fix, general.** Choice icons are bare text glyphs: `src.html:397` "☀ ▣" (sun and battery), `:409` "▧"
   (blanket), `:410` "▯" (door), `:403` "≈" (river), beside one real emoji `:402` 🧊. In a K-2 tool the icon is
   what a pre-reader sees on the big choice button; a hatched square and a tall rectangle do not read as a blanket or
   a door. Frames: out/warm-680.png, audit state-batteries-1366x768.png. Better: small drawn SVG icons (battery
   with a sun, blanket, door, wave), the same on the choice, the map node and the rewind card.

4. **polish, general.** Map strip choice nodes: the two-glyph "☀ ▣" spills out of its 20 px diamond, and "▯" renders
   as a colored emoji box (out/zoom-map-375.png; also visible at 680x425, audit state-night-680x425.png). Better: one
   icon per node that fits the diamond (follows from finding 3).

5. **nit, general.** Crew at 1920x1080 with a badge checked: the scaled watering can (scale 1.12) touches the
   "Plant Keeper" label, and the subtitle "Choose a job. Mime your prop." sits on the first badge's top border
   (out/zoom-crew-1920.png). Props are also small in the big badges (max-height 135 px in about 330 px badges).

6. **nit, general.** Hint text is 11 px at 375 wide and in short windows, 14 px at 1920x1080 (crew-375-hint; audit
   frames). The radio caption carries the same words, so nothing is lost, but the bar hint is hard to read on a projector.

7. **nit, general.** Screen readers read the choice glyphs ("☀ ▣") before the words: `.choice-icon` (`src.html:335-336`)
   and the map dots have no `aria-hidden`; `#map-strip` has an aria-label but no role.

8. **nit, general.** `src.html:804-809` and `:841-845`: Ada's card toggle and Motion call `stop()`, so
   hiding the card mid-transmission cuts the beat's fact line. The spec says any tap stops the radio, so this is to
   spec; Radio again recovers it. Consider letting the card and Motion leave the radio playing.

## Standard voice check

Held clicks (0.12 s), Sound and Motion on, 1366x768. Logs: run on shots1.json and shots2.json in my scratch folder.

| line | kind | expected | spoken |
|---|---|---|---|
| "When the crew is ready, tap Start mission." (joined to the first job line) | how | 1 in 5 badge taps | 1 |
| Plant Keeper job line | event | 5 | 5 |
| "When the crew is done, tap Next." (joined to beat 2) | how | 1 | 1 |
| "Commander, read your card. When the crew answers, tap their choice." (joined to beat 3) | how | 1 | 1 (beats 4 and 6 plain) |
| batteries result B, choice tapped three times | event | 3 | 3 |
| "Tell Ada which choice helped. Tap Rewind." (joined to the ending) | how | 1 | 1 |
| ending line, Radio again three times | event | 3 | 3 |
| beat lines 1 to 7 | event | each beat opened | every one |

1. Repeats: pass (table). Audit five-clicks rows clean.
2. Stale lines: pass. Nine taps 0.2 s apart ending on Crew: every line cut by `hush`, nothing spoken after the Crew
   tap (v-fast). Back from beat 4 speaks beat 3's line, not the dropped result.
3. First-tap timing: stage tap gives the welcome at once (v-first-stage2); ArrowRight gives the welcome (v-first-key);
   Read speaks the hint only (v-first-read); Sound says nothing, Sound on brings the welcome once (v-first-sound);
   a badge gives only its own line. **Fail on the skipped welcome returning (finding 2).**
4. Read: cuts the playing line and speaks the beat line; with Sound off it still speaks (v-read-soundoff); the next
   tap after Read starts its line at once (v-read-mid).
5. Order: spoken lines follow the taps in every log.

## Audit pilot

- Leads confirmed: "welcome not heard" after a first tap on a job badge, and my run shows it never returns (finding 2).
- Leads wrong (as defects): "two quick taps, line cut and never heard whole" on the badges and mode buttons. The spec
  says any tap stops the radio at once, and job lines are events that replay on the next tap. "Not heard" after a
  first Mission tap with no crew: it speaks "Tap a job badge" instead, which names the action, and Sound on still brings the welcome.
- Missed: the glyph icons (3, 4), the radio glow tied to speech synthesis (1), the welcome never coming back (2),
  the 1920 badge crowding (5).
