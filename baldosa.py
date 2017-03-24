from OpenGL.GL import *
from pared import Pared
import random
import math


class Baldosa:
    listaParedes = []
    primero = False

    def __init__(self, punto, lado, rango):
        self.rango = rango
        self.lado = lado
        self.punto = punto[0]*lado, punto[1]*lado
        self.color = random.randrange(2), random.randrange(2), random.randrange(2)
        self.colorOficina = random.randrange(2)/20, random.randrange(2)/30, random.randrange(2)/20

        centro = self.punto[0]+lado/2, self.punto[1]+lado/2
        self.centro = centro


        self.anguloInicial=(5/4)*math.pi

        """Cración de paredes"""
        """todas las baldosas menos las de las fila y columna ultimas"""
        if punto[0] < rango - 1 and punto[1] < rango - 1:
            self.creaPared(0, 2)

        """Columna ultima menos baldosa extremo"""
        if punto[0] == rango - 1 and punto[1] < rango - 1:
            self.creaPared(3, 6)

        """Fila ultima menos baldosa extremo"""
        if punto[0] < rango - 1 and punto[1] == rango - 1:
            self.creaPared(0, 3)

        """baldosa extremo"""
        if punto[0] == rango - 1 and punto[1] == rango - 1:
            self.creaPared(0, 4)


    def dibuja(self, debugueandoEnOficina):
        for pared in self.listaParedes:
            pared.dibuja(debugueandoEnOficina)

        # if debugueandoEnOficina:
        #     glColor3fv(self.colorOficina)
        # else:
        #     glColor3fv(self.color)
        # glRectf(self.punto[0], self.punto[1], self.punto[0]+self.lado, self.punto[1]+self.lado)

        """Lineas en el centro de las baldosas"""
        # if self.primero:
        #     glBegin(GL_LINES)
        #     glVertex3f(self.centro[0],self.centro[1], 0)
        #     glVertex3f(self.centro[0],self.centro[1], 5)
        #     glEnd()

    def creaPared(self, inicio, fin):
        for i in range(inicio, fin):
            angulo = self.anguloInicial - i * math.pi / 2
            punto1 = self.centro[0] + self.lado / 2 * math.sqrt(2) * math.cos(angulo),\
                     self.centro[1] + self.lado / 2 * math.sqrt(2) * math.sin(angulo)
            punto2 = self.centro[0] + self.lado / 2 * math.sqrt(2) * math.cos(angulo + math.pi / 2),\
                     self.centro[1] + self.lado / 2 * math.sqrt(2) * math.sin(angulo + math.pi / 2)

            pared = Pared(punto1, punto2, self.lado)
            self.listaParedes.append(pared)

