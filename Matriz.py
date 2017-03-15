import random
from OpenGL.GL import *
from OpenGL.GLU import *
class Matriz:
    __rango = 15

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

    def dibuja(self,rojo=0):
        white=GLfloat_3(1, 1, 1)
        black=GLfloat_3(0, 0, 0)
        """Draw an 2N*2N checkerboard with given colours"""
        glDisable(GL_LIGHTING)
        try:
            for x in range(-self.__rango,self.__rango):
                for y in range(-self.__rango, self.__rango):
                    if (x + y) % 2 == 0:
                        glColor3f(0.3, 0.1, 1)
                    else:
                        glColor3fv(black)
                    glRectf(x, y, x + 1, y + 1)
        finally:
            glEnable(GL_LIGHTING)
            glBegin(GL_TRIANGLE_STRIP);
            glEnd();
            glFlush()