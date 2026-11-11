import { Unit } from '../types/schema';

export interface ParsedLessonCode {
  group: string;       // e.g. "OG-A1", "Klik-A1", "Klik-A2"
  orderNum: number;    // e.g. 0, 1, 2, 5
  suffix: string;      // e.g. "A", "B"
  formatted: string;   // e.g. "OG-01-A", "KlikA1-05-B"
  lessonLabel: string; // e.g. "Lesson OG-01-A", "Lesson KlikA1-05-B"
  groupName: string;   // e.g. "Original Content (OG-A1)", "Κλικ στα Ελληνικά Α1 (Klik-A1)"
}

// Backwards compatibility alias
export type ParsedUnitCode = ParsedLessonCode;

/**
 * Normalizes group tags to standard curriculum group identifiers (e.g. "OG-A1", "Klik-A1", "Klik-A2").
 * Identifies how the lesson was created (OG vs Klik) and the CEFR level (A1, A2, etc.).
 */
export function normalizeGroupTag(rawGroup: string, orderNum?: number): string {
  const norm = rawGroup.trim().toLowerCase().replace(/[-_]/g, '');
  if (norm === 'og' || norm === 'oga1') return 'OG-A1';
  if (norm === 'oga2') return 'OG-A2';
  if (norm === 'kega2p1' || norm === 'kega21' || norm === 'keg2p1' || norm === 'keg21' || norm === 'a2p1' || norm === 'a21') return 'KEG-A2-P1';
  if (norm === 'kega2p2' || norm === 'kega22' || norm === 'keg2p2' || norm === 'keg22' || norm === 'a2p2' || norm === 'a22') return 'KEG-A2-P2';
  if (norm === 'kega2sp' || norm === 'keg2sp' || norm === 'a2sp' || norm === 'sp' || norm === 'speaking') return 'KEG-A2-SP';
  if (norm === 'kega2' || norm === 'keg2') return 'KEG-A2-P1';
  if (norm === 'kega1' || norm === 'keg1') return 'OG-A1';
  if (norm === 'cyp' || norm === 'cypexam' || norm === 'cyprus') return 'CYP-Exam';
  if (norm === 'klika1' || norm === 'klik1') return 'Klik-A1';
  if (norm === 'klika2' || norm === 'klik2') return 'Klik-A2';
  if (norm === 'klikb1') return 'Klik-B1';
  if (norm === 'klikb2') return 'Klik-B2';
  if (norm.startsWith('klik')) {
    const rest = norm.slice(4).toUpperCase();
    return `Klik-${rest}`;
  }
  if (norm === 'a1') {
    if (orderNum !== undefined && orderNum >= 100) return 'Klik-A1';
    return 'OG-A1';
  }
  if (norm === 'a2') {
    if (orderNum !== undefined && orderNum >= 200) return 'Klik-A2';
    return 'KEG-A2-P1';
  }
  return rawGroup.toUpperCase();
}

/**
 * Intelligent parser that extracts group, numeric order, and suffix.
 * Examples:
 * - "OG-01-A" -> group: "OG-A1", orderNum: 1, suffix: "A", formatted: "OG-01-A"
 * - "KlikA1-05-B" -> group: "Klik-A1", orderNum: 5, suffix: "B", formatted: "KlikA1-05-B"
 * - "Klik-A1-05-B" -> group: "Klik-A1", orderNum: 5, suffix: "B", formatted: "Klik-A1-05-B"
 * - "OG-A1-01-A" -> group: "OG-A1", orderNum: 1, suffix: "A", formatted: "OG-01-A"
 * - 1 or "unit-01" -> group: "OG-A1", orderNum: 1, suffix: "A", formatted: "OG-01-A"
 * - 101 or "unit-101" -> group: "Klik-A1", orderNum: 1, suffix: "A", formatted: "KlikA1-01-A"
 */
