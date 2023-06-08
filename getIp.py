import socket

# Configuración del servidor
HOST = '192.168.1.6' 
# Escucha en todas las interfaces de red
PORT = 1176  
# Puerto en el que se escuchará

# Crear el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Esperando conexión...")

# Aceptar la conexión del cliente
client_socket, address = server_socket.accept()

print("Cliente conectado:", address)

# Recibir la dirección IP privada enviada por el cliente
data = client_socket.recv(1024)
private_ip = data.decode()

print("Dirección IP privada recibida:", private_ip)

# Cerrar el socket del cliente y del servidor
client_socket.close()
server_socket.close()

