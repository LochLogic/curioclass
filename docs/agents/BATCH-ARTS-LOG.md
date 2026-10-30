# Batch ARTS log (2026-10-29)

All 37 remaining Arts and Music tools now have a spec (K-2 11, 3-5 10, 6-8 9, 9-12 7), written by four band agents
under docs/agents/BATCH-ARTS.md, then a cross-band spec check. Every Arts and Music tool now has a spec or is live.

- People images: only mini-documentary-crew asks for any (3 interview frames, Gemini, waits on Cory; an empty
  interview set stands in so the tool works without them). The other 36 need none.
- Spec check: five voice clashes with neighbors in other bands fixed (audience-talkback to knowing-guide,
  folk-song-arranger to hs-narrator, sketchbook-process-journal to clear-teacher, choreography-for-a-cause to
  lively-host, stop-motion-clay-shoot to firm-captain). Image, palette and mechanic repeats were fixed by each band
  agent; no em dashes, no "Curio" alone.

## Open questions for Cory

The ones that need Cory are on the Review Desk as question cards (2026-10-30). Item 2 goes to a fresh review agent per BASELINE.md.

1. name-song-practice: keep the microphone (take 1 and take 2 recorded in memory only, never saved), or drop it?
2. family-dance-night (seven cultural dances) and recital-stage-directions (ballet and jazz cards): cultural and
   accuracy review of the moves and card text before they ship.
3. mini-documentary-crew: approve or drop the 3 Gemini interview frames.
4. Voice bank: 9-12 arts tools borrow younger voices (sketchbook-process-journal, choreography-for-a-cause,
   mini-documentary-crew on friendly-dad). Same gap as the spec revision: add grown-up voices.
5. place-mood-makeover: the lunchroom scene became a playground. Want the lunchroom back?
6. neighborhood-issue-play: the card's "new family who speaks another language" problem became an empty lot (animal
   puppets stand in badly). Bringing it back means people puppets (Gemini) and a sensitivity review.
7. audience-talkback: hear a sample of the two acted character voices before all 20 clips are made?
8. stage-lighting-plot: move its richer light model into kit/stage.js later (kit lights are only off, half, full)?

Decided here (no need to ask): dance and music tools may borrow kit/dance.js and the music-studio engine without
joining those families; in-scene character voices may reuse a neighbor's narrator voice; a voice shared with a
non-neighbor is fine.

## Build-time checks (in the specs' Sources)

- Transcribe "Skip to My Lou", "Simple Gifts", Gymnopedie No. 1 and The Entertainer from named public-domain
  printings (IMSLP) and check notes and bar counts.
- dance-hall-decades: source the Palladium mambo "hotel ballrooms" line or cut it.
- morning-show-crew: a Spanish speaker checks the fixed Spanish announcement.
- viral-video-breakdown: confirm none of the six made-up account names is a real account.
