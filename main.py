from copy import deepcopy

import pygame
from pygame.locals import *

from constante import *
from random import randint


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
        dictionnary = [row for row in reader]
    return dictionnary


dico_personnages = csv_to_dict('dataset_pokemon.csv')
dict_chosen_characters = {"Attack": [], "Defense": []}


def liste_personnages(dict_pokemon: list) -> list:
    liste = []
    for _ in range(len(dict_pokemon)):
        liste.append(dict_pokemon[k]["Name"])
    return liste


def selection_par_nom(nom: str):
    for _ in range(len(dict)):
        if dico_personnages[k]["Name"] == nom:
            return deepcopy(dict[k])


def selection_attaque(dict_pokemon: dict, n: int) -> list:
    liste = []
    for _ in range(len(dict_pokemon)):
        if dict_pokemon[k]["Attack"] == n:
            liste.append(dict_pokemon[k])
    return liste


def selection(dict_pokemon: list, champ: str, operateur: str, val: str, type_data: str) -> list:
    liste = []
    if type_data == "str":
        val = str(val)
    if type_data == "int":
        val = int(val)
    if type_data == "float":
        val = float(val)
    if type_data == "list":
        val = list(val)
    if type_data == "bool":
        val = bool(val)
    for _ in range(len(dict_pokemon)):
        if operateur == "<":
            if dict_pokemon[k][champ] < val:
                liste.append(dict_pokemon[_]["Name"])
        if operateur == ">":
            if dict_pokemon[k][champ] > val:
                liste.append(dict_pokemon[_]["Name"])
        if operateur == "<=":
            if dict_pokemon[k][champ] <= val:
                liste.append(dict_pokemon[_]["Name"])
        if operateur == ">=":
            if dict_pokemon[k][champ] >= val:
                liste.append(dict_pokemon[_]["Name"])
        if operateur == "=" or operateur == "==":
            if dict_pokemon[k][champ] == val:
                liste.append(dict_pokemon[_]["Name"])
    return liste


