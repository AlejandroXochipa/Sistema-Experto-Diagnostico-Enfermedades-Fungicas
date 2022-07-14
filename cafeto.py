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
    lista = open("Sintomas/simt_cafeto.txt", encoding="utf8")
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
    bg = PhotoImage(file="Imagenes/cafeto.png")
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

    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma9=W())), Fact(sintoma0=MATCH.s0), NOT(Fact(sintoma1=W())))
    def sintoma_1_y_9(self, s0):
        if s0 == "si":
            global pregunta
            pregunta=sintomas_once[1]
            abrir_ventana2()
            self.declare(Fact(sintoma1=Respuesta()))
        else:
            #global pregunta
            pregunta=sintomas_once[9]
            abrir_ventana2()
            self.declare(Fact(sintoma9=Respuesta()))
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma2=W())), Fact(sintoma1=MATCH.s1))
    def sintoma_2(self, s1):
        if s1 == "si":
            global pregunta
            pregunta = sintomas_once[2]
            abrir_ventana2()
            self.declare(Fact(sintoma2=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit()
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma3=W())), Fact(sintoma2=MATCH.s2))
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
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma4=W())), Fact(sintoma3=MATCH.s3))
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
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma5=W())), Fact(sintoma4=MATCH.s4))
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
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma6=W())), Fact(sintoma5=MATCH.s5))
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
    
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma7=W())), Fact(sintoma6=MATCH.s6))
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
    
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma8=W())), Fact(sintoma7=MATCH.s7))
    def sintoma_8(self, s7):
        if s7 == "si":
            global pregunta
            pregunta = sintomas_once[8]
            abrir_ventana2()
            self.declare(Fact(sintoma8=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit()
            
    @Rule(Fact(action='encontrar_enfermedad'), Fact(sintoma8=MATCH.s8), NOT(Fact(ac=W())))
    def sintoma_AC(self, s8):
        if s8 == "si":
            global pregunta
            pregunta = "Su cultivo sufre de Antracnosis del Cafeto"
            
            pb.set_diagnostico("ANTRACNOSIS DEL CAFETO")
            respuesta_ms = messagebox.askyesno(message="De a cuerdo a las preguntas respondidas tenemos un diagnóstico, ¿Desea continuar?", title="Continuar")
            if respuesta_ms == True:
               abrir_ventana_dg()
               #print("Hola mundo")
            else: 
                print("Lo sentimos")
            #Poner otra ventana pero con un boton que diga siguiente y este que abra la ventana de Diagnostico
            
            self.declare(Fact(ac="True"))
            #print("Su cultivo sufre de Mancha Roja")
            #KnowledgeEngine.reset()
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa", title="Continuar")
            print("Respuesta desconocida")
            
    
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma10=W())), NOT(Fact(sintoma14=W())),Fact(sintoma9=MATCH.s9), NOT(Fact(ac=MATCH.ac)))
    def sintoma_10_y_14(self, s9):
        if s9 == "si":
            global pregunta
            pregunta=sintomas_once[10]
            abrir_ventana2()
            self.declare(Fact(sintoma10=Respuesta()))
        else:
            #global pregunta
            pregunta=sintomas_once[14]
            abrir_ventana2()
            self.declare(Fact(sintoma14=Respuesta()))
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma11=W())), Fact(sintoma10=MATCH.s10), NOT(Fact(ac=MATCH.ac)))
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
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma12=W())), Fact(sintoma11=MATCH.s11), NOT(Fact(ac=MATCH.ac)))
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
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma13=W())), Fact(sintoma12=MATCH.s12), NOT(Fact(ac=MATCH.ac)))
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
            
    @Rule(Fact(action='encontrar_enfermedad'), Fact(sintoma13=MATCH.s13), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=W())))
    def sintoma_LLM(self, s13):
        if s13 == "si":
            global pregunta
            pregunta = "Su cultivo sufre de Llaga Macana"
            
            pb.set_diagnostico("LLAGA MACANA")
            respuesta_ms = messagebox.askyesno(message="De a cuerdo a las preguntas respondidas tenemos un diagnóstico, ¿Desea continuar?", title="Continuar")
            if respuesta_ms == True:
               abrir_ventana_dg()
               #print("Hola mundo")
            else: 
                print("Lo sentimos")
            #Poner otra ventana pero con un boton que diga siguiente y este que abra la ventana de Diagnostico
            
            self.declare(Fact(llm="True"))
            #print("Su cultivo sufre de Mancha Roja")
            #KnowledgeEngine.reset()
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa", title="Continuar")
            print("Respuesta desconocida")
            
    
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma22=W())), NOT(Fact(sintoma15=W())),Fact(sintoma14=MATCH.s14), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)))
    def sintoma_15_y_22(self, s14):
        if s14 == "si":
            global pregunta
            pregunta=sintomas_once[15]
            abrir_ventana2()
            self.declare(Fact(sintoma15=Respuesta()))
        else:
            #global pregunta
            pregunta=sintomas_once[22]
            abrir_ventana2()
            self.declare(Fact(sintoma22=Respuesta()))
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma16=W())), Fact(sintoma15=MATCH.s15), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)))
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
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma17=W())), Fact(sintoma16=MATCH.s16), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)))
    def sintoma_17(self, s16):
        if s16 == "si":
            global pregunta
            pregunta = sintomas_once[17]
            abrir_ventana2()
            self.declare(Fact(sintoma17=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit()        
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma18=W())), Fact(sintoma17=MATCH.s17), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)))
    def sintoma_18(self, s17):
        if s17 == "si":
            global pregunta
            pregunta = sintomas_once[18]
            abrir_ventana2()
            self.declare(Fact(sintoma18=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit()        
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma19=W())), Fact(sintoma18=MATCH.s18), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)))
    def sintoma_19(self, s18):
        if s18 == "si":
            global pregunta
            pregunta = sintomas_once[19]
            abrir_ventana2()
            self.declare(Fact(sintoma19=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit()
            
    
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma20=W())), Fact(sintoma19=MATCH.s19), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)))
    def sintoma_20(self, s19):
        if s19 == "si":
            global pregunta
            pregunta = sintomas_once[20]
            abrir_ventana2()
            self.declare(Fact(sintoma20=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit()                
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma21=W())), Fact(sintoma20=MATCH.s20), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)))
    def sintoma_21(self, s20):
        if s20 == "si":
            global pregunta
            pregunta = sintomas_once[21]
            abrir_ventana2()
            self.declare(Fact(sintoma21=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit()        
            
    @Rule(Fact(action='encontrar_enfermedad'), Fact(sintoma21=MATCH.s21), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)), NOT(Fact(mh=W())))
    def sintoma_MH(self, s21):
        if s21 == "si":
            global pregunta
            pregunta = "Su cultivo sufre de Mancha de Hierro"
            
            pb.set_diagnostico("MANCHA DE HIERRO")
            respuesta_ms = messagebox.askyesno(message="De a cuerdo a las preguntas respondidas tenemos un diagnóstico, ¿Desea continuar?", title="Continuar")
            if respuesta_ms == True:
               abrir_ventana_dg()
               #print("Hola mundo")
            else: 
                print("Lo sentimos")
            #Poner otra ventana pero con un boton que diga siguiente y este que abra la ventana de Diagnostico
            
            self.declare(Fact(mh="True"))
            #print("Su cultivo sufre de Mancha Roja")
            #KnowledgeEngine.reset()
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa", title="Continuar")
            print("Respuesta desconocida")        
    
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma23=W())), NOT(Fact(sintoma26=W())),Fact(sintoma22=MATCH.s22), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)), NOT(Fact(mh=MATCH.mh)))
    def sintoma_23_y_26(self, s22):
        if s22 == "si":
            global pregunta
            pregunta=sintomas_once[23]
            abrir_ventana2()
            self.declare(Fact(sintoma23=Respuesta()))
        else:
            #global pregunta
            pregunta=sintomas_once[26]
            abrir_ventana2()
            self.declare(Fact(sintoma26=Respuesta()))
            
    
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma24=W())), Fact(sintoma23=MATCH.s23), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)), NOT(Fact(mh=MATCH.mh)))
    def sintoma_24(self, s23):
        if s23 == "si":
            global pregunta
            pregunta = sintomas_once[24]
            abrir_ventana2()
            self.declare(Fact(sintoma24=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit()         
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma25=W())), Fact(sintoma24=MATCH.s24), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)), NOT(Fact(mh=MATCH.mh)))
    def sintoma_25(self, s24):
        if s24 == "si":
            global pregunta
            pregunta = sintomas_once[25]
            abrir_ventana2()
            self.declare(Fact(sintoma25=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit()       
            
    
    @Rule(Fact(action='encontrar_enfermedad'), Fact(sintoma25=MATCH.s25), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)), NOT(Fact(mh=MATCH.mc)), NOT(Fact(og=W())))
    def sintoma_OG(self, s25):
        if s25 == "si":
            global pregunta
            pregunta = "Su cultivo sufre de Ojo de Gallo"
            
            pb.set_diagnostico("OJO DE GALLO")
            respuesta_ms = messagebox.askyesno(message="De a cuerdo a las preguntas respondidas tenemos un diagnóstico, ¿Desea continuar?", title="Continuar")
            if respuesta_ms == True:
               abrir_ventana_dg()
               #print("Hola mundo")
            else: 
                print("Lo sentimos")
            #Poner otra ventana pero con un boton que diga siguiente y este que abra la ventana de Diagnostico
            
            self.declare(Fact(og="True"))
            #print("Su cultivo sufre de Mancha Roja")
            #KnowledgeEngine.reset()
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa", title="Continuar")
            print("Respuesta desconocida") 
            
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma27=W())), Fact(sintoma26=MATCH.s26), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)), NOT(Fact(mh=MATCH.mh)), NOT(Fact(og=MATCH.og)))
    def sintoma_27(self, s26):
        if s26 == "si":
            global pregunta
            pregunta = sintomas_once[27]
            abrir_ventana2()
            self.declare(Fact(sintoma27=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit() 
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma28=W())), Fact(sintoma27=MATCH.s27), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)), NOT(Fact(mh=MATCH.mh)), NOT(Fact(og=MATCH.og)))
    def sintoma_28(self, s27):
        if s27 == "si":
            global pregunta
            pregunta = sintomas_once[28]
            abrir_ventana2()
            self.declare(Fact(sintoma28=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit() 
            
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma29=W())), Fact(sintoma28=MATCH.s28), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)), NOT(Fact(mh=MATCH.mh)), NOT(Fact(og=MATCH.og)))
    def sintoma_29(self, s28):
        if s28 == "si":
            global pregunta
            pregunta = sintomas_once[29]
            abrir_ventana2()
            self.declare(Fact(sintoma29=Respuesta()))
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa, el programa se cerrara", title="Continuar")
            #print("Respuesta desconocida")
            quit() 
    
    
    @Rule(Fact(action='encontrar_enfermedad'), Fact(sintoma29=MATCH.s29), NOT(Fact(ac=MATCH.ac)), NOT(Fact(llm=MATCH.llm)), NOT(Fact(mh=MATCH.mc)), NOT(Fact(og=MATCH.og)), NOT(Fact(rf=W())))
    def sintoma_RF(self, s29):
        if s29 == "si":
            global pregunta
            pregunta = "Su cultivo sufre de Roya del Cafeto"
            
            pb.set_diagnostico("ROYA DEL CAFETO")
            respuesta_ms = messagebox.askyesno(message="De a cuerdo a las preguntas respondidas tenemos un diagnóstico, ¿Desea continuar?", title="Continuar")
            if respuesta_ms == True:
               abrir_ventana_dg()
               #print("Hola mundo")
            else: 
                print("Lo sentimos")
            #Poner otra ventana pero con un boton que diga siguiente y este que abra la ventana de Diagnostico
            
            self.declare(Fact(rf="True"))
            #print("Su cultivo sufre de Mancha Roja")
            #KnowledgeEngine.reset()
        else:
            messagebox.showinfo(message="De a cuerdo a las preguntas respondidas no existe un diagnostico previo, le pedimos una disculpa", title="Continuar")
            print("Respuesta desconocida") 
    
    
