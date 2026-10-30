# Sound and Picture Book

## One idea
A sound can change what a picture means: the class plans a three-page story (beginning, middle, end), builds each page from painted pieces and gives it a background sound and an action sound, plays the book, then swaps two sounds or two pages and hears the same pictures tell a different story (crickets make the cave quiet; thunder makes it scary).

## Not like
- weekend-drawing-share (k-2, studio, this batch): one free drawing about a real day, told by the child. Here a made-up story is assembled from given pieces and sounds, and the sounds carry meaning.
- field-trip-slideshow (k-2, builder, this batch): a crew presents real trip photos to families, and sound is about volume under a speaker. Here sound is part of the story itself.
- act-it-out (k-2, showdown): plays sound effects under a told folktale. Here the class chooses the sounds and moves them to change the story.
- storyboard-studio and flipbook-studio (6-12, studio): camera shots and timing. Here there are three pages, no camera, and the edit is a swap.
- orchestra-zoo (k-2): instrument sounds. Here the sounds are the world's (rain, footsteps, a snore).

## Who and how
- Grade K-2, media arts, module "Picture and Sound Stories".
- Driver: teacher on a projector or smartboard; the class plans together, votes on pieces and sounds, and tells the story aloud while the book plays. 20 to 30 minutes.
- Standards: NCAS MA:Cr1 (generate ideas: plan a story with picture cards), MA:Cr2 (organize: beginning, middle, end), MA:Cr3 (refine: try changes and choose), MA:Pr4 (combine pictures and sounds into one work).
- Media rule: no camera, upload or recording. Every picture is built from given painted pieces, every sound is made in code.

## Screens and modes
Header: title, `Read`, `Motion`, `Sound` (kit). Mode buttons (`.seg`, icon plus word): `Plan` (lightbulb, default), `Make` (paintbrush), `Play` (open book), `Swap` (two arrows). Every control is 60 px or more with an icon and a word.

**Plan.** Focus: three big page slots across the stage, labeled `Beginning`, `Middle`, `End`. Under them, picture cards in three rows: `Who` (4 character cards), `Where` (6 place cards), `What happens` (8 event cards, each a painted prop or a sound icon with a word). Tap a card, then a slot (or drag): Who goes to all three pages at once; each page takes one Where and one What happens. `Sample book` (book icon) loads "Raccoon's Night Walk" (Content). `Make it` (gold) when every page has a Where.

**Make.** Focus: the page being made, big (16:10, about 75% of the stage), with page tabs `1`, `2`, `3` over it. Trays under it:
- `Place`: six backdrop buttons (thumbnails).
- `Characters`: four characters; tap one to drop it on the page, then its three pose buttons appear (`Happy`, `Scared`, `Sleepy`) and `Flip`.
- `Things`: five props.
- Drag any piece to move it; a 60 px corner handle sizes it; `Remove` takes the selected piece off. At most 4 pieces a page.
- `Sounds` panel (right): two rows, `Background` (6 looping sounds) and `Action` (8 one-shot sounds), each a big icon-and-word button with a small play triangle to audition. Tap the big part to put it on this page (one of each per page; tap again to take it off).
The planned What happens card is shown in a corner of the page as a reminder (it is not drawn on the page).

**Play.** Focus: the page, full stage, as a picture book: the page turns (a soft page-curl in code), the background sound fades in, the action sound plays 0.8 s later, and the pieces do their small animations (bob, sway). Bar: `Back page`, `Next page` (gold), `Auto` (toggle: turns pages every 6 s), `Start again`. The class tells the story out loud.

**Swap.** Focus: the three pages as large thumbnails in a row, each with its two sound chips under it (background and action, icon and word). Drag a sound chip onto another page's chip to swap the two; tap two pages (their numbers) to swap the pages. `Play` (gold) plays the book as in Play. `Undo swap` puts back the last swap. A "What changed?" card shows the last swap as icons ("Thunder moved to page 2").

