
##############################
# Problèmes des 8 reines
##############################


n = 8  # Nb max de piles (et taille de l'échiquier)

les_piles = []   # Suites de piles


##############################
# Depuis l'activité "piles"
##############################

def affiche_piles():
    """ Affichage de toutes les piles. """
    r = len(les_piles)
    if r == 0: return
    h = max([len(pile) for pile in les_piles])  # hauteur
    for j in range(h):                      # pour chaque ligne
        for i in range(r):                  # pour chaque colonne
            pile = les_piles[i]        
            if 0 <= h-j-1 < len(pile):
                print(pile[h-j-1],end="")
            else:
                print(" ",end="")
        print("")
    return


##############################

def haut_des_piles():
    """ Renvoie la liste des éléments en haut de chaque pile. """
    return [pile[-1] for pile in les_piles]


##############################
##############################

# Nouvelle fonction choix

def choix(i):
    """ Fonction choix pour le pb des reines.
    La pile de rang i correspond au palcement de la reine sur la colonne numéro i."""

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

    liste_choix = [k for k in range(n) if k not in eviter]

    return liste_choix



# Test remplissage des piles
print("--- Test remplissage ---")
les_piles = [choix(0)]
print("0",les_piles)
les_piles = les_piles + [choix(1)]
print("1",les_piles)
print(les_piles)
print(haut_des_piles())

##############################
# Depuis l'activité "piles"
##############################
    
def retour():
    """ Revient à une configuration d'un cran avant. """

    global les_piles
    r = len(les_piles)-1                     # Numéro de la dernière pile
    while r >= 0 and len(les_piles[r]) == 1: # Si un seul élément sur la dernière pile
        les_piles = les_piles[0:r]           # On supprime la dernière pile
        r = r - 1
    if r >= 0:                                         
        k = len(les_piles[r])                # Hauteur de la dernière pile
        les_piles[r] = les_piles[r][0:k-1]   # On retire l'élément en haut de la dernière pile
    return


##############################

def recherche():
    """ Recherche une ou toutes les solutions au problème. """

    global les_piles

    les_piles = []            # On part de rien
    les_piles = [ choix(0) ]  # Première pile

    nb_solutions = 0
    termine = False

    while not termine:
        r = len(les_piles)

        if r == 0:  # piles vides
            termine = True   # Plus rien à tester

        if 0 < r < n:
            nouv_pile = choix(r)

            if len(nouv_pile) != 0:  # Oui il y a des possibilités
                les_piles = les_piles + [nouv_pile]
            else:                    # Non il n'y a plus des possibilités
                retour()
                
        if r == n:   # On a une solution
            print("Solution :",haut_des_piles()) 
            nb_solutions += 1   
            retour()          # On veut toutes les solutions
            # termine = True  # Ou bien une seule solution nous suffit


    return nb_solutions

# Test recherche
print("--- Test recherche des reines ---")
nb_sol = recherche()
print("Nombre de solutions :", nb_sol)