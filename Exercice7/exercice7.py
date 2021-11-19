#Header

"""
TP1_Ex6
Thomas Gabriel
19/11/2021
"""

##Fonctions

#Question 1

def est_tricolore(n):
    """
    fonction qui teste si n est tricolore
    entrée: n:int
    sortie: bouléen
    """
    carre = str(n**2)
    for e in carre:
        print(e)
        if not (e == 1 or e == 4 or e == 9):
            return False
    return True

#Question 2

def tous_les_tricolores(n):
    """
    fonction qui renvoie tous les tricolores compris entre 1 et n
    entrée: n:int
    sortie: liste
    """
    L = [1]
    for i in range(2, n + 1):
        if est_tricolore(i):
            L += [i]
    return L

