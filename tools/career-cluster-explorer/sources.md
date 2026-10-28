# Sources: Handbook fields

Every `edu`, `outlook`, `ooh`, `oohTitle`, `oohJobs` and `oohPay` (or `oohHourly`) in `careers.json` was read from the
live profile page of the U.S. Bureau of Labor Statistics, Occupational Outlook Handbook, 2025-35 edition, on 2026-10-28
(Quick Facts: "Typical Entry-Level Education", "Job Outlook, 2025-35", "Number of Jobs, 2025" and "2025 Median Pay").
All 93 careers have a profile; none is "Not in the Handbook". Pages fetched with WebFetch (bls.gov refuses plain curl
with a 403). The polish round re-read all 83 original profiles: every edu and outlook still matched. The table lives in
`scripts/careers_data.py` (`HANDBOOK`), which writes this file:
`python scripts/careers_data.py --out tools/career-cluster-explorer/careers.json --more`.

- `pay` and `hourly` are the OEWS May 2025 national median for the exact O*NET job (`scripts/bls.py`); `oohPay` is the
  Handbook profile's pay, which can cover a larger group. Teacher Assistant and Home Health Aide use the OEWS group codes
  25-9045 and 31-1120 (OEWS publishes no detailed 25-9042 or 31-1121 line), so their pay is the group's.
- `oohJobs` ("People doing it" on the sheet) is the Handbook's number of jobs, which counts self-employed workers; the
  old OEWS count left them out (Farmer: OEWS 6,500, Handbook 788,700).
- Cluster changes (Advance CTE 2024): Hairstylist is in Healthcare and Human Services (Personal Care Services), Real
  Estate Agent in Financial Services (Real Estate).
- Unconfirmed placements (kept, settled in Refine round 1): Flight Attendant in Hospitality, Events and Tourism and Public
  Relations Specialist in Marketing and Sales. Advance CTE's 2024 crosswalk was not checked for these two.
- 10 careers added in polish round 1 (`C_MORE` in `scripts/careers_data.py`, written only with `--more`): their Similar
  careers interests are O*NET OnLine's "Career Interest Types" for each code (https://www.onetonline.org/link/details/
  plus the code), read 2026-10-28 on the 0-100 scale and stored as 1 + score * 6 / 100 (`ONET_MORE`). They have no Job
  Zone or work context.

- `level` is the Clusters ladder column: 0 No degree needed (No formal educational credential; High school diploma or
  equivalent), 1 Certificate or some college (Postsecondary nondegree award; Some college, no degree), 2 Associate's,
  3 Bachelor's, 4 Master's, doctoral or professional.
- Where Quick Facts says "See How to Become One", `eduNote` quotes the Handbook's How to Become One sentence for this
  job, and `level` follows that sentence (7 careers, marked * below).
- game-design: the Web Developers and Digital Designers profile lists O*NET "Video Game Designers" under More Information.
- robotics-tech: the Electro-mechanical and Mechatronics profile lists O*NET "Robotics Technicians" under More Information.
- ops-mgr: the Top Executives profile covers general and operations managers ("held about 3.6 million jobs in 2025").

