# 1. Two Stars, Two Fates
minutes: 40
materials: pencil, colored pencils (optional)
ican: I can explain how a star's mass decides its life path and which elements it makes by fusion.
directions: Fill in the stage chart for a star like the Sun and for a massive star (more than about 8 times the Sun's mass). Then draw both life paths as a branching diagram, from nebula to remnant, labeling the fusion at each stage.
mistakes: Students often think the Sun will explode as a supernova; it is far too small and will end as a white dwarf. Another common error is saying a star "burns" fuel; fusion joins nuclei and is not burning. Watch for stars that fuse past iron: fusing iron takes in energy instead of releasing it, so it cannot hold up the core.
notes: Mass boundaries are approximate: stars above about 8 solar masses end as supernovae, leaving a neutron star or, for the most massive (very roughly above 20 to 25 solar masses), often a black hole. The Sun's main-sequence life is about 10 billion years; it is about 4.6 billion years old now. Many elements heavier than iron form by neutron capture in dying giant stars, supernovae and neutron star mergers.

## Warm up
fill:
  - All stars are born in a cloud of gas and dust called a {nebula}.
  - On the main sequence, stars fuse {hydrogen} into {helium} in their cores.
  - The outward push from fusion balances the inward pull of {gravity}.

## Main: Stage chart
table: Stage | Sun-like star (about 1 solar mass) | Massive star (more than about 8 solar masses)
  - Birth | {nebula, then protostar} | {nebula, then protostar}
  - Main sequence: fusion | {hydrogen to helium, for about 10 billion years} | {hydrogen to helium, much faster: a few million to tens of millions of years}
  - Giant stage | {red giant: hydrogen fuses in a shell, then helium to carbon and oxygen in the core} | {red supergiant: helium to carbon, then carbon, neon, oxygen and silicon fusion in layers}
  - Last fusion product | {carbon and oxygen} | {iron}
  - Death | {outer layers drift off as a planetary nebula} | {core collapses: supernova explosion}
  - Remnant | {white dwarf} | {neutron star or black hole}
draw: Draw both life paths as a diagram that starts at one nebula and splits into two branches. Label each stage and its fusion. | 3.2

## Explain
choice: Why does fusion in a massive star's core stop at iron?
  - Iron is too cold to fuse.
  * Fusing iron takes in energy instead of releasing it.
  - All the hydrogen has turned into iron.
  - Iron leaves the star as a solar wind.
write: Massive stars have far more fuel than the Sun, yet they live much shorter lives. Explain why.
  lines: 3
  key: Their much stronger gravity squeezes the core to higher temperature and pressure, so fusion runs far faster. They use up their fuel much faster than the Sun, even though they have more of it.
write: Explain how the iron in your blood connects to the death of massive stars.
  lines: 3
  key: Iron is made by fusion in the cores of massive stars and spread into space by supernova explosions. That material mixed into the nebula that formed the Sun and Earth, so the iron in our bodies was made in stars that died before the Sun was born.

## Stretch
write: A common estimate for a star's main-sequence life is 10 billion years x M^-2.5, where M is its mass in solar masses. Estimate the life of a 10 solar-mass star. Show your work.
  lines: 3
  key: 10^-2.5 = about 0.0032, so 10 billion years x 0.0032 = about 32 million years (roughly 30 million years).

# 5. Hubble's Law From Data
minutes: 40
materials: pencil, ruler, calculator
ican: I can graph galaxy distance against recession speed, find the Hubble constant from the slope, and use it to estimate the age of the universe.
directions: The table gives the distance and the speed moving away from us (recession speed) for six galaxy clusters. Plot the points, draw a best-fit line through the origin, find its slope, and use the slope to estimate how old the universe is.
mistakes: Students often draw a line that misses the origin; at zero distance there is no expansion to see, so the line should pass through (0, 0). Watch the units: the slope is in km/s per Mpc, and students who divide distance by speed get a tiny number. In the age estimate, students forget that 1/H0 assumes the universe has always expanded at today's rate; it is an estimate, not the measured age.
notes: Distances and speeds are rounded from published measurements of the clusters' average redshifts and distances (Virgo and Fornax from surface brightness and Cepheid-based distances; the farther clusters from redshift surveys). Cluster distances carry 5 to 10 percent uncertainty. A least-squares line through the origin gives about 71 km/s per Mpc; accept 65 to 75. The shortcut 978 / H0 converts the Hubble time to billions of years, because 1 Mpc divided by 1 km/s is about 978 billion years. With H0 = 70, the Hubble time is about 14.0 billion years; the measured age of the universe is about 13.8 billion years. Hubble's own 1929 value was about 500 km/s per Mpc, because his distances were too small, which gave an age of about 2 billion years, younger than Earth.

## Warm up
fill:
  - 1 megaparsec (Mpc) is about {3.26} million light-years.
  - Light from a galaxy moving away from us is shifted toward longer, redder wavelengths. This is called {redshift}.

## The data
table: Galaxy cluster | Distance (Mpc) | Recession speed (km/s) | Speed / distance
  - Virgo | 16.5 | 1,100 | {67}
  - Fornax | 20 | 1,380 | {69}
  - Hydra | 50 | 3,780 | {76}
  - Perseus | 75 | 5,370 | {72}
  - Coma | 100 | 6,930 | {69}
  - Hercules | 155 | 10,970 | {71}

## Main: Graph and slope
graph: Distance (Mpc) | 0 160 20 | Recession speed (km/s) | 0 12000 2000
  key: 0,0 160,11300
note: The key line is the least-squares line through the origin, slope about 71 km/s per Mpc. Student points should scatter close to it.
fill:
  - Two points on my line: ({0}, {0}) and ({160}, {about 11,300})
  - Slope = Hubble constant H0 = about {70} km/s per Mpc
choice: What does the straight line through the origin tell us?
  - All galaxies move away at the same speed.
  * The farther away a galaxy is, the faster it moves away, in proportion to its distance.
  - Nearby galaxies move away faster than distant ones.
  - The Milky Way is the center of the universe.

## Age of the universe
example: If everything has moved apart at a steady rate, the time since all of it was together is distance / speed = 1 / H0. In billions of years, age = 978 / H0.
fill:
  - With my H0: age = 978 / {70} = about {14} billion years.
write: The best measurement of the age of the universe is about 13.8 billion years. Give one reason your estimate is not exactly the same.
  lines: 2
  key: The 1/H0 estimate assumes the expansion rate never changed, but it has (slowing at first, now speeding up). Also, the cluster distances and speeds have measurement uncertainty, and clusters have their own motions besides the expansion.

## Stretch
write: In 1929 Hubble found a slope of about 500 km/s per Mpc. What age does that give? Why did scientists find this hard to believe?
  lines: 3
  key: 978 / 500 = about 2.0 billion years. Rocks and radioactive dating already showed Earth was older than that (we now know about 4.5 billion years), and a universe cannot be younger than a planet in it. Better distances later lowered H0 and raised the age.

# 15. Earth's Layers From Seismic Waves
minutes: 40
materials: pencil, compass (or a round lid), protractor, ruler
ican: I can use P-wave and S-wave shadow zones to identify Earth's layers and explain why the outer core must be liquid.
directions: Read the evidence. Draw Earth's cross-section with its layers and the shadow zones in the box, label it, and use the shadow zones to explain what Earth is like inside.
mistakes: Students often say S waves "stop at the mantle" or that the shadow zone means the core blocks all waves. P waves do pass through the core; they bend sharply at the core boundary, which leaves the 104° to 140° ring with no direct P waves. Watch for angles measured along the surface in kilometers instead of at Earth's center in degrees. Students also mix up liquid outer core and solid inner core.
notes: Depths are rounded: average crust about 35 km under continents (5 to 10 km under oceans), mantle to about 2,890 km, outer core to about 5,150 km, center at 6,371 km. On a 5 cm Earth radius, the core boundary is at about 2.7 cm from the center and the inner core at about 1.0 cm. The shadow zones are measured as angles at Earth's center from the earthquake (epicenter at 0°). Andrija Mohorovičić found the crust and mantle boundary in 1909, Beno Gutenberg located the core in 1914, and Inge Lehmann used faint P waves inside the shadow zone to discover the solid inner core in 1936.

## The evidence
table: Wave | How it moves rock | Travels through
  - P wave (primary) | push and pull, like a spring | solids, liquids and gases
  - S wave (secondary) | side to side shaking (shear) | solids only
text: After an earthquake, seismographs all over the world record the waves. **Direct P waves** arrive everywhere from 0° to 104° from the earthquake, and again from 140° to 180°, but not in the ring from 104° to 140°. **Direct S waves** arrive only from 0° to 104°. Nothing from 104° all the way to 180° records an S wave. A few faint P waves do arrive inside the P-wave shadow zone.
fill:
  - The P-wave shadow zone runs from {104}° to {140}° from the earthquake.
  - The S-wave shadow zone runs from {104}° to {180}°.

## Main: Draw it
text: Steps: (1) Draw a circle with a 5 cm radius for Earth. Mark the earthquake at the top (0°). (2) With a protractor at the center, mark 104° and 140° on both sides. (3) Shade the P-wave shadow zone on the surface, and mark the S-wave shadow zone with a different pattern. (4) Draw the core boundary circle at 2.7 cm and the inner core at 1.0 cm. (5) Label the crust, mantle, outer core and inner core.
draw: Earth's cross-section and shadow zones | 3.6
table: Layer | Depth range (km) | Solid or liquid | Seismic evidence
  - Crust | {0 to about 35} | {solid} | {waves speed up sharply at its base (the Moho)}
  - Mantle | {about 35 to 2,890} | {solid (slowly flowing rock)} | {S waves travel through it}
  - Outer core | {2,890 to 5,150} | {liquid} | {S waves cannot pass; P waves slow and bend, making the shadow zone}
  - Inner core | {5,150 to 6,371} | {solid} | {faint P waves bounce off it into the shadow zone}

## Explain
write: Explain how the S-wave shadow zone shows that the outer core is liquid.
  lines: 3
  key: S waves are shear waves and can only travel through solids, because liquids cannot spring back from side-to-side shaking. No S waves reach anywhere from 104° to 180°, so something between them and the far side stops them. That is the outer core, so it must be liquid.
choice: Why is there a P-wave shadow zone if P waves can travel through liquid?
  - P waves stop at the core boundary.
  - P waves turn into S waves in the core.
  * P waves slow down and bend (refract) as they enter the core, so none land in the 104° to 140° ring.
  - The crust is too thick there.

## Stretch
write: If the whole core were solid, how would the shadow zones change? Explain.
  lines: 2
  key: There would be no S-wave shadow zone: S waves would pass through the core and arrive on the far side. There would still be some bending at the core boundary, but the big gap from 104° to 180° would disappear.

# 21. Life Remakes the Planet
minutes: 40
materials: pencil
ican: I can explain how changes in life and Earth's systems have affected each other over Earth's history.
directions: Place each event at its time on the two timelines by writing its letter above the line. Times are in millions of years ago (Ma), so -2400 means 2,400 million years ago. Then explain how each event changed Earth's systems.
mistakes: Students often think oxygen has always been in the air, or that it appeared as soon as life began. Life existed for more than a billion years before oxygen built up in the atmosphere. Another slip: confusing the scale. Timeline 1 covers billions of years; timeline 2 zooms in on the last 600 million.
notes: Dates are rounded, widely cited values and some are debated: the oldest widely accepted fossil evidence (stromatolites) is about 3,500 Ma or older; oxygen-making cyanobacteria were active by about 2,700 Ma or earlier; the Great Oxidation Event began about 2,400 Ma; Ediacaran animals about 575 Ma; the Cambrian explosion about 539 Ma; the first land plants about 470 Ma; the first forests about 385 Ma; coal swamp forests peaked about 300 Ma. Accept reasoning that names the right spheres: atmosphere, hydrosphere, geosphere and biosphere.

## Timeline 1: Early Earth (millions of years ago)
timeline: -4000 -500 500
  - -3500 | Microbes build layered mats called stromatolites in shallow seas.
  - -2700 | Cyanobacteria make oxygen by photosynthesis; it reacts with iron in the oceans.
  - -2400 | The Great Oxidation Event: oxygen builds up in the atmosphere for the first time.
  - -575 | The first large, soft-bodied multicellular animals appear in the oceans.

## Timeline 2: Life gets bigger (millions of years ago)
timeline: -600 -250 50
  - -539 | The Cambrian explosion: many animals with shells and skeletons appear.
  - -470 | The first small plants spread onto land.
  - -385 | The first forests grow, with deep roots.
  - -300 | Huge swamp forests are buried and become coal; oxygen in the air peaks.

## Main: How did each change Earth's systems?
table: Event | Spheres changed | How
  - Cambrian explosion | {biosphere, geosphere} | {shells locked carbon and calcium into seafloor limestone}
  - Coal swamps | {atmosphere, geosphere} | {buried carbon became coal; oxygen in the air rose to its highest level}
  - Cyanobacteria | {hydrosphere, geosphere} | {oxygen rusted dissolved iron, which settled as banded iron rock}
  - First forests | {atmosphere, geosphere} | {roots sped up rock weathering and pulled carbon dioxide from the air}
  - First land plants | {geosphere, biosphere} | {plants broke down rock and began to build soil}
  - First large animals | {biosphere} | {food webs with bigger animals began}
  - Great Oxidation Event | {atmosphere} | {oxygen in the air; methane fell; an ozone layer could form}
  - Stromatolite microbes | {biosphere, geosphere} | {microbes trapped sediment and built rock layers}

## Explain
write: Choose one event. Describe a feedback: how the change to Earth's systems in turn affected life.
  lines: 4
  key: Example: the Great Oxidation Event put oxygen in the air. Oxygen was toxic to many microbes, which retreated to places without oxygen, but it let an ozone layer form and later allowed organisms that use oxygen for energy, including animals. Another: forests pulled carbon dioxide from the air, cooling the climate, which changed where living things could survive.
choice: For about how long did life exist on Earth before oxygen built up in the atmosphere?
  - about 10 million years
  - about 100 million years
  * about 1,100 million years
  - oxygen was always there

## Stretch
write: Today, burning coal returns buried carbon to the atmosphere. Using the coal swamp event, explain why scientists call coal "ancient sunlight."
  lines: 3
  key: The plants in the swamp forests used sunlight to turn carbon dioxide into plant matter. When they were buried and became coal, that carbon and stored energy were locked away for about 300 million years. Burning coal releases that old stored energy and puts the carbon back into the air as carbon dioxide.

# 26. Vinegar Caves
minutes: 55
materials: 2 pieces of calcium carbonate chalk, 2 clear cups, white vinegar, water, balance, paper towels, goggles
ican: I can compare how chalk changes in water and in vinegar and explain how slightly acidic water carves limestone caves.
directions: Chalk and limestone are both made of calcium carbonate. Mass two equal pieces of dry chalk. Soak one in 100 mL of water and one in 100 mL of vinegar for 24 hours. Then dry them and mass them again. Record what you see on both days.
mistakes: Students often mass the chalk while it is still wet, which hides the loss; let pieces dry fully. Watch for students who say the vinegar "melted" the chalk; it reacted, making a new substance and carbon dioxide gas. Students also assume rainwater is far more acidic than vinegar; it is only slightly acidic, which is why caves take hundreds of thousands of years.
notes: Two class days: about 30 minutes to set up and predict, 25 minutes the next day to dry, mass and explain. Use calcium carbonate chalk. Some sidewalk chalk is calcium sulfate (gypsum) and will not fizz; test a crumb in vinegar first. Reaction: CaCO3 + 2CH3COOH makes Ca(CH3COO)2 + H2O + CO2. Vinegar is about pH 2.4 to 3; rainwater is about pH 5.6 because carbon dioxide dissolves in it to make carbonic acid, and water seeping through soil picks up more carbon dioxide and becomes more acidic. Sample data are typical of a 10 g stick in 100 mL of 5 percent vinegar; the stretch shows why the loss stops near 4 g. Safety: goggles; vinegar stings eyes. Do not taste anything.

## Warm up
fill:
  - Limestone and chalk are made mostly of the compound {calcium carbonate}.
  - Carbon dioxide dissolves in rainwater to make a weak acid called {carbonic acid}.
text: Prediction: Which piece will lose more mass, and why?
lines: 1

## Main: My data
table: Cup | Mass before (g) | Mass after drying (g) | Change (g) | Percent change | What I saw
  - Water | | | | |
  - Vinegar | | | | |
  height: 0.55
text: Percent change = (change / mass before) x 100.

## Sample class data
table: Cup | Mass before (g) | Mass after drying (g) | Change (g) | Percent change
  - Water | 10.0 | 9.9 | {-0.1} | {-1%}
  - Vinegar | 10.0 | 6.8 | {-3.2} | {-32%}
choice: The vinegar cup fizzed for hours. What were the bubbles?
  - oxygen
  - water vapor
  * carbon dioxide
  - air trapped in the chalk
write: Why did the chalk in water lose almost nothing, while the chalk in vinegar lost about a third of its mass?
  lines: 3
  key: Calcium carbonate barely dissolves in plain water. Vinegar contains acetic acid, which reacts with calcium carbonate, turning it into calcium acetate (which dissolves) plus water and carbon dioxide gas, so solid chalk is used up.

## Explain caves
write: Rainwater is far less acidic than vinegar. Explain how it can still carve a cave out of limestone.
  lines: 4
  key: Rain picks up carbon dioxide from the air and even more from soil, making weak carbonic acid. It seeps into cracks in limestone and slowly dissolves a tiny bit of calcium carbonate. Over hundreds of thousands of years, water flowing through the same cracks widens them into passages and caves.

## Stretch
write: 100 mL of vinegar holds about 0.083 mol of acetic acid. Each mole of calcium carbonate (100 g) needs 2 moles of acid. What is the most chalk 100 mL of vinegar can dissolve? Does the sample data fit?
  lines: 3
  key: 0.083 / 2 = about 0.042 mol of calcium carbonate, x 100 g/mol = about 4.2 g. The sample lost 3.2 g, less than 4.2 g, so it fits: the acid was not all used up, or the reaction slowed as the acid ran low.

# 36. Why Cities Grew There
minutes: 40
materials: pencil, atlas or world map (optional)
ican: I can explain how resources, natural hazards and climate shaped where cities grew.
directions: Plot each city on the latitude and longitude grid and label it. Read the city facts, then fill in the table and answer the questions.
mistakes: Students often swap latitude and longitude when plotting: longitude (east or west) goes across, latitude (north or south) goes up. West longitudes and south latitudes are negative here. Students also list only one reason per city; most cities grew for a mix of reasons, and the hazards often came with the very feature that drew people (a river that floods, a fault that built the mountains).
notes: Coordinates are rounded to 0.1°. Facts: Cairo grew where the Nile fans out into its delta, on fertile floodplain soil in a desert. Mexico City stands on the site of Tenochtitlan, founded by the Mexica (Aztecs) in about 1325 on an island in Lake Texcoco; the drained lakebed shakes hard in earthquakes (1985) and parts of the city sink by tens of centimeters a year as groundwater is pumped out. New Orleans controls the mouth of the Mississippi River; much of it is below sea level, and Hurricane Katrina flooded about 80 percent of the city in 2005. Mumbai grew around a deep natural harbor, joining seven islands with land reclaimed from the sea; monsoon floods are a yearly risk. Tokyo sits on the Kanto Plain, the largest flat plain in Japan, on a sheltered bay; the 1923 Great Kanto earthquake destroyed much of the city. Johannesburg grew after gold was found in the Witwatersrand in 1886; it has no large river, so water is piped in from far away.

## The cities
table: City | Latitude, longitude | City facts
  - Cairo, Egypt | 30.0° N, 31.2° E | Built where the Nile fans out into its delta, on rich floodplain soil. Rain almost never falls; summers pass 35 °C. Before the Aswan dams, the Nile flooded every summer.
  - Mexico City, Mexico | 19.4° N, 99.1° W | Founded about 1325 on an island in Lake Texcoco, 2,240 m up, with farmland around the lake. Mild all year. The drained lakebed shakes hard in earthquakes (1985) and sinks as groundwater is pumped out.
  - New Orleans, USA | 30.0° N, 90.1° W | Controls the mouth of the Mississippi River, a trade route to the middle of the country. Hot and humid. Much of it is below sea level; Hurricane Katrina flooded about 80 percent of it in 2005.
  - Mumbai, India | 19.1° N, 72.9° E | Seven islands joined by filling in the sea, around a deep, sheltered harbor. Hot all year, with heavy monsoon rains from June to September that flood low streets.
  - Tokyo, Japan | 35.7° N, 139.7° E | On the Kanto Plain, Japan's largest flat land for farming, beside a sheltered bay. Hot, humid summers. Three tectonic plates meet nearby; a 1923 earthquake destroyed much of the city.
  - Johannesburg, South Africa | 26.2° S, 28.0° E | Grew after gold was found in 1886 in the world's richest gold deposits. About 1,750 m up, with mild days and summer storms. No big river nearby, so water is piped in from far away.

## Main: Map them
text: Across: longitude (west is negative). Up: latitude (south is negative). Plot each city as a dot and write its name beside it.
graph: Longitude (°) | -180 180 30 | Latitude (°) | -60 60 15
  key: 31.2,30 -99.1,19.4 -90.1,30 72.9,19.1 139.7,35.7 28,-26.2
  dots: yes
table: City | Resource that drew people | Main hazard | Climate
  - Cairo | {Nile water and fertile soil} | {drought, heat; once, Nile floods} | {hot desert}
  - Mexico City | {lake water, island for defense, farmland} | {earthquakes, sinking ground} | {mild highland}
  - New Orleans | {river trade at the Mississippi's mouth} | {hurricanes and floods} | {hot, humid subtropical}
  - Mumbai | {deep natural harbor} | {monsoon floods} | {tropical monsoon}
  - Tokyo | {flat farmland and a sheltered bay} | {earthquakes (also tsunamis, typhoons)} | {humid subtropical}
  - Johannesburg | {gold} | {water shortage} | {mild highland, summer rain}

## Explain
write: Pick one city. Explain how its resources, hazards and climate together shaped where and how it grew.
  lines: 3
  key: Example: New Orleans grew at the mouth of the Mississippi because ships could move goods between the river and the Gulf of Mexico. The same low, wet land is below sea level and its hot, humid climate brings hurricanes, so the city needed levees and pumps, and it flooded badly when the levees failed in 2005.
