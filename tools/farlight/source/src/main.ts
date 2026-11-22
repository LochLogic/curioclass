import { initWebGpu, type QualityTier } from './render/gpu-context.ts';
import { FarlightRenderer } from './render/renderer.ts';
import { generateStarSystemFromRef, type PlanetData, type StarRef } from './sim/galaxy.ts';
import { createInitialShipState, orientShipToward, stepFlight, type FlightInput } from './sim/flight.ts';
import {
  createPlanetFlightState,
  sampleTerrainHeight,
  stepPlanetFlight,
  toggleLanded,
  toggleOnFoot,
  toggleRover,
  type PlanetFlightState,
} from './sim/planet-flight.ts';
import { createOrbitalActivity, stepOrbitalActivity } from './sim/slalom.ts';
import { getPlanetSpecies } from './proc/world-gen.ts';
import {
  buildCampOnPlanet,
  createInitialJourney,
  planetScanKey,
  scanNearestPlanet,
  selectOrUnlockShip,
  startJump,
  stepJump,
} from './sim/journey.ts';
import { getShipHull, STORY_TRANSMISSIONS } from './sim/narrative.ts';
import { clearJourneyLocal, loadJourneyLocal, saveJourneyLocal } from './sim/save.ts';
import { v3Add, v3Len, v3Norm, v3Scale, v3Sub } from './sim/math.ts';
import { ProceduralAudioEngine } from './audio/engine.ts';
import { Hud } from './ui/hud.ts';
import { Overlays, type OverlayMode } from './ui/overlays.ts';

