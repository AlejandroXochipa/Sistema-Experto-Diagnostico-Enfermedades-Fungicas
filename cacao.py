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
    lista = open("Sintomas/simt_cacao.txt", encoding="utf8")
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
    

def abrir_ventana2():
    #ventana.withdraw()               

    ventana1 = Tk()
    app = ventana2(ventana1)
    bg = PhotoImage(file="Imagenes/cacao.png")
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

    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(ant=W())), Fact(sintoma0=MATCH.s0), NOT(Fact(sintoma1=W())))
    def sintoma_ANT_y_1(self, s0):
        if s0 == "si":
            global pregunta
            pregunta = "Su cultivo sufre de Antracnosis de Cacao"
            
            pb.set_diagnostico("ANTRACNOSIS DE CACAO")
            respuesta_ms = messagebox.askyesno(message="De a cuerdo a las preguntas respondidas tenemos un diagnóstico, ¿Desea continuar?", title="Continuar")
            if respuesta_ms == True:
               abrir_ventana_dg()
               #print("Hola mundo")
            else: 
                print("Lo sentimos")
            self.declare(Fact(ant="True"))
        else:
            #global pregunta
            pregunta=sintomas_once[1]
            abrir_ventana2()
            self.declare(Fact(sintoma1=Respuesta()))
    
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma8=W())), Fact(sintoma1=MATCH.s1), NOT(Fact(sintoma2=W())), NOT(Fact(ant=MATCH.ant)))
    def sintoma_2_y_8(self, s1):
        if s1 == "si":
            global pregunta
            pregunta=sintomas_once[2]
            abrir_ventana2()
            self.declare(Fact(sintoma2=Respuesta()))
            #self.declare(Fact(sintoma5=input(f"¿{sintomas_once[5]}?: ")))
        else:
            pregunta
            pregunta=sintomas_once[8]
            abrir_ventana2()
            self.declare(Fact(sintoma8=Respuesta()))
            #self.declare(Fact(sintoma7=input(f"¿{sintomas_once[7]}?: "))) 
    
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma3=W())), Fact(sintoma2=MATCH.s2), NOT(Fact(ant=MATCH.ant)))
    def sintoma_3(self, s2):
        if s2 == "si":
            global pregunta
            pregunta = sintomas_once[3]
            abrir_ventana2()
            self.declare(Fact(sintoma3=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit()
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma4=W())), Fact(sintoma3=MATCH.s3), NOT(Fact(ant=MATCH.ant)))
    def sintoma_4(self, s3):
        if s3 == "si":
            global pregunta
            pregunta = sintomas_once[4]
            abrir_ventana2()
            self.declare(Fact(sintoma4=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit()
    
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma5=W())), Fact(sintoma4=MATCH.s4), NOT(Fact(ant=MATCH.ant)))
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
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma6=W())), Fact(sintoma5=MATCH.s5), NOT(Fact(ant=MATCH.ant)))
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
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma7=W())), Fact(sintoma6=MATCH.s6), NOT(Fact(ant=MATCH.ant)))
    def sintoma_7(self, s6):
        if s6 == "si":
            global pregunta
            pregunta = sintomas_once[7]
            abrir_ventana2()
            self.declare(Fact(sintoma7=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit()
    
    
    @Rule(Fact(action='encontrar_enfermedad'), Fact(sintoma7=MATCH.s7), NOT(Fact(ant=MATCH.ant)), NOT(Fact(eb=W())))
    def sintoma_EB(self, s7):
        if s7 == "si":
            global pregunta
            pregunta = "Su cultivo sufre de Escoba de Bruja"
            
            pb.set_diagnostico("ESCOBA DE BRUJA")
            respuesta_ms = messagebox.askyesno(message="De a cuerdo a las preguntas respondidas tenemos un diagnóstico, ¿Desea continuar?", title="Continuar")
            if respuesta_ms == True:
               abrir_ventana_dg()
               #print("Hola mundo")
            else: 
                print("Lo sentimos")
            #Poner otra ventana pero con un boton que diga siguiente y este que abra la ventana de Diagnostico
            
            self.declare(Fact(eb="True"))
            #print("Su cultivo sufre de Mancha Roja")
            #KnowledgeEngine.reset()
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa", title="Continuar")
            print("Respuesta desconocida")
    
    @Rule(Fact(action='encontrar_enfermedad'), (Fact(sintoma8=MATCH.s8)), NOT(Fact(sintoma9=W())), NOT(Fact(sintoma14=W())), NOT(Fact(ant=MATCH.ant)), NOT(Fact(eb=MATCH.eb)))
    def sintoma_9_y_14(self, s8):
        if s8 == "si":
            global pregunta
            pregunta=sintomas_once[9]
            abrir_ventana2()
            self.declare(Fact(sintoma9=Respuesta()))
            #self.declare(Fact(sintoma5=input(f"¿{sintomas_once[5]}?: ")))
        else:
            pregunta
            pregunta=sintomas_once[14]
            abrir_ventana2()
            self.declare(Fact(sintoma14=Respuesta()))
            
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma10=W())), Fact(sintoma9=MATCH.s9), NOT(Fact(ant=MATCH.ant)), NOT(Fact(eb=MATCH.eb)))
    def sintoma_10(self, s9):
        if s9 == "si":
            global pregunta
            pregunta = sintomas_once[10]
            abrir_ventana2()
            self.declare(Fact(sintoma10=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit()       
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma11=W())), Fact(sintoma10=MATCH.s10), NOT(Fact(ant=MATCH.ant)), NOT(Fact(eb=MATCH.eb)))
    def sintoma_11(self, s10):
        if s10 == "si":
            global pregunta
            pregunta = sintomas_once[11]
            abrir_ventana2()
            self.declare(Fact(sintoma11=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit() 
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma12=W())), Fact(sintoma11=MATCH.s11), NOT(Fact(ant=MATCH.ant)), NOT(Fact(eb=MATCH.eb)))
    def sintoma_12(self, s11):
        if s11 == "si":
            global pregunta
            pregunta = sintomas_once[12]
            abrir_ventana2()
            self.declare(Fact(sintoma12=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit() 
    
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma13=W())), Fact(sintoma12=MATCH.s12), NOT(Fact(ant=MATCH.ant)), NOT(Fact(eb=MATCH.eb)))
    def sintoma_13(self, s12):
        if s12 == "si":
            global pregunta
            pregunta = sintomas_once[13]
            abrir_ventana2()
            self.declare(Fact(sintoma13=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit() 
            
    @Rule(Fact(action='encontrar_enfermedad'), Fact(sintoma13=MATCH.s13), NOT(Fact(ant=MATCH.ant)), NOT(Fact(eb=MATCH.eb)), NOT(Fact(ppdc=W())))
    def sintoma_PPDC(self, s13):
        if s13 == "si":
            print("entra2")
            global pregunta
            pregunta = "Su cultivo sufre de Podredumbre Parda del Cacao"
            
            pb.set_diagnostico("PODREDUMBRE PARDA DEL CACAO")
            respuesta_ms = messagebox.askyesno(message="De a cuerdo a las preguntas respondidas tenemos un diagnóstico, ¿Desea continuar?", title="Continuar")
            if respuesta_ms == True:
               abrir_ventana_dg()
               #print("Hola mundo")
            else: 
                print("Lo sentimos")
            #Poner otra ventana pero con un boton que diga siguiente y este que abra la ventana de Diagnostico
            
            self.declare(Fact(ppdc="True"))
            #print("Su cultivo sufre de Mancha Roja")
            #KnowledgeEngine.reset()
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa", title="Continuar")
            print("Respuesta desconocida")
            
            
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma15=W())), Fact(sintoma14=MATCH.s14), NOT(Fact(ant=MATCH.ant)), NOT(Fact(eb=MATCH.eb)), NOT(Fact(ppdc=MATCH.ppdc)))
    def sintoma_15(self, s14):
        if s14 == "si":
            global pregunta
            pregunta = sintomas_once[15]
            abrir_ventana2()
            self.declare(Fact(sintoma15=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit() 
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma16=W())), Fact(sintoma15=MATCH.s15), NOT(Fact(ant=MATCH.ant)), NOT(Fact(eb=MATCH.eb)), NOT(Fact(ppdc=MATCH.ppdc)))
    def sintoma_16(self, s15):
        if s15 == "si":
            global pregunta
            pregunta = sintomas_once[16]
            abrir_ventana2()
            self.declare(Fact(sintoma16=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit() 
            
    @Rule(Fact(action='encontrar_enfermedad'), Fact(sintoma16=MATCH.s16), NOT(Fact(pnmc=W())),NOT(Fact(ant=MATCH.ant)), NOT(Fact(eb=MATCH.eb)), NOT(Fact(ppdc=MATCH.ppdc)))
    def sintoma_PNMC(self, s16):
        if s16 == "si":
            global pregunta
            pregunta = "Su cultivo sufre de Podredumbre Pudricion Negra Mazorca de Cacao"
            
            pb.set_diagnostico("PUDRICION NEGRA MAZORCA DE CACAO")
            respuesta_ms = messagebox.askyesno(message="De a cuerdo a las preguntas respondidas tenemos un diagnóstico, ¿Desea continuar?", title="Continuar")
            if respuesta_ms == True:
               abrir_ventana_dg()
               #print("Hola mundo")
            else: 
                print("Lo sentimos")
            #Poner otra ventana pero con un boton que diga siguiente y este que abra la ventana de Diagnostico
            
            self.declare(Fact(pnmc="True"))
            #print("Su cultivo sufre de Mancha Roja")
            #KnowledgeEngine.reset()
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa", title="Continuar")
            print("Respuesta desconocida")
            
    
    

