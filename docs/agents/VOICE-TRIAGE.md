# Voice triage: 36 live tools with no recorded voice

Written 2026-10-26. Read-only pass over each tool's tool.json and src.html. Sources: STANDARDS.md (voice rules and the
narrate/hush/readNow/firstTap queue from tools/collision-lab/src.html), voices/bank.json (23 kept voices; adventure-guide
and calm-guide never used), scripts/localvoice.py.

Findings that apply to every row:
- None of the 36 has a `voice:*` token or `Curio.init({clips: "voice:*"})`. None uses the narrate/hush queue. So every
  NEEDS or OPTIONAL tool needs wiring; the cost column says how big.
- 8 tools (all Grade 2) already have a Read button that speaks with the browser's `speechSynthesis` (best available
  browser voice, rate .95). Their text is partly template built, so each spoken sentence needs a recorded line (or the
  tool keeps browser voice for data-built text). Wiring there means swapping `speak()` for the clip queue plus a
  `voice/lines.json`.
- The other 28 speak nothing today.
- Line counts are estimates (tool text is partly data driven); firm up when writing lines.json.

## Table

| Tool | Grade | Verdict | Speaks today | Est lines | Proposed voice | Wiring needed (cost) |
|---|---|---|---|---|---|---|
| art-passport | K-2 | NEEDS | nothing | 45 (14 works x look/feel prompt, 4 mode welcomes, stamps) | knowing-guide | yes (large: new queue, no Read button either) |
| beat-buddies | K-2 | NEEDS (short lines only) | nothing | 14 (welcomes, march/freeze/echo cues, 4-beat card instructions; never over the beat) | hero-coach | yes (medium; narrate only while audio is stopped) |
| line-safari | K-2 | NEEDS | nothing | 30 (line, shape, color prompts, 4 welcomes) | bright-teacher | yes (medium) |
| orchestra-zoo | K-2 | NEEDS | nothing (taps play instrument recordings) | about 16 to 28 (family intros, quiz prompts, welcomes; instrument sounds are already recordings) | playful-friend | yes (medium; hush before instrument clips) |
| contraction-crusher | 2 | NEEDS | Read button, browser voice, also speaks each result sentence | about 45 (21 pairs x 2 sentences) | warm-teacher | yes (small to medium; say()/Read hook exists, swap to clips) |
| corner-store | 2 | NEEDS | Read button, browser voice, customer lines | about 40 (5 hellos, 5 thanks, price and change prompts; templated numbers are the hard part) | friendly-dad | yes (medium) |
| hamburger-paragraph | 2 | NEEDS | Read button, browser voice | 25 (sentence frames, bear reactions) | curious-librarian | yes (small, Read hook exists) |
| loop-garden | 2 | NEEDS | Read button, browser voice (say() only prints text) | 20 (level goals, bonk and star feedback) | hero-coach | yes (small to medium) |
| marching-band | 2 | NEEDS | Read button, browser voice reads the sentence | 20 (pattern sentences, number words) | playful-friend | yes (small; stay silent while band plays) |
| melt-or-not | 2 | NEEDS | Read button, browser voice; 12 things x yes/why | 30 | clear-teacher | yes (small, say() exists) |
| resource-detective | 2 | NEEDS | Read button, browser voice | 25 | gravel-ranger | yes (small) |
| three-pigs-lab | 2 | NEEDS | Read button, browser voice; story lines are on-screen speech bubbles | 30 (story beats, wolf and pig lines, lab prompts) | gentle-storyteller | yes (medium; story is an awaited sequence) |
| germ-spread-sim | 3-5 | OPTIONAL | nothing | 14 | big-sister | yes (medium); a sim with short instructions, fine silent |
| how-animals-see | 3-5 | OPTIONAL | nothing | 16 | clear-teacher | yes (medium); 4 modes, mostly diagrams |
| label-detective | 3-5 | OPTIONAL | nothing | 18 | friendly-dad | yes (medium); reading practice, a Read button would help weaker readers, works silent |
| melody-maker | 3-5 | OPTIONAL | nothing | 10 (welcomes only) | playful-friend | yes (small); music, narrate only before playing |
| paint-mixer | 3-5 | OPTIONAL | nothing | 10 | easy-coach | yes (small); interface explains itself |
| state-quest | 3-8 | OPTIONAL | nothing | 12 | upbeat-guide | yes (medium); big file, quiz of state names |
| nations-of-north-america | 5 | OPTIONAL | nothing | 22 (region facts) | news-reader | yes (medium); fact text helps grade 5 readers when read |
| career-match-quiz | 6-8 | OPTIONAL | nothing | 15 | casual-peer | yes (medium) |
| classifier-scenes | 6-12 | OPTIONAL | nothing | 8 | science-narrator | yes (small); no modes, short |
| concert-ticket-market | 11-12 | OPTIONAL | nothing | 10 | calm-professor | yes (small); grade 11 batch, students on laptops |
| first-apartment-budget | 9-12 | OPTIONAL | nothing | 12 | wise-mentor | yes (medium); 100 KB file |
| frame-it | 6-8 | OPTIONAL | nothing | 14 | knowing-guide | yes (medium) |
| market-time-machine | 9-12 | OPTIONAL | nothing | 12 | smooth-narrator | yes (medium) |
| mind-map | 9-12 | OPTIONAL | nothing | 14 (stress bucket and help-a-friend benefit most) | soft-breath | yes (medium) |
| moon-phase-model | 6-8 | OPTIONAL | nothing | 10 | science-narrator | yes (small) |
| size-of-everything | 7-9 | OPTIONAL | nothing | 14 (zoom steps) | easy-coach | yes (medium) |
| smoothie-lab | 6-7 | OPTIONAL | nothing | 10 | lively-host | yes (small) |
| vanishing-point-studio | 6-8 | OPTIONAL | nothing | 10 | firm-captain | yes (small) |
| beat-lab | 9-12 | NO | nothing | 0 | none | no; DAW style tool, narration fights the audio |
| chord-explorer | 6-8 | NO | nothing | 0 | none | no; the chords are the point, little prose |
| note-ninja | 3-5 | NO | nothing | 0 | none | no; timed rhythm game, narration fights the beat |
| elements-inspector | 6-12 | NO | nothing | 0 | none | no; 790 KB reference lookup, no fixed lines |
| factor-forge | 6 | NO | nothing | 0 | none | no; math game, almost no text |
| fingerspell-flash | K-12 | NO | nothing (its "Read it" mode reads signs, not speech) | 0 | none | no; visual sign language practice |

