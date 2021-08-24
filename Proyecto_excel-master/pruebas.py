import numpy as np

largo = 100000
canales = 4
#####------------Creación de matrices----------######
num_canales = [a+1 for a in range(canales)]

Matriz_contadora = np.zeros((1,largo))
#matriz_2_2 = [[0.68,0.32],[0.75,0.25]]
#matriz_3_3 = [[0.1166,0.5072,0.3762],[0.0675,0.4682,0.4643],[0.1507,0.5208,0.3285]]
matriz_4_4 = [[0.4, 0.25, 0.25, 0.1],[0.06, 0.6, 0.3, 0.04],[0.07, 0.38, 0.45,0.1],[0.15, 0.3, 0.3, 0.25]]

print("\nmatriz de probabilidades")
for a in range(4):
    print(matriz_4_4[a])
print("")
def cambio_estado(evento,num_vect,cont):
    if evento > 0.000000001 and evento <= matriz_4_4[num_vect-1][0]: #se utiliza el vector 1 para verificar si habra transicion o se mantiene en el mismmo canal
        Matriz_contadora[0][cont] = num_canales[0]
    elif evento > matriz_4_4[num_vect-1][0] and evento <= (matriz_4_4[num_vect-1][0] + matriz_4_4[num_vect-1][1]):
        Matriz_contadora [0][cont] = num_canales[1]
    elif evento > (matriz_4_4[num_vect-1][0] + matriz_4_4[num_vect-1][1]) and evento <= (matriz_4_4[num_vect-1][0] + matriz_4_4[num_vect-1][1]+ matriz_4_4[num_vect-1][2]):
        Matriz_contadora [0][cont] = num_canales[2]
    else:
        Matriz_contadora [0][cont] = num_canales[3]

def canal_cambios(contador,num_rand):
    if Matriz_contadora[0][contador-1] == num_canales[0]: #se verifica si el ultimo canal en el que se encontraba el evento fue el canal1, en base a esto se ubica el vector correspondiente a ese evento
        cambio_estado(num_rand,int(Matriz_contadora[0][contador-1]),contador)
    elif Matriz_contadora[0][contador-1] == num_canales[1]: #igual que el anterior, se verifica si el canal anterior fue el canal2 y se procede de la misma forma
        cambio_estado(num_rand,int(Matriz_contadora[0][contador-1]),contador)
    elif Matriz_contadora[0][contador-1] == num_canales[2]:
        cambio_estado(num_rand,int(Matriz_contadora[0][contador-1]),contador)
    elif Matriz_contadora[0][contador-1] == num_canales[3]:
        cambio_estado(num_rand,int(Matriz_contadora[0][contador-1]),contador)
#####-------------Condiciones iniciales-------#######
Matriz_contadora[0][0]=num_canales[0]
for pivote in range(1,largo):
    evento = np.random.rand(1, 1)
    canal_cambios(pivote,evento)

matriz_total = []
for a in range(largo):
    matriz_total.append(int(Matriz_contadora[0][a]))

num_unos = [b for b in matriz_total if b == 1]
num_dos = [b for b in matriz_total if b == 2]
num_tres = [b for b in matriz_total if b == 3]
num_cuatro = [b for b in matriz_total if b == 4]

matri_result=[len(num_unos),len(num_dos),len(num_tres),len(num_cuatro)]
matriz_porcentaje = [a/largo for a in matri_result]
print("Eventos")
print(matriz_porcentaje)