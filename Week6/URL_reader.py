# Assignement 6
## Scott Warnock
## URL Reader

from urllib import urlopen

#url = raw_input('Enter full url: ')

url = 'http://krqe.com/'

doc = urlopen(url).read()
print doc[0:3000]
print len(doc)