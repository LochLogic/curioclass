# Corner Store: spec notes

The tool was built before specs were kept per tool; see the comment at the top of src.html and plan.md for the lesson. This file holds the voice spec.

## Voice

`voice/lines.json`: `"bank": "friendly-dad"`, `"voice": "Achird"`, `"style": "Say in a relaxed, friendly way, like a kind dad helping with homework"`, plus a `group_style` for the counted cents list. One narrator voice for all five customers (styled lines, no extra voices). `python scripts/neighbors.py corner-store` showed no near neighbor using friendly-dad (no tool uses it yet). 104 lines plus 99 group lines ("1 cent" to "99 cents" in groups of ten), recorded with scripts/localvoice.py.

Queue: the kit (kit/curio.js) plays a recording when the exact text has one and falls back to the browser voice otherwise. The tool's `voice()` follows collision-lab's pattern: nothing before the first tap, lines wait for Read, a new speech bubble drops the old bubble's line (but never cuts Read off), and `hush()` (Read, Open again, Sound off) drops queued lines and releases every waiter. The customer's hello and thanks wait for their clip before the day moves on. On the first tap the bubble on screen is said, unless that tap was Read or Sound or replaced the bubble.

How the money is said: on screen the bubble keeps "25¢" and "$1.00"; the voice says "25 cents" and "one dollar". A customer only ever pays the price, the next quarter amount (25, 50 or 75 cents) or a dollar bill, so every money line is fixed. Money lines are said one sentence at a time, so the sentences are shared:
- Hellos: 5 templates x 6 snacks (30), "Here you go!", 5 thank-yous.
- Counted: "That's <paid>." (9 amounts), then "Just right for the <snack>!" (6) or "The <snack> is <price>, so I need some change, please." (6).
- Too much: "Whoa, that's too much change!", "Count up from <price> again." (6), "Stop at <paid>." (4).
- Too little: "Hmm, I paid <paid>." (4), "Count up from <price> to <paid>." (12), "I think I need a little more."
- Closing (once a day, also what Read says on the closed sign): "Closing time! The bell rang at 3:45. You helped 9 customers.", then "The till has <d> dollars and" with the cents from the group ("15 cents"), then "That's <d> hundred" and the cents again; with no cents, "The till has <d> dollars." and "That's <d> hundred cents!". Nine customers bring between $1.62 and $5.40, and every cents value from 0 to 99 can happen.

Size: every clip is inlined into corner-store.html, and the file must stay under 2 MB. The estimate from other tools' clips is about 1.9 MB when everything is recorded, so check the bundle size after recording; if it is over, set a small "tempo" (for example 1.1) in lines.json and re-encode.

Browser-voice text: only the debug hook `window.__close()` called before nine customers are served ("You helped N customers" for N other than 9). Nothing in normal use.
