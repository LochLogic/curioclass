"""Builds careers.json for the careers family (docs/families/careers.md).

Interest profiles (RIASEC), Job Zones and work context come from the O*NET 30.2 database (O*NET Resource
Center, CC BY 4.0). Pay and employment come from BLS Occupational Employment and Wage Statistics through the
public API (latest year, national). Typical entry-level education, job outlook, the number of jobs and the profile
link come from the BLS Occupational Outlook Handbook, 2025-35 edition (HANDBOOK below). The short descriptions,
paths and "try it" ideas are written for grades 6-8.

    python scripts/careers_data.py [<folder with O*NET text files>] [--out <careers.json>] [--more]

--out    where to write (default tools/career-match-quiz/careers.json)
--more   also write C_MORE, the extra careers career-cluster-explorer uses
Without an O*NET folder (no Interests.txt in it), the O*NET fields of the 83 come from the careers.json already at
--out, or failing that from tools/career-match-quiz/careers.json (read only). Set CURIO_CACHE to keep the BLS cache
somewhere else.
"""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from bls import oews, fetch

ROOT = os.path.join(os.path.dirname(__file__), '..')
QUIZ = os.path.join(ROOT, 'tools', 'career-match-quiz', 'careers.json')
args = sys.argv[1:]
OUT, MORE = QUIZ, '--more' in args
if '--out' in args:
    OUT = args[args.index('--out') + 1]
    del args[args.index('--out'):args.index('--out') + 2]
args = [a for a in args if a != '--more']
ONET = args[0] if args else '.'

CLUSTERS = {
    'mfg': 'Advanced Manufacturing', 'ag': 'Agriculture', 'arts': 'Arts, Entertainment and Design',
    'build': 'Construction', 'digital': 'Digital Technology', 'edu': 'Education',
    'energy': 'Energy and Natural Resources', 'fin': 'Financial Services', 'health': 'Healthcare and Human Services',
    'hosp': 'Hospitality, Events and Tourism', 'mgmt': 'Management and Entrepreneurship', 'mkt': 'Marketing and Sales',
    'public': 'Public Service and Safety', 'trans': 'Supply Chain and Transportation',
}

