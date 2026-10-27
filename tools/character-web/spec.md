# Character Web

## One idea
A character is pulled several ways at once: put their motivations on a web as anchors, give each turning point in the novel its pulls (with the line that proves them), and the character's dot slides toward whatever pulls hardest, tracing a path across the book; the path's shape, where one pull keeps beating another, is the theme, and you write it as "When ___ wins over ___, ___."

## Not like
- theme-ledger (ela 9-12, wave 4 argument group): two themes tracked across a text in a ledger with evidence. Here the unit is one character's competing motives, and the theme comes out of which motive wins.
- dramatic-irony-theater (ela 8, not specced): what the audience knows that a character doesn't. Here it is what the character wants, and how badly.
- satire-decoder (ela 11, wave 4): two readings of one speaker. Here several motives inside one character, measured at each turn.
- ambiguity-lab (ela 12, this group): a story's structure is switched. Here the text never changes; the student weighs it.
- character-face-off and other K-8 character tools: compare two characters' traits. Here one character against themselves, over a whole novel.

## Who and how
- Grade 9 ELA, module Complex Characters: "How characters with conflicting motivations develop theme".
- Standards: RL.9-10.3, RL.9-10.2.
- Driver: students on laptops, alone or in pairs, 25 to 40 minutes for one character; a teacher can project the web and scrub through the turning points with the class.
- tool.json: driver "students", minutes "25-40", modes ["Read the web", "Your read", "Theme"], grades_label "Grade 9". Kit starter with `kit:theme-912` (dark) and an accent override.

## Screens and modes
Kit frame. Header: "Character Web", small line with the character and novel ("Victor Frankenstein, Frankenstein, 1818"); Motion, Sound, Read. A character picker opens first: three cards (Victor Frankenstein, Jane Eyre, Henry Jekyll), each with the novel, year, a one-line setup and a content line.

**The web** (center): the character's name in a circle that moves. Around it, five **pull anchors** on a ring, each a labeled node with an icon (Content). Thin threads run from the dot to each anchor; a thread's thickness shows that pull's strength at the current turning point (0 to 3), with the number on the thread. The dot's position is the weighted pull of all anchors (a weighted average of anchor positions, pulled toward the center when all are weak). Earlier positions leave a dotted **path** with numbered stops.

**Turning point card** (right, or below on narrow screens): number and chapter, a two-sentence plain summary of what happens, the **quote** that shows the pull (one or two sentences from the novel), and **With**: the other character in the scene and what they do to the pull ("Rochester proposes; love pulls hardest just as principle is tested").

**Read the web.** A scrubber of turning points (6 or 7 stops) under the web. Moving it animates the dot from stop to stop (instant with Motion off); threads change thickness. This is "our reading", labeled as such: "One reading, built from the quotes. Yours can differ."

**Your read.** The same turning points, but the threads start at 0. At each stop the student reads the summary and quote and sets each pull with a 0 to 3 stepper, and must tap at least one word of the quote as evidence for the strongest pull. **Compare** draws our dot as a hollow ring beside theirs, with the distance in words ("close", "some way off", "far off"), never a score. Two paths, theirs solid and ours dotted, build across the novel.

**Theme.** The finished path with each stop's winning pull. The tool names the two pulls that most often fight: at each stop the two strongest pulls form a pair (pulls tied for a place share that stop equally), and the pair with the highest total wins. A sentence frame: "When [pull chip] wins over [pull chip], [result]." The result is free text up to 160 characters, and the student attaches two stops as evidence (tap stops on the path). **Show ours** reveals our theme sentence for that character. **Read my theme** shows the sentence with the two quotes, with **Copy**.

