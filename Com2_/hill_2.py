import numpy as np 

palabra = input("\ningrese palabra incriptada: ")
print("\n"+palabra+"\n")
numero = [ord(entrada)-48 for entrada in palabra]
filas = int(len(numero)/3)
matriz_palabra = np.array(numero).reshape(filas,3)
print("\nIngrese llave por favor: "),print("")
m = []
#[[5, 8, 1],[2, 3, 4],[9, 6,  2]]
for a in range(3):
    m.append([])
    for b in range(3):
        valor =int(input("Igrese parametro m[{}][{}]: ".format(a+1,b+1)))
        m[a].append(valor)
matriz = np.array(m)
matriz_inv = np.linalg.inv(matriz)
mul_mat = matriz_inv*151
mul_mat = matriz_inv*(151*455)
mul_list = [round(mul_mat[uno][dos])%76 for uno in range(3) for dos in range(3)]
matriz_llave = np.array(mul_list).reshape(3,3)
matriz_decode = [np.array(np.dot(matriz_palabra[camb,:],matriz_llave)).tolist() for camb in range(filas)]
decode_list = [matriz_decode[tre][cuat] for tre in range(filas) for cuat in range(3)]
decode_mod = [decode_list[cin]%76 for cin in range(len(decode_list))]
print(decode_mod)
decode_esp = [-16 if sei==75 or sei == 0 else sei for sei in decode_mod]
decode_pal = [chr(siet+48) for siet in decode_esp]
palabra_fin =''.join(decode_pal)
print("\nLa palabra decodificada es: ")
print("\n"+palabra_fin)