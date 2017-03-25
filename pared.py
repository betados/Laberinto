import random
from OpenGL.GL import *


class Pared:

    def __init__(self, origen, final, entreCuales, alto=1):
        self.entreCuales = entreCuales
        self.alto = alto
        self.origen = origen
        self.final = final
        # self.color = random.randrange(2), random.randrange(2), random.randrange(2)

        #FIXME que los colores no sean transparentes
        #fixme si lo son que sean "sustractivos" y que cada vez sea más negro, no cada vez más blanco
        self.color = random.randrange(256)/255, random.randrange(256)/255, random.randrange(256)/255
        self.colorOficina = random.randrange(2)/50, random.randrange(2)/40, random.randrange(2)/50

    def dibuja(self, debugueandoEnOficina):
        # color=GLfloat_3(random.randrange(256)/255,random.randrange(256)/255,random.randrange(256)/255)


        # glDisable(GL_LIGHTING)
        # glColor3f(random.randrange(256)/255, random.randrange(256)/255, random.randrange(256)/255)
        if debugueandoEnOficina:
            glColor3fv(self.colorOficina)
        else:
            glColor3fv(self.color)
        glBegin(GL_POLYGON)
        glVertex3f(self.origen[0], self.origen[1], 0)
        glVertex3f(self.final[0], self.final[1], 0)
        glVertex3f(self.final[0], self.final[1], self.alto)
        glVertex3f(self.origen[0], self.origen[1], self.alto)
        glEnd()

        # glEnable(GL_LIGHTING)
        # glBegin(GL_TRIANGLE_STRIP)
        # glEnd()
        # glFlush()
    def getEntreCuales(self):
        return self.entreCuales