from experta import *
from tkinter import *
from tkinter import ttk
import maiz
import garbanzo
import cafeto
import cacao
import tabaco
import berenjena
import platano
import arroz
import ajoycebolla
from tkinter import messagebox
#from tkinter.font import Font

#from PIL import ImageFont
#from fonts.ttf import AmaticSC
#font = ImageFont.truetype('AmaticSC')
#import logicaexperto5 as le





class aplicacion():
    
    def __init__(self, ventana):
        self.vent = ventana
        self.vent.title("Sistema Experto Fungi")
        self.vent.geometry('933x700')
          
          #frame =LabelFrame(self.vent, text="Registro")
          #frame.grid(pady =35, padx= 35)
          
class ventana2():
    def __init__(self, ventana1):
        self.vent2 = ventana1
        self.vent2.title("Sistema Experto Fungi")
        self.vent2.geometry('933x700')  
    #    self.var_radio = StringVar()
        
    #def get_var_radio(self):
    #    return self.var_radio

    #def set_respuesta(self, re):
    #    self.var_radio= re    
    
def ventana_uso():
    ventana.withdraw()
    #ventana.destroy()
    ventana3 = Toplevel()
    app = aplicacion(ventana3)
    #Ingresar imagen
    bg1 = PhotoImage(file="Imagenes/ints_uso.png")
    label1 = Label(ventana3, image=bg1)
    label1.place(x=0, y=0, relwidth=1, relheight=1)
    
    
    #Label de bienvenida
    #amatic_sc = Font(family="Amatic SC", size=35, weight="bold")
    label_welc1 = Label(ventana3, text="INSTRUCCIONES DE USO", font= ("Amatic SC bold", 34), fg="black", bg='#AEE25A')
    label_welc1.grid(pady=70, padx=100)
    #pass
    #ventana3.update()
    
    label_guia = Label(ventana3, text="Lea detenidamente cada pregunta que se le presentara. Es  muy  fácil  de  responder,  en  las  preguntas  se le  pide  que  elija  entre  dos posibilidades, entonces sólo tendrá que marcar la respuesta que haya elegido. De acuerdo a las preguntas respondidas el sistema arrojara una de las dos ventanas emergentes, las cuales le harán saber si el sistema tiene diagnóstico o no para la enfermedad que presenta su cultivo.", font= ("Nunito", 14), fg="black", bg='#FFFFFF', wraplength=680, anchor="e", justify=LEFT)
    label_guia.place(y=190, x=96)
    
    label_nota = Label(ventana3, text="Nota: Antes de continuar por favor seleccione el tipo del cultivo del cual se quiere hacer el diagnóstico.", font= ("Nunito bold", 14), fg="black", bg='#FFFFFF', wraplength=680, anchor="e", justify=LEFT)
    label_nota.place(y=350, x=96)
    
    def tipo_encuesta():
        
        #print(lista_despegable.get())
        #ventana.destroy()
        if lista_despegable.get() == "Maíz":
            maiz.cargar_bs()
            ventana.destroy()
            ed = maiz.DiagnosticoEnfermedad()
            ed.reset()
            ed.run()
        elif lista_despegable.get() == "Garbanzo":
            garbanzo.cargar_bs()
            ventana.destroy()
            ed = garbanzo.DiagnosticoEnfermedad()
            ed.reset()
            ed.run()
        elif lista_despegable.get() == "Cafeto":
            cafeto.cargar_bs()
            ventana.destroy()
            ed = cafeto.DiagnosticoEnfermedad()
            ed.reset()
            ed.run()
        elif lista_despegable.get() == "Cacao":
            cacao.cargar_bs()
            ventana.destroy()
            ed = cacao.DiagnosticoEnfermedad()
            ed.reset()
            ed.run()
        elif lista_despegable.get() == "Tabaco":
            tabaco.cargar_bs()
            ventana.destroy()
            ed = tabaco.DiagnosticoEnfermedad()
            ed.reset()
            ed.run()
        elif lista_despegable.get() == "Berenjena":
            berenjena.cargar_bs()
            ventana.destroy()
            ed = berenjena.DiagnosticoEnfermedad()
            ed.reset()
            ed.run()
        elif lista_despegable.get() == "Platano":
            platano.cargar_bs()
            ventana.destroy()
            ed = platano.DiagnosticoEnfermedad()
            ed.reset()
            ed.run()
        elif lista_despegable.get() == "Arroz":
            arroz.cargar_bs()
            ventana.destroy()
            ed = arroz.DiagnosticoEnfermedad()
            ed.reset()
            ed.run()
        elif lista_despegable.get() == "Ajo y Cebolla":
            ajoycebolla.cargar_bs()
            ventana.destroy()
            ed = ajoycebolla.DiagnosticoEnfermedad()
            ed.reset()
            ed.run()
        
    def info():
        print(lista_despegable.get())
        
        
    lista_despegable = ttk.Combobox(ventana3, width=17, font= ("Nunito bold", 14))    
    lista_despegable.place(y=420, x=330)
    
    opciones = ["Cacao", "Cafeto", "Maíz", "Arroz", "Ajo y Cebolla", "Garbanzo", "Berenjena", "Tabaco", "Platano"]
    lista_despegable['values'] = opciones
    
    validar = Button(ventana3, text="Siguiente", command=tipo_encuesta)
    validar.config(width=15, height=2, font=('Amatic SC bold', 20), bg='#FFFFFF')
    validar.place(y=500, x=360)
    ventana3.mainloop()

