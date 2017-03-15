import random
class Matriz:
    __rango = 3

    haySalida = False

    def __init__(self):
        self.elemento = [[0 for x in range(self.__rango)] for y in range(self.__rango)]
        #la entrada se hace siempre por el norte de elemento 0,0
        for i in range(self.__rango):
            for j in range(self.__rango):
                # TODO forzar a que el primer elemento tenga entrada
                self.elemento[i][j] = random.randrange(7)
    def imprime(self):
        for i in range(3):
            for j in range(3):
                print(self.elemento[i][j], end="")
            print("\n")