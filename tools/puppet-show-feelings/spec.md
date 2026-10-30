# Puppet Show Feelings

## One idea
A sock puppet's face never changes, so the class learns to read a feeling from everything else: watch Pom's short show, then go backstage and change one thing at a time (how the head tilts, how fast Pom talks, how much Pom bounces) and watch the same line turn sad, calm, proud, happy, excited or worried.

## Not like
- act-it-out (k-2, showdown): the class acts a folktale wearing costume pieces. Here the class watches and directs one puppet, and the lesson is reading a feeling, not playing a part.
- director-s-chair (9-12, story): directs a classic scene in five theater traditions. Here there is one puppet, three dials and six feelings, for five-year-olds.
- feeling-scarf-dance (k-2, studio, this batch): the class dances a feeling. Here the class reads a feeling someone else shows, and names the clue.
- moon-base-drama (k-2, roleplay, this batch): the class is in the story. Here the class is the audience, then the puppeteer.
- beat-buddies, levels-and-pathways (k-2): copy movement. Here movement is a clue to read, not a move to copy.

## Who and how
- Grade K-2, theater, module "Puppets and Feelings".
- Driver: teacher on a projector or smartboard; the class names feelings out loud, votes for an ending, and may make their own hand into a puppet. 15 to 20 minutes.
- Standards: NCAS TH:Re7 (recognize how a character's body and voice show feelings), TH:Re8 (say what a choice shows; preferences: choose the ending you like), TH:Cn10 (connect a character's feelings to your own life).

## Screens and modes
Header: title, `Read`, `Motion`, `Sound` (kit). Mode buttons (`.seg`, icon plus word): `Show` (theater icon, default), `Backstage` (sliders icon), `Like me` (heart icon). Every control is 60 px or more with an icon and a word.

**Show.** Focus: the puppet theater, a painted cardboard-box stage filling the stage area, Pom the sock puppet in the middle of its opening, about half the theater's height. Under it: `Back`, `Next` (gold), `Again` (replays the scene). A small scene strip (6 dots) shows where the story is. On the ending scene, three big ending buttons appear on the stage: `Dot helps` (two puppets icon), `A new kite` (kite and scissors), `Wait for the wind` (wind lines).
- Each scene: the narrator tells the line; Pom moves with the scene's settings (head, bounce) and says a short babble line (puppet talk made in code) at the scene's voice speed. Then a question card: "How does Pom feel?" with a big `Show me` button that flips the card to the feeling's face icon and word.

**Backstage.** Focus: Pom, big, alone on the bare stage (the backdrop dimmed), and the three control rows right under the stage, each with three big buttons (icon plus word):
- `Head`: `Down`, `Straight`, `Up` (each a small sock icon tilted that way).
- `Voice`: `Slow` (snail), `Middle` (walking shoe), `Fast` (hare).
- `Bounce`: `Still` (dot), `Small` (small arc), `Big` (big arc).
- `Say it` (speech bubble) repeats Pom's line in babble. `Line` cycles the six scene lines (shown as the scene picture on the button) so the class can direct any line.
- `Audience says` (gold, eye icon) shows the feeling the settings read as, with its face icon and word, on a card over the stage.
- A thin "what changed" row under the controls shows the last change as icon arrows ("Head: Down to Up").
- Try it (optional, `Try it` toggle): a target card "Make Pom look proud" (cycles through the six); when the settings read as the target, the card gets a check and the narrator praises.

**Like me.** Focus: Pom in the middle of a simple painted bedroom shelf (the puppet resting), and six big feeling cards in a ring around Pom (face icon plus word). Tap a card: Pom takes that feeling's settings, and the prompt says "When did you feel <feeling>? Tell a friend." `Ending vote` (ballot icon) shows the three endings as big tiles; the teacher taps the one with the most hands (no counting on screen) and the narrator says why some people like that ending.

## Content
**Feelings** (face icon drawn in code: brows and mouth only): sad, calm, proud, happy, excited, worried.

**What the audience reads** (Head x Voice x Bounce; every one of the 27 settings):
| Head | Voice | Still | Small | Big |
|---|---|---|---|---|
| Down | Slow | sad | sad | sad |
| Down | Middle | sad | worried | worried |
| Down | Fast | worried | worried | worried |
| Straight | Slow | calm | calm | happy |
| Straight | Middle | calm | happy | excited |
| Straight | Fast | worried | worried | excited |
| Up | Slow | proud | proud | happy |
| Up | Middle | proud | happy | excited |
| Up | Fast | happy | excited | excited |

**Motion and voice numbers:** Head tilt: Down 28 degrees forward (the sock droops), Straight 0, Up 18 degrees back. Bounce: Still 0, Small 12 px at 1.2 bounces a second, Big 34 px at 2.2 bounces a second (scaled with the stage). Babble: syllables of 2 to 3 sine-and-noise blips, 150 ms each at Middle; Slow 260 ms and 15% lower pitch; Fast 95 ms and 15% higher. Pom's mouth opens on each syllable.

