
##############################
# Images 3D
##############################

##############################
# Activité 1 - Skyline
##############################

immeubles = [(0,1,5), (2,4,10), (3,5,7), (3,8,2), (7,9,4)]


##############################
## Question 1 ##

# Hauteur maximale d'une liste d'immeubles
# et 0 si pas d'immeubles

def hauteur_max_immeubles(immeubles):
    """ Renvoie la hauteur max d'une liste d'immeubles """
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

# Calcul et tri des bords
# sans redondance

def calcul_bords(immeubles):
    """ Renvoie la liste des bords (droite + gauche) d'une listes d'immeubles """
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
    """ Renvoie un dictionnaire qui à un bord associe 
    la liste des numéros des immeubles correspondants """
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
    """ Calcul de la skyline d'une liste d'immeubles """

    # Initialisation des variables
    liste_bords = calcul_bords(immeubles)
    dico = dictionnaire_bords_immeubles(immeubles)
    skyline = []
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
## Question 5 ##

from random import randint
# Couleur au hasard
def choix_couleur():
    """ Renvoie couleur au hasard """
    R,V,B = randint(0,255), randint(0,255), randint(0,255)
    coul = '#%02x%02x%02x' % (R, V, B)
    return coul

# Affichage graphique avec matplotlib

import matplotlib.pyplot as plt

def affichage_skyline(immeubles,avec_immeubles=True,avec_skyline=True):
    """ Affichage de la skyline """

    plt.axes().set_aspect('equal')

    if avec_immeubles:
        for (x,y,h) in immeubles:
            listex = [x,x,y,y]
            listey = [0,h,h,0]   
            plt.plot([min(listex),max(listex)],[0,0],color='gray',linewidth=2)        
            plt.plot(listex,listey,"r",color='gray',linewidth=2,alpha=0.7)
            plt.fill(listex,listey,"r",color=choix_couleur(),linewidth=2,alpha=0.7)

    if avec_skyline:
        skyline = calcul_skyline(immeubles)
        listex = [x for (x,y) in skyline]
        listey = [y for (x,y) in skyline]
        plt.plot([min(listex),max(listex)],[0,0],color='black',linewidth=3)
        plt.plot(listex,listey,color='black',linewidth=3)

    plt.show()
    return

# Test
print("--- Affichage ---")

immeubles = [(0,1,5), (2,4,10), (3,5,7), (3,8,2), (7,9,4)]

immeubles = [(0,3,2), (2,4,7), (4,8,5), (6,7,8), (9,10,10), (11,12,9)]

# affichage_skyline(immeubles,avec_immeubles=True,avec_skyline=True)

##############################
def hasard_immeubles(n=10,N=10):
    """ Renvoie une liste aléatoire d'immeubles """
    liste = []
    for __ in range(N):
        x = randint(0,n)
        y = x + 1 + randint(5,n)//10
        h = 1+randint(0,n)//4
        liste += [(x,y,h)]
    return liste

immeubles = hasard_immeubles(n=100,N=30)
affichage_skyline(immeubles,avec_immeubles=True,avec_skyline=True)

