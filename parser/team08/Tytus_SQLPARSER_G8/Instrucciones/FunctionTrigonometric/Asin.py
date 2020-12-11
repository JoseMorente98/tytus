
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Asinh(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("ASIN")
        print(math.asin(self.valor))
        return math.asin(self.valor)

instruccion = Asinh(1,None, 1,2)

instruccion.ejecutar(None,None)