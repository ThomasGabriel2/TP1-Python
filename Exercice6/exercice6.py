#Header

"""
TP1_Ex6
Thomas Gabriel
19/11/2021
"""

##Fonctions

#Question 1

def syracuse(n):
    """
    fonction qui renvoie la suite de syracuse pour un entier n donné en entrée
    entrée: n: int
    sortie: L:liste, correspond à la suite de syracuse
    """

    L = [n]  
    while n != 1:
        if (n % 2 == 0):
            n /= 2
            L += [int(n)]
        else:
            n = n * 3 + 1
            L += [int(n)]
    L += [4, 2]
    return L

#Question2

def altitude_syracuse(n):
    """
    fonction qui renvoie l'altitude atteinte par une suite de syracuse
    entrée: n:int
    sortie: altitude:int
    """
    altitude = n
    while n != 1:
        if (n % 2 == 0):
            n /= 2
            altitude = max(n, altitude)
        else:
            n = n * 3 + 1
            altitude= max(n, altitude)
    altitude = max(4, altitude)
    return int(altitude)

# Question 3

def temps_de_vol_syracuse(n):
    """
    fonction qui renvoie le temps de vol d'une suite de syracuse
    entrée: n:int
    sortie: res:int, le temps de vol de la fonction
    """
    res = 0
    while n != 1:
        if (n % 2 == 0):
            n /= 2
        else:
            n = n * 3 + 1
        res += 1
    return res

# Question 4

def max_temps_de_vol_syracuse(n):
    """
    fonction qui renvoie le nombre entre 1 et n ayant le tempsde vol le plus long
    entrée: n:int
    sortie: res: int
    """
    res = 0
    max = 0
    for i in range(2, n + 1):
        temps_de_vol = temps_de_vol_syracuse(i)
        if temps_de_vol > max:
            res = i
            max = temps_de_vol
    return res

# Question 5

def max_altitude_syracuse(n):
    """
    fonction qui renvoie le nombre entre 1 et n ayant l'altitude la plus haute'
    entrée: n:int
    sortie: res: int
    """
    res = 0
    max = 0
    for i in range(2, n + 1):
        altitude = altitude_syracuse(i)
        if altitude > max:
            res = i
            max = altitude
    return res


    