# id, name, O*NET code, cluster, emoji, what they do, how people get there, try it now, strengths it uses
C = [
 ('welder', 'Welder', '51-4121.00', 'mfg', '🔥', 'Joins metal parts together with intense heat to build bridges, ships, trucks and machines.', 'High school, then a welding certificate (a few months to a year) or an apprenticeship.', 'Build something with a hot glue gun, or watch a welding demo at a career fair.', ['build', 'active']),
 ('machinist', 'CNC Machinist', '51-4041.00', 'mfg', '⚙️', 'Programs and runs computer-controlled machines that cut metal into exact parts, down to a hair\'s width.', 'High school, then a technical program or apprenticeship.', 'Try a CAD program like Tinkercad and design a part.', ['build', 'numbers', 'tech']),
 ('ind-eng', 'Industrial Engineer', '17-2112.00', 'mfg', '🏭', 'Figures out how a factory, hospital or warehouse can work faster, safer and with less waste.', 'A bachelor\'s degree in engineering.', 'Time how long it takes to make a sandwich, then redesign the steps to make it faster.', ['numbers', 'organize', 'science']),
 ('robotics-tech', 'Robotics Technician', '17-3024.01', 'mfg', '🤖', 'Builds, tests and repairs the robots that weld, pack and move things in factories.', 'A two-year degree in robotics or engineering technology.', 'Join a robotics club or build a kit robot.', ['build', 'tech', 'science']),
 ('vet', 'Veterinarian', '29-1131.00', 'ag', '🐾', 'Diagnoses and treats sick and injured animals, from pets to farm animals.', 'A bachelor\'s degree, then four years of veterinary school.', 'Volunteer at an animal shelter or join 4-H.', ['care', 'science', 'calm']),
 ('vet-tech', 'Veterinary Technician', '29-2056.00', 'ag', '🐕', 'Helps vets by taking X-rays, running lab tests and caring for animals during surgery.', 'A two-year veterinary technology degree and a license.', 'Help care for a pet and keep a log of its health.', ['care', 'science']),
 ('food-sci', 'Food Scientist', '19-1012.00', 'ag', '🧪', 'Invents new foods and makes sure food is safe, tasty and lasts longer.', 'A bachelor\'s degree in food science, chemistry or biology.', 'Bake a recipe three ways, change one thing each time, and compare.', ['science', 'numbers']),
 ('farmer', 'Farmer or Rancher', '11-9013.00', 'ag', '🚜', 'Runs a farm or ranch: plants crops, raises animals, fixes equipment and sells what they grow.', 'Many learn by working on a farm; an agriculture degree helps.', 'Grow vegetables in a pot or school garden.', ['build', 'active', 'lead']),
 ('graphic-design', 'Graphic Designer', '27-1024.00', 'arts', '🎨', 'Designs logos, posters, apps and packaging that catch your eye and make ideas clear.', 'A bachelor\'s degree or a strong portfolio of work.', 'Design a poster for a school event.', ['art', 'tech']),
 ('animator', 'Animator', '27-1014.00', 'arts', '🎬', 'Creates the moving characters and effects in movies, shows and video games.', 'A bachelor\'s degree in animation or art, plus a demo reel.', 'Make a flip book or a stop-motion video with a phone.', ['art', 'tech']),
 ('musician', 'Musician', '27-2042.00', 'arts', '🎸', 'Plays, sings, writes and records music for concerts, recordings, places of worship, schools and games.', 'Years of practice; some study music in college.', 'Join band, choir or orchestra, or write your own song.', ['art']),
 ('photographer', 'Photographer', '27-4021.00', 'arts', '📷', 'Takes photos for news, weddings, sports, products and art.', 'Training on the job or in college, and a portfolio.', 'Do a photo challenge: one great photo a day for a week.', ['art', 'tech']),
 ('fashion', 'Fashion Designer', '27-1022.00', 'arts', '🧵', 'Sketches and creates clothing, shoes and accessories.', 'A bachelor\'s degree in fashion design, or a portfolio.', 'Redesign an old T-shirt or sketch a clothing line.', ['art']),
 ('game-design', 'Video Game Designer', '15-1255.01', 'arts', '🎮', 'Plans the levels, rules and stories of video games so they are fun to play.', 'A bachelor\'s degree in game design or computer science, plus games you have made.', 'Make a game in Scratch or design a board game.', ['art', 'tech', 'words']),
 ('film-editor', 'Film and Video Editor', '27-4032.00', 'arts', '🎞️', 'Cuts and arranges video clips, sound and effects to tell a story.', 'A bachelor\'s degree or experience and a reel.', 'Film and edit a one-minute video about your school.', ['art', 'tech']),
 ('interior', 'Interior Designer', '27-1025.00', 'arts', '🛋️', 'Plans rooms that look great and work well: colors, furniture, lighting and layout.', 'A bachelor\'s degree; many states require a license.', 'Draw a floor plan of your dream bedroom.', ['art', 'numbers', 'talk']),
 ('writer', 'Writer or Author', '27-3043.00', 'arts', '✍️', 'Writes books, articles, scripts, games and websites.', 'Usually a bachelor\'s degree, and lots of writing.', 'Write for the school paper or start a story journal.', ['words']),
 ('actor', 'Actor', '27-2011.00', 'arts', '🎭', 'Brings characters to life on stage, in films, shows and commercials.', 'Acting classes, practice and many auditions.', 'Try out for a school play.', ['art', 'talk']),
 ('director', 'Producer or Director', '27-2012.00', 'arts', '🎥', 'Leads the team that makes a movie, show, play or podcast, from idea to finished product.', 'A bachelor\'s degree and years of work in media.', 'Direct a short video with friends.', ['lead', 'art', 'organize']),
 ('electrician', 'Electrician', '47-2111.00', 'build', '💡', 'Installs and repairs the wiring that brings power and light to homes and buildings.', 'A four-to-five-year paid apprenticeship and a license.', 'Build a simple circuit with a battery, wire and bulb.', ['build', 'numbers', 'science']),
 ('carpenter', 'Carpenter', '47-2031.00', 'build', '🪚', 'Builds and repairs the wooden frames, stairs, cabinets and floors of buildings.', 'An apprenticeship or on-the-job training.', 'Build a birdhouse or a shelf.', ['build', 'active']),
 ('plumber', 'Plumber', '47-2152.00', 'build', '🔧', 'Installs and fixes the pipes that bring clean water in and take wastewater out.', 'A four-to-five-year paid apprenticeship and a license.', 'Help fix a leaky faucet at home (with an adult).', ['build', 'active']),
 ('architect', 'Architect', '17-1011.00', 'build', '📐', 'Designs buildings that are safe, useful and beautiful.', 'A degree in architecture, internship years and a license.', 'Design a house in Minecraft or on graph paper.', ['art', 'numbers', 'tech']),
 ('civil-eng', 'Civil Engineer', '17-2051.00', 'build', '🌉', 'Designs roads, bridges, tunnels and water systems.', 'A bachelor\'s degree in civil engineering.', 'Build a bridge from craft sticks and test how much it holds.', ['numbers', 'science', 'build']),
 ('hvac', 'HVAC Technician', '49-9021.00', 'build', '❄️', 'Installs and repairs heating, air conditioning and refrigeration systems.', 'A certificate program (six months to two years) or apprenticeship.', 'Find out how your home is heated and cooled.', ['build', 'science']),
 ('equip-op', 'Heavy Equipment Operator', '47-2073.00', 'build', '🚧', 'Drives bulldozers, cranes and excavators to move earth and build roads.', 'On-the-job training or an apprenticeship.', 'Visit a construction site viewing area or a heavy equipment show.', ['active', 'build', 'calm']),
 ('software-dev', 'Software Developer', '15-1252.00', 'digital', '💻', 'Designs and writes the code for apps, websites, games and the software inside cars and phones.', 'A bachelor\'s degree in computer science, or strong skills and projects.', 'Learn to code with Scratch or Python.', ['tech', 'numbers']),
 ('cyber', 'Cybersecurity Analyst', '15-1212.00', 'digital', '🔐', 'Protects computer networks from hackers and investigates attacks.', 'A bachelor\'s degree in computing, plus certifications.', 'Try a student cybersecurity game like picoCTF.', ['tech', 'science', 'calm']),
 ('data-sci', 'Data Scientist', '15-2051.00', 'digital', '📊', 'Finds patterns in huge amounts of data to answer questions and make predictions.', 'A bachelor\'s or master\'s degree in data science, statistics or math.', 'Survey your class and make a chart of the results.', ['numbers', 'tech', 'science']),
 ('web-dev', 'Web Developer', '15-1254.00', 'digital', '🌐', 'Builds websites and makes them fast, good-looking and easy to use.', 'A degree, a coding bootcamp or self-taught skills and a portfolio.', 'Build a web page about your favorite hobby.', ['tech', 'art']),
 ('it-support', 'IT Support Specialist', '15-1232.00', 'digital', '🖥️', 'Helps people fix computer problems and keeps a school or company\'s tech running.', 'Some college or certifications.', 'Help family members set up a new device.', ['tech', 'talk', 'calm']),
 ('teacher', 'Elementary Teacher', '25-2021.00', 'edu', '🍎', 'Teaches young students reading, math, science and how to be part of a class.', 'A bachelor\'s degree and a teaching license.', 'Read to younger kids or help at a summer camp.', ['care', 'words', 'talk']),
 ('preschool', 'Preschool Teacher', '25-2011.00', 'edu', '🧸', 'Helps 3- and 4-year-olds learn through play, songs and stories.', 'A certificate or two-year degree; some states require a bachelor\'s.', 'Babysit or help in a children\'s program.', ['care', 'art']),
 ('counselor', 'School Counselor', '21-1012.00', 'edu', '🧭', 'Helps students with school, friendships and planning their future.', 'A master\'s degree in counseling.', 'Be a peer mentor or buddy for a new student.', ['care', 'talk', 'calm']),
 ('librarian', 'Librarian', '25-4022.00', 'edu', '📚', 'Helps people find information, runs programs and chooses books and media.', 'A master\'s degree in library science.', 'Volunteer at your school or public library.', ['words', 'organize', 'tech']),
 ('coach', 'Coach', '27-2022.00', 'edu', '🏅', 'Trains athletes and teams, plans practices and makes game-day decisions.', 'Experience in the sport; many have a bachelor\'s degree.', 'Help coach a younger kids\' team.', ['active', 'lead', 'talk']),
 ('wind-tech', 'Wind Turbine Technician', '49-9081.00', 'energy', '🌬️', 'Climbs giant wind turbines to inspect and repair them.', 'A certificate or two-year degree.', 'Build a small wind turbine from a kit or cardboard.', ['build', 'active', 'science']),
 ('solar', 'Solar Panel Installer', '47-2231.00', 'energy', '☀️', 'Installs solar panels on roofs and in solar farms.', 'On-the-job training or a short certificate.', 'Track how much sun your house gets in a day.', ['build', 'active']),
 ('env-sci', 'Environmental Scientist', '19-2041.00', 'energy', '🌿', 'Studies air, water and soil to protect people and nature from pollution.', 'A bachelor\'s degree in a natural science.', 'Test the water in a local creek with a science kit.', ['science', 'numbers']),
 ('wildlife', 'Wildlife Biologist', '19-1023.00', 'energy', '🦉', 'Studies animals in the wild and how to protect them and their homes.', 'A bachelor\'s degree; many have a master\'s.', 'Keep a nature journal of birds or animals you see.', ['science', 'active']),
 ('lineworker', 'Power Line Worker', '49-9051.00', 'energy', '⚡', 'Builds and repairs the power lines that carry electricity, often after storms.', 'A certificate and a long paid apprenticeship.', 'Learn how electricity gets from a power plant to your outlet.', ['build', 'active', 'calm']),
 ('meteorologist', 'Meteorologist', '19-2021.00', 'energy', '🌦️', 'Studies the atmosphere to forecast weather and track storms.', 'A bachelor\'s degree in meteorology or atmospheric science.', 'Keep a weather log and make your own forecast.', ['science', 'numbers', 'tech']),
 ('accountant', 'Accountant', '13-2011.00', 'fin', '🧾', 'Tracks money for people and businesses, prepares taxes and checks that records are correct.', 'A bachelor\'s degree in accounting.', 'Keep a budget for your allowance or a club.', ['numbers', 'organize']),
 ('fin-advisor', 'Financial Advisor', '13-2052.00', 'fin', '💰', 'Helps people plan how to save, invest and reach goals like college or retirement.', 'A bachelor\'s degree and licenses.', 'Try a stock market simulation game.', ['numbers', 'talk']),
 ('actuary', 'Actuary', '15-2011.00', 'fin', '🎲', 'Uses math and statistics to measure risk for insurance companies.', 'A bachelor\'s degree and a series of exams.', 'Run a probability experiment with dice and chart the results.', ['numbers', 'tech']),
 ('nurse', 'Registered Nurse', '29-1141.00', 'health', '🩺', 'Cares for patients, gives medicine, watches for changes and teaches families.', 'A two-year or four-year nursing degree and a license.', 'Take a first-aid or babysitting safety class.', ['care', 'science', 'calm']),
 ('doctor', 'Family Doctor', '29-1215.00', 'health', '🧑‍⚕️', 'Diagnoses and treats illness and helps people of all ages stay healthy.', 'A bachelor\'s degree, four years of medical school and three or more years of residency.', 'Join a science club or health careers program.', ['science', 'care']),
 ('pa', 'Physician Assistant', '29-1071.00', 'health', '💉', 'Examines patients, diagnoses illnesses and prescribes treatment as part of a doctor-led team.', 'A bachelor\'s degree, then a two-year master\'s program.', 'Learn how the body works with a model or app.', ['science', 'care']),
 ('pt', 'Physical Therapist', '29-1123.00', 'health', '🦵', 'Helps people recover from injuries and move better through exercise.', 'A doctor of physical therapy degree (about three years after college).', 'Learn the muscles you use in your favorite sport.', ['care', 'active', 'science']),
 ('hygienist', 'Dental Hygienist', '29-1292.00', 'health', '🦷', 'Cleans teeth, takes X-rays and teaches people how to keep their mouths healthy.', 'A two-year degree and a license.', 'Find out why fluoride protects teeth.', ['care', 'science']),
 ('paramedic', 'Paramedic', '29-2043.00', 'health', '🚑', 'Rushes to emergencies and gives life-saving care on the way to the hospital.', 'EMT training, then a paramedic certificate or degree.', 'Learn CPR and first aid.', ['calm', 'care', 'active']),
 ('pharmacist', 'Pharmacist', '29-1051.00', 'health', '💊', 'Prepares medicines and makes sure people take them safely.', 'A doctor of pharmacy degree (about six years after high school).', 'Find out how medicines are tested before they are sold.', ['science', 'organize', 'care']),
 ('social-worker', 'Social Worker', '21-1021.00', 'health', '🤝', 'Helps children and families get through hard times and find support.', 'A bachelor\'s or master\'s degree in social work.', 'Volunteer with a food bank or community group.', ['care', 'talk', 'calm']),
 ('psychologist', 'Psychologist', '19-3033.00', 'health', '🧠', 'Helps people understand their thoughts and feelings and studies how the mind works.', 'A master\'s or doctoral degree in psychology (clinical psychologists need a doctorate).', 'Read about how memory works and test it on yourself.', ['care', 'science', 'talk']),
 ('med-assist', 'Medical Assistant', '31-9092.00', 'health', '🏥', 'Checks patients in, takes vital signs and helps doctors with exams.', 'A certificate program (about a year).', 'Learn to take a pulse and blood pressure.', ['care', 'organize']),
 ('athletic-trainer', 'Athletic Trainer', '29-9091.00', 'health', '🏈', 'Prevents and treats sports injuries for athletes.', 'A master\'s degree in athletic training and a license.', 'Ask your school\'s athletic trainer about their job.', ['active', 'care', 'science']),
 ('chef', 'Chef', '35-1011.00', 'hosp', '🧑‍🍳', 'Creates menus, cooks and runs a restaurant kitchen.', 'Experience in kitchens; some go to culinary school.', 'Cook dinner for your family once a week.', ['art', 'lead', 'active']),
 ('cook', 'Restaurant Cook', '35-2014.00', 'hosp', '🍳', 'Prepares meals quickly and carefully during busy restaurant shifts.', 'On-the-job training.', 'Learn five recipes you can cook on your own.', ['active', 'calm']),
 ('event-planner', 'Event Planner', '13-1121.00', 'hosp', '🎉', 'Plans weddings, concerts, conferences and festivals so everything goes right.', 'A bachelor\'s degree or experience.', 'Plan a class party or school event.', ['organize', 'talk', 'lead']),
 ('hotel-mgr', 'Hotel Manager', '11-9081.00', 'hosp', '🏨', 'Runs a hotel: guests, staff, budgets and solving problems.', 'Experience in hotels; many have a hospitality degree.', 'Plan a pretend weekend trip and compare three places to stay online.', ['lead', 'talk', 'organize']),
 ('flight-attendant', 'Flight Attendant', '53-2031.00', 'hosp', '✈️', 'Keeps passengers safe and comfortable on flights.', 'High school and airline training.', 'Learn some phrases in another language.', ['talk', 'calm', 'care']),
 ('stylist', 'Hairstylist', '39-5012.00', 'health', '✂️', 'Cuts, colors and styles hair and helps clients look their best.', 'Cosmetology school (about a year) and a license.', 'Practice braids or styles with family or friends.', ['art', 'talk']),
 ('ops-mgr', 'Business Manager', '11-1021.00', 'mgmt', '📋', 'Runs the day-to-day work of a company: people, budgets and goals.', 'A bachelor\'s degree and work experience.', 'Run a small business like a lemonade or craft stand.', ['lead', 'organize', 'talk']),
 ('hr', 'Human Resources Specialist', '13-1071.00', 'mgmt', '🧑‍💼', 'Hires new workers, helps employees and makes workplaces fair.', 'A bachelor\'s degree.', 'Interview an adult about how they got hired.', ['talk', 'organize']),
 ('project-mgr', 'Project Manager', '13-1082.00', 'mgmt', '🗂️', 'Plans big projects, sets deadlines and keeps a team on track.', 'A bachelor\'s degree and experience; certifications help.', 'Plan a group project with a timeline and roles.', ['organize', 'lead']),
 ('marketing-mgr', 'Marketing Manager', '11-2021.00', 'mkt', '📣', 'Plans how to get people excited about a product, brand or cause.', 'A bachelor\'s degree and experience in marketing.', 'Create an ad campaign for a school event.', ['talk', 'art', 'lead']),
 ('realtor', 'Real Estate Agent', '41-9022.00', 'fin', '🏡', 'Helps people buy and sell homes.', 'A pre-licensing course and a state license.', 'Compare three homes for sale online and pick the best value.', ['talk', 'numbers']),
 ('pr', 'Public Relations Specialist', '27-3031.00', 'mkt', '🎙️', 'Shapes how the public sees a company, team or person: press releases, events and social media.', 'A bachelor\'s degree in communications or journalism.', 'Write a news release about something great at your school.', ['words', 'talk']),
 ('market-research', 'Market Research Analyst', '13-1161.00', 'mkt', '🔎', 'Studies what people want to buy and why, using surveys and data.', 'A bachelor\'s degree.', 'Survey classmates about a snack and present the results.', ['numbers', 'tech', 'words']),
 ('firefighter', 'Firefighter', '33-2011.00', 'public', '🚒', 'Puts out fires, rescues people and answers medical emergencies.', 'Fire academy training and EMT certification.', 'Learn fire safety and visit a fire station open house.', ['active', 'calm', 'care']),
 ('police', 'Police Officer', '33-3051.00', 'public', '🚓', 'Protects people, responds to emergencies and enforces laws.', 'Police academy training; some departments require college.', 'Join a youth explorer program.', ['calm', 'talk', 'active']),
 ('lawyer', 'Lawyer', '23-1011.00', 'public', '⚖️', 'Advises people and argues cases in court.', 'A bachelor\'s degree, three years of law school and a bar exam.', 'Join debate or mock trial.', ['words', 'talk']),
 ('paralegal', 'Paralegal', '23-2011.00', 'public', '📁', 'Helps lawyers research laws, organize evidence and prepare documents.', 'A two-year degree or certificate.', 'Research how a law in your state was made.', ['words', 'organize']),
 ('planner', 'Urban Planner', '19-3051.00', 'public', '🏙️', 'Plans how towns grow: parks, housing, transit and roads.', 'A master\'s degree in planning.', 'Design a better park or street for your neighborhood.', ['art', 'science', 'talk']),
 ('dispatcher', '911 Dispatcher', '43-5031.00', 'public', '📞', 'Answers emergency calls and sends police, fire and ambulances.', 'On-the-job training and certification.', 'Learn what to say when you call 911.', ['calm', 'talk', 'organize']),
 ('forensic', 'Forensic Science Technician', '19-4092.00', 'public', '🔬', 'Collects and tests evidence from crime scenes.', 'A bachelor\'s degree in a natural science.', 'Try fingerprinting or chromatography with a science kit.', ['science', 'organize']),
 ('pilot', 'Airline Pilot', '53-2011.00', 'trans', '🛫', 'Flies passengers and cargo safely around the world.', 'A bachelor\'s degree, flight training, FAA licenses and about 1,500 hours of flying.', 'Try a flight simulator or visit an airport.', ['calm', 'tech', 'numbers']),
 ('trucker', 'Truck Driver', '53-3032.00', 'trans', '🚚', 'Drives big trucks to deliver goods across the country.', 'A commercial driver\'s license (a few weeks of training).', 'Plan a road trip route on a map.', ['calm', 'organize']),
 ('logistician', 'Logistician', '13-1081.00', 'trans', '📦', 'Plans how products get from factories to stores and doorsteps on time.', 'A bachelor\'s degree.', 'Track a package and map the route it took.', ['organize', 'numbers']),
 ('auto-tech', 'Auto Technician', '49-3023.00', 'trans', '🚗', 'Diagnoses and repairs cars, including electric vehicles.', 'A certificate or two-year program.', 'Learn to check a car\'s oil and tire pressure.', ['build', 'tech']),
 ('aircraft-mech', 'Aircraft Mechanic', '49-3011.00', 'trans', '🛩️', 'Inspects and repairs airplanes so they are safe to fly.', 'An 18-to-24-month FAA-approved school and a license.', 'Build a model airplane and learn what each part does.', ['build', 'science']),
 ('atc', 'Air Traffic Controller', '53-2021.00', 'trans', '📡', 'Guides airplanes safely through the sky and on runways.', 'An associate\'s or bachelor\'s degree from an FAA-approved program (or work experience), then FAA Academy training; most must apply before age 31.', 'Watch a live flight-tracking map.', ['calm', 'organize', 'numbers']),
 ('aerospace', 'Aerospace Engineer', '17-2011.00', 'trans', '🚀', 'Designs airplanes, rockets and satellites.', 'A bachelor\'s degree in aerospace engineering.', 'Build and launch a bottle rocket.', ['science', 'numbers', 'build']),
]