export function parseLessonCode(orderOrId: string | number | undefined, fallbackIndex = 1): ParsedLessonCode {
  if (orderOrId === undefined || orderOrId === null) {
    const padded = String(fallbackIndex).padStart(2, '0');
    return {
      group: 'OG-A1',
      orderNum: fallbackIndex,
      suffix: 'A',
      formatted: `OG-${padded}-A`,
      lessonLabel: `Lesson OG-${padded}-A`,
      groupName: getGroupTitle('OG-A1'),
    };
  }

  const raw = String(orderOrId).trim();

  // Pattern 1: Explicit group prefix: <Group>-<number>-<suffix> or <Group>-<number><suffix>
  // e.g. "OG-01-A", "KlikA1-05-B", "Klik-A1-05-B", "OG-A1-01-A", "A1-01-A", "KEG-A2-P1-00-A", "KEG-A2-P2-01-A"
  const prefixMatch = raw.match(/^([A-Za-z0-9]+(?:[-_][A-Za-z0-9]+)*)[-_](\d+)[-_]?([A-Za-z])?$/i);
  if (prefixMatch) {
    const rawGroup = prefixMatch[1];
    const orderNum = parseInt(prefixMatch[2], 10);
    const suffix = (prefixMatch[3] || 'A').toUpperCase();
    const group = normalizeGroupTag(rawGroup, orderNum);
    const padded = String(orderNum).padStart(2, '0');

    // Retain clean formatted tag: OG-XX-A for OG, KlikA1-XX-A / Klik-A1-XX-A for Klik, KEG-A2-P1-XX-A / KEG-A2-P2-XX-A
    let prefixForFormatted: string;
    if (group === 'OG-A1') {
      prefixForFormatted = rawGroup.toUpperCase().includes('A1') && rawGroup.toUpperCase().includes('OG') ? 'OG-A1' : 'OG';
    } else if (group === 'KEG-A2-P1') {
      prefixForFormatted = 'KEG-A2-P1';
    } else if (group === 'KEG-A2-P2') {
      prefixForFormatted = 'KEG-A2-P2';
    } else if (group === 'KEG-A2-SP') {
      prefixForFormatted = 'SP';
    } else if (group === 'CYP-Exam') {
      prefixForFormatted = 'CYP';
    } else if (group === 'Klik-A1') {
      prefixForFormatted = rawGroup.toLowerCase().includes('-') ? 'Klik-A1' : 'KlikA1';
    } else if (group === 'Klik-A2') {
      prefixForFormatted = rawGroup.toLowerCase().includes('-') ? 'Klik-A2' : 'KlikA2';
    } else {
      prefixForFormatted = rawGroup;
    }

    const formatted = `${prefixForFormatted}-${padded}-${suffix}`;
    return {
      group,
      orderNum,
      suffix,
      formatted,
      lessonLabel: `Lesson ${formatted}`,
      groupName: getGroupTitle(group),
    };
  }

  // Pattern 2a-sp: A2 Speaking unit ID format (e.g. "unit-sp-01", "unit_sp_01", "unit-a2-sp-01")
  const a2spUnitMatch = raw.match(/^unit[-_](?:a2[-_]?)?sp[-_](\d+)([A-Za-z])?$/i);
  if (a2spUnitMatch) {
    const num = parseInt(a2spUnitMatch[1], 10);
    const suf = (a2spUnitMatch[2] || 'A').toUpperCase();
    const padded = String(num).padStart(2, '0');
    const formatted = `SP-${padded}-${suf}`;
    return {
      group: 'KEG-A2-SP',
      orderNum: num,
      suffix: suf,
      formatted,
      lessonLabel: `Lesson ${formatted}`,
      groupName: getGroupTitle('KEG-A2-SP'),
    };
  }

  // Pattern 2a: A2 Part 2 unit ID format (e.g. "unit-a2p2-01", "unit-a2-p2-01", "unit_a2p2_01")
  const a2p2UnitMatch = raw.match(/^unit[-_]a2[-_]?p2[-_](\d+)([A-Za-z])?$/i);
  if (a2p2UnitMatch) {
    const num = parseInt(a2p2UnitMatch[1], 10);
    const suf = (a2p2UnitMatch[2] || 'A').toUpperCase();
    const padded = String(num).padStart(2, '0');
    const formatted = `KEG-A2-P2-${padded}-${suf}`;
    return {
      group: 'KEG-A2-P2',
      orderNum: num,
      suffix: suf,
      formatted,
      lessonLabel: `Lesson ${formatted}`,
      groupName: getGroupTitle('KEG-A2-P2'),
    };
  }

  // Pattern 2b: A2 Part 1 unit ID format (e.g. "unit-a2-01", "unit_a2_01", "unit-a2-00", "unit-a2p1-01")
  const a2UnitMatch = raw.match(/^unit[-_]a2(?:[-_]?p1)?[-_](\d+)([A-Za-z])?$/i);
  if (a2UnitMatch) {
    const num = parseInt(a2UnitMatch[1], 10);
    const suf = (a2UnitMatch[2] || 'A').toUpperCase();
    const padded = String(num).padStart(2, '0');
    const formatted = `KEG-A2-P1-${padded}-${suf}`;
    return {
      group: 'KEG-A2-P1',
      orderNum: num,
      suffix: suf,
      formatted,
      lessonLabel: `Lesson ${formatted}`,
      groupName: getGroupTitle('KEG-A2-P1'),
    };
  }

  // Pattern 2b: Cyprus Exam unit ID format (e.g. "unit-cyp-01", "unit_cyp_01")
  const cypUnitMatch = raw.match(/^unit[-_]cyp[-_](\d+)([A-Za-z])?$/i);
  if (cypUnitMatch) {
    const num = parseInt(cypUnitMatch[1], 10);
    const suf = (cypUnitMatch[2] || 'A').toUpperCase();
    const padded = String(num).padStart(2, '0');
    const formatted = `CYP-${padded}-${suf}`;
    return {
      group: 'CYP-Exam',
      orderNum: num,
      suffix: suf,
      formatted,
      lessonLabel: `Lesson ${formatted}`,
      groupName: getGroupTitle('CYP-Exam'),
    };
  }

  // Pattern 2: Legacy unit-XX ID format
  const unitIdMatch = raw.match(/^unit[-_](\d+)([A-Za-z])?$/i);
  if (unitIdMatch) {
    const num = parseInt(unitIdMatch[1], 10);
    const suf = (unitIdMatch[2] || 'A').toUpperCase();
    if (num >= 200) {
      const mappedNum = num - 200;
      const padded = String(mappedNum).padStart(2, '0');
      const formatted = `KlikA2-${padded}-${suf}`;
      return {
        group: 'Klik-A2',
        orderNum: mappedNum,
        suffix: suf,
        formatted,
        lessonLabel: `Lesson ${formatted}`,
        groupName: getGroupTitle('Klik-A2'),
      };
    }
    if (num >= 100) {
      const mappedNum = num - 100;
      const padded = String(mappedNum).padStart(2, '0');
      const formatted = `KlikA1-${padded}-${suf}`;
      return {
        group: 'Klik-A1',
        orderNum: mappedNum,
        suffix: suf,
        formatted,
        lessonLabel: `Lesson ${formatted}`,
        groupName: getGroupTitle('Klik-A1'),
      };
    }
    const padded = String(num).padStart(2, '0');
    const formatted = `OG-${padded}-${suf}`;
    return {
      group: 'OG-A1',
      orderNum: num,
      suffix: suf,
      formatted,
      lessonLabel: `Lesson ${formatted}`,
      groupName: getGroupTitle('OG-A1'),
    };
  }

  // Pattern 3: Legacy numeric order
  const numericMatch = raw.match(/^(\d+)([A-Za-z])?$/);
  if (numericMatch) {
    const num = parseInt(numericMatch[1], 10);
    const suf = (numericMatch[2] || 'A').toUpperCase();
    if (num >= 200) {
      const mappedNum = num - 200;
      const padded = String(mappedNum).padStart(2, '0');
      const formatted = `KlikA2-${padded}-${suf}`;
      return {
        group: 'Klik-A2',
        orderNum: mappedNum,
        suffix: suf,
        formatted,
        lessonLabel: `Lesson ${formatted}`,
        groupName: getGroupTitle('Klik-A2'),
      };
    }
    if (num >= 100) {
      const mappedNum = num - 100;
      const padded = String(mappedNum).padStart(2, '0');
      const formatted = `KlikA1-${padded}-${suf}`;
      return {
        group: 'Klik-A1',
        orderNum: mappedNum,
        suffix: suf,
        formatted,
        lessonLabel: `Lesson ${formatted}`,
        groupName: getGroupTitle('Klik-A1'),
      };
    }
    const padded = String(num).padStart(2, '0');
    const formatted = `OG-${padded}-${suf}`;
    return {
      group: 'OG-A1',
      orderNum: num,
      suffix: suf,
      formatted,
      lessonLabel: `Lesson ${formatted}`,
      groupName: getGroupTitle('OG-A1'),
    };
  }

  return {
    group: 'OG-A1',
    orderNum: fallbackIndex,
    suffix: 'A',
    formatted: raw,
    lessonLabel: `Lesson ${raw}`,
    groupName: getGroupTitle('OG-A1'),
  };
}

