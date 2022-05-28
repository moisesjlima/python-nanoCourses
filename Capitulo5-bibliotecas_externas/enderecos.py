from pygeocoder import Geocoder

endereco = 'avenida paulista, 100 sao paulo'

# Acessa uma informação na nuvem .reverse_geocode
resultado = Geocoder('HASH_API_GERADA').geocode(endereco)

print(resultado)
