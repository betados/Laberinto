import random
from pared import Pared
from Suelo import Suelo
from baldosa import Baldosa
from OpenGL.GL import *


class Matriz:
    __rango =2
    lado = 1
    suelo = Suelo()
    pared = Pared((0, 0), (1, 1), lado)

    haySalida = False

    def __init__(self):
        self.elemento = [[0 for x in range(self.__rango)] for y in range(self.__rango)]
        # la entrada se hace siempre por el norte de elemento 0,0
        for i in range(self.__rango):
            for j in range(self.__rango):
                # TODO forzar a que el primer elemento tenga entrada
                self.elemento[i][j] = random.randrange(4)
                # TODO crear baldosas
                contador = 0
                for x in range(0, self.__rango):
                    for y in range(0, self.__rango):
                        baldosa = Baldosa((x,y),contador,self.lado)
                        # baldosa = Baldosa([
                        #     [self.lado * x, self.lado * y],
                        #     [self.lado * (x + 1), self.lado * (y + 1)]
                        # ],contador,self.lado)
                        contador+=1
                        # baldosa = Baldosa([
                        #     [self.lado * x, self.lado * y],
                        #     [self.lado * (x+1), self.lado * y],
                        #     [self.lado * (x + 1), self.lado * (y + 1)],
                        #     [self.lado * x, self.lado * (y+1)]
                        # ])
                        self.suelo.add(baldosa)

    def imprime(self):

        for i in range(3):
            for j in range(3):
                print(self.elemento[i][j], end="")
            print("\n")

    def dibuja(self, rojo=0):

        white = GLfloat_3(1, 1, 1)
        black = GLfloat_3(0, 0.2, 0.2)
        """Draw an 2N*2N checkerboard with given colours"""

        #
        try:
            # glDisable(GL_LIGHTING)
            # for x in range(0, self.__rango):
            #     for y in range(0, self.__rango):
            #         if (x + y) % 2 == 0:
            #             glColor3f(0.4, 0.0, 1)
            #         else:
            #             glColor3fv(black)
            #         glRectf(self.lado * x, self.lado * y,  self.lado * (x + 1),  self.lado * (y + 1))
            #
            #
            # # )
            pass
        finally:

            self.suelo.dibuja()

            # self.pared.dibuja()




