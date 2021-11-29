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

#MODELOS
mesa = Model('mesa.obj', 'gun.bmp')
mesa.position.z = -5
gun = Model('pichu.obj', 'gun.bmp')
gun.position.z = -8
cafe = Model('cafe.obj', 'model.bmp')
cafe.position.z = -2
Wolf = Model('Wolf.obj', 'gun.bmp')
Wolf.position.z = -3


rend.scene.append( mesa )

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
        print(rend.camPosition.z)
    elif rend.camPosition.z >= 2:
        rend.camPosition.z = 1
    if mouse[0]:
        rend.camPosition.z -= 1 * deltaTime
        print(rend.camPosition.z)
    elif rend.camPosition.z <= -2.0:
        rend.camPosition.z = 1
       
    if keys[K_w]:
        rend.camPosition.y -= 1 * deltaTime
    if keys[K_s]:
        rend.camPosition.y += 1 * deltaTime
    

    # Cambio de Modelos
    if keys[K_y]:
        rend.scene.clear()
        rend.scene.append( mesa )
    if keys[K_u]:
        rend.scene.clear()
        rend.scene.append( gun )
    if keys[K_i]:
        rend.scene.clear()
        rend.scene.append( cafe )
    if keys[K_o]:
        rend.scene.clear()
        rend.scene.append( Wolf )
    #Cambio de Shaders
    if keys[K_h]:
        rend.setShaders(shaders.vertex_shader, shaders.blanco)
    if keys[K_j]:
        rend.setShaders(shaders.vertex_shader, shaders.amarillo)
    if keys[K_k]:
        rend.setShaders(shaders.vertex_shader, shaders.Gris)
    if keys[K_l]:
        rend.setShaders(shaders.vertex_shader, shaders.green)

 








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
