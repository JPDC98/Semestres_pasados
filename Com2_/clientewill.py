import socket
import threading

#apodo
nickname = input('Choose a nickname:')

#conetado al servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('169.254.203.134', 55555))

#escuchar el servidor y enviar el apodo
def receive():
    while True:
        try:   
            #recivir mensaje del servidor
            #si Nick envia el apodo
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
                
        except:
            #cerrar la coneccion cuando haya error
            print("Error ocurrido")
            client.close()
            break

#enviar mensaje al servido
def write():
    #ms = True     
    while True:
        message = "{} : {}".format(nickname, input(''))
        client.send(message.encode('ascii'))
        #ms = false

#temas de inicio para escuchar y escribir
recive_thread = threading.Thread(target=receive)
recive_thread.start

write_tread = threading.Thread(target=write)
write_tread.start