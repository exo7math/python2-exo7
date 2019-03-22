
##############################
# Logarithme
##############################


##############################
# Activité 5 - Le logarithme en base 2 (ou pas)
##############################

from math import *

##############################
## Question 1 ##


def logarithme_entier(x):  # x >= 1
    """ Logarithme décimal entier de x """
    l = 0
    while 10**l <= x:
        l = l + 1
    return l-1

# Test
print("--- Partie entière du logarithme : base 10 ---")
for x in range(1,11):
    print("x =",x)
    print("mon calcul",logarithme_entier(x))
    print("Python",log(x,10))


##############################
## Question 2 ##

def logarithme_entier_2(n):
    """ Logarithme entier en base 2 """
    l = 0
    while 2**l <= n:
        l = l + 1
    return l-1

 # Test
print("--- Partie entière du logarithme : base 2 ---")
for x in range(1,20):
    print("x =",x)
    print("mon calcul",logarithme_entier_2(x))
    print("Python",log(x,2))



##############################
## Question 3 ##

def dichotomie(n):
    """ Simule la dichotomie en compte le nombre d'étape maximal """
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
    print("log2 entier",logarithme_entier_2(n))  # valable uniquement si n puissance de 2 (sinon faire +1)


##############################
## Question 4 ##

def logarithme_base(x,b):
    """ Logarithme en base b qcq à partir de ln """
    return log(x)/log(b)

# Test
print("--- Logarithme en base quelconque ---")
x = 555
b = 10
print("x =",x)
print("Moi log(x,b)",logarithme_base(x,b))   
print("Python log(x,b)",log(x,b))



##############################
## Question 5 ##

def nombre_de_chiffres(n,b):
    """ Nombre de chiffres d'un entier n dans son écriture en base b """
    return floor(logarithme_base(n,b))+1
# Test
print("--- Nombre de chiffres ---")
n = 123
print("base 10, n =",n)
print("nb chiffres",nombre_de_chiffres(n,10))
print("base 2, n =",bin(n))
print("nb chiffres",nombre_de_chiffres(n,2))
print("base 16, n =",hex(n))
print("nb chiffres",nombre_de_chiffres(n,16))


