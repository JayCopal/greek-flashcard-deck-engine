import { Unit } from '../types/schema';

export interface ParsedLessonCode {
  group: string;       // e.g. "A1", "A2", "B1"
  orderNum: number;    // e.g. 1, 2, 5
  suffix: string;      // e.g. "A", "B"
  formatted: string;   // e.g. "A1-01-A", "KlikA1-05-B"
  lessonLabel: string; // e.g. "Lesson A1-01-A", "Lesson KlikA1-05-B"
  groupName: string;   // e.g. "Κλικ στα Ελληνικά Α1 (A1)"
}

// Backwards compatibility alias
export type ParsedUnitCode = ParsedLessonCode;

/**
 * Normalizes group tags to standard CEFR level identifiers (e.g. "A1", "A2").
 * Maps legacy "OG" and textbook "KlikA1" to canonical "A1".
 */
export function normalizeGroupTag(rawGroup: string): string {
  const norm = rawGroup.trim().toLowerCase();
  if (norm === 'og' || norm === 'klika1' || norm === 'a1') return 'A1';
  if (norm === 'klika2' || norm === 'a2') return 'A2';
  if (norm === 'klikb1' || norm === 'b1') return 'B1';
  if (norm === 'klikb2' || norm === 'b2') return 'B2';
  if (norm.startsWith('klik')) return norm.slice(4).toUpperCase();
  return rawGroup.toUpperCase();
}

/**
 * Intelligent parser that extracts group, numeric order, and suffix.
 * Examples:
 * - "A1-01-A" -> group: "A1", orderNum: 1, suffix: "A", formatted: "A1-01-A"
 * - "KlikA1-05-B" -> group: "A1", orderNum: 5, suffix: "B", formatted: "KlikA1-05-B"
 * - "OG-01-A" -> group: "A1", orderNum: 1, suffix: "A", formatted: "A1-01-A"
 * - 1 or "unit-01" -> group: "A1", orderNum: 1, suffix: "A", formatted: "A1-01-A"
 * - 101 -> group: "A1", orderNum: 1, suffix: "A", formatted: "KlikA1-01-A"
 */
export function parseLessonCode(orderOrId: string | number | undefined, fallbackIndex = 1): ParsedLessonCode {
  if (orderOrId === undefined || orderOrId === null) {
    const padded = String(fallbackIndex).padStart(2, '0');
    return {
      group: 'A1',
      orderNum: fallbackIndex,
      suffix: 'A',
      formatted: `A1-${padded}-A`,
      lessonLabel: `Lesson A1-${padded}-A`,
      groupName: getGroupTitle('A1'),
    };
  }

  const raw = String(orderOrId).trim();

  // Pattern 1: Explicit group prefix: <Group>-<number>-<suffix> or <Group>-<number><suffix>
  // e.g. "A1-01-A", "KlikA1-05-B", "OG-01-A", "KlikA2-01-A"
  const prefixMatch = raw.match(/^([A-Za-z0-9]+)[-_](\d+)[-_]?([A-Za-z])?$/i);
  if (prefixMatch) {
    const rawGroup = prefixMatch[1];
    const group = normalizeGroupTag(rawGroup);
    const orderNum = parseInt(prefixMatch[2], 10);
    const suffix = (prefixMatch[3] || 'A').toUpperCase();
    const padded = String(orderNum).padStart(2, '0');
    // Normalize legacy OG prefix to A1 for clean display
    const prefixForFormatted = rawGroup.toUpperCase() === 'OG' ? 'A1' : rawGroup;
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
        group: 'A2',
        orderNum: mappedNum,
        suffix: suf,
        formatted,
        lessonLabel: `Lesson ${formatted}`,
        groupName: getGroupTitle('A2'),
      };
    }
    if (num >= 100) {
      const mappedNum = num - 100;
      const padded = String(mappedNum).padStart(2, '0');
      const formatted = `KlikA1-${padded}-${suf}`;
      return {
        group: 'A1',
        orderNum: mappedNum,
        suffix: suf,
        formatted,
        lessonLabel: `Lesson ${formatted}`,
        groupName: getGroupTitle('A1'),
      };
    }
    const padded = String(num).padStart(2, '0');
    const formatted = `A1-${padded}-${suf}`;
    return {
      group: 'A1',
      orderNum: num,
      suffix: suf,
      formatted,
      lessonLabel: `Lesson ${formatted}`,
      groupName: getGroupTitle('A1'),
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
        group: 'A2',
        orderNum: mappedNum,
        suffix: suf,
        formatted,
        lessonLabel: `Lesson ${formatted}`,
        groupName: getGroupTitle('A2'),
      };
    }
    if (num >= 100) {
      const mappedNum = num - 100;
      const padded = String(mappedNum).padStart(2, '0');
      const formatted = `KlikA1-${padded}-${suf}`;
      return {
        group: 'A1',
        orderNum: mappedNum,
        suffix: suf,
        formatted,
        lessonLabel: `Lesson ${formatted}`,
        groupName: getGroupTitle('A1'),
      };
    }
    const padded = String(num).padStart(2, '0');
    const formatted = `A1-${padded}-${suf}`;
    return {
      group: 'A1',
      orderNum: num,
      suffix: suf,
      formatted,
      lessonLabel: `Lesson ${formatted}`,
      groupName: getGroupTitle('A1'),
    };
  }

  return {
    group: 'A1',
    orderNum: fallbackIndex,
    suffix: 'A',
    formatted: raw,
    lessonLabel: `Lesson ${raw}`,
    groupName: getGroupTitle('A1'),
  };
}

// Backwards compatibility alias
export const parseUnitCode = parseLessonCode;

/**
 * Returns human-friendly group title for a group ID
 */
export function getGroupTitle(group: string): string {
  const norm = group.toLowerCase();
  if (norm === 'a1' || norm === 'klika1' || norm === 'og') return 'Κλικ στα Ελληνικά Α1 (A1)';
  if (norm === 'a2' || norm === 'klika2') return 'Κλικ στα Ελληνικά Α2 (A2)';
  if (norm === 'b1' || norm === 'klikb1') return 'Κλικ στα Ελληνικά Β1 (B1)';
  if (norm === 'b2' || norm === 'klikb2') return 'Κλικ στα Ελληνικά Β2 (B2)';
  return `${group.toUpperCase()} Curriculum`;
}

// Backwards compatibility alias
export const getTrackTitle = getGroupTitle;

/**
 * Formats a lesson label, e.g. "Lesson A1-01-A", "Lesson KlikA1-05-B"
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
