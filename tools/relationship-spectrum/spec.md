# Relationship Spectrum

## One idea
Every scenario card has one detail you can flip (asks or demands, once or every day, takes a no or pushes past it), and flipping it slides the card along a line from healthy to unhealthy to abusive in front of you, so you see that respect, choice and pressure, not the action itself, move a relationship along the line; then you practice saying the boundary and see the two ways the other person might answer.

## Not like
- conflict-coach (6-8 SEL, roleplay): rewinds an argument between equals to swap blaming lines for I-statements. Here nobody is wrong about a misunderstanding: the question is whether a behavior is respectful or controlling, and the tool shows the line it sits on.
- pressure-point (group sibling, story): refusing a vape or a drink in a scene with bystanders' thoughts. Relationship Spectrum is about how a friend or partner treats you over time, placed on a line, with no story branches.
- stress-toolkit (group sibling): coping tools you try on yourself. screen-time-detective (group sibling): a pretend kid's week of data. Neither places behaviors on a scale.
- walk-in-their-shoes (3-5 SEL, story): seeing one moment from several points of view. Here it is one behavior seen at several strengths.
- mind-map (9-12 feelings): the "help a friend" practice is about mental health. Here it is boundaries and warning signs in friendships and dating.

## Who and how
- Grade 6-8, Health, module Healthy Relationships (communication, boundaries and conflict resolution).
- Driver: students on laptops, alone or in pairs (pairs talk about where to place a card before the reveal). A teacher can project one card and take a class vote.
- Minutes: 15-25.
- Standards: NHES.S4 (interpersonal communication: setting boundaries, asking for help), with NHES.S1 (healthy and unhealthy relationship behaviors) as background; also CASEL.Relationship Skills (healthy relationships, boundaries and warning signs).
- Topic line: "healthy relationships and boundaries".
- Modes (tool.json): ["The line", "Flags"].

## Screens and modes
Header: title "Relationship Spectrum" with the topic line under it, mode buttons **The line**, **Flags**, then **Teacher**, **Motion**, **Sound**, **Read**. Stage left, panel right. A help footer in every mode (Content).

### The line (opens first)
- Stage, top: the spectrum, a wide horizontal band in three zones, left to right: **Healthy** (circle glyph, solid light tint), **Unhealthy** (triangle glyph, diagonal hatch), **Abusive** (square glyph, cross-hatch). Under the band the three zone sentences (Content). Positions run 0 (left) to 100 (right).
- Stage, middle: the current scenario card (who, the situation, the current detail) and a marker "Your spot" that starts above the band at 50.
- Stage, bottom: the deck: 12 small card backs (6 with a two-friends icon, 6 with a heart icon); played cards show their last guide zone glyph.
- Panel, step by step:
  1. **Place it**: hint, then **Healthy**, **Unhealthy**, **Abusive** buttons (drop your marker in the middle of that zone) or drag the marker along the band (steps of 5; arrow keys move it, Enter drops). Then **Show the guide's spot**.
  2. **Reveal**: a second marker "Guide" slides to the guide's position; your marker stays where you put it. The flag card opens: the green or red flags for this detail (each a chip with its glyph: green flags a filled leaf, red flags a filled flag, missing green flags a hollow leaf "Missing: Respect"), and a one-line why. No score.
  3. **Flip a detail**: the scenario's detail chips (2 or 3, each one short phrase). Tapping one swaps the card text, slides the Guide marker to the new spot (500 ms, instant with Motion off) and swaps the flag card. This is the main thing to explore.
  4. **Say it** (shown when the current detail is in Unhealthy): see "Say it" below. When the current detail is in Abusive, the **Get support** card shows instead.
  Buttons under the steps: **Next card**, **Shuffle deck**.
- Tapping any card in the deck opens it at step 1.