## Content
**Characters** (painted, three poses each): Raccoon, Turtle, Frog, Fox.
**Places** (painted backdrops): Forest path, Pond, Cave, Campsite at night, Rainy hill, Meadow at sunrise.
**Things** (painted props): lantern, umbrella, berry basket, map, rowboat.
**What happens cards** (plan only): "Goes for a walk" (footprints), "A storm comes" (cloud and lightning), "Gets lost" (map), "Finds food" (berries), "Hears a noise" (ear), "Falls asleep" (moon), "Meets a friend" (two hearts), "Gets home" (house).
**Background sounds** (loop, made in code with Web Audio; gain in brackets):
- Rain: pink noise through a band-pass (1.5 kHz) with random soft ticks (0.18).
- Wind: brown noise with a slow (0.2 Hz) swell of a low-pass between 300 and 900 Hz (0.20).
- Birds: random short chirps (sine sweeps 2.5 to 4 kHz, 80 ms), one every 0.4 to 1.5 s (0.12).
- Crickets: 4.5 kHz pulses in groups of three, every 0.6 s (0.08).
- Stream: white noise through a low-pass at 1.2 kHz with fast random gain (0.14).
- Campfire: brown noise bed plus random crackles (5 ms clicks) (0.15).
**Action sounds** (once; peak gain 0.4 or less):
- Thunder: a low rumble (brown noise, low-pass 120 Hz, 2.5 s decay) after a crack (noise burst 60 ms).
- Splash: a noise burst with a falling band-pass (3 kHz to 400 Hz) over 400 ms.
- Footsteps: four soft thumps (80 Hz sine plus a short noise tick) 400 ms apart.
- Snore: two slow breaths (filtered noise with a 30 Hz buzz) 1.6 s each.
- Munch: three crunches (short noise bursts, 1.5 kHz) 250 ms apart.
- Hoot: two owl-like hoots (sine 380 Hz with a slight pitch fall), 600 ms apart.
- Snap: one sharp twig crack (2 ms click plus a 40 ms noise burst).
- Ta-da: a rising three-note chime (C5 E5 G5, 120 ms apart).

**Sample book: Raccoon's Night Walk** (Who: Raccoon):
1. Beginning: Forest path; Raccoon (Happy) center left with the lantern; Birds, Footsteps. Plan card: Goes for a walk.
2. Middle: Cave; Raccoon (Scared) at the cave mouth; Wind, Snap. Plan card: Hears a noise.
3. End: Campsite at night; Raccoon (Sleepy) by the tent; Crickets, Snore. Plan card: Falls asleep.
Suggested swaps (shown as a hint card in Swap, one at a time with `Another idea`): "Swap the Snap on page 2 with the Snore on page 3." / "Put Thunder on page 2." / "Swap pages 1 and 3." / "Give page 2 Crickets instead of Wind."

## Interactions in detail
- Plan: tapping a filled slot clears that card. Who changes all pages' main character (Make replaces it on each page, keeping its place and pose).
- Make: pieces are stored in page units (0 to 1000 by 0 to 625) so pages look the same at every size. A fifth piece shows "Four pieces is the most on a page." Selecting a piece outlines it with a dashed line and shows `Remove`.
- Sound buttons: the play triangle auditions (stops any other sound); the big part assigns. Assigning a background replaces this page's background; same for action.
- Play: one page at a time; leaving a page fades its background over 300 ms. `Next page` on page 3 shows a "The end" card with `Start again` and `Swap`. Auto never runs past "The end".
- Tap while it plays: Next page, Back page, Start again, a mode switch or a swap acts at once (sounds stop or fade within 300 ms, the page changes at once; Motion off: no curl).
- Swap: swapping two chips of different kinds (a background onto an action) is not allowed: the chip slides back and the hint says "Swap a background with a background, or an action with an action." Swapping pages moves pictures and their sounds together; swapping chips moves only sounds. `Undo swap` keeps up to 10 swaps.
- Save: the book saves itself on this device after every change (localStorage `curio-spb-book`, in try/catch; one book). `New book` (Plan bar) asks `Yes, start new` or `Keep my book`. If storage fails, the book still works for this visit.
- Empty pages: a page with no place shows a soft cream page with the page word. Play works with any number of filled pages.
- Sound off: the sound chips still show, and Play shows a small speaker-slash under the page.
- Motion off: no page curl, bob or sway; timing the same. Keyboard: arrows move the selected piece 10 units, Delete removes it, Right and Left turn pages in Play.

## Look
- Accent (`--brand`) #1e3a8a night-story navy (header, Next page, selected chips). Paper #f6f3ea, ink #1c2030, muted #5a5c66. The book page sits on a warm linen table color #e8dfcc with a soft shadow. Background chips are rounded rectangles, action chips are circles (shape plus icon plus word, never color alone).
- Contrast (WCAG 2.1, computed): white on brand 10.36:1; brand on paper 9.34:1; ink on paper 14.57:1; muted on paper 5.99:1.
- Different from the k-2 arts neighbors: line-safari #c0612b, art-passport #1f5f8b, beat-buddies #c2482f, orchestra-zoo #2f7a4a, sound-elevator #3d4fa8, act-it-out #7d2e7f, levels-and-pathways #00798c.

