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
    #print 'Retrieved',len(data),'characters'
    #print data
    output = ET.fromstring(data)
    
    short_code = ouput.findall('result')
    
    for item in short_code:
        print 'Short Country Code', item.find('short_name').text