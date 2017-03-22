import random
from Suelo import Suelo
from baldosa import Baldosa
from OpenGL.GL import *


class Matriz:
    __rango =5
    lado = 1
    suelo = Suelo()

    haySalida = False

    def __init__(self):
        for x in range(0, self.__rango):
            for y in range(0, self.__rango):
                print("x: ", x, "   y: ", y)
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


    def imprime(self):

        for i in range(3):
            for j in range(3):
                print(self.elemento[i][j], end="")
            print("\n")

    def getZ(self):
        return self.lado/2
        return 5

    def dibuja(self, rojo=0):
        self.suelo.dibuja()