### Say it (a step inside The line)
- The panel shows a two-person text thread (you on the right). Pick one of three lines to send: the scenario's own line, "That's not okay with me. Please stop." and "Can we talk about this later, when we're both calm?"
- After sending, a switch **If they respect you** | **If they don't** shows the other person's reply for each. Under it, always: "A boundary isn't a test you pass or fail. If someone keeps pushing after you say it, that tells you about them, not about you. Talk to a trusted adult."

### Get support (replaces Say it for Abusive details)
"When someone threatens you, scares you or tries to cut you off from others, you don't have to handle it alone or face them by yourself. Tell a trusted adult: a parent, the school counselor, a teacher or a coach. You can also reach loveisrespect (below)."

### Flags
- Stage: two columns of flag cards, **Green flags** and **Red flags** (Content). Tapping a card lists every scenario detail that shows it; tapping one jumps to The line with that card and detail open.
- Panel: hint and a short note: "One red flag once can be a bad day. A red flag that keeps happening, or that comes with fear, is a pattern. Patterns are what move a relationship toward abusive."

### Teacher
Dialog with a choice **Friendships only** | **Friendships and dating** (default: Friendships and dating) and **Done**. Friendships only hides the six heart cards and every dating mention. Remembered in localStorage `curio-relationship-spectrum-set` (a classroom setting, not student data), try/catch.

## Content

### Zone sentences (from loveisrespect's relationship spectrum)
- Healthy (0 to 33): "Based on equality and respect."
- Unhealthy (34 to 66): "Based on attempts to control the other person."
- Abusive (67 to 100): "Based on power and control."
Under the band: "All relationships sit somewhere on this line, friendships too, and they can move."

### Flags
Green (loveisrespect green flags): **Communication**: you talk openly about how you feel and you listen. **Respect**: you value each other's feelings, boundaries and choices. **Trust**: you believe each other without needing proof. **Honesty**: you tell each other the truth. **Equality**: you make decisions together and hold each other to the same standards. **Boundaries**: you each say what you're comfortable with, and the other person respects it.
Red (loveisrespect warning signs, unless marked): **Checking your phone without permission**. **Putting you down, especially in front of others**. **Isolating you from friends or family**. **Extreme jealousy**. **Explosive temper**. **Possessive or controlling**. **Threats** (CDC: words meant to harm someone mentally or emotionally). **Repeated, unwanted contact** (CDC: a pattern of unwanted attention and contact). **Any physical harm** (glossary only; no scenario shows it).

