# Assignement 6
## Scott Warnock
## URL Reader

import urllib

url = ('https://www.google.com/')

html = urllib.urlopen(url)

size = 0

c_count = 0 #total character count.

site =' ' #store the fully downloaded site

while True:
    char = html.read(512)
    if (len(char)<1):
        break
    site = site + char
    c_count += len(char)
html.close()

site = site[:3000]

print site

print c_count