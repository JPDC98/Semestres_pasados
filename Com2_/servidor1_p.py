import socket

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.bind(('localhost',8000))
mi_socket.listen(5)
sock.setblocking(False)


while True:
    conexion, addr = mi_socket.accept()
    conn.setblocking(False)
    lista_clientes
    print("nueva conexion establecida")
    print (addr)

    peticion = conexion.recv(1024)
    print(peticion)
    conexion.send("Hola, te saludo desde el servidor".encode('UTF-8'))

    conexion.close()