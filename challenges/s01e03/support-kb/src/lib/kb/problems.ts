// What a merged ticket holds, problem by problem. causes.ts decides parser vs hint by tenant and
// channel; a report the desk read as a one-day move (desk-notes.json) is neither: its date keeps
// day and month, only the day shifts. So it is a problem of its own here, not a footnote.
import notes from '#lib/data/desk-notes.json';
import { causeOf, uniqueById, type Report, type Tenant } from '#lib/kb/causes';

export type Problem = 'parser' | 'hint' | 'one-day' | 'unplaced';

export const PROBLEM_TEXT: Record<Problem, string> = {
  parser: 'the shared parser reads day-first dates month first',
  hint: 'booking-v3 hints MM/DD/YYYY, then reads the date day first',
  'one-day': 'the invite lands one day off: same date, wrong day',
  unplaced: 'no tenant on file',
};

export function problemOf(r: Report, t: Tenant | undefined): Problem {
  if (notes.oneDayMove.includes(r.id)) return 'one-day';
  return causeOf(r, t) ?? 'unplaced';
}

export type ProblemGroup = {
  problem: Problem;
  reports: number;
  tenants: number;
  firstSeen: string;
  lastSeen: string;
  // Reports intake tagged with something other than this problem.
  mistagged: number;
};

export function splitTicket(all: Report[], ticket: number, tenantOf: (r: Report) => Tenant | undefined) {
  const exported = all.filter((r) => r.mergedInto === ticket).length;
  const merged = uniqueById(all).filter((r) => r.mergedInto === ticket);
  const by = new Map<Problem, Report[]>();
  for (const r of merged) {
    const p = problemOf(r, tenantOf(r));
    by.set(p, [...(by.get(p) ?? []), r]);
  }
  const groups: ProblemGroup[] = [...by.entries()]
    .map(([problem, rs]) => {
      const days = rs.map((r) => r.receivedAt.slice(0, 10)).sort();
      return {
        problem,
        reports: rs.length,
        tenants: new Set(rs.map((r) => r.tenant)).size,
        firstSeen: days[0],
        lastSeen: days[days.length - 1],
        mistagged: rs.filter((r) => r.meta.intakeTag !== problem).length,
      };
    })
    .sort((a, b) => b.reports - a.reports);
  return { exported, unique: merged.length, groups };
}
