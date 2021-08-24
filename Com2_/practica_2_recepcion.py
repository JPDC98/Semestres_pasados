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

def deteccion_repeticion(cadena_2):  
    bin_num = [int(numero) for numero in cadena_2] 
    lista_inf = [bin_num[desp]+bin_num[desp+1]+bin_num[desp+2] for desp in range(0,21,3)]  
    lista_final = [0 if ver <= 1 else 1 for ver in lista_inf]
    print("\n\nLa cadena correcta es:\n")
    print(lista_final)
    exponentes = [64,32,16,8,4,2,1]
    pre_letra = [lista_final[uno]*exponentes[uno] for uno in range(7)]
    numero_letra = pre_letra[0]+pre_letra[1]+pre_letra[2]+pre_letra[3]+pre_letra[4]+pre_letra[5]+pre_letra[6]
    print("\n\nLa letra es:")
    return chr(numero_letra)
#----------------------------------------------Codigo-------------------------------------------------------------------------
opcion = int(input("\n\nIngrese (1) para corrección hamming o (2) para corrección por repetición: "))
cadena_bit = input("\nIngrese cadena de bit: ")
if opcion == 1:
    print(deteccion_hamming(cadena_bit)) 
else:    
    print(deteccion_repeticion(cadena_bit))