def cerrar_ventana(ventana):
    #ventana.destroy()
    pass
        
        
class variable():
    def __init__(self, respuesta = ""):
        self._respuesta = respuesta

    def get_respuesta(self):
        return self._respuesta

    def set_respuesta(self, re):
        self._respuesta = re
        
variable_re = variable() 

#def Mostrar():
#    variable_re.set_respuesta(var3.get())
#    #print(var3.get())
        





if __name__ == '__main__':
    ventana = Tk()
    app = aplicacion(ventana)
    #Ingresar imagen
    bg = PhotoImage(file="Imagenes/dg.png")
    label = Label(ventana, image=bg)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    #Label de bienvenida
    
    bg2 = PhotoImage(file="Imagenes/logo_uaem.png")
    label2 = Label(ventana, image=bg2, bg='#AEE25A')
    label2.place(x=780, y=0)
    
    #amatic_sc = Font(family="Amatic SC", size=35, weight="bold")
    label_welc = Label(ventana, text="Bienvenido a UP-FUNGI", font= ("Amatic SC bold", 50), fg="black", bg='#AEE25A')
    label_welc.grid(pady=1, padx=220)
    
    #boton = Button(unframe, text="hola")
    #boton.grid(pady=20, padx=5)
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    
    
    #Frame
    unframe = LabelFrame(ventana, bg='#FFFFFF', text="INICIAR SESIÓN")
    unframe.config(font=("Amatic SC bold", 35), bd=0)
    unframe.config(width = 309, height=315)
    unframe.place(y=130, x=300)
    
    label_usu = Label(unframe, text="Usuario: ", font=("Amatic SC bold", 30))
    label_usu.config(bg='#FFFFFF')
    label_usu.grid(row=1, column=0, pady=10)
    
    usuario=Entry(unframe)
    usuario.config(textvariable=var1, font=("Amatic SC bold", 30))
    usuario.focus()
    usuario.grid(row=1, column=1, pady=10)
    
    label_contra = Label(unframe, text="Contraseña:", font=("Amatic SC bold", 30))
    label_contra.config(bg='#FFFFFF')
    label_contra.grid(row=2, column=0)
    
    contra = Entry(unframe)
    contra.focus()
    contra.config(show="*", textvariable=var2, font=("Amatic SC bold", 30))
    contra.grid(row=2, column=1)
    
    
    def validacion():
        if var1.get() == "root" and var2.get() == "123456":
            print("Sesion iniciada")
            #ventana.destroy()
            ventana_uso()
        else:
            messagebox.showinfo(message="Su contraseña o usuario es incorrecto", title="Advertencia")
            print("Su contraseña o usuario es incorrecto")
    
    validar = Button(ventana, text="Iniciar Sesion", command=validacion)
    validar.config(width=15, height=2, font=('Amatic SC bold', 20), bg='#FFFFFF')
    validar.place(y=380, x=360)
    
    
    
    
    #label_welc.pack(pady=50)
    
    ventana.mainloop()