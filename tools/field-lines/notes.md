## A 5-minute start

1. Open **Twin boards**. It loads the **Opposite pair**: on the left two amber "m 3" discs with every line pointing in; on the right a "+3" and a "−3" with lines running from plus to minus. Ask: the objects are the same, so why do the pictures differ? (Charge has two signs, mass has one.)
2. Press **Single**, then **Halve distance** once so the probe sits 1.5 units out, then **Double distance**. Both readouts change by "× 0.25" at once: twice as far, a quarter of the field, on both boards.
3. Press **Like pair**. The probe sits at the midpoint and both boards read 0.00. Press **Release probe**: it stays still.
4. Switch to **Spread** and drag the Distance slider to 2, then 3. The same 36 lines cover 4, then 9 tiles, so each tile gets 9, then 4 lines: 1/4 and 1/9 of the strength at distance 1.
5. Switch to **Real pairs** and compare the hydrogen atom (electric 2.27 × 10<sup>39</sup> times stronger) with Earth and Moon (gravity wins).

## The three modes

- **Twin boards:** a 12 by 12 unit board drawn twice. Each object has a size from 1 to 5 that is its mass on the gravity board and the size of its charge on the electric board; only the electric board shows the sign. Drag objects or the probe on either board and the twin moves too. Up to 6 objects. View toggles: **Field lines** (on), **Arrow grid** (13 by 13 arrows, length grows with the log of strength), **Strength shading** (log strength, the same scale on both boards). The probe reads both fields, the direction ("pointing in" means toward the nearest object) and the distance to the selected or nearest object. **Double** and **Halve distance** move the probe along the line from the selected (or nearest) object. **Release probe** lets it go from rest on both boards at once: amber solid trail for gravity, red dashed trail for electric; each path ends when it touches a disc (landed, a filled dot), leaves the board (escaped) or after 8 seconds (an open ring).
- **Spread:** a point source sends 36 lines through a screen at distance r that is r by r tiles. One tile is highlighted with the lines that cross it. The plot shows lines per tile, 36 / r squared; **Show one over r** adds 36 / r dashed for comparison. **Gravity** and **Electric** change only the formula card and the source color, because the shape is the same.
- **Real pairs:** gravity and electric force for five real pairs on one log scale from 10<sup>−70</sup> N to 10<sup>40</sup> N. **Double** and **Halve distance** (up to 8 times, down to 1/8 of the start) change both forces by the same factor, so the ratio line never changes.

## Talk about it

- The gravity board always looks like an electric board where every charge is negative. Why can gravity never push?
- Where on the Like pair board do the fields cancel? Is there such a spot on the Opposite pair electric board?
- Why does the line spacing on a flat screen only sketch the strength? (In 3D the lines spread over a sphere, so the count per area falls as one over r squared; on a flat page they spread over a circle.)
- In Spread, why does doubling the distance cut the lines per tile to a quarter and not to a half?
- The electric force in a hydrogen atom is about 10<sup>39</sup> times the gravity, yet gravity holds the Moon in orbit. What makes the difference? (Matter is almost perfectly neutral, so charges cancel; mass only adds up.)

## Good to know

- Board units are invented: both boards use field = size / r squared with the constant 1, so the two pictures can be compared directly. Inside a disc the field uses r = the disc radius so values stay finite. Readouts under 0.005 show 0.00.
- Field lines: 6 per size unit evenly around each object, traced in steps of 0.05 units (RK4) along the field from positives and against it from negatives. A line stops on another disc, 2 units outside the board, at a zero point, or after 2000 steps; a line from a negative that ends on a positive is dropped (it is already drawn from the positive). Arrowheads every 2 units along each line start at a different spot on each line, and one that would land on top of another arrow is skipped, so crowded spots stay readable.
- **Release in Opposite pair:** the probe starts on the line of symmetry, so gravity pulls it straight through the midpoint and it swings back and forth until the 8 seconds are up; it does not land. The electric trail heads from the plus side toward the minus and swings around it. The trail shows each return pass a little to the side with a dot at every turnaround, the readout counts the turns, and the hint explains the balance. Nudge the probe sideways by at least 0.75 units first (Shift+arrow moves it 1 unit; one plain arrow press, 0.25 units, is not enough to land within 8 seconds) and the gravity trail lands on a disc. A good question for students: why does a perfectly centered probe never land?
- Real pairs constants (NIST CODATA 2018): G = 6.6743 × 10<sup>−11</sup> N m² / kg², k = 8.9875517923 × 10<sup>9</sup> N m² / C², e = 1.602176634 × 10<sup>−19</sup> C, proton 1.67262192369 × 10<sup>−27</sup> kg, electron 9.1093837015 × 10<sup>−31</sup> kg, Bohr radius 5.29177210903 × 10<sup>−11</sup> m. Earth 5.9722 × 10<sup>24</sup> kg and 6371.0 km, Moon 7.346 × 10<sup>22</sup> kg at 384,400 km (NASA fact sheets). The forces are computed live from these:

| Pair | Distance | Gravity | Electric | Ratio |
|---|---|---|---|---|
| Hydrogen atom | 5.29 × 10<sup>−11</sup> m | 3.63 × 10<sup>−47</sup> N | 8.24 × 10<sup>−8</sup> N, attract | 2.27 × 10<sup>39</sup> |
| Two protons | 1.0 × 10<sup>−15</sup> m | 1.87 × 10<sup>−34</sup> N | 231 N, repel | 1.24 × 10<sup>36</sup> |
| Two 1 kg balls, 1 μC each | 1 m | 6.67 × 10<sup>−11</sup> N | 8.99 × 10<sup>−3</sup> N, repel | 1.35 × 10<sup>8</sup> |
| Earth and a 1 kg apple | 6.371 × 10<sup>6</sup> m | 9.82 N | about 0 | Gravity wins |
| Earth and Moon | 3.844 × 10<sup>8</sup> m | 1.98 × 10<sup>20</sup> N | about 0 | Gravity wins |

- The apple cannot be moved closer than Earth's surface: inside Earth the one over r squared formula for a point mass no longer applies.
- Keyboard: Tab reaches each object (gravity board) and then the probe. Arrows move 0.25 units (Shift: 1 unit), + and − change size, S flips the sign, Delete removes, Escape deselects.
- With Motion off, Release draws both full paths at once and the Spread screen jumps instead of gliding. Nothing is saved except the Motion setting.
