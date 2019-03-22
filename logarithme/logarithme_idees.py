
##############################
# Logarithme
##############################


##############################
# Activité 1 - Le logarithme décimal - Échelle de Richter
##############################

from math import *

##############################
## Question 1 ##

def magnitude(E):
    M = 2/3 * log(E/(1.6*10**-5),10) -3.2
    return M


# Test
print("--- Échelle de Richter ---")
# Vérification -> M ~ 4
E0 = 10**6
print("Energie E =",E0,"magnitude M = ",magnitude(E0))



##############################
## Question 2 ##

# Energie = puissance de 10, afficher magnitude jusqu'à avoir M>9
E = E0
for i in range(6,15):
    E = 10**i
    print("E = 10^",i,"  Energie E =",E,"  magnitude M = ",magnitude(E))



##############################
## Question 3 ##

# Trouver E tel que M = 7 (tatonnment, balyage, calcul):
# Tâtonnement + balayage
for E in range(10**10,10**11,10**9):
    print("Energie E =",E,"  magnitude M = ",magnitude(E))

# Réponse E = 3.2 * 10*10


##############################
## Question 4 ##

# Montrer que si E = 1000 E0 alors M = M0+2
# Quelle facteur k, pour E = k E0 donne M = M0 + 1
# Réponse k = sqrt(1000) ~ 32 


##############################
# Activité 2 - Le logarithme décimal - Décibels
##############################

##############################
## Question 1 ##

def decibel(P):
    P0 = 2 * 10**-5
    D = 20 * log(P/P0,10)
    return D

# Test
print("--- Décibel ---")
# Vérification -> D ~ 94
P = 1
print("Pression P =",P,"décibels D = ",decibel(P))


##############################
## Question 2 ##

# compléter tableau



##############################
# Activité 3 - Le logarithme décimal - Partie entière
##############################

def logarithme_entier(x):  # x >= 1
    l = 0
    while 10**l <= x:
        l = l + 1
    return l-1

# Test
print("--- Partie entière du logarithme ---")
for x in range(1,11):
    print("x =",x)
    print("mon calcul",logarithme_entier(x))
    print("Python",log(x,10))



##############################
# Activité 4 - Le logarithme décimal - Échelle logarithmique
##############################

import matplotlib.pyplot as plt

def afficher_points_xy(points):
    for (x,y) in points:
        plt.scatter(x,y,color="red")

def afficher_points_xlogy(points):
    for (x,y) in points:
        plt.scatter(x,log(y,10),color="green")

def afficher_points_logxlogy(points):
    for (x,y) in points:
        plt.scatter(log(x,10),log(y,10),color="blue")


# Test
points1 = [ (x,1.5*x+2) for x in [2,3,5,7,11] ]      # y = ax+b a=1.5, b=-2
points2 = [ (x,exp(0.25*x+1)) for x in [2,3,5,7,11] ]  # y = exp(a x + b) log(y) = a x + b
points3 = [ (x,2*x**1.5) for x in [2,3,5,7,11] ]     # y = beta x^alpha, log(y) = alpha*log(x) + log(beta) 
points = points3
print(points)
afficher_points_xy(points)
# afficher_points_xlogy(points)
# afficher_points_logxlogy(points)
# plt.axes().set_aspect('equal')
# plt.xlim(xmin=0)
# plt.ylim(ymin=0)
# plt.grid()
# plt.show()



##############################
# Activité 5 - Le logarithme népérien
##############################

from math import *

##############################
## Question 1 ##

a = 2
b = 3
e = exp(1)
n = 7

print("--- Propriétés du logarithme ---")
print(log(a*b),log(a)+log(b))
print(log(a/b),log(a)-log(b))
print(log(1/a),-log(a))
print(log(a**n),n*log(a))
print(log(sqrt(a)),0.5*log(a))
print(a**b,exp(b*log(a)))

##############################
## Question 2 ##


def table_ln(x,N):
    l = floor(log(x)*10**N)/10**N
    return l

def table_exp(x,N):
    e = floor(exp(x)*10**N)/10**N
    return e

# Test
print("--- Table des logarithme ---")
N = 4
print("Nombre de chiffre après la virgule N=",N)
x = 54
print("x =",x)
print("ln(x) =",table_ln(x,N))
y = 1.23
print("y =",y)
print("exp(y) =",table_exp(y,N))



##############################
## Question 3 ##

def multiplication(a,b,N):
    la = table_ln(a,N)
    lb = table_ln(b,N)
    lc = la + lb
    c = table_exp(lc,N)
    return c
# Test
print("--- Produit par table des logarithme ---")
N = 5
print("Nombre de chiffre après la virgule de la table N=",N)
a = 98.765
b = 43.201
print("a =",a)
print("b =",b)
print("par table   : c =",multiplication(a,b,N))
print("vérfication : c =",a*b)



##############################
# Activité 6 - Le logarithme en base 2 (ou pas)
##############################

from math import *

##############################
## Question 1 ##

def logarithme_entier_2(n):
    l = 0
    while 2**l <= n:
        l = l + 1
    return l-1

 # Test
print("--- Partie entière du logarithme en base 2 ---")
for x in range(1,20):
    print("x =",x)
    print("mon calcul",logarithme_entier_2(x))
    print("Python",log(x,2))



##############################
## Question 2 ##

