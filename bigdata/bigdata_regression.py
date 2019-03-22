
##############################
# Big data
##############################

##############################
# Activité 5 - Régression linéaire
##############################


##############################
## Question 1 ##

def moyenne(liste):
    n = len(liste)
    somme = sum(liste)
    if n==0: 
        return 0
    else:
        return somme/n

def variance(liste):
    n = len(liste)
    m = moyenne(liste)
    somme = 0
    for x in liste:
        somme = somme + (x-m)**2
    return somme/n

def covariance(listex,listey):
    n = len(listex)  # = len(listey)
    mx = moyenne(listex)
    my = moyenne(listey)
    somme = 0
    for i in range(n):
        x = listex[i]
        y = listey[i]
        somme = somme + (x-mx)*(y-my)
    return somme/n

# Test
print("--- Moyenne, variance, covariance---")
liste = [1,2,3,4,5]
print("liste : ",liste)
print("moyenne :",moyenne(liste)) 
print("variance :",variance(liste))
print("covariance de la liste avec elle même = variance :",covariance(liste,liste))

listex = [1,2,3,4,5]
listey = [4,5,4,7,6]
print("liste des x : ",listex)
print("liste des y : ",listey)
print("covariance  :",covariance(listex,listey))

##############################
## Question 2 ##

def regression_lineaire(points):
    listex = [x for (x,y) in points]
    listey = [y for (x,y) in points]
    a = covariance(listex,listey)/variance(listex)
    b = moyenne(listey)-a*moyenne(listex)
    return a,b

# Heures/notes
print("--- Régression linéaire ---")
eleves = [(0.25,5),(0.5,4),(0.75,7),(1,6),(1,7),(1,10),(1.5,9),(1.75,14),(2,9),(2,11),(2.25,15),(2.5,10),(2.5,13),(2.75,18),(3,13),(3,16)]

# Pour le cours
cours = [(1,13),(2,10),(2,15),(3,8),(3,14),(5,7),(5,10),(6,3),(7,5),(7,9),(8,4),(9,1),(9,5),(10,2)]

a,b = regression_lineaire(eleves)
print("a,b",a,b)

##############################
## Question 3 ##

import matplotlib.pyplot as plt
import numpy as np  # juste pour la grille de numérotation !!

def afficher(points):

    # Points
    n = len(points)
    for i in range(n):
        x,y = points[i]
        plt.scatter(x,y,color='blue') 

    # Droite
    a,b = regression_lineaire(points)
    # Deux points P1 = (x1,y1), P2=(x2,y2) de la droite y = ax+b
    listex = [x for (x,y) in points]
    x1 = min(listex)-1
    y1 = a*x1 + b
    x2 = max(listex)+1
    y2 = a*x2 + b
    plt.plot([x1,x2],[y1,y2],color='red')

    # Axes
    # plt.axis('equal')
    plt.xlim(0,4)   
    plt.ylim(0,20)
    plt.yticks(range(0,21,2))

    # Pour cours
    # plt.xlim(0,11)   
    # plt.ylim(0,16)
    # plt.xticks(range(0,12,1))   
    # plt.yticks(range(0,17,1))    
    plt.grid()



    plt.show()
    plt.close()
    return

# Test
afficher(eleves)


##############################
## Question 4 ##

def combien_de_temps():
    note_str = input("Quelle note voudrais-tu obtenir ? ")
    y = float(note_str)
    a,b = regression_lineaire(eleves)
    x = (y-b)/a

    # heure_str = '{0:.2f}'.format(x)
    heures = int(x)
    minutes = int((x-heures)*60)
    print("Tu dois travailler au moins",str(heures),"heures et",str(minutes),"minutes.")
    return

# Test
print("--- Travailler plus pour gagner plus ---")
combien_de_temps()
