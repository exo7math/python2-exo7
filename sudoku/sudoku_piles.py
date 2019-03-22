
##############################
# Problèmes des 8 reines
##############################

n = 4  # Nb max de piles

les_piles = []   # Suites de piles

##############################
##############################

##############################
## Question 0 ##

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

# Test
print("--- Affichage des les_piles ---")
les_piles = [[1,2,3],[6],[5,7],[3]]
affiche_piles()


##############################
## Question 1 ##

def haut_des_piles():
    """ Renvoie la liste des éléments en haut de chaque pile. """
    return [pile[-1] for pile in les_piles]


##############################
## Question 2 ##

def choix_1(i):
    """ Choix pour problème 1. """
    if i == 0:
        return [1,2,3,4]
    if i == 1:
        return [5,6]
    if i == 2:
        return [7,8]
    if i == 3:
        return [9]


##############################
## Question 5a ##

def choix_2(i):
    """ Choix pour problème 2. """

    haut = haut_des_piles()  # Configuration en cours
    if i == 0:
        return [1,2,3]
    if i == 1:
        return [2*haut[0]]
    if i == 2:
        return [5,7,9]
    if i == 3:
        return [haut[2]]


##############################
## Question 5b ##

def choix_3(i):
    """ Choix pour problème 3. """ 

    haut = haut_des_piles()  # Configuration en cours    

    if i == 0:
        return [1,3,5,7,9]
    if i == 1:
        if haut[0] <= 5:
            return [2,4]
        else:
            return [6,8]
    if i == 2:
        return [haut[1]//2]
    if i == 3:
        return [haut[0]-1,9]


##############################
## Question 5c ##

def choix_4(i):
    """ Choix pour problème 4. """    
    if i == 0:
        return [0,1]
    if i == 1:
        return [0,1]
    if i == 2:
        return [0,1]
    if i == 3:
        return [0,1]


##############################

# Pour pouvoir choisir 
def choix(i):
    return choix_3(i)


# Test remplissage des les_piles
print("--- Test remplissage ---")
les_piles = []
les_piles = les_piles + [choix(0)]
les_piles = les_piles + [choix(1)]
les_piles = les_piles + [choix(2)]
les_piles = les_piles + [choix(3)]
affiche_piles()
print(haut_des_piles())



##############################
## Question 3 ##
    
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


# Test retour
print("--- Test retour ---")
for __ in range(10):
    print("---")
    affiche_piles()
    retour()


##############################
## Question 4 ##

def recherche():
    """ Recherche une ou toutes les solutions au problème. """

    global les_piles

    les_piles = []            # On part de rien
    les_piles = [ choix(0) ]  # Première pile

    termine = False

    while not termine:
        r = len(les_piles)

        # affiche_piles()  # Affichage pour mieux comprendre

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
            retour()          # On veut toutes les solutions
            # termine = True  # Ou bien une seule solution nous suffit


    return

# Test recherche
print("--- Test recherche ---")
recherche()