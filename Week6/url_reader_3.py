import urllib.request

url = ('http://int.lanl.gov/')

html = urllib.request.urlopen(url)

size = 0

c_count = 0 #total character count.

site =' ' #store the fully downloaded site

while True:
    char = html.read(512)
    if (len(char)<1):
        break
    site = site + str(char)
    c_count += len(char)
html.close()

site = site[:2999]

print (site)
print (c_count)