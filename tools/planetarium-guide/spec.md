# Planetarium Guide

## One idea
Under a dark dome, the student becomes tonight's guide: they pick and order four stops on a sky tour, choose the facts and one picture or sound for each, record each stop's lines, and give the show twice, first for kindergartners on field trip day and then for visiting scientists, so they hear that a clear talk has an order, a pace and words that fit who is listening.

## Not like
- show-and-tell-spotlight (K-2, concept): one object and a listener switch. Here a planned four-stop talk with media at grades 3-5.
- script-read-through (3-5, concept): reading someone else's script. Here writing and pacing your own talk.
- audience-shift-briefing (high school, concept): a formal briefing. Here a kid sky show.
- radio-hour-notes (3-5, spec): listening to speakers. Here being the speaker.
- mood-in-the-pictures (3-5, spec): what media add to a story. Here choosing media to make a talk's main ideas stick.

## Who and how
- Grades 3-5, ELA, module "Presenting Clearly" (Speaking and Listening). Standards: SL.3.4, SL.3.5, SL.3.6, SL.4.4, SL.4.5, SL.4.6, SL.5.4, SL.5.5, SL.5.6.
- Driver: one student (tool.json `driver: "student"`). Records with the microphone; the privacy line always shows: "Your recordings stay on this device and are gone when you close the page." No speech recognition.
- tool.json `modes: []`, `minutes: "20-30"`, `grades_label: "Grades 3-5"`. Without a microphone, the student can still build the show and read it with the browser's speech voice, and a note says so.
- Nothing is saved after the page closes. `Print` prints the show plan (stops, facts, media, lines).

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| SL.3.4, SL.4.4, SL.5.4 | Order four stops so the tour makes sense (nearest to farthest, or a story order), pick two facts and one detail per stop | the tour path across the dome | 2, 3 |
| SL.3.4, SL.4.4, SL.5.4 | Record each stop; the pace meter compares recording length and pauses with the word count | the pace meter: too fast, just right, too slow | 4 |
| SL.4.5, SL.5.5 | Attach one picture or sound per stop and say why it helps (shows size, shows motion, makes it stick) | the media icon at each stop | 5 |
| SL.3.6, SL.4.6, SL.5.6 | Audience switch: swap each stop's line between formal and informal cards to fit kindergartners or scientists; complete sentences required | the two show scripts side by side | 6 |
| SL.3.5 | Grade 3 closing: record a reading of Jane Taylor's "The Star" (1806) at a clear pace | the poem on the dome with the pace meter | 7 |

## Screens and modes
Header (kit): title "Planetarium Guide"; `Show`, `Audience`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A dark dome with stars, a podium, and Dr. Nova the barn owl, the planetarium director. First hint: "Tap a stop on the dome to see what it is." The first tap names the stop; the welcome is queued after it (`welcomeAfter: true`).

**Plan.** Six possible stops glow on the dome: the Moon, Mars, Jupiter, Saturn's rings, the Big Dipper, a comet. Pick four and drag them onto the tour path in order. The order check accepts two rules from data: distance order (Moon, then planets by distance from the Sun, then the Big Dipper's stars, which are far beyond the planets) or a "story" order the student names from a card (bright to faint, or near to far). A comet can go anywhere with a reason card. For each stop: 5 fact cards; pick two facts and one detail.

**Media.** Each stop offers three media: a picture (scale picture, like Earth beside Jupiter), a sound (a made-in-code tone pattern for the comet's tail, a ring hum), or an animation (the Moon's phases). Pick one and its reason card.

**Record.** For each stop, the lines appear as a script (the two facts and the detail, turned into sentences from cards; grade 5 can type their own). `Record` captures up to 45 seconds; the pace meter uses words per minute from the script's word count and the recording length, minus long pauses detected by volume (more than 2 seconds of quiet counts as a pause). Just right is 110 to 160 words per minute (a design range). Play back and re-record freely.

**Audience switch.** Two audience cards: kindergartners on field trip day, and visiting scientists. Each stop's lines have a formal and an informal card ("Saturn's rings are made of ice and rock." or "Guess what? Saturn wears a hula hoop of ice!"). Pick per audience; a mismatch gets the audience's reaction picture (a puzzled kindergartner; a scientist raising an eyebrow). Then record both shows and play them back to back. A fragment card ("Big rings. Ice.") is never accepted for either audience: "Use whole sentences so everyone can follow."

**Closing (grade 3).** "The Star" (Jane Taylor, 1806, public domain): the first stanza appears on the dome; record a reading with the pace meter.

At 1366x768 the dome and the script panel fit; at 680x425 the panel slides over the dome.

## Content
Fact cards (written for Curio Class, 5 per stop, sourced): Moon (about 384,000 km away; we always see the same side; its light is reflected sunlight; astronauts walked on it in 1969; phases come from how much of the lit side we see). Mars (the fourth planet; red from iron-rich dust; has the tallest volcano known, Olympus Mons; two small moons; a day a bit longer than ours). Jupiter (the biggest planet; more than 1,300 Earths could fit inside; the Great Red Spot is a giant storm; dozens of moons; made mostly of gas). Saturn's rings (made of ice and rock pieces; very wide but very thin; Saturn is the sixth planet; it could float in a big enough bathtub, a common way to say it is less dense than water; many moons). Big Dipper (seven bright stars; part of a bigger constellation, Ursa Major; two of its stars point to the North Star; its stars are much farther than the planets). Comet (a ball of ice and dust; grows a tail when near the Sun; the tail points away from the Sun; Halley's Comet comes back about every 76 years).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Recording uses the browser's media recorder; audio stays in memory only, and closing the page clears it.
- The pace meter never judges words, only length and pauses against the script's word count; it shows a range, not a grade.
- Formal and informal cards flip with one tap; the reaction picture appears after each pick.
- Motion off: the dome stays still and stops jump.

