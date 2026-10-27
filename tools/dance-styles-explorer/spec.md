# Dance Styles Explorer

## One idea
Dance disappears as it happens, so this explorer makes it hold still: each style's demo phrase can be watched as a long-exposure trace (the shape it carves in space) and a rhythm line (where its accents land in time), so ballet's tall verticals can sit beside breaking's low circles or tap's quiet top beside its busy feet, and every critique note is stamped to the count where you saw it.

## Not like
- gallery-critique (9-12 art, this wave): a role-play panel about a still painting, each claim pinned to a spot in the picture. Here there is no role play; the work moves, the evidence is a moment in time (a count), and the trace and rhythm line are how you hold that moment still.
- art-style-match (3-5 art): a style as a set of tells to identify a painting. Here nothing is identified or scored: styles are open files to watch, measure and compare.
- director-s-chair (9-12 theater): one scene staged in several traditions. Here each style has its own phrase and music; the comparison is of movement, measured.
- music-history-radio (9-12 music) and world-music-map (6-8): eras and instruments. Here dance, with only enough music to show each style's time.
- virtual-gallery, city-skyline-studio, beat-lab (9-12 arts): curating, perspective, production. No shared mechanic.
- Dance siblings: levels-and-pathways (floor ribbons), dance-pattern-puzzle (patterns in move cards), choreography-board (devices and versions). Only this tool has styles, the exposure trace, the rhythm line and written critique.

## Who and how
- Grade 9-12, arts (dance), module "Dance Styles and Criticism (Dance)".
- Topic line: analyzing and critiquing dance styles
- Driver: students on laptops (alone or in pairs); a teacher can project Styles for a class discussion. Minutes: 20-45.
- tool.json modes: ["Styles", "Compare", "Critique"]; driver "students or teacher".
- Standards (NCAS dance): DA:Re7.1.HSI (analyze movement and patterns, style), DA:Re8.1.HSI (interpret with context and vocabulary), DA:Re9.1.HSI (evaluate with criteria); DA:Cn11.1.HSI (cultural and historical context).

## Screens and modes
Kit frame with `kit/theme-912.css`. Header: title "Dance Styles Explorer", small line "Analyzing and critiquing dance styles", modes (`.seg`, keys 1 to 3) **Styles** (default), **Compare**, **Critique**, then `motion`, `sound`, `read`. Stage left, panel right (panel below under 1000 px wide, transport first).

Stage (all modes): the engine's `'void'` view, a dark space with a faint floor line and a height scale at the left (High, Middle, Low bands, thin). One dancer drawn from simple shapes. Under it the **rhythm line**: the counts as ticks, each accent as a bar whose height is its strength, foot sounds as dots (tap, step and flamenco footwork), the playhead. Under that the **transport**: **▶ Play** / **⏸ Pause**, **◀ count** and **count ▶** (step one count), speed **0.5x** and **1x**, count readout "Count 6 of 16".

View toggles over the stage (`.btn`, aria-pressed): **Live** (just the dancer), **Trace** (long exposure: a ghost copy every half count, older ghosts fainter, plus the paths of both hands and both feet drawn as lines in their colors), **Rhythm line** (on by default). Trace builds while playing and stays when paused; **Clear trace** wipes it.

