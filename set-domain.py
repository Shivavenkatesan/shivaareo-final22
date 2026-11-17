#!/usr/bin/env python3
"""Usage: python3 set-domain.py aeroprimemed.com [enquiries@aeroprimemed.com]
Replaces the YOURDOMAIN.COM placeholders (canonicals, sitemap, robots, contact form, legal pages)."""
import sys,glob,os
if len(sys.argv)<2: sys.exit(__doc__)
dom=sys.argv[1].lower().replace('https://','').replace('http://','').replace('www.','').strip('/')
mail=sys.argv[2] if len(sys.argv)>2 else 'info@'+dom
files=[f for f in glob.glob('**/*',recursive=True) if os.path.isfile(f) and f.endswith(('.html','.php','.xml','.txt'))]
for f in files:
    t=open(f,encoding='utf8').read()
    n=t.replace('info@YOURDOMAIN.COM',mail).replace('YOURDOMAIN.COM',dom)
    if n!=t: open(f,'w',encoding='utf8').write(n)
print('Domain set to',dom,'| enquiries go to',mail)
