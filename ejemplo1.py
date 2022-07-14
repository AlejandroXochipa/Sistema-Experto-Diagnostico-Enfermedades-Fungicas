from experta import*
import tk 


lista_enfermedades = []
lista_sintomas = []
dic_sintomas = {}
dic_descripcion  = {}
dic_tratamiento = {}
cultivos = ["arroz", "frijol", "ajo y cebolla", "cafeto", "cacao", "tabaco", "platano", "maiz"]
for i in cultivos:
    print(i)

def carga_bs():
    global lista_enfermedades, lista_sintomas, dic_descripcion, dic_sintomas, dic_tratamiento
    seleccion_cultivo = (str)(input("¿De que es su cultivo?"))
    enfermedades = open("Enfermedades/enfermedad_"+ seleccion_cultivo + ".txt")
    lectura_enfermedades = enfermedades.read()
    e_lista = lectura_enfermedades.split("\n")
    lista_enfermedades.append(e_lista)
    #print(len(lista_enfermedades))
    enfermedades.close()
    #print(len(lista_enfermedades[0]))
    for enfermedad in lista_enfermedades:
        for enfermedad_p in enfermedad:
            descripcion = open("Descripcion/" + enfermedad_p + ".txt")
            lectura_descripcion = descripcion.read()
            dic_descripcion[enfermedad_p] = lectura_descripcion
            descripcion.close()
     
     #Imprimir los numeros primos        
   # print(dic_descripcion) 
    
def indentificar_enfermedad(*argumentos):
    lista_sintomas = []
           
    pass
        

carga_bs()

class motor_inferencia(KnowledgeEngine):
    @DefFacts()
    def datos_necesarios():
        yield Fact(action = "encontrar_enfermedad")
        yield Fact(sintoma = "Las hojas presentan manchas ovaladas en sentido longitudinal")
        
    
    
    pass

#Hacer una iteracion que me permita seleccionar el cultivo y asi de inmediato saber los sintomas(hechos) que se deberan de tomar
