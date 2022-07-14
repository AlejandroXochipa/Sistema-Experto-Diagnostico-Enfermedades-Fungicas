from experta import *


    
sintomas = []
sintoma1 = []   
    
def saludo():
    cultivo = input("¿Que tipo de cultivo es el tuyo?")
        
def cargar_bs():
    lista = open("Sintomas/ajo_y_cebolla.txt")
    leer_lista = lista.read()
    e_lista = leer_lista.split("\n")
    sintomas.append(e_lista)
    #print(len(sintomas))
    lista.close
    
    
    #print(len(sintoma)) 
        
class DiagnosticoEnfermedad(KnowledgeEngine):
    
    @DefFacts()
    def inicial(self):
        yield Fact(action="encontrar_enfermedad")
        #sintoma1 = []
        for sintoma in sintomas:
            for i in range(len(sintoma)):
                sintoma1.append(sintoma[i])
     
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma1=W())))
    def sintoma_1(self):
        #for sintoma in sintomas():
        self.declare(Fact(sintoma1=input(f"¿{sintoma1[0]}?: ")))
        #print(sintoma[:])
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma2=W())), Fact(sintoma1="si"))
    def sintoma_2(self):
        self.declare(Fact(sintoma2=input(f"¿{sintoma1[1]}?: ")))
  
    
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma5=W())), Fact(sintoma1="no"))
    def sintoma_5(self):
        self.declare(Fact(sintoma5=input(f"¿{sintoma1[4]}?: ")))
        
    
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma3=W())), Fact(sintoma2=MATCH.s2))
    def sintoma_3(self, s2):
        if s2 == "si":
            print("Que bueno carnal")
        else:
            print("Ni pedo")              
            
            
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma4=W())), Fact(sintoma3="si"))
    def sintoma_4(self):
        self.declare(Fact(sintoma4=input(f"¿{sintoma1[3]}?: ")))
    
  
cargar_bs() 

ed = DiagnosticoEnfermedad()
ed.reset()
ed.run()