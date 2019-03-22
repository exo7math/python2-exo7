
##############################
# Logarithme
##############################

from math import *

##############################
# Activité 6 - Calculs des logarithmes I
##############################

##############################
## Question 1 ##

# ln(x) = ln(1+u) = u-u^2/2+u^3/3 + ...
# u = x - 1
def logarithme_serie_1(x,N):
    """ Calcul approché de ln(x) par une somme """
    u = x-1
    somme = 0
    for i in range(1,N):
        if i%2 == 0:
            somme = somme - (u**i)/i
        else:
            somme = somme + (u**i)/i
    return somme

##############################
## Question 2 ##

# ln(x) = ln(1+u/1-u) = 2 u + 2u^3/3 + 2 u^5/5 + ...
# u = (x-1)/(x+1)
def logarithme_serie_2(x,N):
    """ Calcul approché de ln(x) par une somme """
    u = (x-1)/(x+1)
    somme = 0
    for i in range(1,N,2):
        somme = somme + 2*(u**i)/i
    return somme

##############################
## Question 3 ##

def reduction_intervalle_e(x):
    """ Ecriture x = y * e^k avec 0.5 < y < 1.5, k exposant entier
    On ramène x par division par e à l'intervalle [0.5,1.5] """
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
x = 1.543
# x = 0.1234
N = 10
print("x =",x)
print("Précision N =",N)
print("Valeur python",log(x))
print("Valeur série 1",logarithme_serie_1(x,N))
print("Valeur série 2",logarithme_serie_2(x,N))


print("--- Réduction intervalle ---")
x = 12.34
y,k = reduction_intervalle_e(x)
print("x =",x,"y = ",y,"k =",k,"vérif = ",y*e**k)

##############################
## Question 4 ##

def logarithme_serie_3(x,N):
    """ Calcul approché de ln(x) par une somme """
    y,k = reduction_intervalle_e(x)
    logy = logarithme_serie_2(y,N)    # Méthode valide car y ~ 1
    logx = logy + k                   # Décalage
    return logx

# Test
print("--- Logarithme après réduction d'intervalle ---")
x = 154.3
N = 10
print("x =",x)
print("Précision N =",N)
print("Valeur python",log(x))
print("Valeur série 3 (après réduction)",logarithme_serie_3(x,N))

