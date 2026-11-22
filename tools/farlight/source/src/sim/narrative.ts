export type ShipHullId = 'starhopper' | 'sunskipper' | 'cloudwhale' | 'comet-dart';

export interface ShipHullSpec {
  id: ShipHullId;
  name: string;
  costStars: number;
  bonusRangeLY: number;
  speedMult: number;
  description: string;
}

export const SHIP_HULLS: readonly ShipHullSpec[] = [
  {
    id: 'starhopper',
    name: 'Starhopper',
    costStars: 0,
    bonusRangeLY: 0,
    speedMult: 1.0,
    description: 'Your trusty cream-and-coral explorer craft. Agile, cozy, and ready for adventure!',
  },
  {
    id: 'sunskipper',
    name: 'Sunskipper',
    costStars: 6,
    bonusRangeLY: 40,
    speedMult: 1.15,
    description: 'Golden twin-boom glider with wide solar wings for longer star jumps.',
  },
  {
    id: 'cloudwhale',
    name: 'Cloudwhale',
    costStars: 12,
    bonusRangeLY: 75,
    speedMult: 1.28,
    description: 'Mint-and-cream science cruiser with twin observation domes for deep-space expeditions.',
  },
  {
    id: 'comet-dart',
    name: 'Comet Dart',
    costStars: 20,
    bonusRangeLY: 120,
    speedMult: 1.45,
    description: 'Cobalt-and-gold delta-wing star-chaser built to leap across spiral arms!',
  },
];

export function getShipHull(id: ShipHullId): ShipHullSpec {
  return SHIP_HULLS.find((h) => h.id === id) ?? SHIP_HULLS[0]!;
}

export interface Transmission {
  id: string;
  minJumps: number;
  sender: string;
  title: string;
  body: string;
}

export const STORY_TRANSMISSIONS: readonly Transmission[] = [
  {
    id: 'tx-0',
    minJumps: 0,
    sender: 'Prof. Aria · Earth Observatory',
    title: 'We Found Your Signal!',
    body: 'Good news, explorer! When the Fold-Drive hiccuped during our astronomy test, it bounced you about 620 light-years out. Follow the golden HOME beacon on your Galaxy Map (M), and scan any cool planets you pass!',
  },
  {
    id: 'tx-1',
    minJumps: 1,
    sender: 'Prof. Aria · Earth Observatory',
    title: 'First Jump Complete!',
    body: 'Your telemetry just pinged our dish! Every planet, tree, and critter you scan sends Discovery Stars back to our observatory and boosts your jump computer. Try landing on a world (L) and building a Cozy Research Camp (B) while on foot!',
  },
  {
    id: 'tx-3',
    minJumps: 3,
    sender: 'Leo · Junior Astronomer',
    title: 'The Whole Class Is Watching!',
    body: 'We put your star-trail up on the classroom projector! Have you seen a spinning Pulsar or a Black Hole yet? They bend light like a giant cosmic magnifying glass, and they are totally safe to admire from orbit!',
  },
  {
    id: 'tx-5',
    minJumps: 5,
    sender: 'Prof. Aria · Earth Observatory',
    title: 'Halfway Across the Spiral Arm',
    body: 'Years pass faster here at home while you fold through space, and students are already studying the worlds you named. Check your Hangar in the Journal (Q): you might have enough Discovery Stars to unlock a faster ship!',
  },
  {
    id: 'tx-home',
    minJumps: 999, // Unlocked specially upon reaching Sol
    sender: 'Earth Observatory · Sol',
    title: 'Welcome Home, Starfarer!',
    body: 'Earth’s orbital beacons are flashing green for your landing! You crossed hundreds of light-years and brought back wonders nobody had ever seen.',
  },
];

export interface EndingSummary {
  title: string;
  badge: string;
  description: string;
}

export function evaluateEnding(stats: {
  scannedCount: number;
  campCount: number;
  visitedExotic: boolean;
  discoveryStars: number;
}): EndingSummary {
  const botanist = stats.scannedCount >= 4;
  const trailblazer = stats.campCount >= 2;
  const starlight = stats.visitedExotic && stats.discoveryStars >= 15;

  if (botanist && trailblazer && starlight) {
    return {
      title: 'Grand Explorer of Farlight',
      badge: '🌟 Secret Master Ending',
      description:
        'You cataloged alien ecosystems, built a network of cozy research camps, and charted pulsars and black holes! Your Explorer’s Journal becomes Earth’s favorite atlas of the stars.',
    };
  }
  if (trailblazer) {
    return {
      title: 'The Trailblazer’s Network',
      badge: '⛺ Outpost Builder Ending',
      description:
        'Your cozy glowing Research Camps form a welcoming bridge across the galaxy, guiding future explorers safely between distant suns!',
    };
  }
  if (botanist) {
    return {
      title: 'The Galactic Naturalist',
      badge: '🌿 Wildlife & Flora Ending',
      description:
        'You returned with sketches and scans of singing dunes, lantern forests, and bouncy critters, inspiring a whole generation of young space scientists!',
    };
  }
  return {
    title: 'The Swift Starfarer',
    badge: '🚀 Homecoming Ending',
    description:
      'You navigated straight home across hundreds of light-years back to blue Earth and ringed Saturn! Keep flying anytime to unlock every ship and discover more worlds.',
  };
}