def generer_grille_pokemon(x_coord, y_coord):
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
    On créé et affiche la fenètre de jeu à laquelle on la grille des pokémons.q
    """
    pygame.draw.rect(fenetre_jeu, Color("#000000"), (0, 0, 1920, 1080))
    pygame.display.set_caption('Pokédex')
    image_niveau = "grille.bmp"
    fond_niveau = pygame.image.load(image_niveau).convert_alpha()
    fond_niveau = pygame.transform.scale(fond_niveau, (1920, 1080))
    fenetre_jeu.blit(fond_niveau, (0, 0))
    pygame.display.flip()


def creation_menu():
    image_niveau = "menu.png"
    fond_niveau = pygame.image.load(image_niveau).convert_alpha()
    fond_niveau = pygame.transform.scale(fond_niveau, (1920, 1080))
    fenetre_jeu.blit(fond_niveau, (0, 0))
    pygame.display.flip()


pygame.init()
creation_menu()

running = True


def afficher_pokemon(x_coord, y_coord, team):
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
        types_pokemon = my_font.render("Type : " + dico_personnages[pokemon_id]["Type 1"], False, (255, 255, 255))
    else:
        types_pokemon = my_font.render(
            "Types : " + dico_personnages[pokemon_id]["Type 1"] + " and " + dico_personnages[pokemon_id]["Type 2"],
            False, (255, 255, 255))
    if team == "blue":
        fenetre_jeu.blit(image_pokemon, (1032, 850))
        fenetre_jeu.blit(nom_pokemon, (1207, 860))
        fenetre_jeu.blit(types_pokemon, (1207, 890))
    if team == "red":
        fenetre_jeu.blit(image_pokemon, (50, 850))
        fenetre_jeu.blit(nom_pokemon, (225, 860))
        fenetre_jeu.blit(types_pokemon, (225, 890))

    image_pokemon = "images/system/chosen_character_blue.png"
    image = pygame.image.load(image_pokemon).convert_alpha()
    image = pygame.transform.scale(image, (100, 100))
    fenetre_jeu.blit(image, (1789, 925))
    pygame.image.save(fenetre_jeu, 'grille.bmp')

    image_pokemon = "images/system/chosen_character_red.png"
    image = pygame.image.load(image_pokemon).convert_alpha()
    image = pygame.transform.scale(image, (100, 100))
    fenetre_jeu.blit(image, (807, 925))
    pygame.display.flip()
    pygame.font.init()
    return pokemon_id


id_chosen = -1


def attack(attacker: dict, defenser: dict) -> int:
    return int((((int(attacker["Attack"]) * 0.6 + int(attacker["Speed"]) * 4) / (int(defenser["Defense"]) * 0.5)) + 2) * randint(1, 4))


def whos_first(attacker: dict, defenser: dict, id: int):
    if int(attacker[id]["Speed"]) > int(defenser[id]["Speed"]):
        return attacker, defenser
    if int(attacker[id]["Speed"]) < int(defenser[id]["Speed"]):
        return defenser, attacker
    else:
        n = randint(1, 2)
        if n == 1:
            return attacker, defenser
        else:
            return defenser, attacker


def fighting(dico: dict):
    gagnant = []
    for fight_number in range(0, 3):
        attacker, defenser = whos_first(dico["Attack"], dico["Defense"], fight_number)
        damages = attack(attacker[fight_number], defenser[fight_number])
        print(damages)
        health_points = int(defenser[fight_number]["HP"])
        health_points -= damages
        defenser[fight_number]["HP"] = str(health_points)
        attacker, defenser = defenser, attacker
        print(int(attacker[fight_number]["HP"]), int(defenser[fight_number]["HP"]), fight_number)
        if int(attacker[fight_number]["HP"]) > 0 or int(defenser[fight_number]["HP"]) > 0:
            fight_number -= 1
        if defenser[fight_number]["HP"] < attacker[fight_number]["HP"]:
            gagnant.append(attacker[fight_number]["Name"] + " - Rouge")
            fight_number += 1
        else:
            gagnant.append(defenser[fight_number]["Name"] + " - Rouge")
            fight_number += 1
    print("exit")
    return gagnant


while running:
    pygame.init()
    for event in pygame.event.get():
        # si on appuie sur <echap>
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            continuer_la_boucle = False
        # si on utilise les clics de la souris
        if event.type == MOUSEBUTTONDOWN:
            # si on est dans le choix des personnages
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
                    if id_chosen != -1 and 0 <= len(dict_chosen_characters["Attack"]) < 3:
                        dict_chosen_characters["Attack"].append(dico_personnages[id_chosen])
                        if len(dict_chosen_characters["Attack"]) == 1:
                            my_font = pygame.font.SysFont('Arial', 25)
                            attaquants_new = my_font.render(
                                "Pokemon choisis : " + str(dict_chosen_characters["Attack"][0]["Name"]),
                                False, (255, 255, 255))
                            fenetre_jeu.blit(attaquants_new, (50, 1000))
                            pygame.display.flip()
                        if len(dict_chosen_characters["Attack"]) == 2:
                            my_font = pygame.font.SysFont('Arial', 25)
                            attaquants_old = my_font.render(
                                "Pokemon choisis : " + str(dict_chosen_characters["Attack"][0]["Name"]),
                                False, (0, 0, 0))
                            fenetre_jeu.blit(attaquants_old, (50, 1000))
                            attaquants_new = my_font.render("Pokemon choisis : " + str(
                                dict_chosen_characters["Attack"][0]["Name"]) + " - " + str(
                                dict_chosen_characters["Attack"][1]["Name"]), False, (255, 255, 255))
                            fenetre_jeu.blit(attaquants_new, (50, 1000))
                        if len(dict_chosen_characters["Attack"]) == 3:
                            my_font = pygame.font.SysFont('Arial', 25)
                            attaquants_old = my_font.render("Pokemon choisis : " + str(
                                dict_chosen_characters["Attack"][0]["Name"]) + " - " + str(
                                dict_chosen_characters["Attack"][1]["Name"]), False, (0, 0, 0))
                            fenetre_jeu.blit(attaquants_old, (50, 1000))
                            attaquants_new = my_font.render("Pokemon choisis : " + str(
                                dict_chosen_characters["Attack"][0]["Name"]) + " - " + str(
                                dict_chosen_characters["Attack"][1]["Name"]) + " - " + str(
                                dict_chosen_characters["Attack"][2]["Name"]), False, (255, 255, 255))
                            fenetre_jeu.blit(attaquants_new, (50, 1000))
                        print(dict_chosen_characters)
                        pygame.display.flip()
                # lorsqu'on valide choix pokémon rouge
                if 1789 <= event.pos[0] <= 1889 and 925 <= event.pos[1] <= 1025 and event.button == 1:
                    if id_chosen != -1 and 0 <= len(dict_chosen_characters["Defense"]) < 3:
                        dict_chosen_characters["Defense"].append(dico_personnages[id_chosen])
                        if len(dict_chosen_characters["Defense"]) == 1:
                            my_font = pygame.font.SysFont('Arial', 25)
                            attaquants_new = my_font.render(
                                "Pokemon choisis : " + str(dict_chosen_characters["Defense"][0]["Name"]),
                                False, (255, 255, 255))
                            fenetre_jeu.blit(attaquants_new, (1032, 1000))
                            pygame.display.flip()
                        if len(dict_chosen_characters["Defense"]) == 2:
                            my_font = pygame.font.SysFont('Arial', 25)
                            attaquants_old = my_font.render(
                                "Pokemon choisis : " + str(dict_chosen_characters["Defense"][0]["Name"]),
                                False, (0, 0, 0))
                            fenetre_jeu.blit(attaquants_old, (1032, 1000))
                            attaquants_new = my_font.render("Pokemon choisis : " + str(
                                dict_chosen_characters["Defense"][0]["Name"]) + " - " + str(
                                dict_chosen_characters["Defense"][1]["Name"]), False, (255, 255, 255))
                            fenetre_jeu.blit(attaquants_new, (1032, 1000))
                        if len(dict_chosen_characters["Defense"]) == 3:
                            my_font = pygame.font.SysFont('Arial', 25)
                            attaquants_old = my_font.render("Pokemon choisis : " + str(
                                dict_chosen_characters["Defense"][0]["Name"]) + " - " + str(
                                dict_chosen_characters["Defense"][1]["Name"]), False, (0, 0, 0))
                            fenetre_jeu.blit(attaquants_old, (1032, 1000))
                            attaquants_new = my_font.render("Pokemon choisis : " + str(
                                dict_chosen_characters["Defense"][0]["Name"]) + " - " + str(
                                dict_chosen_characters["Defense"][1]["Name"]) + " - " + str(
                                dict_chosen_characters["Defense"][2]["Name"]), False, (255, 255, 255))
                            fenetre_jeu.blit(attaquants_new, (1032, 1000))
                        print(dict_chosen_characters)
                        pygame.display.flip()
            # si on est dans le menu du jeu
            if status == "Menu":
                # si on appuye sur le bouton 'jouer'
                if 1337 <= event.pos[0] <= 1820 and 374 <= event.pos[1] <= 529 and event.button == 1:
                    status = "Choix Personnages"
                    creation_fenetre_jeu()
                # si on appuye sur le bouton 'quitter'
                if 708 <= event.pos[0] <= 1191 and 832 <= event.pos[1] <= 987 and event.button == 1:
                    pygame.quit()
                    continuer_la_boucle = False
            else:
                pass
    if len(dict_chosen_characters["Attack"]) == 3 and len(dict_chosen_characters["Defense"]) == 3:
        print(fighting(dict_chosen_characters))
        dict_chosen_characters = {"Attack": [], "Defense": []}
pygame.quit()
