
##############################
# Logarithme
##############################

##############################
# Activité 4 - Le logarithme népérien
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
    """ Simule une table x -> ln(x) """
    l = floor(log(x)*10**N)/10**N
    return l

def table_exp(x,N):
    """ Simule une table x -> exp(x) autrement dit ln(x) -> x """
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
    """ Multiplication par table des logarithmes """
    la = table_ln(a,N)
    lb = table_ln(b,N)
    lc = la + lb
    c = table_exp(lc,N)
    return c
# Test
print("--- Produit par tables des logarithme ---")
N = 7
print("Nombre de chiffres après la virgule de la table N=",N)
a = 98.765
b = 43.201
print("a =",a)
print("b =",b)
print("par table   : c =",multiplication(a,b,N))
print("vérfication : c =",a*b)

