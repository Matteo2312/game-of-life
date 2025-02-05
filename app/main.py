import os
import numpy as np
import time

def init_grille(taille):
    return np.random.choice(['  ', '# '], taille * taille, p=[0.8, 0.2]).reshape(taille, taille)


def afficher_grille(grille):
    for i in range(grille.shape[0]):
        for j in range(grille.shape[1]):
            print(grille[i, j], end='')
        print()        


def calculer_prochain_etat(grille):
    nouvelle_grille = np.copy(grille)
    for i in range(grille.shape[0]):
        for j in range(grille.shape[1]):
            nb_voisins = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k == 0 and l == 0:
                        continue
                    if grille[(i + k) % grille.shape[0], (j + l) % grille.shape[1]] == '# ':
                        nb_voisins += 1
            if grille[i, j] == '# ' and (nb_voisins < 2 or nb_voisins > 3):
                nouvelle_grille[i, j] = '  '
            elif grille[i, j] == '  ' and nb_voisins == 3:
                nouvelle_grille[i, j] = '# '

    return nouvelle_grille


def jeu_de_la_vie(taille, generations):
    grille = init_grille(taille)
    for _ in range(generations):
        afficher_grille(grille)
        grille = calculer_prochain_etat(grille)
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        

jeu_de_la_vie(40, 100)