def dichotomie(n):
    compteur = 0
    while n>1:
        n = max(n//2,n-n//2)
        compteur = compteur + 1
    return compteur

 # Test
print("--- Dichotomie et logarithme en base 2 ---")
for n in range(4,10):
    print("n =",n)
    print("dichotomie",dichotomie(n))
    print("Python",ceil(log(n,2)))    
    print("log2 entier",logarithme_entier_2(n))  # valable uiqueme si n puissance de 2 (sinon faire +1)


##############################
## Question 3 ##

def logarithme_base(x,b):
    return log(x)/log(b)

# Test
print("--- Logarithme en base quelconque ---")
x = 555
b = 10
print("x =",x)
print("Moi log(x,b)",logarithme_base(x,b))   
print("Python log(x,b)",log(x,b))



##############################
## Question 4 ##

def nombre_de_chiffres(n,b):
    return floor(logarithme_base(n,b))+1
# Test
print("--- Nombre de chiffres ---")
n = 16
print("base 10, n =",n)
print("nb chiffres",nombre_de_chiffres(n,10))
print("base 2, n =",bin(n))
print("nb chiffres",nombre_de_chiffres(n,2))
print("base 16, n =",hex(n))
print("nb chiffres",nombre_de_chiffres(n,16))



##############################
# Activité 7 - Calculs des logarithmes
##############################

# ln(x) = ln(1+u) = u-u^2/2+u^3/3 + ...
# u = x - 1
def logarithme_serie_1(x,N):
    u = x-1
    somme = 0
    for i in range(1,N):
        if i%2 == 0:
            somme = somme - (u**i)/i
        else:
            somme = somme + (u**i)/i
    return somme


# ln(x) = ln(1+u/1-u) = 2 u + 2u^3/3 + 2 u^5/5 + ...
# u = (x-1)/(x+1)
def logarithme_serie_2(x,N):
    u = (x-1)/(x+1)
    somme = 0
    for i in range(1,N,2):
        somme = somme + 2*(u**i)/i
    return somme

# Ecriture x = y * e^k avec 0.5 < y < 1.5, k exposant entier
def reduction_intervalle_e(x):
    y = x
    k = 0
    # Cas x trop grand
    while y > 1.5:
        y =  y/e  # e = exp(1) définie dans le module math
        k += 1
    # Cas x trop petit
    while y < 0.5:
        y = y*e 
        k += -1
    return y, k


# Test
print("--- Calcul du logarithme ---")
x = 1.934
# x =12.34
# x = 0.1234
N = 10
print("x =",x)
print("Précision N=",N)
print("Valeur python",log(x))
print("Valeur série 1",logarithme_serie_1(x,N))
print("Valeur série 2",logarithme_serie_2(x,N))

print("--- Réduction intervalle ---")
x = 12.34
y,k = reduction_intervalle_e(x)
print("x =",x,"y = ",y,"k =",k,"vérif = ",y*e**k)

def logarithme_serie_3(x,N):
    y,k = reduction_intervalle_e(x)
    logy = logarithme_serie_2(y,N)    # Méthode valide car y ~ 1
    logx = logy + k                   # Décalage
    return logx

# Test
print("--- Logarithme après réduction d'intervalle ---")
x = 123.4
N = 10
print("x =",x)
print("Précision N=",N)
print("Valeur python",log(x))
print("Valeur série 3 (après réduction)",logarithme_serie_3(x,N))



# ln(x) est la solution de exp(y)=x
# Donc méthode de Newton avec f(u) = exp(u) - x
# u <- u - f(u)/f'(u)
def logarithme_inverse(x,N):

    u = 1

    for i in range(N):
        # print(i,u)
        u = u - (exp(u)-x)/exp(u)

    return u

# Test
print("--- Logarithme comme réciproque de l'exponentielle ---")
x = 1.234
N = 10
print("x =",x)
print("Précision N =",N)
print("Valeur python",log(x))
print("Valeur par réciproque",logarithme_inverse(x,N))


# Ecriture x = y * 10^k avec 1 <= y < 10, k exposant entier
def reduction_intervalle_10(x):
    y = x
    k = 0
    # Cas x trop grand
    while y > 10:
        y =  y/10  
        k += 1
    # Cas x trop petit
    while y < 1:
        y = y*10 
        k += -1
    return y, k


# CORDIC
# D'après Nicole ROBB - APMEP
def logarithme_cordic(x,N):
    # Réduction d'intervalle
    x, k = reduction_intervalle_10(x)

    # x dans [1,10]
    y = log(10)
    for i in range(N):
        z = 1 + 10**-i
        while x*z <= 10:
            x = x*z
            y = y - log(z)

    return y + k*log(10)  # Résultat après décalage de k*ln(10)

# Test
print("--- Logarithme par algorithme CORDIC ---")
x = 1200
N = 10
print("x =",x)
print("Précision N =",N)
print("Valeur python",log(x))
print("Valeur CORDIC",logarithme_cordic(x,N))


# Algorithme de Briggs 2^n ln(x) = ln(x^(1/2^n))
# puis ln(u) ~ u-1 pour u proche de 0

def logarithme_briggs(x,epsilon):
    n = 0
    while abs(x-1) > epsilon:
        x = sqrt(x)
        n = n+1

    l = x-1
    for i in range(n):
        l = 2*l

    return l


# Test
print("--- Logarithme par algorithme de Briggs ---")
x = 1.234
epsilon = 0.00001
print("x =",x)
print("Précision epsilon =",epsilon)
print("Valeur python",log(x))
print("Valeur Briggs",logarithme_briggs(x,epsilon))




