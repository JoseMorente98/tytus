from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo

class Enum(Instruccion):
    def __init__(self, id, tipo, linea, columna, strSent):
        Instruccion.__init__(self,Tipo("",Tipo_Dato.TIPOENUM),linea,columna,"", strSent)
        self.id = id
        self.listaValores = []

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        return self.valor

    
    def buscarTipo(self, nombre):
        for x in range(0, len(self.listaValores)):
            if self.listaValores[x] == nombre:
                return nombre
        
        return None