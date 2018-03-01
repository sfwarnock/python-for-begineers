# Assignement 6
## Scott Warnock
## URL Reader

# https://www.google.com/

import urllib

try:
    url = raw_input('Enter full url: ')
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

    site = site[:2999]

    print '\n', site, '\n', '\nThe site you entered contains '+ str(c_count) + ' characters.',

except:
    print 'The URL you entered does not work.'