| Career | Handbook profile | Typical entry-level education | Job outlook 2025-35 | URL |
|---|---|---|---|---|
| welder | Welders, Cutters, Solderers, and Brazers | High school diploma or equivalent | 2% (Slower than average) | https://www.bls.gov/ooh/production/welders-cutters-solderers-and-brazers.htm |
| machinist | Machinists and Tool and Die Makers | See How to Become One * "Machinists typically need a high school diploma or equivalent" | -1% (Decline) | https://www.bls.gov/ooh/production/machinists-and-tool-and-die-makers.htm |
| ind-eng | Industrial Engineers | Bachelor's degree | 12% (Much faster than average) | https://www.bls.gov/ooh/architecture-and-engineering/industrial-engineers.htm |
| robotics-tech | Electro-mechanical and Mechatronics Technologists and Technicians | Associate's degree | 3% (As fast as average) | https://www.bls.gov/ooh/architecture-and-engineering/electro-mechanical-technicians.htm |
| vet | Veterinarians | Doctoral or professional degree | 9% (Much faster than average) | https://www.bls.gov/ooh/healthcare/veterinarians.htm |
| vet-tech | Veterinary Technologists and Technicians | Associate's degree | 9% (Much faster than average) | https://www.bls.gov/ooh/healthcare/veterinary-technologists-and-technicians.htm |
| food-sci | Agricultural and Food Scientists | Bachelor's degree | 6% (Faster than average) | https://www.bls.gov/ooh/life-physical-and-social-science/agricultural-and-food-scientists.htm |
| farmer | Farmers, Ranchers, and Other Agricultural Managers | High school diploma or equivalent | -3% (Decline) | https://www.bls.gov/ooh/management/farmers-ranchers-and-other-agricultural-managers.htm |
| graphic-design | Graphic Designers | Bachelor's degree | -2% (Decline) | https://www.bls.gov/ooh/arts-and-design/graphic-designers.htm |
| animator | Special Effects Artists and Animators | Bachelor's degree | 0% (Little or no change) | https://www.bls.gov/ooh/arts-and-design/multimedia-artists-and-animators.htm |
| musician | Musicians and Singers | No formal educational credential | 0% (Little or no change) | https://www.bls.gov/ooh/entertainment-and-sports/musicians-and-singers.htm |
| photographer | Photographers | High school diploma or equivalent | -1% (Decline) | https://www.bls.gov/ooh/media-and-communication/photographers.htm |
| fashion | Fashion Designers | Bachelor's degree | 0% (Little or no change) | https://www.bls.gov/ooh/arts-and-design/fashion-designers.htm |
| game-design | Web Developers and Digital Designers | Bachelor's degree | 5% (Faster than average) | https://www.bls.gov/ooh/computer-and-information-technology/web-developers.htm |
| film-editor | Film and Video Editors and Camera Operators | Bachelor's degree | 3% (As fast as average) | https://www.bls.gov/ooh/media-and-communication/film-and-video-editors-and-camera-operators.htm |
| interior | Interior Designers | Bachelor's degree | 3% (As fast as average) | https://www.bls.gov/ooh/arts-and-design/interior-designers.htm |
| writer | Writers and Authors | Bachelor's degree | 0% (Little or no change) | https://www.bls.gov/ooh/media-and-communication/writers-and-authors.htm |
| actor | Actors | Some college, no degree | 0% (Little or no change) | https://www.bls.gov/ooh/entertainment-and-sports/actors.htm |
| director | Producers and Directors | Bachelor's degree | 4% (As fast as average) | https://www.bls.gov/ooh/entertainment-and-sports/producers-and-directors.htm |
| electrician | Electricians | High school diploma or equivalent | 9% (Much faster than average) | https://www.bls.gov/ooh/construction-and-extraction/electricians.htm |
| carpenter | Carpenters | High school diploma or equivalent | 4% (As fast as average) | https://www.bls.gov/ooh/construction-and-extraction/carpenters.htm |
| plumber | Plumbers, Pipefitters, and Steamfitters | High school diploma or equivalent | 7% (Much faster than average) | https://www.bls.gov/ooh/construction-and-extraction/plumbers-pipefitters-and-steamfitters.htm |
| architect | Architects | Bachelor's degree | 4% (As fast as average) | https://www.bls.gov/ooh/architecture-and-engineering/architects.htm |
| civil-eng | Civil Engineers | Bachelor's degree | 6% (Faster than average) | https://www.bls.gov/ooh/architecture-and-engineering/civil-engineers.htm |
| hvac | Heating, Air Conditioning, and Refrigeration Mechanics and Installers | Postsecondary nondegree award | 11% (Much faster than average) | https://www.bls.gov/ooh/installation-maintenance-and-repair/heating-air-conditioning-and-refrigeration-mechanics-and-installers.htm |
| equip-op | Construction Equipment Operators | High school diploma or equivalent | 4% (As fast as average) | https://www.bls.gov/ooh/construction-and-extraction/construction-equipment-operators.htm |
| software-dev | Software Developers, Quality Assurance Analysts, and Testers | Bachelor's degree | 10% (Much faster than average) | https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm |
| cyber | Information Security Analysts | Bachelor's degree | 21% (Much faster than average) | https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm |
| data-sci | Data Scientists | Bachelor's degree | 35% (Much faster than average) | https://www.bls.gov/ooh/math/data-scientists.htm |
| web-dev | Web Developers and Digital Designers | Bachelor's degree | 5% (Faster than average) | https://www.bls.gov/ooh/computer-and-information-technology/web-developers.htm |
| it-support | Computer Support Specialists | See How to Become One * "user support specialists typically need to complete some college courses" | -3% (Decline) | https://www.bls.gov/ooh/computer-and-information-technology/computer-support-specialists.htm |
| teacher | Kindergarten and Elementary School Teachers | Bachelor's degree | 0% (Little or no change) | https://www.bls.gov/ooh/education-training-and-library/kindergarten-and-elementary-school-teachers.htm |
| preschool | Preschool Teachers | Associate's degree | 4% (As fast as average) | https://www.bls.gov/ooh/education-training-and-library/preschool-teachers.htm |
| counselor | School and Career Counselors and Advisors | Master's degree | 3% (As fast as average) | https://www.bls.gov/ooh/community-and-social-service/school-and-career-counselors.htm |
| librarian | Librarians and Library Media Specialists | Master's degree | 3% (As fast as average) | https://www.bls.gov/ooh/education-training-and-library/librarians.htm |
| coach | Coaches and Scouts | Bachelor's degree | 6% (Faster than average) | https://www.bls.gov/ooh/entertainment-and-sports/coaches-and-scouts.htm |
| wind-tech | Wind Turbine Technicians | Postsecondary nondegree award | 30% (Much faster than average) | https://www.bls.gov/ooh/installation-maintenance-and-repair/wind-turbine-technicians.htm |
| solar | Solar Photovoltaic Installers | High school diploma or equivalent | 37% (Much faster than average) | https://www.bls.gov/ooh/construction-and-extraction/solar-photovoltaic-installers.htm |
| env-sci | Environmental Scientists and Specialists | Bachelor's degree | 6% (Faster than average) | https://www.bls.gov/ooh/life-physical-and-social-science/environmental-scientists-and-specialists.htm |
| wildlife | Zoologists and Wildlife Biologists | Bachelor's degree | 4% (As fast as average) | https://www.bls.gov/ooh/life-physical-and-social-science/zoologists-and-wildlife-biologists.htm |
| lineworker | Electrical Power-Line Installers and Repairers | High school diploma or equivalent | 10% (Much faster than average) | https://www.bls.gov/ooh/installation-maintenance-and-repair/line-installers-and-repairers.htm |
| meteorologist | Atmospheric Scientists, Including Meteorologists | Bachelor's degree | 3% (As fast as average) | https://www.bls.gov/ooh/life-physical-and-social-science/atmospheric-scientists-including-meteorologists.htm |
| accountant | Accountants and Auditors | Bachelor's degree | 5% (Faster than average) | https://www.bls.gov/ooh/business-and-financial/accountants-and-auditors.htm |
| fin-advisor | Personal Financial Advisors | Bachelor's degree | 1% (Slower than average) | https://www.bls.gov/ooh/business-and-financial/personal-financial-advisors.htm |
| actuary | Actuaries | Bachelor's degree | 9% (Much faster than average) | https://www.bls.gov/ooh/math/actuaries.htm |
| nurse | Registered Nurses | Bachelor's degree | 6% (Faster than average) | https://www.bls.gov/ooh/healthcare/registered-nurses.htm |
| doctor | Physicians and Surgeons | Doctoral or professional degree | 4% (As fast as average) | https://www.bls.gov/ooh/healthcare/physicians-and-surgeons.htm |
| pa | Physician Assistants | Master's degree | 21% (Much faster than average) | https://www.bls.gov/ooh/healthcare/physician-assistants.htm |
| pt | Physical Therapists | Doctoral or professional degree | 12% (Much faster than average) | https://www.bls.gov/ooh/healthcare/physical-therapists.htm |
| hygienist | Dental Hygienists | Associate's degree | 8% (Much faster than average) | https://www.bls.gov/ooh/healthcare/dental-hygienists.htm |
| paramedic | EMTs and Paramedics | Postsecondary nondegree award | 6% (Faster than average) | https://www.bls.gov/ooh/healthcare/emts-and-paramedics.htm |
| pharmacist | Pharmacists | Doctoral or professional degree | 5% (Faster than average) | https://www.bls.gov/ooh/healthcare/pharmacists.htm |
| social-worker | Social Workers | See How to Become One * "A bachelor's degree in social work (BSW) is the most common requirement for entry-level nonclinical social worker positions." | 6% (Faster than average) | https://www.bls.gov/ooh/community-and-social-service/social-workers.htm |
| psychologist | Psychologists | See How to Become One * "Psychologists typically need at least a master's degree to enter the occupation." | 6% (Faster than average) | https://www.bls.gov/ooh/life-physical-and-social-science/psychologists.htm |
| med-assist | Medical Assistants | Postsecondary nondegree award | 13% (Much faster than average) | https://www.bls.gov/ooh/healthcare/medical-assistants.htm |
| athletic-trainer | Athletic Trainers | Master's degree | 13% (Much faster than average) | https://www.bls.gov/ooh/healthcare/athletic-trainers.htm |
| chef | Chefs and Head Cooks | High school diploma or equivalent | 7% (Much faster than average) | https://www.bls.gov/ooh/food-preparation-and-serving/chefs-and-head-cooks.htm |
| cook | Cooks | See How to Become One * "Most cooks learn their skills through on-the-job training and work-related experience." | 7% (Much faster than average) | https://www.bls.gov/ooh/food-preparation-and-serving/cooks.htm |
| event-planner | Meeting, Convention, and Event Planners | Bachelor's degree | 6% (Faster than average) | https://www.bls.gov/ooh/business-and-financial/meeting-convention-and-event-planners.htm |
| hotel-mgr | Lodging Managers | High school diploma or equivalent | 4% (As fast as average) | https://www.bls.gov/ooh/management/lodging-managers.htm |
| flight-attendant | Flight Attendants | High school diploma or equivalent | 9% (Much faster than average) | https://www.bls.gov/ooh/transportation-and-material-moving/flight-attendants.htm |
| stylist | Barbers, Hairstylists, and Cosmetologists | Postsecondary nondegree award | 7% (Much faster than average) | https://www.bls.gov/ooh/personal-care-and-service/barbers-hairstylists-and-cosmetologists.htm |
| ops-mgr | Top Executives | Bachelor's degree | 5% (Faster than average) | https://www.bls.gov/ooh/management/top-executives.htm |
| hr | Human Resources Specialists | Bachelor's degree | 6% (Faster than average) | https://www.bls.gov/ooh/business-and-financial/human-resources-specialists.htm |
| project-mgr | Project Management Specialists | Bachelor's degree | 7% (Much faster than average) | https://www.bls.gov/ooh/business-and-financial/project-management-specialists.htm |
| marketing-mgr | Advertising, Promotions, and Marketing Managers | Bachelor's degree | 6% (Faster than average) | https://www.bls.gov/ooh/management/advertising-promotions-and-marketing-managers.htm |
| realtor | Real Estate Brokers and Sales Agents | High school diploma or equivalent | 2% (Slower than average) | https://www.bls.gov/ooh/sales/real-estate-brokers-and-sales-agents.htm |
| pr | Public Relations Specialists | Bachelor's degree | 2% (Slower than average) | https://www.bls.gov/ooh/media-and-communication/public-relations-specialists.htm |
| market-research | Market Research Analysts | Bachelor's degree | 7% (Much faster than average) | https://www.bls.gov/ooh/business-and-financial/market-research-analysts.htm |
| firefighter | Firefighters | Postsecondary nondegree award | 4% (As fast as average) | https://www.bls.gov/ooh/protective-service/firefighters.htm |
| police | Police and Detectives | See How to Become One * "Police and detective applicants must have at least a high school diploma or equivalent" | 3% (As fast as average) | https://www.bls.gov/ooh/protective-service/police-and-detectives.htm |
| lawyer | Lawyers | Doctoral or professional degree | 5% (Faster than average) | https://www.bls.gov/ooh/legal/lawyers.htm |
| paralegal | Paralegals and Legal Assistants | Associate's degree | 0% (Little or no change) | https://www.bls.gov/ooh/legal/paralegals-and-legal-assistants.htm |
| planner | Urban and Regional Planners | Master's degree | 4% (As fast as average) | https://www.bls.gov/ooh/life-physical-and-social-science/urban-and-regional-planners.htm |
| dispatcher | Public Safety Telecommunicators | High school diploma or equivalent | 4% (As fast as average) | https://www.bls.gov/ooh/office-and-administrative-support/police-fire-and-ambulance-dispatchers.htm |
| forensic | Forensic Science Technicians | Bachelor's degree | 13% (Much faster than average) | https://www.bls.gov/ooh/life-physical-and-social-science/forensic-science-technicians.htm |
| pilot | Airline and Commercial Pilots | See How to Become One * "Airline pilots typically need a bachelor's degree and experience as a commercial or military pilot." | 7% (Much faster than average) | https://www.bls.gov/ooh/transportation-and-material-moving/airline-and-commercial-pilots.htm |
| trucker | Heavy and Tractor-Trailer Truck Drivers | Postsecondary nondegree award | 4% (As fast as average) | https://www.bls.gov/ooh/transportation-and-material-moving/heavy-and-tractor-trailer-truck-drivers.htm |
| logistician | Logisticians | Bachelor's degree | 18% (Much faster than average) | https://www.bls.gov/ooh/business-and-financial/logisticians.htm |
| auto-tech | Automotive Service Technicians and Mechanics | Postsecondary nondegree award | 5% (Faster than average) | https://www.bls.gov/ooh/installation-maintenance-and-repair/automotive-service-technicians-and-mechanics.htm |
| aircraft-mech | Aircraft and Avionics Equipment Mechanics and Technicians | Postsecondary nondegree award | 6% (Faster than average) | https://www.bls.gov/ooh/installation-maintenance-and-repair/aircraft-and-avionics-equipment-mechanics-and-technicians.htm |
| atc | Air Traffic Controllers | Associate's degree | 2% (Slower than average) | https://www.bls.gov/ooh/transportation-and-material-moving/air-traffic-controllers.htm |
| aerospace | Aerospace Engineers | Bachelor's degree | 8% (Much faster than average) | https://www.bls.gov/ooh/architecture-and-engineering/aerospace-engineers.htm |
| admin-asst | Secretaries and Administrative Assistants | High school diploma or equivalent | -2% (Decline) | https://www.bls.gov/ooh/office-and-administrative-support/secretaries-and-administrative-assistants.htm |
| retail | Retail Sales Workers | No formal educational credential | 0% (Little or no change) | https://www.bls.gov/ooh/sales/retail-sales-workers.htm |
| cs-research | Computer and Information Research Scientists | Master's degree | 22% (Much faster than average) | https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm |
| childcare | Childcare Workers | High school diploma or equivalent | -2% (Decline) | https://www.bls.gov/ooh/personal-care-and-service/childcare-workers.htm |
| teacher-asst | Teacher Assistants | Some college, no degree | 0% (Little or no change) | https://www.bls.gov/ooh/education-training-and-library/teacher-assistants.htm |
| home-aide | Home Health and Personal Care Aides | High school diploma or equivalent | 18% (Much faster than average) | https://www.bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm |
| bookkeeper | Bookkeeping, Accounting, and Auditing Clerks | Some college, no degree | -6% (Decline) | https://www.bls.gov/ooh/office-and-administrative-support/bookkeeping-accounting-and-auditing-clerks.htm |
| mover | Hand Laborers and Material Movers | No formal educational credential | 4% (As fast as average) | https://www.bls.gov/ooh/transportation-and-material-moving/hand-laborers-and-material-movers.htm |
| drafter | Drafters | Associate's degree | 1% (Slower than average) | https://www.bls.gov/ooh/architecture-and-engineering/drafters.htm |
| env-tech | Environmental Science and Protection Technicians | Associate's degree | 7% (Much faster than average) | https://www.bls.gov/ooh/life-physical-and-social-science/environmental-science-and-protection-technicians.htm |

Spot-check (Done when 2), from the live pages: Graphic Designers (Bachelor's degree, -2% (Decline), $62,960 in 2025,
matching the spec); Welders, Cutters, Solderers, and Brazers for welder (a larger profile: High school diploma or
equivalent, 2% (Slower than average)); Web Developers and Digital Designers for game-design (larger profile:
Bachelor's degree, 5% (Faster than average)).

Clusters: Advance CTE, Career Clusters Framework (2024), https://careertech.org/career-clusters/

Cluster definitions (the one line under each ladder heading and on the sheet's lantern line): plain-word versions,
written for grades 6-8, of the "The Cluster Defined" paragraph on each cluster's page under
https://careertech.org/career-clusters/ (read 2026-10-28). They are in `DEF` in `src.html` and in the spec's Content.
