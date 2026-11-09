# Codex review: spot-the-ai

## Played

Cold Grade 1 solo and projector walk: all ten shop machines, both new-example branches and all ten showdown rounds, before reading the builder's report or source. The large painted machines and mop surprise are strong.

## Findings fixed

- Blocker, general, runJob: startup pitch encoded every answer (620 Hz AI, 360 Hz rule). Real held taps confirmed the perfect cue. All ten now start at 480 Hz.
- Should fix, general, voice: at a 2 s pace reveal descriptions swallowed action instructions. Shortened and prioritized the next-action lines, kept once-only how-to and serial validity checks; main-path recheck heard all eight action keys once.
- Should fix, general, speaker: queued questions could be spoken after the picture already showed an answer. The visible bubble now follows the question/answer that the shared voice queue actually starts.
- Should fix, general, teddy: Same every time implied an identical sentence despite the three-phrase cycle. Added a current-phrase outline and return arrow, Same three in order, cycle-specific repeat narration and accurate steps wording for all rules.
- Should fix, general, photo finder: the mop's wrong Dog guess carried a check mark. It now carries a cross; the puppy keeps its matching check. The wrong path still teaches through the same painted mop and spoken explanation.
- Should fix, general, phone: a square glyph stood for locked. Replaced it with a clear open/closed padlock, keeping the successful check separate.
- Should fix, general, privacy/facts: made Motion storage visible on screen and scoped the displayed AI definition to this shop's machine-learning examples. Notes distinguish enrolled face matching from generic facial features.
- Polish, general, art: redrew the magenta-fringed shelf with imagegen in the same house style. First candidate rejected for edge artifacts; second green-key candidate converted with art.py --rekey shelf and despill.
- Audit coverage now includes the actual machine, inside and recap drawings, plus teddy, cat and cloud states, rather than treating the entire shelf-covered SVG as an unobscured keep region.
- Should fix, general, audit voice leads: a second showdown greeting arrived after its voting instruction. Removed the redundant delayed greeting; the vote instruction is the mode entry.
- Should fix, general, audit re-selection leads: rapid taps on the pressed shelf tile restarted the same job, cutting its how-to and in-machine responses. The tile now acknowledges selection without restarting; the explicit repeat control still replays the job. Teddy bubbles also stay with their spoken saying.

## Findings left

- Blocker, general, spec-bound: memorizing the mandated fixed order earns 10/10 without reasoning. The spec forbids changing that order. Kept it, documented the limit, and explicitly disallowed using bulbs as mastery evidence in notes.
- Should fix before shipping: recorded curious-librarian clips are absent. The build/review brief explicitly forbids recording; browser narration and a synchronized manifest remain. No narration recording service was invoked.

## Break it

- Matching bulbs are the only score. No best score, saved result, confidence meter, reflection gate or separate mastery check exists.
- Real held-click full rounds: always AI 5/10; always Not AI 5/10; alternate 6/10; sweep both choices before each reveal 5/10; every answer wrong 0/10; memorize order 10/10 (spec conflict above).
- Open before voting and Next before opening do not advance. Changing both choices before opening records only the last one. Repeated Open adds no duplicate; mode hopping preserves the committed result.
- Post-reveal A/N and repeated reveal: all ten keyboard rounds keep their committed vote; 34 keyboard checks passed, including focus on Next and Play again, with zero exceptions or network requests. All ten startup tones remeasured at 480 Hz; the old high/low classification rule cannot distinguish answers and reduces to constant guessing.
- Independent enumeration: five AI, five rules, required mixed order, longest type run two, one all-matching vector among 1024. Teddy returns to its first phrase after three repeats; new-example cycles remain specified.

## Voice walk

Default Sound on, held 120 ms clicks, 2 s gaps: stage, door, Open, repeat, shelf, phone, Open, hat, shelf, showdown, vote/Open/Next through ten. Cat, mop and cloud were checked as side paths.

Final spoken action keys in order: pick, open, again, back, tryNew, vote, openShow, next. Each started once on that page. A separate fresh plain-stage tap also started pick immediately.

Job, rule/AI, hat/cat and closing events were checked against their current state. Fast actions drop stale descriptions; no instruction names an unavailable control. Welcomes skipped/cut by an action remain allowed by BASELINE 16; the hint and Read retain the action.

| Line kind | Expected | Observed |
|---|---:|---:|
| Eight action how-to keys, main route | once each | once each |
| Repeat control, five actions at both 8 s and 2 s gaps | 5 | 5 |
| Six quick double selections, 0.7 s gaps | one whole how-to per selection | 6/6, no cuts |
| Repeated selected teddy/speaker tiles | preserve one complete job | saying and Q/A complete, no cuts |
| Read with Sound on/off; immediate mode switch | current hint, prompt new mode | passed |

Evidence under _scratch/spot-the-ai/: post-audit-main.json, post-audit-mode-entry.json, post-quick-machine-*.json, post-selected-machine-*.json, post-repeat-five-fast.json, voice-repeat-five.json, voice-read-switch.json and speaker-timing.json. At 680x425 a mutation trace confirmed both cowQ and cowA matched their bubble when each started. The full voice manifest equals allLines(), with no missing or extra strings. Browser narration only; no claim of listening to recorded Aoede clips.

## Facts checked

