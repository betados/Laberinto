# -*- coding: utf-8 -*-
from Matriz import Matriz
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *  # trigonometry
import pygame  # just to get a display

# Definimos algunos colores
NEGRO = (0, 0, 0)
pygame.init()
pantalla = pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Laberinto")
# Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()


# COSAS DEL OPENGL--------------------------------------
glClearColor(0.0, 0.0, 0.0, 1.0)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
# Get a perspective at the helix
glMatrixMode(GL_PROJECTION);
glLoadIdentity()
gluPerspective(90, 1, 0.01, 1000)
gluLookAt(0,  0, 25, #pos
          1, 0, -100, #hacia donde mira
          0, 0, 1) # eje vertical
CameraPos = [40.0,50.0,40.0]
# Draw the helix (this ought to be a display list call)
glMatrixMode(GL_MODELVIEW)
glEnable(GL_BLEND);
glBlendFunc(GL_SRC_ALPHA, GL_ONE);  # XXX Why GL_ONE?
glEnable(GL_TEXTURE_2D);
# COSAS DEL OPENGL-----------------------------------

matriz = Matriz()
done = False
pulsado=False


x=0
y=0


# -------- Bucle principal del Programa -----------
while not done:

    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            done = True
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pass
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                pass
                # gluLookAt(1, 1, 1, 0, 0, 0, 0, 0, 1)



        # if tecla cambia el punto de vista:
            # gluLookAt(3, 3, 3, 0, 0, 0, 0, 0, 1)




    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
    incremento=0.00000001
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        x=x+0.2
    if teclas[pygame.K_a]:
        y=y+0.2
    if teclas[pygame.K_s]:
        x=x-0.2
    if teclas[pygame.K_d]:
        y=y-0.2

    t=reloj.get_time()
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity()
    gluPerspective(90, 1, 0.01, 1000)
    gluLookAt(x, y, 1,  # pos
              1000, 0, 1,  # hacia donde mira
              0, 0, 1)  # eje vertical


    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ

    glClearColor(0.0, 0.0, 0.0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # dibuja suelo

    # gluLookAt(x+3, y+3, 3,0, 0, 0, 0, 0, 1)
    matriz.dibuja()
    # use the texture
    # vertices & texture data






    # print(reloj.get_time())
    # listaGranos.actualiza(reloj.get_time())
    # listaGranos.dibuja()

    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.

    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    # print("iteracion")
    reloj.tick(20)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()