async function boot(): Promise<void> {
  const canvas = document.getElementById('gpu-canvas') as HTMLCanvasElement;
  const uiRoot = document.getElementById('ui-root') as HTMLElement;

  const audio = new ProceduralAudioEngine();
  let journey = loadJourneyLocal() ?? createInitialJourney();
  let currentSystem = generateStarSystemFromRef(journey.galaxySeed, journey.currentStar);
  let orbital = createOrbitalActivity(currentSystem);
  audio.setSystemMood(currentSystem.starKind, currentSystem.seed);
  let ship = createInitialShipState();
  ship.maxSpeed = 120 * getShipHull(journey.activeShip).speedMult;
  let planetFlight: PlanetFlightState | null = null;

  const keys = new Set<string>();
  let cruiseToggle = false;
  let dragging = false;
  let yawAccum = 0;
  let pitchAccum = 0;
  let visualBank = 0;
  let visualPitch = 0;
  let scanPulse = 0;
  let photoMode = false;

  let gpu: Awaited<ReturnType<typeof initWebGpu>>;
  let renderer: FarlightRenderer;

  const enterPlanet = (planet: PlanetData) => {
    if (!planet.landable) {
      hud.showToast(`${planet.name} is a swirling Gas Giant. Admire its rings from orbit!`);
      return;
    }
    planetFlight = createPlanetFlightState(planet, currentSystem.seed);
    cruiseToggle = false;
    overlays.open('none', journey, currentSystem, ship);
    hud.showToast(`Entering ${planet.name}'s atmosphere! Enjoy the view, then press G low over land to touch down.`, 5.0);
  };

  const exitPlanetToOrbit = () => {
    if (!planetFlight) return;
    const p = planetFlight.planet;
    const outDir = v3Norm(v3Sub(ship.position, p.position));
    ship.position = v3Add(p.position, v3Scale(outDir, p.radius * 3.4));
    ship.velocity = v3Scale(outDir, 25);
    planetFlight = null;
    cruiseToggle = false;
    hud.showToast(`Returned to orbit above ${p.name}!`);
  };

  const findNearestLandablePlanet = (): { planet: PlanetData; dist: number } | null => {
    let best: { planet: PlanetData; dist: number } | null = null;
    for (const p of currentSystem.planets) {
      if (!p.landable) continue;
      const d = v3Len(v3Sub(p.position, ship.position)) - p.radius;
      if (!best || d < best.dist) best = { planet: p, dist: d };
    }
    return best;
  };

  const handleLandOrOrbit = () => {
    if (journey.jumpPhase !== 'idle') return;
    if (planetFlight) {
      exitPlanetToOrbit();
      return;
    }
    const near = findNearestLandablePlanet();
    if (!near) {
      hud.showToast('No landable worlds in this system.');
      return;
    }
    // Kids can descend directly with L from anywhere reasonably close, or open System Map (N)
    if (near.dist > Math.max(420, near.planet.radius * 10)) {
      enterPlanet(near.planet);
    } else {
      enterPlanet(near.planet);
    }
  };

  const handleTouchdown = () => {
    if (!planetFlight) return;
    const res = toggleLanded(planetFlight);
    if (res.ok) audio.playTouchdown(planetFlight.landed);
    hud.showToast(res.message);
  };

  const handleToggleOnFoot = () => {
    if (!planetFlight) return;
    const res = toggleOnFoot(planetFlight);
    if (res.ok) audio.playUiTap();
    hud.showToast(res.message, 5.0);
  };

  const handleToggleRover = () => {
    if (!planetFlight) return;
    const res = toggleRover(planetFlight);
    if (res.ok) audio.playTouchdown(false);
    hud.showToast(res.message, 5.0);
  };

  const handleBuildCamp = () => {
    if (!planetFlight || (!planetFlight.onFoot && !planetFlight.inRover)) {
      hud.showToast('Touch down (G) and step out (E) or deploy Rover (K) to build a Cozy Research Camp!');
      return;
    }
    const cx = planetFlight.x + Math.sin(planetFlight.yaw) * 9.5;
    const cz = planetFlight.z - Math.cos(planetFlight.yaw) * 9.5;
    const cy = sampleTerrainHeight(cx, cz, planetFlight.seed, planetFlight.planet.biome);
    if (cy < planetFlight.seaLevel + 1.5) {
      hud.showToast('Walk onto dry land to place your Cozy Research Camp!');
      return;
    }
    const res = buildCampOnPlanet(journey, currentSystem, planetFlight.planet, cx, cy - 0.15, cz);
    if (res.ok) {
      audio.playScanDiscovery();
      saveJourneyLocal(journey);
    } else {
      audio.playUiTap();
    }
    hud.showToast(res.message, 5.5);
  };

  const triggerJump = (dest: StarRef | null) => {
    if (journey.jumpPhase !== 'idle') return;
    if (planetFlight) {
      hud.showToast('Launch back to orbit (L) before engaging the Jump Drive!');
      return;
    }
    const target = dest ?? journey.targetStar;
    if (!target) {
      overlays.open('galaxy', journey, currentSystem, ship);
      hud.showToast('Pick a destination star inside the glowing ring!');
      return;
    }
    const res = startJump(journey, ship, target);
    if (!res.ok) {
      hud.showToast(res.reason);
      return;
    }
    overlays.open('none', journey, currentSystem, ship);
    cruiseToggle = false;
    audio.playJumpWarp();
    hud.showToast(`Jumping to ${target.name} (${Math.round(res.distanceLY)} LY)...`, 2.2);
  };

  const triggerScan = () => {
    if (journey.jumpPhase !== 'idle') return;
    scanPulse = 1.0;
    if (planetFlight) {
      if (planetFlight.onFoot || planetFlight.inRover) {
        const sp = getPlanetSpecies(planetFlight.planet.biome);
        const floraKey = `${currentSystem.ref.id}#${planetFlight.planet.id}:flora`;
        const critterKey = `${currentSystem.ref.id}#${planetFlight.planet.id}:critter`;
        const flierKey = `${currentSystem.ref.id}#${planetFlight.planet.id}:flier`;
        const ruinKey = `${currentSystem.ref.id}#${planetFlight.planet.id}:ruin`;
        if (!journey.scannedPlanets.some((r) => r.key === floraKey)) {
          journey.scannedPlanets.push({
            key: floraKey,
            planetName: `${sp.floraName} (${planetFlight.planet.name})`,
            systemName: currentSystem.name,
            biome: planetFlight.planet.biome,
            funFact: sp.floraFact,
          });
          journey.discoveryStars += 2;
          saveJourneyLocal(journey);
          audio.playScanDiscovery();
          hud.showToast(`🌿 Discovered ${sp.floraName}! (+2 Discovery Stars) ${sp.floraFact}`, 5.5);
          return;
        }
        if (!journey.scannedPlanets.some((r) => r.key === critterKey)) {
          journey.scannedPlanets.push({
            key: critterKey,
            planetName: `${sp.critterName} (${planetFlight.planet.name})`,
            systemName: currentSystem.name,
            biome: planetFlight.planet.biome,
            funFact: sp.critterFact,
          });
          journey.discoveryStars += 3;
          saveJourneyLocal(journey);
          audio.playScanDiscovery();
          hud.showToast(`🐾 Discovered ${sp.critterName}! (+3 Discovery Stars) ${sp.critterFact}`, 5.5);
          return;
        }
        if (!journey.scannedPlanets.some((r) => r.key === flierKey)) {
          journey.scannedPlanets.push({
            key: flierKey,
            planetName: `${sp.flierName} (${planetFlight.planet.name})`,
            systemName: currentSystem.name,
            biome: planetFlight.planet.biome,
            funFact: sp.flierFact,
          });
          journey.discoveryStars += 3;
          saveJourneyLocal(journey);
          audio.playScanDiscovery();
          hud.showToast(`🦅 Discovered ${sp.flierName}! (+3 Discovery Stars) ${sp.flierFact}`, 5.5);
          return;
        }
        if (!journey.scannedPlanets.some((r) => r.key === ruinKey)) {
          journey.scannedPlanets.push({
            key: ruinKey,
            planetName: `Ancient Star-Arch (${planetFlight.planet.name})`,
            systemName: currentSystem.name,
            biome: planetFlight.planet.biome,
            funFact: 'Carved by ancient travelers to align with the spiral arms of the galaxy!',
          });
          journey.discoveryStars += 4;
          saveJourneyLocal(journey);
          audio.playScanDiscovery();
          hud.showToast(`🏛 Decoded Ancient Star-Arch on ${planetFlight.planet.name}! (+4 Discovery Stars!)`, 5.5);
          return;
        }
        audio.playUiTap();
        hud.showToast(`You've cataloged all flora, critters, sky-gliders, and ancient ruins on ${planetFlight.planet.name}!`);
        return;
      }
      // Scanning from ship on surface automatically puts ship in range of that planet
      const savedPos = ship.position;
      ship.position = { ...planetFlight.planet.position };
      const res = scanNearestPlanet(journey, currentSystem, ship);
      ship.position = savedPos;
      if (res.scanned) {
        audio.playScanDiscovery();
        saveJourneyLocal(journey);
      } else {
        audio.playUiTap();
      }
      hud.showToast(res.message, 4.5);
      return;
    }
    const res = scanNearestPlanet(journey, currentSystem, ship);
    if (res.scanned) {
      audio.playScanDiscovery();
      saveJourneyLocal(journey);
    } else {
      audio.playUiTap();
    }
    hud.showToast(res.message, 4.5);
  };

  const toggleOverlay = (mode: OverlayMode) => {
    audio.unlock();
    audio.playUiTap();
    const next = overlays.getMode() === mode ? 'none' : mode;
    overlays.open(next, journey, currentSystem, ship);
  };

  const hud = new Hud(uiRoot, {
    onOpenOverlay: toggleOverlay,
    onScan: triggerScan,
    onJump: () => triggerJump(journey.targetStar),
    onLandOrOrbit: handleLandOrOrbit,
    onTouchdown: handleTouchdown,
    onToggleOnFoot: handleToggleOnFoot,
    onToggleRover: handleToggleRover,
    onBuildCamp: handleBuildCamp,
    onToggleMute() {
      audio.unlock();
      const muted = audio.toggleMute();
      hud.setMuted(muted);
    },
    onTogglePhotoMode() {
      photoMode = !photoMode;
      hud.setPhotoMode(photoMode);
      hud.showToast(photoMode ? '📸 Photo Mode ON: press H or Esc to show menus!' : 'Menus restored.', 2.2);
    },
    onLaunchGame() {
      audio.unlock();
      audio.playScanDiscovery();
      hud.showToast(`Welcome to ${currentSystem.name}! Press L to descend to a planet or M for the Galaxy Map.`, 5.0);
    },
    onSelectQuality(tier: QualityTier) {
      if (!gpu || !renderer) return;
      gpu.resize(tier);
      renderer.rebuildPostBindGroup();
      hud.setQuality(tier);
    },
  });

  const overlays = new Overlays(uiRoot, {
    onJumpTo: (star) => triggerJump(star),
    onSelectTarget: (star) => {
      if (star.id !== journey.currentStar.id) {
        journey.targetStar = star;
      }
    },
    onPointAtPlanet: (planet) => {
      if (planetFlight) exitPlanetToOrbit();
      orientShipToward(ship, planet.position);
      hud.showToast(`Nose aligned with ${planet.name}! Press C for Cruise Drive.`);
    },
    onDescendToPlanet: (planet) => enterPlanet(planet),
    onSelectShip: (hull) => {
      const res = selectOrUnlockShip(journey, hull);
      if (res.ok) {
        audio.playScanDiscovery();
        ship.maxSpeed = 120 * getShipHull(journey.activeShip).speedMult;
        renderer?.setShipHull(journey.activeShip);
        saveJourneyLocal(journey);
      } else {
        audio.playUiTap();
      }
      hud.showToast(res.message, 4.5);
    },
    onResetJourney: () => {
      clearJourneyLocal();
      journey = createInitialJourney(Math.floor(Date.now() % 1_000_000));
      currentSystem = generateStarSystemFromRef(journey.galaxySeed, journey.currentStar);
      audio.setSystemMood(currentSystem.starKind, currentSystem.seed);
      ship = createInitialShipState();
      renderer?.setShipHull(journey.activeShip);
      planetFlight = null;
      cruiseToggle = false;
      hud.setSystem(currentSystem);
      overlays.open('none', journey, currentSystem, ship);
      saveJourneyLocal(journey);
      hud.showToast('Started a brand new galaxy journey!');
    },
    onClose: () => overlays.open('none', journey, currentSystem, ship),
  });

  try {
    gpu = await initWebGpu(canvas);
    renderer = new FarlightRenderer(gpu);
    renderer.setShipHull(journey.activeShip);
  } catch (err) {
    hud.showError(err instanceof Error ? err.message : String(err));
    return;
  }

  hud.setSystem(currentSystem);
  hud.setQuality(gpu.quality);

  window.addEventListener('resize', () => {
    gpu.resize();
    renderer.rebuildPostBindGroup();
  });

  window.addEventListener('keydown', (e) => {
    audio.unlock();
    if (hud.isTitleVisible()) return;
    if (e.code === 'Escape') {
      if (photoMode) {
        photoMode = false;
        hud.setPhotoMode(false);
      }
      overlays.open('none', journey, currentSystem, ship);
      return;
    }
    if (e.code === 'KeyH' && overlays.getMode() === 'none') {
      photoMode = !photoMode;
      hud.setPhotoMode(photoMode);
      hud.showToast(photoMode ? '📸 Photo Mode ON: press H or Esc to show menus!' : 'Menus restored.', 2.2);
      return;
    }
    if (e.code === 'KeyM') { toggleOverlay('galaxy'); return; }
    if (e.code === 'KeyN') { toggleOverlay('system'); return; }
    if (e.code === 'KeyQ') { toggleOverlay('journal'); return; }
    if (e.code === 'KeyJ') { triggerJump(journey.targetStar); return; }
    if (e.code === 'KeyL' && overlays.getMode() === 'none') { handleLandOrOrbit(); return; }
    if (e.code === 'KeyG' && overlays.getMode() === 'none') { handleTouchdown(); return; }
    if (e.code === 'KeyE' && overlays.getMode() === 'none' && planetFlight) { handleToggleOnFoot(); return; }
    if (e.code === 'KeyK' && overlays.getMode() === 'none' && planetFlight) { handleToggleRover(); return; }
    if (e.code === 'KeyB' && overlays.getMode() === 'none' && planetFlight) { handleBuildCamp(); return; }
    if (e.code === 'KeyF' && overlays.getMode() === 'none') { triggerScan(); return; }
    if (e.code === 'KeyC' && overlays.getMode() === 'none') { cruiseToggle = !cruiseToggle; }
    keys.add(e.code);
  });
  window.addEventListener('keyup', (e) => keys.delete(e.code));

  canvas.addEventListener('pointerdown', (e) => {
    audio.unlock();
    if (overlays.getMode() !== 'none') return;
    dragging = true;
    canvas.setPointerCapture(e.pointerId);
  });
  canvas.addEventListener('pointerup', () => {
    dragging = false;
  });
  canvas.addEventListener('pointermove', (e) => {
    if (overlays.getMode() !== 'none') return;
    if (!dragging && document.pointerLockElement !== canvas) return;
    const sens = 0.0028;
    yawAccum += e.movementX * sens;
    pitchAccum += e.movementY * sens;
  });

  let lastTime = performance.now();
  let fpsSmooth = 60;
  let hudTimer = 0;

  const frame = (now: number) => {
    const dt = Math.min(0.05, Math.max(0.001, (now - lastTime) / 1000));
    lastTime = now;
    fpsSmooth = fpsSmooth * 0.92 + (1 / dt) * 0.08;
    scanPulse = Math.max(0, scanPulse - dt * 1.4);

    if (journey.jumpPhase === 'tunnel') {
      const { arrivedSystem, newDiscovery } = stepJump(journey, dt);
      if (arrivedSystem) {
        currentSystem = arrivedSystem;
        orbital = createOrbitalActivity(currentSystem);
        audio.setSystemMood(currentSystem.starKind, currentSystem.seed);
        ship = createInitialShipState();
        ship.maxSpeed = 120 * getShipHull(journey.activeShip).speedMult;
        planetFlight = null;
        hud.setSystem(currentSystem);
        saveJourneyLocal(journey);
        const newTx = STORY_TRANSMISSIONS.find((t) => t.minJumps === journey.totalJumps);
        if (journey.reachedHome && currentSystem.ref.isHome) {
          audio.playScanDiscovery();
          hud.showToast('🎉 Welcome home to Sol! Open Journal (Q) to see your Homecoming Ending!', 6.5);
        } else if (newTx) {
          audio.playScanDiscovery();
          hud.showToast(`📡 New Message from ${newTx.sender}: "${newTx.title}". Press Q to read!`, 6.0);
        } else if (newDiscovery) {
          hud.showToast(`Arrived in ${currentSystem.name}! (+Discovery Stars)`);
        } else {
          hud.showToast(`Returned to ${currentSystem.name}.`);
        }
      }
    } else if (planetFlight && overlays.getMode() === 'none') {
      // Shift sun angle interactively with [ and ]
      if (keys.has('BracketLeft')) planetFlight.sunAngle -= dt * 0.85;
      if (keys.has('BracketRight')) planetFlight.sunAngle += dt * 0.85;

      const forward = (keys.has('KeyW') || keys.has('ArrowUp') ? 1 : 0) - (keys.has('KeyS') || keys.has('ArrowDown') ? 1 : 0);
      const strafe = (keys.has('KeyD') || keys.has('ArrowRight') ? 1 : 0) - (keys.has('KeyA') || keys.has('ArrowLeft') ? 1 : 0);
      const vertical = (keys.has('KeyR') ? 1 : 0) - (keys.has('KeyV') ? 1 : 0);
      const boost = keys.has('ShiftLeft') || keys.has('ShiftRight');

      const targetBank = Math.max(-0.42, Math.min(0.42, -yawAccum * 12 - strafe * 0.28));
      const targetPitch = Math.max(-0.26, Math.min(0.26, -pitchAccum * 10));
      visualBank += (targetBank - visualBank) * Math.min(1, dt * 8);
      visualPitch += (targetPitch - visualPitch) * Math.min(1, dt * 8);

      const { exitToOrbit } = stepPlanetFlight(
        planetFlight,
        {
          forward,
          strafe,
          vertical,
          yawDelta: yawAccum,
          pitchDelta: pitchAccum,
          boost,
          brake: keys.has('Space'),
          cruise: cruiseToggle,
        },
        dt,
      );
      if (exitToOrbit) {
        exitPlanetToOrbit();
      }
    } else if (overlays.getMode() === 'none' && !hud.isTitleVisible()) {
      const input: FlightInput = {
        forward: (keys.has('KeyW') || keys.has('ArrowUp') ? 1 : 0) - (keys.has('KeyS') || keys.has('ArrowDown') ? 1 : 0),
        strafe: (keys.has('KeyD') || keys.has('ArrowRight') ? 1 : 0) - (keys.has('KeyA') || keys.has('ArrowLeft') ? 1 : 0),
        vertical: (keys.has('KeyR') ? 1 : 0) - (keys.has('KeyV') ? 1 : 0),
        roll: (keys.has('KeyE') ? 1 : 0) - (keys.has('KeyZ') ? 1 : 0),
        yawDelta: yawAccum,
        pitchDelta: pitchAccum,
        boost: keys.has('ShiftLeft') || keys.has('ShiftRight'),
        brake: keys.has('Space'),
        cruise: cruiseToggle,
      };
      const targetBank = Math.max(-0.45, Math.min(0.45, -yawAccum * 14 - input.strafe * 0.25));
      const targetPitch = Math.max(-0.28, Math.min(0.28, -pitchAccum * 12));
      visualBank += (targetBank - visualBank) * Math.min(1, dt * 8);
      visualPitch += (targetPitch - visualPitch) * Math.min(1, dt * 8);

      stepFlight(ship, input, dt, currentSystem.starRadius, currentSystem.planets);

      // Orbital Slalom Ring Course & Discovery Station proximity recharge
      const orbRes = stepOrbitalActivity(orbital, ship.position);
      if (orbRes.passedRingIndex !== null) {
        audio.playRingChime(orbRes.passedRingIndex);
        if (orbRes.slalomCompletedNow) {
          journey.discoveryStars += 4;
          saveJourneyLocal(journey);
          audio.playScanDiscovery();
          hud.showToast(`🏆 Orbital Slalom Complete! (+4 Discovery Stars!)`, 5.0);
        } else {
          hud.showToast(`✨ Ring ${orbital.passedCount}/${orbital.rings.length} cleared!`, 1.8);
        }
      }
      if (orbRes.nearStation) {
        ship.solarCharge = Math.min(100, ship.solarCharge + 45 * dt);
        if (orbRes.rechargedAtStation) {
          audio.playUiTap();
          hud.showToast(`🛰 Welcome to ${orbital.stationName}! Solar Charge topped up. Press Q for Hangar!`, 4.5);
        }
      }

      // Seamless automatic atmospheric entry when flying right up to a landable planet!
      const near = findNearestLandablePlanet();
      if (near && near.dist < Math.max(18, near.planet.radius * 0.42)) {
        enterPlanet(near.planet);
      }
    }

    yawAccum = 0;
    pitchAccum = 0;

    if (planetFlight) {
      const boostVisual = keys.has('ShiftLeft') || keys.has('ShiftRight') ? 1 : cruiseToggle ? 0.65 : 0.15;
      const campKey = planetScanKey(currentSystem.ref.id, planetFlight.planet.id);
      const activeCamp = journey.camps.find((c) => c.key === campKey) ?? null;
      renderer.renderPlanet(currentSystem, planetFlight, now * 0.001, visualBank, visualPitch, boostVisual, activeCamp);
      const jetting = planetFlight.onFoot && (keys.has('Space') || keys.has('KeyR')) && planetFlight.jetpackFuel > 2;
      audio.update(
        dt,
        planetFlight.onFoot ? 'on-foot' : 'planet-fly',
        planetFlight.speed / 120,
        boostVisual,
        jetting,
      );
    } else {
      renderer.render(
        currentSystem,
        ship,
        now * 0.001,
        visualBank,
        visualPitch,
        journey.jumpPhase === 'tunnel' ? journey.jumpProgress : 0,
        scanPulse,
        orbital,
      );
      audio.update(
        dt,
        journey.jumpPhase === 'tunnel' ? 'jump' : 'space',
        ship.speed / (ship.maxSpeed * 2),
        ship.boostAmount,
        false,
      );
    }

    hudTimer += dt;
    if (hudTimer >= 0.1) {
      hud.update(ship, currentSystem, journey, fpsSmooth, hudTimer, planetFlight, orbital);
      hudTimer = 0;
    }

    requestAnimationFrame(frame);
  };

  requestAnimationFrame(frame);
}

boot();
