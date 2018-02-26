#from urllib import urlopen

import urllib

url = ('https://www.google.com/')

fhand = urllib.urlopen(url)

size = 0

while True:
    data = fhand.read(512)
    size = size + len(data)
    if (len(data))<1: break
print size

fhand.close()