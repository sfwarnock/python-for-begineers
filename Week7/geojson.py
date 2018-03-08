# Assignement 7
## Scott Warnock
## Google Geocoding

import urllib
import json
import time


serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    time.sleep(2)
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    uh = urllib.urlopen(url)
    data = uh.read()


    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        continue
    
    results = js['results'][0]
    code = js["results"][0]["address_components"][2]["short_name"]
    print 'Country Code:', code