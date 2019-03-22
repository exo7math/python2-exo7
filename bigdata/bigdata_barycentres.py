
##############################
# Big data
##############################

from math import *
from random import *
import matplotlib.pyplot as plt


##############################
# Activité 3 - Barycentres
##############################

##############################
## Question 1 ##

xmin,xmax,ymin,ymax = 0,100,0,100 # Fenêtre des points


def afficher_points(points,couleurs):

    liste_couleurs = ["red","blue","green","orange","cyan","chartreuse","purple","black","pink"]
    n = len(points)

    for i in range(n):
        x,y = points[i]
        coul = couleurs[i]
        plt.scatter(x,y,color=liste_couleurs[coul],s=100)

    plt.axes().set_aspect('equal')
    plt.xlim(xmin-1,xmax+1)
    plt.ylim(ymin-1,ymax+1)
    plt.grid()
    plt.show()
    plt.close()
    return

# Test
points = [(20,20),(60,40),(40,80),(70,70)]
couleurs = [0,1,2,0]
# afficher_points(points,couleurs)


##############################
## Question 2 ##

def generer_points(k=3,nb_points=50,dispersion=20):

    points = []
    for __ in range(k):
        # centre
        xc = xmin + (xmax-xmin)*(0.2+0.6*random())
        yc = ymin + (ymax-ymin)*(0.2+0.6*random())

        n = 0
        while n < nb_points:
            theta = 2*pi*random()
            r = dispersion * random()**2
            x = xc + r*cos(theta)
            y = yc + r*sin(theta)
            if (xmin <= x <= xmax) and (ymin <= y <= ymax): 
                points = points + [(x,y)]
                n = n+1

    return points

# Test
points = generer_points(k=1,nb_points=100,dispersion=20)
couleurs = [0] * len(points)
# afficher_points(points,couleurs)


##############################
## Question 3 ##

def calcul_barycentre(points):
    """ Calcul les coordonnée (xG,yG) du barycentres des points) """
    n = len(points)
    if n == 0: return None
    xG = sum([pt[0] for pt in points ]) / n
    yG = sum([pt[1] for pt in points ]) / n
    return xG,yG

# Test
points = [(20,60),(40,20),(60,80)]
bar = calcul_barycentre(points)
# print("Points :",points)
# print("Barycentre :",bar)
# points = points + [bar]
# afficher_points(points,[0,0,0,1])


##############################
## Question 4 ##

## Question 4.a ##

def distance(P,Q):
    """ Calcule la distance entre deux points """
    x1,y1 = P
    x2,y2 = Q
    d = sqrt((x2-x1)**2 + (y2-y1)**2)
    return d


## Question 4.b ##

def barycentre_proche(P,barycentres):
    """ Renvoie le rang (c-à-d la couleur) du barycentre le plus proche """
    i0 = 0
    bar =  barycentres[0]
    d0 = distance(P,bar)
    for i in range(len(barycentres)):
        bar = barycentres[i]
        d = distance(P,bar)
        if d < d0:
            i0 = i
            d0 = d
    return i0
    
# Test
barycentres = [(80,40),(20,80),(60,60)]
point = (40,40)
# print(barycentre_proche(point,barycentres))
# afficher_points(barycentres+[point],[0,0,0,7])



##############################
## Question 4.c ##

def couleurs_barycentres_proches(points,barycentres):
    """ Pour chaque point renvoie la couleur c-à-d le rang du barycentre le plus proche """
    couleurs = []
    for pt in points:
        num_bar = barycentre_proche(pt,barycentres)
        couleurs = couleurs + [num_bar]
    return couleurs


# Test
barycentres = [(80,40),(20,80),(60,60)]
points = [(40,40),(20,40),(80,70),(50,10)]
# points = generer_points()
# afficher_points(points + barycentres,[7,7,7,7] + [0,1,2])
# couleurs = couleurs_barycentres_proches(points,barycentres)
# afficher_points(points + barycentres,couleurs + [0,1,2])



##############################
## Question 5 ##

def recalculer_barycentres(points,barycentres):
    k = len(barycentres)
    n = len(points)
    nouv_barycentres = []
    couleurs = couleurs_barycentres_proches(points,barycentres)
    for c in range(k):
        liste_partielle = []
        for i in range(n):
            if couleurs[i] == c:
                liste_partielle = liste_partielle + [points[i]]
        if len(liste_partielle) == 0:
            (x0,y0) = barycentres[c]
        else:
            (x0,y0) = calcul_barycentre(liste_partielle)
        nouv_barycentres = nouv_barycentres + [(x0,y0)]
    return nouv_barycentres


# Test
barycentres = [(80,40),(20,80),(40,20)]
# points = generer_points()
points = [(10,30),(30,20),(80,20),(30,40),(40,40),(20,50),(80,70),(40,70),(50,10),(70,60)]
n = len(points)
# afficher_points(points + barycentres,[7]*n + [3,4,5])
# couleurs = couleurs_barycentres_proches(points,barycentres)
# afficher_points(points + barycentres,couleurs + [3,4,5])
# nouv_barycentres = recalculer_barycentres(points,barycentres)
# afficher_points(points + nouv_barycentres,couleurs + [3,4,5])
# print(nouv_barycentres)


##############################
## Question 5 ##

def iterer_barycentres(points,barycentres_init):
    barycentres = list(barycentres_init)
    k = len(barycentres)
    couleurs = couleurs_barycentres_proches(points,barycentres)    

    while True:
        afficher_points(points + barycentres,couleurs + [7]*k)  

        nouv_barycentres = recalculer_barycentres(points,barycentres)
        nouv_couleurs = couleurs_barycentres_proches(points,nouv_barycentres)
 
        barycentres = list(nouv_barycentres)

        if couleurs == nouv_couleurs:           
            break

        couleurs = list(nouv_couleurs)

    return barycentres


# Test
# mon_k = 5
# points = generer_points(k=mon_k,nb_points=30,dispersion=20)
# print(points)
# afficher_points(points,[0]*len(points))
# barycentres_init = generer_points(k=mon_k,nb_points=1)
# barycentres_init = [(20,40),(80,40),(65,70),(50,20),(25,70)]
# barycentres = iterer_barycentres(points,barycentres_init)
# couleurs = couleurs_barycentres_proches(points,barycentres)
# afficher_points(points + barycentres,couleurs + [7]*mon_k) 
# print(barycentres)

# Pour le cours
# import exemple_barycentres
# points = exemple_barycentres.points
# barycentres_init = exemple_barycentres.barycentres_init
# afficher_points(points,[0]*len(points))
# barycentres = iterer_barycentres(points,barycentres_init)
# couleurs = couleurs_barycentres_proches(points,barycentres)
# afficher_points(points + barycentres,couleurs + [7]*3)

# Pour le cours
import exemple_barycentres_bis
points = exemple_barycentres_bis.points
barycentres_init = exemple_barycentres_bis.barycentres_init
afficher_points(points,[0]*len(points))
barycentres = iterer_barycentres(points,barycentres_init)
couleurs = couleurs_barycentres_proches(points,barycentres)
afficher_points(points + barycentres,couleurs + [7]*5)

##############################
## Question 6 - à virer ##

def erreur_barycentres(points,barycentres):
    
    n = len(points)
    k = len(barycentres)
    couleurs = couleurs_barycentres_proches(points,barycentres)
    err = 0

    for c in range(k):
        bar = barycentres[c]
        for i in range(n):
            if couleurs[i] == c:
                err = err + distance(points[i],bar)

    return err

# Test
# erreur  = erreur_barycentres(points,barycentres)
# print(erreur)