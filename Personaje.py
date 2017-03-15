import math
class Personaje:
    def __init__(self,pos=(0,0,5),mira=(100,100,1)):
        self.pos=pos
        self.mira=mira

        self.moduloPosicion = math.sqrt( math.pow(pos[0],2) +  math.pow(pos[0],2) ),\
                      math.sqrt( math.pow(pos[1],2) +  math.pow(pos[1],2) )

        #TODO arreglar esto para todos los cuadrantes y ver si esto funciona el grados o radianes
        if pos[0]==0:
            self.argumentoPosicion = 90
        else:
            self.argumentoPosicion = math.atan(pos[1]/pos[0])

        self.moduloMirada = math.sqrt( math.pow(pos[0],2) +  math.pow(pos[0],2) ),\
                      math.sqrt( math.pow(pos[1],2) +  math.pow(pos[1],2) )

        #TODO arreglar esto para todos los cuadrantes y ver si esto funciona el grados o radianes
        if mira[0]==0:
            self.argumentoMirada = 90
        else:
            self.argumentoMirada = math.atan(mira[1]/mira[0])

    def avanza(self):
        pass
    def setMirada(self,movimiento):
        # la x del raton cambia el ángulo y la y
        # cambia la z hacia donde mira el person
        self.mira=self.mira[0],self.mira[1],self.mira[2]-movimiento[1]*0.1

        self.argumentoMirada -= movimiento[0]*0.05

    def getPos(self):
        return self.pos

    def getMirada(self):
        self.mira=math.cos(self.argumentoMirada), math.sin(self.argumentoMirada),self.mira[2]
        return self.mira