
import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((480,540))

perso = pygame.image.load("Macgyver.png").convert()
position_perso = perso.get_rect() #pour utiler les fleches du clavier
fenetre.blit(perso,(perso, position_perso))

while continuer_accueil:
	
	#Limitation de vitesse de la boucle
	pygame.time.Clock().tick(30)
	
	for event in pygame.event.get():
		
		#Si l'utilisateur quitte, on met les variables 
		#de boucle à 0 pour n'en parcourir aucune et fermer
		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			continuer_accueil = 0
			continuer_jeu = 0
			continuer = 0
			#Variable de choix du niveau
			choix = 0
				
		elif event.type == KEYDOWN:				
			#Lancement du jeu
			if event.key == K_F1:
				continuer_accueil = 1	
			
		

	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
	if choix != 0:
		#Chargement du fond
		fond = pygame.image.load("tile-crusader-logo.png").convert()

pygame.display.flip() #rafraichir

contibuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                position_perso = position_perso.move(0,36)#a completer
            if event.key == K_UP:
                position_perso = position_perso.move(0,-36)# a completer
            if event.key == K_Left:
                position_perso = position_perso.move(-32,0)# a completer
            if event.key == K_RIGHT:
                position_perso = position_perso.move(32,O) # a completer

