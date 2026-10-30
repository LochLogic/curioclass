# Batch ARTS: spec the last 37 Arts and Music tools (2026-10-29)

Spec only. Each agent owns one grade band and writes its specs one at a time in the order below, following
`docs/agents/SPEC.md` (with the five rules from Cory's reviews) and `docs/agents/STANDARDS.md`. Repo for this wave:
`S:\CurioClass-media` (a worktree of S:\CurioClass). Write only `tools/<id>/spec.md` for your own ids. Do not commit.

| Band | Agent | Tools, in order |
|---|---|---|
| K-2 | A1 | weekend-drawing-share, hallway-art-museum, parade-and-bedtime-music, name-song-practice, puppet-show-feelings, moon-base-drama, feeling-scarf-dance, family-dance-night, sound-and-picture-book, field-trip-slideshow, cereal-ad-questions |
| 3-5 | A2 | traveling-art-show, place-mood-makeover, recorder-concert-rehearsal, cartoon-soundtrack-mixer, neighborhood-issue-play, audience-talkback, poem-to-movement, recital-stage-directions, stop-motion-clay-shoot, toy-ad-reality-check |
| 6-8 | A3 | school-wall-mural, folk-song-arranger, cover-version-review, three-viewpoints-scene, scene-staging-comparison, dancers-on-tour, dance-hall-decades, morning-show-crew, viral-video-breakdown |
| 9-12 | A4 | sketchbook-process-journal, recital-practice-plan, stage-lighting-plot, monologue-rehearsal, choreography-for-a-cause, museum-courtyard-performance, mini-documentary-crew |

## Notes for this subject

- **Neighbors.** 35 Arts and Music tools already have a spec or are live. `neighbors.py` lists them; read the specs of
  the close ones before you pick a mechanic, image list, palette or voice.
- **Art.** Arts tools look at art, so painted images matter most here. Local FLUX (`scripts/localart.py`) for
  anything without people. People, faces and hands go to Gemini (`scripts/art.py`), which is set aside for now, so
  every `people: true` image waits on Cory: prefer a stage, an instrument, a costume on a stand, a puppet, an animal or
  a silhouette in code when it teaches just as well, and keep people only where the person is the point. Artworks a
  student studies are original paintings in a named style, never copies of a real work; real works may be named and
  linked in Sources, not reproduced.
- **Music and sound.** Notes, rhythms and mixes are made in code with Web Audio (the kit's sound). Original tunes or
  public-domain songs only (check the date in Sources). Any tool that plays music in time follows the voice "speak now
  and wait" rule and keeps every control live while it plays.
- **Dance and movement.** Students move in the room, not on screen. A figure on screen is a simple code figure or a
  painted cutout set (one pose per cutout), never a drawn person from a local model.
- **Media tools** (ads, videos, documentaries, slideshows): no camera, upload or recording. Clips are made of painted
  frames and code; anything the student "films" is assembled from given pieces.
- **Voice.** Pick a kept bank voice (`voices/bank.json`, status "kept") that no neighbor and no other spec in your band
  uses. If the 9-12 voices are used up, pick the closest fit and say so in Open questions.
- **Band check.** After your last spec, read all your band's specs side by side and fix repeats (images, palettes,
  voices, mechanics) in the files.

## Report (short)

One line per spec: the one idea, voice and accent, images (and how many with people), open questions only Cory can
decide. Then the band check result. Plain words, no em dashes, "Curio Class" never "Curio" alone.
