import json, sys, re, datetime as D, collections as C
M = 'January February March April May June July August September October November December'.split()
U = json.load(open(sys.argv[1]))
pat = re.compile(r'(?:(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) )?(\d{1,2}) (' + '|'.join(M) + ')')
kinds = C.Counter(); odd = []
for r in U:
    ds = pat.findall(r['body'])
    if len(ds) != 2:
        odd.append(('ndates=%d' % len(ds), r)); kinds['other'] += 1; continue
    (w1, d1, m1), (w2, d2, m2) = ds
    d1, d2 = int(d1), int(d2); m1, m2 = M.index(m1) + 1, M.index(m2) + 1
    if (d1, m1) == (m2, d2): k = 'flip'
    elif m1 == m2 and abs(d1 - d2) == 1: k = 'one-day'
    else: k = 'other'
    # weekday check against 2026
    wk = []
    for w, d, m in ((w1, d1, m1), (w2, d2, m2)):
        if w: wk.append(D.date(2026, m, d).strftime('%A') == w)
    kinds[k] += 1
    if k != 'flip' or (wk and not all(wk)):
        odd.append((k + (' weekday-mismatch' + str(wk) if wk and not all(wk) else ''), r))
print(kinds)
for k, r in odd: print(k, r['id'], r['tenant'], r['channel'], '|', r['body'])
