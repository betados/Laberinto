import random
from Suelo import Suelo
from baldosa import Baldosa
from OpenGL.GL import *


class Matriz:
    __rango =3
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
        self.suelo.quitaParedes(self.listaCamino)

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
        x = 0
        y = 0
        lista = [(x, y)]

        while x != self.__rango - 1 or y != self.__rango - 1:
            # TODO hacer que no pueda volver a una baldosa donde ya estuvo salvo que sea retroceder por su camino

            # fixme en vez de hacer la aleatoriedad sobre la x e y por separado creo que sería mejor hacer la aleatoriedad
            # fixme sobre la direccíon a tomar y luego en base a ella actualizar la x e y

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



            # print("x: ", x,"   y: ", y)

        # print("FIN:   x: ", x, "   y: ",y, "     RANGO: ", self.__rango)
        # todo quitar los repetidos de la lista
        print(lista)
        for i, elemento in enumerate(lista):
            if i != 0:
                if elemento == lista[i-1]:
                    lista.pop(i)
        return lista
