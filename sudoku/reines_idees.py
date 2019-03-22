
##############################
# Problèmes des 8 reines
##############################



n = 8  # Nb max de piles (et taille du damier)

piles = []   # Suites de piles

def haut_des_piles():
    return [pile[-1] for pile in piles]

##############################
def choix(i):

    haut = haut_des_piles()

    # Eviter les directions verticales 
    eviter = haut

    # Eviter les diagonales
    for j in range(len(haut)):

        droite = haut[j]+i-j   # Diagonale à droite
        if 0<= droite < n:
            eviter = eviter + [droite]

        gauche = haut[j]-i+j   # Diagonale à droite
        if 0 <= gauche < n:
            eviter = eviter + [gauche]           

        # print("j",j)
        # print("haut[j]",haut[j])
        # print("droite",droite)
        # print("gauche",gauche)

#    print("éviter",eviter)

    liste_choix = [k for k in range(n) if k not in eviter]

    return liste_choix



# Test remplissage des piles
print("--- Test remplissage ---")
piles = piles + [choix(0)]
print("0",piles)
piles = piles + [choix(1)]
print("1",piles)
print(piles)
print(haut_des_piles())



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
# for __ in range(10):
#     print(piles)
#     retour()



def recherche():
    global piles

    nb_solutions = 0

    termine = False

    while not termine:
        r = len(piles)

        # print(piles)

        if r == 0:  # Piles vide
            termine = True   # Plus rien à tester

        if r == n:   # On a une solution
            nb_solutions = nb_solutions + 1
            print("Solution :",haut_des_piles())    
            retour()
            # termine = True  # Ou alors rechercher d'autres solutions

        if r < n:
            nouv_pile = choix(r)

            if len(nouv_pile) != 0:  # Oui il y a des possibilités
                piles = piles + [choix(r)]
            else:                    # Non il n'y a plus des possibilités
                retour()

    return nb_solutions

# Test recherche
print("--- Test recherche ---")
piles = []
piles = piles + [ choix(0) ]
# print(piles)
nb_sol = recherche()
print("Nb de solutions :", nb_sol)