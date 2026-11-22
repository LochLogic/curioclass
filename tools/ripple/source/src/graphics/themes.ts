import { ThemeId } from '../core/state';

export interface ThemePalette {
  id: ThemeId;
  name: string;
  bgTop: [number, number, number];
  bgBot: [number, number, number];
  causticTint: [number, number, number];
  accentGlow: [number, number, number];
  contourStrength: number; // > 0 adds subtle cymatic topographic isolines
  causticStrength: number;
  chromaticStrength: number;
  stringCore: string;
}

export const THEMES: Record<ThemeId, ThemePalette> = {
  obsidian: {
    id: 'obsidian',
    name: 'Obsidian Water',
    bgTop: [0.024, 0.035, 0.062],
    bgBot: [0.045, 0.062, 0.098],
    causticTint: [0.55, 0.78, 1.0],
    accentGlow: [0.85, 0.92, 1.0],
    contourStrength: 0.12,
    causticStrength: 1.0,
    chromaticStrength: 0.85,
    stringCore: '#fbf6e9',
  },
  cymatic: {
    id: 'cymatic',
    name: 'Cymatic Silk',
    bgTop: [0.028, 0.026, 0.055],
    bgBot: [0.052, 0.046, 0.088],
    causticTint: [0.72, 0.68, 1.0],
    accentGlow: [0.92, 0.86, 1.0],
    contourStrength: 0.55,
    causticStrength: 0.72,
    chromaticStrength: 1.0,
    stringCore: '#f6f2ff',
  },
  warm: {
    id: 'warm',
    name: 'Warm Studio',
    bgTop: [0.042, 0.031, 0.025],
    bgBot: [0.072, 0.052, 0.040],
    causticTint: [1.0, 0.78, 0.52],
    accentGlow: [1.0, 0.90, 0.76],
    contourStrength: 0.18,
    causticStrength: 0.9,
    chromaticStrength: 0.75,
    stringCore: '#fff7e8',
  },
};

export const THEME_ORDER: ThemeId[] = ['obsidian', 'cymatic', 'warm'];