// Backwards compatibility alias
export const parseUnitCode = parseLessonCode;

/**
 * Returns human-friendly group title for a group ID
 */
export function getGroupTitle(group: string): string {
  const norm = group.trim().toLowerCase().replace(/[-_]/g, '');
  if (norm === 'kega2p1' || norm === 'kega21' || norm === 'keg2p1' || norm === 'keg21' || norm === 'a2p1' || norm === 'a21') {
    return 'Ελληνομάθεια Α2 - Μέρος 1 (KEG-A2 P1)';
  }
  if (norm === 'kega2p2' || norm === 'kega22' || norm === 'keg2p2' || norm === 'keg22' || norm === 'a2p2' || norm === 'a22') {
    return 'Ελληνομάθεια Α2 - Μέρος 2 (KEG-A2 P2)';
  }
  if (norm === 'kega2sp' || norm === 'keg2sp' || norm === 'a2sp' || norm === 'sp' || norm === 'speaking') {
    return 'Ελληνομάθεια Α2 - Προφορικά (KEG-A2 Speaking)';
  }
  if (norm === 'kega2' || norm === 'keg2' || norm === 'oga2') return 'Ελληνομάθεια Α2 - Μέρος 1 (KEG-A2 P1)';
  if (norm === 'cypexam' || norm === 'cyp' || norm === 'cyprus') return 'Εξετάσεις Πολιτογράφησης Κύπρου (CYP-Exam)';
  if (norm === 'oga1' || norm === 'og') return 'Original Content (OG-A1)';
  if (norm === 'klika1' || norm === 'klik1') return 'Κλικ στα Ελληνικά Α1 (Klik-A1)';
  if (norm === 'klika2' || norm === 'klik2') return 'Κλικ στα Ελληνικά Α2 (Klik-A2)';
  if (norm === 'klikb1' || norm === 'klik1b1') return 'Κλικ στα Ελληνικά Β1 (Klik-B1)';
  if (norm === 'klikb2' || norm === 'klik1b2') return 'Κλικ στα Ελληνικά Β2 (Klik-B2)';
  return `${group} Curriculum`;
}

