from OpenGL.raw.GL.VERSION.GL_1_0 import GL_GREEN
import pygame
from pygame.locals import *
import numpy as np
from gl import Renderer, Model
import shaders


width = 960
height = 540

deltaTime = 0.0
pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )
clock = pygame.time.Clock()


rend = Renderer(screen)
rend.setShaders(shaders.vertex_shader, shaders.blanco)

face = Model('mesa.obj', 'gun.bmp')
face.position.z = -5

rend.scene.append( face )
rolas=['zelad.mp3']
pygame.mixer.music.load(rolas[0])
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


#bg= pygame.image.load("space.jpg").convert()


#white = [255, 255, 255]



isRunning = True
while isRunning:    

    #screen.blit(bg,0,0)

    pygame.mixer.music.fadeout(99999)
    pygame.display.set_caption("OPENGL Diego Proyecto 4")

    
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    mouse2 = pygame.MOUSEBUTTONDOWN;

        

    # Traslacion de camara
    if keys[K_d]:
        rend.camPosition.x += 1 * deltaTime
    if keys[K_a]:
        rend.camPosition.x -= 1 * deltaTime
    if mouse[2]:
        rend.camPosition.z += 1 * deltaTime
    elif rend.camPosition.z >= 4.5:
        rend.camPosition.z = 1
    if mouse[0]:
        rend.camPosition.z -= 1 * deltaTime
    elif rend.camPosition.z <= -4.5:
        rend.camPosition.z = 1
    if keys[K_w]:
        rend.camPosition.y -= 1 * deltaTime
    if keys[K_s]:
        rend.camPosition.y += 1 * deltaTime
            

    if keys[K_LEFT]:
        if rend.valor > 0:
            rend.valor -= 0.1 * deltaTime

    if keys[K_RIGHT]:
        if rend.valor < 0.2:
            rend.valor += 0.1 * deltaTime

    # Rotacion de camara
    if keys[K_z]:
        rend.camRotation.y += 15 * deltaTime
        rend.camPosition.x += 1.5 * deltaTime
    if keys[K_x]:
        rend.camRotation.y -= 15 * deltaTime
        rend.camPosition.x -= 1.5 * deltaTime

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False

        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                isRunning = False

            if ev.key == K_1:
                rend.filledMode()
            if ev.key == K_2:
                rend.wireframeMode()

    rend.tiempo += deltaTime
    deltaTime = clock.tick(60) / 1000

    rend.render()

    pygame.display.flip()

pygame.quit()
