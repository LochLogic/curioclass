# Author's Mailbox

## One idea
Every author writes for a reason, and at Postmaster Moose's little post office each short fact text arrives as a letter that must go in the mailbox for its author's job (to answer a question, to explain how something works or is done, or to describe what something is like), but a letter is only stamped when the class taps the sentence that gave the job away; at the end the class becomes the boss, giving three owl authors three different jobs, and sees three owl letters come back that each do the job they were given.

## Not like
- postcard-writer (1, spec): fixing capitals, commas and spelling on postcards a pigeon carries. Here sorting fact texts by the author's purpose; the mail is only the frame.
- main-idea-umbrella (2, concept): what a text is about. Here why it was written.
- because-bridge (k-2, spec): finding the reason an author gives for a point. Here the author's job for the whole text.
- moral-of-the-story (2, concept): a lesson in a fable. Here purpose in informational texts.
- word-zoo (1, spec, same format): sorting words by kind. Here sorting whole texts by purpose, with a proof tap.

## Who and how
- Grade 2, ELA, module "Author's Purpose" (Reading Informational Text). Standard: RI.2.6.
- Driver: a pair at one device or the teacher on a projector (tool.json `driver: "either"`). Every letter is read aloud on open and every sentence on tap; mailboxes have pictures (BASELINE rule 4).
- Two parts: `Sort the Mail` (nine letters, three of them mixed) and `Be the Boss` (owls). tool.json `modes: []`, `minutes: "10-15"`, `grades_label: "Grade 2"`. Nothing is saved.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.2.6 | Read a letter and drop it in the mailbox for its author's main job: Answer, Explain, Describe | three mailboxes with pictures (a question mark, gears, a magnifying glass) | 2 |
| RI.2.6 | Tap the sentence that gives the job away; the letter is stamped | the sentence glows; a stamp | 3 |
| RI.2.6 | Mixed letters: one sentence does a different job; find the job most sentences do | each sentence gets a small job tag after sorting | 4 |
| RI.2.6 | Be the Boss: give three owl authors three jobs, then match each owl letter to the author whose job it does | three author desks and three letters | 5 |

