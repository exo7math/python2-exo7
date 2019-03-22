
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


