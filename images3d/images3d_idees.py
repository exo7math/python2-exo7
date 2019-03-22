
##############################
# Images 3D
##############################

##############################
# Activité 1 - Skyline
##############################

immeubles = [(0,1,5),(2,4,10),(3,5,7),(3,8,2),(7,9,4)]


##############################
## Question 1 ##

# Hauteur maximale d'une liste d'immeubles
# et 0 si pas d'immeubles

def hauteur_max_immeubles(immeubles):
    hmax = 0
    for x,y,h in immeubles:
        if h > hmax:
            hmax = h
    return hmax

# Test
print("--- Hauteur maximale d'une liste d'immeubles ---")
h = hauteur_max_immeubles(immeubles)
print(h)

##############################
## Question 2 ##

# Calcule et tri des bords
# sans redondance

def calcul_bords(immeubles):
    liste_bords = []
    for x,y,h in immeubles:
        if x not in liste_bords:
            liste_bords.append(x)
        if y not in liste_bords:
            liste_bords.append(y)
    liste_bords.sort()
    return liste_bords

# Test
print("--- Calcul des bords ---")
liste_bords = calcul_bords(immeubles)
print(liste_bords)

##############################
## Question 3 ##

# dico : bord -> liste des numéros des immeubles correspondants

def dictionnaire_bords_immeubles(immeubles):
    dico = {}
    n = len(immeubles)
    for i in range(n):
        x,y,h = immeubles[i]
        if x not in dico:
            dico[x] = [i]
        else:
            dico[x].append(i)
        if y not in dico:
            dico[y] = [i]
        else:
            dico[y].append(i)

    return dico

# Test
print("--- Calcul du dictionnaire bords/immeubles ---")
dico = dictionnaire_bords_immeubles(immeubles)
print(dico)


##############################
## Question 4 ##

# Calcul de la skyline

def calcul_skyline(immeubles):
    # Initialisation des variables
    skyline = []
    liste_bords = calcul_bords(immeubles)
    dico = dictionnaire_bords_immeubles(immeubles)
    num_immeubles_actifs = []

    # Boucle principale
    h_avant = 0
    for x in liste_bords:

        # Calcul des immeubles actifs
        for i in dico[x]:
            if i not in num_immeubles_actifs:
                num_immeubles_actifs.append(i)
            else:
                num_immeubles_actifs.remove(i)

        # Calcul de la nouvelle hauteur maximale
        immeubles_actifs = [immeubles[k] for k in num_immeubles_actifs]
        h_apres = hauteur_max_immeubles(immeubles_actifs) 

        # Est-ce que cela change la skyline ?
        if h_avant != h_apres:
            skyline.append((x,h_avant))
            skyline.append((x,h_apres))

        # Pour passer à la suite
        h_avant = h_apres
    return skyline


# Test
print("--- Calcul de la skyline ---")
skyline = calcul_skyline(immeubles)
print("Immeubles :",immeubles)
print("Skyline :",skyline)


##############################
## Question 4 ##

# Affichage graphique avec matplotlib

import matplotlib.pyplot as plt
# import matplotlib.patches as patches

def affichage_skyline(immeubles,avec_immeubles=True,avec_skyline=True):
    plt.axes().set_aspect('equal')

    if avec_immeubles:
        for (x,y,h) in immeubles:
            listex = [x,x,y,y]
            listey = [0,h,h,0]           
            plt.plot(listex,listey,"r",color='gray',linewidth=2)
            plt.fill(listex,listey,"r",color='green',linewidth=2)

    if avec_skyline:
        skyline = calcul_skyline(immeubles)
        listex = [x for (x,y) in skyline]
        listey = [y for (x,y) in skyline]
        plt.plot([0,max(listex)],[0,0],color='black',linewidth=2)
        plt.plot(listex,listey,color='red',linewidth=3)

    plt.show()
    return

# Test
print("--- Affichage ---")
affichage_skyline(immeubles)


