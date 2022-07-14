from experta import *


sintomas = []
sintomas_once = []
sintom = []


def saludo():
    cultivo = input("¿Que tipo de cultivo es el tuyo?")


def cargar_bs():
    lista = open("Sintomas/ajo_y_cebolla.txt")
    leer_lista = lista.read()
    e_lista = leer_lista.split("\n")
    sintomas.append(e_lista)
    # print(len(sintomas))
    lista.close

    # print(len(sintoma))

def regla(Fact):
    print("kk")
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma444=W())))
    def sintoma_444(self):
        print("Hola mundo")


class DiagnosticoEnfermedad(KnowledgeEngine):

    @DefFacts()
    def inicial(self):
        yield Fact(action="encontrar_enfermedad")
        #sintoma1 = []
        
                                

            #Server = {}
            #Server = [ 'server1' , 'server2' , 'server3' , 'server4' ]

            # print(sintoma1)
        # print('sintoma1')
        # print(diccionario2['sintoma0'][0])
        # print(len(diccionario['sintoma0']))

        for sintoma in sintomas:
            for i in range(len(sintoma)):
                sintomas_once.append(sintoma[i])
                
                
        

            
        
                            
   
          
    
    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma0=W())))
    def sintoma_0(self):
        # for sintoma in sintomas():
        #print("Hola mundo")
        self.declare(Fact(sintoma0=input(f"¿{sintomas_once[0]}?: ")))
        regla(Fact(action='encontrar_enfermedad'))
        # print(sintoma[:])
        diccionario = {"sintoma0": [sintomas_once[1], sintomas_once[4]], "sintoma1": [sintomas_once[2]], "sintoma2": [sintomas_once[3]]}
        diccionario2 = {"sintoma0": [{"sintoma1": sintomas_once[1]}, {"sintoma4": sintomas_once[4]}]}
        # for clave, valor in diccionario2['sintoma0'][0].items():
        #    print(type(clave))

        #sintom = []

        for clave, valor in diccionario2.items():
            if len(diccionario2[clave]) > 1:
                for i in range(len(diccionario2[clave])):
                    for clave1, valor1 in diccionario2[clave][i].items():
                        print(clave1, valor1)
                        sintom.append(clave1)
                        if len(sintom) > 1:
                            print(len(sintom))
                            # for j in sintom:
                            #exec(j+"=6", globals())
                            # print(sintoma1)
                            exec(sintom[0]+"=6", globals())
                            print(sintoma1)
                            
                            print("noxd")
                            
        

    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma1=W())), Fact(sintoma0=MATCH.s0), NOT(Fact(sintoma4=W())))
    def sintoma_1_y_4(self, s0):
        if s0 == "si":
            self.declare(Fact(sintoma1=input(f"¿{sintomas_once[1]}?: ")))
        else:
            self.declare(Fact(sintoma4=input(f"¿{sintomas_once[4]}?: ")))

    @Rule(Fact(action='encontrar_enfermedad'), NOT(Fact(sintoma2=W())), Fact(sintoma1=MATCH.s1))
    def sintoma_2(self, s1):
        if s1 == "si":
            self.declare(Fact(sintoma2=input(f"¿{sintomas_once[2]}?: ")))
        else:
            print("Respuesta desconocida")


cargar_bs()

ed = DiagnosticoEnfermedad()
ed.reset()
ed.declare(regla(Fact(action='encontrar_enfermedad')))
ed.run()