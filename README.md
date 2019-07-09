# labyrinthe.py

import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((4800,540))

perso = pygame.image.load("Macgyver.PNG").convert()
position_perso = perso.get_rect() #pour utiler les fleches du clavier
fenetre.blit(perso,(perso, position_perso))

pygame.display.flip()

contibuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                position_perso = position_perso.move(0,36)
            if event.key == K_UP:
                position_perso = position_perso.move(0,-36)
            if event.key == K_Left:
                position_perso = position_perso.move(-32,0)
            if event.key == K_RIGHT:
                position_perso = position_perso.move(32,O) 

