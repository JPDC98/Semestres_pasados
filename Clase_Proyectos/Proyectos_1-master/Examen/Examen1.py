from math import pi
import psycopg2
repetir = True
llave = 0
archivo = open("Resultado.txt","a")
def table_insert(oper,res):	
	try:
	    connection = psycopg2.connect(user = "postgres",password = "123456",host = "127.0.0.1",port = "5432",database = "postgres")
	    cursor = connection.cursor()
	    # Print PostgreSQL version
	    cursor.execute("""INSERT INTO public."examen"(operacion,resultado)VALUES(%s,%s)""",(oper,res))
	    connection.commit()
	    connection.close()
	except (Exception, psycopg2.Error) as error :
	    print(error)
	    print("Conexcion fallida, intente de nuevo")
menu = """---------------------------------------------------------------------------------------
Elije programa a ejecutar​ \n\n​ 1)Peso de personas​ \n​ 2)Diferencia entre cuadrados​ \n​ 3)Num primos
  4)Fibonacci​ \n​ 5)Cono​\n​ 6) Exit"""
while repetir == True:
    try:
        print(menu)
        llave = int(input("Ingrese número correspondiente al programa a ejecutar: "))
        def errores():
            print("\n Usted no esta ingresando un número \n")
            archivo.write("Error usuario \n")

        if llave == 6:
            print("\nGracias por usar nuestro programas\n")
            archivo.close()
            repetir = False
        elif llave == 1:
            try:
                personas = int(input("Ingrese el número de personas a ingresar: "))
                matriz = []
                conteo1 = 0
                conteo2 = 0
                conteo3 = 0
                conteo4 = 0
                mujeres = 0
                hombres = 0

                for i in range(personas):
                    matriz.append([])
                    for j in range(3):
                        despliege = ["Ingrese genero Masculino(1) Femenino(2)","Ingrese peso[lb]","Ingrese altura[m]"]
                        print(despliege[j])
                        valor = float(input("Dato: "))
                        matriz[i].append(valor)
                        if j==0 and valor ==1:
                            sexo = 1
                            altura = 1
                        elif j==0 and valor==2:
                            sexo=2
                            altura=2
                        elif j==2 and sexo==1:
                            conteo1+=valor
                            promedio_peso_hombres=conteo1/hombres
                        elif j==2 and sexo==2:
                            conteo2+=valor
                            promedio_peso_mujer= conteo2/mujeres
                        elif j==1 and altura ==1:
                            conteo3+=valor
                            hombres+=1
                            promedio_altura_hombres= conteo3/hombres
                        elif j==1 and altura ==2:
                            conteo4+=valor
                            mujeres+=1
                            promedio_altura_mujer = conteo4/mujeres
                print("\n    Genero M(1)/F(2)         Peso      Altura")
                for personas in matriz:
                    print("[", end ="")
                    for elemento in personas:
                        print("{:8.2f}".format(elemento), end="")

                    print("]\n")
                print("El promedi de la altrua masculina es: {}".format(promedio_altura_hombres))
                archivo.write("El promedio de la alturma masculina es: "+str(promedio_altura_hombres)+"\n") 
                table_insert("Promedios",str(promedio_altura_hombres))  
                print("El promedi de la altrua femenina es: {}".format(promedio_altura_mujer))
                archivo.write("El promedio de la alturma femenina es: "+str(promedio_altura_mujer)+"\n")
                table_insert("Promedios",str(promedio_altura_mujer))  
                print("El promedi del peso masculino es: {}".format(promedio_peso_hombres))
                archivo.write("El promedio del peso masculino es: "+str(promedio_peso_hombres)+"\n")
                table_insert("Promedios",str(promedio_peso_hombres))  
                print("El promedi del peso femenina es: {}".format(promedio_peso_mujer))
                archivo.write("El promedio del peso femenino es: "+str(promedio_peso_mujer)+"\n")   
                table_insert("Promedios",str(promedio_peso_mujer))                              
            except ValueError:         
                errores()
        elif llave==2:
            try:
                print("La diferencia de la suma de los cuadrados de los primeros 100 números naturales y el cuadrado de la suma es: ")
                suma_cuadrados = [a**2 for a in range(1,101)]
                suma_nat = [b for b in range(1,101)]
                sum_cua=0
                sum_nat=0
                for un in range(len(suma_cuadrados)):
                    sum_cua = sum_cua + suma_cuadrados[un]
                for do in range(len(suma_nat)):
                    sum_nat = sum_nat + suma_nat[do]
                result = sum_cua-sum_nat
                print(result)
                archivo.write("La diferencia cuadrados y naturales es: "+str(result)+"\n")
                table_insert("Diferencia",str(result))
            except:
                errores()
        elif llave==3:
            try:
                numero = int(input("ingrese numero: "))
                primos = [primo for primo in range(1,numero+1) if numero%primo == 0]
                print("\nEl número primo más grande es:")
                print(max(primos))
                archivo.write("El número primo más grande es: "+str(max(primos))+"\n")
                table_insert("Maximo",str(max(primos)))  
            except:
                errores()
        elif llave==4:  
            try:  
                num = int(input("ingrese número: "))
                m = []
                a, b = 0,1
                while a < num:
                    m.append(a)
                    a, b = b, a+b
                print("La serie de fibonacci es: \n{}".format(m))
                lista_m = [str(m[cua]) for cua in range(len(m))]
                archivo.write("La serie fibonacci es: "+str(''.join(lista_m))+"\n")
                table_insert("Fibonacci",str(''.join(lista_m)))  
            except:
                errores()
        elif llave==5:
            try:
                oraciones = ["Radio: ","Generatriz: ","Altrua: "]
                datos = [float(input(oraciones[tre])) for tre in range(3)]
                area_bas = pi*(datos[0]**2)
                area_lat = pi*datos[0]*datos[1]
                area_tot = area_bas+area_lat
                volumen = (area_bas*datos[2])/3
                print("El área de la base es: {}".format(area_bas))
                table_insert("A_base",str(area_bas)) 
                print("El área lateral es: {}".format(area_lat))
                table_insert("A_lat",str(area_lat)) 
                print("El área total es: {}".format(area_tot))
                table_insert("A_total",str(area_tot)) 
                print("El volumen es: {}".format(volumen))
                table_insert("Volumen",str(volumen1)) 
                archivo.write("El area de base,lateral,total y volumen es respectivamente: {};{};{};{}\n".format(area_bas,area_lat,area_tot,volumen))
            except:
                errores()
        else:
            errores()        
    except:
        errores()    