from tkinter import messagebox
from tkinter import *
from experta import *
#import diagnostico as dg
#import diagnostico as dg




sintomas = []
sintomas_once = []
sintom = []




def saludo():
    cultivo = input("¿Que tipo de cultivo es el tuyo?")


def cargar_bs():
    lista = open("Sintomas/simt_tabaco.txt", encoding="utf8")
    leer_lista = lista.read()
    e_lista = leer_lista.split("\n")
    sintomas.append(e_lista)
    # print(len(sintomas))
    lista.close

    # print(len(sintoma))



class Prueba:

    def __init__(self, diagnostico = ""):
        self._diagnostico = diagnostico


    def get_disganostico(self):
        return self._diagnostico

    def set_diagnostico(self, pre):
        self._diagnostico = pre

        
pb = Prueba()




class ventana2():
    def __init__(self, ventana1):
        self.vent2 = ventana1
        self.vent2.title("Sistema Experto Fungi")
        self.vent2.geometry('933x700')
    #    self._var3 = var3 
        #self.var3 = StringVar() 
    #def get_respuesta(self):
    #    return self._var3.get()

    #def set_respuesta(self, re):
    #    self._var3 = re
        
#def abrir_ventana_dg():
#    dg.abrir_ventana        
class Diagnostico():
    def __init__(self, ventana1):
        self.vent2 = ventana1
        self.vent2.title("Sistema Experto Fungi")
        self.vent2.geometry('933x700')

      
def Mostrar(var, app):
    #print(var)
    global respuesta
    respuesta = var
    app.destroy()
    
respuesta = ""

def Respuesta():
    return respuesta
    
    
pregunta = ""
    
def Pregunta():
    #print(pregunta, "xd")
    return pregunta
    

#def mostrarMensaje():
#    messagebox.showinfo(message="Mensaje", title="Título")
#    pass
    
def abrir_ventana2():
    #ventana.withdraw()               

    ventana1 = Tk()
    app = ventana2(ventana1)
    bg = PhotoImage(file="Imagenes/tabaco.png")
    label = Label(ventana1, image=bg)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label_pre = Label(ventana1, text="A continuación se te pide contestar una serie de preguntas:", font=("Amatic SC bold", 29), fg="black", bg = '#FFFFFF')
    label_pre.place(y=0, x=5)
    #print(le.pregunta)
    
    var = StringVar()
    
    radio_boton = Radiobutton(ventana1, text="SI", variable=var, value="si", command=lambda: Mostrar(var.get(), ventana1))
    radio_boton2 = Radiobutton(ventana1, text="NO", variable=var, value="no", command=lambda: Mostrar(var.get(), ventana1))
    
    #Trae la pregunta 
    label_pregunta = Label(ventana1, text= "¿" + Pregunta() + "?" , font=("Nunito", 18), fg="black", bg = '#FFFFFF', wraplength=450)
    label_pregunta.place(y=120, x=10)
    
    #Radio Buttom - Responde la pregunta 
    var_radio = StringVar()
    #app.set_respuesta(var_radio)
    
    #print(var_radio)
    radio_boton.place(y=320, x=90)
    radio_boton.config(font=("Nunito", 18), bg='#FFFFFF', activebackground='#AEE25A', cursor="target")
    radio_boton2.place(y=320, x=240)
    radio_boton2.config(font=("Nunito", 18), bg='#FFFFFF', activebackground='#AEE25A', cursor="target")
    #variable_re.set_respuesta(var_radio)
    #print(variable_re.get_respuesta)
    #print(var_radio.get())
    
   
    #label_pre.place(y=20, x=165)
    #label.pack()
    ventana1.mainloop()



