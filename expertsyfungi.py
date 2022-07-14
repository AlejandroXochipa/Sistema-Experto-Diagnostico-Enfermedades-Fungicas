from experta import*
#import tkinter
from tkinter import* 
from PIL import ImageTk, Image


raiz = Tk()
raiz.title("Sistema Experto Fungi")
raiz.geometry('933x700')

frame = Frame(master = raiz, width = 933, height=700, bg="white")
frame.pack()
frame.propagate(0)
#frame.config(width = 933, height=700, bg="white")

imagen1 = PhotoImage(file="Imagenes/Principal.png")
imagen1.config(width =933, height=750)
#lb_imagen = Label(master = frame, image=imagen1).place(x=0, y=0)
labelx = Label(master = frame, image=imagen1)
labelx.place(x=0, y=0)
labelx.pack(side="bottom", fill="both", expand="yes")
#labelx.pack()

label2 = Label(master=labelx,text="Bienvenido a UPFungi" )
label2.config(bg="white",fg="black", font=("Bookman Old Style", 40, "bold"))
label2.pack(expand=0, fill=Y)

label3 = Label(master = labelx, text="Es prueba del segundo Label")

label3.pack()



print(type(labelx))

#label_usuario = Label(frame, text="Ingrese su usuario")
#label_usuario.grid_propagate(False)
#label_usuario.grid(row=1, column=0)

#frame.pack()
raiz.mainloop()
