
##############################
# Récursivité
##############################

##############################
# Cours 2 - Parcours d'arbre
##############################        


def parcours(n):
    # Cas terminal
    if n == 1:
        return [[0],[1],[2]]    # ou bien n == 0 il faut [[]]

    # Cas général
    sous_liste = parcours(n-1)  
    liste_deb_0 = [ [0] + x for x in sous_liste ]
    liste_deb_1 = [ [1] + x for x in sous_liste ]
    liste_deb_2 = [ [2] + x for x in sous_liste ]
    liste = liste_deb_0 + liste_deb_1 + liste_deb_2
    return liste


# Test
print("--- Parcours d'arbre ---")
n = 3
print("n =",n)
print("Listes = ",parcours(n)) 


