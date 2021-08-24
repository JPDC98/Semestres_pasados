#Iniciamos importanto las librerias necesarias para el proyecto
from tkinter import *
from tkinter import messagebox
import psycopg2

#Funiones de botones, peticiones y acciónes del programa

#-----------------------------------------Funciones del programa-------------------------------------------------
###FUNCIONES QUE SUBE A BASE DE DATOS
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
###FUNCIONES QUE RECIBE DE LA BASE DE DATOS
def datos_tabla():
    try:
        #Conectarme a base de datos existente
        conn = psycopg2.connect(user="postgres", database= "postgres", password= "123456", host= "127.0.0.1", port= "5432")
        #Activamos cursor
        conn.commit()
        cur = conn.cursor()
        cur.execute("SELECT*FROM examen22")
        rows = cur.fetchall()
        #cerramos cursor
        cur.close()
        #Terminar la conexión 
        conn.close()
    except:
        print("Conexión fallida")
    return rows

#----------------------------------------Funciones de los botones-------------------------------------------------
#FUNION QUE CREA VENTANA EMERGENTE PARA SALIR
def salir():
    valor = messagebox.askquestion("Salir","¿Quiere salir del programa?")
    if valor=="yes":
        raiz.destroy()
#DESPLIEGE DE DATOS NO EDITABLES EN LAS DIFERENTES PARTES DE LA PANTALLA
def despliege():
    pres = [[50,35,70],[40,25,55],[25,10,25]]
    pres_op = [pres[classs.get()][a] for a in range(3)]
    presios.config(text="Comida: Q{}.00  Bebida: Q{}.00  Pelicula: Q{}.00".format(pres_op[0],pres_op[1],pres_op[2]))
    cant_com = int(cantidad_com.get())
    cant_beb = int(cantidad_beb.get())
    cant_pel = int(cantidad_pel.get())
    return pres_op,classs.get(),cant_com,cant_beb,cant_pel,op1.get(),op2.get(),op3.get()
#FUNCION QUE CALCULA LOS DESCUENTOS
def calculat():
    try:
        pres_tr,cass_tra,cant_comtr,cant_bebtr,cant_peltr,opp1,opp2,opp3=despliege()
        sub = pres_tr[0]*cant_comtr+pres_tr[1]*cant_bebtr+pres_tr[2]*cant_peltr
        if cant_comtr+cant_bebtr+cant_peltr>=10 and cass_tra>0:
            des = 10
            total = sub*0.90
        elif cass_tra==0 and opp1>0 and opp2>0 and opp3>0:
            des = 5
            total= sub*0.95
        else:
            des = 0
            total = sub
        resultados.config(text="sub: Q{}.00   descuento {}%   total: Q{}".format(sub,des,total))
        table_insert(sub,des,total)
    except:
        print("Cantidad de información muy grande")
#FUNCION QUE DESPLIEGA LOS DATOS DE LA BASE DE DATOS EN UN TEXTO
def estado():
    try:
        datos_guar = datos_tabla()
        comentario.insert(INSERT," ID !SUBTOTAL!DESCUENTO!TOTAL\n")
        for linea in datos_guar:#Acá se muestra el resultado en pantalla de forma tabulada
            comentario.insert(INSERT,"{}\t{}\t{}%\t{}\n".format(linea[0],linea[1],linea[2],linea[3]))
    except:
        print("Algo salio mal en la conexión")

#FUNCION QUE BORRA LA BENTANA QUE MUESTRA LOS DATOS DE LA BASE DE DATOS
def borrar():
    comentario.delete(1.0,END)
#-----------------------------------------Construcción del programa-----------------------------------------------
raiz = Tk()
#--------------------------------------INICIO VARIABLES INERFASE GRÁFICA------------------------------------------
classs=IntVar()#variable usada radio_button
op1=IntVar()# --
op2=IntVar()# --|-->Variables check button
op3=IntVar()# --
cantidad_com=StringVar()  
cantidad_beb=StringVar() 
cantidad_pel=StringVar() 
#--------------------------------------FINAL VARIABLES INERFASE GRÁFICA-------------------------------------------
raiz.title("VENTA DE VOLETOS")
ventana = Frame(raiz)
ventana.pack()
#-----BOTONES-----
text_boton = Label(ventana,text="Acciones")
text_boton.grid(row=0,column=0)

