# Inline the prerendered page's CSS and drop its JS, so the page opens as one file.
import sys, re, os
src, dst = sys.argv[1], sys.argv[2]
h = open(src).read(); base = os.path.dirname(src)
def css(m):
    return '<style>\n' + open(os.path.normpath(os.path.join(base, m.group(1)))).read() + '\n</style>'
h = re.sub(r'<link href="([^"]+\.css)" rel="stylesheet">', css, h)
h = re.sub(r'<link[^>]*rel="modulepreload"[^>]*>', '', h)
h = re.sub(r'<script\b.*?</script>', '', h, flags=re.S)
open(dst, 'w').write(h)
print(dst, len(h), 'bytes; links left:', re.findall(r'<link[^>]*>', h), 'scripts left:', h.count('<script'))
