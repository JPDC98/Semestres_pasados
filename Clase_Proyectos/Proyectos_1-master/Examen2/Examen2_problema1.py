import psycopg2
repetir = True
llave = 0
def table_insert(nombre,edad,peso,altura,fecha,hora):
    try:
        conn = psycopg2.connect(user = "postgres",password = "123456",host = "127.0.0.1",port = "5432",database = "postgres")
        cur = conn.cursor()
        # Print PostgreSQL version
        cur.execute("""INSERT INTO public."examen12"(nombre,edad,peso,altura,fecha,hora)VALUES(%s,%s,%s,%s,%s,%s)""",(nombre,edad,peso,altura,fecha,hora))
        conn.commit()
        conn.close()
    except:
        print("Conexión fallida")

def datos_tabla(fechad):
    try:
        #Conectarme a base de datos existente
        conn = psycopg2.connect(user="postgres", database= "postgres", password= "123456", host= "127.0.0.1", port= "5432")
        #Activamos cursor
        conn.commit()
        cur = conn.cursor()
        cur.execute("SELECT nombre,fecha FROM examen12 WHERE fecha = %(fecha)s",{'fecha':fechad})
        rows = cur.fetchall()
        print("\nPasientes programados para el {}\n".format(fechad))
        for r in rows:
            print("nombre {} fecha {}".format(r[0],r[1]))
        #cerramos cursor
        cur.close()
        #Terminar la conexión 
        conn.close()
    except:
        print("Conexión fallida")

menu="""
-------------------------------------------------------------------------------------------------------
BIENVENIDO A CONTROL DE LA CLINICA
1) INGRESAR CITA
2) REVISAR CITAS EN FECHA DETERMINADA
3) EXIT
"""

while repetir==True:
    try:
        print(menu)
        select = int(input("Ingrese número correspondiente a la acción a realizar: "))
        if select==1:
            nump = int(input("Ingrese número de usuarios a ingresar: "))
            for a in range(nump):
                nom = input("Ingrese Nombre {}: ".format(a))
                ed = input("Ingrese Edad {}: ".format(a))
                pes = input("Ingrese Peso en libras {}: ".format(a))
                alt = input("Ingrese Altura en metros {}: ".format(a))
                fech = input("Ingrese Fecha formato dd/mm/aa {}: ".format(a))
                hor = input("Ingrese hora en formato 00:00 24 horas {}: ".format(a))
                table_insert(nom,ed,pes,alt,fech,hor)
        elif select==2: 
            fechr = input("Ingrese fecha en formato dd/mm/aa: ")
            datos_tabla(fechr) 

        elif select==3: 
            print("Gracias por usar nuestro programa")
            repetir=False
        else:
            print("Esta ingresando un campo inexistente")
    except:
        print("Algo salio mal")


    