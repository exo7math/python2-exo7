
##############################
# Récursivité
##############################

##############################
# Activité 3 - Parcours d'arbre
##############################

##############################
## Question 1 ##

def pile_ou_face(n):
    """ Liste de tous les tirages de longueur n de piles ou faces """
    if n == 1:
        return ['P','F']  # ou bien n == 0 il faut ['']

    # Cas général
    sous_arbre = pile_ou_face(n-1)
    arbre_deb_P = ['P' + chaine for chaine in sous_arbre]
    arbre_dep_F = ['F' + chaine for chaine in sous_arbre]
    arbre = arbre_deb_P + arbre_dep_F

    return arbre

# Test
print("--- Pile ou face ---")
print(pile_ou_face(3))


##############################
## Question 2 ##

def une_seule_liste(liste):
    """ Transforme une liste qui contient des élément 
    et des sous-listes (et même des sous-sous-liste...)
    et une liste d'éléments """
    reduc_liste = []
    for l in liste:
        if isinstance(l, int):
            reduc_liste = reduc_liste + [l]     # Cas terminal
        else:
            reduc_liste = reduc_liste + une_seule_liste(l)

    return reduc_liste

# Test
print("--- Une seule liste ---")
liste = [[1,2], 3, [9,8,7,[6,5],[4,3]], 2, [[1],[1]], 0]
print(liste)
print(une_seule_liste(liste))


##############################
## Question 3 ##

def atteindre_somme(S,liste):
    """ Comment atteindre la somme S en additionnant 
    les élements de la liste donnée (les répétitions sont possibles) """
    
    # Cas terminaux
    if S == 0:
        return []
    if S < 0:
        return None

    # Cas général
    for x in liste:     
        parcours = atteindre_somme(S-x,liste)
        if parcours != None:
            parcours = [x] + parcours
            return parcours

    return None

# Test
print("--- Atteindre une somme ---")
liste = [5, 7, 11]
somme = 19
print(liste)
print(somme)
parcours = atteindre_somme(somme,liste)
print("Parcours :",parcours)
if parcours:
    print("Vérification :",sum(parcours))







