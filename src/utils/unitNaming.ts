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
    return 'OG-A2';
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
  // e.g. "OG-01-A", "KlikA1-05-B", "Klik-A1-05-B", "OG-A1-01-A", "A1-01-A"
  const prefixMatch = raw.match(/^([A-Za-z]+(?:[-_]?[A-Za-z0-9]+)?)[-_](\d+)[-_]?([A-Za-z])?$/i);
  if (prefixMatch) {
    const rawGroup = prefixMatch[1];
    const orderNum = parseInt(prefixMatch[2], 10);
    const suffix = (prefixMatch[3] || 'A').toUpperCase();
    const group = normalizeGroupTag(rawGroup, orderNum);
    const padded = String(orderNum).padStart(2, '0');

    // Retain clean formatted tag: OG-XX-A for OG, KlikA1-XX-A / Klik-A1-XX-A for Klik
    let prefixForFormatted: string;
    if (group === 'OG-A1') {
      prefixForFormatted = rawGroup.toUpperCase().includes('A1') && rawGroup.toUpperCase().includes('OG') ? 'OG-A1' : 'OG';
    } else if (group === 'Klik-A1') {
      prefixForFormatted = rawGroup.toLowerCase().includes('-') ? 'Klik-A1' : 'KlikA1';
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
  if (norm === 'oga1' || norm === 'og') return 'Original Content (OG-A1)';
  if (norm === 'oga2') return 'Original Content (OG-A2)';
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