**Show scenes** (narrator line; Pom's settings as Head, Voice, Bounce; babble syllables; feeling):
1. "This is Pom, a sock puppet. Pom has a brand new red kite." Up, Middle, Small; 6; happy.
2. "Whoosh! The wind lifts the kite up high." Up, Fast, Big; 8; excited.
3. "Oh no! The kite is stuck in the tall tree." Down, Fast, Small; 7; worried.
4. "Pom tugs and tugs. The kite will not come down." Down, Slow, Still; 5; sad.
5. "What happens next? Tap an ending." (Pom: Straight, Slow, Still; no babble.)
6. Endings:
   - Dot helps: "Pom's friend Dot comes by with a long stick. Together they wiggle the kite free!" Pom and Dot: Up, Fast, Big; 8; excited.
   - A new kite: "Pom finds paper and string, and makes a brand new kite, all by herself." Up, Slow, Still; 6; proud.
   - Wait for the wind: "Pom sits under the tree and waits. A soft breeze drops the kite right down." Straight, Slow, Still; 5; calm.

**Ending vote lines:** Dot helps: "Some people like it when a friend helps." / A new kite: "Some people like it when you fix it yourself." / Wait for the wind: "Some people like a quiet, patient ending."

## Interactions in detail
- Every setting change in Backstage shows at once: Pom eases to the new tilt over 250 ms, the bounce changes size and speed from the current position (no jump), and a babble line plays at the new speed. A new tap cuts the old babble.
- The audience card hides when any setting changes (so the class reads the puppet first), and stays hidden until `Audience says` is tapped again.
- Try it: the target check is tested on every change; the praise is an event (every time a target is met). A new target appears after 2 s, or on `Next target`.
- Show: `Next` and `Back` are never locked; a tap during a line or a babble stops it and goes. On scene 5 `Next` is disabled until an ending is tapped (the hint says so, and no line names Next there). `Again` replays the scene. After an ending, `Next` becomes `Play again` (scene 1) and the ending buttons stay so a different one can be chosen.
- Like me: the cards cycle the prompt; the ending vote can be changed.
- Nothing is saved. Switching modes keeps Backstage's settings.
- Motion off: no bounce or ease (tilt jumps), but the babble timing is the same; the bounce row's chosen button still shows the choice and the "what changed" row still updates. Keyboard: H, V and B step Head, Voice and Bounce; A is Audience says; arrows are Next and Back in Show.

## Look
- Accent (`--brand`) #0b7a5f jade (header, Next, chosen control). Paper #f4f8f3, ink #16241f, muted #4f625b. Theater: corrugated cardboard browns with a painted red curtain; the bare backstage is a soft spotlight on a warm grey.
- Feeling icons always pair the face with the word. Chosen controls show a check icon and a thicker border, never only color.
- Contrast (WCAG 2.1, computed): white on brand 5.30:1; brand on paper 4.94:1; ink on paper 14.98:1; muted on paper 6.06:1.
- Different from the k-2 arts neighbors: line-safari #c0612b, art-passport #1f5f8b, beat-buddies #c2482f, orchestra-zoo #2f7a4a, sound-elevator #3d4fa8, act-it-out #7d2e7f, levels-and-pathways #00798c.

## Art
Local FLUX (`scripts/localart.py`). No people: the puppets are socks seen from the wrist up, with the lower edge hidden behind the theater's ledge. One cut-paper and gouache style.
- theater: "A homemade puppet theater made from a big cardboard box, a rectangle cut in the front with a red fabric curtain tied back, a blank cardboard sign area on top, cut paper and gouache illustration, the opening plain white"; 4:3; cutout yes (the opening cut out); people no; frames every scene.
- park: "A sunny park with a grassy hill and one tall leafy tree on the right, blue sky with a few clouds, cut paper and gouache illustration"; 4:3; cutout no; people no; the backdrop inside the theater for scenes 1 to 6.
- pom-closed, pom-open: "A striped orange and teal sock puppet with two big button eyes and a red felt tongue, mouth <closed / wide open>, upright as if on a hand, seen from the side front, cut paper and gouache illustration, plain white background"; 3:4; cutout yes; people no; Pom, swapped on every babble syllable, rotated for tilt around the bottom center.
- dot-closed, dot-open: the same kind of sock puppet in purple with yellow polka dots and one big button eye patch; 3:4; cutout yes; people no; Dot in the first ending.
- kite: "A red diamond kite with a long ribbon tail, cut paper and gouache illustration, plain white background"; 3:4; cutout yes; people no; in the sky (scene 2), in the tree (3 and 4), in Pom's mouth (endings).
- new-kite: the same kite in yellow and green stripes; 3:4; cutout yes; people no; ending A new kite.
- stick: "A long thin wooden stick, cut paper and gouache illustration, plain white background"; 4:1; cutout yes; people no; ending Dot helps.
- shelf: "A child's bedroom shelf with books and a small plant, soft light, cut paper and gouache illustration, the middle of the shelf empty"; 16:10; cutout no; people no; the Like me backdrop.
10 images, none with people. Drawn in code: the feeling faces, controls and their icons, the "what changed" row, the dimming, and the breeze lines.

## Voice
Bank voice `smooth-narrator` (Algieba), style "Say smoothly and warmly, like an audiobook narrator". The storyteller of the show; Pom only babbles (code). Not used by any K-2 arts neighbor (line-safari bright-teacher, art-passport knowing-guide, beat-buddies lively-host, orchestra-zoo playful-friend, sound-elevator hero-coach, act-it-out gentle-storyteller, levels-and-pathways warm-teacher) or by another K-2 spec in this batch. `Curio.voice` with `scope: () => state.mode + ':' + state.scene`.

- how, welcome (Show; stale once Next is tapped): "Welcome to the puppet show! Watch Pom. Then tap Next."
- event: each scene line in Content, when the scene opens (stale when the scene changes).
- event, after each scene's babble: "How does Pom feel? Tell me. Then tap Show me." (spoken every scene: it is the question, not a how-to; stale when Show me or Next is tapped)
- event, Show me: "Pom feels <feeling>." (6 lines)
- how, ending scene (stale when an ending is tapped): "Choose an ending. Tap Dot helps, A new kite, or Wait for the wind."
- how, welcome (Backstage; stale on the first control tap): "You're the puppeteer now. Change one thing at a time: Head, Voice or Bounce."
- how, after the first change (stale when Audience says is tapped): "What do you see now? Say it. Then tap Audience says."
- event, Audience says: "The audience sees <feeling>." (6 lines; stale on the next change)
- event, once per page load the first time a single change flips the feeling (how): "Only one thing changed, and the feeling changed!"
- event, Try it met: "Yes! That's <feeling>!" (6 lines)
- how, welcome (Like me; stale when a card is tapped): "Puppets have feelings like we do. Tap a feeling."
- event, a card tapped: "When did you feel <feeling>? Tell a friend." (6 lines)
- event, ending vote: each ending vote line in Content.
- Read speaks the scene line (Show), the feeling and controls (Backstage), or the prompt (Like me).

## Family engine
none

## Sources
- National Core Arts Standards, Theatre, grades K to 2 (TH:Re7, TH:Re8, TH:Cn10): https://www.nationalartsstandards.org
- Body posture and movement carry emotion without a face (slumped and slow for sadness, upright for pride, quick and big for joy): Dael, Mortillaro and Scherer (2012), "Emotion expression in body action and posture", Emotion 12(5), 1085 to 1101; Wallbott (1998), "Bodily expression of emotion", European Journal of Social Psychology 28, 879 to 896. Speech rate as a cue (slow for sadness, fast for fear and joy): Juslin and Laukka (2003), Psychological Bulletin 129(5), 770 to 814. The table is a simplified classroom model of these cues, not a rule.
- The story of Pom and the kite is original.
- Checks run (Python, 2026-10-29): coded Head -1/0/1, Voice -1/0/1, Bounce 0/1/2 and took the nearest of six prototypes (sad -1,-1,0; calm 0,-1,0; proud 1,-1,0; happy 1,0,1; excited 1,1,2; worried -1,1,1) for all 27 settings; five ties (Straight-Middle-Big, Up-Slow-Small, Up-Middle-Still, Up-Middle-Big, Up-Fast-Small) were settled by hand in the table (excited, proud, proud, excited, excited); the other 22 are the nearest prototype. The table has every feeling at least 3 times (sad 4, worried 7, calm 3, proud 3, happy 5, excited 5) and every scene's settings read as its stated feeling. One-change walks work: Down-Slow-Still sad, Straight calm, Up proud (only the head changes). Contrast ratios as listed.

## Done when
1. Focus: at 1366x768 and 680x425 Pom is the largest thing in the theater in Show and on the bare stage in Backstage, with all nine control buttons visible below without scrolling.
2. All 27 settings read as the table says, and every scene's settings read as its feeling.
3. Every change eases Pom to the new tilt and bounce from where it is, and the babble speed and pitch follow (Slow 260 ms, Middle 150 ms, Fast 95 ms a syllable).
4. Tap while it plays: a control tap during a babble or a bounce acts at once, cuts the old babble, and hides the audience card.
5. Show plays all three endings; Next is disabled only on scene 5 until an ending is chosen, and no line names it there.
6. Try it praises every time a target is met, and cycles all six targets.
7. How-to lines are spoken once in five actions; scene lines and "How does Pom feel?" are spoken every scene.
8. Every control is 60 px or more with an icon and a word; feelings always show a face and a word.
9. Motion off: no bounce or ease, babble timing unchanged.
10. No network requests; nothing is saved.