### Scenarios (guide position, flags, why). Names are gender neutral and every person is "they".
Friendships:
- F1 Casey and your phone. (a) "You hand Casey your phone to show a video. Casey watches it and hands it back." 8; Trust. (b) "When you leave the table, Casey picks up your phone and reads your messages." 52; Checking your phone without permission. Why: "Once, it breaks trust. It isn't okay, but it can be talked about." (c) "Casey demands your password and says you're hiding something if you won't share it." 74; Checking your phone without permission, Possessive or controlling. Say it line (b): "Please don't read my messages. My phone is private."
- F2 Avery and the party. (a) "You're going to someone else's party. Avery says, 'I'll miss you. Tell me about it Monday.'" 6; Respect. (b) "Avery gives you the silent treatment for two days." 45; Missing: Communication. (c) "Avery says if you go, they'll tell everyone your secret." 86; Threats. Line (b): "I can tell you're upset. I'd rather talk about it than not talk at all."
- F3 Morgan's jokes. (a) "Morgan jokes about your laugh once. When you say it's getting old, Morgan stops." 14; Respect, Communication. (b) "Morgan makes fun of your laugh every day at the lunch table, even after you said it bothers you." 64; Putting you down, especially in front of others. Why: "Every day, in front of others, after you asked them to stop: this is close to a pattern." Line (b): "It's not funny to me anymore. Please stop."
- F4 Jamie and the new friend. (a) "You start hanging out with a kid from band. Jamie says, 'Cool! Can I come next time?'" 5; Trust, Equality. (b) "Every time, Jamie says, 'Guess I'm not good enough anymore.'" 42; Extreme jealousy. (c) "Jamie says choose: them or the band kid, and won't talk to you until you drop your new friend." 76; Isolating you from friends or family. Line (b): "You're still my friend. I can have more than one."
- F5 Quinn and the homework. (a) "Quinn asks to copy your homework. You say no. Quinn says, 'Okay, fair.'" 10; Respect, Boundaries. (b) "Quinn keeps asking after you say no and calls you selfish." 48; Missing: Respect. Line (b): "I already said no. That's my answer."
- F6 Riley and the photo. (a) "Riley asks before posting a photo of you." 4; Respect, Boundaries. (b) "Riley posts a photo you hate and won't take it down when you ask." 50; Missing: Respect. (c) "Riley says they'll share your private messages unless you do what they say." 90; Threats. Line (b): "Please take that photo down. Ask me before you post me."
Dating (hidden in Friendships only):
- D1 Taylor's texts. (a) "Taylor texts a few times a day and is fine when you don't answer during practice." 6; Trust. (b) "Taylor texts every few minutes and gets upset if you don't answer right away." 48; Possessive or controlling. (c) "Taylor makes you share your location all the time and check in about where you are." 76; Possessive or controlling. Line (b): "I like texting you, but not every few minutes. I'll answer when I can."
- D2 Devon and your clothes. (a) "Devon says you look nice." 4; Respect. (b) "Devon tells you what to wear when you go out." 50; Possessive or controlling. (c) "Devon gets angry and won't drop it until you change." 72; Possessive or controlling, Explosive temper. Line (b): "I pick my own clothes."
- D3 Skyler's weekend plans. (a) "You and Skyler take turns picking what to do." 5; Equality. (b) "Skyler always picks and says your ideas are boring." 50; Missing: Equality, Putting you down. (c) "Skyler decides which friends you're allowed to see." 82; Isolating you from friends or family. Line (b): "I want us both to get a say. This week it's my pick."
- D4 Reese and jealousy. (a) "Reese says, 'I felt a little jealous when you talked to them. Can we talk about it?'" 18; Communication, Honesty. Why: "Feeling jealous is normal. Saying so calmly and listening is healthy." (b) "Reese accuses you of liking someone else and won't talk to you all day." 54; Extreme jealousy. (c) "Reese goes through your messages and yells at you in the hallway." 84; Checking your phone without permission, Explosive temper, Putting you down. Line (b): "I'm not doing anything wrong. I need you to trust me."
- D5 Kendall and the breakup. (a) "You say you want to break up. Kendall is sad but says, 'Okay. Thanks for telling me.'" 8; Respect. (b) "Kendall keeps texting to change your mind after you asked them to stop." 58; Repeated, unwanted contact. (c) "Kendall says they'll spread rumors about you if you leave." 90; Threats. Line (b): "I asked you to stop texting about this. I mean it."
- D6 Emery and holding hands. (a) "You say you're not ready to hold hands at school. Emery says, 'Okay, thanks for telling me.'" 4; Respect, Boundaries. (b) "Emery jokes about it in front of friends to change your mind." 56; Putting you down, especially in front of others. Line (b): "It's not a joke to me. Please drop it."
Why lines not given above default to the zone sentence plus the first flag's text. Each card opens on its (b) detail; (a) and (c) are reached by flipping.