## Look
- Accent `--brand` #1f2f6b night navy (header, podium, buttons); gold #f4c542 (stars, the tour path, the pace meter's just-right zone); paper #f4f6fc (panels); ink #0d1430; muted #4c5470. The dome itself is a dark scene with gold stars; text on the dome sits on paper panels.
- Contrast (WCAG 2.1, computed): white on brand 12.52:1; brand on paper 11.59:1; ink on paper 16.76:1; muted on paper 6.92:1; ink on gold 11.13:1.
- Never color alone: pace meter zones have words (too fast, just right, too slow); audience reactions are pictures with captions.
- Different from this batch (gallery plum, radio orange, reading-table green, story teal).

## Art
Local FLUX (`scripts/localart.py`). Audiences are animals (kindergarten bunnies, scientist owls in lab coats), so no people art.
- dome (1): "Inside a planetarium dome at night with stars and a podium, soft gouache, no text"; 16:9; cutout no.
- Dr. Nova (4, point, listen, nod, applaud): "A friendly barn owl planetarium director with a pointer <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- stops (6): "<the Moon / Mars / Jupiter with its storm / Saturn and its rings / the Big Dipper stars / a comet with its tail>, space illustration, dark background"; 1:1; cutout no.
- scale pictures (6), audience reactions (6).
About 23 images. Drawn in code: tour path, pace meter, cards, tones.

## Voice
Bank voice `upbeat-guide` as Dr. Nova (unique in this batch). The student's own voice is the show. `Curio.voice` with `scope: () => state.stage + ':' + state.stop`, `welcomeAfter: true`.
- event `stop`: "{Saturn's rings}."
- how `welcome`: "Tonight's show needs a guide, and that's you. Pick four stops, put them in an order that makes sense, then tell the audience about each one."
- how `orderHow`: "Drag four stops onto the tour path in an order you can explain."
- event `orderOk` / `orderHint`: "That tour makes sense." / "Try near to far. Which is closest to us?"
- how `recordHow`: "Tap Record and read your lines. Your recording stays on this device."
- event `pace`: "Just right." / "A little fast. Try a breath at each period." / "A little slow. Keep it moving."
- how `audienceHow`: "Who's in the seats? Pick the line that fits them."
- event `fragment`: "Use whole sentences so everyone can follow."
- event `bothShows`: "Same sky, two shows. Hear the difference?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tour order | Random order | Accepted only if it follows a named rule; 45 of 360 random four-stop orders pass (checked). |
| Pace meter | Mumble fast | The meter checks pace only, by design; playback lets the student hear it. Not a gate. |
| Audience cards | Pick all formal | Kindergartners react puzzled to formal lines; scientists to informal. Each stop has a fit per audience. |
| Fragments | Use the short cards | Fragment cards never fit any audience. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a stop: `stop`, `welcome` (queued, first time).
2. Plan: `orderHow`; check: `orderOk` or `orderHint`.
3. Record: `recordHow`; after each take: `pace`.
4. Audience: `audienceHow`; fragment: `fragment`; both recorded: `bothShows`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| SL.3.4 to SL.5.6 wording | thecorestandards.org, Speaking and Listening Grades 3 to 5 | CCSS ELA 2010 PDF | yes |
| Moon facts (about 384,000 km; same side faces us; reflected light; 1969 landing; phases) | NASA Science, Moon | ESA, the Moon | yes |
| Mars facts (fourth planet; iron-rich red dust; Olympus Mons; two moons; day about 24.6 hours) | NASA Science, Mars | ESA, Mars | yes |
| Jupiter facts (largest; over 1,300 Earths by volume; Great Red Spot storm; mostly hydrogen and helium) | NASA Science, Jupiter | ESA, Jupiter | yes |
| Saturn facts (ring particles of ice and rock; rings wide but thin; sixth planet; less dense than water) | NASA Science, Saturn | ESA, Saturn | yes |
| Big Dipper is part of Ursa Major; its pointer stars lead to Polaris | NASA Science, skywatching guide to the Big Dipper | Royal Museums Greenwich, the Plough (Big Dipper) | yes |
| Comet tails point away from the Sun; Halley's period about 76 years | NASA Science, comets | ESA, comets | yes |
| "The Star" by Jane Taylor, 1806, public domain | Poetry Foundation, Jane Taylor | Project Gutenberg, Rhymes for the Nursery | yes |
Backed twice: 8. Cut: 0.

Design choices (not claims): the 110 to 160 words per minute range and the 2-second pause.

Checks run (Python, scratchpad b9, 2026-11-08): 45 of 360 random four-stop orders (12.5 percent) pass the distance rule; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the dome and script fit; at 680x425 the panel slides over.
2. The tour accepts a distance order or a named story order. (SL.x.4)
3. Each stop takes two facts and one detail. (SL.x.4)
4. Recording works and the pace meter shows its zone from length, pauses and word count. (SL.x.4, SL.3.5)
5. Each stop takes one medium with a reason card. (SL.4.5, SL.5.5)
6. The audience switch shows reactions, rejects fragments and plays both shows back to back. (SL.x.6)
7. The grade 3 closing records "The Star" with the meter. (SL.3.5)
8. The privacy line always shows; without a microphone, the speech voice reads the show.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: the dome is still; no network requests.

## Open questions
- None for Cory.
