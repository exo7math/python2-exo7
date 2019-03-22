
##############################
# Suites
##############################



##############################
# Activité 1 - Suites arithmétiques
##############################

##############################
## Question 1 ##

def arithmetique_1(n,u0,r):
    """ Renvoie le terme de rang n d'une suite arithmétique 
    de terme initial u0 et de raison r
    par formule de récurrence """

    u = u0
    for i in range(n):
        u = u + r
    return u


##############################
## Question 2 ##

def arithmetique_2(n,u0,r):
    """ Renvoie le terme de rang n d'une suite arithmétique 
    de terme initial u0 et de raison r
    par formule directe """

    return u0 + n*r


##############################
## Question 3 ##

def liste_arithmetique(n,u0,r):
    """ Renvoie la liste des termes de rang 0 à n d'une suite arithmétique 
    de terme initial u0 et de raison r
    par formule de récurrence """

    liste = [u0]
    u = u0
    for i in range(n):
        u = u + r
        liste = liste + [u]
    return liste


##############################
## Question 4 ##

def est_arithmetique(liste):
    """ Teste si la liste correspond aux premiers termes d'une suite arithmétique """

    n = len(liste)-1

    u0 = liste[0]
    u1 = liste[1]
    r = u1 - u0

    liste_arith = liste_arithmetique(n,u0,r)

    if liste == liste_arith:
        return True
    else:
        return False


# Tests
print("--- Suites arithmétiques ---")
u0 = 2
r = 3
print(arithmetique_1(1,u0,r))
print(arithmetique_2(1,u0,r))
print(liste_arithmetique(1,u0,r))

liste = [2,5,8,11,12]
print(est_arithmetique(liste))


##############################
## Question 5 ##

def somme_arithmetique_1(n,u0,r):
    """ Renvoie la somme des termes de rang 0 à n d'une suite arithmétique 
    de terme initial u0 et de raison r
    par formule de récurrence """

    u = u0
    s = u0
    for i in range(n):
        u = u + r
        s = s + u

    return s

def somme_arithmetique_2(n,u0,r):
    """ Renvoie la somme des termes de rang 0 à n d'une suite arithmétique 
    de terme initial u0 et de raison r
    par formule directe """

    s = (n+1)*u0+(n*(n+1)//2)*r

    return s    

# Tests
print("--- Sommes suites arithmétiques ---")
u0 = 2
r = 3
print(somme_arithmetique_1(10,u0,r))
print(somme_arithmetique_2(10,u0,r))



##############################
# Activité 2 - Suites arithmétiques
##############################

# But : rechercher dans une liste s'il existe trois termes
# qui forment un partie d'une suite arithmétiques.
# Il s'agit donc de trouver trois termes u[i],u[j],u[k] tels que 
# u[i] = u[j] - r, u[k] = u[j] + r (pour un certain r>0).
# On suppose la liste ordonnée.

# Ref : "Finding longest arithmetic progressions" by Jeff Erickson


def chercher_arithmetique(u):
    """ ... """

    n = len(u)
    for j in range(n):
        i = j-1
        k = i + 1
        while (i>=0) and (k<n):
            if u[j]-u[i] == u[k]-u[j]:
                return u[i],u[j],u[k]
            if u[j]-u[i] < u[k]-u[j]:
                i = i - 1
            if u[j]-u[i] > u[k]-u[j]:
                k = k + 1                

    return None

# Test
print("--- Recherche d'une progression arithmétique ---")

u = [10,11,13,17,19,23,29,31]
print(chercher_arithmetique(u))

# from random import *


##############################
# Activité 3 - Suites géométriques
##############################



##############################
## Question 1 ##


##############################
## Question 2 ##


##############################
## Question 3 ##



##############################
# Activité 4 - Tracer la somme d'une suite géométrique
##############################

from turtle import *

##############################
## Question 1 ##

def affiche_un_carre(longueur):
    for i in range(4):
        forward(longueur)
        left(90)
    return


##############################
## Question 2 ##

def decoupe_un_carre(longueur):
    # On mémorise la position
    x,y = position()
    angle = heading()
    # On avance
    left(90)
    forward(longueur/2)
    right(90)
    forward(longueur)
    # On revient à la position de départ
    up()
    goto(x,y)
    setheading(angle)
    down()
    return


##############################
## Question 3 ##

def affiche_les_carres(n):
    
    cote  = 256
    up()
    goto(-cote//2,-cote//2)
    down()
    width(2)
    color('blue')

    for k in range(n):
        affiche_un_carre(cote / 2**k)
        decoupe_un_carre(cote / 2**k)
    
    exitonclick()
    return

# Lancement !
# affiche_les_carres(4)











##############################
# Activité 5 - Meilleure suite arithmétique
##############################

# On a une liste
# On cherche les termes d'une suite arithmétique 
# qui approximent le mieux cette liste

# v la liste à approcher
# u la meileure suite de premier terme u0 et de raison r
# c-à-d somme(|v_i-u_i|) minimale

##############################
## Question 1 ##

def distance(u,v):
    n = len(u)-1
    somme = 0
    for i in range(n+1):
        somme = somme + abs(v[i]-u[i])

    return somme


##############################
## Question 2 ##

def calcule_mediane(liste):
    """ Calcule la médiane des éléments
    Entrée : une liste de nombre
    Sortie : leur médiane """        
    liste_triee = sorted(liste)

    n = len(liste_triee)

    if n%2 == 0:   # n est pair
        indice_milieu = n//2
        mediane = (liste_triee[indice_milieu-1]+liste_triee[indice_milieu]) / 2
    else: 
        indice_milieu = (n-1)//2 
        mediane = liste_triee[indice_milieu]

    return mediane

# Test
print("--- Calcule médiane ---")
liste = [3,6,9,12]
print(calcule_mediane(liste))

##############################
## Question 3 ##

def balayage(v,N):
    n = len(v)-1

    pas = 2*(v[1]-v[0])/N

    dmin = 10000  # l'infini

    r = 0

    for k in range(N+1):

        w = [v[i]-i*r for i in range(n+1)]
        u0 = calcule_mediane(w)

        u = liste_arithmetique(n,u0,r)

        d = distance(u,v)
        print(w,u0,r,d,u)
        if d < dmin:
            dmin = d
            rmin = r
            u0min = u0
        r = r + pas

    print(u0min,rmin,dmin)
    return u0min,rmin

# Test
print("--- Balayage r ---")
v = [3,6,9,11]
n = len(v)-1
u0,r = balayage(v,10)
print("---")
print("Suite à approcher :",v)
print("r =",r)
print("u0 =",u0)
u = liste_arithmetique(n,u0,r)
print("Suite arithmétique trouvée",u)
print("Erreur =",distance(u,v))




##############################
## Question 3 ##




##############################
# Activité 4 - Suites arithmético-géométriques
##############################

# Idem sauf somme


##############################
## Question 1 ##


##############################
## Question 2 ##


##############################
## Question 3 ##



