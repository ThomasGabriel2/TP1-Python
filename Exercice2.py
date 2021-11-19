"""
TP1_Ex2
Thomas Gabriel
19/11/2021
"""
def est_bissextile(annee):
    """
    fonction qui teste si une année est bissextile
    entrée: année, int
    sortie, booléen
    """
    if (annee % 4 == 0 and not(annee % 100 ==0) or (annee % 400 == 0)):
        return True
    else:
        return False