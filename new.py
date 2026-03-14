import phonenumbers
from phonenumbers import geocoder, carrier 
from test import number
import folium
from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("api_key")
geo_api = OpenCageGeocode(key)

check_number = phonenumbers.parse(number)
location = geocoder.description_for_number(check_number, "en")
service_provider = carrier.name_for_number(check_number, "en")

query = str(location)
results = geo_api.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
map = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(map)
map.save("map.html")

print(location)
print(service_provider)
print("Approximate Country Center Coordinates:")
print(lat)
print(lng)