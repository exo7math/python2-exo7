
##############################
# Suites
##############################



##############################
# Activité 3 - Suites géométrique
##############################

##############################
## Question 1 ##

def geometrique_1(n,u0,q):
    """ Renvoie le terme de rang n d'une suite géométrique 
    de terme initial u0 et de raison q
    par formule de récurrence """

    u = u0
    for i in range(n):
        u = u * q
    return u


##############################
## Question 2 ##

def geometrique_2(n,u0,q):
    """ Renvoie le terme de rang n d'une suite géométrique 
    de terme initial u0 et de raison q
    par formule directe """

    return u0 * (q ** n)


##############################
## Question 3 ##

def liste_geometrique(n,u0,q):
    """ Renvoie la liste des termes de rang 0 à n d'une suite géométrique 
    de terme initial u0 et de raison q
    par formule de récurrence """

    liste = [u0]
    u = u0
    for i in range(n):
        u = u * q
        liste = liste + [u]
    return liste


##############################
## Question 4 ##

def est_geometrique(liste):
    """ Teste si la liste correspond aux premiers 
    termes d'une suite géométrique """

    n = len(liste)-1

    u0 = liste[0]
    u1 = liste[1]
    q = u1 / u0

    liste_arith = liste_geometrique(n,u0,q)

    if liste == liste_arith:
        return True
    else:
        return False


# Tests
print("--- Suites géométriques ---")
u0 = 2
q = 3
print(geometrique_1(2,u0,q))
print(geometrique_2(2,u0,q))
print(liste_geometrique(5,u0,q))

liste = [2,6,18,54,162]
print(liste)
print(est_geometrique(liste))


##############################
## Question 5 ##

def somme_geometrique_1(n,u0,q):
    """ Renvoie la somme des termes de rang 0 à n d'une suite géométrique 
    de terme initial u0 et de raison q
    par formule de récurrence """

    u = u0
    s = u0
    for i in range(n):
        u = u * q
        s = s + u

    return s

def somme_geometrique_2(n,u0,q):
    """ Renvoie la somme des termes de rang 0 à n d'une suite géométrique 
    de terme initial u0 et de raison q
    par formule directe """

    s = u0 * (1 - q**(n+1))/(1-q)

    return s    

# Tests
print("--- Sommes suites géométriques ---")
u0 = 1
q = 1/2
print(somme_geometrique_1(10,u0,q))
print(somme_geometrique_2(10,u0,q))


