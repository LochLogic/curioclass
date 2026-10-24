"""Builds tools/career-match-quiz/careers.json.

Interest profiles (RIASEC), Job Zones and work context come from the O*NET 30.2 database (O*NET Resource
Center, CC BY 4.0). Pay and employment come from BLS Occupational Employment and Wage Statistics through the
public API (latest year, national). The short descriptions, paths and "try it" ideas are written for grades 6-8.

    python scripts/careers_data.py <folder with O*NET text files>
"""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from bls import oews, fetch

ONET = sys.argv[1] if len(sys.argv) > 1 else '.'
OUT = os.path.join(os.path.dirname(__file__), '..', 'tools', 'career-match-quiz', 'careers.json')

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
 ('musician', 'Musician', '27-2042.00', 'arts', '🎸', 'Plays, sings, writes and records music for concerts, recordings, churches, schools and games.', 'Years of practice; some study music in college.', 'Join band, choir or orchestra, or write your own song.', ['art']),
 ('photographer', 'Photographer', '27-4021.00', 'arts', '📷', 'Takes photos for news, weddings, sports, products and art.', 'Training on the job or in college, and a portfolio.', 'Do a photo challenge: one great photo a day for a week.', ['art', 'tech']),
 ('fashion', 'Fashion Designer', '27-1022.00', 'arts', '👗', 'Sketches and creates clothing, shoes and accessories.', 'A bachelor\'s degree in fashion design, or a portfolio.', 'Redesign an old T-shirt or sketch a clothing line.', ['art']),
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
 ('doctor', 'Family Doctor', '29-1215.00', 'health', '👩‍⚕️', 'Diagnoses and treats illness and helps people of all ages stay healthy.', 'A bachelor\'s degree, four years of medical school and three or more years of residency.', 'Join a science club or health careers program.', ['science', 'care']),
 ('pa', 'Physician Assistant', '29-1071.00', 'health', '💉', 'Examines patients, diagnoses illnesses and prescribes treatment as part of a doctor-led team.', 'A bachelor\'s degree, then a two-year master\'s program.', 'Learn how the body works with a model or app.', ['science', 'care']),
 ('pt', 'Physical Therapist', '29-1123.00', 'health', '🦵', 'Helps people recover from injuries and move better through exercise.', 'A doctor of physical therapy degree (about three years after college).', 'Learn the muscles you use in your favorite sport.', ['care', 'active', 'science']),
 ('hygienist', 'Dental Hygienist', '29-1292.00', 'health', '🦷', 'Cleans teeth, takes X-rays and teaches people how to keep their mouths healthy.', 'A two-year degree and a license.', 'Find out why fluoride protects teeth.', ['care', 'science']),
 ('paramedic', 'Paramedic', '29-2043.00', 'health', '🚑', 'Rushes to emergencies and gives life-saving care on the way to the hospital.', 'EMT training, then a paramedic certificate or degree.', 'Learn CPR and first aid.', ['calm', 'care', 'active']),
 ('pharmacist', 'Pharmacist', '29-1051.00', 'health', '💊', 'Prepares medicines and makes sure people take them safely.', 'A doctor of pharmacy degree (about six years after high school).', 'Find out how medicines are tested before they are sold.', ['science', 'organize', 'care']),
 ('social-worker', 'Social Worker', '21-1021.00', 'health', '🤝', 'Helps children and families get through hard times and find support.', 'A bachelor\'s or master\'s degree in social work.', 'Volunteer with a food bank or community group.', ['care', 'talk', 'calm']),
 ('psychologist', 'Psychologist', '19-3033.00', 'health', '🧠', 'Helps people understand their thoughts and feelings and studies how the mind works.', 'A doctoral degree in psychology.', 'Read about how memory works and test it on yourself.', ['care', 'science', 'talk']),
 ('med-assist', 'Medical Assistant', '31-9092.00', 'health', '🏥', 'Checks patients in, takes vital signs and helps doctors with exams.', 'A certificate program (about a year).', 'Learn to take a pulse and blood pressure.', ['care', 'organize']),
 ('athletic-trainer', 'Athletic Trainer', '29-9091.00', 'health', '🏈', 'Prevents and treats sports injuries for athletes.', 'A master\'s degree in athletic training and a license.', 'Ask your school\'s athletic trainer about their job.', ['active', 'care', 'science']),
 ('chef', 'Chef', '35-1011.00', 'hosp', '👨‍🍳', 'Creates menus, cooks and runs a restaurant kitchen.', 'Experience in kitchens; some go to culinary school.', 'Cook dinner for your family once a week.', ['art', 'lead', 'active']),
 ('cook', 'Restaurant Cook', '35-2014.00', 'hosp', '🍳', 'Prepares meals quickly and carefully during busy restaurant shifts.', 'On-the-job training.', 'Learn five recipes you can cook on your own.', ['active', 'calm']),
 ('event-planner', 'Event Planner', '13-1121.00', 'hosp', '🎉', 'Plans weddings, concerts, conferences and festivals so everything goes right.', 'A bachelor\'s degree or experience.', 'Plan a class party or school event.', ['organize', 'talk', 'lead']),
 ('hotel-mgr', 'Hotel Manager', '11-9081.00', 'hosp', '🏨', 'Runs a hotel: guests, staff, budgets and solving problems.', 'Experience in hotels; many have a hospitality degree.', 'Plan a family trip and compare places to stay.', ['lead', 'talk', 'organize']),
 ('flight-attendant', 'Flight Attendant', '53-2031.00', 'hosp', '✈️', 'Keeps passengers safe and comfortable on flights.', 'High school and airline training.', 'Learn some phrases in another language.', ['talk', 'calm', 'care']),
 ('stylist', 'Hairstylist', '39-5012.00', 'hosp', '💇', 'Cuts, colors and styles hair and helps clients look their best.', 'Cosmetology school (about a year) and a license.', 'Practice braids or styles with family or friends.', ['art', 'talk']),
 ('ops-mgr', 'Business Manager', '11-1021.00', 'mgmt', '📋', 'Runs the day-to-day work of a company: people, budgets and goals.', 'A bachelor\'s degree and work experience.', 'Run a small business like a lemonade or craft stand.', ['lead', 'organize', 'talk']),
 ('hr', 'Human Resources Specialist', '13-1071.00', 'mgmt', '🧑‍💼', 'Hires new workers, helps employees and makes workplaces fair.', 'A bachelor\'s degree.', 'Interview an adult about how they got hired.', ['talk', 'organize']),
 ('project-mgr', 'Project Manager', '13-1082.00', 'mgmt', '🗂️', 'Plans big projects, sets deadlines and keeps a team on track.', 'A bachelor\'s degree and experience; certifications help.', 'Plan a group project with a timeline and roles.', ['organize', 'lead']),
 ('marketing-mgr', 'Marketing Manager', '11-2021.00', 'mkt', '📣', 'Plans how to get people excited about a product, brand or cause.', 'A bachelor\'s degree and experience in marketing.', 'Create an ad campaign for a school event.', ['talk', 'art', 'lead']),
 ('realtor', 'Real Estate Agent', '41-9022.00', 'mkt', '🏡', 'Helps people buy and sell homes.', 'A pre-licensing course and a state license.', 'Compare three homes for sale online and pick the best value.', ['talk', 'numbers']),
 ('pr', 'Public Relations Specialist', '27-3031.00', 'mkt', '🎙️', 'Shapes how the public sees a company, team or person: press releases, events and social media.', 'A bachelor\'s degree in communications or journalism.', 'Write a news release about something great at your school.', ['words', 'talk']),
 ('market-research', 'Market Research Analyst', '13-1161.00', 'mkt', '🔎', 'Studies what people want to buy and why, using surveys and data.', 'A bachelor\'s degree.', 'Survey classmates about a snack and present the results.', ['numbers', 'tech', 'words']),
 ('firefighter', 'Firefighter', '33-2011.00', 'public', '🚒', 'Puts out fires, rescues people and answers medical emergencies.', 'Fire academy training and EMT certification.', 'Learn fire safety and visit a fire station open house.', ['active', 'calm', 'care']),
 ('police', 'Police Officer', '33-3051.00', 'public', '🚓', 'Protects people, responds to emergencies and enforces laws.', 'Police academy training; some departments require college.', 'Join a youth explorer program.', ['calm', 'talk', 'active']),
 ('lawyer', 'Lawyer', '23-1011.00', 'public', '⚖️', 'Advises people and argues cases in court.', 'A bachelor\'s degree, three years of law school and a bar exam.', 'Join debate or mock trial.', ['words', 'talk']),
 ('paralegal', 'Paralegal', '23-2011.00', 'public', '📁', 'Helps lawyers research laws, organize evidence and prepare documents.', 'A two-year degree or certificate.', 'Research how a law in your state was made.', ['words', 'organize']),
 ('planner', 'Urban Planner', '19-3051.00', 'public', '🏙️', 'Plans how towns grow: parks, housing, transit and roads.', 'A master\'s degree in planning.', 'Design a better park or street for your neighborhood.', ['art', 'science', 'talk']),
 ('dispatcher', '911 Dispatcher', '43-5031.00', 'public', '📞', 'Answers emergency calls and sends police, fire and ambulances.', 'On-the-job training and certification.', 'Learn what to say when you call 911.', ['calm', 'talk', 'organize']),
 ('forensic', 'Forensic Science Technician', '19-4092.00', 'public', '🔬', 'Collects and tests evidence from crime scenes.', 'A bachelor\'s degree in a natural science.', 'Try fingerprinting or chromatography with a science kit.', ['science', 'organize']),
 ('pilot', 'Airline Pilot', '53-2011.00', 'trans', '🛫', 'Flies passengers and cargo safely around the world.', 'Flight school, 1,500 flight hours and licenses; many airlines want a degree.', 'Try a flight simulator or visit an airport.', ['calm', 'tech', 'numbers']),
 ('trucker', 'Truck Driver', '53-3032.00', 'trans', '🚚', 'Drives big trucks to deliver goods across the country.', 'A commercial driver\'s license (a few weeks of training).', 'Plan a road trip route on a map.', ['calm', 'organize']),
 ('logistician', 'Logistician', '13-1081.00', 'trans', '📦', 'Plans how products get from factories to stores and doorsteps on time.', 'A bachelor\'s degree.', 'Track a package and map the route it took.', ['organize', 'numbers']),
 ('auto-tech', 'Auto Technician', '49-3023.00', 'trans', '🚗', 'Diagnoses and repairs cars, including electric vehicles.', 'A certificate or two-year program.', 'Learn to check a car\'s oil and tire pressure.', ['build', 'tech']),
 ('aircraft-mech', 'Aircraft Mechanic', '49-3011.00', 'trans', '🛩️', 'Inspects and repairs airplanes so they are safe to fly.', 'An 18-to-24-month FAA-approved school and a license.', 'Build a model airplane and learn what each part does.', ['build', 'science']),
 ('atc', 'Air Traffic Controller', '53-2021.00', 'trans', '📡', 'Guides airplanes safely through the sky and on runways.', 'FAA Academy training; most start before age 31.', 'Watch a live flight-tracking map.', ['calm', 'organize', 'numbers']),
 ('aerospace', 'Aerospace Engineer', '17-2011.00', 'trans', '🚀', 'Designs airplanes, rockets and satellites.', 'A bachelor\'s degree in aerospace engineering.', 'Build and launch a bottle rocket.', ['science', 'numbers', 'build']),
]

