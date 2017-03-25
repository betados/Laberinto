import random
from Suelo import Suelo
from baldosa import Baldosa
from OpenGL.GL import *


class Matriz:
    __rango =4
    lado = 3
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
        #print(self.listaCamino)
        self.suelo.quitaParedes(self.listaCamino)

    def getZ(self):
        return self.lado/2

    def dibuja(self, rojo=0):
        self.suelo.dibuja(self.debugueandoEnOficina)


        """camino"""
        glColor3f(0, 0, 1)
        glBegin(GL_LINE_LOOP)
        for elemento in self.listaCamino:
            glVertex2f(elemento[0]*+self.lado+self.lado/2, elemento[1]*+self.lado+self.lado/2)
        glEnd()


    def camino(self):

        tryAgain = True

        while tryAgain:
            i = 0
            x = 0
            y = 0
            xAnt = 0
            yAnt = 0
            lista = [(x, y)]
            while x != self.__rango - 1 or y != self.__rango - 1:
                tryAgain = False
                aleatorioD = random.randrange(4)
                if aleatorioD == 0:
                    x += 1
                if aleatorioD == 1:
                    y += 1
                if aleatorioD == 2:
                    x -= 1
                if aleatorioD == 3:
                    y -= 1

                if x < 0:
                    x = 0
                if x > self.__rango - 1:
                    x = self.__rango - 1

                if y < 0:
                    y = 0
                if y > self.__rango - 1:
                    y = self.__rango - 1

                sePuedeApendear = False
                if (x, y) != lista[len(lista)-1]:
                    for elemento in lista:
                        if (x, y) == elemento:
                            sePuedeApendear = False
                            break
                        sePuedeApendear = True

                    # FIXME hacer que SI pueda volver sobre sus pasos para crear callejones sin salida
                    # fixme se supone que esto lo hace pero NO
                    if (x, y) == (xAnt, yAnt):
                        sePuedeApendear = True
					#fixme quiza no haya que dejarle volver sobre sus pasos si no permitir que en una baldosa 
					# haya una bifurcación que más tarde muera sin salida

                if sePuedeApendear:
                    lista.append((x, y))
                    xAnt=x
                    yAnt=y
                else:
                    x = xAnt
                    y = yAnt

                i += 1
                if i == 999:
                    tryAgain = True
                    break
                #lista.pop(i)


        #print(lista)
        return lista
