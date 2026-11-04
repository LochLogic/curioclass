// Timelines generator, grades 2-12. Built-in, fact-checked event sets (each event: year, a short neutral description,
// and a source). Students place lettered events on an SVG timeline, then answer questions about order, years between
// events and centuries. Grade sets how many events, and whether BCE years and centuries appear. "My own life" is a
// blank timeline of the student's own years. Years: negative numbers are BCE (-490 prints as 490 BCE).
(() => {
const { blank, part, example, esc, svg, lines } = Gen.h;

const B = 'Encyclopaedia Britannica', NA = 'National Archives (archives.gov)', NPS = 'National Park Service (nps.gov)',
  LOC = 'Library of Congress', OH = 'U.S. State Department, Office of the Historian', NASA = 'NASA', SI = 'Smithsonian Institution';
const SETS = {
  inv: { name: 'Inventions and technology', ev: [
    [1608, 'Hans Lippershey asks for a patent on a telescope in the Netherlands.', B],
    [1712, 'Thomas Newcomen builds a steam engine to pump water out of mines.', B],
    [1769, 'James Watt patents a more efficient steam engine.', B],
    [1793, 'Eli Whitney builds the cotton gin, a machine that separates cotton fibers from seeds.', B],
    [1800, 'Alessandro Volta makes the first electric battery.', B],
    [1804, 'Richard Trevithick runs the first steam locomotive on rails, in Wales.', B],
    [1825, 'The Stockton and Darlington Railway in England opens, the first public railway to use steam locomotives.', B],
    [1839, 'Louis Daguerre announces the daguerreotype, an early way to take photographs.', SI],
    [1844, 'Samuel Morse sends a telegraph message from Washington, D.C., to Baltimore.', LOC],
    [1846, 'Elias Howe patents a sewing machine.', B],
    [1854, 'Elisha Otis shows a safety elevator that will not fall if its rope breaks.', B],
    [1867, 'Alfred Nobel patents dynamite.', 'Nobel Prize Outreach (nobelprize.org)'],
    [1876, 'Alexander Graham Bell patents the telephone.', LOC],
    [1877, 'Thomas Edison invents the phonograph, a machine that records and plays back sound.', LOC],
    [1879, 'Thomas Edison\'s team tests a light bulb that glows for many hours.', SI],
    [1886, 'Karl Benz patents a car powered by a gasoline engine.', B],
    [1901, 'Guglielmo Marconi receives a radio signal sent across the Atlantic Ocean.', B],
    [1903, 'Orville and Wilbur Wright make the first controlled, powered airplane flights, at Kitty Hawk, North Carolina.', SI],
    [1908, 'The Ford Motor Company begins selling the Model T car.', 'The Henry Ford museum (thehenryford.org)'],
    [1913, 'Ford starts a moving assembly line to build cars faster.', 'The Henry Ford museum (thehenryford.org)'],
    [1927, 'Philo Farnsworth first sends a picture with his all-electronic television system.', B],
    [1946, 'ENIAC, one of the first general-purpose electronic computers, is shown to the public.', SI],
    [1947, 'Scientists at Bell Labs invent the transistor.', B],
    [1958, 'Jack Kilby builds the first integrated circuit (computer chip).', 'Texas Instruments; Nobel Prize Outreach'],
    [1969, 'The first message is sent over ARPANET, the network that grew into the internet.', SI],
    [1971, 'Intel releases the 4004, the first microprocessor offered for sale.', SI],
    [1973, 'Martin Cooper makes the first call from a handheld cell phone.', B],
    [1981, 'IBM releases its Personal Computer.', SI],
    [1989, 'Tim Berners-Lee proposes the World Wide Web.', 'CERN (home.cern)'],
    [2007, 'Apple introduces the iPhone, a touchscreen smartphone.', B],
  ] },
  space: { name: 'Space exploration', ev: [
    [1926, 'Robert Goddard launches the first liquid-fueled rocket.', NASA],
    [1957, 'The Soviet Union launches Sputnik 1, the first artificial satellite.', NASA],
    [1958, 'Explorer 1, the first U.S. satellite, is launched.', NASA],
    [1959, 'The Soviet probe Luna 2 becomes the first spacecraft to reach the Moon.', NASA],
    [1961, 'Yuri Gagarin of the Soviet Union becomes the first person in space.', NASA],
    [1962, 'John Glenn becomes the first American to orbit Earth.', NASA],
    [1963, 'Valentina Tereshkova of the Soviet Union becomes the first woman in space.', NASA],
    [1965, 'Alexei Leonov makes the first spacewalk.', NASA],
    [1966, 'The Soviet probe Luna 9 makes the first soft landing on the Moon.', NASA],
    [1968, 'Apollo 8 astronauts become the first people to orbit the Moon.', NASA],
    [1969, 'Apollo 11 lands on the Moon; Neil Armstrong and Buzz Aldrin walk on its surface.', NASA],
    [1971, 'The Soviet Union launches Salyut 1, the first space station.', NASA],
    [1972, 'Apollo 17 makes the last crewed Moon landing of the Apollo program.', NASA],
    [1973, 'NASA launches Skylab, the first U.S. space station.', NASA],
    [1976, 'Viking 1 becomes the first U.S. spacecraft to land on Mars.', NASA],
    [1977, 'NASA launches the Voyager 1 and Voyager 2 probes.', NASA],
    [1981, 'Space Shuttle Columbia makes the first shuttle flight.', NASA],
    [1983, 'Sally Ride becomes the first American woman in space.', NASA],
    [1986, 'The Soviet Union launches the first part of the Mir space station.', NASA],
    [1990, 'The Hubble Space Telescope is launched.', NASA],
    [1992, 'Mae Jemison becomes the first African American woman in space.', NASA],
    [1997, 'Mars Pathfinder lands, and its small rover Sojourner drives on Mars.', NASA],
    [1998, 'Zarya, the first part of the International Space Station, is launched.', NASA],
    [2000, 'The first long-term crew moves into the International Space Station.', NASA],
    [2003, 'Yang Liwei becomes the first astronaut launched by China.', B],
    [2004, 'The rovers Spirit and Opportunity land on Mars.', NASA],
    [2012, 'The rover Curiosity lands on Mars.', NASA],
    [2015, 'The New Horizons probe flies past Pluto.', NASA],
    [2020, 'SpaceX\'s Crew Dragon carries NASA astronauts to the space station, the first time a company-owned spacecraft takes people into orbit.', NASA],
    [2021, 'The James Webb Space Telescope is launched.', NASA],
  ] },
  sci: { name: 'Science discoveries', ev: [
    [1543, 'Nicolaus Copernicus publishes a book saying Earth and the planets move around the Sun.', B],
    [1610, 'Galileo Galilei reports seeing four moons circling Jupiter through his telescope.', B],
    [1665, 'Robert Hooke publishes drawings of cork seen under a microscope and calls its tiny boxes "cells."', B],
    [1676, 'Antonie van Leeuwenhoek reports seeing tiny living things in water with his microscope.', B],
    [1687, 'Isaac Newton publishes his laws of motion and his law of gravity.', B],
    [1735, 'Carl Linnaeus publishes a system for sorting and naming living things.', B],
    [1774, 'Joseph Priestley makes oxygen gas in his lab and sees a candle burn brightly in it.', 'American Chemical Society'],
    [1781, 'William Herschel discovers the planet Uranus.', B],
    [1796, 'Edward Jenner uses cowpox to protect a boy from smallpox, work that leads to the first vaccine.', 'Centers for Disease Control and Prevention'],
    [1831, 'Michael Faraday discovers that a moving magnet can make electricity flow.', B],
    [1846, 'Astronomers in Berlin find the planet Neptune.', NASA],
    [1859, 'Charles Darwin publishes On the Origin of Species, about evolution by natural selection.', B],
    [1865, 'Gregor Mendel reports his experiments on how pea plants pass on traits.', B],
    [1869, 'Dmitri Mendeleev publishes his periodic table of the elements.', 'Royal Society of Chemistry'],
    [1885, 'Louis Pasteur gives a rabies vaccine to a boy bitten by a rabid dog, and the boy lives.', 'Institut Pasteur'],
    [1895, 'Wilhelm Roentgen discovers X-rays.', 'Nobel Prize Outreach (nobelprize.org)'],
    [1898, 'Marie and Pierre Curie discover the elements polonium and radium.', 'Nobel Prize Outreach (nobelprize.org)'],
    [1905, 'Albert Einstein publishes his theory of special relativity.', B],
    [1912, 'Alfred Wegener proposes that the continents have drifted apart.', B],
    [1928, 'Alexander Fleming discovers penicillin, which later becomes the first widely used antibiotic.', 'American Chemical Society'],
    [1929, 'Edwin Hubble publishes evidence that the universe is expanding.', NASA],
    [1930, 'Clyde Tombaugh discovers Pluto.', NASA],
    [1953, 'James Watson and Francis Crick, using X-ray images from Rosalind Franklin\'s lab, describe the double helix shape of DNA.', 'National Human Genome Research Institute'],
    [1955, 'Jonas Salk\'s polio vaccine is announced as safe and effective.', 'Centers for Disease Control and Prevention'],
    [1960, 'Jane Goodall begins studying wild chimpanzees in Tanzania and sees them make tools.', 'Jane Goodall Institute'],
    [1962, 'Rachel Carson publishes Silent Spring, about the harm pesticides can do.', B],
    [1974, 'Scientists in Ethiopia find "Lucy," a 3.2-million-year-old skeleton of an early human relative.', SI],
    [1980, 'Luis and Walter Alvarez propose that an asteroid impact helped wipe out the dinosaurs.', B],
    [2003, 'The Human Genome Project finishes reading almost all of the code in human DNA.', 'National Human Genome Research Institute'],
    [2012, 'Scientists at CERN announce the discovery of the Higgs boson particle.', 'CERN (home.cern)'],
    [2015, 'The LIGO observatories detect gravitational waves for the first time.', 'Caltech and MIT LIGO Laboratory'],
  ] },
  us1: { name: 'U.S. history: to 1800', ev: [
    [1492, 'Christopher Columbus\'s ships reach islands in the Caribbean, starting lasting contact between Europe and the Americas.', B],
    [1513, 'Juan Ponce de Leon reaches Florida and names it.', B],
    [1565, 'Spanish settlers found St. Augustine, Florida, the oldest continuously settled European city in the continental U.S.', NPS],
    [1607, 'English colonists found Jamestown, Virginia, on land of the Powhatan people.', NPS],
    [1619, 'The House of Burgesses, the first elected lawmaking assembly in the English colonies, meets in Virginia.', B],
    [1620, 'The Pilgrims arrive on the Mayflower and found Plymouth Colony, on land of the Wampanoag people.', B],
    [1630, 'Puritan colonists found Boston in the Massachusetts Bay Colony.', B],
    [1636, 'Harvard, the first college in the English colonies, is founded.', B],
    [1664, 'The English take New Amsterdam from the Dutch and rename it New York.', B],
    [1675, 'King Philip\'s War (Metacom\'s War) begins between New England colonists and Native nations.', B],
    [1680, 'In the Pueblo Revolt, Pueblo people drive Spanish colonists out of New Mexico.', NPS],
    [1681, 'William Penn receives a charter to start the colony of Pennsylvania.', B],
    [1692, 'The Salem witch trials take place in Massachusetts.', B],
    [1733, 'James Oglethorpe and settlers found Savannah, starting Georgia, the last of the 13 colonies.', B],
    [1754, 'The French and Indian War begins.', OH],
    [1763, 'The Treaty of Paris ends the French and Indian War.', OH],
    [1765, 'Britain\'s Parliament passes the Stamp Act, a tax on printed papers in the colonies.', B],
    [1770, 'In the Boston Massacre, British soldiers shoot and kill five colonists.', B],
    [1773, 'Colonists dump British tea into the harbor at the Boston Tea Party.', B],
    [1775, 'The Battles of Lexington and Concord begin the Revolutionary War.', NPS],
    [1776, 'The Continental Congress adopts the Declaration of Independence.', NA],
    [1781, 'British forces surrender at Yorktown, Virginia.', NPS],
    [1783, 'In the Treaty of Paris, Britain recognizes the United States as independent.', OH],
    [1787, 'Delegates sign the U.S. Constitution in Philadelphia.', NA],
    [1789, 'George Washington becomes the first president of the United States.', LOC],
    [1790, 'The United States counts its people in the first national census.', 'U.S. Census Bureau'],
    [1791, 'The Bill of Rights, the first ten amendments to the Constitution, is ratified.', NA],
    [1800, 'Congress meets in Washington, D.C., the new capital, for the first time.', 'U.S. Senate (senate.gov)'],
  ] },
  us2: { name: 'U.S. history: 1800 to 1877', ev: [
    [1803, 'The United States buys the Louisiana Territory from France.', NA],
    [1804, 'Lewis and Clark set out to explore the land west of the Mississippi River.', NPS],
    [1812, 'The War of 1812 between the United States and Britain begins.', OH],
    [1814, 'Francis Scott Key writes the poem that becomes "The Star-Spangled Banner."', SI],
    [1820, 'The Missouri Compromise allows Missouri to join as a slave state and Maine as a free state.', LOC],
    [1823, 'President James Monroe warns European nations not to set up new colonies in the Americas (the Monroe Doctrine).', OH],
    [1825, 'The Erie Canal opens, linking the Great Lakes to the Hudson River and New York City.', B],
    [1830, 'President Andrew Jackson signs the Indian Removal Act.', LOC],
    [1831, 'Nat Turner leads a revolt of enslaved people in Virginia.', B],
    [1838, 'The U.S. Army forces the Cherokee Nation west; thousands die on the journey known as the Trail of Tears.', NPS],
    [1845, 'Frederick Douglass publishes the story of his life in slavery.', LOC],
    [1846, 'The Mexican-American War begins.', OH],
    [1848, 'Gold is found at Sutter\'s Mill, starting the California Gold Rush.', B],
    [1849, 'Harriet Tubman escapes from slavery in Maryland.', NPS],
    [1852, 'Harriet Beecher Stowe publishes Uncle Tom\'s Cabin, a novel against slavery.', B],
    [1857, 'In the Dred Scott decision, the Supreme Court rules that Black Americans cannot be citizens.', NA],
    [1860, 'Abraham Lincoln is elected president.', B],
    [1861, 'The Civil War begins with the attack on Fort Sumter in South Carolina.', NPS],
    [1862, 'The Homestead Act offers western land, for a small fee, to settlers who live on it and farm it for five years.', NA],
    [1863, 'The Emancipation Proclamation takes effect, declaring enslaved people in Confederate states free.', NA],
    [1865, 'The Civil War ends, and the 13th Amendment ends slavery in the United States.', NA],
    [1867, 'The United States buys Alaska from Russia.', OH],
    [1868, 'The 14th Amendment makes everyone born in the U.S. a citizen and promises equal protection of the laws.', NA],
    [1869, 'The first transcontinental railroad is completed in Utah.', NPS],
    [1870, 'The 15th Amendment says a man cannot be denied the vote because of his race.', NA],
    [1872, 'Yellowstone becomes the first national park.', NPS],
    [1876, 'Lakota, Northern Cheyenne and Arapaho warriors defeat U.S. troops at the Battle of the Little Bighorn.', NPS],
    [1877, 'Reconstruction ends as President Rutherford B. Hayes pulls federal troops back from Southern state capitals.', B],
  ] },
  us3: { name: 'U.S. history: 1877 to today', ev: [
    [1886, 'The Statue of Liberty is dedicated in New York Harbor.', NPS],
    [1892, 'Ellis Island opens as an immigration station in New York.', NPS],
    [1896, 'In Plessy v. Ferguson, the Supreme Court allows racial segregation as "separate but equal."', NA],
    [1898, 'The Spanish-American War is fought.', OH],
    [1906, 'Congress passes the Pure Food and Drug Act.', 'U.S. Food and Drug Administration'],
    [1909, 'The NAACP is founded to work for the rights of Black Americans.', LOC],
    [1914, 'The Panama Canal opens.', B],
    [1917, 'The United States enters World War I.', NA],
    [1920, 'The 19th Amendment says citizens cannot be denied the vote because of their sex.', NA],
    [1924, 'The Indian Citizenship Act makes Native Americans born in the U.S. citizens.', NA],
    [1927, 'Charles Lindbergh flies alone without stopping across the Atlantic Ocean.', SI],
    [1929, 'The stock market crashes, and the Great Depression begins.', B],
    [1933, 'Franklin D. Roosevelt becomes president and starts the New Deal.', B],
    [1935, 'The Social Security Act becomes law.', 'Social Security Administration'],
    [1941, 'Japan attacks Pearl Harbor, Hawaii, and the United States enters World War II.', NA],
    [1942, 'An order by President Roosevelt leads to the forced removal and imprisonment of about 120,000 Japanese Americans.', NA],
    [1945, 'World War II ends.', NA],
    [1947, 'Jackie Robinson joins the Brooklyn Dodgers and integrates Major League Baseball.', LOC],
    [1954, 'In Brown v. Board of Education, the Supreme Court rules that school segregation is unconstitutional.', NA],
    [1955, 'Rosa Parks is arrested, and the Montgomery Bus Boycott begins.', LOC],
    [1959, 'Alaska and Hawaii become the 49th and 50th states.', NA],
    [1963, 'About 250,000 people join the March on Washington for Jobs and Freedom.', NPS],
    [1964, 'The Civil Rights Act outlaws discrimination based on race, color, religion, sex or national origin.', NA],
    [1965, 'The Voting Rights Act protects the right to vote.', NA],
    [1969, 'Apollo 11 astronauts become the first people to walk on the Moon.', NASA],
    [1973, 'The last U.S. combat troops leave Vietnam.', OH],
    [1990, 'The Americans with Disabilities Act becomes law.', 'ADA.gov (U.S. Department of Justice)'],
    [2001, 'Terrorist attacks on September 11 kill nearly 3,000 people in New York, Virginia and Pennsylvania.', '9/11 Memorial and Museum'],
    [2008, 'Barack Obama is elected the first African American president.', B],
  ] },
  w1: { name: 'World history: ancient world, to 500 CE', minGrade: 6, ev: [
    [-776, 'By tradition, the first recorded Olympic Games are held at Olympia in Greece.', B],
    [-490, 'At the Battle of Marathon, Athenians defeat an invading Persian army.', B],
    [-480, 'A Persian army defeats a small Greek force led by Spartans at Thermopylae.', B],
    [-447, 'Athenians begin building the Parthenon.', B],
    [-399, 'The philosopher Socrates is put on trial and sentenced to death in Athens.', B],
    [-336, 'Alexander the Great becomes king of Macedonia.', B],
    [-332, 'Alexander the Great founds the city of Alexandria in Egypt, in about this year.', B],
    [-323, 'Alexander the Great dies in Babylon.', B],
    [-264, 'The First Punic War between Rome and Carthage begins.', B],
    [-221, 'Qin Shi Huang unites China and becomes its first emperor.', B],
    [-218, 'Hannibal of Carthage leads an army with elephants across the Alps.', B],
    [-206, 'The Han dynasty begins in China.', B],
    [-146, 'Rome destroys the city of Carthage.', B],
    [-44, 'Julius Caesar is killed in Rome.', B],
    [-27, 'Augustus becomes the first Roman emperor.', B],
    [70, 'Roman soldiers destroy the Second Temple in Jerusalem.', B],
    [79, 'The volcano Vesuvius erupts and buries the Roman town of Pompeii.', B],
    [80, 'The Colosseum opens in Rome.', B],
    [105, 'By tradition, Cai Lun presents an improved way of making paper to the Han emperor of China.', B],
    [117, 'The Roman Empire reaches its largest size under the emperor Trajan.', B],
    [122, 'Work begins on Hadrian\'s Wall across northern Britain, in about this year.', 'English Heritage'],
    [313, 'The Edict of Milan lets Christians in the Roman Empire worship openly.', B],
    [330, 'Constantinople becomes the new capital of the Roman Empire.', B],
    [410, 'The Visigoths capture and loot the city of Rome.', B],
    [476, 'The last Western Roman emperor is removed from power.', B],
  ] },
  w2: { name: 'World history: 500 to 1750', ev: [
    [537, 'The Hagia Sophia is completed in Constantinople.', B],
    [618, 'The Tang dynasty begins in China.', B],
    [622, 'The Prophet Muhammad moves from Mecca to Medina, the year that begins the Islamic calendar.', B],
    [732, 'Frankish forces defeat an Umayyad army at the Battle of Tours in France.', B],
    [800, 'Charlemagne is crowned emperor in Rome.', B],
    [868, 'The Diamond Sutra, the oldest known dated printed book, is printed in China.', 'British Library'],
    [1066, 'William of Normandy conquers England after the Battle of Hastings.', B],
    [1096, 'The First Crusade begins.', B],
    [1206, 'Genghis Khan is named ruler of the united Mongol peoples.', B],
    [1215, 'King John of England agrees to the Magna Carta, which limits the king\'s power.', 'British Library'],
    [1271, 'Marco Polo sets out from Venice on his journey to China.', B],
    [1324, 'Mansa Musa, ruler of the Mali Empire, passes through Cairo on his pilgrimage to Mecca.', B],
    [1325, 'By tradition, the Mexica (Aztec) people found the city of Tenochtitlan.', B],
    [1347, 'The Black Death, a plague, reaches Europe.', B],
    [1368, 'The Ming dynasty begins in China.', B],
    [1405, 'Admiral Zheng He of China sets out on the first of seven great sea voyages.', B],
    [1453, 'The Ottoman Empire captures Constantinople.', B],
    [1492, 'Christopher Columbus\'s ships reach islands in the Caribbean.', B],
    [1498, 'Vasco da Gama of Portugal reaches India by sailing around Africa.', B],
    [1517, 'Martin Luther writes his Ninety-five Theses, starting the Protestant Reformation.', B],
    [1521, 'Tenochtitlan falls to Spanish forces and their Indigenous allies.', B],
    [1522, 'The surviving ship of Ferdinand Magellan\'s expedition finishes the first voyage around the world.', B],
    [1588, 'The English navy defeats the Spanish Armada.', B],
    [1603, 'Tokugawa Ieyasu becomes shogun, starting more than 250 years of Tokugawa rule in Japan.', B],
    [1632, 'Work begins on the Taj Mahal in Agra, India, in about this year.', 'UNESCO World Heritage Centre'],
    [1644, 'The Qing dynasty takes Beijing and begins its rule of China.', B],
    [1648, 'The Peace of Westphalia ends the Thirty Years\' War in Europe.', B],
    [1688, 'In the Glorious Revolution, King James II of England is replaced by William and Mary.', B],
  ] },
  w3: { name: 'World history: 1750 to today', ev: [
    [1789, 'The French Revolution begins with the storming of the Bastille in Paris.', B],
    [1791, 'Enslaved people in the French colony of Saint-Domingue rise up, beginning the Haitian Revolution.', B],
    [1804, 'Haiti declares independence, the first nation founded after a successful revolt by enslaved people.', B],
    [1815, 'Napoleon is defeated at the Battle of Waterloo.', B],
    [1821, 'Mexico wins independence from Spain.', B],
    [1833, 'Britain passes a law to end slavery in most of its empire.', 'UK Parliament (parliament.uk)'],
    [1857, 'Soldiers and others in India rise up against the British East India Company.', B],
    [1868, 'The Meiji Restoration returns power to Japan\'s emperor and begins rapid modernization.', B],
    [1869, 'The Suez Canal opens, linking the Mediterranean Sea and the Red Sea.', B],
    [1884, 'European powers meet at the Berlin Conference to set rules for claiming land in Africa.', B],
    [1888, 'Brazil abolishes slavery, the last country in the Americas to do so.', B],
    [1893, 'New Zealand becomes the first self-governing country where women can vote in national elections.', 'New Zealand Ministry for Culture and Heritage (nzhistory.govt.nz)'],
    [1914, 'World War I begins in Europe.', 'Imperial War Museums'],
    [1917, 'The Russian Revolution overthrows the czar.', B],
    [1918, 'World War I ends.', 'Imperial War Museums'],
    [1939, 'World War II begins when Germany invades Poland.', 'Imperial War Museums'],
    [1945, 'The United Nations is founded after World War II.', 'United Nations (un.org)'],
    [1947, 'India and Pakistan become independent from Britain.', B],
    [1948, 'The United Nations adopts the Universal Declaration of Human Rights.', 'United Nations (un.org)'],
    [1949, 'The People\'s Republic of China is founded.', B],
    [1957, 'Led by Kwame Nkrumah, Ghana wins independence from Britain.', B],
    [1961, 'The Berlin Wall is built, dividing East and West Berlin.', B],
    [1989, 'The Berlin Wall is opened, and people begin tearing it down.', B],
    [1991, 'The Soviet Union breaks apart into 15 countries.', B],
    [1993, 'The European Union is formed.', 'European Union (european-union.europa.eu)'],
    [1994, 'Nelson Mandela is elected the first Black president of South Africa.', 'Nelson Mandela Foundation'],
  ] },
};
// the "all eras" sets combine the era sets
SETS.usall = { name: 'U.S. history: all eras', ev: [...SETS.us1.ev, ...SETS.us2.ev, ...SETS.us3.ev] };
SETS.wall = { name: 'World history: all eras', ev: [...SETS.w1.ev, ...SETS.w2.ev, ...SETS.w3.ev] };
const ORDER = ['inv', 'space', 'sci', 'us1', 'us2', 'us3', 'usall', 'w1', 'w2', 'w3', 'wall'];
const GRADES = Array.from({ length: 11 }, (_, i) => [String(i + 2), `Grade ${i + 2}`]);
const COUNT = g => g <= 3 ? 6 : g === 4 ? 7 : g <= 8 ? 8 : 10;
const LET = 'ABCDEFGHIJ';

// year helpers: negative is BCE; there is no year 0
const yr = y => y < 0 ? `${-y} BCE` : (y < 1000 ? `${y} CE` : String(y));
const between = (a, b) => { const [x, y] = a < b ? [a, b] : [b, a]; return x < 0 && y > 0 ? y - x - 1 : y - x; };
const ord = n => n + (n % 100 >= 11 && n % 100 <= 13 ? 'th' : ['th', 'st', 'nd', 'rd'][n % 10] || 'th');
const century = y => y < 0 ? `${ord(Math.ceil(-y / 100))} century BCE` : `${ord(Math.ceil(y / 100))} century`;
const pos = y => y;   // place on the line (the missing year 0 is one year out of hundreds, too small to see)
const events = (key, g) => (SETS[key] ? SETS[key].ev : []).filter(e => g >= 6 || e[0] > 0);

// a nice tick step for a span of years
function step(span) {
  for (const s of [1, 2, 5, 10, 20, 25, 50, 100, 200, 250, 500, 1000]) if (span / s <= 10) return s;
  return 1000;
}
const tick = t => t === 0 ? 'BCE | CE' : t < 0 ? `${-t} BCE` : String(t);
function drawLine(evs, showKey) {
  const W = 720, H = 132, L = 34, R = 686, Y = 78;
  const lo = Math.min(...evs.map(e => pos(e.y))), hi = Math.max(...evs.map(e => pos(e.y)));
  const st = step(hi - lo);
  const a = Math.floor(lo / st) * st, b = Math.ceil(hi / st) * st;
  const x = p => L + (p - a) / (b - a) * (R - L);
  let body = `<line x1="${L - 12}" y1="${Y}" x2="${R + 12}" y2="${Y}" stroke="#222" stroke-width="2"/>` +
    `<path d="M${R + 12} ${Y - 5} L${R + 20} ${Y} L${R + 12} ${Y + 5} Z" fill="#222"/><path d="M${L - 12} ${Y - 5} L${L - 20} ${Y} L${L - 12} ${Y + 5} Z" fill="#222"/>`;
  const minor = st / (st % 5 === 0 && st >= 5 ? 5 : st % 2 === 0 ? 2 : 1);
  for (let t = a; t <= b + 1e-9; t += minor) if (Math.abs(t / st - Math.round(t / st)) > 1e-9) body += `<line x1="${x(t).toFixed(1)}" y1="${Y - 4}" x2="${x(t).toFixed(1)}" y2="${Y + 4}" stroke="#222" stroke-width="1"/>`;
  for (let t = a; t <= b; t += st) {
    const lab = tick(t);
    body += `<line x1="${x(t).toFixed(1)}" y1="${Y - 9}" x2="${x(t).toFixed(1)}" y2="${Y + 9}" stroke="#222" stroke-width="1.6"/>` +
      `<text x="${x(t).toFixed(1)}" y="${Y + 26}" text-anchor="middle" font-size="${b - a >= 1000 && st >= 100 ? 12 : 13}" font-family="sans-serif" fill="#222">${lab}</text>`;
  }
  // key: a mark and the letter for each event, raised to a second or third row when letters would touch
  const rows = [];
  let key = '';
  for (const e of evs.slice().sort((p, q) => p.y - q.y)) {
    const ex = x(pos(e.y));
    let lv = 0; while (rows[lv] != null && ex - rows[lv] < 18) lv++;
    rows[lv] = ex;
    const ty = Y - 16 - lv * 17;
    key += `<line x1="${ex.toFixed(1)}" y1="${Y}" x2="${ex.toFixed(1)}" y2="${ty + 3}" stroke="#b03020" stroke-width="1.2"/><circle cx="${ex.toFixed(1)}" cy="${Y}" r="3.5" fill="#b03020"/>` +
      `<text x="${ex.toFixed(1)}" y="${ty}" text-anchor="middle" font-size="14" font-weight="700" font-family="sans-serif" fill="#b03020">${e.letter}</text>`;
  }
  if (showKey !== false) body += `<g class="ws-keyonly">${key}</g>`;
  return { html: svg(W, H, body, `Timeline from ${tick(a)} to ${tick(b)}, with tick marks every ${st} years`), a, b, st, x };
}

const LIFE = ['I was born.', 'I learned to walk.', 'I started school.', 'I lost my first tooth.', 'I learned to ride a bike or a scooter.',
  'I learned to swim.', 'I made a good friend.', 'I went on a trip I remember.', 'I read a whole book by myself.', 'I learned something new that I am proud of.',
  'I had a favorite birthday.', 'I moved to a new grade.', 'I tried a new food I liked.', 'I joined a team, club or class.'];

Gen.add('timeline', {
  title: 'Timelines', type: 'Timeline',
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '5' },
    { id: 'set', label: 'Events', type: 'select', def: 'inv',
      options: v => ORDER.filter(k => +v.grade >= (SETS[k].minGrade || 0)).map(k => [k, SETS[k].name]).concat([['life', 'My own life (a blank timeline)']]) },
  ],
  make(v, r) {
    const g = +v.grade, items = [], parts = [];
    if (v.set === 'life') {
      const top = Math.min(18, g + 6);
      const W = 720, H = 120, L = 30, R = 690, Y = 70, x = a => L + a / top * (R - L);
      let body = `<line x1="${L}" y1="${Y}" x2="${R}" y2="${Y}" stroke="#222" stroke-width="2"/>`;
      for (let a = 0; a <= top; a++) body += `<line x1="${x(a)}" y1="${Y - 8}" x2="${x(a)}" y2="${Y + 8}" stroke="#222" stroke-width="1.5"/><text x="${x(a)}" y="${Y + 24}" text-anchor="middle" font-size="13" font-family="sans-serif">${a}</text>`;
      body += `<text x="${(L + R) / 2}" y="${Y + 44}" text-anchor="middle" font-size="12" font-family="sans-serif">my age in years</text>`;
      const picks = [LIFE[0]].concat(r.sample(LIFE.slice(1), g <= 3 ? 4 : 5));
      picks.forEach((p, i) => items.push({ q: p, a: 'Answers vary', letter: LET[i] }));
      parts.push(part('', example('If you started school when you were 5, write the letter for "I started school" above the 5.', 'Then write the year it happened on the line next to the event.')));
      parts.push(part('My timeline', svg(W, H + 10, body, `A blank timeline of ages 0 to ${top}`)));
      parts.push(part('Events from my life', `<ol class="ws-fill gen-tlife" type="A">${picks.map(p => `<li>${esc(p)} Age: <span class="ws-blank" style="min-width:3em"></span> Year: <span class="ws-blank" style="min-width:4em"></span></li>`).join('')}</ol>` +
        `<p class="ws-text">${LET[picks.length]}. Add one more event of your own. Write it here, then put its letter on the timeline.</p>${lines(1)}`));
      const qs = ['How many years passed between event A and event C?', 'Which event on your timeline happened most recently?'];
      qs.forEach(q => items.push({ q, a: 'Answers vary' }));
      parts.push(part('Think about it', qs.map((q, i) => `<p class="ws-text"><b>${i + 1}.</b> ${q}</p>${lines(1)}`).join('')));
      return { title: 'My Life Timeline', level: `Grade ${g}`, ican: 'I can put events from my own life in order on a timeline.',
        directions: 'Write your age and the year for each event. Then write each event\'s letter above the timeline at the age it happened.',
        minutes: 20, materials: 'pencil', parts, items,
        mistakes: 'Placing letters by the order they are listed instead of by age, and mixing up ages with years.',
        notes: 'There is no key: every student\'s timeline is different. Students may ask a family member for dates, or estimate; "about age 4" is fine. Let students skip any event they would rather not share and add their own instead.' };
    }
    const all = events(v.set, g);
    const n = COUNT(g);
    // pick events with different years, spread out enough to place
    let evs = null;
    for (let t = 0; t < 400 && !evs; t++) {
      const s = r.sample(all, n).sort((p, q) => p[0] - q[0]);
      const ys = s.map(e => pos(e[0]));
      if (new Set(ys).size < n) continue;
      const span = ys[n - 1] - ys[0];
      if (ys.slice(1).every((y, i) => y - ys[i] >= span / 34)) evs = s;
    }
    if (!evs) evs = r.sample(all, n).sort((p, q) => p[0] - q[0]);
    const letters = r.shuffle(LET.slice(0, n).split(''));
    const list = evs.map((e, i) => ({ y: e[0], text: e[1], src: e[2], letter: letters[i] })).sort((p, q) => p.letter.localeCompare(q.letter));
    const tl = drawLine(list);
    for (const e of list) items.push({ q: `Place ${e.letter}: ${e.text}`, a: yr(e.y), letter: e.letter, y: e.y, text: e.text, kind: 'place' });
    const byY = list.slice().sort((p, q) => p.y - q.y);
    const hasBCE = list.some(e => e.y < 0);
    // questions
    const qs = [];
    qs.push({ html: 'Write the letters in order, from the earliest event to the most recent.', a: byY.map(e => e.letter).join(', '), kind: 'order', em: n * 1.6 });
    const pairs = [];
    for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) if (i !== j) pairs.push([list[i], list[j]]);
    const ba = r.sample(pairs, g <= 2 ? 3 : g <= 5 ? 2 : 1);
    for (const [p, q] of ba) qs.push({ html: `Did ${p.letter} happen before or after ${q.letter}?`, a: p.y < q.y ? 'before' : 'after', kind: 'ba', p: p.letter, q2: q.letter });
    if (g <= 2) {
      qs.push({ html: 'Which event happened first?', a: byY[0].letter, kind: 'first' });
      qs.push({ html: 'Which event happened last?', a: byY[n - 1].letter, kind: 'last' });
    } else {
      const k = g === 3 ? 2 : g <= 8 ? 2 : 3;
      const ok = ([p, q]) => p.y < q.y && (g >= 9 || (p.y < 0) === (q.y < 0)) && (g > 3 || between(p.y, q.y) < 1000) && between(p.y, q.y) >= 5;
      const cross = ([p, q]) => p.y < 0 && q.y > 0;
      let cand = r.shuffle(pairs.filter(ok));
      // at most one question crosses from BCE to CE (and at grade 9-12, one does when it can); spread the letters out
      const crossing = cand.filter(cross), plain = cand.filter(c => !cross(c));
      const picked = [];
      if (g >= 9 && crossing.length) picked.push(crossing[0]);
      const busy = c => picked.some(([p, q]) => [p, q].some(e => e === c[0] || e === c[1]));
      for (const pass of [0, 1]) for (const c of plain) {
        if (picked.length >= k) break;
        if (picked.includes(c) || (pass === 0 && busy(c))) continue;
        picked.push(c);
      }
      for (const [p, q] of picked) qs.push({ html: `How many years passed between ${p.letter} and ${q.letter}?`, a: String(between(p.y, q.y)), kind: 'yrs', p: p.letter, q2: q.letter });
    }
    if (g >= 4) {
      const cs = r.sample(list.filter(e => e.y % 100 !== 0), 2);
      for (const e of cs) qs.push({ html: `In which century did ${e.letter} happen?`, a: century(e.y), kind: 'cent', p: e.letter });
    }
    qs.forEach((q, i) => items.push({ q: `${i + 1}. ${q.html}`, a: q.a, kind: q.kind, p: q.p, q2: q.q2 }));
    // a model, from an event in the set that is not on this sheet
    const spare = all.filter(e => !list.some(x => x.y === e[0]));
    const m = spare.length ? r.pick(spare) : all[0];
    const cnote = g >= 4 ? ` It happened in the ${century(m[0])}${m[0] > 0 ? `: the ${ord(Math.ceil(m[0] / 100))} century is the years ${Math.ceil(m[0] / 100) * 100 - 99} to ${Math.ceil(m[0] / 100) * 100}` : ''}.` : '';
    parts.push(part('', example(`<b>${yr(m[0])}:</b> ${esc(m[1])}`,
      `Find ${yr(m[0])} between the tick marks on the timeline and write the event's letter just above that spot.${cnote}`)));
    parts.push(part('The timeline', tl.html));
    parts.push(part('Events', `<ul class="gen-tlist">${list.map(e => `<li><b class="gen-tlet">${e.letter}</b><b class="gen-tyr">${yr(e.y)}</b><span>${esc(e.text)}</span></li>`).join('')}</ul>`));
    parts.push(part('Questions', `<ol class="ws-fill gen-tq">${qs.map(q => `<li>${q.html} ${blank(q.a, q.em)}</li>`).join('')}</ol>` +
      (hasBCE ? '<p class="ws-sub">BCE years count down toward year 1, so 500 BCE comes before 400 BCE. There was no year 0: 1 BCE is followed by 1 CE.</p>' : '')));
    const setName = SETS[v.set].name;
    const teacher = '<h3>Events and sources</h3><ul>' + byY.map(e => `<li><b>${e.letter}</b>, ${yr(e.y)}: ${esc(e.text)} <i>Source: ${esc(e.src)}.</i></li>`).join('') + '</ul>' +
      (qs.some(q => q.kind === 'yrs') ? '<h3>Years between</h3><ul>' + qs.filter(q => q.kind === 'yrs').map(q => {
        const p = list.find(e => e.letter === q.p), w = list.find(e => e.letter === q.q2);
        const [x1, x2] = p.y < w.y ? [p, w] : [w, p];
        return `<li>${q.p} to ${q.q2}: ${x1.y < 0 && x2.y > 0 ? `${-x1.y} + ${x2.y} − 1 = ${q.a} (no year 0)` : x1.y < 0 ? `${-x1.y} − ${-x2.y} = ${q.a}` : `${x2.y} − ${x1.y} = ${q.a}`}</li>`; }).join('') + '</ul>' : '');
    return {
      title: `${setName}: Timeline`, level: `Grade ${g}, ${n} events`,
      ican: `I can put events in order on a timeline${g >= 3 ? ' and find the years between them' : ''}${g >= 4 ? ' and name the century' : ''}.`,
      directions: 'Read each event. Write its letter above the timeline where its year belongs. Then answer the questions on the lines.',
      minutes: g <= 3 ? 20 : 25, materials: 'pencil, ruler (optional)', parts, items, teacher,
      mistakes: (g >= 4 ? 'Naming the century by its first two digits (1969 is in the 20th century, not the 19th). ' : '') +
        (hasBCE ? 'Treating BCE years like CE years: 300 BCE is earlier than 200 BCE, and the years between 50 BCE and 50 CE are 99 because there was no year 0. ' : '') +
        'Placing letters evenly along the line instead of by the scale.',
      notes: 'Press New sheet for a different set of events from the same group. Every event comes with a source on this page. Descriptions are short and neutral; hard history is stated plainly, and is worth a class conversation.',
    };
  },
  verify(s, v) {
    const out = [];
    if (v.set === 'life') return out;
    const g = +v.grade, data = events(v.set, g);
    const place = s.items.filter(i => i.kind === 'place');
    const yOf = {};
    for (const it of place) {
      const e = data.find(x => x[1] === it.text);
      if (!e) { out.push(`${it.letter}: event not in the set`); continue; }
      if (it.a !== (e[0] < 0 ? `${-e[0]} BCE` : e[0] < 1000 ? `${e[0]} CE` : String(e[0]))) out.push(`${it.letter}: year ${it.a}, data says ${e[0]}`);
      if (e[0] < 0 && g < 6) out.push(`${it.letter}: BCE year at grade ${g}`);
      yOf[it.letter] = e[0];
    }
    if (new Set(Object.values(yOf)).size !== place.length) out.push('two events share a year');
    for (const it of s.items) {
      if (it.kind === 'order') { const want = Object.keys(yOf).sort((a, b) => yOf[a] - yOf[b]).join(', '); if (it.a !== want) out.push(`order ${it.a}, should be ${want}`); }
      if (it.kind === 'ba') { const want = yOf[it.p] < yOf[it.q2] ? 'before' : 'after'; if (it.a !== want) out.push(`${it.q}: ${it.a}, should be ${want}`); }
      if (it.kind === 'first' || it.kind === 'last') { const ls = Object.keys(yOf).sort((a, b) => yOf[a] - yOf[b]); const want = it.kind === 'first' ? ls[0] : ls[ls.length - 1]; if (it.a !== want) out.push(`${it.q}: ${it.a}`); }
      if (it.kind === 'yrs') {
        let a = yOf[it.p], b = yOf[it.q2]; if (a > b) [a, b] = [b, a];
        // count year by year from a to b; the step from 1 BCE (-1) to 1 CE is one year, since there was no year 0
        let want = 0; for (let y = a; y !== b;) { y = y === -1 ? 1 : y + 1; want++; }
        if (it.a !== String(want)) out.push(`${it.q}: ${it.a}, should be ${want}`);
        if (want < 0) out.push(`${it.q}: negative`);
      }
      if (it.kind === 'cent') {
        const y = yOf[it.p], c = Math.floor((Math.abs(y) - 1) / 100) + 1;
        const sfx = [11, 12, 13].includes(c % 100) ? 'th' : ({ 1: 'st', 2: 'nd', 3: 'rd' }[c % 10] || 'th');
        const want = `${c}${sfx} century${y < 0 ? ' BCE' : ''}`;
        if (it.a !== want) out.push(`${it.q}: ${it.a}, should be ${want}`);
        if (y % 100 === 0) out.push(`${it.q}: a year ending in 00 is ambiguous`);
      }
    }
    return out;
  },
  css: `.gen-tlist { list-style: none; padding: 0; margin: 4px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 6px 20px; font-size: 14px; }
.gen-tlist li { display: grid; grid-template-columns: auto auto 1fr; gap: 6px; align-items: baseline; }
.gen-tyr { white-space: nowrap; }
.gen-tlet { display: inline-grid; place-items: center; min-width: 1.6em; height: 1.6em; border: 1.5px solid #333; border-radius: 50%; font-size: 12px; flex: none; }
.gen-tq li { margin-bottom: 9px; }
.gen-tlife li { margin-bottom: 10px; }
@media print { .gen-tlist { font-size: 9.5pt; } }`,
});
})();
