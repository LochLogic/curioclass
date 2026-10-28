CHANGES

# Sensitivity review: career-cluster-explorer

Fresh review, 2026-10-28, done cold against BASELINE.md (rules 4, 5, 6) and STANDARDS.md. I read spec.md, src.html,
careers.json, notes.md, art/prompts.json and voice/lines.json, and checked the bundled draft in headless Chrome at
1366x768 (the crosswalk, the braids booth, the help booth and the clinic cards).

Overall: careful work. Job titles are gender neutral (Power Line Worker, Firefighter, Police Officer, Flight
Attendant). Every trail line and description uses "A ..." or singular "they", and no line says who does a job. Trades
and service work are written about with respect, and the shared pay scale makes the point well (a power line worker
with a high school diploma at $95,320 sits above most bachelor's jobs). There are no blockers. The one thing to fix is
the people emoji.

## Blocker

None.

## Should fix

1. **The people emoji give jobs a gender, and not evenly.** Only three careers use a person emoji. Family Doctor is a
   woman (👩‍⚕️). Chef is a man (👨‍🍳), which matches the stereotype (BLS: most head chefs are men). Hairstylist is 💇,
   which Windows (checked in the render), Apple and Google all draw as a woman, and it shows the client instead of the
   worker; that matches the stereotype too. Human Resources Specialist already uses the gender-neutral 🧑‍💼, so the
   set is inconsistent. A student scanning cards sees "the doctor is a woman, the chef is a man, the hair person is a
   woman," which is exactly the casting this tool should avoid.
   **Fix:** in `scripts/careers_data.py`, change the emoji on line 72 (doctor) `👩‍⚕️` to `🧑‍⚕️`, line 82 (chef)
   `👨‍🍳` to `🧑‍🍳`, and line 87 (stylist) `💇` to `✂️`. Rebuild `careers.json` with the builder so both
   career-cluster-explorer and career-match-quiz get the same emoji. That changes career-match-quiz's display too; it
   is the same fix there, so note it in that tool's notes. The gender-neutral person emoji render on Windows 10 1903+
   and 11, ChromeOS, iOS and Android.

## Polish

2. **The only person drawn in the town has one fixed skin tone.** The police officer at the crosswalk (src.html line
   637) is the only human figure in the scene, and its head is filled `#d9b98a`, a light tan. It is tiny and mostly
   under the marker, but it still gives the one townsperson a race. Everything else in the scene is stylized plum and
   lavender.
   **Fix:** on line 637, change the head circle's fill from `'#d9b98a'` to `'#c9c3ea'` (the scene's lavender), so the
   figure reads as a stylized silhouette like the rest of the town. Keep the blue uniform and cap.

## Nit

3. **Fashion Designer's 👗 shows only a dress,** while the job (its own "does" line) is "clothing, shoes and
   accessories" for everyone. **Fix:** `scripts/careers_data.py` line 38, `👗` to `🧵`.
4. **Musician names one faith:** "concerts, recordings, churches, schools and games." **Fix:** `scripts/careers_data.py`
   line 36, "churches" to "places of worship".
5. **Hotel Manager's Try it now assumes the family travels:** "Plan a family trip and compare places to stay."
   **Fix:** `scripts/careers_data.py` line 85, to "Plan a pretend weekend trip and compare three places to stay
   online."

## Checked and fine (no change)

- **Braids booth** ("The braids and face paint booth", Hairstylist). Braid and face paint booths are ordinary at
  county fairs, the scene draws only a tent, and hair braiding is respected work across many cultures. It does not
  link the job to any group. The Try line ("Practice braids or styles with family or friends") is fine. Keep it.
- **Police figure at the crosswalk.** A crosswalk is the gentlest public-safety moment to show, and the second line
  ("someone tests evidence from a stolen bike case") is low-stakes and age-appropriate. No weapons, no arrests, no
  victims. Keep it, with polish 2 for the skin tone.
- **Help booth wording.** "The community help booth. 'Someone to talk to, and help finding help.'" It is warm and
  non-clinical, it does not stigmatize, and it does not imply the student needs help. The three descriptions (school
  counselor, social worker, psychologist) are plain and kind. The tool asks nothing personal, so it needs no crisis
  line. Keep it.
- **Pay and "which jobs need a degree."** The column is called "No degree needed," not "low" or "entry." The ladder
  goes left to right without ranking words, and every cluster uses one pay scale. The key says "many also have other
  ways in." The trades' paths name paid apprenticeships. Cook ("quickly and carefully during busy restaurant shifts")
  and the other service jobs are written about with respect. notes.md's talk question about a bachelor's-heavy cluster
  and the "Decline does not mean disappearing" prompt are balanced. "Ways in at 4 of 5 levels" is a neutral count.
- **Who does which job.** No gendered titles, no pronouns that assign a gender (the farmer "sells what they grow"),
  and no line ties a job to a culture, class or ability. Air Traffic Controller's "most start before age 31" is the
  FAA's real rule.
- **Disability.** Nothing excludes or pities anyone. The physical therapist and athletic trainer are framed around
  recovery and moving better.
- **Every other emoji** is an object, an animal or a vehicle (🔥 ⚙️ 🏭 🤖 🐾 🐕 🧪 🚜 🎨 🎬 🎸 📷 🎮 🎞️ 🛋️ ✍️ 🎭 🎥 💡 🪚 🔧 📐 🌉
  ❄️ 🚧 💻 🔐 📊 🌐 🖥️ 🍎 🧸 🧭 📚 🏅 🌬️ ☀️ 🌿 🦉 ⚡ 🌦️ 🧾 💰 🎲 🩺 💉 🦵 🦷 🚑 💊 🤝 🧠 🏥 🏈 🍳 🎉 🏨 ✈️ 📋 🗂️ 📣 🏡 🎙️ 🔎
  🚒 🚓 ⚖️ 📁 🏙️ 📞 🔬 🛫 🚚 📦 🚗 🛩️ 📡 🚀). ✍️ and 🤝 are hands in default yellow, with no skin tone set. That is fine.
- **Art prompts.** None: `assets` is empty and everything is drawn in code, so no local-model prompt draws people.
- **Voice lines.** All nine are neutral how-to and event lines.
- **Classroom-safe language and privacy** (rules 6 and 7) pass. The privacy line is on screen in the panel.
