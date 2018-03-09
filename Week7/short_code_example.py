
import xml.etree.ElementTree as ET


data = '''<?xml version="1.0" encoding="UTF-8"?>
<GeocodeResponse>
 <status>OK</status>
 <result>
  <type>locality</type>
  <type>political</type>
  <formatted_address>Berlin, Germany</formatted_address>
  <address_component>
   <long_name>Berlin</long_name>
   <short_name>Berlin</short_name>
   <type>locality</type>
   <type>political</type>
  </address_component>
  <address_component>
   <long_name>Berlin</long_name>
   <short_name>Berlin</short_name>
   <type>administrative_area_level_1</type>
   <type>political</type>
  </address_component>
  <address_component>
   <long_name>Germany</long_name>
   <short_name>DE</short_name>
   <type>country</type>
   <type>political</type>
  </address_component>
  <geometry>
   <location>
    <lat>52.5200066</lat>
    <lng>13.4049540</lng>
   </location>
   <location_type>APPROXIMATE</location_type>
   <viewport>
    <southwest>
     <lat>52.3382340</lat>
     <lng>13.0883460</lng>
    </southwest>
    <northeast>
     <lat>52.6754542</lat>
     <lng>13.7611175</lng>
    </northeast>
   </viewport>
   <bounds>
    <southwest>
     <lat>52.3382340</lat>
     <lng>13.0883460</lng>
    </southwest>
    <northeast>
     <lat>52.6754542</lat>
     <lng>13.7611175</lng>
    </northeast>
   </bounds>
  </geometry>
  <place_id>ChIJAVkDPzdOqEcRcDteW0YgIQQ</place_id>
 </result>
</GeocodeResponse>'''

stuff = ET.fromstring(data)

address = stuff.findall('result/address_component')

for item in address:
        if item.find('type').text == 'country':
                print item.find('short_name').text