boton_reporte=Button(ventana,text="Reporte",command=estado)
boton_reporte.grid(row=1,column=0,padx=4,pady=4)
boton_calcular=Button(ventana,text="Calcular",command=calculat)
boton_calcular.grid(row=2,column=0,padx=4,pady=4)
boton_limpiar=Button(ventana,text="Limpiar",command=borrar)
boton_limpiar.grid(row=3,column=0,padx=4,pady=4)
boton_salir=Button(ventana,text="Salir",command=salir)
boton_salir.grid(row=4,column=0,padx=4,pady=4)
#-----DESPLIEGE TEXTO-----
text_texto = Label(ventana,text="Listado")
text_texto.grid(row=0,column=1,columnspan=2)

comentario = Text(ventana,width=39,height=9)#controla tamaño
comentario.grid(row=1,column=1,columnspan=2,rowspan=4)#controla posición 
scrollvertical = Scrollbar(ventana,command=comentario.yview)
scrollvertical.grid(row=1,column=3,sticky="nsew",rowspan=4)
comentario.config(yscrollcommand=scrollvertical.set)
#----Despliege de presios en pantalla y otras etiquetas-----
resultados = Label(ventana)
resultados.grid(row=5,column=0,columnspan=4,padx=4,pady=4)
clase  = Label(ventana,text="Clases")
clase.grid(row=6,column=0,padx=4,pady=4)
servicio = Label(ventana,text="Servicios")
servicio.grid(row=6,column=1,padx=4,pady=4)
cantidad = Label(ventana,text="Cantidad")
cantidad.grid(row=6,column=2,padx=4,pady=4)
#------Despliege de Radio button-------
Radio_uno = Radiobutton(ventana,text="1° Clase",variable=classs,value=0,command=despliege)
Radio_uno.grid(row=7,column=0,padx=4,pady=4)
Radio_dos = Radiobutton(ventana,text="2° Clase",variable=classs,value=1,command=despliege)
Radio_dos.grid(row=8,column=0,padx=4,pady=4)
Radio_tres = Radiobutton(ventana,text="3° Clase",variable=classs,value=2,command=despliege)
Radio_tres.grid(row=9,column=0,padx=4,pady=4)
#------Despliege check button-------------
check_uno = Checkbutton(ventana,text="Comida",variable=op1,onvalue=1,offvalue=0,command=despliege)
check_uno.grid(row=7,column=1,padx=4,pady=4)
check_dos = Checkbutton(ventana,text="Bebida",variable=op2,onvalue=2,offvalue=0,command=despliege)
check_dos.grid(row=8,column=1,padx=4,pady=4)
check_tres = Checkbutton(ventana,text="Pelicula",variable=op3,onvalue=3,offvalue=0,command=despliege)
check_tres.grid(row=9,column=1,padx=4,pady=4)
#-----Despliege Spinbox-----------------
spin_un = Spinbox(ventana,from_=0,to=150,state='readonly',width=3,textvariable=cantidad_com)
spin_un.grid(row=7,column=2,padx=4,pady=4)
spin_un = Spinbox(ventana,from_=0,to=150,state='readonly',width=3,textvariable=cantidad_beb)
spin_un.grid(row=8,column=2,padx=4,pady=4)
spin_un = Spinbox(ventana,from_=0,to=150,state='readonly',width=3,textvariable=cantidad_pel)
spin_un.grid(row=9,column=2,padx=4,pady=4)
#-----Despliegue de presios-------------
presios = Label(ventana)
presios.grid(row=10,column=0,columnspan=4,padx=4,pady=4)

raiz.mainloop()
