from tkinter import*
from tkinter import messagebox#libreira utilizada para ventanas emergentes
from tkinter import ttk

#Funciones que hacen los botones
def boton():
    comentario.insert(INSERT,prueba)#inserta comentario en Texto

def borrar():
    comentario.delete(0,END)#Borra el texto enviado a mostrar

def imprimir():
    const=variable_radio.get()#Imprime valores de radio button
    if const==1:
        etiqueta.config(text="Has elegido hombre")
    else:
        etiqueta.config(text="Has elegido mujer")
def chechss():
    suma = op1.get()+op2.get()+op3.get()
    etiqueta2.config(text="{}".format(suma))

def mostrar():
    etiqueta3.config(text=palabra.get()+palabra2.get())

def salir():
    valor=messagebox.askquestion("Salir","¿Desea salir de la aplicación?")
    if valor=="yes":
        raiz.destroy()

#inicialización de metoods
raiz = Tk()
#----------------------------------------INICIO VARIABLES--------------------------------------------
variable_radio = IntVar()
op1 = IntVar()
op2 = IntVar()
op3 = IntVar()
palabra2 = StringVar()
palabra = StringVar()
prueba = """{} Hola como estamos
esta es una prueba para {}
ver 
si se puede {}
escribir asi
""".format(156,45,3)
#-----------------------------------------FIN VARIABLES---------------------------------------------

raiz.title("Pruebas")
#Frame = Hace como la ventana o escritorio donde estaran los botones y otras cosas que se desplegaran (área de trabajo)
frame_uno = Frame(raiz,width=1200,height=600)
frame_uno.pack()

#Entry = Este es un cuadro que nos permitira ingresar texto 
cuadroTexto=Entry(frame_uno,textvariable=palabra) 
cuadroTexto.grid(row=0,column=1)

#Labe = Este es un texto no editable que es parte de una interfaz
text_nombre = Label(frame_uno,text="Nombre:")
text_nombre.grid(row=0,column=0)

#Text = Es un cuadro de escritura preparado para mostrar gran cantidad de palabras o caracteres
comentario = Text(frame_uno,width=16,height=5)#controla tamaño
comentario.grid(row=1,column=0,columnspan=2)#controla posición 
scrollvertical = Scrollbar(frame_uno,command=comentario.yview)
scrollvertical.grid(row=1,column=2,sticky="nsew")
comentario.config(yscrollcommand=scrollvertical.set)

#Button= Despliega bontones que por medio de una fución se hará cierta acción 
boton_envio = Button(frame_uno,text='Enviar',command=boton)
boton_envio.grid(row=6,column=0)

boton_limpiar = Button(frame_uno,text='Limpiar',command=borrar)
boton_limpiar.grid(row=6,column=1)

boton_mostrar = Button(frame_uno,text='Mostrar',command=mostrar)
boton_mostrar.grid(row=6,column=2)

boton_salir = Button(frame_uno,text='Salir',command=salir)
boton_salir.grid(row=7,column=1)

#Esto es un extra a los botones que no es necesario ya es parte de las pruebas
etiqueta3 = Label(frame_uno)
etiqueta3.grid(row=7,column=0,columnspan=3)

#Radiobutton = Esta fucion nos permite seleccionar una de muchos botones
Radio_uno = Radiobutton(frame_uno,text="Maculino",variable=variable_radio,value=1,command=imprimir)
Radio_uno.grid(row=2,column=0)

Radio_dos = Radiobutton(frame_uno,text="Femenino",variable=variable_radio,value=2,command=imprimir)
Radio_dos.grid(row=2,column=1)

#Spinbox = Una caja de opcciónes en donde el usuario puede elegir el numero de opciones internas
spin_un = Spinbox(frame_uno,from_=0,to=10,state='readonly',textvariable=palabra2)#El parametro state permite anular, activar o solo editar por mause el spyn
spin_un.grid(row=0,column=2)

#Checkbutton = estos son opciones que no son excluyentes entre si
check_uno = Checkbutton(frame_uno,text="Opción 1",variable=op1,onvalue=1,offvalue=0,command=chechss)
check_uno.grid(row=4,column=0)

check_dos = Checkbutton(frame_uno,text="Opción 2",variable=op2,onvalue=1,offvalue=0,command=chechss)
check_dos.grid(row=4,column=1)

check_tres = Checkbutton(frame_uno,text="Opción 3",variable=op3,onvalue=1,offvalue=0,command=chechss)
check_tres.grid(row=4,column=2)

etiqueta2= Label(frame_uno)
etiqueta2.grid(row=5,column=0,columnspan=3)

#COMBOX = Esto perminte tener una lista predeterminada para que el usuraio escoja
country = ttk.Combobox(frame_uno, width = 27)#textvariable = n 
country['values'] = (' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',' Canada')   
country.grid(column = 0, row = 9) 
country.current()


#Estas ya son implementaciones extras de codigo ya utilizando las definiciones anteriores
etiqueta = Label(frame_uno)
etiqueta.grid(row=3,column=0,columnspan=3)



raiz.mainloop()