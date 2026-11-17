#!/usr/bin/env python3
"""Run once on a computer with internet, inside the site folder:  python3 download-images.py
Downloads every remote product image into assets/images/catalogue/ and rewrites the HTML to use the local copies."""
import re,glob,os,hashlib,urllib.request
os.makedirs('assets/images/catalogue',exist_ok=True)
pat=re.compile(r'https://(?:www\.aeromedsintl\.com|images\.unsplash\.com)/[^"\')\s]+')
cache={}
for f in glob.glob('*.html'):
    t=open(f,encoding='utf8').read()
    def rep(m):
        u=m.group(0)
        if u not in cache:
            ext='.jpg' if 'unsplash' in u else os.path.splitext(u.split('?')[0])[1] or '.png'
            name=re.sub(r'[^a-z0-9]+','-',u.split('?')[0].split('/imagess/')[-1].lower().rsplit('.',1)[0]).strip('-') if 'aeromeds' in u else 'photo-'+hashlib.md5(u.encode()).hexdigest()[:8]
            path='assets/images/catalogue/'+name+ext
            try:
                req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})
                open(path,'wb').write(urllib.request.urlopen(req,timeout=30).read()); cache[u]=path
            except Exception as e:
                print('FAILED',u,e); cache[u]=u
        return cache[u]
    n=pat.sub(rep,t)
    if n!=t: open(f,'w',encoding='utf8').write(n)
print('Downloaded',sum(1 for v in cache.values() if v.startswith('assets')),'of',len(cache),'images')
