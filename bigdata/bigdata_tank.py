
##############################
# Big data
##############################


from random import *


##############################
# Activité 3 - Tank
##############################


##############################
## Question 1 ##

def formule_tanks(echantillon):
    """ Applique la formule des tanks qui estime ... """
    k = len(echantillon)
    m = max(echantillon)
    N = m + m/k - 1
    return N

# Test
print("--- Formule des tanks ---")
echantillon = [143,77,198,32]
N = formule_tanks(echantillon)
print("Echantillon :",echantillon)
print("Nombre de tanks total estimé : ",round(N))

##############################
## Question 2 ##

def double_moyenne(echantillon):
    """ Applique la formule ... """
    k = len(echantillon)
    S = sum(echantillon)
    N = 2 * S/k
    return N

# Test
print("--- Formule des tanks ---")
echantillon = [143,77,198,32]
N1 = formule_tanks(echantillon)
N2 = double_moyenne(echantillon)
print("Echantillon :",echantillon)
print("Nombre de tanks total estimé, par la formule des tanks : ",round(N1))
print("Nombre de tanks total estimé, par le double de la moyenne : ",round(N2))


##############################
## Question 3 ##

def tirage_sans_remise(N,k):
    tirage = []
    while len(tirage) < k:
        n = randint(0,N)
        if n not in tirage:
            tirage.append(n)
    return tirage

# Test
print("--- Tirage sans remise ---")
N = 100
k = 4
tirage = tirage_sans_remise(N,k)
print("N, k :",N,k)
print("Tirage : ",tirage)   


##############################
## Question 4 ##

def erreurs(N,k,nb_tirages=1000):
    erreur_tanks = 0
    erreur_double = 0
    for i in range(nb_tirages):
        echantillon = tirage_sans_remise(N,k)
        N1 = formule_tanks(echantillon)
        N2 = double_moyenne(echantillon)
        # print(N1,N2)
        erreur_tanks += abs(N-N1)
        erreur_double += abs(N-N2)
        moyenne_erreur_tank = erreur_tanks/nb_tirages
        moyenne_erreur_double = erreur_double/nb_tirages
    return moyenne_erreur_tank, moyenne_erreur_double

# Test
print("--- Erreurs formules des tanks/double de la moyenne ---")
N = 1000
k = 20
E1,E2 = erreurs(N,k)
print("N, k :",N,k)
print("Erreur moyenne formule des tanks :",E1)  
print("Erreurs moyenne formule double de la moyenne :",E2) 



