import random
from OpenGL.GL import *
class Pared:
    def __init__(self, origen, final, alto=1):
        self.alto=alto
        self.origen=origen
        self.final=final
        pass

    def dibuja(self):
        # color=GLfloat_3(random.randrange(256)/255,random.randrange(256)/255,random.randrange(256)/255)


        # glDisable(GL_LIGHTING)
        glColor3f(random.randrange(256)/255, random.randrange(256)/255, random.randrange(256)/255)
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