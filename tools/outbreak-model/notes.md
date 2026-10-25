## A 5-minute start

1. Open **Grow** with **Virus X in a city** (10 cases, doubling every 3 days). Press **Play** and watch the **Milestones** list: 100, 1 thousand, 10 thousand ... each arrives 9.97 days after the last.
2. Press **Log**. The curve becomes a straight line, and the note says why: every 10 times bigger takes the same 9.97 days.
3. Switch to **Ask when** and press **1 million**. The **Solve it** panel works it three ways (base 2, base 10, base e) and all land on t = 49.83 days. Press **Check it** to run the clock to that moment.

## The three modes

- **Grow** (explore): the clock runs across the window in about 8 seconds and the curve draws itself. **Compare steady growth** adds a dashed straight line that adds the first day's gain every day, with its own milestone column (Virus X steady needs about 385 thousand days to reach 1 million).
- **Ask when** (the one idea): drag the blue target line, type a target (plain digits, commas or 1e6), or use the quick buttons. Each Solve column ends at the same t; the table shows the whole days either side (day 49: 825,702; day 50: 1,040,319). **Guess first** covers the answer until a guess pin is dropped on the time axis and **Show the answer** is pressed. Nothing is scored.
- **Hit the ceiling** (where the model breaks): pick Denver, Colorado, United States or World. The pure exponential passes the population (shaded and labeled "more people than exist"); a dashed logistic curve with the same start and rate levels off under it. Virus X passes the United States on day 74.95, and the logistic reaches half of it the same day.

Shared controls: **Story** (five made-up presets), **Describe growth by** (doubling time, tenfold time or continuous rate: the curve never moves, only the description), **Start (a)**, the rate slider, **Growing / Shrinking**, **Play / Pause / Reset clock** and **Scale: Linear / Log**.

## Talk about it

- Why does every tenfold step take the same time? What would make the steps shorter?
- The three Solve columns use different bases. Why must they agree? Where does log 2 come from in the base 2 column?
- The Fading rumor halves every 5 days. Why is "when does it reach 2,100?" answered "Never", and what does the negative t from the formula mean?
- In Hit the ceiling, the exponential and logistic agree at first. When do they start to disagree, and why?
- Which assumption of the exponential model breaks first in a real school or city?

## Good to know

- Model: N(t) = a e^(k t). D = ln 2 / k, W = ln 10 / k, growth per unit e^k, percent (e^k minus 1) times 100. Virus X: D 3, W 9.97, k 0.2310, times 1.260 a day, up 26.0 percent.
- Checked answers: Rumor at school to 1,000: 16.76 hours. Virus X to 1 million: 49.83 days. Viral post to 1 million: 51.61 hours. Fading rumor to 10: 38.22 days. Steady spread to 1 million: 55.26 days. Virus X ceilings: Denver 48.38, Colorado 57.42, United States 74.95, World 88.73 days.
- The Solve columns show more digits for D, W and k (for example k = 0.23105) so the calculator line lands on the same 2-decimal answer.
- Every story is invented and labeled "A made-up example to explore the math, not a real forecast." Populations: 2020 Census (Denver 715,522, Colorado 5,773,714, United States 331,449,281) and the UN's 8 billion (November 15, 2022).
- In Hit the ceiling the linear y axis runs to 1.8 times the ceiling, so the shaded region and the logistic leveling are both visible; the exponential leaves the top with an "off the chart" arrow.
- Keyboard: Tab to the target handle (Up and Down change it, PageUp and PageDown by 10 times), the guess pin and the trace dot (Left and Right). With Motion off, Play and Check it jump straight to the end and zooms are instant.
- Content follows OpenStax, Algebra and Trigonometry 2e, sections 6.5 to 6.7 (CC BY 4.0). Standards: F-LE.A.4, F-IF.C.8b, F-IF.C.9.
