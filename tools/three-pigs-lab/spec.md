# Three Pigs Lab: spec notes

The tool was built before specs were kept per tool; see the comment at the top of src.html and plan.md for the lesson. This file holds the voice spec.

## Voice

`voice/lines.json`: `"bank": "gentle-storyteller"`, `"voice": "Vindemiatrix"`, `"style": "Say gently and expressively, like a grandmother reading a picture book aloud"`. One narrator voice for everything, the wolf and the pig included (the lines carry the character, not extra voices). `python scripts/neighbors.py three-pigs-lab` showed no near neighbor with this voice (its only other user is walk-in-their-shoes, not a neighbor). 87 lines, recorded with scripts/localvoice.py (Qwen3-TTS cloning the bank voice).

Queue: the kit (kit/curio.js) plays a recording when the exact text has one and falls back to the browser voice otherwise. The tool's `voice()` follows collision-lab's narrate/hush/readNow/firstTap pattern: lines wait for Read, a line is marked said when it starts, `hush()` drops queued lines and releases every waiter (a stopped clip never fires `ended`). A new test, Rebuild or a material change resets the scene and hushes.

Lines:
1. Welcome, once, after the first tap (skipped when that tap starts a test, left unsaid): "Help the pig build a house. Pick the walls and the roof, then test them with the wolf, the rain, a peek and a cold night."
2. Story beats, said in order; each beat waits for both its reading time and its clip: "Little pig, little pig, let me come in!", "Not by the hair of my chinny chin chin!", "Then I'll huff," (bubble shows "Then I'll HUFF..."), "and I'll puff!" (bubble "...and I'll PUFF!"), "Huff... puff... phew!" (strong walls), "Hi there!" (see-through walls), "Is that... a shadow?" (paper). The capitals stay on screen; the voice gets plain words so it doesn't spell them out.
3. Results, said when each test ends and read by Read: 7 materials x 4 tests, "<Material> walls: <word>" (Wolf, Peek, Cold night) and "<Material> roof: <word>" (Rain), the same text as the result card.
4. Read before any build: "What do you think will happen? Predict first!" After a material pick, Read says the build line in two parts: "<Wall> walls and a <roof> roof." (49) then "Predict first, then test!".

Read order: the result card, else the speech bubble on screen, else the build line. Every spoken string is in lines.json (checked by enumerating every combination from src.html); there is no intentional browser-voice text.
