import urllib.parse

def dms_to_decimal(dms, direction):
    degrees, minutes, seconds = dms
    decimal = degrees + minutes/60 + seconds/3600
    if direction in ['S', 'W']:  # S = sul, W = oeste
        decimal *= -1
    return decimal

# Coordenadas de exemplo
latitude_dms = (8.0, 0.0, 59.39)
longitude_dms = (34.0, 50.0, 57.85)
latitude_direction = 'S'  # Indicando que é latitude sul
longitude_direction = 'W'  # Indicando que é longitude oeste

# Convertendo para graus decimais
latitude_decimal = dms_to_decimal(latitude_dms, latitude_direction)
longitude_decimal = dms_to_decimal(longitude_dms, longitude_direction)

# Formatar a latitude e longitude para a URL do Google Maps
google_maps_url = f"https://www.google.com/maps/search/?api=1&query={latitude_decimal},{longitude_decimal}"

# Codificar a URL corretamente
google_maps_url_encoded = urllib.parse.quote(google_maps_url, safe=':/?&=')

print("URL do Google Maps para a localização:", google_maps_url_encoded)
