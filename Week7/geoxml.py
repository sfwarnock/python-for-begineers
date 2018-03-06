# Assignement 7
## Scott Warnock
## Google Geocoding

import urllib
import time
import xml.etree.ElementTree as ET
import re

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    time.sleep(2)
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    #print 'Retrieved',len(data),'characters'
    #print data
    tree = ET.fromstring(xmlstring)
    
    for line in tree:
        line = line.rstrip()
        x = re.findall('<short_name>([A-Z]+)<', line)
        for code in x:
            if re.findall('[A-Z]', code):print code