def tab(name):
    return list(csv.DictReader(open(os.path.join(ONET, name), encoding='utf-8'), delimiter='\t'))

interest, zone, ctx = {}, {}, {}
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

series = []
for c in C:
    series += [oews(c[2], '13'), oews(c[2], '08'), oews(c[2], '01')]
bls = fetch(series)

out, year = [], None
for cid, name, code, cl, emoji, does, path, tryit, uses in C:
    i = interest[code]
    pay = bls[oews(code, '13')]
    hourly = bls[oews(code, '08')]
    jobs = bls[oews(code, '01')]
    if pay: year = pay['year']
    out.append({
        'id': cid, 'name': name, 'onet': code, 'cluster': cl, 'emoji': emoji, 'does': does, 'path': path, 'try': tryit, 'uses': uses,
        'riasec': [round(i[k], 2) for k in 'RIASEC'], 'zone': zone[code], 'ctx': ctx.get(CTX_FROM.get(code, code), {}),
        'pay': round(pay['value']) if pay else None, 'hourly': hourly['value'] if hourly else None,
        'jobs': round(jobs['value']) if jobs else None,
    })
    if not pay: print('no annual pay:', name, 'hourly', hourly and hourly['value'])
    if len(ctx.get(CTX_FROM.get(code, code), {})) < 5: print('missing context:', name)

json.dump({'year': year, 'clusters': CLUSTERS, 'careers': out}, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(len(out), 'careers, OEWS', year, '->', OUT)