// Backwards compatibility alias
export const getTrackTitle = getGroupTitle;

/**
 * Formats a lesson label, e.g. "Lesson OG-01-A", "Lesson KlikA1-05-B"
 */
export function formatLessonLabel(item: Unit | { order: string | number; id?: string } | string | number | undefined): string {
  if (typeof item === 'object' && item !== null) {
    const parsed = parseLessonCode((item as any).order || (item as any).id);
    return parsed.lessonLabel;
  }
  const parsed = parseLessonCode(item);
  return parsed.lessonLabel;
}

// Backwards compatibility alias
export const formatUnitLabel = formatLessonLabel;

/**
 * Extracts the thematic unit or textbook chapter context from a unit's title.
 * Examples:
 * - "Χαιρετισμοί & Γνωριμία (Greetings & Introductions)" -> "Unit: Χαιρετισμοί & Γνωριμία"
 * - "Κλικ στα Ελληνικά Α1: Σελίδες 87-110 (Ενότητα 4: Από το πρωί...)" -> "Unit: Ενότητα 4"
 */
export function extractUnitContext(title: string, _order?: string | number): string {
  if (!title) return '';

  // Check for textbook "Ενότητα X"
  const enotitaMatch = title.match(/Ενότητα\s*\d+[^:)]*/i);
  if (enotitaMatch) {
    return enotitaMatch[0].trim();
  }

  // Check for introductory unit
  if (/Εισαγωγική Ενότητα/i.test(title)) {
    return 'Εισαγωγική Ενότητα';
  }

  // Check for exam / rubrics unit
  if (/Γλώσσα Εξετάσεων/i.test(title) || /Μάθημα 0/i.test(title)) {
    return 'Οδηγίες & Rubrics';
  }

  // For core thematic units, use clean Greek title
  const parenMatch = title.match(/^([^(]+)/);
  if (parenMatch) {
    return parenMatch[1].trim();
  }

  return title;
}

