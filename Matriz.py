import random
from Suelo import Suelo
from baldosa import Baldosa
from OpenGL.GL import *


class Matriz:
    __rango =5
    lado = 1
    suelo = Suelo()

    listaCamino = []

    haySalida = False

    def __init__(self,debugueandoEnOficina):
        self.debugueandoEnOficina = debugueandoEnOficina
        for x in range(0, self.__rango):
            for y in range(0, self.__rango):
                baldosa = Baldosa((x, y), self.lado, self.__rango)
                self.suelo.add(baldosa)
                # baldosa = Baldosa([
                #     [self.lado * x, self.lado * y],
                #     [self.lado * (x + 1), self.lado * (y + 1)]
                # ],contador,self.lado)
                # baldosa = Baldosa([
                #     [self.lado * x, self.lado * y],
                #     [self.lado * (x+1), self.lado * y],
                #     [self.lado * (x + 1), self.lado * (y + 1)],
                #     [self.lado * x, self.lado * (y+1)]
                # ])
        self.listaCamino = self.camino()
        print(self.listaCamino)

    def getZ(self):
        return self.lado/2
        return 5

    def dibuja(self, rojo=0):
        self.suelo.dibuja(self.debugueandoEnOficina)


        """camino"""
        glColor3f(0, 0, 1)
        glBegin(GL_LINE_LOOP)
        for elemento in self.listaCamino:
            glVertex2f(elemento[0]+self.lado/2, elemento[1]+self.lado/2)
        glEnd()


    def camino(self):
        lista = []
        x=0
        y=0
        while x != self.__rango - 1 or y != self.__rango - 1:
            aleatorioX = random.randrange(-1, 2)
            x += aleatorioX
            if x < 0:
                x = 0
            if x > self.__rango - 1:
                x = self.__rango - 1
            lista.append((x, y))

            aleatorioY = random.randrange(-1, 2)
            y += aleatorioY
            if y < 0:
                y = 0
            if y > self.__rango - 1:
                y = self.__rango - 1

            lista.append((x, y))

            #todo quitar los repetidos de la lista

            # print("x: ", x,"   y: ", y)

        print("FIN:   x: ", x, "   y: ",y, "     RANGO: ", self.__rango)
        return lista
