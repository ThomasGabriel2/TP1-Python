#Header

"""
TP1_Ex5
Thomas Gabriel
19/11/2021
"""

# Fonctions

def hanoi(nb_disques, position_initiale, position_finale):
    """
    fonction récursive qui résout le problème d'Hanoi
    entrée: nb_disques: int, le nombre de disques du problème; position_initiale:int, position_finale:int
    sortie: pas de sortie 
    """
    if nb_disques == 1:
        print("Déplacer le disque du plot " + str(position_initiale) + " vers le plot " + str(position_finale) + "\n")
    else: 
        position_intermediaire  = 3 - (position_finale + position_initiale)
        hanoi(nb_disques - 1, position_initiale, position_intermediaire)
        print("Déplacer le disque du plot " + str(position_initiale) + " vers le plot " + str(position_finale) + "\n")
        hanoi(nb_disques - 1, position_intermediaire, position_finale)

def nb_coups_hanoi(nb_disques):
    """
    fonction récursive qui résout le problème d'Hanoi
    entrée: nb_disques: int, le nombre de disques du problème; position_initiale:int, position_finale:int
    sortie: pas de sortie 
    """
    if nb_disques == 1:
        nb_coups = 1
    else: 
        nb_coups = 2 * nb_coups_hanoi(nb_disques - 1) + 1 
    return nb_coups