# Ten more Handbook careers, added for career-cluster-explorer so each cluster's "Ways in" ladder has a career at more
# levels of training (refine round 1, 2026-10-28). They are written only with --more, so career-match-quiz's data keeps
# its 83 until that tool chooses to take them. O*NET OnLine shows interests on a 0-100 scale; ONET_MORE stores them
# back on the 1-7 scale of Interests.txt (1 + score * 6 / 100). Their Job Zones and work context are not stored.
C_MORE = [
 ('admin-asst', 'Administrative Assistant', '43-6014.00', 'mgmt', '📎', 'Keeps an office running: schedules, files, phone calls and helping visitors.', 'High school, then training on the job; some take office or computer courses.', 'Organize a family calendar for one month.', ['organize', 'talk']),
 ('retail', 'Retail Sales Worker', '41-2031.00', 'mkt', '🛍️', 'Helps customers find what they need, answers questions and rings up sales in a store.', 'Training on the job; no diploma is needed to start.', 'Describe your favorite product in three sentences that would make a friend want it.', ['talk', 'organize']),
 ('cs-research', 'Computer Research Scientist', '15-1221.00', 'digital', '🧮', 'Invents new ways to use computers, like smarter AI and faster, safer software.', 'A master\'s degree in computer science; some go on to a doctorate.', 'Try a free coding or AI lesson online.', ['science', 'tech', 'numbers']),
 ('childcare', 'Childcare Worker', '39-9011.00', 'edu', '🧩', 'Cares for young children, plans play and learning, and keeps them safe.', 'High school; many states also ask for childcare training or a certificate.', 'Help a younger cousin or neighbor learn a game, with a grown-up nearby.', ['care', 'active']),
 ('teacher-asst', 'Teacher Assistant', '25-9042.00', 'edu', '✏️', 'Works beside a teacher, helping students one on one or in small groups.', 'Some college, or passing a test of reading, writing and math skills.', 'Help a younger student practice reading.', ['care', 'talk']),
 ('home-aide', 'Home Health Aide', '31-1121.00', 'health', '🏠', 'Helps older adults and people with disabilities with daily care in their homes.', 'High school; many agencies require a short training course and a test.', 'Help an older neighbor or relative with a chore.', ['care', 'calm']),
 ('bookkeeper', 'Bookkeeper', '43-3031.00', 'fin', '📒', 'Keeps track of the money a business earns and spends.', 'Some college courses in accounting; many learn the rest on the job.', 'Track your own spending or savings for a month in a table.', ['numbers', 'organize']),
 ('mover', 'Warehouse Worker', '53-7062.00', 'trans', '🏷️', 'Moves, packs and loads goods in a warehouse so orders ship on time.', 'Training on the job; some also earn a forklift certificate.', 'Pack a box so nothing inside can move, then label it.', ['active', 'build']),
 ('drafter', 'Drafter', '17-3011.00', 'build', '📏', 'Turns architects\' and engineers\' ideas into detailed drawings on a computer.', 'A two-year degree in drafting or computer-aided design (CAD).', 'Draw a floor plan of your room to scale on graph paper.', ['build', 'tech', 'organize']),
 ('env-tech', 'Environmental Technician', '19-4042.00', 'energy', '💧', 'Tests air, water and soil for pollution and helps keep them clean.', 'A two-year degree in science or an environmental program.', 'Test water from two places with a pool or aquarium test kit and compare.', ['science', 'active']),
]
# O*NET OnLine "Career Interest Types", read 2026-10-28, in R I A S E C order (0-100 scale)
ONET_MORE = {
 '43-6014.00': [16, 6, 0, 44, 53, 99], '41-2031.00': [37, 0, 16, 33, 86, 70], '15-1221.00': [46, 100, 33, 17, 25, 63],
 '39-9011.00': [35, 8, 43, 86, 29, 41], '25-9042.00': [26, 22, 30, 92, 33, 54], '31-1121.00': [54, 36, 8, 89, 13, 42],
 '43-3031.00': [11, 20, 0, 8, 31, 100], '53-7062.00': [84, 2, 0, 8, 17, 66], '17-3011.00': [76, 54, 58, 9, 9, 65],
 '19-4042.00': [81, 77, 4, 16, 6, 66],
}

