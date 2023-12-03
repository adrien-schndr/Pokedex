import time
from random import randint

from constante import *


def attack(attacker: dict, defenser: dict) -> int:
    return int((((int(attacker["Attack"]) * 0.6 + int(attacker["Speed"]) * 4) / (int(defenser["Defense"]) * 0.5)) + 2))


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


def fighting(dico: dict, gagnant: list, fight_number: int, scores: list):

    # Images

    my_font = pygame.font.SysFont('Arial', 25)
    image_niveau = "arena_background.png"
    fond_niveau = pygame.image.load(image_niveau).convert_alpha()
    fond_niveau = pygame.transform.scale(fond_niveau, (1920, 1080))
    fenetre_jeu.blit(fond_niveau, (0, 0))
    attacker_picture = "images/" + dico["Defense"][fight_number]["Name"] + ".png"
    attacker_picture = pygame.image.load(attacker_picture).convert_alpha()
    attacker_picture = pygame.transform.scale(attacker_picture, (500, 500))
    attacker_picture = pygame.transform.flip(attacker_picture, True, False)
    fenetre_jeu.blit(attacker_picture, (150, 490))
    defenser_picture = "images/" + dico["Attack"][fight_number]["Name"] + ".png"
    defenser_picture = pygame.image.load(defenser_picture).convert_alpha()
    defenser_picture = pygame.transform.scale(defenser_picture, (350, 350))
    fenetre_jeu.blit(defenser_picture, (1400, 240))
    pygame.display.flip()
    base_health_bar = "images/system/filled_health_bar.png"
    base_health_bar = pygame.image.load(base_health_bar).convert_alpha()
    base_health_bar = pygame.transform.scale(base_health_bar, (800, 40))
    attacker, defenser = whos_first(dico["Attack"][fight_number], dico["Defense"][fight_number])
    tour = 0
    while True:
        if int(defenser["HP"]) <= 0:
            defenser["HP"] = "0"
        if int(attacker["HP"]) <= 0:
            attacker["HP"] = "0"

        # Images

        fenetre_jeu.blit(base_health_bar, (50, 50))
        fenetre_jeu.blit(base_health_bar, (1070, 50))
        score_display = my_font.render(str(scores[0]) + " : " + str(scores[1]), True, (255, 255, 255))
        fenetre_jeu.blit(score_display, (950, 60))
        red_health_bar = "images/system/base_health_bar.png"
        red_health_bar = pygame.image.load(red_health_bar).convert_alpha()
        red_health_bar = pygame.transform.scale(red_health_bar, (800-health_bar_maker(
            dico, fight_number, "Defense")*8, 40))
        fenetre_jeu.blit(red_health_bar, (50, 50))
        red_health_bar = pygame.transform.scale(red_health_bar, (800-health_bar_maker(
            dico, fight_number, "Attack")*8, 40))
        fenetre_jeu.blit(red_health_bar, (1070, 50))
        pygame.display.flip()

        pygame.display.flip()
        if tour == -1:
            break
        if tour % 2 == 0:
            damages = attack(attacker, defenser)
            health_points = int(defenser["HP"])
            health_points -= damages
            if health_points <= 0:
                if attacker["Name"] == dico["Attack"][fight_number]["Name"]:
                    gagnant.append({"Name": attacker["Name"], "Team": "Attack"})
                    scores[1] += 1
                if attacker["Name"] == dico["Defense"][fight_number]["Name"]:
                    gagnant.append({"Name": attacker["Name"], "Team": "Defense"})
                    scores[0] += 1
                fenetre_jeu.blit(fond_niveau, (0, 0))
                # fenetre_jeu.blit(score_display, (950, 60))
                image_pokemon = "images/" + attacker["Name"] + ".png"
                image_pokemon = pygame.image.load(image_pokemon).convert_alpha()
                image_pokemon = pygame.transform.scale(image_pokemon, (500, 500))
                fenetre_jeu.blit(image_pokemon, (760, 300))
                tour = -2
            defenser["HP"] = str(health_points)
        else:
            damages = attack(defenser, attacker)
            health_points = int(attacker["HP"])
            health_points -= damages
            if health_points <= 0:
                fenetre_jeu.blit(fond_niveau, (0, 0))
                # fenetre_jeu.blit(score_display, (950, 60))
                pygame.display.flip()
                image_pokemon = "images/" + defenser["Name"] + ".png"
                image_pokemon = pygame.image.load(image_pokemon).convert_alpha()
                image_pokemon = pygame.transform.scale(image_pokemon, (500, 500))
                fenetre_jeu.blit(image_pokemon, (760, 300))
                if defenser["Name"] == dico["Attack"][fight_number]["Name"]:
                    gagnant.append({"Name": defenser["Name"], "Team": "Attack"})
                    scores[1] += 1
                if defenser["Name"] == dico["Defense"][fight_number]["Name"]:
                    gagnant.append({"Name": defenser["Name"], "Team": "Defense"})
                    scores[0] += 1
                tour = -2
            attacker["HP"] = str(health_points)
        tour += 1
        time.sleep(0.5)
    time.sleep(2)
    return gagnant, scores


def fight_gui(dict_chosen_characters: dict):
    gagnant = []
    scores = [0, 0]
    my_font = pygame.font.SysFont('Arial', 25)
    for fight_number in range(0, 3):
        score_display = my_font.render(str(scores[0]) + " : " + str(scores[1]), True, (255, 255, 255))
        fenetre_jeu.blit(score_display, (900, 50))
        pygame.display.flip()
        gagnant, scores = fighting(dict_chosen_characters, gagnant, fight_number, scores)
    return gagnant, scores


def health_bar_maker(dict_chosen_characters, fight_number, team):
    """
    Renvoie le pourcentage de vie d'un Pokémon appelé dict_chosen_characters[team][fight_number]
    """
    max_health = int(dict_chosen_characters[team][fight_number]["Base HP"])
    current_health = int((int(dict_chosen_characters[team][fight_number]["HP"]) / max_health) * 100)
    if current_health <= 0:
        current_health = 0
    return current_health


def ending_screen(gagnant):
    my_font = pygame.font.SysFont('Arial', 25)
    image_niveau = "win_background.png"
    fond_niveau = pygame.image.load(image_niveau).convert_alpha()
    fond_niveau = pygame.transform.scale(fond_niveau, (1920, 1080))
    fenetre_jeu.blit(fond_niveau, (0, 0))
    leave_button = "images/system/leave_button.png"
    leave_button = pygame.image.load(leave_button).convert_alpha()
    restart_button = "images/system/play_again_button.png"
    restart_button = pygame.image.load(restart_button).convert_alpha()
    time.sleep(0.5)
    x_pos = 100
    for _ in range(len(gagnant)):
        image_pokemon = "images/" + gagnant[_]["Name"] + ".png"
        image = pygame.image.load(image_pokemon).convert_alpha()
        image = pygame.transform.scale(image, (500, 500))
        fenetre_jeu.blit(image, (x_pos, 480))
        if gagnant[_]["Team"] == "Attack":
            score_display = my_font.render("Equipe rouge", True, (255, 0, 0))
            fenetre_jeu.blit(score_display, (x_pos, 980))
        if gagnant[_]["Team"] == "Defense":
            score_display = my_font.render("Equipe bleue", True, (0, 0, 255))
            fenetre_jeu.blit(score_display, (x_pos+200, 980))
        x_pos += 600
        pygame.display.flip()
        time.sleep(0.5)
    fenetre_jeu.blit(leave_button, (100, 100))
    fenetre_jeu.blit(restart_button, (600, 100))
    pygame.display.flip()
