from tkinter import *
import logicaexperto5 as le


class Diagnostico():
    def __init__(self, ventana1):
        self.vent2 = ventana1
        self.vent2.title("Sistema Experto Fungi")
        self.vent2.geometry('933x700')


def abrir_ventana_dg():
    # ventana.withdraw()

    #prueba = le.Prueba()
    #prueba.set_pregunta("Hola paquito")
    # print(le.pb.get_pregunta())

    ventana1 = Tk()
    app = Diagnostico(ventana1)
    bg = PhotoImage(file="Imagenes/Diagnostico.png")
    label = Label(ventana1, image=bg)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    # label_pre = Label(ventana1, text="A continuación se te pide contestar una serie de preguntas:", font=("Baskerville Old Face", 20), fg="black", bg = '#AECC36')
    #label_pre.grid(pady=20, padx=80)
    # print(le.pregunta)
    unframe = LabelFrame(ventana1, bg='#00983C', text="Diagnóstico")
    unframe.config(font=("Baskerville Old Face", 25), bd=5)
    unframe.config(width=509, height=560)
    unframe.place(y=85, x=200)

    label_usu = Label(unframe, text="SU CULTIVO SUFRE DE" + le.pb.get_disganostico(), font=("Baskerville Old Face", 15))
    label_usu.config(bg='#00983C')
    #label_usu.grid(row=1, column=0, pady=10)
    label_usu.place(x=10, y=10, anchor="w")
    #unframe.config(width = 509, height=560)
    #label_pre.grid(pady=20, padx=80)
    #var = StringVar()

    #radio_boton = Radiobutton(ventana1, text="Si", variable=var, value="si", command=lambda: Mostrar(var.get(), ventana1))
    #radio_boton2 = Radiobutton(ventana1, text="No", variable=var, value="no", command=lambda: Mostrar(var.get(), ventana1))

    # Trae la pregunta
    # label_pregunta = Label(ventana1, text= "¿" + Pregunta() + "?" , font=("Baskerville Old Face", 20), fg="black", bg = '#AECC36')
    #label_pregunta.grid(pady=50, padx=80)

    # Radio Buttom - Responde la pregunta
    #var_radio = StringVar()
    # app.set_respuesta(var_radio)

    # print(var_radio)
    #radio_boton.grid(pady=70, padx=80)
    #radio_boton2.grid(pady=75, padx=80)
    # variable_re.set_respuesta(var_radio)
    # print(variable_re.get_respuesta)
    # print(var_radio.get())

    #label_pre.place(y=20, x=165)
    # label.pack()
    ventana1.mainloop()

# abrir_ventana()
