from OpenGL.GL import *

from pared import Pared
import random
import math


class Baldosa:
    listaParedes = []
    primero = False

    def __init__(self, punto, lado, rango):
        if punto[0] == 0 and punto[1] == 0:
            self.primero = True
        self.lado = lado
        # self.punto = punto
        self.punto = punto[0]*lado, punto[1]*lado
        # print("lado:", lado)
        self.color = random.randrange(2), random.randrange(2), random.randrange(2)

        centro = self.punto[0]+lado/2,  self.punto[1]+lado/2
        self.centro=centro


        anguloInicial=(5/4)*math.pi

        if punto[0] < rango - 1 and punto[1] < rango - 1:
            for i in range(0, 2):
                angulo = anguloInicial - i * math.pi / 2
                punto1 = centro[0] + self.lado/2 * math.sqrt(2) * math.cos(angulo), centro[1] + self.lado/2 * math.sqrt(2) * math.sin(angulo)
                punto2 = centro[0] + self.lado/2 * math.sqrt(2) * math.cos(angulo+math.pi/2), centro[1] + self.lado/2 * math.sqrt(2) * math.sin(angulo+math.pi/2)

                pared = Pared(punto1, punto2, self.lado)
                # angulo -= math.pi/2
                self.listaParedes.append(pared)

        if punto[0] == rango - 1 and punto[1] < rango - 1:
            for i in range(3, 6):
                angulo=anguloInicial-i*math.pi/2
                punto1 = centro[0] + self.lado/2 * math.sqrt(2) * math.cos(angulo), centro[1] + self.lado/2 * math.sqrt(2) * math.sin(angulo)
                punto2 = centro[0] + self.lado/2 * math.sqrt(2) * math.cos(angulo+math.pi/2), centro[1] + self.lado/2 * math.sqrt(2) * math.sin(angulo+math.pi/2)

                pared = Pared(punto1, punto2, self.lado)
                # angulo -= math.pi/2
                self.listaParedes.append(pared)

        if punto[0] < rango - 1 and punto[1] == rango - 1:
            for i in range(0, 3):
                angulo=anguloInicial-i*math.pi/2
                punto1 = centro[0] + self.lado/2 * math.sqrt(2) * math.cos(angulo), centro[1] + self.lado/2 * math.sqrt(2) * math.sin(angulo)
                punto2 = centro[0] + self.lado/2 * math.sqrt(2) * math.cos(angulo+math.pi/2), centro[1] + self.lado/2 * math.sqrt(2) * math.sin(angulo+math.pi/2)

                pared = Pared(punto1, punto2, self.lado)
                # angulo -= math.pi/2
                self.listaParedes.append(pared)

        if punto[0] == rango - 1 and punto[1] == rango - 1:
            for i in range(0, 4):
                angulo = anguloInicial - i * math.pi / 2
                punto1 = centro[0] + self.lado/2 * math.sqrt(2) * math.cos(angulo), centro[1] + self.lado/2 * math.sqrt(2) * math.sin(angulo)
                punto2 = centro[0] + self.lado/2 * math.sqrt(2) * math.cos(angulo+math.pi/2), centro[1] + self.lado/2 * math.sqrt(2) * math.sin(angulo+math.pi/2)

                pared = Pared(punto1, punto2, self.lado)
                # angulo -= math.pi/2
                self.listaParedes.append(pared)



    def dibuja(self):
        for pared in self.listaParedes:
            pared.dibuja()

        glColor3fv(self.color)
        glRectf(self.punto[0], self.punto[1], self.punto[0]+self.lado, self.punto[1]+self.lado)



        """Lineas en el centro de las baldosas"""
        # if self.primero:
        #     glBegin(GL_LINES)
        #     glVertex3f(self.centro[0],self.centro[1], 0)
        #     glVertex3f(self.centro[0],self.centro[1], 5)
        #     glEnd()
