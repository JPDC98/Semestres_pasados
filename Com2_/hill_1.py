import numpy as np 
#-----------------------------------------------CIFRADO--------------------------------------------------
palabra = input("Ingrese palabra a cifrar: ")
print("-------------------CIFRADO----------------------")
print(palabra+"\n")
numero = [ord(entrada)-48 for entrada in palabra]
cifrado_p1 = [75 if mov==-16 else mov for mov in numero]
corrector = 0
while corrector == 0:# Esto pondra 0 en los espacios faltantes del mensaje
    if len(cifrado_p1)%3 != 0:
        cifrado_p1 = cifrado_p1 + [76]
    else: 
        corrector = 1     
filas = int(len(cifrado_p1)/3)
print("La clave es:")
llave = np.array([[5, 8, 1],[2, 3, 4],[9, 6,  2]])
print(llave)
matriz = np.array(cifrado_p1).reshape(filas,3)
matriz_code = [np.array(np.dot(matriz[pivote,:],llave)).tolist() for pivote in range(filas)]
lista_lista = [(matriz_code[uno][dos])%76 for uno in range(filas) for dos in range(3)]
pal_cifra = [chr(num+48) for num in lista_lista]
union = ''.join(pal_cifra)
print("\n\npalabra cifrada es\n")
print(union)