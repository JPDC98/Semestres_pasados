import psycopg2
repetir = True
llave = True
def table_insert(sub,des,total):
    try:
        conn = psycopg2.connect(user = "postgres",password = "123456",host = "127.0.0.1",port = "5432",database = "postgres")
        cur = conn.cursor()
        # Print PostgreSQL version
        cur.execute("""INSERT INTO public."examen22"(subtotal,descuento,total)VALUES(%s,%s,%s)""",(sub,des,total))
        conn.commit()
        conn.close()
    except:
        print("Conexión fallida")

def calculo(clas,com,beb,pel):
    try:
        llave=1
        precios = [[50,35,70],[40,25,55],[25,10,25]]
        pres_op = [precios[clas][a] for a in range(3)]
        sub = com*pres_op[0]+beb*pres_op[1]+pel*pres_op[2]
        if com+beb+pel > 10 and clas >0 :
            total = sub*0.9
            descu = '10%'
        elif clas==0 and com>0 and beb>0 and pel>0:
            total = sub*0.95
            descu = '5%'
        else:
            total = sub
            descu = '0%'
        return str(sub),descu,str(total)
    except:
        print("Algo salio mal")
    
menu = """-----------------------------------------------------------------
BIENVENIDO A NUESTRA AEREOLINEA\nEscoja una clases:\n1) Primera clase\n2) Segunda clase\n3) Tercera clase"""

menu2 = """-----------------------------------------------------------------
¿Qué acción desea realizar?\n1) Limpiar\n2) Salir\n3) Reporte\n4) Calcular"""

precios ="""-----------------------------------------------
Tipo servicio/tipo clase ! primera clase ! segunda clase ! tercera clase
         Comida                 50              40              25
         Bebida                 35              25              10
         Pelicula               70              55              25
"""

while repetir==True:
    try:
        print(precios)
        print(menu)
        clase = int(input("Ingrese clase a seleccionar: "))
        comida = int(input("Ingrese número de servcios de comida a pedir: "))       
        bebida = int(input("Ingrese número de servcios de bebida a pedir: "))   
        pelicula = int(input("Ingrese número de servcios de pelicula a pedir: "))
        print(menu2)
        select = int(input("Ingrese acción a realizar: "))
        if select==1:
            clase = 0
            comida = 0      
            bebida = 0 
            pelicula = 0          
        elif select==2:
            repetir = False
        elif select==3:
            print("\nUsted eligio viajar en {}° clase, sus ordenes son:\n".format(clase))
            print("{} de comida\n{} de bebida\n{} de pelicula\n".format(comida,bebida,pelicula)) 
            des = int(input("Desea clacular(1)/Desea salir sin guardar(2): "))
            if des == 1:
                subto,desc,tott=calculo(clase-1,comida,bebida,pelicula)
                table_insert(subto,desc,tott)
                print("El subtotal es:  {}".format(subto))
                print("El descuento es: {}".format(desc))
                print("El TOTAL es:     {}".format(tott)) 
                        
        elif select==4:
            subto,desc,tott=calculo(clase-1,comida,bebida,pelicula)
            table_insert(subto,desc,tott)
            print("El subtotal es:  {}".format(subto))
            print("El descuento es: {}".format(desc))
            print("El TOTAL es:     {}".format(tott))
        else:
            print("Usted selección una opción inexistente")
    except:
        print("Algo anda mal")