# BLS Occupational Outlook Handbook, 2025-35 edition, each read on its live page (bls.gov blocks scripts, so these
# were copied by hand from each page's Quick Facts). id: (page, page title, typical entry-level education, job outlook,
# number of jobs 2025, the page's median pay 2025 (yearly, or hourly where the page gives only hourly)).
# Where the Handbook says "See How to Become One", EDU_NOTE quotes its sentence and gives the ladder level.
HB = 'https://www.bls.gov/ooh/'
HANDBOOK = {
 'graphic-design': ('arts-and-design/graphic-designers.htm', 'Graphic Designers', "Bachelor's degree", '-2% (Decline)', 253100, 62960),
 'welder': ('production/welders-cutters-solderers-and-brazers.htm', 'Welders, Cutters, Solderers, and Brazers', 'High school diploma or equivalent', '2% (Slower than average)', 437700, 53750),
 'machinist': ('production/machinists-and-tool-and-die-makers.htm', 'Machinists and Tool and Die Makers', 'See How to Become One', '-1% (Decline)', 344900, 59620),
 'ind-eng': ('architecture-and-engineering/industrial-engineers.htm', 'Industrial Engineers', "Bachelor's degree", '12% (Much faster than average)', 365100, 102440),
 'robotics-tech': ('architecture-and-engineering/electro-mechanical-technicians.htm', 'Electro-mechanical and Mechatronics Technologists and Technicians', "Associate's degree", '3% (As fast as average)', 15700, 73900),
 'vet': ('healthcare/veterinarians.htm', 'Veterinarians', 'Doctoral or professional degree', '9% (Much faster than average)', 91100, 130100),
 'vet-tech': ('healthcare/veterinary-technologists-and-technicians.htm', 'Veterinary Technologists and Technicians', "Associate's degree", '9% (Much faster than average)', 131400, 47380),
 'food-sci': ('life-physical-and-social-science/agricultural-and-food-scientists.htm', 'Agricultural and Food Scientists', "Bachelor's degree", '6% (Faster than average)', 37400, 81970),
 'farmer': ('management/farmers-ranchers-and-other-agricultural-managers.htm', 'Farmers, Ranchers, and Other Agricultural Managers', 'High school diploma or equivalent', '-3% (Decline)', 788700, 89900),
 'animator': ('arts-and-design/multimedia-artists-and-animators.htm', 'Special Effects Artists and Animators', "Bachelor's degree", '0% (Little or no change)', 51900, 102030),
 'musician': ('entertainment-and-sports/musicians-and-singers.htm', 'Musicians and Singers', 'No formal educational credential', '0% (Little or no change)', 170400, 47.80),
 'photographer': ('media-and-communication/photographers.htm', 'Photographers', 'High school diploma or equivalent', '-1% (Decline)', 145000, 44660),
 'fashion': ('arts-and-design/fashion-designers.htm', 'Fashion Designers', "Bachelor's degree", '0% (Little or no change)', 32700, 80960),
 'web-dev': ('computer-and-information-technology/web-developers.htm', 'Web Developers and Digital Designers', "Bachelor's degree", '5% (Faster than average)', 220100, 99520),
 'game-design': ('computer-and-information-technology/web-developers.htm', 'Web Developers and Digital Designers', "Bachelor's degree", '5% (Faster than average)', 220100, 99520),
 'film-editor': ('media-and-communication/film-and-video-editors-and-camera-operators.htm', 'Film and Video Editors and Camera Operators', "Bachelor's degree", '3% (As fast as average)', 72000, 75100),
 'interior': ('arts-and-design/interior-designers.htm', 'Interior Designers', "Bachelor's degree", '3% (As fast as average)', 97100, 67190),
 'writer': ('media-and-communication/writers-and-authors.htm', 'Writers and Authors', "Bachelor's degree", '0% (Little or no change)', 140300, 76910),
 'actor': ('entertainment-and-sports/actors.htm', 'Actors', 'Some college, no degree', '0% (Little or no change)', 67500, 29.05),
 'director': ('entertainment-and-sports/producers-and-directors.htm', 'Producers and Directors', "Bachelor's degree", '4% (As fast as average)', 181000, 90360),
 'electrician': ('construction-and-extraction/electricians.htm', 'Electricians', 'High school diploma or equivalent', '9% (Much faster than average)', 821000, 63190),
 'carpenter': ('construction-and-extraction/carpenters.htm', 'Carpenters', 'High school diploma or equivalent', '4% (As fast as average)', 889700, 60580),
 'plumber': ('construction-and-extraction/plumbers-pipefitters-and-steamfitters.htm', 'Plumbers, Pipefitters, and Steamfitters', 'High school diploma or equivalent', '7% (Much faster than average)', 510600, 63800),
 'architect': ('architecture-and-engineering/architects.htm', 'Architects', "Bachelor's degree", '4% (As fast as average)', 124600, 99280),
 'civil-eng': ('architecture-and-engineering/civil-engineers.htm', 'Civil Engineers', "Bachelor's degree", '6% (Faster than average)', 380600, 100840),
 'hvac': ('installation-maintenance-and-repair/heating-air-conditioning-and-refrigeration-mechanics-and-installers.htm', 'Heating, Air Conditioning, and Refrigeration Mechanics and Installers', 'Postsecondary nondegree award', '11% (Much faster than average)', 440900, 61010),
 'equip-op': ('construction-and-extraction/construction-equipment-operators.htm', 'Construction Equipment Operators', 'High school diploma or equivalent', '4% (As fast as average)', 534100, 59600),
 'software-dev': ('computer-and-information-technology/software-developers.htm', 'Software Developers, Quality Assurance Analysts, and Testers', "Bachelor's degree", '10% (Much faster than average)', 1905400, 134040),
 'cyber': ('computer-and-information-technology/information-security-analysts.htm', 'Information Security Analysts', "Bachelor's degree", '21% (Much faster than average)', 192900, 129180),
 'data-sci': ('math/data-scientists.htm', 'Data Scientists', "Bachelor's degree", '35% (Much faster than average)', 275600, 120230),
 'it-support': ('computer-and-information-technology/computer-support-specialists.htm', 'Computer Support Specialists', 'See How to Become One', '-3% (Decline)', 903100, 62890),
 'teacher': ('education-training-and-library/kindergarten-and-elementary-school-teachers.htm', 'Kindergarten and Elementary School Teachers', "Bachelor's degree", '0% (Little or no change)', 1530500, 63820),
 'preschool': ('education-training-and-library/preschool-teachers.htm', 'Preschool Teachers', "Associate's degree", '4% (As fast as average)', 583200, 38140),
 'counselor': ('community-and-social-service/school-and-career-counselors.htm', 'School and Career Counselors and Advisors', "Master's degree", '3% (As fast as average)', 389500, 64330),
 'librarian': ('education-training-and-library/librarians.htm', 'Librarians and Library Media Specialists', "Master's degree", '3% (As fast as average)', 142300, 68270),
 'coach': ('entertainment-and-sports/coaches-and-scouts.htm', 'Coaches and Scouts', "Bachelor's degree", '6% (Faster than average)', 298800, 47320),
 'wind-tech': ('installation-maintenance-and-repair/wind-turbine-technicians.htm', 'Wind Turbine Technicians', 'Postsecondary nondegree award', '30% (Much faster than average)', 11800, 64120),
 'solar': ('construction-and-extraction/solar-photovoltaic-installers.htm', 'Solar Photovoltaic Installers', 'High school diploma or equivalent', '37% (Much faster than average)', 31100, 53140),
 'env-sci': ('life-physical-and-social-science/environmental-scientists-and-specialists.htm', 'Environmental Scientists and Specialists', "Bachelor's degree", '6% (Faster than average)', 93400, 82220),
 'wildlife': ('life-physical-and-social-science/zoologists-and-wildlife-biologists.htm', 'Zoologists and Wildlife Biologists', "Bachelor's degree", '4% (As fast as average)', 19500, 76780),
 'lineworker': ('installation-maintenance-and-repair/line-installers-and-repairers.htm', 'Electrical Power-Line Installers and Repairers', 'High school diploma or equivalent', '10% (Much faster than average)', 131900, 95320),
 'meteorologist': ('life-physical-and-social-science/atmospheric-scientists-including-meteorologists.htm', 'Atmospheric Scientists, Including Meteorologists', "Bachelor's degree", '3% (As fast as average)', 10700, 99070),
 'accountant': ('business-and-financial/accountants-and-auditors.htm', 'Accountants and Auditors', "Bachelor's degree", '5% (Faster than average)', 1595200, 83680),
 'fin-advisor': ('business-and-financial/personal-financial-advisors.htm', 'Personal Financial Advisors', "Bachelor's degree", '1% (Slower than average)', 299400, 105070),
 'actuary': ('math/actuaries.htm', 'Actuaries', "Bachelor's degree", '9% (Much faster than average)', 31200, 130000),
 'nurse': ('healthcare/registered-nurses.htm', 'Registered Nurses', "Bachelor's degree", '6% (Faster than average)', 3465400, 97550),
 'doctor': ('healthcare/physicians-and-surgeons.htm', 'Physicians and Surgeons', 'Doctoral or professional degree', '4% (As fast as average)', 862800, 275930),
 'pa': ('healthcare/physician-assistants.htm', 'Physician Assistants', "Master's degree", '21% (Much faster than average)', 168900, 135880),
 'pt': ('healthcare/physical-therapists.htm', 'Physical Therapists', 'Doctoral or professional degree', '12% (Much faster than average)', 283700, 102760),
 'hygienist': ('healthcare/dental-hygienists.htm', 'Dental Hygienists', "Associate's degree", '8% (Much faster than average)', 225300, 98100),
 'paramedic': ('healthcare/emts-and-paramedics.htm', 'EMTs and Paramedics', 'Postsecondary nondegree award', '6% (Faster than average)', 284100, 48150),
 'pharmacist': ('healthcare/pharmacists.htm', 'Pharmacists', 'Doctoral or professional degree', '5% (Faster than average)', 325200, 140910),
 'social-worker': ('community-and-social-service/social-workers.htm', 'Social Workers', 'See How to Become One', '6% (Faster than average)', 816100, 61780),
 'psychologist': ('life-physical-and-social-science/psychologists.htm', 'Psychologists', 'See How to Become One', '6% (Faster than average)', 209400, 99110),
 'med-assist': ('healthcare/medical-assistants.htm', 'Medical Assistants', 'Postsecondary nondegree award', '13% (Much faster than average)', 833900, 45690),
 'athletic-trainer': ('healthcare/athletic-trainers.htm', 'Athletic Trainers', "Master's degree", '13% (Much faster than average)', 35200, 62520),
 'chef': ('food-preparation-and-serving/chefs-and-head-cooks.htm', 'Chefs and Head Cooks', 'High school diploma or equivalent', '7% (Much faster than average)', 220300, 62470),
 'cook': ('food-preparation-and-serving/cooks.htm', 'Cooks', 'See How to Become One', '7% (Much faster than average)', 2705800, 36640),
 'event-planner': ('business-and-financial/meeting-convention-and-event-planners.htm', 'Meeting, Convention, and Event Planners', "Bachelor's degree", '6% (Faster than average)', 172100, 61160),
 'hotel-mgr': ('management/lodging-managers.htm', 'Lodging Managers', 'High school diploma or equivalent', '4% (As fast as average)', 54800, 69250),
 'flight-attendant': ('transportation-and-material-moving/flight-attendants.htm', 'Flight Attendants', 'High school diploma or equivalent', '9% (Much faster than average)', 133700, 63580),
 'stylist': ('personal-care-and-service/barbers-hairstylists-and-cosmetologists.htm', 'Barbers, Hairstylists, and Cosmetologists', 'Postsecondary nondegree award', '7% (Much faster than average)', 670800, 35880),
 'ops-mgr': ('management/top-executives.htm', 'Top Executives', "Bachelor's degree", '5% (Faster than average)', 3890600, 108780),
 'hr': ('business-and-financial/human-resources-specialists.htm', 'Human Resources Specialists', "Bachelor's degree", '6% (Faster than average)', 939700, 75940),
 'project-mgr': ('business-and-financial/project-management-specialists.htm', 'Project Management Specialists', "Bachelor's degree", '7% (Much faster than average)', 1094300, 102320),
 'marketing-mgr': ('management/advertising-promotions-and-marketing-managers.htm', 'Advertising, Promotions, and Marketing Managers', "Bachelor's degree", '6% (Faster than average)', 454800, 165780),
 'realtor': ('sales/real-estate-brokers-and-sales-agents.htm', 'Real Estate Brokers and Sales Agents', 'High school diploma or equivalent', '2% (Slower than average)', 530600, 57400),
 'pr': ('media-and-communication/public-relations-specialists.htm', 'Public Relations Specialists', "Bachelor's degree", '2% (Slower than average)', 314500, 74750),
 'market-research': ('business-and-financial/market-research-analysts.htm', 'Market Research Analysts', "Bachelor's degree", '7% (Much faster than average)', 952700, 78760),
 'firefighter': ('protective-service/firefighters.htm', 'Firefighters', 'Postsecondary nondegree award', '4% (As fast as average)', 355300, 59280),
 'police': ('protective-service/police-and-detectives.htm', 'Police and Detectives', 'See How to Become One', '3% (As fast as average)', 824200, 77310),
 'lawyer': ('legal/lawyers.htm', 'Lawyers', 'Doctoral or professional degree', '5% (Faster than average)', 863700, 159670),
 'paralegal': ('legal/paralegals-and-legal-assistants.htm', 'Paralegals and Legal Assistants', "Associate's degree", '0% (Little or no change)', 404900, 62890),
 'planner': ('life-physical-and-social-science/urban-and-regional-planners.htm', 'Urban and Regional Planners', "Master's degree", '4% (As fast as average)', 45800, 89320),
 'dispatcher': ('office-and-administrative-support/police-fire-and-ambulance-dispatchers.htm', 'Public Safety Telecommunicators', 'High school diploma or equivalent', '4% (As fast as average)', 105600, 53040),
 'forensic': ('life-physical-and-social-science/forensic-science-technicians.htm', 'Forensic Science Technicians', "Bachelor's degree", '13% (Much faster than average)', 20100, 72060),
 'pilot': ('transportation-and-material-moving/airline-and-commercial-pilots.htm', 'Airline and Commercial Pilots', 'See How to Become One', '7% (Much faster than average)', 154900, 210020),
 'trucker': ('transportation-and-material-moving/heavy-and-tractor-trailer-truck-drivers.htm', 'Heavy and Tractor-Trailer Truck Drivers', 'Postsecondary nondegree award', '4% (As fast as average)', 2221200, 58640),
 'logistician': ('business-and-financial/logisticians.htm', 'Logisticians', "Bachelor's degree", '18% (Much faster than average)', 255100, 82320),
 'auto-tech': ('installation-maintenance-and-repair/automotive-service-technicians-and-mechanics.htm', 'Automotive Service Technicians and Mechanics', 'Postsecondary nondegree award', '5% (Faster than average)', 825800, 50620),
 'aircraft-mech': ('installation-maintenance-and-repair/aircraft-and-avionics-equipment-mechanics-and-technicians.htm', 'Aircraft and Avionics Equipment Mechanics and Technicians', 'Postsecondary nondegree award', '6% (Faster than average)', 159800, 80180),
 'atc': ('transportation-and-material-moving/air-traffic-controllers.htm', 'Air Traffic Controllers', "Associate's degree", '2% (Slower than average)', 24000, 148080),
 'aerospace': ('architecture-and-engineering/aerospace-engineers.htm', 'Aerospace Engineers', "Bachelor's degree", '8% (Much faster than average)', 68700, 134960),
 'admin-asst': ('office-and-administrative-support/secretaries-and-administrative-assistants.htm', 'Secretaries and Administrative Assistants', 'High school diploma or equivalent', '-2% (Decline)', 3515600, 48310),
 'retail': ('sales/retail-sales-workers.htm', 'Retail Sales Workers', 'No formal educational credential', '0% (Little or no change)', 4271400, 35560),
 'cs-research': ('computer-and-information-technology/computer-and-information-research-scientists.htm', 'Computer and Information Research Scientists', "Master's degree", '22% (Much faster than average)', 38600, 140300),
 'childcare': ('personal-care-and-service/childcare-workers.htm', 'Childcare Workers', 'High school diploma or equivalent', '-2% (Decline)', 1010300, 34980),
 'teacher-asst': ('education-training-and-library/teacher-assistants.htm', 'Teacher Assistants', 'Some college, no degree', '0% (Little or no change)', 1463000, 36780),
 'home-aide': ('healthcare/home-health-aides-and-personal-care-aides.htm', 'Home Health and Personal Care Aides', 'High school diploma or equivalent', '18% (Much faster than average)', 4677100, 35800),
 'bookkeeper': ('office-and-administrative-support/bookkeeping-accounting-and-auditing-clerks.htm', 'Bookkeeping, Accounting, and Auditing Clerks', 'Some college, no degree', '-6% (Decline)', 1532400, 50670),
 'mover': ('transportation-and-material-moving/hand-laborers-and-material-movers.htm', 'Hand Laborers and Material Movers', 'No formal educational credential', '4% (As fast as average)', 6917800, 38220),
 'drafter': ('architecture-and-engineering/drafters.htm', 'Drafters', "Associate's degree", '1% (Slower than average)', 180200, 68090),
 'env-tech': ('life-physical-and-social-science/environmental-science-and-protection-technicians.htm', 'Environmental Science and Protection Technicians', "Associate's degree", '7% (Much faster than average)', 36400, 55090),
}
EDU_NOTE = {
 'machinist': ('Machinists typically need a high school diploma or equivalent', 0),
 'it-support': ('user support specialists typically need to complete some college courses', 1),
 'social-worker': ("A bachelor's degree in social work (BSW) is the most common requirement for entry-level nonclinical social worker positions.", 3),
 'psychologist': ("Psychologists typically need at least a master's degree to enter the occupation.", 4),
 'cook': ('Most cooks learn their skills through on-the-job training and work-related experience.', 0),
 'police': ('Police and detective applicants must have at least a high school diploma or equivalent', 0),
 'pilot': ("Airline pilots typically need a bachelor's degree and experience as a commercial or military pilot.", 3),
}


