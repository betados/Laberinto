import math
from OpenGL.GL import *
class Personaje:
    def __init__(self,pos=(0,0,5),mira=(100,100,1)):
        self.pos=pos
        self.posAnt=pos
        self.mirada=mira

        self.moduloPosicion =self.getModulo(pos)

        self.argumentoPosicion = self.getArgumento(pos)


        self.moduloMirada = math.sqrt( math.pow(pos[0],2) +  math.pow(pos[0],2) ),\
                      math.sqrt( math.pow(pos[1],2) +  math.pow(pos[1],2) )

        self.argumentoMirada = self.getArgumento(mira)

    def avanza(self):
        pass
    def setMirada(self,movimiento):
        # la x del raton cambia el ángulo y la y
        # cambia la z hacia donde mira el person
        self.argumentoMirada -= movimiento[0] * 0.05

        self.mirada= self.getModulo(self.mirada)*math.cos(self.argumentoMirada), \
                     self.getModulo(self.mirada)*math.sin(self.argumentoMirada), \
                     self.mirada[2] - movimiento[1] * 0.5
        print("argumento: ", self.argumentoMirada)
        print("coseno: ", math.cos(self.argumentoMirada))
        print("------------------: ")

    def getPos(self):
        return self.pos

    def getMirada(self):
        return self.mirada
    def avanza(self,avance):
        # print("pos: ",self.pos)
        # print("mir: ",self.mirada)
        # print(" ")
        self.pos=self.pos[0]+self.getUnitario(self.mirada)[0]*avance[0]*0.1,\
                 self.pos[1]+self.getUnitario(self.mirada)[1]*avance[0]*0.1

        self.pos = self.pos[0]+self.getPerpendicular(self.getUnitario(self.mirada))[0]*avance[1]*0.1,\
                   self.pos[1]+self.getPerpendicular(self.getUnitario(self.mirada))[1]*avance[1]*0.1

        self.mirada=self.mirada[0]+self.getVariacionPos()[0],\
                    self.mirada[1]+self.getVariacionPos()[1],\
                    self.mirada[2]

        self.argumentoMirada = self.getArgumento(self.mirada)
        # print(self.argumentoMirada)
    def getUnitario(self,vector):
        modulo = self.getModulo(vector)
        return vector[0]/modulo, vector[1]/modulo
    def getModulo(self,vector):
        return math.sqrt(math.pow(vector[0], 2) + math.pow(vector[1], 2))
    def getPerpendicular(self,vector):
        argumento=self.getArgumento(vector)+math.pi/2

        return math.cos(argumento), math.sin(argumento)

    def getArgumento(self,vector):
        if vector[0] == 0:
            if vector[1] > 0:
                return math.pi/2
            else:
                return (3 * math.pi) / 2
        else:
            return math.atan2(self.mirada[1] , self.mirada[0])
    def getVariacionPos(self):
        variacion = self.pos[0]-self.posAnt[0], self.pos[1]-self.posAnt[1]
        self.posAnt=self.pos
        return variacion
    def dibuja(self):
        glDisable(GL_LIGHTING)
        glColor3f(0.1, 0.02, 0)
        glRectf(self.pos[0]-.5, self.pos[1]-.5,self.pos[0]+.5, self.pos[1]+.5)

        glColor3f(0, 0, 0.5)
        glBegin(GL_LINES)
        glVertex2f(self.pos[0],self.pos[1])
        glVertex2f(self.mirada[0],self.mirada[1])
        glEnd()

        glColor3f(0, 0, 0.5)
        glBegin(GL_LINES)
        glVertex2f(self.pos[0],self.pos[1])
        glVertex2f(self.getPerpendicular(self.mirada)[0],self.getPerpendicular(self.mirada)[1])
        glEnd()


        glEnable(GL_LIGHTING)
        glBegin(GL_TRIANGLE_STRIP)
        glEnd()
        glFlush()
