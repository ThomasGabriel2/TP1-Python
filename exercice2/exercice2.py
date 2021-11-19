
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
    return (annee % 4 == 0 and not(annee % 100 ==0) or (annee % 400 == 0))

#Question 2

def nombre_jour(mois, est_bissextile):
    """
    fonction qui renvoie le nombre de jours d'un mois
    entrée: mois: int; est_bissextile: bouleen: indique si l'année est bisssextile 
    sortie: nombre de jours: int
    """
    if (mois <= 0) or (mois >= 13):
        return "Le mois saisi n'est pas valide"
    elif mois == 2:
        return 28 + int(est_bissextile)
    elif (mois <= 7 and mois % 2 == 1) or (mois > 7 and mois % 2 == 0):
        return 31
    else:
        return 30

# Question 3

def est_valide(date):
    """
    fonction qui indique si une date est valide, le format de la date doit être jj/mm/aaaa
    entrée: date: string
    sortie: bouléen: true si valide, false sinon
    """
    if len(date) != 10:
        return False

    tab_date = date.split("/")
    if len(tab_date) != 3:
        return  False
    try: 
        jour = int(tab_date[0])
        mois = int(tab_date[1])
        annee = int(tab_date[2])
    except ValueError:
        return False

    bissextile = est_bissextile(annee)
    nb_jour = nombre_jour(mois, bissextile)
    return (1 <= jour <= nb_jour) and (1 <= mois <= 12) and (0 <= annee)



