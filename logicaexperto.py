from experta import *

tipo_cultivo = str(input("¿Se que tipo es su cultivo?"))


class DiagnosticoEnfermedad(KnowledgeEngine):
    @DefFacts()
    def carga_sintomas(self):
        #Hechos iniciales
        
        yield Fact(sint="¿En el follaje tiene lesiones blancas hundidas justo en el centro y son de color purpura rojizo?", resp=input(), pregunta=1)
        print("Hola bienvenido a UP-Fungi")
        #yield Fact(accion="Encontrar_enfermedad")
        yield Fact(sint="¿Las lesiones al envejecer, forman una zona oscura compuesta por una masa superficial de esporas del hongo?", resp=input(), pregunta=2)
        yield Fact(sint="¿Las manchas son eclipticas, y pueden alcanzar varios cm de largo formando un halo amarillo?", resp=input(), pregunta=3)
        yield Fact(sint="¿Cuando la infeccion es fuerte, durante la recoleccion se observa la afectacion del bulbo en forma de putrefaccion semiacosa, adquiriendo una coloracion amarillo intenso o rojo vinoso?", resp=input(), pregunta=4)
        yield Fact(sint="¿La enfermedad aparece en los bulbos despues de su recoleccion en forma de un reblandecimiento del tejido afectado de las escamas?", resp=input(), pregunta=5)
        yield Fact(sint="¿Toma una apariencia de mojado y cocido, separando el tejido sano por un margen de color ambar bien definido?", resp=input(), pregunta=6)
        yield Fact(sint="¿Sobre el tejido reblandecido se hace evidente un tinte grisaceo pardo y una ligera contracción?", resp=input(), pregunta=7)
        yield Fact(sint="¿La enfermedad se caracteriza por una coloracion rosada o morada en el tejido de las raices?", resp=input(), pregunta=8)
        yield Fact(sint="¿Luego estas raices adquieren un color cafe oscuro y luego mueren?", resp=input(), pregunta=9)
        yield Fact(sint="¿Las plantas contin&an emitiendo raices pero de forma senciblemente mas reducidas?", resp=input(), pregunta=10)
        yield Fact(sint="¿El follaje se torna amarillento y las plantas presentan enanismo?", resp=input(), pregunta=11)
    @Rule(Fact(resp=MATCH.r, pregunta=MATCH.n))
    
    
if __name__ == '__main__':
    de = DiagnosticoEnfermedad()
    de.reset()
    de.run()

#de = DiagnosticoEnfermedad()
#de.reset()
#de.run()  
        
        