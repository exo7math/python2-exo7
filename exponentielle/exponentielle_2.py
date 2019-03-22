
##############################
# Exponentielle
##############################

from math import *

# La fonction exponentielle est importée mais
# juste pour vérification des formules

##############################
# Activité 2 - Définition de l'exponentielle
##############################


##############################
## Question 1  ##

def exponentielle_limite(x,n):
    """ Valeur approchée de exp(x) par limite """
    expo = (1+x/n)**n
    return expo

##############################
## Question 2  ##

def factorielle(n):
    """ Calcul de n! par une boucle """
    fact = 1
    for k in range(1,n+1):
        fact = fact* k
    return fact

##############################
## Question 3  ##

def exponentielle_somme(x,n):
    """ Valeur approchée de exp(x) par somme """
    expo = 0
    for k in range(n+1):    
        expo = expo + (x**k)/factorielle(k)
    return expo

    
##############################
## Question 4  ##

# e^x = 1 + (x/1) (1 + (x/2) (1 + (x/3) (........) ) ) 
def exponentielle_horner(x,n):
    """ Valeur approchée de exp(x) par Hörner pour limiter les mutliplications """
    expo = 1
    for k in reversed(range(1,n+1)):   
        expo = x/k * expo + 1
    return expo


    
##############################
## Question 5  ##

# Exponentielle via les fractions continues
# https://en.wikipedia.org/wiki/Euler%27s_continued_fraction_formula
def exponentielle_euler(x,n):
    """ Valeur approchée de exp(x) par les fractions continues """
    expo = 0
    for k in reversed(range(1,n+1)):   
        expo = x/(k+x-k*expo)
    expo = 1/(1-expo)
    return expo


##############################
## Question 6  ##

# e = exponentielle_somme(1,n=25)

def exponentielle_astuce(x,n):
    """ Valeur approchée de exp(x) en réduisant d'abord la valeur de x """
    e = 2.718281828459045
    k = floor(x)  # partie entière
    f = x-k       # partie fractionnaire
    expo_entier = e**k 
    expo_frac = exponentielle_somme(f,n=n)
    expo = expo_entier * expo_frac
    return expo


# Test
print("--- Définition(s) de l'exponentielle ---")
print("- Exemple 1 -")
x = 2.8
print("x =",x)
print("Valeur python :",exp(x))
print("Valeur limite :",exponentielle_limite(x,n=100))
print("Valeur somme :",exponentielle_somme(x,n=10))
# print("Valeur somme inverse :",exponentielle_somme_inverse(x,n=20))
print("Valeur somme Hörner :",exponentielle_horner(x,n=10))
print("Valeur Euler :",exponentielle_euler(x,n=10))
print("Valeur astuce :",exponentielle_astuce(x,n=10))

##
print("- Exemple 2 -")
x = 0.1
print("x =",x)
print("Valeur python :",exp(x))
print("Valeur limite :",exponentielle_limite(x,n=100))
print("Valeur somme :",exponentielle_somme(x,n=10))
# print("Valeur somme inverse :",exponentielle_somme_inverse(x,n=20))
print("Valeur somme Hörner :",exponentielle_horner(x,n=10))
print("Valeur Euler :",exponentielle_euler(x,n=10))
print("Valeur astuce :",exponentielle_astuce(x,n=10))

##
print("- Exemple 3 -")
x = 100.5
print("x =",x)
print("Valeur python :",exp(x))
print("Valeur limite :",exponentielle_limite(x,n=100))
print("Valeur somme :",exponentielle_somme(x,n=10))
# print("Valeur somme inverse :",exponentielle_somme_inverse(x,n=20))
print("Valeur somme Hörner :",exponentielle_horner(x,n=10))
# print("Valeur Euler :",exponentielle_euler(x,n=35))
print("Valeur astuce :",exponentielle_astuce(x,n=10))