def abrir_ventana_dg():
    
    ventana1 = Toplevel()
    app = ventana2(ventana1)
    bg = PhotoImage(file="Imagenes/descripcion.png")
    label = Label(ventana1, image=bg)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    unframe = Label(ventana1, bg='#AEE25A', text="DIAGNÓSTICO")
    unframe.config(font= ("Amatic SC bold", 34), fg="black")
 
    unframe.place(y=99, x=170)

    label_usu = Label(ventana1, text="SU CULTIVO SUFRE DE " + pb.get_disganostico() , font= ("Amatic SC bold", 30), fg="black")
    label_usu.config(bg='#AEE25A')
    label_usu.place(x=170, y=190, anchor="w")
  
    enfermedades = open("Descripcion/"+ pb.get_disganostico() + ".txt", encoding="utf8")
    lectura_enfermedades = enfermedades.read()
    
    
    label_des = Label(ventana1, text=lectura_enfermedades, font= ("Nunito", 15), fg="black",  wraplength=700, anchor="e", justify=LEFT)
    label_des.config(bg='#AEE25A')
    label_des.place(x=170, y=220)
    
    def abrir_ventana_tratamiento():
        #ventana3.withdraw
        #ventana4 = Toplevel()
        #app = ventana2(ventana4)
        bg = PhotoImage(file="Imagenes/tratamiento.png")
        label = Label(ventana1, image=bg)
        label.place(x=0, y=0, relwidth=1, relheight=1) 
        
        tratamiento = open("Tratamiento/TRATAMIENTOS_"+ pb.get_disganostico() + ".txt", encoding="utf8")
        lectura_enfermedades = tratamiento.read()
    
    
        label_trata = Label(ventana1, text=lectura_enfermedades, font= ("Nunito bold", 15), fg="black",  wraplength=500, anchor="e", justify=LEFT)
        label_trata.config(bg='#AEE25A')
        label_trata.place(x=50, y=100)
        
        ventana1.mainloop()
    
    validar = Button(ventana1, text="Siguiente", command=abrir_ventana_tratamiento)
    validar.config(width=15, height=2, font=('Amatic SC bold', 20), bg='#FFFFFF')
    validar.place(y=500, x=380)
    
    ventana1.mainloop()




