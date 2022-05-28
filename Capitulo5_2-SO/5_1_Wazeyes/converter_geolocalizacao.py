from geopy.geocoders import Nominatim
'''Geopy is a python package that communicate with Google Maps or OpenStreetMap and you can use functionalities like latitude and longitude in your application '''

geolocator = Nominatim(user_agent="wazeyes")
location = geolocator.geocode("172 5th Avenue NYC")

print(location.address)
print((location.latitude, location.longitude))