def tab(name):
    return list(csv.DictReader(open(os.path.join(ONET, name), encoding='utf-8'), delimiter='\t'))

interest, zone, ctx = {}, {}, {}
if os.path.exists(os.path.join(ONET, 'Interests.txt')):
    for r in tab('Interests.txt'):
        if r['Scale ID'] == 'OI':
            interest.setdefault(r['O*NET-SOC Code'], {})[r['Element Name'][0]] = float(r['Data Value'])
    for r in tab('Job_Zones.txt'):
        zone[r['O*NET-SOC Code']] = int(r['Job Zone'])
    WANT = {'Outdoors, Exposed to All Weather Conditions': 'outdoors',
            'Deal With External Customers or the Public in General': 'people',
            'Spend Time Using Your Hands to Handle, Control, or Feel Objects, Tools, or Controls': 'hands',
            'Importance of Repeating Same Tasks': 'routine',
            'Work With or Contribute to a Work Group or Team': 'team'}
    # O*NET has no work context for these three; borrow a close relative
    CTX_FROM = {'15-2051.00': '15-2041.00', '29-2043.00': '33-2011.00', '13-1082.00': '13-1111.00'}
    for r in tab('Work_Context.txt'):
        if r['Scale ID'] == 'CX' and r['Element Name'] in WANT:
            ctx.setdefault(r['O*NET-SOC Code'], {})[WANT[r['Element Name']]] = round((float(r['Data Value']) - 1) / 4, 2)
    for code, frm in CTX_FROM.items():
        if frm in ctx: ctx[code] = ctx[frm]
    onet_src = 'O*NET folder ' + ONET