### Styles (opens on Ballet)
- Panel: the 8 style chips in a two-column grid; the **style file** for the chosen style (`.sec` cards): Where and when; Roots; People (3); Signature, as five rows Body, Action, Space, Time, Energy; Look for (3 things); Music (what the demo's track stands for). Then **Measured from this demo** readouts (Interactions). Every file ends with the line "The demo is a short phrase drawn by Curio Class to show traits of the style. It is not a recording of a real performance."
- Choosing a style loads its phrase and track, resets the trace and plays from count 1.

### Compare
- Stage shows two dancers side by side (left: style A, right: style B), one shared clock in counts, one rhythm line each (A above B), the same view toggles. **Overlay** puts both on one spot so their traces lie over each other (A in coral and aqua, B in gold and blue).
- Panel: **Style A** and **Style B** selects (default Ballet and Breaking); the two Signature tables side by side, rows aligned (Body with Body, and so on); the two Measured readouts side by side.
- Styles with a different cycle length (flamenco 12, ballet 16) loop on their own; the counts readout shows each.

### Critique
- Stage as in Styles (or Compare, with a **Critique a comparison** toggle).
- **📌 Note** button (also key N) beside the transport: stamps the current count (or count range, while held) and opens a small form: **Term** (picked from the vocabulary guide), a few words (up to 140 characters), **Save note**. Notes list under the transport, sorted by count; tapping a note jumps the playhead there and shows the trace for those counts.
- Panel: **Vocabulary guide** (Content, grouped Body, Action, Space, Time, Energy; tap a term to see its definition and to use it in a note), then the **draft** with three boxes: **What I saw** (describe and analyze), **What it means** (interpret, with context from the style file), **How well it works** (evaluate against criteria). Under each box **Insert note** adds a note as "(count 5-6, contraction: torso hollows, arms follow)". Criteria chips for the third box: Clarity of style, Musicality, Use of space, Contrast of energy, Communicates an idea, Technique as shown.
- Checks under the draft (shown, never graded): each box cites at least one count; at least 3 vocabulary terms used; the third box names a criterion. Each check shows a ✓ or a ○ with words.
- **Copy text**, **Print**, **Clear critique** (confirm). The draft and notes are saved on this device only.

## Content
Styles (Where and when / Roots / People / Signature B, A, S, T, E / Look for / Music):
1. **Ballet.** Italian Renaissance courts in the 1400s and 1500s, shaped in the French court; Louis XIV founded the Académie Royale de Danse in 1661. / Court dance and spectacle; Pierre Beauchamp set the five positions of the feet; the terms are French. / Marie Taglioni (La Sylphide, 1832, early pointe work), Anna Pavlova, Misty Copeland (first African American female principal dancer at American Ballet Theatre, 2015). / B: turnout from the hips, long lifted spine, pointed feet. A: jumps, turns, extensions. S: vertical lines, often high, shown to the front. T: phrased with the music. E: controlled and light, effort hidden. / Turnout; arms framing the head; the finish of each turn. / A ballet class piano waltz in 3, 84 beats a minute.
2. **Modern dance.** United States and Germany, early 1900s, as a break from ballet's rules. / Dancers wanted movement from natural impulses and their own time. / Isadora Duncan (bare feet, natural movement), Martha Graham (contraction and release; company founded 1926), Alvin Ailey (Revelations, 1960). / B: movement led from the torso, bare feet. A: falls, contractions, floor work. S: low levels and the floor, asymmetry. T: may move with, against or without the beat. E: weight given to gravity, strong contrasts. / The spine curving; weight dropping into the floor; stillness. / Sparse piano and low pad, 68 beats a minute.
3. **Jazz dance.** United States, 1900s, from African American social dance into theater and film. / The cakewalk, the Charleston and the Lindy Hop; theatrical jazz from the 1940s. / Jack Cole (theatrical jazz technique), Katherine Dunham, Bob Fosse. / B: isolations (one body part moves alone), low center. A: kicks, turns, struts. S: presented outward to the audience. T: syncopation, off-beat accents. E: sharp hits and smooth rolls. / Isolations; accents that land between beats; a strong finish. / Swung brass-like stabs and walking bass, 120 beats a minute.
4. **Tap dance.** United States, 1800s. / African American dance (juba, buck dancing) meeting Irish and Scottish step dancing; metal taps from the early 1900s. / William Henry Lane, "Master Juba" (1840s), Bill "Bojangles" Robinson, Gregory Hines. National Tap Dance Day is May 25, Robinson's birthday (US Congress, 1989). / B: relaxed upper body, busy feet. A: shuffles, flaps, heel drops, time steps. S: mostly in place. T: the dancer is a drummer; rhythm and improvisation. E: crisp and light. / Sound over shape; how quiet the top stays; trading phrases. / Light swing bass only; the taps are the music, 104 beats a minute.
5. **Breaking.** The Bronx, New York City, early 1970s, part of hip hop culture. / At block parties DJ Kool Herc looped the "break" of records; b-boys and b-girls danced to the breaks; battles in a circle (the cypher). / DJ Kool Herc, Rock Steady Crew (1977), and the first Olympic breaking event (Paris 2024). / B: whole body, hands to the floor. A: toprock, footwork, power moves, freezes. S: low levels, circles. T: on the breakbeat; freezes hit the accents. E: explosive, personal style. / Going down from standing; the freeze on an accent; style as a signature. / Breakbeat drums with scratch-like sweeps, 110 beats a minute.
6. **Irish step dance.** Ireland; dancing masters taught steps across the country from the 1700s. / Competition (the feis); the Irish Dancing Commission set rules from 1930; Riverdance (Eurovision, Dublin, 1994) took it worldwide. / Riverdance's first leads, Jean Butler and Michael Flatley. / B: upright, arms still at the sides. A: fast, precise footwork, leaps, kicks. S: in place and in lines. T: jigs, reels and hornpipes. E: light in soft shoes, loud in hard shoes. / The still arms; the speed of the feet; crossed feet and turned-out toes. / A reel in 4 on a fiddle-like lead, 112 beats a minute.
7. **Flamenco.** Andalusia, southern Spain; on UNESCO's list of Intangible Cultural Heritage since 2010. / Grew among Gitano (Roma) communities with many Andalusian influences; three parts: cante (song), toque (guitar), baile (dance). / Carmen Amaya, Antonio Gades, Sara Baras. / B: proud upright torso, curving arms (braceo), turning hands (floreo). A: zapateado (footwork as rhythm), turns, stops. S: in place, strong verticals. T: compás; soleá and alegrías cycles of 12 counts with accents on 3, 6, 8, 10 and 12. E: intense, with sudden stops (remate). / How accents fall in the 12; arms against feet; a sharp closing pose. / Plucked guitar rasgueado with palmas (handclaps), 150 counts a minute.
8. **Bharatanatyam.** Tamil Nadu, South India; reshaped and named in the 1930s. / Grew from temple and court dance of hereditary women dancers (sadir), with roots in the Natya Shastra, an ancient treatise on performance; Rukmini Devi Arundale founded Kalakshetra in 1936. / T. Balasaraswati, Rukmini Devi Arundale. / B: araimandi (half-sitting, knees bent outward), mudras (hand gestures that carry meaning), eyes leading. A: adavus (basic step units), striking feet, sculptural poses. S: geometric lines and triangles. T: rhythm syllables (tha ka dhi mi) in tala cycles; Adi tala has 8 beats. E: crisp pure dance (nritta) and expressive storytelling (abhinaya). / The triangle of the bent knees; the hands; feet striking with the syllables. / Barrel-drum-like strokes and small cymbals, Adi tala, 80 beats a minute.

Demo phrases (16 counts unless noted; the builder makes the keyframes):
- Ballet: 1-2 plié in first, 3-4 relevé, arms in fifth, 5-6 tendu front, 7-8 arabesque, 9-10 passé relevé, 11-12 pirouette (one turn), 13-14 close in fifth with port de bras, 15-16 bow (révérence).
- Modern: 1-2 contraction, 3-4 release, 5-6 spiral to the floor, 7-8 roll, 9-10 rise to kneel, 11-12 fall and recovery swing, 13-14 off-balance tilt, 15-16 suspend, then collapse to stillness.
- Jazz: 1-4 head and shoulder isolations, 5-6 jazz walk, 7-8 kick ball change, 9-10 pas de bourrée, 11-12 jazz turn, 13-14 hip isolations, 15-16 hit a pose with spread hands.
- Tap: 1-4 shuffle ball change twice, 5-8 flaps traveling right, 9-12 single time step, 13-14 heel drops, 15-16 stamp, stamp, hold. Foot sounds on every tap.
- Breaking: 1-4 toprock (cross steps, arms open), 5-6 go down to the floor, 7-12 six-step footwork, 13-14 back spin, 15-16 baby freeze.
- Irish: 1-2 hop and point, 3-4 sevens to the right, 5-6 two threes, 7-8 high kick, 9-16 the same to the left. Arms never move.
- Flamenco (2 cycles of 12 = 24 counts): arms rise in braceo with floreo, footwork accents on 3, 6, 8, 10, 12; the second cycle ends in a remate and a held pose on 12.
- Bharatanatyam (2 cycles of 8): araimandi; tatta adavu striking with the syllables; natta adavu stretching to the side; pataka (flat hand) and alapadma (lotus) mudras labeled as they show; a closing pose.

Vocabulary guide (term: definition):
- Body: isolation (one part moves alone); turnout (legs rotated out from the hips); contraction (the torso hollows and curves); release (the torso lengthens back out); gesture (a movement of a part that does not carry weight); mudra (a hand gesture with meaning).
- Action: locomotor (moves through space); nonlocomotor (moves in place); elevation (jumps and leaps); turn; freeze (a held shape); fall and recovery; footwork.
- Space: level (high, middle, low); pathway (the line traveled); direction and facing; general space and personal space; formation; cypher (the circle of a breaking battle).
- Time: tempo; meter (counts in a cycle); accent; syncopation (accent off the main beat); stillness; unison and canon.
- Energy: sustained, percussive, swinging, suspended, collapsing, vibratory; weight (strong or light); flow (free or bound).

## Interactions in detail
- Measured from this demo (computed by the tool from the dancer's own keyframes; the tool's own measures, labeled so): time at each level (percent of counts with the hips in the High, Middle or Low band); reach (widest hand-to-hand span, as a share of the dancer's height); travel (floor distance covered, in body heights); accents per 8 counts (from the rhythm line); stillness (counts with no joint moving more than 5 degrees).
- Trace: a ghost every half count, kept for the last 16 counts (older ones fade to 10 percent); hand paths coral #ffb4a2, foot paths aqua #7de2d1 (in Compare, B uses gold #ffd166 and blue #8fb8ff). Trace is never color alone: hands are solid lines, feet dotted.
- Step one count while paused moves the dancer one count and adds that count's ghosts. 0.5x halves the tempo, music too.
- Critique notes keep their style; changing style in Critique keeps notes for all styles, filtered to the current one (an **All notes** toggle shows every note).
- Saved on this device (localStorage `dance-styles-explorer`): notes and the draft only. **Clear critique** removes both. Nothing else is stored.
- Motion off: the dancer jumps between keyframes; Trace shows ghosts at the same half-count times; rhythm line and music unchanged.
- Sound off: no music, foot sounds or voice; the rhythm line carries the timing.

## Look
- `kit/theme-912.css` with accent `--brand` #c9b3ff (stage lilac) and `--brand-ink` #1c1203. Stage void #0a0c12; dancer #e8edf3 with a 1 px #a6b3c4 outline.
- Contrast: accent on panel #141b25 9.38:1, on section #18202b 8.88:1; brand-ink on accent 10.0:1; dancer on void 16.61:1; trace colors on void: coral 11.45:1, aqua 12.73:1, gold 13.56:1, blue 9.74:1; muted on void 9.18:1.
- Different from gallery-critique (pink #f39cbc), city-skyline-studio (cyan #6fd6e8), virtual-gallery (lime #b8e07a), the 9-12 default gold, and the dance siblings (teal, cobalt, mint).

## Art
none: drawn in code (void stage, dancer from simple shapes, traces, rhythm line). people: false.

## Voice
`knowing-guide` (Sadaltager): "Say in a knowledgeable, friendly way, like a museum curator." Different from gallery-critique (calm-professor), virtual-gallery (wise-mentor), city-skyline-studio (casual-peer) and the dance siblings. Style files and the guide are read on screen; Read speaks them.
| Key | Kind | Line | Stale when |
|---|---|---|---|
| wStyles | how | Pick a style and watch its phrase. Turn on Trace to see the shape it leaves in space. | mode left |
| wCompare | how | Two styles, one clock. Turn on Overlay to lay one trace over the other. | mode left |
| wCritique | how | Press Note when you see something worth saying. It's stamped to that count. | mode left |
| traceHow | how | Each ghost is half a count apart. Hands draw solid lines, feet draw dotted ones. | trace turned off |
| rhythmHow | how | Tall bars are strong accents. Dots are the sound of the feet. | style changed |
| draftHow | how | Insert a note into each part of your draft, so every claim points to a moment. | mode left |
| i.ballet | how | Ballet began in Renaissance courts and grew up in France, which is why its words are French. | style changed |
| i.modern | how | Modern dance broke ballet's rules and let weight, breath and the floor back in. | style changed |
| i.jazz | how | Jazz dance grew from African American social dance into theater and film. | style changed |
| i.tap | how | In tap, the dancer is also the drummer. Listen as much as you watch. | style changed |
| i.breaking | how | Breaking started at Bronx block parties in the 1970s, danced to the breaks of records. | style changed |
| i.irish | how | Irish step dance keeps the arms still, so all the speed lives in the feet. | style changed |
| i.flamenco | how | Flamenco joins song, guitar and dance in a cycle of twelve counts. | style changed |
| i.bharatanatyam | how | Bharatanatyam, from South India, tells stories with the hands and keeps time with the feet. | style changed |
- Lines never play over a running demo: a line queued while playing waits for Pause or the end (`valid: () => !state.playing`), except the welcomes, which play before Play starts.

## Family engine
**dance** (`kit/dance.js`; full description in levels-and-pathways/spec.md). Uses the shared figure, `Dance.poses` plus its style poses, `Dance.dyn`, `Dance.phrase`, `Dance.clock` (meters 3, 4, 8 and 12; seek; 0.5x), `Dance.play` (two dancers in Compare), `Dance.floor('void')`, `Dance.trail` in `'exposure'` mode with `trail.points` (for the Measured readouts), `Dance.music` and `Dance.counts`. Feeds it: 8 style phrases with their accents and foot sounds, 8 tracks. The rhythm line and readouts are this tool's own.

## Sources
- National Core Arts Standards, Dance (2014), high school DA:Re7.1, DA:Re8.1, DA:Re9.1, DA:Cn11.1: https://www.nationalartsstandards.org/
- Ballet (court origins, Académie Royale de Danse 1661, Beauchamp's five positions, Taglioni and La Sylphide 1832): Encyclopaedia Britannica, "ballet": https://www.britannica.com/art/ballet
- Misty Copeland, principal dancer 2015: American Ballet Theatre, https://www.abt.org/people/misty-copeland/
- Modern dance (Duncan, Graham's contraction and release, company 1926): Britannica, "modern dance": https://www.britannica.com/art/modern-dance; Martha Graham Dance Company: https://marthagraham.org/history/
- Alvin Ailey, Revelations (1960): Alvin Ailey American Dance Theater, https://www.alvinailey.org/
- Jazz dance (roots in African American social dance, Jack Cole, Katherine Dunham, Fosse): Britannica, "jazz dance": https://www.britannica.com/art/jazz-dance
- Tap (juba, Irish and Scottish step dance, Master Juba, Bojangles): Britannica, "tap dance": https://www.britannica.com/art/tap-dance; National Tap Dance Day: Public Law 101-21 (1989); Library of Congress, https://www.loc.gov/
- Breaking (Bronx, DJ Kool Herc, breaks, Rock Steady Crew): Britannica, "breakdancing": https://www.britannica.com/art/breakdancing; Olympic debut at Paris 2024: https://olympics.com/en/sports/breaking/
- Irish step dance (dancing masters, the feis, An Coimisiún 1930, Riverdance 1994): An Coimisiún le Rincí Gaelacha, https://www.clrg.ie/; Riverdance, https://riverdance.com/about/
- Flamenco (Andalusia, Gitano communities, cante, toque, baile, UNESCO 2010): UNESCO, https://ich.unesco.org/en/RL/flamenco-00363; Britannica, "flamenco": https://www.britannica.com/art/flamenco; 12-count compás accents: Paco Peña, Toques Flamencos (Musical New Services, 1976).
- Bharatanatyam (Tamil Nadu, sadir, Natya Shastra, 1930s, Kalakshetra 1936, araimandi, adavus, mudras, Adi tala): Britannica, "Bharata natyam": https://www.britannica.com/art/Bharata-natyam; Kalakshetra Foundation, https://www.kalakshetra.in/
- Energy qualities and the Body, Action, Space, Time, Energy frame: Perpich Center for Arts Education, "The Elements of Dance".

## Done when
1. All 8 styles open with their file, phrase and track; each file's facts match Sources.
2. Trace builds a ghost every half count and solid hand and dotted foot paths; Clear trace wipes it; stepping a count adds that count's ghosts.
3. The rhythm line shows flamenco's accents on 3, 6, 8, 10 and 12, and tap's foot sounds as dots.
4. Measured readouts match a hand recomputation from the keyframes for Ballet and Breaking.
5. Compare runs two styles on one clock; Overlay lays both traces in their two color pairs; 12-count and 16-count styles loop on their own.
6. A note stamps the right count; tapping it jumps there; Insert note writes "(count n, term: words)"; the three checks update live.
7. Copy text and Print work; Clear critique empties notes and draft; reload keeps them until cleared.
8. At 1366x768 the stage, rhythm line and transport are visible with the panel; at 1000x625 the preview reads (rhythm line labels 10 px or more); at 375 wide nothing scrolls sideways.
9. Every style file shows the demo disclaimer; no line plays over a running demo.

## Open questions
- Eight styles here: ballet, modern, jazz, tap, breaking, Irish step, flamenco, Bharatanatyam. Keep this set, or swap one (for example West African dance or a Native American social dance) for your students?
- The code dancer stands in for living traditions (breaking, flamenco, Bharatanatyam). OK to ship with the on-screen disclaimer, or should a dancer from each tradition review the demo phrases first?
