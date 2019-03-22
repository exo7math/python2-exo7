
##############################
# Complexes I
##############################

##############################
# Activité 4 - Equation du second degré
##############################

from math import *

##############################
## Question 1 ##

def solution_trinome(a,b,c):
    """ Solutions de ax^2 + bx + c = 0 avec a,b,c réels """

    Delta = b**2 - 4*a*c

    if Delta == 0:
        sol = [-b/(2*a),-b/(2*a)]

    if Delta > 0:
        d = sqrt(Delta)
        sol = [(-b-d)/(2*a), (-b+d)/(2*a)]

    if Delta < 0:
        d = 1j*sqrt(-Delta)
        sol = [(-b-d)/(2*a), (-b+d)/(2*a)]

    return sol

# Test
print("--- Solution d'une équation de degré 2 ---")
sol = solution_trinome(1,-2,1)  # x^2 - 2x + 1, Delta = 0
print("Solution :", sol)
sol = solution_trinome(1,1,-1)  # x^2 + x - 1, Delta > 0
print("Solution :", sol)
sol = solution_trinome(1,1,1)  # x^2 + x + 1, Delta < 0
print("Solution :", sol)


##############################
## Question 2 ##

def solution_somme_produit(S,P):
    return solution_trinome(1,-S,P)

# Test
print("--- Solution somme/produit ---")
x,y = solution_somme_produit(10,20)  # S = 10, P = 20
print("Solution :", x,y)
print("Vérification :", x+y, x*y)


##############################
## Question 3 ##

def solution_bicarre(a,b,c):
    """ Solutions de ax^4 + bx^2 + c = 0 avec a,b,c réels et Delta >= 0 """

    Delta = b**2 - 4*a*c

    if Delta < 0:
        print("Discriminant négatif. Je ne sais pas faire.")
        return None

    # On récupère les solution de aX^2 + bX + c
    X1, X2 = solution_trinome(a,b,c)

    sol = []
    for X in [X1,X2]:

        if X >= 0: 
            # Si Xi >= 0 on prend les racines carrées
            x1 = +sqrt(X)
            x2 = -sqrt(X)
            sol = sol + [x1,x2]

        if X < 0:
            # Si Xi < 0 on prend les racines carrées  +/- i*racine(-Xi)
            x1 = +1j*sqrt(-X)
            x2 = -1j*sqrt(-X)
            sol = sol + [x1,x2]

    return sol


# Test
print("--- Solution bicarré ---")
sol = solution_bicarre(1,-2,-3)
print(sol)

