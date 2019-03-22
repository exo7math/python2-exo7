
##############################
# Suites
##############################



##############################
# Rappels - Activité 1
##############################

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
    """ Calcule la distance entre deux listes de même longueur """

    n = len(u)-1
    somme = 0
    for i in range(n+1):
        somme = somme + abs(v[i]-u[i])

    return somme


##############################
## Question 2 ##

# Tiré de de Python (Livre 1) "Analyse de données - Statistique"

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
print("--- Calcul de la médiane ---")
liste = [3,6,9,11]
print(liste)

m = calcule_mediane(liste)
print("Médiane :",m)

liste_m = [m]*4
d = distance(liste,liste_m)
print("Distance à la médiane :",d)


##############################
## Question 3 ##

def balayage(v,N):
    """ Recherche d'une progression arithmétique u 
    qui approche au mieux la liste v.
    Le paramètre N correspond à la précision du balayge.
    La fonction renvoie un terme intitial u0 
    et une raison r. """

    n = len(v)-1

    pas = 2*(v[1]-v[0])/N

    dmin = 10000  # l'infini

    r = 0

    for k in range(N+1):

        w = [v[i]-i*r for i in range(n+1)]
        u0 = calcule_mediane(w)

        u = liste_arithmetique(n,u0,r)

        d = distance(u,v)

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

# Test
print("--- Balayage r ---")
v = [6,11,14,20,24,29,37]
n = len(v)-1
u0,r = balayage(v,10000)
print("---")
print("Suite à approcher :",v)
print("r =",r)
print("u0 =",u0)
u = liste_arithmetique(n,u0,r)
print("Suite arithmétique trouvée",u)
print("Erreur =",distance(u,v))