- Learning patterns from data: [AI4K12, Big Idea 3](https://ai4k12.org/big-idea-3-overview/). This tool illustrates machine learning; it does not define all AI approaches.
- Learned facial matching, enrolled owner and hat support: [Apple Platform Security, Facial matching security](https://support.apple.com/en-om/guide/security/sece151358d1/web), checked 2026-11-07; unregionalized route returned 429. Eyes/nose/mouth are picture clues, not an identity-matching algorithm or a literal stored portrait pile.
- Speech learned from examples: [Hinton et al., IEEE SPM 2012](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/HintonDengYuEtAl-SPM2012.pdf). Cow/duck/cloud words and answers are scripted spec content.
- Traffic history, live conditions and alternative routes: [Google Maps 101, Johann Lau, 2020-09-03](https://blog.google/products-and-platforms/products/maps/google-maps-101-how-ai-helps-predict-traffic-and-determine-routes/). Park, after-school and rain trips are illustrative cases, not measured route predictions.
- Learning labeled photo classes and making mistakes: [Krizhevsky, Sutskever and Hinton, NeurIPS 2012](https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html). Puppy/mop outcomes and legs/ears/tail are conceptual scenes, not performance claims or hand-written classifier rules.
- Learned recommendations: [Covington, Adams and Sargin, RecSys 2016](https://research.google.com/pubs/pub45530.html?hl=uk). Dinosaur/space sequences are original demonstrations.
- Code 1234, floor 3, channel 5, camera press and teddy's three sayings: original simplified rule machines in spec.md. Real products can combine rules and AI; the visible caveat and notes preserve that distinction.
- CSTA ids E1-ALG-ML-02 and E1-SOC-HU-15 exist in data/standards/csta-2026-ids.txt. Inspecting examples/new inputs and comparing everyday uses/mistakes enact the spec's stated goals; no extra standard was added.
- Recomputed all seven specified contrast pairs: 11.503, 14.854, 6.175, 10.744, 11.496, 8.316 and 4.837. Evidence: Scratch/review-numbers.json.

## Sensitivity

Three marked people assets inspected: owner, identical owner with hat, and 12-portrait grid. Varied ages/skin tones, glasses and a headscarf are presented warmly; no named culture or religion is taught. A cultural lens should still check the grid for stock ethnic shorthand and the facial-matching explanation for implied differences in whose face works. No real biometric input is collected.

## Flattest moment left

Later showdown rounds repeat already-known machines. The teddy's cycle now gives a visible cause/result payoff; richer replay variation would change the specified fixed sequence/content.

## Graphics

All 30 painted assets inspected in the art sheet and machine/reveal frames; three people images also inspected separately. Kept the workshop, all machine cutouts, portraits, photos and cartoons. Shelf alone redrawn, two candidates, selected file art/shelf.webp; built-in imagegen prompt/provenance in art/prompts.json. Art about 924 KiB; bundle 1,343,767 bytes (1312 KiB). Independently inspected the existing Beat Lab and Snowy Mail Route benchmark frames; the workshop retains comparable depth, large art and clear feedback.

## Audit

One full audit completed within the 40-minute limit, Chrome 9941 / host 8745: _scratch/spot-the-ai/review-audit/audit.md. All 84 frames inspected in sheets; critical compact/phone frames also opened full size.

- Its 55 leads: 7 specified scrolling-shelf warnings; 26 cropped-SVG bounding-box warnings (24 inside, 2 recap); 1 wood-grain path behind an opaque recap card. Confirmed visually, not layout faults.
- Eleven missing first-tap welcomes are allowed by BASELINE 16: the tap speaks for itself, and hint/Read/reveals retain the content. The one genuinely late greeting was fixed.
- Six quick-tap instruction cuts and three lost in-machine lines came from restarting the selected tile. Fixed the selection behavior, then rechecked all six quick-tap cases and the teddy/speaker chains. Repeat-button events still start five times.
- No undersized targets, actual clipped controls/hints, console exceptions, focus loss, infinite calm animations, resize exceptions or stuck controls. Grayscale and 34 independent keyboard checks also passed.
- No second full audit. Only the changed voice/selection paths were rerun: final full main voice route, slow showdown entry and nine targeted cases, all console-clean. All task Chrome/server ports verified closed; no host.html remains.

Wave lessons checked: next-action hints/Read and once-only how-to; stable focus/controls/reserved hint space; all sizes and 60 px targets; giveaways and honest bulbs (fixed-order exception above); both standard goals; Motion off with unchanged timers; both vote choices visible; resize during actions; no late welcome; unknown insides hidden; distinct rule/pattern symbols; truthful mop badge; hints restored on Back/mode switch; no answer-word copying before a vote.

Spec Done when: runtime items 1-6 and 8-9 verified; item 7 passes the tested browser-voice lifecycle, with recorded-voice identity still open. Notes begin with the three required headings; metadata remains teacher-led Grade 1, 10-20 minutes.

Final evidence: _scratch/spot-the-ai/review-validation.json records the bundle hash, bytes, voice counts and closed ports.

## Left open

The fixed-order assessment loophole and missing recorded clips above need a later spec/recording decision. No new features, kit edits, commits, shipping or outreach. Where a choice was needed, retained the spec's order and people art and the current build brief's recording prohibition.

Process note: the initial rules/memory reads returned immediately but lacked an explicit subprocess timeout; subsequent commands used bounded wrappers (bundle 120 s, drive 300 s, audit 2400 s).
