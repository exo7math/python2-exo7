
##############################
# Big data
##############################

from math import *
from random import *
import matplotlib.pyplot as plt


##############################
# Activité - Voisins
##############################

##############################
## Question 1 ##

## Question 1.a ##

def afficher_cpoints(cpoints):

    for x,y,c in cpoints:
        if c == 0:
            plt.scatter(x,y,color='red',s=100)
        elif c == 1:
            plt.scatter(x,y,color='blue',marker="s",s=100)
        elif c == 2:
            plt.scatter(x,y,color='red',s=100)
        elif c == 3:
            plt.scatter(x,y,color='blue',marker="s",s=100)           
        elif c == 4:
            plt.scatter(x,y,color='black',marker="*",s=100)
    
    plt.axes().set_aspect('equal')
    plt.xlim(xmin-0.5,xmax+0.5)
    plt.ylim(ymin-0.5,ymax+0.5)
    # plt.xticks(range(xmin,xmax+1,10))
    # plt.yticks(range(ymin,ymax+1,10))
    plt.grid()
    plt.show()
    plt.close()
    return

# Test
print("--- Affichage de cpoints ---")
xmin,xmax,ymin,ymax = 0,10,0,10 # Fenêtre des cpoints
cpoints = [(2,3,0),(5,7,1)]
# afficher_cpoints(cpoints)


## Question 1.b ##

def fonction_couleur(x,y):

    res = ((x**2+3*y**2) % 100) - 50

    # res = (0.1*(y-ymax/2))**2 - (0.1*(x-xmax/2))**3 + (0.1*(x-xmax/2)) - xmax/100
    # res = (x-xmax/2)**3-3*(x-xmax/2)*(y-ymax/2)**2 - xmax

    # res = randint(0,1)

    if res > 0:
        return 1
    else:
        return 0


## Question 1.c ##

def generer_cpoints(N):

    cpoints = []
    for __ in range(N):
        x = int((xmax-xmin)*random())
        y = int((ymax-ymin)*random())
        c = fonction_couleur(x,y)
        if ((x,y,0) not in cpoints) or ((x,y,1) not in cpoints):
            cpoints = cpoints + [(x,y,c)]

    return cpoints

# Test
xmin,xmax,ymin,ymax = 0,100,0,100 # Fenêtre des cpoints
cpoints = generer_cpoints(30)
# afficher_cpoints(cpoints)



##############################
## Question 2 ##

## Question 2.a ##

def distance(P,Q):
    x1,y1 = P
    x2,y2 = Q
    d = sqrt((x2-x1)**2 + (y2-y1)**2)
    return d


## Question 2.b ##

def un_voisin_proche(P,cpoints):
    dmin = 1000  # un très grand nb ou bien l'infini de Python : 'inf'

    for Qc in cpoints:
        d = distance(P,Qc[0:2])
        if d < dmin:
            dmin = d
            Qcmin = Qc

    return Qcmin


# Test
xmin,xmax,ymin,ymax = 0,10,0,10 # Fenêtre des cpoints
P = (4,3)
cpoints = [ (8,6,0), (1,2,0), (5,9,1), (6,2,1) ]
x,y,c = un_voisin_proche(P,cpoints)
Pc = (P[0],P[1],4)
# afficher_cpoints(cpoints+[Pc])
print(cpoints)
print(Pc)




##############################
## Question 3 ##

def colorier_par_un_voisin_proche(cpoints):

    for x,y,c in cpoints:
        if c == 0:
            plt.scatter(x,y,color='red',s=75)
        elif c == 1:
            plt.scatter(x,y,color='blue',s=75,marker="s")

    pts = [ (x,y) for x,y,c in cpoints]  # cpoints références

    for x in range(xmin,xmax+1):
        for y in range(ymin,ymax+1):
            if (x,y) not in pts:
                c = un_voisin_proche((x,y),cpoints)[2]
                if c == 0:
                    plt.scatter(x,y,color='red',s=20, alpha=0.7)
                elif c == 1:
                    plt.scatter(x,y,color='blue',s=20,marker="s", alpha=0.7)           

    plt.axes().set_aspect('equal')
    plt.xlim(xmin-0.5,xmax+0.5)
    plt.ylim(ymin-0.5,ymax+0.5)
    plt.grid()
    plt.show()
    plt.close() 

    return

