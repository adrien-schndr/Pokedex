from random import randint


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


def fighting(dico: dict):
    gagnant = []
    for fight_number in range(0, 3):
        attacker, defenser = whos_first(dico["Attack"][fight_number], dico["Defense"][fight_number])
        while int(attacker["HP"]) > 0 or int(defenser["HP"]) > 0:
            damages = attack(attacker, defenser)
            health_points = int(defenser["HP"])
            health_points -= damages
            if health_points <= 0:
                gagnant.append(attacker["Name"])
                break
            defenser["HP"] = str(health_points)
            attacker, defenser = defenser, attacker
    return gagnant


def gagnants_dico(dico: dict, gagnants: list) -> dict:
    liste_gagnants = {}
    for k in range(len(gagnants)):
        if dico["Attack"][k]["Name"] == gagnants[k]:
            liste_gagnants[str(str(k+1) + ". Equipe Rouge")] = dico["Attack"][k]
        if dico["Defense"][k]["Name"] == gagnants[k]:
            liste_gagnants[str(str(k+1) + ". Equipe Bleue")] = dico["Defense"][k]
    for cle in liste_gagnants:
        print(f"{cle}", f"{liste_gagnants[cle]}")
    return liste_gagnants