## Art
Local FLUX (`scripts/localart.py`). No people. One soft gouache and ink picture-book style, so pieces sit well on any backdrop.
- 6 backdrops, each "<place>, soft gouache and ink picture book illustration, the lower half open ground"; 16:10; cutout no; people no; Make and Play pages: a winding forest path between tall pines in daylight; a small pond with reeds and lily pads; the dark rocky mouth of a cave in a hillside; a forest campsite at night with a small tent and a ring of stones, stars above; a grassy hill under grey rain clouds; a meadow with wildflowers at sunrise.
- 12 character cutouts, "A small <animal> character, <pose>, standing on the ground, soft gouache and ink picture book illustration, plain white background", 1:1, cutout yes, people no: raccoon, turtle, frog, fox; poses: smiling and waving a paw; startled with wide eyes and raised fur; curled up asleep with eyes closed. Swapped by the pose buttons; bob and sway in code.
- 5 props, "<thing>, soft gouache and ink picture book illustration, plain white background", 1:1, cutout yes, people no: a glowing camping lantern; an open red umbrella; a small basket of berries; a folded paper map with a blank face; a small wooden rowboat.
23 images, none with people. Drawn in code: the page curl, chips, sound icons, plan slots and cards' icons, the reminder corner.

## Voice
Bank voice `gravel-ranger` (Algenib), style "Say warmly with a gravelly voice, like an old park ranger telling stories". Fits a book of forest stories. Not used by any K-2 arts neighbor (line-safari bright-teacher, art-passport knowing-guide, beat-buddies lively-host, orchestra-zoo playful-friend, sound-elevator hero-coach, act-it-out gentle-storyteller, levels-and-pathways warm-teacher) or by another K-2 spec in this batch. `Curio.voice` with `scope: () => state.mode + ':' + state.page`. The ranger never reads the story (the class tells it); lines never play over a page's action sound (they wait for it, then play over the background lowered 6 dB).

- how, welcome (Plan; stale when a card is placed): "Every good story has a beginning, a middle and an end. Tap a Who card, then a page."
- how, Who placed first time (stale when a Where card is placed): "Now, where does each part happen? Tap a Where card, then a page."
- event, a slot filled: "Beginning: <card>." / "Middle: <card>." / "End: <card>." (spoken for Where and What happens; built from the card word, 3 x 14 lines)
- event, all pages have a place: "That's a plan. Tap Make it."
- how, welcome (Make; stale when a piece is placed): "Build page one. Tap a place, then add a character."
- how, first piece placed (stale when a sound is assigned): "Now give the page sounds. Pick a background sound and an action sound."
- event, a sound assigned: the sound's word ("Rain." "Thunder!", 14 lines)
- how, welcome (Play; stale when Next page is tapped): "Tell the story out loud while the book plays. Tap Next page to turn."
- event, "The end" card: "The end. Now try Swap, and see what changes."
- how, welcome (Swap; stale when a swap is made): "Drag a sound to another page to swap them. Or tap two page numbers."
- event, each swap: "Swapped! Tap Play. Is it a different story now?"
- event, wrong-kind swap: "Swap a background with a background, or an action with an action."
- event, each suggested swap card in Content when shown.
- Read speaks the hint, or the plan cards of the current page.

## Family engine
none

## Sources
- National Core Arts Standards, Media Arts, grades K to 2 (MA:Cr1, MA:Cr2, MA:Cr3, MA:Pr4): https://www.nationalartsstandards.org
- Sound shapes how a picture is read (the same image with different sound reads differently): Chion, M. (1994), Audio-Vision: Sound on Screen, Columbia University Press (added value). Used as a general idea, not a claim on screen.
- All sounds are made in code; all pictures are original paintings (Art).
- Checks run (Python, 2026-10-29): background gains 0.08 to 0.20 and action peaks at 0.4 keep a page under 0.6 combined (no clipping at a 1.0 limit). Page timing: action at 0.8 s, Auto turns at 6 s, so the longest action (Snore, 2 x 1.6 = 3.2 s) ends at 4.0 s, before the turn. Page units 1000 by 625 match 16:10. Every sample-book swap suggestion names chips that exist on the named pages. Contrast ratios as listed.

## Done when
1. Focus: at 1366x768 and 680x425 the page is the largest thing in Make and Play, and the three pages are large in Swap with readable chips.
2. Sample book plays three pages with the right pieces and sounds; every suggested swap can be done and played.
3. Every background loops without a click at the loop point, and every action plays once, 0.8 s after the page opens.
4. Swapping chips moves only sounds; swapping pages moves pictures with their sounds; wrong-kind swaps slide back with the line; Undo swap reverses up to 10.
5. Tap while it plays: Next page, Back page, a mode switch or a swap mid-page stops or fades sounds within 300 ms and acts at once.
6. The book survives a reload; storage blocked still lets the class make and play a book.
7. How-to lines are spoken once in five actions; the ranger never speaks over an action sound.
8. Every control is 60 px or more with an icon and a word; the sound panel and Next page are visible without scrolling at every size in STANDARDS.md.
9. Motion off: no curl, bob or sway; timing unchanged.
10. No camera, microphone, upload or network request anywhere.