## Screens and modes
Header (kit): title "Author's Mailbox"; `Sort`, `Boss`; `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** A small country post office with Postmaster Moose behind the counter and a mail sack. First hint: "Tap the mail sack to get the first letter." The first tap opens the first letter with its line; the welcome is queued after it (`welcomeAfter: true`).

**Sort the Mail.** Focus: the open letter (700 x 420: the author's name and picture at the top, then four sentences; the title stays folded under a flap until the letter is stamped, so the class reads the sentences, not the title, each read on tap) and the three mailboxes below (240 x 220 each): `Answer` (a big question mark: the author wants to answer a question), `Explain` (gears: the author wants to tell how something works or how to do it), `Describe` (a magnifying glass: the author wants to tell what something is like). The whole letter is read when it opens; `Read again`. Drag the letter (folded to an envelope) to a mailbox, or tap a mailbox. Right box: the box opens and Moose says "Now show me the sentence that told you." The letter unfolds again; tap the giveaway sentence. Right: a stamp lands on it and the letter drops in. Wrong box: the letter bounces back and Moose asks the box's question ("Does this author tell how to do something, step by step?").

**Mixed letters.** Three letters have one sentence that does a different job (a describing sentence in an explain letter). After stamping, each sentence gets a small tag (?, gears, magnifier) and Moose says "Most sentences explain, so the main job is Explain."

**Be the Boss.** Three owl authors (Hoot, Wren and Barney the barn owl) at desks. The class drags one job card to each author (any assignment). Then three owl letters arrive, unsigned; the class drops each on the author whose job it does, then taps the giveaway sentence. If a letter is dropped on an author with a different job, that author reads the letter and says "That's not my job. I was asked to {describe}."

At 1366x768 the letter and mailboxes fit above the fold. At 680x425 mailboxes are 160 x 150 beside the letter.

## Content
All written for Curio Class. (job: title by author | four sentences | giveaway sentence numbers)

**Answer:**
1. Why Do Cats Purr? by Penny Pug | Have you ever wondered why cats purr? Cats often purr when they feel safe and calm. They can also purr when they are hurt or scared. Scientists think purring may help a cat calm itself. | 1, 4
2. Why Is the Sky Blue? by Sol the Sunbird | Why is the sky blue on a sunny day? Sunlight looks white, but it is made of many colors. When sunlight hits the air, blue light bounces around the most. That is why we see blue all over the sky. | 1, 4
3. Where Do Bees Go in Winter? (mixed) by Bea Bumble | Where do honeybees go when it gets cold? They stay inside their hive. Their hive is snug and full of sweet, golden honey. The bees huddle in a ball and shiver to stay warm. | 1, 4 (the describing sentence is 3)

**Explain:**
4. How a Kite Flies by Kip Crane | Here is how a kite flies. First, the wind pushes up under the kite. Next, the string holds it so it does not blow away. Then the kite rises high into the sky. | 1, 2
5. How to Wash Your Hands by Dr. Otter | Here is how to wash your hands. First, wet your hands and add soap. Next, scrub every part for 20 seconds, as long as singing "Happy Birthday" twice. Last, rinse and dry them with a clean towel. | 1, 2
6. How a Seed Grows (mixed) by Fern Frog | This is how a seed grows. First, it needs water and warm soil. Next, a tiny root grows down and a green shoot pokes up. The shoot is soft, pale and curly like a hook. | 1, 2 (the describing sentence is 4)

**Describe:**
7. The Desert at Night by Dusty Kit Fox | The desert at night is cool and quiet. The sand is dark, and the sky is full of bright stars. Soft wind whispers over the dunes. Owls hoot and little mice scurry. | 1, 2
8. What a Sloth Is Like by Sami Sloth | A sloth is a slow, sleepy animal. It has long arms and long curved claws. Its fur is shaggy and can look a little green. It hangs upside down in the trees. | 1, 3
9. Our Busy Rainforest (mixed) by Tico Toucan | The rainforest is warm, wet and green. Tall trees reach up like giant umbrellas. Why is it so wet? It rains almost every day. | 1, 2 (the answering sentences are 3 and 4)

**Be the Boss, owl letters (job | text | giveaway):**
- Answer: Why Can Owls Fly So Quietly? | How can an owl fly without a sound? The edges of its wing feathers are soft and fringed. The soft edges break up the air so it makes less noise. That is why a mouse cannot hear an owl coming. | 1, 4
- Explain: How an Owl Catches Its Dinner | Here is how an owl hunts at night. First, it sits still and listens. Next, it hears a mouse and turns its head to find it. Last, it swoops down without a sound. | 1, 2
- Describe: What a Barn Owl Looks Like | A barn owl has a white face shaped like a heart. Its eyes are dark and round. Its back is soft gold and gray. Its legs are long and covered in white feathers. | 1, 2

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A letter cannot be stamped until it is in the right box; giveaway taps on other sentences read them and Moose says "Look for the sentence that shows the job."
- Mixed letters accept only the main job; picking the minority job gets "One sentence does that. What do most sentences do?"
- Letters come in a fixed order (by number above): 1, 4, 7, 2, 5, 8, 3, 6, 9, so never two of one job in a row. The mailbox wall shows three stamps per box when done.
- Be the Boss: every author must get a different job; the letters match by job, so any assignment works.
- One star for Sort when all nine are stamped; a second for stamping each on the first try; one for Be the Boss.

## Look
- Accent `--brand` #4d6b1f olive (header, mailboxes, Moose's vest); gold #f4c542 (stamps, stars); each mailbox has its icon and word; paper #f8faf2; ink #1b240f; muted #545e48. Scene: a cozy country post office.
- Contrast (WCAG 2.1, computed): white on brand 6.11:1; brand on paper 5.80:1; ink on paper 15.28:1; muted on paper 6.49:1; ink on gold 9.89:1.
- Never color alone: the three mailboxes differ by icon, word and shape (round top, square, slot); job tags are icons.
- Different from this batch (dusk violet, workshop teal, brick map, coral sea) and from postcard-writer's airmail blue.

## Art
Local FLUX (`scripts/localart.py`); no people.
- post office (1): "A cozy cartoon country post office counter with mailboxes and a mail sack, soft gouache, no text"; 16:9; cutout no.
- Postmaster Moose (3, stand, point, stamp): "A friendly moose postmaster in an olive vest <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- authors (12: the nine letter authors and the three owls): "A cute <pug / sunbird / bumblebee / crane / otter in a white coat / frog / kit fox / sloth / toucan / owl at a desk / ...>, soft gouache, plain white background"; 1:1; cutout yes.
- letter pictures (12, one per letter): "<a cat purring on a lap / a blue sky over a field / ...>, soft gouache"; 4:3; cutout no.
About 28 images. Drawn in code: letters, envelopes, mailboxes, stamps, tags, desks, controls.

## Voice
Bank voice `friendly-dad` as Postmaster Moose (unique in this batch); letters are read by Moose. `Curio.voice` with `scope: () => state.part + ':' + state.letter`, `welcomeAfter: true`.
- event `sack`: "Mail's here!"
- how `welcome`: "Welcome to my post office! Every author writes for a reason. Read the letter, then put it in the mailbox for the author's job."
- event, whole, `letter`: the title, author and four sentences.
- event, whole, `sentence`: the tapped sentence.
- event `rightBox`: "Yes! Now show me the sentence that told you."
- event `wrongBox`: "{Does this author tell how to do something, step by step?}"
- event `stamp` / `lookAgain`: "Stamped! Authors often tell you their job right at the start." / "Look for the sentence that shows the job."
- event `mixed`: "One sentence does that. What do most sentences do?" and after stamping: "Most sentences {explain}, so the main job is {Explain}."
- how `boss`: "You're the boss now. Give each owl author a different job."
- event `notMyJob`: "That's not my job. I was asked to {describe}."
- event `done`: "Every letter delivered!"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Mailbox | Try boxes in turn | It goes in eventually, but the second star counts first tries and the stamp needs the giveaway sentence. |
| Giveaway | Tap the first sentence | It works: every letter opens with a sentence that names its job, as good fact writing does, and the stamp line says so ("Authors often tell you their job in the first sentence"). The stamp teaches where to look; the box drop carries the check. |
| Title words | Go by Why or How in the title | Titles are hidden until the stamp. Inside the text, mixed letter 9 has a Why question in a Describe letter, so spotting one question word is not enough. |
| Be the Boss | Drop letters at random | 3 letters on 3 authors: 6 ways, 1 right (computed). |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the sack: `sack`, `welcome` (queued, first time), `letter` (whole).
2. Drop: `rightBox` or `wrongBox`; taps: `sentence` (whole), then `stamp` or `lookAgain`; mixed letters add `mixed`.
3. Boss: `boss`, then per letter `letter` (whole) and `notMyJob` if wrong; end `done`.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.2.6 wording (main purpose of a text, including what the author wants to answer, explain or describe) | thecorestandards.org, RI Grade 2 | CCSS ELA 2010 PDF | yes |
| Cats purr when content and also when stressed or hurt; purring may help them calm or heal | Scientific American, "Why do cats purr?" | Library of Congress, Everyday Mysteries, "Why do cats purr?" | yes |
| The sky looks blue because air scatters blue light more than other colors (Rayleigh scattering) | NASA Space Place, "Why is the sky blue?" | NOAA SciJinks, "Why is the sky blue?" | yes |
| Honeybees overwinter in the hive in a cluster and shiver flight muscles to make heat | Penn State Extension, honey bee winter cluster | USDA ARS, honey bee biology | yes |
| Handwashing: wet, lather, scrub at least 20 seconds (two "Happy Birthday"s), rinse, dry with a clean towel | CDC, handwashing (When and How to Wash Your Hands) | Mayo Clinic, "Hand-washing: Do's and don'ts" | yes |
| Sloths are slow, hang upside down, have long curved claws, and algae can grow in their fur | Smithsonian's National Zoo, sloth facts | San Diego Zoo Wildlife Alliance, sloth | yes |
| Owls fly quietly because of soft, fringed edges on their wing feathers | Audubon (audubon.org), silent owl flight | Cornell Lab of Ornithology, All About Birds, owls | yes |
| Barn owls have a white heart-shaped face | Cornell Lab, All About Birds, "Barn Owl" | The Barn Owl Trust, barn owl facts | yes |
| A seed's root grows first, then the shoot, which comes up bent like a hook | RHS (rhs.org.uk), seed germination advice | University of Illinois Extension, seed germination | yes |
Backed twice: 9. Cut: 0.

Checks run (Python, scratchpad b6, 2026-11-08): three letters per job and one mixed letter per job; four sentences per letter; no two letters of one job in a row in the fixed order; Be the Boss 3! = 6; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the letter and three mailboxes show with no scroll; at 680x425 the same, smaller.
2. Each of the nine letters goes only in its job's box; mixed letters only in the main job's box. (RI.2.6)
3. Each letter is stamped only on a giveaway sentence. (RI.2.6)
4. Mixed letters show each sentence's job tag after stamping, with the main-job line. (RI.2.6)
5. Be the Boss: any three different jobs can be given; each owl letter matches only the author with its job. (RI.2.6)
6. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
7. Pre-reader: every letter and sentence is read; mailboxes have icons.
8. Motion off: envelopes appear in boxes instead of flying; no network requests; nothing saved.

## Open questions
- None for Cory.
