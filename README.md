# labyrinthe.py

import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640,640))

perso = pygame.image.load("Macgyver.PNG").convert()
position_perso = perso.get_rect() #pour utiler les fleches du clavier
fenetre.blit(perso,(perso, position_perso))

pygame.display.flip()

contibuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0

