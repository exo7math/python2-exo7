
##############################
# Sudoku
##############################

# Grille 4x4 facile

N = 4   # Taille de la grille
Mx = 2  # Largeur d'un bloc
My = 2  # Hauteur d'un bloc

grille_depart = [[0 for j in range(N)] for i in range(N)]
# 0 signifie par encore déterminé, sinon nb de 1 à N

grille_depart[0][0] = 1
grille_depart[1][2] = 2
grille_depart[3][1] = 3
grille_depart[3][3] = 4


##############################
def voir_grille(grille):
    for i in range(N):
        for j in range(N):
            if grille[i][j] != 0:
                print(grille[i][j], end="")
            else:
                print('␣', end="")
        print()
    return

voir_grille(grille_depart)


##############################
def case_vers_numero(i,j):
    return i*N+j

##############################
def numero_vers_case(k):
    return(k//N,k%N)

# Test
print("--- Test numérotation ---")
k = case_vers_numero(1,2)
print(k)
print(numero_vers_case(k))


##############################
def chiffres_ligne(i,grille):
    chiffres = []
    for j in range(N):
        if grille[i][j] != 0:
            chiffres = chiffres + [grille[i][j]]

    return chiffres    

##############################
def chiffres_colonne(j,grille):
    chiffres = []
    for i in range(N):
        if grille[i][j] != 0:
            chiffres = chiffres + [grille[i][j]]

    return chiffres

##############################
def chiffres_bloc(i,j,grille):
    chiffres = []
    a = My*(i//My)
    b = Mx*(j//Mx)

    for i in range(a,a+My):
        for j in range(b,b+Mx):
            if grille[i][j] != 0:
                chiffres = chiffres + [grille[i][j]] 

    return chiffres           

# Test
print("--- Test chiffres déjà placé ---")
voir_grille(grille_depart)
i = 1
print("Chiffres de la ligne i =",i,chiffres_ligne(i,grille_depart))
j = N-1
print("Chiffres de la colonne j =",j,chiffres_colonne(j,grille_depart))
print("Chiffres du bloc contenant (i,j) =",i,j,chiffres_bloc(i,j,grille_depart))

##############################
##############################
def liste_vers_grille(liste):

    grille = [[0 for j in range(N)] for i in range(N)] # Grille vide
    for k in range(len(liste)):
        i,j = numero_vers_case(k)
        grille[i][j] = liste[k]

    return grille

# Test
# print("--- Test piles vers grille ---")
# ma_grille = liste_vers_grille([1,2,3,4,4,3,2,1,2])
# voir_grille(ma_grille)


##############################
##############################

n = N*N  # Nb max de piles (une par case)



piles = []   # Suites de piles

def haut_des_piles():
    return [pile[-1] for pile in piles]


##############################
def choix(k):

    i,j = numero_vers_case(k)

    # Si la case a un numéro au départ on le conserve (un seul choix) !
    if grille_depart[i][j] != 0:
        return [grille_depart[i][j]]

    # Sinon il faut calculer les chiffres possibles

    # On commence par recréer la grille
    haut = haut_des_piles()  # La configuration en cours
    grille = liste_vers_grille(haut)
    # On rajoute aussi les numéros au départ
    for ii in range(N):
        for jj in range(N):
            if grille_depart[ii][jj] != 0:
                grille[ii][jj] = grille_depart[ii][jj]


    # Eviter les chiffres sur la même ligne
    # ou sur la même colonne ou sur la case
    eviter = chiffres_ligne(i,grille) + chiffres_colonne(j,grille) + chiffres_bloc(i,j,grille)

    # Choix possibles : c'est donc le complément
    liste_choix = [k for k in range(1,N+1) if k not in eviter]

    return liste_choix



# Test remplissage des piles
print("--- Test remplissage ---")
piles = piles + [choix(0)]
print("0",piles)
piles = piles + [choix(1)]
print("1",piles)
print(piles)
piles = piles + [choix(3)]
print("2",piles)
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

    termine = False

    while not termine:

        r = len(piles)

        # print(piles)

        if r == 0:  # Piles vide
            termine = True   # Plus rien à tester

        if r == n:   # On a une solution
            solution = haut_des_piles()
            #retour()       # Ou bien on cherche d'autres solutions
            termine = True  # Ou bien on arrête

        if r < n:
            nouv_pile = choix(r)

            if len(nouv_pile) != 0:  # Oui il y a des possibilités
                piles = piles + [choix(r)]
            else:                    # Non il n'y a plus des possibilités
                retour()

    return solution

# Test recherche
print("--- Test recherche ---")
voir_grille(grille_depart)
piles = []
piles = piles + [ choix(0) ]
# print(piles)
liste_solution = recherche()
grille_solution = liste_vers_grille(liste_solution)
voir_grille(grille_solution)


print("--- Test recherche ---")

N = 9   # Taille de la grille
Mx = 3  # Largeur d'un bloc
My = 3  # Hauteur d'un bloc

# Grille 9x9 facile
liste_depart = [ 
3,0,4, 0,8,0, 0,5,0,
7,0,0, 0,1,0, 0,0,3, 
8,0,0, 0,0,2, 6,0,0,
0,0,9, 1,0,0, 3,0,5,
4,0,5, 3,0,7, 9,0,2,
6,0,8, 0,0,9, 7,0,0,
0,0,7, 4,0,0, 0,0,6,
5,0,0, 0,9,0, 0,0,8,
0,4,0, 0,7,0, 5,0,9,
] 

# Grille 9x9 moyenne
liste_depart = [ 
5,0,8, 0,3,0, 4,6,0,
0,0,0, 2,0,0, 8,0,0, 
1,9,0, 4,0,0, 7,3,0,
8,0,7, 9,2,0, 0,0,0,
0,0,9, 6,0,4, 2,0,0,
0,0,0, 0,8,3, 1,0,5,
0,3,1, 0,0,2, 0,7,6,
0,0,2, 0,0,9, 0,0,0,
0,7,5, 0,6,0, 9,0,8,
]


# Grille 9x9 très difficile
liste_depart = [ 
0,4,0, 1,0,0, 9,0,0,
0,0,0, 0,0,0, 0,6,0, 
0,8,0, 6,3,0, 0,0,0,
5,1,7, 2,9,0, 0,0,8,
0,0,4, 0,5,0, 2,0,0,
9,0,0, 0,1,4, 7,5,6,
0,0,0, 0,7,5, 0,8,0,
0,9,0, 0,0,0, 0,0,0,
0,0,1, 0,0,2, 0,4,0,
]

# # Grille 9x9 très difficile
# liste_depart = [ 
# #8,0,0, 0,0,0, 0,0,0,  # Ligne 1 : Vraie premiere ligne (impossible car trop long)
# #8,1,2, 0,0,0, 0,0,0,  # Ligne 1 : Difficile
# 8,1,0, 0,0,0, 0,0,0,   # Ligne 1 : Très difficile
# 0,0,3, 6,0,0, 0,0,0, 
# 0,7,0, 0,9,0, 2,0,0,
# 0,5,0, 0,0,7, 0,0,0,
# 0,0,0, 0,4,5, 7,0,0,
# 0,0,0, 1,0,0, 0,3,0,
# 0,0,1, 0,0,0, 0,6,8,
# 0,0,8, 5,0,0, 0,1,0,
# 0,9,0, 0,0,0, 4,0,0,
# ]

grille_depart = liste_vers_grille(liste_depart)
# 0 signifie par encore déterminé, sinon nb de 1 à N
voir_grille(grille_depart)
n = N*N
piles = []
piles = piles + [ choix(0) ]
# print(piles)
liste_solution = recherche()
grille_solution = liste_vers_grille(liste_solution)
voir_grille(grille_solution)