Panel (right): `#hint`, a **Pulls** legend, **Stops set** count in Your read (n of the character's stops: 6, 6 or 8), and **Clear my work** (asks Yes / No).

## Content
Editions: Frankenstein, 1818 text (Project Gutenberg eBook #84; no 1831 introduction); Jane Eyre (eBook #1260); Strange Case of Dr Jekyll and Mr Hyde (eBook #43). Every quote below was checked against those files. Summaries and our readings are written for Curio Class. Pull weights are listed as (pull: weight) for our reading; unlisted pulls are 0.

**Victor Frankenstein** (Mary Shelley, 1818). Pulls: **Knowledge and glory**, **Family and friends**, **Fear and disgust**, **Guilt**, **Revenge**. Content line: "Includes deaths and an execution, described without detail."
1. Chapter 3, Ingolstadt. After M. Waldman's lecture on modern chemistry, Victor decides to go further than any scientist. Quote: "more, far more, will I achieve; treading in the steps already marked, I will pioneer a new way, explore unknown powers, and unfold to the world the deepest mysteries of creation." With: M. Waldman, whose praise of science lights the ambition. (Knowledge 3, Family 1.)
2. Chapter 4, two years of work. Quote: "the same feelings which made me neglect the scenes around me caused me also to forget those friends who were so many miles absent, and whom I had not seen for so long a time." With: his father and Elizabeth, whose letters go unanswered. (Knowledge 3, Family 2.)
3. Chapter 5, the creature wakes. Quote: "Unable to endure the aspect of the being I had created, I rushed out of the room". With: the creature, who reaches toward him. (Fear 3, Knowledge 1.)
4. Chapter 8, Justine's trial. Justine, a family servant, is accused of the murder the creature committed; Victor stays silent. Quote: "A thousand times rather would I have confessed myself guilty of the crime ascribed to Justine, but I was absent when it was committed, and such a declaration would have been considered as the ravings of a madman and would not have exculpated her who suffered through me." With: Justine, who is condemned. (Guilt 3, Fear 2, Family 2.)
5. Chapter 20, the second creature. Victor destroys the companion he promised to make. Quote: "trembling with passion, tore to pieces the thing on which I was engaged." With: the creature, watching at the window, who swears revenge. (Fear 3, Family 2, Guilt 1.)
6. Chapter 24, the chase. After the creature kills Elizabeth, Victor swears to hunt him. Quote: "to execute this dear revenge will I again behold the sun" With: the creature, who leaves him clues to follow. (Revenge 3, Guilt 2.)
Look back card (shown at the end of the path): Victor to Walton, chapter 4, telling his story near death: "Learn from me, if not by my precepts, at least by my example, how dangerous is the acquirement of knowledge and how much happier that man is who believes his native town to be the world, than he who aspires to become greater than his nature will allow."
Most-fought pair (our reading): Knowledge and glory against Family and friends. Our theme: "When the hunger for knowledge wins over the people who love you, it can destroy them and you."

**Jane Eyre** (Charlotte Brontë, 1847). Pulls: **Self-respect**, **Love**, **Principle**, **Independence**, **Belonging**. Content line: "Includes a secret first marriage and a fire."
1. Chapter 12, Thornfield. Jane, a governess, paces the roof and wants more of the world. Quote: "Women are supposed to be very calm generally: but women feel just as men feel; they need exercise for their faculties, and a field for their efforts, as much as their brothers do;" With: Mrs. Fairfax, kind and content, who does not feel the same restlessness. (Independence 3, Belonging 1.)
2. Chapter 23, the orchard. Rochester teases her about leaving; she answers him as an equal before he proposes. Quote: "Do you think, because I am poor, obscure, plain, and little, I am soulless and heartless? You think wrong!" With: Rochester, who then asks her to marry him. (Self-respect 3, Love 3.)
3. Chapter 27, after the wedding is stopped. Jane has learned that Rochester is already married; his wife, Bertha Mason, is confined at Thornfield. He begs her to stay. Quote: "I care for myself. The more solitary, the more friendless, the more unsustained I am, the more I will respect myself." and "Laws and principles are not for the times when there is no temptation: they are for such moments as this, when body and soul rise in mutiny against their rigour;" (the first "I" is italic in the source; show it in italics). With: Rochester, who pleads. (Self-respect 3, Principle 3, Love 3.)
4. Chapter 33, the inheritance. Jane learns she has inherited twenty thousand pounds and that the Rivers siblings are her cousins; she insists on sharing it. Quote: "It would please and benefit me to have five thousand pounds; it would torment and oppress me to have twenty thousand;" With: St. John Rivers, who thinks her foolish. (Belonging 3, Principle 1.)
5. Chapter 34, St. John's proposal. He wants her as a missionary's wife without love. Quote: "I scorn your idea of love," I could not help saying (show the narration with the quote). With: St. John, cold and certain. (Self-respect 3, Love 2, Principle 1.)
6. Chapter 38, conclusion. She returns to Rochester, now free to marry and herself independent. Quote: "Reader, I married him." With: Rochester, blinded and humbled. (Love 3, Independence 2, Self-respect 2.)
Most-fought pair: Love against Self-respect (and Principle). Our theme: "When self-respect wins over love that would cost her it, Jane ends up with both."
Bertha note on the card at stop 3, neutral and short: "The novel shows Bertha only through Rochester's account. Many readers question that picture." Afterlife line in the panel: Wide Sargasso Sea, Jean Rhys (1966), tells Bertha's story from her side.

**Henry Jekyll** (Robert Louis Stevenson, 1886). All stops come from "Henry Jekyll's Full Statement of the Case", the last chapter. Pulls: **Reputation**, **Hidden pleasure**, **Curiosity**, **Conscience**, **Fear**. Content line: "Includes a murder, described briefly."
1. Youth. Quote: "Hence it came about that I concealed my pleasures; [...] I stood already committed to a profound duplicity of life." With: the respectable public he wants to impress. (Reputation 3, Hidden pleasure 2.)
2. The idea. Quote: "man is not truly one, but truly two." With: no one; he works alone in his laboratory. (Curiosity 3, Hidden pleasure 1.)
3. The first dose. Quote: "with a strong glow of courage, drank off the potion." With: no one; Hyde appears for the first time. (Curiosity 3, Hidden pleasure 2, Fear 1.)
4. The drift. Quote: "I was slowly losing hold of my original and better self, and becoming slowly incorporated with my second and worse." With: Hyde, who begins to appear without the drug. (Hidden pleasure 3, Reputation 2, Fear 1.)
5. The choice. Quote: "I chose the better part and was found wanting in the strength to keep to it." With: his friends, whom he returns to. (Conscience 3, Hidden pleasure 2.)
6. Two months. Quote: "For two months, however, I was true to my determination;" With: Utterson and Lanyon, at his dinners. (Conscience 3, Reputation 2.)
7. The relapse. Quote: "My devil had been long caged, he came out roaring." With: Sir Danvers Carew, whom Hyde murders in the street. (Hidden pleasure 3, Reputation 2, Fear 1.)
Last card: "Here then, as I lay down the pen and proceed to seal up my confession, I bring the life of that unhappy Henry Jekyll to an end." (Fear 3, Conscience 2.) Seven stops plus this card, eight in all.
Most-fought pair: Reputation against Hidden pleasure. Our theme: "When a hidden pleasure wins over the self you show the world, the hidden self can take over."

Pull icons (drawn in code): Knowledge, a lamp; Family, two linked rings; Fear, an open eye; Guilt, a scale; Revenge, a blade outline; Self-respect, a spine; Love, a heart; Principle, a book; Independence, an open door; Belonging, a hearth; Reputation, a mask facing out; Hidden pleasure, a mask facing in; Curiosity, a flask; Conscience, a candle; Fear, the open eye.

## Interactions in detail
- Dot motion: position = sum(weight x anchor) / max(sum(weight), 3), so weak pulls leave the dot near the center; 400 ms ease between stops, instant with Motion off. Threads show their number as text; screen readers hear "Stop 4: Guilt 3, Fear 2, Family 2. Strongest: Guilt."
- Steppers: 0 to 3, arrow keys or buttons. Setting a stop is done when at least one pull is above 0 and one quote word is tapped.
- Compare: hollow ring for our dot; distance words by Euclidean distance on the unit ring (under 0.15 close, under 0.35 some way off, else far off).
- Theme: the most-fought pair is computed by the rule in Screens (top two per stop, ties shared) from the student's weights in Your read if all stops are set, else from ours; the chip row offers all five pulls anyway. With our weights: Victor, Knowledge and Family 2.0 (every other pair 1.0 or less); Jane, Self-respect and Love 2.83; Jekyll, Reputation and Hidden pleasure 3.0 (next Curiosity and Hidden pleasure 2.0).
- Store: localStorage `cweb-work`, per character (weights, evidence words, theme sentence), try/catch. Clear my work (after Yes) empties it.
- Keyboard: picker cards, scrubber (arrow keys), steppers, quote words (Tab then Space), path stops in Theme.
- Sizes: at 1366x768 and 1280x720 the web (about 460 px) and the card sit side by side, scrubber under the web, all without page scroll. At 680x425 the card becomes a drawer. At 760 and 375 wide the web shrinks to the width, the anchors' labels move outside the ring as short words, and the card stacks below.

## Look
- `kit:theme-912` dark, accent `--brand #ff8fb8` (pulled-thread rose: the dot, header rule, buttons), `--btn #ff8fb8`, brand text on brand `--brand-ink #1c1203`.
- Threads in `--muted`, the strongest pull's thread in the accent and thicker; the path dotted in `--focus`; our hollow ring `--ink`.
- Anchor nodes on `--sec-bg` with a 1 px `--line` border and their icon; never color alone.
- Neighbors: tone-dial orchid `#f29ff0` (this group, dE 26), idea-threads magenta `#ff6fd0` (this group), boolean-builder orchid, satire-decoder oxblood. Nearest catalog color: `--gr-4` `#ff8a8a` (dE 23), used in charts only.
- Contrast (WCAG 2.1): brand on paper `#0d1219` 8.83:1, on panel 8.14:1, on sec-bg 7.71:1; brand-ink on brand 8.68:1; `--focus` on paper 13.2:1 or better. All pass AA.

## Art
Optional portraits of the three characters as small round cards on the picker, made with Codex (`scripts/gptart.py`, people:true, Cory reviews): Victor in an 1810s student's coat by lamplight; Jane in a plain grey governess dress on Thornfield's roof; Jekyll in a frock coat in a cluttered laboratory. Style: muted ink-and-wash, no gore, no Hyde. If they are not made, the cards use drawn monograms. Everything else (web, anchors, icons, preview.svg showing a web with a path) is drawn in code.

## Voice
Bank voice `wise-mentor` (Gacrux), style "Say thoughtfully and warmly, like a wise high school mentor". `Curio.voice`, scope the mode.
- welcome (how, first open): "Pick a character. Every turning point pulls them several ways at once."
- scrub (how, first Read the web): "Slide through the turning points. The dot goes where the pulls are strongest."
- yours (how, first Your read): "Now you weigh it. Set each pull, then tap the words that prove the strongest one."
- far (event, each Compare that shows far off; stale when that stop changes): "We read that one differently. Which words made you choose that pull?"
- theme (how, first Theme view): "Look at which pulls keep fighting. Finish the sentence: when one wins over the other, what happens?"
- done (event, a theme saved with two stops attached; stale when the sentence changes): "That's a theme with proof. Read it to a partner and see if they'd pick the same stops."

## Family engine
none

## Sources
- Mary Shelley, Frankenstein; or, the Modern Prometheus (1818 text), Project Gutenberg eBook #84, https://www.gutenberg.org/ebooks/84 . Chapter numbers as in that file.
- Charlotte Brontë, Jane Eyre: An Autobiography (1847), Project Gutenberg eBook #1260, https://www.gutenberg.org/ebooks/1260 . Chapter numbers as in that file.
- Robert Louis Stevenson, The Strange Case of Dr. Jekyll and Mr. Hyde (1886), Project Gutenberg eBook #43, https://www.gutenberg.org/ebooks/43 , chapter "Henry Jekyll's Full Statement of the Case".
- Plot facts in the summaries (Waldman's lecture, Justine's trial, the destroyed companion, Elizabeth's death; Bertha Mason, the inheritance and the Rivers cousins, St. John's proposal; Carew's murder): the same editions, cross-checked with Britannica, "Frankenstein," "Jane Eyre," and "Strange Case of Dr. Jekyll and Mr. Hyde."
- Wide Sargasso Sea (1966) as a retelling of Bertha's story: Britannica, "Jean Rhys."
- Standards: CCSS ELA RL.9-10.3 and RL.9-10.2, https://www.thecorestandards.org/ELA-Literacy/RL/9-10/

## Done when
1. Every quote matches its edition word for word; Jane's "I" at stop 3 is italic; Jekyll's stop 1 shows the "[...]" cut.
2. In Read the web, Victor's dot sits near Knowledge at stops 1 and 2, swings to Fear at stop 3, to Guilt at stop 4 and to Revenge at stop 6; the path shows six numbered stops and the look back card.
3. The screen reader text for Jane's stop 3 reads "Self-respect 3, Principle 3, Love 3" and names a tie as "Strongest: Self-respect, Principle and Love, tied."
4. In Your read, a stop cannot be set without a tapped quote word; Compare shows our ring and a distance word.
5. Theme computes the most-fought pair with the shared-tie rule and matches the totals in Interactions for all three characters with our weights; Show ours reveals our sentence.
6. Read my theme shows the sentence with the two attached quotes; Copy gives plain text.
7. Reload keeps work per character; Clear my work (after Yes) empties it; no network; console clean.
8. At every size in STANDARDS.md the web and the scrubber are visible together; 375 wide works in `drive.py --host`.

## Open questions
- [character-web] Jane Eyre's Bertha Mason is handled with one neutral line and the Wide Sargasso Sea afterlife. Enough, or leave the Bertha note out at grade 9?
- [character-web] Codex portraits for the three characters, or monograms only?
