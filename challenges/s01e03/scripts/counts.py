# Final grouping: kb causes.ts rule (tenant + channel), except reports the desk read as a one-day move.
import json, sys, glob, os, collections as C
kb, out = sys.argv[1], sys.argv[2]
R = json.load(open(os.path.join(kb, 'src/lib/data/reports-4471.json')))
T = {t['handle']: t for t in (json.load(open(f)) for f in glob.glob(os.path.join(kb, 'src/lib/data/tenants/*.json')))}
one = set(json.load(open(os.path.join(kb, 'src/lib/data/desk-notes.json')))['oneDayMove'])
U = [r for r in {r['id']: r for r in R}.values() if r['mergedInto'] == 4471]
def problem(r):
    if r['id'] in one: return 'one-day'
    return 'hint' if r['channel'] == 'form' and T[r['tenant']]['form'] == 'booking-v3' else 'parser'
g = C.defaultdict(list)
for r in U: g[problem(r)].append(r)
res = {k: {'reports': len(v), 'tenants': len({r['tenant'] for r in v}), 'first': min(r['receivedAt'] for r in v)[:10],
           'last': max(r['receivedAt'] for r in v)[:10], 'intakeTag': dict(C.Counter(r['meta']['intakeTag'] for r in v)),
           'ids': sorted(r['id'] for r in v)} for k, v in g.items()}
json.dump(res, open(out, 'w'), indent=1)
print('rows', len(R), 'unique merged', len(U))
for k, v in res.items(): print(k, {x: y for x, y in v.items() if x != 'ids'})
