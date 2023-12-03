from copy import deepcopy

from pygame.locals import *

from fight_system import *
from random import randint

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


# ---------------------------------------------- DICTIONNARY FUNCTIONS ---------------------------------------------- #
# On transfrome le fichier dataset_pokemon.csv en une liste de dictionnaire telle que :
# dico_personnages = [..., {}, ...]

def csv_to_dict(file: str) -> list:
    import csv

    with open(file, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        dictionnary = [row for row in reader]
    return dictionnary


dico_personnages = csv_to_dict('dataset_pokemon.csv')
dict_chosen_characters = {"Attack": [], "Defense": []}


# noinspection PyArgumentEqualDefault
def affiche_dico(dico):
    print("----------------------------------------")
    for pokemon in dico:
        for cle, val in pokemon.items():
            print(str(cle).center(20), end=" ")
            print(str(val).center(20), end="\n")
        print("----------------------------------------")


# affiche_dico(dico_personnages)


# ------------------------------------------------ USELESS FUNCTIONS ------------------------------------------------ #


def liste_personnages(dict_pokemon: list) -> list:
    liste = []
    for _ in range(len(dict_pokemon)):
        liste.append(dict_pokemon[k]["Name"])
    return liste


def selection_par_nom(nom: str):
    for _ in range(len(dict)):
        if dico_personnages[_]["Name"] == nom:
            return deepcopy(dict[_])


def selection_attaque(dict_pokemon: dict, n: int) -> list:
    liste = []
    for _ in range(len(dict_pokemon)):
        if dict_pokemon[_]["Attack"] == n:
            liste.append(dict_pokemon[_])
    return liste


def selection_vitesse(dict_pokemon: dict, n: int) -> list:
    liste = []
    for _ in range(len(dict_pokemon)):
        if dict_pokemon[_]["Speed"] >= n:
            liste.append(dict_pokemon[_])
    return liste


# noinspection PyCompatibility
def selection(dico: list, champ: str, operateur: str, n: str, type_data="str"):
    L = []
    for pokemon in range(0, len(dico)):
        if eval(f"{type_data}('{dico[pokemon][champ]}') {operateur} {type_data}('{n}')"):
            L.append(dico[pokemon]["Name"])
    return L


# print(selection(dico_personnages, "Speed", "<=", "60", type_data="int"))


def generer_grille_pokemon(x_coord, y_coord):
    """
    On génère la grille de séléction des Pokémon que l'on exporte en grille.bmp, à l'aide du dictionnaire en récupérant
    les Noms des personnages auquels ont associe le fichier .png éponyme.
    """
    image_pokemon = "background.png"
    image = pygame.image.load(image_pokemon).convert_alpha()
    image = pygame.transform.scale(image, (1920, 1080))
    fenetre_jeu.blit(image, (0, 0))
    for sprite in range(0, len(dico_personnages)):
        if sprite == 9 or sprite == 18 or sprite == 27 or sprite == 36:
            y_coord += taille_sprite
            x_coord = 50
        image_pokemon = "images/" + dico_personnages[sprite]["Name"] + ".png"
        image = pygame.image.load(image_pokemon).convert_alpha()
        image = pygame.transform.scale(image, (taille_sprite, taille_sprite))
        fenetre_jeu.blit(image, (x_coord, y_coord))
        x_coord += taille_sprite + 58
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

    image_pokemon = "images/system/chosen_character_blue.png"
    image = pygame.image.load(image_pokemon).convert_alpha()
    image = pygame.transform.scale(image, (100, 100))
    fenetre_jeu.blit(image, (1789, 925))
    pygame.image.save(fenetre_jeu, 'grille.bmp')

    image_pokemon = "images/system/chosen_character_red.png"
    image = pygame.image.load(image_pokemon).convert_alpha()
    image = pygame.transform.scale(image, (100, 100))
    fenetre_jeu.blit(image, (807, 925))
    pygame.image.save(fenetre_jeu, 'grille.bmp')


generer_grille_pokemon(x, y)


def creation_fenetre_jeu():
    """
    On créé et affiche la fenètre de jeu à laquelle on ajoute la grille des pokémons.
    """
    pygame.draw.rect(fenetre_jeu, Color("#000000"), (0, 0, 1920, 1080))
    pygame.display.set_caption('Pokédex')
    image_niveau = "grille.bmp"
    fond_niveau = pygame.image.load(image_niveau).convert_alpha()
    fond_niveau = pygame.transform.scale(fond_niveau, (1920, 1080))
    fenetre_jeu.blit(fond_niveau, (0, 0))
    pygame.display.flip()


def creation_menu():
    """
    Initialise le menu du jeu
    """
    image_niveau = "menu.png"
    fond_niveau = pygame.image.load(image_niveau).convert_alpha()
    fond_niveau = pygame.transform.scale(fond_niveau, (1920, 1080))
    fenetre_jeu.blit(fond_niveau, (0, 0))
    pygame.display.flip()


pygame.init()
creation_menu()

running = True


def afficher_pokemon(x_coord, y_coord, team):
    """
    Affiche en bas de l'écran les informations du Pokémon sélectionné, equipe rouge si choisi avec clic gauche, équipe
    bleue si choisi avec clic droit.
    """
    if x_coord == y_coord and x_coord == -1:
        pokemon_id = randint(0, 44)
    else:
        pokemon_id = y_coord * 9 + x_coord
    image_pokemon = "images/system/" + team + "_rectangle.png"
    image = pygame.image.load(image_pokemon).convert_alpha()
    image = pygame.transform.scale(image, (832, 150))
    if team == "blue":
        fenetre_jeu.blit(image, (1032, 850))
    if team == "red":
        fenetre_jeu.blit(image, (50, 850))
    #  image Pokémon
    image_pokemon = "images/" + dico_personnages[pokemon_id]["Name"] + ".png"
    image_pokemon = pygame.image.load(image_pokemon).convert_alpha()
    image_pokemon = pygame.transform.scale(image_pokemon, (taille_sprite, taille_sprite))
    # noinspection PyShadowingNames
    my_font = pygame.font.SysFont('Arial', 25)
    # nom + ID + Gen Pokémon
    nom_pokemon = my_font.render(
        "Name : " + dico_personnages[pokemon_id]["Name"] + " | N°" + dico_personnages[pokemon_id]["ID"] + " | Gen : " +
        dico_personnages[pokemon_id]["Generation"], False, (255, 255, 255))
    if dico_personnages[pokemon_id]["Type 2"] == "":
        types_pokemon = my_font.render("Type : " + dico_personnages[pokemon_id]["Type 1"], True, (255, 255, 255))
    else:
        types_pokemon = my_font.render(
            "Types : " + dico_personnages[pokemon_id]["Type 1"] + " and " + dico_personnages[pokemon_id]["Type 2"],
            False, (255, 255, 255))
    stat = my_font.render("Attack : " + dico_personnages[pokemon_id]["Attack"] + " | Speed : " +
                          dico_personnages[pokemon_id]["Speed"], False, (255, 255, 255))
    stat2 = my_font.render("Health Points : " + dico_personnages[pokemon_id]["HP"] + " | Defense : " +
                           dico_personnages[pokemon_id]["Defense"], False, (255, 255, 255))
    if team == "blue":
        fenetre_jeu.blit(image_pokemon, (1032, 850))
        fenetre_jeu.blit(nom_pokemon, (1207, 860))
        fenetre_jeu.blit(types_pokemon, (1207, 890))
        fenetre_jeu.blit(stat, (1207, 920))
        fenetre_jeu.blit(stat2, (1207, 950))
    if team == "red":
        fenetre_jeu.blit(image_pokemon, (50, 850))
        fenetre_jeu.blit(nom_pokemon, (225, 860))
        fenetre_jeu.blit(types_pokemon, (225, 890))
        fenetre_jeu.blit(stat, (225, 920))
        fenetre_jeu.blit(stat2, (225, 950))

    image_pokemon = "images/system/chosen_character_blue.png"
    image = pygame.image.load(image_pokemon).convert_alpha()
    image = pygame.transform.scale(image, (100, 100))
    fenetre_jeu.blit(image, (1789, 925))

    image_pokemon = "images/system/chosen_character_red.png"
    image = pygame.image.load(image_pokemon).convert_alpha()
    image = pygame.transform.scale(image, (100, 100))
    fenetre_jeu.blit(image, (807, 925))
    pygame.display.flip()
    pygame.font.init()
    return pokemon_id


# noinspection PyShadowingNames
def choisir_pokemon(side: str) -> list:
    """
    Ajoute le Pokémon (son dictionnaire) choisi quand cliqué sur le bouton "valider" de l'équipe au dictionnaire
    dict_chosen_characters dans la clé de l'équipe associée dont la valeur est une liste de dictionnaires tel que
    dict = {
        "Attack": [
            {
                stats
            }
        ]
    }
    """
    if side == "Attack":
        x = 50
    else:
        x = 1032
    if id_chosen != -1 and 0 <= len(dict_chosen_characters[side]) < 3:
        dict_chosen_characters[side].append(dico_personnages[id_chosen])
        dict_chosen_characters[side][-1]["Base HP"] = dict_chosen_characters[side][-1]["HP"]
        if len(dict_chosen_characters[side]) == 1:
            my_font = pygame.font.SysFont('Arial', 25)
            attaquants_new = my_font.render(
                "Pokemon choisis : " + str(dict_chosen_characters[side][0]["Name"]),
                True, (255, 255, 255))
            fenetre_jeu.blit(attaquants_new, (x, 1000))
            pygame.display.flip()
        if len(dict_chosen_characters[side]) == 2:
            my_font = pygame.font.SysFont('Arial', 25)
            attaquants_old = my_font.render(
                "Pokemon choisis : " + str(dict_chosen_characters[side][0]["Name"]),
                True, (0, 0, 0))
            fenetre_jeu.blit(attaquants_old, (x, 1000))
            attaquants_new = my_font.render("Pokemon choisis : " + str(
                dict_chosen_characters[side][0]["Name"]) + " - " + str(
                dict_chosen_characters[side][1]["Name"]), True, (255, 255, 255))
            fenetre_jeu.blit(attaquants_new, (x, 1000))
        if len(dict_chosen_characters[side]) == 3:
            my_font = pygame.font.SysFont('Arial', 25)
            attaquants_old = my_font.render("Pokemon choisis : " + str(
                dict_chosen_characters[side][0]["Name"]) + " - " + str(
                dict_chosen_characters[side][1]["Name"]), True, (0, 0, 0))
            fenetre_jeu.blit(attaquants_old, (x, 1000))
            attaquants_new = my_font.render("Pokemon choisis : " + str(
                dict_chosen_characters[side][0]["Name"]) + " - " + str(
                dict_chosen_characters[side][1]["Name"]) + " - " + str(
                dict_chosen_characters[side][2]["Name"]), True, (255, 255, 255))
            fenetre_jeu.blit(attaquants_new, (x, 1000))
        pygame.display.flip()


# ------------------------------------------------ MAIN LOOP PYGAME ------------------------------------------------- #


while running:
    pygame.init()
    for event in pygame.event.get():
        # si on appuie sur <echap>
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            running = False
        # si on utilise les clics de la souris
        if event.type == MOUSEBUTTONDOWN:
            # si on est dans le choix des personnages
            # noinspection PyUnboundLocalVariable
            if status == "Choix Personnages":
                if 50 <= event.pos[0] <= 1864 and 50 <= event.pos[1] <= 800:
                    y_grille = (event.pos[1] - 50) // taille_sprite
                    x_grille = 0
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
                        id_chosen = afficher_pokemon(x_grille, y_grille, "red")
                    elif event.button == 3:
                        id_chosen = afficher_pokemon(x_grille, y_grille, "blue")
                # random
                if 907 <= event.pos[0] <= 1007 and 875 <= event.pos[1] <= 975:
                    if event.button == 1:
                        id_chosen = afficher_pokemon(-1, -1, "red")
                    elif event.button == 3:
                        id_chosen = afficher_pokemon(-1, -1, "blue")
                # lorsqu'on valide choix pokémon rouge
                if 807 <= event.pos[0] <= 907 and 925 <= event.pos[1] <= 1025 and event.button == 1:
                    choisir_pokemon("Attack")
                # lorsqu'on valide choix pokémon rouge
                if 1789 <= event.pos[0] <= 1889 and 925 <= event.pos[1] <= 1025 and event.button == 1:
                    choisir_pokemon("Defense")

            # si on est dans le menu du jeu
            if status == "Menu":
                # si on appuye sur le bouton 'jouer'
                if 1315 <= event.pos[0] <= 1315 + 442 and 460 <= event.pos[1] <= 460 + 159 and event.button == 1:
                    status = "Choix Personnages"
                    creation_fenetre_jeu()
                # si on appuye sur le bouton 'quitter'
                if 739 <= event.pos[0] <= 739 + 442 and 877 <= event.pos[1] <= 877 + 159 and event.button == 1:
                    pygame.quit()
                    running = False
            if status == "Fight":
                if 100 <= event.pos[0] <= 489 and 100 <= event.pos[1] <= 236:
                    pygame.quit()
                    running = False
                if 600 <= event.pos[0] <= 1089 and 100 <= event.pos[1] <= 236:
                    status = "Menu"
                    dict_chosen_characters = {"Attack": [], "Defense": []}
                    creation_menu()

            else:
                pass
    # quand trois pokémon dans chaque équipe, on lance le combat (suite dans fight_system.py)
    if len(dict_chosen_characters["Attack"]) == 3 and len(dict_chosen_characters["Defense"]) == 3:
        status = "Fight"
        gagnant, scores = (fight_gui(dict_chosen_characters))
        dict_chosen_characters = {"Attack": [], "Defense": []}
        ending_screen(gagnant)
pygame.quit()
