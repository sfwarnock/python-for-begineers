import urllib

fhand = urllib.urlopen('http://krqe.com/')
for line in fhand:
    data = fhand.read(512)
    line = data.strip()
    print line