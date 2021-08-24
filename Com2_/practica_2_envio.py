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
#------------------------------------------CODIGOOOO----------------------------------------------------    
#--------------------------------------SE INGRESA UNA LETRA---------------------------------------------
letra = input("-------------------------------------------------------------\n\nIngrese una palabra (sin espacios): ")
lista_resultados = [cadena_hamming(variable) for variable in letra]
lista_cadena  = [lista_resultados[pos][desli] for pos in range(len(lista_resultados)) for desli in range(11)]
####----------------------------------------Monitoreo visual de resultados---------------------------------------
print("\n\nLas cadenas codificadas con hamming es:\n")
[print(lista_resultados[pivote]) for pivote in range(len(lista_resultados))]### ----------------cada uno de los resultados por separado
print("\nLa cadena a enviar en hamming es:\n")
print(lista_cadena)
