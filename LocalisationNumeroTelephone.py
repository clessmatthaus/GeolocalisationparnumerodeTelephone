import phonenumbers

import folium

from MonNumerodeTelephone import number

from phonenumbers import geocoder

key = 'da492b92235a4056b0d876dcfd93e5c4'

clessnumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(clessnumber, "fr")
print(yourLocation)

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "fr"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)

results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=8)

folium.Marker([lat, lng], popup=yourLocation).add_to((myMap))

myMap.save("myLocation.html")