## Counts

- NEEDS: 12 (4 K-2: art-passport, beat-buddies, line-safari, orchestra-zoo; 8 Grade 2: contraction-crusher,
  corner-store, hamburger-paragraph, loop-garden, marching-band, melt-or-not, resource-detective, three-pigs-lab)
- OPTIONAL: 18
- NO: 6
- Total 36.

Voice notes: hs-narrator is not used. No two neighbors were deliberately given the same voice, but only the
subject-based neighbors were reasoned, not checked; run `python scripts/neighbors.py <id>` before committing each
voice. Free fallback for K-2: warm-teacher (used once, on no one here besides contraction-crusher).

## Build list, cheapest wins first

1. The Grade 2 tools with an existing Read button and speak hook (small swap to the collision-lab queue, write
   lines.json, record): hamburger-paragraph (25), resource-detective (25), marching-band (20), loop-garden (20),
   melt-or-not (30), contraction-crusher (about 45). K-2 band standard says the narrator voices every fixed line, so
   these come first.
2. three-pigs-lab (30) and corner-store (about 40): same hook exists, but story sequencing and templated numbers add
   effort.
3. line-safari (30), orchestra-zoo (16 to 28), beat-buddies (14): K-2 teacher led, no speech today, so the whole queue
   plus a Read button must be added. Keep lines short and never over the audio.
4. art-passport (45): biggest K-2 build (14 artworks, new queue, new Read button).
5. OPTIONAL, only if time, highest reading value first: label-detective, nations-of-north-america, mind-map
   (soft-breath), size-of-everything, how-animals-see, germ-spread-sim. Then the rest as one batch: moon-phase-model,
   classifier-scenes, vanishing-point-studio, smoothie-lab, concert-ticket-market, paint-mixer, melody-maker,
   state-quest, career-match-quiz, frame-it, first-apartment-budget, market-time-machine.
6. Skip the 6 NO tools.

## Done 2026-10-26

All 12 NEEDS tools are voiced, live and on the Review Desk (orders 36 to 47). Voice changes from the table above:
marching-band uses firm-captain (Alnilam, as a drum major) so it differs from Orchestra Zoo, and beat-buddies uses
lively-host (Sadachbia) because Sound Elevator already has Puck. Orchestra Zoo and Art Passport needed 16 kbps clips
and smaller art to fit 2 MB (Orchestra Zoo also tempo 1.05). OPTIONAL tools wait for Cory.
