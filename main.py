def csv_to_dict(file: str) -> list:
    """
    dict = [ ... , {
            'ID': <int>,
            'Name': <str>,
            'Type 1': <str>,
            'Type 2': <str>,
            'Total': <int>,
            'HP': <int>,
            'Attack': <int>,
            'Defense': <int>,
            'Sp. Atk': <int>,
            'Sp. Def': <int>,
            'Speed': <int>,
            'Generation': <int>,
            'Legendary': <bool>,
    }, ... ]
    len(dict) = 45
    """
    import csv

    with open(file, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        dict = [row for row in reader]
    return dict
from constante import *
from random import *

dict = csv_to_dict('dataset_pokemon.csv')

import pygame
from pygame.locals import *

def liste_personnages(dict: list) -> dict:
    L = []
    for k in range(len(dict)):
        L.append(dict[k]["Name"])
    return L

def selection_par_nom(nom: str) -> dict:
    for k in range(len(dict)):
        if dict[k]["Name"] == nom:
            return dict[k]
        
def generer_grille_pokemon(x, y):
    for sprite in range(0, len(dict)):
        if sprite == 9 or sprite == 18 or sprite == 27 or sprite == 36:
            y += taille_sprite
            x = 50
        image_pokemon = "images/" + dict[sprite]["Name"] + ".png"
        image = pygame.image.load(image_pokemon).convert_alpha()
        image = pygame.transform.scale(image, (taille_sprite, taille_sprite))
        fenetre_jeu.blit(image, (x, y))
        x += taille_sprite + 58
    image_pokemon = "images/system/red_rectangle.png"
    image = pygame.image.load(image_pokemon).convert_alpha()
    image = pygame.transform.scale(image, (832, 150))
    fenetre_jeu.blit(image, (50, 850))

    image_pokemon = "images/system/blue_rectangle.png"
    image = pygame.image.load(image_pokemon).convert_alpha()
    image = pygame.transform.scale(image, (832, 150))
    fenetre_jeu.blit(image, (1032, 850))

    image_pokemon = "images/system/random.png"
    image = pygame.image.load(image_pokemon).convert_alpha()
    image = pygame.transform.scale(image, (100, 100))
    fenetre_jeu.blit(image, (907, 875))
    pygame.image.save(fenetre_jeu, 'grille.bmp')

generer_grille_pokemon(x, y)

def creation_fenetre():
    """
    On créé et affiche la fenètre de jeu à laquelle on la grille des pokémons.
    """
    pygame.draw.rect(fenetre_jeu, Color("#000000"), (0, 0, 1920, 1080), 0)
    pygame.display.set_caption('Pokédex')
    image_niveau = "grille.bmp"
    fond_niveau = pygame.image.load(image_niveau).convert_alpha()
    fond_niveau = pygame.transform.scale(fond_niveau, (1920, 1080))
    fenetre_jeu.blit(fond_niveau, (0, 0))
    pygame.display.flip()

pygame.init()
creation_fenetre()

continuer_la_boucle = True

def afficher_pokemon(x, y, team):
    if x == y and x == -1:
        pokemon_id = randint(0, 44)
    else:
        pokemon_id = y*9+x
    image_pokemon = "images/system/" + team + "_rectangle.png"
    image = pygame.image.load(image_pokemon).convert_alpha()
    image = pygame.transform.scale(image, (832, 150))
    if team == "blue":
        fenetre_jeu.blit(image, (1032, 850))
    if team == "red":
        fenetre_jeu.blit(image, (50, 850))
    # image Pokémon
    image_pokemon = "images/" + dict[pokemon_id]["Name"] + ".png"
    image_pokemon = pygame.image.load(image_pokemon).convert_alpha()
    image_pokemon = pygame.transform.scale(image_pokemon, (taille_sprite, taille_sprite))
    # nom + ID + Gen Pokémon
    my_font = pygame.font.SysFont('Arial', 25)
    nom_pokemon = my_font.render("Name : " + dict[pokemon_id]["Name"] + " | N°" + dict[pokemon_id]["ID"] + " | Gen : " + dict[pokemon_id]["Generation"], False, (255, 255, 255))
    if dict[pokemon_id]["Type 2"] == "":
        types_pokemon = my_font.render("Type : " + dict[pokemon_id]["Type 1"], False, (255, 255, 255))
    else:
        types_pokemon = my_font.render("Types : " + dict[pokemon_id]["Type 1"] + " and " + dict[pokemon_id]["Type 2"], False, (255, 255, 255))
    if team == "blue":
        fenetre_jeu.blit(image_pokemon, (1032, 850))
        fenetre_jeu.blit(nom_pokemon, (1207, 860))
        fenetre_jeu.blit(types_pokemon, (1207, 890))
    if team == "red":
        fenetre_jeu.blit(image_pokemon, (50, 850))
        fenetre_jeu.blit(nom_pokemon, (225, 860))
        fenetre_jeu.blit(types_pokemon, (225, 890))
    pygame.font.init()
    pygame.display.flip()
    return pokemon_id

while continuer_la_boucle:

    pygame.init()   
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            continuer_la_boucle = False
        if event.type == MOUSEBUTTONDOWN:
            if 50 <= event.pos[0] <= 1864 and 50 <= event.pos[1] <= 800:
                y_grille = (event.pos[1]-50)//taille_sprite
                if 50 <= event.pos[0] <= 200:
                    x_grille = 0
                if 256 <= event.pos[0] <= 408:
                    x_grille = 1
                if 466 <= event.pos[0] <= 616:
                    x_grille = 2
                if 674 <= event.pos[0] <= 824:
                    x_grille = 3
                if 882 <= event.pos[0] <= 1032:
                    x_grille = 4
                if 1090 <= event.pos[0] <= 1240:
                    x_grille = 5
                if 1298 <= event.pos[0] <= 1448:
                    x_grille = 6
                if 1506 <= event.pos[0] <= 1656:
                    x_grille = 7
                if 1714 <= event.pos[0] <= 1864:
                    x_grille = 8
                if 1714 <= event.pos[0] <= 1864:
                    x_grille = 8
                if event.button == 1:
                    afficher_pokemon(x_grille, y_grille, "red")
                elif event.button == 3:
                    afficher_pokemon(x_grille, y_grille, "blue")
            # random
            if 907 <= event.pos[0] <= 1007 and 875 <= event.pos[1] <= 975:
                if event.button == 1:
                    afficher_pokemon(-1, -1, "red")
                elif event.button == 3:
                    afficher_pokemon(-1, -1, "blue")

pygame.quit()