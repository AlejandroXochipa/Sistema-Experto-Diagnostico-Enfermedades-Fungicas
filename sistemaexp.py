import tkinter 
from tkinter import messagebox
from tkinter import filedialog
#import tkinter.messagebox

raiz = tkinter.Tk()
raiz.title("Sistema Experto")
raiz.geometry("900x500")

#Componente Frame
#frame = tkinter.Frame(raiz)
#frame.config(bg="blue", width=400, height=300)

texto = "Sistema Experto Fungi"
etiqueta = tkinter.Label(raiz, text = texto) #Label
etiqueta.config(fg="black", bg="lightgrey", font=("Cortana", 30))
entrada = tkinter.Entry(raiz) #Entrada de texto
entrada.config(justify = "right")
#Entrada de Texto largo de varias lineas
entrada2 = tkinter.Text(raiz)
entrada2.config(width = 20, height = 10, font =("Verdana",15), padx=10, pady =10, fg="green", selectbackground = "lightgrey")

#Botones
def accion():
    print("Hola mundo")
boton = tkinter.Button(raiz, text="soy un boton", command =accion)
boton.config(fg="green", bg="pink")
#RadioButton
def seleccion():
    print(f"La oopcion seleccionada es: {opcion.get()}")

opcion = tkinter.IntVar()
radioboton = tkinter.Radiobutton(raiz, text= "opcion 1", variable=opcion, value=4, command=seleccion)

#CheckButton 
def verificar():
    if check1.get() == 1:
        print("Usted ha sido verificado")
    else:
        print("Usted no ha sido verificado")
check1 = tkinter.IntVar()
check = tkinter.Checkbutton(raiz, text="opcion 3", variable=check1, onvalue=1, offvalue=0, command=verificar)

#Messagebox (mostrar informacion)
#   -> Crear ventana de informacion 

def notificacion():
    #tkinter.messagebox.showinfo("Titulo", "Mensaje con la informacion")
    tkinter.messagebox.showinfo("Hola", "Mundo")
boton1 = tkinter.Button(raiz, text="Pulsar para aviso", command=notificacion)

#Messagebox para realizar una pregunta
def preguntar():
    resultado= tkinter.messagebox.askquestion("Titulo de la pregunta", "Quieres borrar el fichero")
    if resultado == "si":
        print("Si borra el fichero")
    else:
        print("No quiero")
boton3 = tkinter.Button(raiz,text="Pulsar para preguntar", command=preguntar)


#Abrir un fichero

def abrir_fichero():
    rutafichero = filedialog.askopenfilename(title="Abrir un fichero")
    print(rutafichero)

boton4 = tkinter.Button(raiz,text="Abrir fichero", command=abrir_fichero)


#Generar documentacion Docstrings cadenas para documentacion 

def saludar(nombre):
    """
    Esto sera un comentario de la funcion saludar
    Esta funcion recibira un parametro una cadena 
    Imprimira por pantalla por la terminal
    """
    print("Buenos dias" + nombre)

saludar("Antonio")
help(saludar)


entrada.pack()
boton1.pack()
boton3.pack()
boton4.pack()
#frame.pack()
check.pack()
entrada2.pack()
radioboton.pack()
boton.pack()
etiqueta.pack()


raiz.mainloop()