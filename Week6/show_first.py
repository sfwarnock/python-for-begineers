import urllib
#url = raw_input('Enter full url: ')

url = 'https://www.google.com/'

doc = urllib.urlopen(url)

#char = doc.read()
#print char[0:3000]
#print len(char)

count = 0
while True:
    data = doc.read(512)
    if (len(data)<1):break
    count = len(data) + count
    print data[0:3000], count