else:
    base = OUT if os.path.exists(OUT) else QUIZ
    for c in json.load(open(base, encoding='utf-8'))['careers']:
        interest[c['onet']] = dict(zip('RIASEC', c['riasec']))
        zone[c['onet']] = c['zone']
        ctx[c['onet']] = c['ctx']
    onet_src = 'O*NET fields from ' + os.path.normpath(base)
for code, v in ONET_MORE.items():
    if code not in interest:
        interest[code] = {k: round(1 + x * 6 / 100, 2) for k, x in zip('RIASEC', v)}

LEVEL = {'No formal educational credential': 0, 'High school diploma or equivalent': 0, 'Postsecondary nondegree award': 1,
         'Some college, no degree': 1, "Associate's degree": 2, "Bachelor's degree": 3, "Master's degree": 4,
         'Doctoral or professional degree': 4}

careers = C + (C_MORE if MORE else [])
# OEWS publishes these two only as combined groups (SOC 2018 aggregates): Teaching Assistants, Except Postsecondary and
# Home Health and Personal Care Aides, the same groups as their Handbook pages
OEWS_SOC = {'25-9042.00': '25-9045', '31-1121.00': '31-1120'}
pay_soc = lambda code: OEWS_SOC.get(code, code)
series = []
for c in careers:
    series += [oews(pay_soc(c[2]), t) for t in ('13', '08', '01')]
