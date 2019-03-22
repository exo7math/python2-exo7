
##############################
# Big data
##############################


from random import *

##############################
# Activité 1 - Cardinal d'un multi-ensemble
##############################


##############################
## Question 0 ##

def cardinal_1(liste):
    """ Renvoie le nb d'élément distincts d'une liste (utilise set() """
    ensemble = set(liste)
    n = len(ensemble)
    return n


def cardinal_2(liste):
    """ Renvoie le nb d'élément distincts d'une liste (à la main) """
    ensemble = []
    for k in liste:
        est_present = False  # Est déjà présent dans ensemble ? 
        for l in ensemble:
            if  k == l:
                est_present = True
                break   # beurk !
        if not est_present:
            ensemble.append(k)
    print(ensemble)
    n = len(ensemble)
    return n


# Test
print("--- Cardinal classique ---")
liste = [1,2,1,8,8,5,4,3,1]
n = cardinal_1(liste)
nn = cardinal_2(liste)
print("Liste :",liste)
print("Longueur :",len(liste))
print("Cardinal (méthode Python) :",n)
print("Cardinal (à la main) :",nn)


##############################
# Pour exemples difficiles
from random import *
liste = [randint(1,100) for __ in range(50)]
print(liste)
print("Liste :",liste)
print("Longueur :",len(liste))
print("Cardinal :",cardinal_1(liste))

liste1 = [65, 88, 6, 67, 16, 10, 65, 81, 7, 7, 51, 15, 11, 67, 5, 53, 47, 54, 72, 58, 15, 38, 82, 47, 11, 53, 42, 53, 4, 9, 31, 64, 54, 52, 98, 15, 69, 55, 100, 61, 41, 99, 10, 87, 22, 8, 65, 25, 20, 79]
liste2 = [78, 32, 21, 2, 59, 64, 35, 67, 83, 87, 35, 55, 95, 20, 79, 22, 44, 19, 63, 47, 59, 78, 41, 20, 100, 85, 59, 59, 37, 41, 31, 56, 1, 2, 65, 3, 95, 79, 25, 36, 87, 2, 11, 20, 71, 1, 91, 75, 49, 44]
# [8, 57, 22, 100, 73, 20, 37, 56, 13, 100, 61, 25, 28, 90, 90, 44, 51, 79, 41, 31, 23, 84, 74, 37, 77, 52, 50, 3, 93, 7, 63, 2, 10, 66, 77, 16, 21, 80, 100, 24, 57, 94, 61, 77, 70, 88, 30, 77, 39, 50, 23, 45, 28, 90, 73, 16, 16, 47, 2, 32, 47, 30, 53, 12, 16, 25, 48, 50, 2, 69, 29, 39, 45, 25, 81, 91, 51, 91, 79, 95, 1, 80, 61, 24, 91, 73, 6, 50, 74, 63, 71, 4, 3, 48, 55, 4, 67, 24, 42, 39]
# [71, 2, 71, 61, 66, 80, 17, 56, 63, 65, 45, 3, 24, 86, 21, 37, 21, 76, 81, 34, 88, 73, 58, 65, 2, 41, 32, 82, 63, 19, 32, 15, 27, 97, 80, 5, 98, 26, 50, 86, 92, 77, 88, 17, 74, 1, 80, 85, 70, 25, 5, 92, 89, 84, 61, 59, 87, 56, 48, 79, 52, 98, 83, 97, 4, 41, 1, 47, 67, 88, 16, 19, 36, 38, 29, 41, 72, 13, 23, 30, 73, 15, 15, 8, 62, 74, 40, 83, 77, 85, 89, 34, 66, 35, 37, 18, 89, 20, 79, 87]
##############################
## Question 1 ##

import hashlib 

def hash_binaire(element):
    chaine = str(element)
    hash_object = hashlib.sha256(chaine.encode())  # Hash
    hex_dig = hash_object.hexdigest()   # Format hexadécimal
    entier = int(hex_dig,16)            # Entier
    bin_dig = format(entier, '0>256b')  # Format binaire
    return bin_dig

# def mon_hash(chaine):
#     entier = hash(chaine)              # Hash
#     bin_dig = format(entier, '0>64b')  # Format binaire
#     return bin_dig

# Test
print("--- Binaire ---")

mot = "Hello"
mot = 1
my_hash = hash_binaire(mot) 

print("Mot :",mot)
print("Hash en écriture binaire :\n",my_hash)
print("Longueur du hash :",len(my_hash))


##############################
## Question 2 ##

def indice_binaire(binaire):
    """ Nombre de 0 en fin de l'écriture de la chaîne binaire. """
    N = len(binaire)
    i = 0
    while i < N and binaire[N-1-i] == "0":
        i += 1
    return i

# Test
print("--- Indice ---")

my_hash = "00101000"
indice = indice_binaire(my_hash)
print("Hash :",my_hash)
print("Indice :",indice)

mot = "Hello girl"
my_hash = hash_binaire(mot) 
indice = indice_binaire(my_hash)
print("Hash :",my_hash)
print("Indice :",indice)


##############################
## Question 3 ##    

def table_bitmap(liste):
    """ Rempli la table de BITMAP par les indices des éléments de la liste """
    N = 256
    bitmap = [0 for i in range(N)]
    for element in liste:
        binaire = hash_binaire(element)
        indice = indice_binaire(binaire)
        bitmap[indice] = 1
    return bitmap

# Test
print("--- Remplissage de la table bitmap ---")
liste = [0,1,2,3,0]
bitmap = table_bitmap(liste)
print("bitmap =\n",bitmap)

liste = ["A","B","C","A","D","D"]
bitmap = table_bitmap(liste)
print("bitmap =\n",bitmap)


##############################
## Question 3 ##  

def rang_premier_nul(liste):
    n = len(liste)
    i = 0
    while i < n and liste[i] != 0:
        i += 1
    return i  

# Test
print("--- Rang du premier terme nul ---")
print(rang_premier_nul([1,1,1,0,0,1,0]))


##############################
## Question 4 ## 

def estimation_cardinal(liste):
    """ Estimation du cardinal par formule de Flajolet-Martin """
    bitmap = table_bitmap(liste)
    r = rang_premier_nul(bitmap)
    phi = 0.77351
    return 1/phi * 2**r

# Test
print("--- Estimation cardinal ---")

# liste = [0,1,2,3,0]
liste = ["A","B","C","A","D","D"]
n = estimation_cardinal(liste)
print("Cardinal estimé",n)
print("Cardinal réel",cardinal_1(liste))

liste = liste1
n = estimation_cardinal(liste)
print("Cardinal estimé",n)
print("Cardinal réel",cardinal_1(liste))

liste = [randint(1,100000) for __ in range(100000)]
n = estimation_cardinal(liste)
print("Cardinal estimé",n)
print("Cardinal réel",cardinal_1(liste))