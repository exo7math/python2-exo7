
##############################
# Logarithme
##############################

from math import *

##############################
# Activité 7 - Calculs des logarithmes II
##############################


##############################
## Question 1 ##

def logarithme_inverse(x,N):
    """ Calcul approché de ln(x) comme solution de exp(y)=x 
    Calcul par méthode de Newton  avec 
    f(u) = exp(u) - x u <- u - f(u)/f'(u) """
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


##############################
## Question 2 ##

# Ecriture x = y * 10^k avec 1 <= y < 10, k exposant entier
def reduction_intervalle_10(x):
    """ Ecriture x = y * 10^k avec 1 <= y < 10, k exposant entier
    On ramène x par division par e à l'intervalle [0.5,1.5] """    
    y = x
    k = 0
    # Cas x trop grand
    while y >= 10:
        y =  y/10  
        k += 1
    # Cas x trop petit
    while y < 1:
        y = y*10 
        k += -1
    return y, k


##############################
## Question 3 ##

def logarithme_cordic(x,N):
    """ Calcul approché de ln(x) par l'algorithme CORDIC
    D'après Nicole Robb - APMEP """

    # Réduction d'intervalle
    y, k = reduction_intervalle_10(x)

    # y dans [1,10[
    p = log(10)
    for i in range(N):
        q = 1 + 10**-i
        print(q,y)
        while q*y <= 10:
            print(q,y)
            y = q*y
            p = p - log(q)

    return p + k*log(10)  # Résultat après décalage de k*ln(10)

# Test
print("--- Logarithme par algorithme CORDIC ---")
x = 37
N = 4
print("x =",x)
print("Précision N =",N)
print("Valeur python",log(x))
print("Valeur CORDIC",logarithme_cordic(x,N))


##############################
## Question 4 ##

def logarithme_briggs(x,epsilon):
    """ Calcul approché de ln(x) par l'algorithme de Briggs
    2^n ln(x) = ln(x^(1/2^n))
    puis ln(u) ~ u-1 pour u proche de 0 """
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
x = 1.543
epsilon = 10**-10
print("x =",x)
print("Précision epsilon =",epsilon)
print("Valeur python",log(x))
print("Valeur Briggs",logarithme_briggs(x,epsilon))




