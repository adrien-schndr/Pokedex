from random import randint
from constante import *
import time
from pygame.locals import *


def attack(attacker: dict, defenser: dict) -> int:
    return int((((int(attacker["Attack"]) * 0.6 + int(attacker["Speed"]) * 4) / (int(defenser["Defense"]) * 0.5)) + 2) *
               randint(1, 4))


def whos_first(attacker: dict, defenser: dict):
    if int(attacker["Speed"]) > int(defenser["Speed"]):
        return attacker, defenser
    if int(attacker["Speed"]) < int(defenser["Speed"]):
        return defenser, attacker
    else:
        n = randint(1, 2)
        if n == 1:
            return attacker, defenser
        else:
            return defenser, attacker


def fighting(dico: dict, gagnant: list, fight_number: int):
    image_niveau = "arena_background.png"
    fond_niveau = pygame.image.load(image_niveau).convert_alpha()
    fond_niveau = pygame.transform.scale(fond_niveau, (1920, 1080))
    fenetre_jeu.blit(fond_niveau, (0, 0))
    attacker, defenser = whos_first(dico["Attack"][fight_number], dico["Defense"][fight_number])
    attacker_picture = "images/" + attacker["Name"] + ".png"
    attacker_picture = pygame.image.load(attacker_picture).convert_alpha()
    attacker_picture = pygame.transform.scale(attacker_picture, (500, 500))
    attacker_picture = pygame.transform.flip(attacker_picture, True, False)
    fenetre_jeu.blit(attacker_picture, (150, 490))
    defenser_picture = "images/" + defenser["Name"] + ".png"
    defenser_picture = pygame.image.load(defenser_picture).convert_alpha()
    defenser_picture = pygame.transform.scale(defenser_picture, (350, 350))
    fenetre_jeu.blit(defenser_picture, (1400, 240))
    pygame.display.flip()
    reverse = False
    print("Attacker ", health_bar_maker(dico, fight_number, "Attack"))
    print("Defenser ", health_bar_maker(dico, fight_number, "Defense"))
    tour = 0
    while tour == -1:
        if int(defenser["HP"]) <= 0:
            defenser["HP"] = "0"
        if int(attacker["HP"]) <= 0:
            attacker["HP"] = "0"
        print("Attacker ", health_bar_maker(dico, fight_number, "Attack"))
        print("Defenser ", health_bar_maker(dico, fight_number, "Defense"))
        base_health_bar = "images/system/base_health_bar.png"
        base_health_bar = pygame.image.load(base_health_bar).convert_alpha()
        base_health_bar = pygame.transform.scale(base_health_bar, (100, 20))
        fenetre_jeu.blit(base_health_bar, (150, 390))
        red_health_bar = "images/system/red_health_bar.png"
        red_health_bar = pygame.image.load(red_health_bar).convert_alpha()
        red_health_bar = pygame.transform.scale(red_health_bar, (int(attacker["HP"]), 20))
        fenetre_jeu.blit(red_health_bar, (150, 390))
        pygame.display.flip()
        base_health_bar = "images/system/base_health_bar.png"
        base_health_bar = pygame.image.load(base_health_bar).convert_alpha()
        base_health_bar = pygame.transform.scale(base_health_bar, (100, 20))
        fenetre_jeu.blit(base_health_bar, (1500, 390))
        blue_health_bar = "images/system/blue_health_bar.png"
        blue_health_bar = pygame.image.load(blue_health_bar).convert_alpha()
        blue_health_bar = pygame.transform.scale(blue_health_bar, (int(defenser["HP"]), 20))
        fenetre_jeu.blit(blue_health_bar, (1500, 390))
        pygame.display.flip()
        if tour < 0:
            break
        if tour % 2 == 0:
            damages = attack(attacker, defenser)
            health_points = int(defenser["HP"])
            health_points -= damages
            if health_points <= 0:
                gagnant.append(attacker["Name"])
                tour = -2
            defenser["HP"] = str(health_points)
        else:
            damages = attack(defenser, attacker)
            health_points = int(attacker["HP"])
            health_points -= damages
            if health_points <= 0:
                gagnant.append(defenser["Name"])
                tour = -2
            attacker["HP"] = str(health_points)
        tour += 1
        time.sleep(0.5)
    time.sleep(2)
    return gagnant


def gagnants_dico(dico: dict, gagnants: list) -> dict:
    liste_gagnants = {}
    for _ in range(len(gagnants)):
        if dico["Attack"][_]["Name"] == gagnants[_]:
            liste_gagnants[str(str(_ + 1) + ". Equipe Rouge")] = dico["Attack"][_]
        if dico["Defense"][_]["Name"] == gagnants[_]:
            liste_gagnants[str(str(_ + 1) + ". Equipe Bleue")] = dico["Defense"][_]
    print(liste_gagnants)
    for cle in liste_gagnants:
        # noinspection PyCompatibility
        print(f"{cle}", f"{liste_gagnants[cle]}")
    return liste_gagnants


def fight_gui(dict_chosen_characters: dict):
    gagnant = []
    for fight_number in range(0, 3):
        gagnant = fighting(dict_chosen_characters, gagnant, fight_number)
    return gagnant


def health_bar_maker(dict_chosen_characters, fight_number, team):
    max_health = int(dict_chosen_characters[team][fight_number]["Base HP"])
    current_health = int((int(dict_chosen_characters[team][fight_number]["HP"]) / max_health) * 100)
    if current_health <= 0:
        current_health = 0
    return current_health
