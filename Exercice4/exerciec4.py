#Header

"""
TP1_Ex4
Thomas Gabriel
19/11/2021
"""

#Importation des bibliotèques

import numpy as np

#Fonctions

def multiplication(A, B):
    if len(A[0]) != len(B):
        return "dimensions non valides"
    dimensions_resultat =[len(A), len(B[0])]
    C = np.zeros(dimensions_resultat)
    nb_termes = len(B)
    for i in range(dimensions_resultat[0]):
        for j in range(dimensions_resultat[1]):
            for k in range(nb_termes):
                C[i, j] += A[i, k] * B[k, j]
    return C

    