import numpy as np
from os import system
salir=0
system("cls")

def cadena_hamming(numero): 
    binario = bin(ord(numero)) # de caracter a binario
    separacion = [variable for variable in binario] # se separa en variables 
    limite = len(separacion)
    binario_cadena = separacion[2:limite] #quitar caracteres innecesarios
    binario_numeros = [int(pivote) for pivote in binario_cadena]#convertir caracteres a numeros 
    suma = []
    suma.append(binario_numeros[0]+binario_numeros[1]+binario_numeros[3]+binario_numeros[4]+binario_numeros[6])
    suma.append(binario_numeros[0]+binario_numeros[2]+binario_numeros[3]+binario_numeros[5]+binario_numeros[6])
    suma.append(binario_numeros[1]+binario_numeros[2]+binario_numeros[3])
    suma.append(binario_numeros[4]+binario_numeros[5]+binario_numeros[6])
    paridad = [0 if elemento%2 == 0 else 1 for elemento in suma]#analisis matematico de los bits de paridad
    binario_numeros.insert(0,paridad[0])#--!
    binario_numeros.insert(1,paridad[1])#  !-->  CONCATENACION FINAL
    binario_numeros.insert(3,paridad[2])#  !
    binario_numeros.insert(7,paridad[3])#--!
    return binario_numeros

def deteccion_hamming(cadena):
    bin_num = [int(numero) for numero in cadena]
    suma = []
    exponentes = [1,2,4,8,16,32,64]
    suma.append(bin_num[0]+bin_num[2]+bin_num[4]+bin_num[6]+bin_num[8]+bin_num[10])
    suma.append(bin_num[1]+bin_num[2]+bin_num[5]+bin_num[6]+bin_num[9]+bin_num[10])
    suma.append(bin_num[3]+bin_num[4]+bin_num[5]+bin_num[6])
    suma.append(bin_num[7]+bin_num[8]+bin_num[9]+bin_num[10])
    paridad = [0 if elemento%2 == 0 else 1 for elemento in suma]#analisis matematico de los bits de paridad
    pre_suma = [paridad[pivote]*exponentes[pivote] for pivote in range(4)]
    suma_total = pre_suma[0]+pre_suma[1]+pre_suma[2]+pre_suma[3]-1
    truco = bin_num[suma_total]+1
    if suma_total <= 0:
        print("todo correcto")
    else: 
        residuo = truco%2
        if residuo != 0:
            bin_num[suma_total] = 1
        else:
            bin_num[suma_total] = 0  
    letra = [bin_num[10],bin_num[9],bin_num[8],bin_num[6],bin_num[5],bin_num[4],bin_num[2]]
    pre_letra = [letra[uno]*exponentes[uno] for uno in range(7)]
    numero_letra = pre_letra[0]+pre_letra[1]+pre_letra[2]+pre_letra[3]+pre_letra[4]+pre_letra[5]+pre_letra[6]
    return chr(numero_letra)

while salir==0:
    try:
        print('\n----Cifrado Hill----')
        print('(1) Iniciar programa ')
        print('(2) salir ')
        opcion=int(input('ingrese una opcion: '))
    
    

        if opcion==1:

            #system("cls")
            filas=0
            x=(input("\nIngrese el texto a cifrar: ")) #x es el tecto ingresado
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
            print("mensaje a enviar en codigo hamming: ")
            mensaje_envio = [cadena_hamming(pal) for pal in mensajecodificado]
            print(mensaje_envio)
            print("decodificación de rafaga de bints")
            palabra_deco = [deteccion_hamming(mensaje_envio[paso]) for paso in range(len(mensaje_envio))]
            print(palabra_deco)
            pal_final = ''.join(palabra_deco)
            print("palabra enviada finalmente")
            print(pal_final)
        if opcion==2:
            salir=1
    except:
        print('\ningrese una opcion valida')