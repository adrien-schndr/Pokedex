import pygame
from pygame.locals import *

for k in range(15):
    print("")
# fullscreen_bool = input("Bienvenue ! \nMode plein écran ?\nATTENTION : Ne fonctionne que si le paramètre d'échelle dans Windows est à 100% (Paramètres Windows -> Affichage/Ecran -> Echelle)\nPour quitter ou si vous avez des difficultés à lancer le jeu, appuyez sur <Echap>\nRéponse boléenne (True/False) : ")
# if fullscreen_bool == "True":
fenetre_jeu = pygame.display.set_mode((1920, 1080),pygame.SCALED | pygame.FULLSCREEN)
# else:
#     fenetre_jeu = pygame.display.set_mode((1920, 1080))
taille_sprite = 150
x = 50
y = 50