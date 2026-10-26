## A 5-minute start

1. Open **Workshop**. Tap **Multiply by a** in the parts list, then tap the first slot on the top line; do the same with **Add a**. Use the card's **+** to make them Multiply by 3 and Add 4. The strip above the floor reads **f(x) = 3x + 4**.
2. Build the undo line in the "obvious" order: **Divide by 3**, then **Subtract 4** (the undo line runs right to left, from OUT back to HOME). Press **Run**. Tokens come home wrong: 2 comes back as −0.6667. Ask why.
3. Swap the two undo cards (select one and press **[** or **]**, or the arrows on the card). Run again: all 8 tokens come home, and the strip shows **g(x) = f⁻¹(x)**. Socks and shoes: the last thing done is the first thing undone.
4. Now make the top line **Add 3, Square** and clear the undo line. Before anything runs, the OUT bin shows a crash: "−2 and −4 both come out as 1", and the verdict is **Can't be undone as built**. Turn on **Gate**, set it to x ≥ −3, and build Square root, Subtract 3.

## The two modes

- **Workshop** (free explore): any top line (up to 6 machines), any undo line (up to 8), an optional gate on the input, **Run** (the 8 test tokens −6, −2.5, −1, 0, 0.5, 2, 3, 9), **Send my number** (one token of your own), **Random chain**, **Clear undo**, **Clear all**.
- **Puzzles** (optional challenge): 12 levels. The top line is locked (except level 11). Levels 1 to 6 and 12 ask for the undo chain; 7, 8 and 10 need a gate first; 9 cannot be undone (press **Can't be undone**); 11 asks for a 2-machine chain that undoes itself. **Hint** gives up to three hints; the third on undo levels shows a glowing ghost card. Solved levels get a check mark that is remembered on this device.
- **Graph** (either mode): f (solid blue), the undo chain g (dashed purple) and y = x (dotted green), each with its equation. **Mirror** flips f across y = x; a right g lies on the mirror. If f is not one-to-one, a vertical line marks one output with two ways back.

## Talk about it

- Why must the undo line run in reverse order? Where else in life do you undo things last-in, first-out?
- Which machines undo themselves? (Flip sign, Reciprocal.) What 2-machine chains undo themselves?
- Square and absolute value "forget" the sign. Why does a gate that only lets in x ≥ 0 (or only x ≤ 0) fix them? What is the smallest gate that works for Add 3, Square?
- Rounding forgets more than a sign. Why can no gate fix level 9?
- On the graph, why is the inverse the mirror image across y = x? What does the vertical line test say about the mirror of x squared?

## Good to know

- Done-when arithmetic: Multiply by 3, Add 4 with undo Divide by 3, Subtract 4 sends 2 to 6, 10, 3.3333, −0.6667. Level 7 with gate x ≤ −3: −6 + 3 = −3, squared 9, root 3, flipped −3, minus 3 gives −6.
- A token is home when its result is within one billionth (relative) of where it started. Tokens stopped on the top line (by the gate or by a machine's domain) are not counted; tokens stopped on the undo line are lost.
- The crash check runs after every edit without animation. It follows the set of values that can enter each machine as a union of intervals (from all real numbers, or the gate's ray). Square and Absolute value are safe only when everything entering them is on one side of zero; Round and Always 5 never are. When a machine is unsafe, the tool tries inputs 0, 1, −1, 2, −2 ... to ±10, then tenths near zero first, then a wider search, and shows the first two inputs that truly crash: the values entering the machine differ, the machine sends them to the same value, and both get through the rest of the chain. Outputs that are only close never count. If none of the listed inputs crash (a fold far from zero), it works a pair out from the interval sets, preferring inputs that still crash when typed in; a pair it can only give approximately is marked "about".
- If a machine can merge two inputs but no pair that gets through the rest of the chain turns up, the tool never says "Undoes it": a run where every token comes home shows **Can't confirm the undo** instead.
- In Puzzles the crash appears after the first Run (or after pressing Can't be undone), so level 9 is not given away on load. In Workshop it shows after every edit.
- After a run, the verdict also names two test tokens that crashed, when there are any (for Add 3, Square: −6 and 0 both leave the top line as 9).
- Very large results show in scientific notation (7.29e+8); a result too large for the computer is tagged "too big" (Cube, Cube, Power of 2 sends 9 off the scale). Power of 2 of a huge negative number shows as 0, because the computer cannot hold such a tiny number.
- Keyboard: Tab to a part, Enter lifts it, arrow keys pick a slot (Up and Down switch lines), Enter drops, Escape cancels. Tab to a machine card: + and − change its number, [ and ] move it, Delete removes it. The **Selected machine** box in the panel has the same actions as full-size buttons.
- In the site's 16:10 embed and on narrow screens the floor switches to a compact design that draws only the filled slots plus one empty slot, so its text stays readable; the verdict and tips sit in a bar under the floor. Full screen shows every slot.
- Facts follow OpenStax Precalculus 2e, sections 1.4, 1.7 and 6.3 (CC BY 4.0). Standards: F-BF.A.1c, F-BF.B.4a to 4d, F-BF.B.5.
