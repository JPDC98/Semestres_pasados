#!/usr/bin/env python

#Variables
host = '192.168.0.13'
port = 8050
#Se importa el módulo
import socket

#Creación de un objeto socket (lado cliente)
obj = socket.socket()
 
#Conexión con el servidor. Parametros: IP (puede ser del tipo 192.168.1.1 o localhost), Puerto
obj.connect((host, port))
print("Conectado al servidor")
 
#Creamos un bucle para retener la conexion
#Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
mens = input("Ingrese palabra a enviar: ")
#Con el método send, enviamos el mensaje
obj.send(mens.encode('UTF-8'))
recivido = obj.recv(1024)
print(recivido.decode('UTF-8'))
#Cerramos la instancia del objeto servidor
obj.close()

#Imprimimos la palabra Adios para cuando se cierre la conexion
print("Conexión cerrada")