export interface GroupAccentStyles {
  borderLeft: string;
  borderLeftHover: string;
  pillBg: string;
  badgeBg: string;
  badgeIconColor: string;
  dotColor: string;
  hoverGlow: string;
  titleHover: string;
}

/**
 * Returns consistent, distinctive accent colors for each curriculum group
 * to visually distinguish lesson cards across groups without interfering with mastery colors.
 */
export function getGroupAccentStyles(group: string): GroupAccentStyles {
  const norm = group.trim().toLowerCase().replace(/[-_]/g, '');

  if (norm.startsWith('klika1') || norm === 'klik1') {
    return {
      borderLeft: 'border-l-indigo-500',
      borderLeftHover: 'hover:border-l-indigo-400',
      pillBg: 'bg-indigo-500/15 text-indigo-300 border-indigo-500/30',
      badgeBg: 'bg-indigo-950/70 text-indigo-300 border-indigo-700/50',
      badgeIconColor: 'text-indigo-400',
      dotColor: 'bg-indigo-400',
      hoverGlow: 'hover:shadow-indigo-500/10',
      titleHover: 'group-hover:text-indigo-300',
    };
  }

  if (norm.startsWith('klika2') || norm === 'klik2') {
    return {
      borderLeft: 'border-l-purple-500',
      borderLeftHover: 'hover:border-l-purple-400',
      pillBg: 'bg-purple-500/15 text-purple-300 border-purple-500/30',
      badgeBg: 'bg-purple-950/70 text-purple-300 border-purple-700/50',
      badgeIconColor: 'text-purple-400',
      dotColor: 'bg-purple-400',
      hoverGlow: 'hover:shadow-purple-500/10',
      titleHover: 'group-hover:text-purple-300',
    };
  }

  if (norm.startsWith('klikb') || norm.startsWith('klik1b')) {
    return {
      borderLeft: 'border-l-violet-500',
      borderLeftHover: 'hover:border-l-violet-400',
      pillBg: 'bg-violet-500/15 text-violet-300 border-violet-500/30',
      badgeBg: 'bg-violet-950/70 text-violet-300 border-violet-700/50',
      badgeIconColor: 'text-violet-400',
      dotColor: 'bg-violet-400',
      hoverGlow: 'hover:shadow-violet-500/10',
      titleHover: 'group-hover:text-violet-300',
    };
  }

  if (norm.startsWith('kega2sp') || norm === 'keg2sp' || norm === 'a2sp' || norm === 'sp' || norm === 'speaking') {
    return {
      borderLeft: 'border-l-rose-500',
      borderLeftHover: 'hover:border-l-rose-400',
      pillBg: 'bg-rose-500/15 text-rose-300 border-rose-500/30',
      badgeBg: 'bg-rose-950/70 text-rose-300 border-rose-700/50',
      badgeIconColor: 'text-rose-400',
      dotColor: 'bg-rose-400',
      hoverGlow: 'hover:shadow-rose-500/10',
      titleHover: 'group-hover:text-rose-300',
    };
  }

  if (norm.startsWith('kega2p2') || norm === 'keg2p2' || norm === 'a2p2' || norm === 'a22') {
    return {
      borderLeft: 'border-l-teal-500',
      borderLeftHover: 'hover:border-l-teal-400',
      pillBg: 'bg-teal-500/15 text-teal-300 border-teal-500/30',
      badgeBg: 'bg-teal-950/70 text-teal-300 border-teal-700/50',
      badgeIconColor: 'text-teal-400',
      dotColor: 'bg-teal-400',
      hoverGlow: 'hover:shadow-teal-500/10',
      titleHover: 'group-hover:text-teal-300',
    };
  }

  if (norm.startsWith('kega2') || norm === 'keg2' || norm.startsWith('oga2') || norm.startsWith('a2p1') || norm === 'a21') {
    return {
      borderLeft: 'border-l-emerald-500',
      borderLeftHover: 'hover:border-l-emerald-400',
      pillBg: 'bg-emerald-500/15 text-emerald-300 border-emerald-500/30',
      badgeBg: 'bg-emerald-950/70 text-emerald-300 border-emerald-700/50',
      badgeIconColor: 'text-emerald-400',
      dotColor: 'bg-emerald-400',
      hoverGlow: 'hover:shadow-emerald-500/10',
      titleHover: 'group-hover:text-emerald-300',
    };
  }

  if (norm.startsWith('cyp') || norm === 'cyprus') {
    return {
      borderLeft: 'border-l-amber-500',
      borderLeftHover: 'hover:border-l-amber-400',
      pillBg: 'bg-amber-500/15 text-amber-300 border-amber-500/30',
      badgeBg: 'bg-amber-950/70 text-amber-300 border-amber-700/50',
      badgeIconColor: 'text-amber-400',
      dotColor: 'bg-amber-400',
      hoverGlow: 'hover:shadow-amber-500/10',
      titleHover: 'group-hover:text-amber-300',
    };
  }

  // Default / OG-A1 (Original Curriculum)
  return {
    borderLeft: 'border-l-sky-500',
    borderLeftHover: 'hover:border-l-sky-400',
    pillBg: 'bg-sky-500/15 text-sky-400 border-sky-500/30',
    badgeBg: 'bg-sky-950/70 text-sky-300 border-sky-700/50',
    badgeIconColor: 'text-sky-400',
    dotColor: 'bg-sky-400',
    hoverGlow: 'hover:shadow-sky-500/10',
    titleHover: 'group-hover:text-sky-300',
  };
}

