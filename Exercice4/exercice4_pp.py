#Header

"""
Programme principal de TP1_Ex4
Thomas Gabriel
19/11/2021
"""

#Importation des bibliotèques

import numpy as np
import exerciec4 as ex4

#Programme principal

A = np.array([[1, 2], [3, 4], [5, 6]])

B = np.array([[13, 9], [5, 11]])

print(ex4.multiplication(A, B))