import requests
import socket

# URL de la API Textbelt
url = 'https://textbelt.com/text'

# Número de teléfono del destinatario
numero_destinatario = '+50245472034'

# Función para obtener la dirección IP pública
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        public_ip = response.text
        return public_ip
    except requests.RequestException as e:
        print("Error al obtener la dirección IP pública:", e)
        return None

# Obtener la dirección IP pública
public_ip = get_public_ip()

if public_ip:
    # Convertir la dirección IP en un formato con espacios en lugar de puntos
    ip_con_espacios = public_ip.replace('.', ' ')

    # Mensaje a enviar
    mensaje = f'Mi dirección IP {ip_con_espacios}'

    # Parámetros de la solicitud
    params = {
        'phone': numero_destinatario,
        'message': mensaje,
        'key': 'textbelt',  # Clave de la API (opcional)
    }

    # Realizar la solicitud POST a la API Textbelt
    response = requests.post(url, data=params)

    # Obtener la respuesta de la API
    response_json = response.json()

    # Verificar el estado de la respuesta
    if response_json['success']:
        print('Mensaje enviado exitosamente.')
    else:
        print('Error al enviar el mensaje:', response_json['error'])
else:
    print("No se pudo obtener la dirección IP pública.")

