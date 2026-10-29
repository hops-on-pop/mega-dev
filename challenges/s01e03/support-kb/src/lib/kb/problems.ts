// What a merged ticket holds, problem by problem, counted the desk's way. causes.ts files each
// report under parser or hint by tenant and channel. A report the desk read as a one-day move
// (desk-notes.json) is a problem of its own: its date keeps day and month, only the day shifts.
// The desk still counts it where it is filed, so it is counted there and again on its own row.
import notes from '#lib/data/desk-notes.json';
import { causeOf, uniqueById, type Report, type Tenant } from '#lib/kb/causes';

export type Problem = 'parser' | 'hint' | 'one-day' | 'unplaced';

export const PROBLEM_TEXT: Record<Problem, string> = {
  parser: 'the shared parser reads day-first dates month first',
  hint: 'booking-v3 hints MM/DD/YYYY, then reads the date day first',
  'one-day': 'the invite lands one day off: same date, wrong day',
  unplaced: 'no tenant on file',
};

export type ProblemGroup = {
  problem: Problem;
  reports: number;
  tenants: number;
  firstSeen: string;
  lastSeen: string;
  // Reports intake tagged with something other than this problem.
  mistagged: number;
  // For one-day: the problem the desk files these reports under, by tenant.
  filedUnder: Problem[];
};

function group(problem: Problem, rs: Report[], filedUnder: Problem[] = []): ProblemGroup {
  const days = rs.map((r) => r.receivedAt.slice(0, 10)).sort();
  return {
    problem,
    reports: rs.length,
    tenants: new Set(rs.map((r) => r.tenant)).size,
    firstSeen: days[0],
    lastSeen: days[days.length - 1],
    mistagged: rs.filter((r) => r.meta.intakeTag !== problem).length,
    filedUnder,
  };
}

export function splitTicket(all: Report[], ticket: number, tenantOf: (r: Report) => Tenant | undefined) {
  const exported = all.filter((r) => r.mergedInto === ticket).length;
  const merged = uniqueById(all).filter((r) => r.mergedInto === ticket);
  const filed = (r: Report): Problem => causeOf(r, tenantOf(r)) ?? 'unplaced';

  const by = new Map<Problem, Report[]>();
  for (const r of merged) by.set(filed(r), [...(by.get(filed(r)) ?? []), r]);
  const groups = [...by.entries()].map(([p, rs]) => group(p, rs)).sort((a, b) => b.reports - a.reports);

  const moved = merged.filter((r) => notes.oneDayMove.includes(r.id));
  if (moved.length) groups.push(group('one-day', moved, [...new Set(moved.map(filed))]));

  return { exported, unique: merged.length, groups };
}
