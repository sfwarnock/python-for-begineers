#from urllib import urlopen

import urllib

url = ('https://www.google.com/')

fhand = urllib.urlopen(url)

size = 0

c_count = 0 #total character count.

site =' '

while True:
    char = fhand.read(512)
    if (len(char)<1):
        break
    site = site + char
    c_count += len(char)
fhand.close()

site = site[:3000]

print site

print c_count