### Say it replies (If they respect you / If they don't)
F1 "Sorry. You're right, I shouldn't have." / "If you had nothing to hide, you wouldn't care." F2 "Yeah. I was hurt you didn't invite me. Can we talk?" / "Whatever." F3 "Oh. Sorry, I'll stop." / "Can't you take a joke?" F4 "Okay. Sorry, I just felt left out." / "So you do like them more." F5 "Fine. Fair enough." / "Some friend you are." F6 "Sorry! Taking it down now." / "It's funny, relax." D1 "Got it. Text me after practice?" / "If you cared you'd answer." D2 "You're right. You look good anyway." / "I'm just saying it for your own good." D3 "Deal. Your pick." / "Your ideas are still boring." D4 "Okay. I'm sorry I got weird." / "Then why were you smiling at them?" D5 "Okay. I'll stop." / "Just one more talk, please, I'll be outside your class." D6 "Sorry. That wasn't cool of me." / "Relax, everybody was laughing."

### Help footer (every mode)
One calm line: "Is something like this happening to you or a friend? Talk to a trusted adult or the school counselor. loveisrespect: text LOVEIS to 22522 or call 1-866-331-9474." **More help** dialog: the same contacts, "loveisrespect is free and confidential, for teens and young adults.", "If you are in immediate danger, call 911.", "This tool is for learning. It can't tell you about your own relationship." The link `https://www.loveisrespect.org` opens only when clicked.

## Interactions in detail
- Your marker and the Guide marker can overlap; when they are within 5 the panel says "Close to the guide." Otherwise "You put it in {zone}. The guide puts it in {zone}." plus the why. Never right or wrong, no points, no totals.
- Flipping details never asks you to place again; to place a new detail fresh, tap **Place again** (moves your marker back to 50).
- Next card goes through the visible deck in order F1 to F6 then D1 to D6; Shuffle reorders it for the page session. Played glyphs on card backs are session only.
- With Friendships only, the Flags mode hides dating examples from each flag's list; a flag with no examples left says "Shows up in dating too." only when dating is on (otherwise nothing).
- Say it: the sent line appears in a bubble; the switch starts on If they respect you. Changing details clears the thread.
- Keyboard: arrow keys move the marker, H, U, A drop in a zone, Enter reveals, Tab reaches detail chips before the deck.
- Narrow: the band stays full width over the card; the deck becomes a horizontal strip that scrolls; the panel steps stack under the stage below 1000 px, with Place it buttons in view without scrolling at 1366x768.

