# Assignement 7
## Scott Warnock
## Google Geocoding

import urllib
import time
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    time.sleep(2)
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'character'
    
    stuff = ET.fromstring(data)

    address = stuff.findall('result/address_component')

    for item in address:
        if item.find('type').text == 'country':
            print 'The country code is: ', item.find('short_name').text
        elif item.find('type').text == 'establishment':
            print 'The location you entered is not a country'
    break