import socket
import requests

# Función para obtener la dirección IP pública
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        public_ip = response.text
        return public_ip
    except requests.RequestException as e:
        print("Error al obtener la dirección IP pública:", e)
        return None

# Enviar la dirección IP pública a través de un socket
def send_ip_via_socket(ip, host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        client_socket.send(ip.encode())
        print("Dirección IP pública enviada correctamente.")
    except Exception as e:
        print("Error al enviar la dirección IP pública:", e)
    finally:
        client_socket.close()

# Obtener la dirección IP pública
public_ip = get_public_ip()

if public_ip:
    # Configurar el host y el puerto del servidor receptor
    host = "192.168.1.6"
    port = 1176

    # Enviar la dirección IP pública a través del socket
    send_ip_via_socket(public_ip, host, port)
else:
    print("No se pudo obtener la dirección IP pública.")

