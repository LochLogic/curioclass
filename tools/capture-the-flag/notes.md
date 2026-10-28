## A 5-minute start

1. Open **Codes 100**. Tap the scrambled note to copy it into the Toolbox, then try Base64 and press **Decode**. Ask: was that note locked? (No: Base64 has no key, so anyone can read it.)
2. Type the flag it shows in **Flag** and press **Submit**. The tile asks for the **Patch**: three fixes, each with a cost. Pick the one that fits what the night guard needs, then read what each one trades.
3. Back on the board, let pairs pick their own tiles. One partner reads the artifact aloud while the other works the tools.

## The modes

- **Board:** twelve tiles in four columns (Passwords, Codes, People, Logs), worth 100, 200 or 300. Each tile has two steps:
  - **Find the flag.** It looks like `flag{...}` and is typed into **Flag** (with or without the `flag{ }` wrapper, any case). Each tile accepts only its own flag.
  - **Patch the hole.** The question says what Larkspur needs (who uses the system, what it can spend). Three defensible fixes, each with a cost and a gain; the one that fits turns the tile green and says what was traded. A wrong pick shows its reason and you choose again.
  - Scoring: the flag scores its value. **Hint (half points)** takes half, and each wrong flag (or wrong Check lines, or a wrong full order in Logs 300) takes a quarter, never below a quarter of the tile; the challenge says so before the first try. A patch right on the first try adds 50. Most is 3,000.
  - Progress is kept on this device (which tiles are done and how), so the board can span two periods. **Clear progress** asks Yes or No first.
- **Toolbox:** the four tools on their own. **Shift** (a Caesar wheel, 0 to 25 places, back or forward), **Keyword** (Vigenere, Encode or Decode), **Base64** (Encode or Decode) and **Strength** (length, character pools, bits by characters, bits by words or pattern, the lowest one used, guessing time at 10 billion guesses a second, and a check against a list of 20 very common passwords). In a challenge the same tools sit in the Toolbox drawer.

## Talk about it

- Base64, a shift cipher and AES all turn text into something unreadable. Which ones actually lock it, and what makes the difference?
- Strength rates Winter2026! by its parts (a word, a year, a symbol), not by its 11 characters. Why do guessers try those patterns first? Why does "kettle orbit maple" fall in under a minute, and what changes with six random words?
- The meter assumes 10 billion guesses a second, an offline attack on stolen password hashes. Why is guessing at a sign-in page (Logs 100) so much slower, and what makes it slower still?
- The password was right at 3 a.m. and the sign-in still failed. What would have happened without the second step? Why might a security key be worth its cost next year?
- The caller in People 100 was friendly and knew Dana's name. Which two lines should have stopped her, and why is calling back on a known number better than asking for an ID?
- Pick one patch you chose. What did it cost, and who pays that cost? Would a different company (no help desk, a bigger budget) pick another fix?
- In the break-in timeline, where does each fix stop the chain? Why is stopping it at the sign-in better than cleaning up after step C?

## Good to know

- Larkspur Freight, its people, logs and messages are made up, so students can practice. Every address is a reserved test name (larkspur.example, birchline.example, birchline-billing.example). Nothing here touches a real system, and nothing typed is saved or sent. The board says the rule plainly: only ever test a real system you own or have written permission to test.
- Strength is a model, and it says what it assumes on screen: bits by characters assume random characters; words and patterns (a capital, a year, digits or a symbol added, letter swaps, keyboard runs, repeats) are rated by their parts; it has no dictionary, so a name or phrase it doesn't know can still rate too high; the time assumes a fast offline attack.
- The flags are not listed here, since the tool page shows these notes. Every flag sits in its own challenge: a decoded note, a printed meter reading, an opened log row, a checked pair of call lines, a log, an email, or the letters of the break-in timeline.
- After three wrong flags on a tile, the **Hint** button glows. **Read** speaks the current hint, and the paid hint once it is shown.
- Works on a projector, a laptop or a phone. On a phone the challenge sits above the Flag box, and the artifact scrolls inside its own card; after a tap copies text into a tool, the page brings the tool's answer into view.
