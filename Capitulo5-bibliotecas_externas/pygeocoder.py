from pygeocoder import Geocoder

endereco = "Shopping Taboão - Rodovia Régis Bittencourt - Jardim Helena, Taboão da Serra - SP"
print(Geocoder('HASH_API_GERADA').geocode(endereco).coordinates)
