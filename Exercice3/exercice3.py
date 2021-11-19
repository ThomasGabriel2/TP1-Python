#Header

"""
TP1_Ex3
Thomas Gabriel
19/11/2021
"""

#Fonctions

def mes_impots(revenu):
    """
    fonction qui calcule le montant d'imopots à payer pour un revenu donné
    entrée: revenu: int
    sortie: impots: int
    """
    impots = 0
    if revenu > 158123:
        impots += (revenu - 158123) * 0.45
    if revenu > 73517: 
        impots += (min(revenu, 158122)- 73517) * 0.41
    if revenu > 25711: 
        impots += (min(revenu, 73516)- 25711) * 0.3
    if revenu > 10085:
        impots += (min(revenu, 25710)- 10085) * 0.11
    return impots
