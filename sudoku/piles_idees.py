
##############################
# Problèmes des 8 reines
##############################

# Faire différentes pb, dont:
# choix i+1 dépend de i
# choix i en fait fixé (un seul choix)

n = 4  # Nb max de piles

piles = []   # Suites de piles


##############################
def choix(i):
    if i == 0:
        return [1,2,3,4]
    if i == 1:
        return [5,6]
    if i == 2:
        return [7,8]
    if i == 3:
        return [4]


def solution():
    # On suppose que bonne longueur
    return [pile[-1] for pile in piles]


# Test remplissage des piles
print("--- Test remplissage ---")
piles = piles + [choix(0)]
piles = piles + [choix(1)]
piles = piles + [[1]]
piles = piles + [[8,8]]
print(piles)
print(solution())



##############################
def affiche_piles():
    print(piles)
    return
    
    
##############################
def retour():
    global piles
    r = len(piles)-1
    while r >= 0 and len(piles[r]) == 1:  # Si un seul éléments
        piles = piles[0:r]  # On supprime la dernière pile
        r = r - 1
    if r >= 0:              # On retire un élément en haut de la pile
        k = len(piles[r])        # Hauteur de la dernière pile
        piles[r] = piles[r][0:k-1] 
    return


# Test retour
print("--- Test retour ---")
for __ in range(10):
    print(piles)
    retour()



def recherche():
    global piles
    termine = False

    while not termine:
        r = len(piles)

        # print(piles)

        if r == 0:  # Piles vide
            termine = True   # Plus rien à tester

        if r == n:   # On a une solution
            print("Solution :",solution())    
            retour()
            # termine = True  # Ou alors rechercher d'autres solutions

        if r < n:
            nouv_pile = choix(r)

            if len(nouv_pile) != 0:  # Oui il y a des possibilités
                piles = piles + [choix(r)]
            else:                    # Non il n'y a plus des possibilités
                retour()

    return

# Test recherche
print("--- Test recherche ---")
piles = [ choix(0) ]
print(piles)
recherche()