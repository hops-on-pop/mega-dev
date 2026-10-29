import json, sys, collections as C, glob, os
kb = sys.argv[1]
R = json.load(open(os.path.join(kb, 'src/lib/data/reports-4471.json')))
T = {json.load(open(f))['handle']: json.load(open(f)) for f in glob.glob(os.path.join(kb, 'src/lib/data/tenants/*.json'))}
notes = json.load(open(os.path.join(kb, 'src/lib/data/desk-notes.json')))
print('rows', len(R))
ids = C.Counter(r['id'] for r in R)
dups = {i: n for i, n in ids.items() if n > 1}
print('dup ids', len(dups), dups)
for i in dups:
    rows = [r for r in R if r['id'] == i]
    same = all(json.dumps(x, sort_keys=True) == json.dumps(rows[0], sort_keys=True) for x in rows)
    if not same: print('  DIFFERENT CONTENT', i, rows)
U = list({r['id']: r for r in R}.values())  # last wins, like JS Map
print('unique', len(U))
print('mergedInto', C.Counter(r['mergedInto'] for r in U))
print('channel', C.Counter(r['channel'] for r in U))
print('tenant', C.Counter(r['tenant'] for r in U))
print('missing tenants', set(r['tenant'] for r in U) - set(T))
print('intakeTag', C.Counter(r['meta']['intakeTag'] for r in U))
print('browserLocale', C.Counter(r['meta']['browserLocale'] for r in U))
print('keys', C.Counter(tuple(sorted(r)) for r in U))
print('meta keys', C.Counter(tuple(sorted(r['meta'])) for r in U))
print('receivedAt range', min(r['receivedAt'] for r in U), max(r['receivedAt'] for r in U))
print('mergedAt none', sum(1 for r in U if not r['mergedAt']))
V3 = {h for h, t in T.items() if t['form'] == 'booking-v3'}
def cause(r):
    t = T.get(r['tenant'])
    if not t: return 'unplaced'
    return 'hint' if r['channel'] == 'form' and t['form'] == 'booking-v3' else 'parser'
print('v3 tenants', V3)
print('causeOf', C.Counter(cause(r) for r in U))
print('cause x intakeTag', C.Counter((cause(r), r['meta']['intakeTag']) for r in U))
print('form channel by tenant', C.Counter(r['tenant'] for r in U if r['channel']=='form'))
print('oneDayMove', [(r['id'], cause(r), r['body']) for r in U if r['id'] in notes['oneDayMove']])
json.dump(sorted(U, key=lambda r: r['id']), open(sys.argv[2], 'w'), indent=0, ensure_ascii=False)
