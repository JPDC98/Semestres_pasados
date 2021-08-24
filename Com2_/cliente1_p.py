import socket

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM=)
#mi_skt.connect(('169.254.203.134',8000))
mi_skt.connect(('localhost',8000))

mi_skt.send("Hola desde el cliete".encode('UTF-8'))
respueta = mi_skt.recv(1024)

print("La respuesta es:")
print(respueta.decode('UTF-8'))

mi_skt.close()