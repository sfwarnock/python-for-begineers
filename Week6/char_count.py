#from urllib import urlopen

import urllib

url = ('https://www.google.com/')

fhand = urllib.urlopen(url)

size = 0

c_count = 0 #total character count.

while True:
    char = fhand.read(512)
    c_count = c_count + len(char)
    if c_count >= 3000:break
    print char
print c_count