bls = fetch(series)

out, year = [], None
for cid, name, code, cl, emoji, does, path, tryit, uses in careers:
    i = interest[code]
    pay = bls[oews(pay_soc(code), '13')]
    hourly = bls[oews(pay_soc(code), '08')]
    jobs = bls[oews(pay_soc(code), '01')]
    if pay: year = pay['year']
    c = {
        'id': cid, 'name': name, 'onet': code, 'cluster': cl, 'emoji': emoji, 'does': does, 'path': path, 'try': tryit, 'uses': uses,
        'riasec': [round(i[k], 2) for k in 'RIASEC'], 'zone': zone.get(code), 'ctx': ctx.get(code, {}),
        'pay': round(pay['value']) if pay else None, 'hourly': hourly['value'] if hourly else None,
        'jobs': round(jobs['value']) if jobs else None,
    }
    page, title, edu, outlook, hb_jobs, hb_pay = HANDBOOK[cid]
    c.update({'edu': edu, 'outlook': outlook, 'ooh': HB + page, 'oohTitle': title, 'oohJobs': hb_jobs})
    c['oohPay' if hb_pay >= 1000 else 'oohHourly'] = hb_pay
    if cid in EDU_NOTE:
        assert edu == 'See How to Become One', cid
        c['eduNote'], c['level'] = EDU_NOTE[cid]
    else:
        c['level'] = LEVEL[edu]
    out.append(c)
    if not pay: print('no annual pay:', name, 'hourly', hourly and hourly['value'])
    if len(c['ctx']) < 5: print('missing context:', name)

handbook = {'edition': '2025-35', 'name': 'Occupational Outlook Handbook', 'by': 'U.S. Bureau of Labor Statistics', 'url': HB}
json.dump({'year': year, 'clusters': CLUSTERS, 'handbook': handbook, 'careers': out}, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(len(out), 'careers, OEWS', year, ',', onet_src, '->', os.path.normpath(OUT))
