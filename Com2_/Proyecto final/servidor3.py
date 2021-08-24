#!/usr/bin/env python

#Se importa el módulo
import socket
import numpy as np
from os import system
system("cls")

def cesarr(cadena):
    palabra = [chr(ord(a)-3) for a in cadena]
    return ''.join(palabra)

def descesarr(cadena):
    palabra = [chr(ord(a)+3) for a in cadena]
    return ''.join(palabra)

def otro1(cadena):
    palabra = [chr(ord(a)-5) for a in cadena]
    return ''.join(palabra)

def desotro1(cadena):
    palabra = [chr(ord(a)+5) for a in cadena]
    return ''.join(palabra)


salir=0
while salir==0:

    print('1) Recibir mensaje')
    print('2) Enviar mensaje a Manuel')
    print('3) Enviar mensaje a Willi')    
    print('5) Salir')
    opcion=int(input('ingrese una opcion: '))
    
    if opcion==1:
        system("cls")

        #instanciamos un objeto para trabajar con el socket
        ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
        #Puerto y servidor que debe escuchar
        ser.bind(("192.168.0.15", 8050))
 
        #Aceptamos conexiones entrantes con el metodo listen. Por parámetro las conexiones simutáneas.
        ser.listen(10)
 
        #Instanciamos un objeto cli (socket cliente) para recibir datos
        cli, addr = ser.accept()
        #Recibimos el mensaje, con el metodo recv recibimos datos. Por parametro la cantidad de bytes para recibir
        recibido = cli.recv(1024)
        #Si se reciben datos nos muestra la IP y el mensaje recibido
        print ("Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]))
        usuario = ''.join(addr[0])
        print (recibido.decode("UTf-8"))
        
        if  (usuario=="192.168.0.7"):
            print("mensaje de willi")
            palabra = [chr(ord(a)+5) for a in recibido.decode("UTf-8")]
            pal=''.join(palabra)
            print('El texto descifrado es: '+pal)
            


        if  (usuario=="192.168.0.13"):
            print("mensaje de Manuel")
            filas=0
            x=(recibido.decode("UTf-8")) #x es el tecto ingresado
            #print(x)
            #print(len(x))
            a=0 # a es la  variable de conteo a igualar a la longitud x

            columnas=3
            filas=int(len(x)/3)
            residuo= int(len(x))%3
            if  residuo !=0:
                filas=filas+1
            d=0 #variable para recorriodo de columnas
            e=0 #variable control de filas
            #print(filas)
            matriz=np.zeros([filas,columnas])
            mult=np.zeros([filas,columnas])
            matriz2=np.zeros([filas,columnas])

            while a < len(x):
                
                b=x[a] #b muestra datos de la matriz original
                if b =="a":
                    c=0 #c es variable de mi segunda matriz
                if b =="b":
                    c=1
                if b =="c":
                    c=2
                if b =="d":
                    c=3
                if b =="e":
                    c=4
                if b =="f":
                    c=5
                if b =="g":
                    c=6
                if b =="h":
                    c=7
                if b =="i":
                    c=8
                if b =="j":
                    c=9
                if b =="k":
                    c=10
                if b =="l":
                    c=11
                if b =="m":
                    c=12
                if b =="n":
                    c=13
                if b =="ñ":
                    c=14
                if b =="o":
                    c=15
                if b =="p":
                    c=16
                if b =="q":
                    c=17
                if b =="r":
                    c=18
                if b =="s":
                    c=19
                if b =="t":
                    c=20
                if b =="u":
                    c=21
                if b =="v":
                    c=22
                if b =="w":
                    c=23
                if b =="x":
                    c=24
                if b =="y":
                    c=25
                if b =="z":
                    c=26
                if b ==" ":
                    c=27
                if b ==".":
                    c=28
                if b ==",":
                    c=29
                if d>2:
                    d=0
                    e=e+1
                if e>filas:
                    e=0
                matriz[e,d]=c

                #print(b)
                #print(c)
                a=a+1
                d=d+1
                
            #llave=np.array([[24/22,-12/22,-2/22],[5/22,3/22,-5/22],[-4/22,2/22,4/22]])
            #llaveoriginal=np.array([[1,2,3],[0,4,5],[1,0,6]])
            
            #llave=np.linalg.inv(llaveoriginal)
            
            llave=np.array([[6,24,22],[26,21,1],[17,5,10]])
            
            mensaje=[]
            #grupo1=np.array([2,21,0])
            #print(matriz)
           #print("Texto cifrado:")
            i=0

            for i in range (filas):
                mult[i,:]=np.matmul(llave,matriz[i,:])#mult corresponde a la multiplicacion de cada grupo de 3 por la llave
                matriz2=mult[i,:]%27
                a=0
                while a<columnas:
                    b=matriz2[a] #b muestra datos de la matriz original
                    if b ==0:
                        c='a' #c es variable de mi segunda matriz
                    if b ==1:
                        c='b'
                    if b ==2:
                        c='c'
                    if b ==3:
                        c='d'
                    if b ==4:
                        c='e'
                    if b ==5:
                        c='f'
                    if b ==6:
                        c='g'
                    if b ==7:
                        c='h'
                    if b ==8:
                        c='i'
                    if b ==9:
                        c='j'
                    if b ==10:
                        c='k'
                    if b ==11:
                        c='l'
                    if b ==12:
                        c='m'
                    if b ==13:
                        c='n'
                    if b ==14:
                        c='ñ'
                    if b ==15:
                        c='o'
                    if b ==16:
                        c='p'
                    if b ==17:
                        c='q'
                    if b ==18:
                        c='r'
                    if b ==19:
                        c='s'
                    if b ==20:
                        c='t'
                    if b ==21:
                        c='u'
                    if b ==22:
                        c='v'
                    if b ==23:
                        c='w'
                    if b ==24:
                        c='x'
                    if b ==25:
                        c='y'
                    if b ==26:
                        c='z'
                    if b ==27:
                       c=' '
                    if b ==28:
                       c='.'
                    if b ==29:
                       c=','
                    mensaje.append(c)
                    a=a+1
                    
                i=i+1
            mensajecodificado=''.join(mensaje)
            print('Texto descifrado: '+mensajecodificado)

             


        
        #Devolvemos el mensaje al cliente
        cli.send("mensaje recibido".encode("UTF-8"))
        
        #Cerramos la instancia del socket cliente y servidor
        cli.close()
        ser.close()
        print("Conexiones cerradas")






    if opcion==2:
        system("cls")

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
       
            
       
        #mens = input("Ingrese palabra a enviar: ")

        filas=0
        x=(input("\nIngrese el texto a cifrar: ")) #x es el texto ingresado
        #print(x)
        #print(len(x))
        a=0 # a es la  variable de conteo a igualar a la longitud x

        columnas=3
        filas=int(len(x)/3)
        residuo= int(len(x))%3
        if  residuo !=0:
            filas=filas+1
        d=0 #variable para recorriodo de columnas
        e=0 #variable control de filas
        #print(filas)
        matriz=np.zeros([filas,columnas])
        mult=np.zeros([filas,columnas])
        matriz2=np.zeros([filas,columnas])

        while a < len(x):
            
            b=x[a] #b muestra datos de la matriz original
            if b =="a":
                c=0 #c es variable de mi segunda matriz
            if b =="b":
                c=1
            if b =="c":
                c=2
            if b =="d":
                c=3
            if b =="e":
                c=4
            if b =="f":
                c=5
            if b =="g":
                c=6
            if b =="h":
                c=7
            if b =="i":
                c=8
            if b =="j":
                c=9
            if b =="k":
                c=10
            if b =="l":
                c=11
            if b =="m":
                c=12
            if b =="n":
                c=13
            if b =="ñ":
                c=14
            if b =="o":
                c=15
            if b =="p":
                c=16
            if b =="q":
                c=17
            if b =="r":
                c=18
            if b =="s":
                c=19
            if b =="t":
                c=20
            if b =="u":
                c=21
            if b =="v":
                c=22
            if b =="w":
                c=23
            if b =="x":
                c=24
            if b =="y":
                c=25
            if b =="z":
                c=26
            if b ==" ":
                c=27
            if b ==".":
                c=28
            if b ==",":
                c=29
            if d>2:
                d=0
                e=e+1
            if e>filas:
                e=0
            matriz[e,d]=c

            #print(b)
            #print(c)
            a=a+1
            d=d+1
            
        llave=np.array([[1,2,3],[0,4,5],[1,0,6]])
        mensaje=[]
        #grupo1=np.array([2,21,0])
        #print(matriz)
        #print("Texto cifrado:")
        i=0

        for i in range (filas):
            mult[i,:]=np.matmul(llave,matriz[i,:])#mult corresponde a la multiplicacion de cada grupo de 3 por la llave
            matriz2=mult[i,:]%27
            a=0
            while a<columnas:
                b=matriz2[a] #b muestra datos de la matriz original
                if b ==0:
                    c='a' #c es variable de mi segunda matriz
                if b ==1:
                    c='b'
                if b ==2:
                    c='c'
                if b ==3:
                    c='d'
                if b ==4:
                    c='e'
                if b ==5:
                    c='f'
                if b ==6:
                    c='g'
                if b ==7:
                    c='h'
                if b ==8:
                    c='i'
                if b ==9:
                    c='j'
                if b ==10:
                    c='k'
                if b ==11:
                    c='l'
                if b ==12:
                    c='m'
                if b ==13:
                    c='n'
                if b ==14:
                    c='ñ'
                if b ==15:
                    c='o'
                if b ==16:
                    c='p'
                if b ==17:
                    c='q'
                if b ==18:
                    c='r'
                if b ==19:
                    c='s'
                if b ==20:
                    c='t'
                if b ==21:
                    c='u'
                if b ==22:
                    c='v'
                if b ==23:
                    c='w'
                if b ==24:
                    c='x'
                if b ==25:
                    c='y'
                if b ==26:
                    c='z'
                if b ==27:
                    c=' '
                if b ==28:
                    c='.'
                if b ==29:
                    c=','
                mensaje.append(c)
                a=a+1
                
            i=i+1
        mensajecodificado=''.join(mensaje)
        print('Texto cifrado: '+mensajecodificado)
       
        #Con el método send, enviamos el mensaje
        obj.send(mensajecodificado.encode('UTF-8'))
        recivido = obj.recv(1024)
        print(recivido.decode('UTF-8'))
        #Cerramos la instancia del objeto servidor
        obj.close()

        #Imprimimos la palabra Adios para cuando se cierre la conexion
        print("Conexión cerrada")

    if opcion==3:
        system("cls")

        #Variables
        host = '192.168.0.7'
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
        
        palabra = [chr(ord(a)-5) for a in mens]
        cod=''.join(palabra)
        
         #Con el método send, enviamos el mensaje
        obj.send(cod.encode('UTF-8'))
        recivido = obj.recv(1024)
        print(recivido.decode('UTF-8'))
        #Cerramos la instancia del objeto servidor
        obj.close()

        #Imprimimos la palabra Adios para cuando se cierre la conexion
        print("Conexión cerrada")


    if opcion==5:
        salir=1
