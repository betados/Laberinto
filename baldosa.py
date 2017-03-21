from OpenGL.GL import *
from pared import Pared
import random
import math


class Baldosa:
    color = 0, 0, 0
    listaParedes = []
    def __init__(self, punto, indice, lado=1):
        self.lado = lado
        self.punto = punto
        self.indice=indice
        self.color = random.randrange(2), random.randrange(2), random.randrange(2)
        # self.color = random.randrange(256)/255, random.randrange(256)/255, random.randrange(256)/255
        if indice % 2 != 0:
            self.colorFijo = GLfloat_3(0, 0.1, 0.9)
        else:
            self.colorFijo = GLfloat_3(0, 0, 0)

        centro = punto[0]+lado/2,  punto[1]+lado/2
        # print("constructor baldosa")
        angulo=(5/4)*math.pi
        for i in range(0,4,1):
            punto1 = centro[0] + math.sqrt(2)/2 * math.cos(angulo), centro[1]+math.sqrt(2)/2 * math.sin(angulo)
            punto2 = centro[0] + math.sqrt(2)/2 * math.cos(angulo+math.pi/2), centro[1] + math.sqrt(2)/2 * math.sin(angulo+math.pi/2)
            pared = Pared(punto1, punto2, self.lado)
            angulo += math.pi/2
            self.listaParedes.append(pared)



    def dibuja(self):
        for pared in self.listaParedes:
            pared.dibuja()


        glColor3fv(self.colorFijo)
        glRectf(self.punto[0],self.punto[1],self.lado*(self.punto[0]+1),self.lado*(self.punto[1]+1))