# Test
xmin,xmax,ymin,ymax = 0,10,0,10
cpoints = [ (5,4,0), (5,9,1), (2,8,0), (6,1,1) ]
# afficher_cpoints(cpoints)
# colorier_par_un_voisin_proche(cpoints)

xmin,xmax,ymin,ymax = 0,40,0,40
cpoints = generer_cpoints(20)
# afficher_cpoints(cpoints)
# colorier_par_un_voisin_proche(cpoints)


##############################
## Question 4 ##

## Question 4.a ##

def les_voisins_proches(P,cpoints,k):

    liste_voisins = []
    liste_distances = []

    for Qc in cpoints:

        d = distance(P,Qc[0:2])
       
        # On commence par prendre les k premiers
        if len(liste_voisins) < k:
            liste_voisins = liste_voisins + [Qc]
            liste_distances = liste_distances + [d]

        else: 
            dmax = max(liste_distances)  # le maximum parmi les plus petites distances !
            if d < dmax:
                imax = liste_distances.index(dmax)
                del liste_voisins[imax]
                del liste_distances[imax]
                liste_voisins = liste_voisins + [Qc]
                liste_distances = liste_distances + [d]     

    return liste_voisins


# Test
print("--- Voisins proches ---")
P = (18,45)
cpoints = [ (20,10,0), (20,59,1), (15,50,0) ]
voisins = les_voisins_proches(P,cpoints,2)
print(voisins)


## Question 4.b ##

def couleur_majoritaire(cpoints):
    nb_zero = len([pt for pt in cpoints if pt[2]==0])
    nb_un = len(cpoints) - nb_zero
    if nb_zero >= nb_un:
        return 0
    else: 
        return 1

# Test
print("--- Couleur majoritaire ---")
cpoints = [ (20,10,0), (20,59,1), (15,50,1), (5,5,0) ]
print(couleur_majoritaire(cpoints))


## Question 4.c ##

def colorier_par_les_voisins_proches(cpoints,k):

    for x,y,c in cpoints:
        if c == 0:
            plt.scatter(x,y,color='red',s=50)
        elif c == 1:
            plt.scatter(x,y,color='blue',s=50,marker="s")

    pts = [ (x,y) for x,y,c in cpoints]  # cPoints références

    for x in range(xmin,xmax+1):
        for y in range(ymin,ymax+1):
            if (x,y) not in pts:
                voisins = les_voisins_proches((x,y),cpoints,k)
                c = couleur_majoritaire(voisins)
                if c == 0:
                    plt.scatter(x,y,color='red',s=20, alpha=0.7)
                elif c == 1:
                    plt.scatter(x,y,color='blue',s=20,marker="s", alpha=0.7)           

    plt.axes().set_aspect('equal')
    plt.xlim(xmin-0.5,xmax+0.5)
    plt.ylim(ymin-0.5,ymax+0.5)
    plt.grid()
    plt.show()
    plt.close() 

    return

xmin,xmax,ymin,ymax = 0,10,0,10
cpoints = [ (3,2,0), (6,4,1), (3,5,1), (2,8,0), (3,6,0), (7,7,1), (9,4,0) ]
# voisins = les_voisins_proches((2,1),cpoints,3)
# print(voisins)
# print(couleur_majoritaire(voisins))
# afficher_cpoints(cpoints)
# colorier_par_les_voisins_proches(cpoints,1)
# colorier_par_les_voisins_proches(cpoints,2)
# colorier_par_les_voisins_proches(cpoints,3)

xmin,xmax,ymin,ymax = 0,50,0,50
cpoints = generer_cpoints(100)
afficher_cpoints(cpoints)
colorier_par_les_voisins_proches(cpoints,3)
colorier_par_les_voisins_proches(cpoints,5)
colorier_par_les_voisins_proches(cpoints,7)

