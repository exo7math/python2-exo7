
##############################
# Tri
##############################

##############################
# Activité 1 - Tri par sélection
##############################

def tri_selection_complexite(liste):
    """ Trie par sélection et renvoie le nb de comparaisons effectuées """
    cliste = list(liste)
    n = len(cliste)
    comp = 0

    for i in range(n):
        rg_min = i
        for j in range(i+1,n):
            if cliste[j] < cliste[rg_min]:
                rg_min = j
            comp = comp + 1

        if rg_min != i:  # alors échange
            cliste[i], cliste[rg_min] = cliste[rg_min], cliste[i]

    return cliste, comp


##############################
# Activité 2 - Tri par insertion
##############################

def tri_insertion_complexite(liste):
    """ Trie par insertion et renvoie le nb de comparaisons effectuées """
    cliste = list(liste)
    n = len(cliste)
    comp = 0

    for i in range(1,n):
        el = cliste[i]
        j = i
        while (j>0) and (cliste[j-1]>el):
            cliste[j] = cliste[j-1]
            j = j-1
            comp = comp + 1
        if j>0:
            comp = comp + 1 # +1 pour la comparaison qui sort du while

        cliste[j] = el

    return cliste, comp


##############################
# Activité 3 - Tri à bulles
##############################

def tri_a_bulles_complexite(liste):
    """ Tri à bulles et nb de comparaisons effectuées """

    cliste = list(liste)
    n = len(cliste)
    comp = 0

    for i in range(n-1,-1,-1):
        for j in range(i):
            if cliste[j+1] < cliste[j]:
                cliste[j], cliste[j+1] = cliste[j+1], cliste[j]
            comp = comp + 1

    return cliste, comp





##############################
# Activité 4 - Tri fusion
##############################

# def fusion_recursive(liste_g,liste_d):
#     if len(liste_g)==0: return liste_d
#     if len(liste_d)==0: return liste_g
#     if liste_g[0] <= liste_d[0]:
#         liste_fus = [liste_g[0]] + fusion_recursive(liste_g[1:],liste_d)
#     else:
#         liste_fus = [liste_d[0]] + fusion_recursive(liste_g,liste_d[1:])
#     return liste_fus

# # Test
# print("--- Fusion récursive ---")
# liste_g = [1,4,7]
# liste_d = [2,5,6,9]
# print(liste_g,liste_d)
# print(fusion_recursive(liste_g,liste_d))


def fusion_complexite(liste_g,liste_d):
    """ Fusion et compléxité de deux listes ordonnées """
    n, m = len(liste_g), len(liste_d)
    i, j = 0, 0
    liste_fus = []
    comp = 0
    while (i<n) and (j<m):
        if liste_g[i] < liste_d[j]:
            liste_fus.append(liste_g[i])
            i = i +1
        else:
            liste_fus.append(liste_d[j])
            j = j +1
        comp = comp + 1
    while (i<n):
        liste_fus.append(liste_g[i])
        i = i +1
    while (j<m):
        liste_fus.append(liste_d[j])
        j = j +1    

    return liste_fus, comp    

def tri_fusion_complexite(liste):
    """ Tri fusion et compléxité d'une liste """
    cliste = list(liste)
    n = len(cliste)
    comp = 0
    if n <= 1:
        return cliste, 0
    else:
        liste_g, comp_g = tri_fusion_complexite(cliste[:n//2])
        liste_d, comp_d = tri_fusion_complexite(cliste[n//2:])
        liste_tri, comp_f = fusion_complexite(liste_g,liste_d)
        comp = comp_g + comp_d + comp_f
    return liste_tri, comp

# Test
from random import *
from math import *

print("--- Complexité des algorithmes de tri ---")

# Liste aléatoire
liste = [randint(0,10000) for i in range(1000)]

# Liste déjà ordonnée
# liste = list(range(1000))

# Liste ordonnée dans le mauvais sens
# liste = list(reversed(range(1000)))

liste1,comp1 = tri_selection_complexite(liste)
liste2,comp2 = tri_insertion_complexite(liste)
liste3,comp3 = tri_a_bulles_complexite(liste)
liste4,comp4 = tri_fusion_complexite(liste)

print("  -- Complexités --")
if liste1 == liste2 and liste2==liste3 and liste3==liste4:
    print("Tri ok !")
else:
    print("Problème de tri :",liste1,liste2,liste3,liste4)

n = len(liste)
print("n^2 =",n**2/2,"   n*ln_2(n) =",n*log(n,2))
print(comp1,comp2,comp3,comp4)

