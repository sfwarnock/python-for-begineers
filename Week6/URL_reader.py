# Assignement 6
## Scott Warnock
## URL Reader

from urllib import urlopen

#url = raw_input('Enter full url: ')

url = 'https://www.google.com/'

size = 0

while True:
    doc = urlopen(url).read(512)
    if len(doc)<1: break
    print doc
    
doc.close()

print doc[0:3000]
print len(doc)