export interface GroupMetadata {
  id: string;
  shortLabel: string;
  name: string;
  greekTitle: string;
  subtitle: string;
  levelBadge: string;
  description: string;
  gradientBg: string;
  accentBorder: string;
  accentBorderActive: string;
  accentText: string;
  accentBg: string;
  badgeBg: string;
  badgeBorder: string;
  badgeText: string;
  dotColor: string;
  progressGradient: string;
  glowEffect: string;
}

/**
 * Returns comprehensive presentation metadata for curriculum groups
 * used on the landing page showcase, headers, and navigation.
 */
export function getGroupMetadata(group: string): GroupMetadata {
  const norm = group.trim().toLowerCase().replace(/[-_]/g, '');

  if (norm.startsWith('klika1') || norm === 'klik1') {
    return {
      id: 'Klik-A1',
      shortLabel: 'Klik-A1',
      name: 'Κλικ στα Ελληνικά Α1 (Klik-A1)',
      greekTitle: 'Κλικ στα Ελληνικά Α1',
      subtitle: 'Επίσημο Εγχειρίδιο • Ενότητες 1–12 (σελ. 8–180)',
      levelBadge: 'CEFR A1 • Textbook',
      description: 'Πλήρες δομημένο πρόγραμμα εκμάθησης βασισμένο στο επίσημο βιβλίο Κλικ στα Ελληνικά Α1.',
      gradientBg: 'from-indigo-950/70 via-slate-900/90 to-slate-900/90',
      accentBorder: 'border-indigo-500/30',
      accentBorderActive: 'border-indigo-400 ring-2 ring-indigo-500/40 shadow-lg shadow-indigo-500/20',
      accentText: 'text-indigo-400',
      accentBg: 'bg-indigo-500/10',
      badgeBg: 'bg-indigo-500/20',
      badgeBorder: 'border-indigo-500/40',
      badgeText: 'text-indigo-300',
      dotColor: 'bg-indigo-400',
      progressGradient: 'from-indigo-500 to-cyan-400',
      glowEffect: 'hover:shadow-indigo-500/15',
    };
  }

  if (norm.startsWith('kega2p2') || norm === 'keg2p2' || norm === 'a2p2' || norm === 'a22') {
    return {
      id: 'KEG-A2-P2',
      shortLabel: 'KEG-A2 P2',
      name: 'Ελληνομάθεια Α2 - Μέρος 2 (KEG-A2 P2)',
      greekTitle: 'Πιστοποιητικό Ελληνομάθειας Α2 (Μέρος 2)',
      subtitle: 'Εξεταστική Ύλη • Προχωρημένα Θέματα & Ανακοινώσεις',
      levelBadge: 'CEFR A2 • Exam',
      description: 'Προχωρημένες θεματικές ενότητες εξετάσεων ΚΕΓ Α2, επίσημες ανακοινώσεις, επιστολές και εκφράσεις.',
      gradientBg: 'from-teal-950/70 via-slate-900/90 to-slate-900/90',
      accentBorder: 'border-teal-500/30',
      accentBorderActive: 'border-teal-400 ring-2 ring-teal-500/40 shadow-lg shadow-teal-500/20',
      accentText: 'text-teal-400',
      accentBg: 'bg-teal-500/10',
      badgeBg: 'bg-teal-500/20',
      badgeBorder: 'border-teal-500/40',
      badgeText: 'text-teal-300',
      dotColor: 'bg-teal-400',
      progressGradient: 'from-teal-500 to-emerald-400',
      glowEffect: 'hover:shadow-teal-500/15',
    };
  }

  if (norm.startsWith('kega2sp') || norm === 'keg2sp' || norm === 'a2sp' || norm === 'sp' || norm === 'speaking') {
    return {
      id: 'KEG-A2-SP',
      shortLabel: 'KEG-A2 SP',
      name: 'Ελληνομάθεια Α2 - Προφορικά (KEG-A2 SP)',
      greekTitle: 'Προφορική Εξέταση Α2 (SP-01 έως SP-06)',
      subtitle: 'Διάδραση & Παραγωγή Προφορικού Λόγου',
      levelBadge: 'CEFR A2 • Speaking',
      description: 'Προσομοίωση προφορικών εξετάσεων ΚΕΓ με διπλές απαντήσεις υποψηφίου και ήχο Chirp-3 HD.',
      gradientBg: 'from-rose-950/70 via-slate-900/90 to-slate-900/90',
      accentBorder: 'border-rose-500/30',
      accentBorderActive: 'border-rose-400 ring-2 ring-rose-500/40 shadow-lg shadow-rose-500/20',
      accentText: 'text-rose-400',
      accentBg: 'bg-rose-500/10',
      badgeBg: 'bg-rose-500/20',
      badgeBorder: 'border-rose-500/40',
      badgeText: 'text-rose-300',
      dotColor: 'bg-rose-400',
      progressGradient: 'from-rose-500 to-pink-400',
      glowEffect: 'hover:shadow-rose-500/15',
    };
  }

  if (norm.startsWith('kega2') || norm === 'keg2' || norm.startsWith('oga2') || norm.startsWith('a2p1') || norm === 'a21') {
    return {
      id: 'KEG-A2-P1',
      shortLabel: 'KEG-A2 P1',
      name: 'Ελληνομάθεια Α2 - Μέρος 1 (KEG-A2 P1)',
      greekTitle: 'Πιστοποιητικό Ελληνομάθειας Α2 (Μέρος 1)',
      subtitle: 'Επίσημη Εξεταστική Ύλη • Κείμενα & Διάλογοι',
      levelBadge: 'CEFR A2 • Exam',
      description: 'Προετοιμασία για τις επίσημες εξετάσεις του Κέντρου Ελληνικής Γλώσσας (ΚΕΓ) - Πρώτο Μέρος.',
      gradientBg: 'from-emerald-950/70 via-slate-900/90 to-slate-900/90',
      accentBorder: 'border-emerald-500/30',
      accentBorderActive: 'border-emerald-400 ring-2 ring-emerald-500/40 shadow-lg shadow-emerald-500/20',
      accentText: 'text-emerald-400',
      accentBg: 'bg-emerald-500/10',
      badgeBg: 'bg-emerald-500/20',
      badgeBorder: 'border-emerald-500/40',
      badgeText: 'text-emerald-300',
      dotColor: 'bg-emerald-400',
      progressGradient: 'from-emerald-500 to-teal-400',
      glowEffect: 'hover:shadow-emerald-500/15',
    };
  }

  if (norm.startsWith('klika2') || norm === 'klik2') {
    return {
      id: 'Klik-A2',
      shortLabel: 'Klik-A2',
      name: 'Κλικ στα Ελληνικά Α2 (Klik-A2)',
      greekTitle: 'Κλικ στα Ελληνικά Α2',
      subtitle: 'Ενδιάμεσο Επίπεδο • Προχωρημένο Λεξιλόγιο',
      levelBadge: 'CEFR A2 • Textbook',
      description: 'Εγχειρίδιο Κλικ στα Ελληνικά Α2 με εμβάθυνση στη γραμματική και πλούσιο λεξιλόγιο.',
      gradientBg: 'from-purple-950/70 via-slate-900/90 to-slate-900/90',
      accentBorder: 'border-purple-500/30',
      accentBorderActive: 'border-purple-400 ring-2 ring-purple-500/40 shadow-lg shadow-purple-500/20',
      accentText: 'text-purple-400',
      accentBg: 'bg-purple-500/10',
      badgeBg: 'bg-purple-500/20',
      badgeBorder: 'border-purple-500/40',
      badgeText: 'text-purple-300',
      dotColor: 'bg-purple-400',
      progressGradient: 'from-purple-500 to-fuchsia-400',
      glowEffect: 'hover:shadow-purple-500/15',
    };
  }

  if (norm.startsWith('cyp') || norm === 'cyprus') {
    return {
      id: 'CYP-Exam',
      shortLabel: 'CYP-Exam',
      name: 'Εξετάσεις Πολιτογράφησης Κύπρου (CYP-Exam)',
      greekTitle: 'Εξετάσεις Πολιτογράφησης Κύπρου',
      subtitle: 'Προετοιμασία Εξετάσεων Πολιτογράφησης',
      levelBadge: 'Exam Prep',
      description: 'Ειδική εξεταστική ύλη και πρακτικές ασκήσεις για τις εξετάσεις πολιτογράφησης της Κυπριακής Δημοκρατίας.',
      gradientBg: 'from-amber-950/70 via-slate-900/90 to-slate-900/90',
      accentBorder: 'border-amber-500/30',
      accentBorderActive: 'border-amber-400 ring-2 ring-amber-500/40 shadow-lg shadow-amber-500/20',
      accentText: 'text-amber-400',
      accentBg: 'bg-amber-500/10',
      badgeBg: 'bg-amber-500/20',
      badgeBorder: 'border-amber-500/40',
      badgeText: 'text-amber-300',
      dotColor: 'bg-amber-400',
      progressGradient: 'from-amber-500 to-orange-400',
      glowEffect: 'hover:shadow-amber-500/15',
    };
  }

  // Default / OG-A1 (Original Curriculum)
  return {
    id: 'OG-A1',
    shortLabel: 'OG-A1',
    name: 'Original Content (OG-A1)',
    greekTitle: 'Βασικό Λεξιλόγιο & Θεμελιώδεις Έννοιες',
    subtitle: 'Αριθμοί, Οικογένεια, Καθημερινές Φράσεις',
    levelBadge: 'CEFR A1 • Core',
    description: 'Βασικές θεματικές ενότητες με καθημερινό λεξιλόγιο και δομημένες κάρτες εκμάθησης.',
    gradientBg: 'from-sky-950/70 via-slate-900/90 to-slate-900/90',
    accentBorder: 'border-sky-500/30',
    accentBorderActive: 'border-sky-400 ring-2 ring-sky-500/40 shadow-lg shadow-sky-500/20',
    accentText: 'text-sky-400',
    accentBg: 'bg-sky-500/10',
    badgeBg: 'bg-sky-500/20',
    badgeBorder: 'border-sky-500/40',
    badgeText: 'text-sky-300',
    dotColor: 'bg-sky-400',
    progressGradient: 'from-sky-500 to-teal-400',
    glowEffect: 'hover:shadow-sky-500/15',
  };
}

