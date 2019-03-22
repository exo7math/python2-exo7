
##############################
# Récursivité
##############################

from math import *


##############################
# Activité 5 - Dérangements
##############################


##############################
## Question 1 ##

def derangement_classique(n):
    """ Formule dérangement d_n par formule classique """
    d = 1
    for k in range(1,n+1):
        if k%2 == 0:
            epsilon = 1
        else:
            epsilon = -1
        d = d*k + epsilon
    return d

##############################
## Question 2 ##

def derangement(n):
    """ Formule dérangement d_n par formule récursive """    
    if n==0:
        d = 1
    else:
        if n%2 == 0:
            epsilon = 1
        else:
            epsilon = -1        
        d = derangement(n-1)*n + epsilon
    return d

# Test
print("--- Dérangement ---")
n = 100
print("n =",n)
print("n! = ",derangement_classique(n))
print("n! = ",derangement(n))


##############################
## Rappels ##

def factorielle(n):
    """ Factorielle par formule récursive classique """
    if n == 0:      # Cas terminal
        f = 1
    else:           # Cas général
        f = factorielle(n-1)*n
    return f


##############################
## Question 3 ##

def quotient(n):
    """ Proportion des dérangements parmi les permutations """
    return derangement(n)/factorielle(n)

# Test
print("--- Limite ---")
n = 10
print("n =",n)
print("d(n)/n! = ",quotient(n))
print("1/e = ",1/exp(1))


##############################
## Question 4 ##

def est_derangement(permutation):
    """ Est-ce que la permutation donnée est un dérangement ? """
    n = len(permutation)
    der = True
    for i in range(n):
        if permutation[i] == i:
            der = False
    return der

# Test
print("--- Etre ou ne pas être un dérangement ---")
permutation = [2,1,0,3]
print("permutation =",permutation)
print("dérangement ? ",est_derangement(permutation))

permutation = [3,2,0,1]
print("permutation =",permutation)
print("dérangement ? ",est_derangement(permutation))

##############################
## Question 5 ##

# Idée 1 : liste des permutations par ajout de l'élément n à toutes les permutations de {0,...,n-1} 
# avantage : un seule paramètre n

def toutes_permutations(n):
    """ Renvoie la liste de toutes les permutations de n éléments """
    if n == 1:
        return [[0]]    # ou bien n == 0 il faut [[]]

    old_liste = toutes_permutations(n-1) 
    new_liste = []
    for old_permut in old_liste:
        for i in range(n):
            new_permut = old_permut[:i] + [n-1] + old_permut[i:]   
            new_liste += [new_permut] 
    return new_liste

# Test
print("--- Toutes les permutations  ---")
n = 3
permutations = toutes_permutations(n)
print("n =",n)
print(permutations)
print("Total =",len(permutations))
print("n! =",factorielle(n))


# Idées 2 : permutation de n objets, puis recursivité avec n-1 (autres) objets

def toutes_permutations_bis(liste):
    """ Renvoie la liste de toutes les permutations de n éléments """

    n = len(liste)
    if n == 1:
        permutations = [liste]
    else:
        permutations = []
        for i in range(n):
            element = liste[i]
            sous_liste =  liste[:i] + liste[i+1:]

            for permut in toutes_permutations_bis(sous_liste):
                nouv_perm = [element] + permut
                permutations += [nouv_perm]
    return permutations

     
# Test
print("--- Toutes les permutations (bis) ---")
liste = [0,1,2,3]
permutations = toutes_permutations_bis(liste)
n = len(liste)
print(liste)
print(permutations)
print("Total =",len(permutations))
print("n! =",factorielle(n))

##############################
## Question 6 ##

def tous_derangements(n):
    """ Renvoie la liste de toutes les dérangements de n éléments """
    derangements = []
    for permutation in toutes_permutations(n):
        if est_derangement(permutation):
            derangements += [permutation]
    return derangements

# Test
print("--- Tous les dérangements ---")
n = 3
print("n =",n)
liste = tous_derangements(n)
print(liste)
print("Total =",len(liste))
print("d(n) =",derangement(n))
