
#Header

"""
TP1_Ex2
Thomas Gabriel
19/11/2021
"""

#Importation des bibliotèques

import exercice2 as ex2


#Programme principal

date = input("Entrez une date au format jj/mm/aaaa: ")

if ex2.est_valide(date):
    print("date valide")
else:
    print("date non valide")