class DiagnosticoEnfermedad(KnowledgeEngine):
    
       
    
    @DefFacts()
    def inicial(self):
        yield Fact(action="encontrar_enfermedad")
        #yield Fact(bandera=False)
        #sintoma1 = []
        for sintoma in sintomas:
            for i in range(len(sintoma)):
                sintomas_once.append(sintoma[i])
        

        #print(sintomas_once[:])

    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma0=W())), salience=1)
    def sintoma_0(self):
 
        global pregunta
        pregunta=sintomas_once[0]
        abrir_ventana2()
        self.declare(Fact(sintoma0=Respuesta()))


    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma1=W())), Fact(sintoma0=MATCH.s0), NOT(Fact(sintoma2=W())))
    def sintoma_1_y_2(self, s0):
        if s0 == "si":
            global pregunta
            pregunta = sintomas_once[1]
            abrir_ventana2()
            #pb.set_pregunta(sintomas_once[1])
            #self.declare(Fact(sintoma1=input(f"¿{sintomas_once[1]}?: ")))
            self.declare(Fact(sintoma1=Respuesta()))
        else:
            #global pregunta
            pregunta = sintomas_once[2]
            abrir_ventana2()
            self.declare(Fact(sintoma2=Respuesta()))
            
            
    @Rule(Fact(action='encontrar_enfermedad'), Fact(sintoma1=MATCH.s1), NOT(Fact(do=W())))
    def sintoma_MR(self, s1):
        if s1 == "si":
            global pregunta
            pregunta = "Su cultivo sufre de Damping Off"
            
            pb.set_diagnostico("DAMPING OFF")
            respuesta_ms = messagebox.askyesno(message="De a cuerdo a las preguntas respondidas tenemos un diagnóstico, ¿Desea continuar?", title="Continuar")
            if respuesta_ms == True:
               abrir_ventana_dg()
               #print("Hola mundo")
            else: 
                print("Lo sentimos")
            #Poner otra ventana pero con un boton que diga siguiente y este que abra la ventana de Diagnostico
            
            self.declare(Fact(do="True"))
            #print("Su cultivo sufre de Mancha Roja")
            #KnowledgeEngine.reset()
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa", title="Continuar")
            print("Respuesta desconocida")
            #quit()
    
    
    
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma3=W())), Fact(sintoma2=MATCH.s2), NOT(Fact(sintoma4=W())), NOT(Fact(do=MATCH.do)))
    def sintoma_3_y_4(self, s2):
        if s2 == "si":
            global pregunta
            pregunta = sintomas_once[3]
            abrir_ventana2()
            #pb.set_pregunta(sintomas_once[1])
            #self.declare(Fact(sintoma1=input(f"¿{sintomas_once[1]}?: ")))
            self.declare(Fact(sintoma3=Respuesta()))
        else:
            #global pregunta
            pregunta = sintomas_once[4]
            abrir_ventana2()
            self.declare(Fact(sintoma4=Respuesta()))
            
            
    
            

    @Rule(Fact(action='encontrar_enfermedad'), Fact(sintoma3=MATCH.s3), NOT(Fact(do=MATCH.do)), NOT(Fact(ml=W())))
    def sintoma_ML(self, s3):
        if s3 == "si":
            global pregunta
            pregunta = "Su cultivo sufre de Moho Azul del Tabaco"
            #print("entro")
            pb.set_diagnostico("MOHO AZUL DEL TABACO")
            respuesta_ms = messagebox.askyesno(message="De a cuerdo a las preguntas respondidas tenemos un diagnóstico, ¿Desea continuar?", title="Continuar")
            if respuesta_ms == True:
               abrir_ventana_dg()
               #print("Hola mundo")
            else: 
                print("Lo sentimos")
            #Poner otra ventana pero con un boton que diga siguiente y este que abra la ventana de Diagnostico
            
            self.declare(Fact(ml="True"))
            #print("Su cultivo sufre de Mancha Roja")
            #KnowledgeEngine.reset()
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa", title="Continuar")
            print("Respuesta desconocida")
            #quit()
            
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma5=W())), Fact(sintoma4=MATCH.s4), NOT(Fact(do=MATCH.do)), NOT(Fact(ml=MATCH.ml)))
    def sintoma_5(self, s4):
        if s4 == "si":
            global pregunta
            pregunta = sintomas_once[5]
            abrir_ventana2()
            self.declare(Fact(sintoma5=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit()
            
    
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma6=W())), Fact(sintoma5=MATCH.s5), NOT(Fact(do=MATCH.do)), NOT(Fact(ml=MATCH.ml)))
    def sintoma_6(self, s5):
        if s5 == "si":
            global pregunta
            pregunta = sintomas_once[6]
            abrir_ventana2()
            self.declare(Fact(sintoma6=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit()
    
    
    @Rule(Fact(action='encontrar_enfermedad'), Fact(sintoma6=MATCH.s6), NOT(Fact(pp=W())), NOT(Fact(do=MATCH.do)), NOT(Fact(ml=MATCH.ml)))
    def sintoma_PP(self, s6):
        if s6 == "si":
            global pregunta
            pregunta = "Su cultivo sufre de Pata Prieta"
            
            pb.set_diagnostico("PATA PRIETA")
            respuesta_ms = messagebox.askyesno(message="De a cuerdo a las preguntas respondidas tenemos un diagnóstico, ¿Desea continuar?", title="Continuar")
            if respuesta_ms == True:
               abrir_ventana_dg()
               #print("Hola mundo")
            else: 
                print("Lo sentimos")
            #Poner otra ventana pero con un boton que diga siguiente y este que abra la ventana de Diagnostico
            
            self.declare(Fact(mr="True"))
            #print("Su cultivo sufre de Mancha Roja")
            #KnowledgeEngine.reset()
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa", title="Continuar")
            print("Respuesta desconocida")
            #quit()
              

