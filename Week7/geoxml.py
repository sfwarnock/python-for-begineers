# Assignement 7
## Scott Warnock
## Google Geocoding

import urllib
import time
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    time.sleep(6)
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)
    
    results = tree.findall('result')
    for item in results:
        print 'address_component'.find('short_name').text
    break