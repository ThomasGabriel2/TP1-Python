
#Header

"""
TP1_Ex2
Thomas Gabriel
19/11/2021
"""

#Question 1

def est_bissextile(annee):
    """
    fonction qui teste si une année est bissextile
    entrée: année, int
    sortie: booléen
    """
    if (annee % 4 == 0 and not(annee % 100 ==0) or (annee % 400 == 0)):
        return True
    else:
        return False

#Question 2

def nombre_jour(mois):
    """
    fonction qui renvoie le nombre de jours d'un mois
    entrée: mois: int
    sortie: nombre de jours: int
    """
    if (mois <= 0) or (mois >= 13):
        return "Le mois saisi n'est pas valide"
    elif mois == 2:
        return 28
    elif (mois <= 7 and mois % 2 == 1) or (mois > 7 and mois % 2 == 0):
        return 31
    else:
        return 30