## Look
- Accent `--brand` #0f6e8c (deep teal blue: steady and trustworthy), on a cool light `:root`: paper #f4f7f8, ink #172a33, muted #52666f, line #d6e2e6, focus #c2410c, panel #ffffff. Zones: Healthy tint #dff0e6 with text #1e6b45 and shape #2e8b57; Unhealthy tint #fbefd2 with text #8a5d00 and shape #a87300; Abusive tint #f1e1ef with text #7d3c78 and shape #7d3c78. Hatching patterns are SVG, about 30 percent opacity.
- Contrast: accent on white 5.79:1, on paper 5.37:1; white on accent 5.79:1; ink on paper 13.78:1; muted on paper 5.59:1; ink on the three zone tints 12.54, 12.98 and 11.84:1; zone texts on white 6.47, 5.76 and 7.53:1; zone shapes on white 4.25, 4.10 and 7.53:1 (graphics, over 3:1). Zones never rely on color: glyph, hatch and label each time.
- Different from group siblings (pressure-point berry #a3263f, stress-toolkit moss #4f6b2c, screen-time-detective blue #1f5fbf on a night stage) and neighbors (conflict-coach burnt orange, goal-tracker indigo, rules-referee gold, growing-up-q-a mauve).

## Art
none: drawn in code (the band, hatching, glyphs, card fronts with a small two-friends or heart icon, the text thread). No people.

## Voice
`wise-mentor` (Gacrux): "Say thoughtfully and warmly, like a wise high school mentor." The trusted older voice the topic calls for. Different from conflict-coach (big-sister), goal-tracker (easy-coach), rules-referee (firm-captain) and the group siblings (smooth-narrator, soft-breath, science-narrator).
| Key | Kind | Line | Stale when |
|---|---|---|---|
| wLine | how | Read the card. Then tap Healthy, Unhealthy or Abusive to place it, and tap Show the guide's spot. | mode left |
| wFlags | how | Tap a flag to see where it shows up. | mode left |
| flip | how | Now tap a different detail and watch the card move. | card changed |
| sayit | how | Pick a line to send. Then flip the switch to see two ways they might answer. | detail changed |
| reveal | event | You put it in {zone}. The guide puts it in {zone}. | detail or card changed |
| support | event | You don't have to handle this alone. Tell a trusted adult. | detail or card changed |
| boundary | event | A boundary isn't a test you pass. If they keep pushing, that tells you about them, not you. | thread cleared |
Card texts, flags and replies are read on screen; Read speaks the hint or the open card.

## Family engine
none

## Sources
- loveisrespect, Relationship spectrum: all relationships on a spectrum from healthy to abusive, unhealthy in the middle; healthy based on equality and respect, unhealthy on attempts to control, abusive on power and control. https://www.loveisrespect.org/everyone-deserves-a-healthy-relationship/relationship-spectrum/ (builder: quote the zone sentences from loveisrespect's spectrum PDF linked on that page)
- loveisrespect, Green flags in relationships: communication, respect, trust, honesty, equality. https://www.loveisrespect.org/resources/green-flags-in-relationships/
- loveisrespect, Warning signs of abuse: checking your phone without permission, putting you down especially in front of others, isolating you, extreme jealousy, explosive temper, physical harm, possessive or controlling behavior. https://www.loveisrespect.org/about-dating/warning-signs-of-abuse/
- loveisrespect, What are my boundaries?: digital boundary examples (texting frequency, passwords), "Is this okay?". https://www.loveisrespect.org/resources/what-are-my-boundaries/
- loveisrespect contacts: call 866-331-9474, text LOVEIS to 22522, chat on the site; 911 in immediate danger. https://www.loveisrespect.org
- CDC, About Teen Dating Violence: can happen in person, online or through technology; psychological aggression and stalking definitions; teaching healthy communication prevents it (Dating Matters for ages 11 to 14). https://www.cdc.gov/intimate-partner-violence/about/about-teen-dating-violence.html
- National Health Education Standards (SHAPE America), Standards 1 and 4.
- Tool's own choices: the 0 to 100 positions within each zone, the 5-point "close" margin, the scenario wording and replies (original).

## Done when
1. Every card's details slide the Guide marker to the listed positions, in the listed zone, with the listed flags; recompute that every position sits inside its zone's range.
2. Your marker stays where you placed it after the reveal; the reveal line names both zones; nothing scores or totals.
3. Say it appears only for Unhealthy details and Get support only for Abusive ones; both replies show for all 12 Say it threads.
4. Teacher Friendships only hides all six heart cards, dating flag examples and every dating word after reload; Friendships and dating restores them.
5. Flags: tapping Threats lists F2c, F6c and D5c (with dating on) and jumps to the right card and detail.
6. Zones are readable with color turned off (grayscale screenshot): glyph, hatch and label tell them apart.
7. Voice: flip is spoken once across the deck; reveal is spoken every reveal and dropped if the student flips first.
8. At 1366x768 and 680x425 the band, the card and the Place it buttons are visible without scrolling; at 375 wide the deck scrolls sideways and the band stays full width.
9. Nothing about the student is stored; only `curio-relationship-spectrum-set` is in localStorage; help numbers match Sources.

## Open questions
- Default for Teacher: Friendships and dating (this spec) or Friendships only, so dating is something a teacher turns on? A parent might want to see the dating cards first.
- The Abusive zone includes threats, isolating and controlling behavior but no physical or sexual harm (physical harm is named only in the Flags glossary; loveisrespect's "pressuring you to have sex" sign is left out entirely for 6-8). Is that the right line?
- Show the loveisrespect text and phone numbers in the footer, or only "a trusted adult or the school counselor" with loveisrespect inside More help?
