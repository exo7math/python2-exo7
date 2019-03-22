
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
    """ Calcul la magnitude d'un seisme en fonction de l'energie """
    E0 = 1.6*10**-5
    M = 2/3 * log(E/E0,10) - 3.2
    return M


# Test
print("--- Échelle de Richter ---")
# Vérification -> M ~ 4
E1 = 10**6
print("Energie E =",E1,"magnitude M = ",magnitude(E1))


##############################
## Question 2 ##

# Energie = puissance de 10, afficher magnitude jusqu'à avoir M>9
print("--- Quelques calculs de magnitude ---")
for i in range(6,15):
    E = 10**i
    print("E = 10^",i,"  Energie E =",E,"  magnitude M = ",magnitude(E))



##############################
## Question 3 ##

# Trouver E tel que M = 7 (tatonnment, balyage, calcul):
# Tâtonnement + balayage
print("--- Balayage des énergie pour obtenir un magnitude 7 ---")

for E in range(10**10,10**11,10**9):
    print("Energie E =",E,"  magnitude M = ",magnitude(E))

print("Vérification")
E = 3.2 * 10*10
print("Energie E =",E,"  magnitude M = ",magnitude(E))

##############################
## Question 4 ##

print("--- Magnitude augmenté de 1 ----")
# Montrer que si E2 = 1000 E1 alors M2 = M1 + 2
E1 = 10**7  # n'importe quelle valeur
E2 = 1000 * E1
print("Energie E1 =",E1,"  magnitude M1 = ",magnitude(E1))
print("Energie E2 =",E2,"  magnitude M2 = ",magnitude(E2))

# Montrer que si E2 = sqrt(1000) E1 alors M2 = M1 + 1
# Réponse k = sqrt(1000) ~ 32 
E1 = 10*7  # n'importe quelle valeur
E2 = sqrt(1000) * E1   # sqrt(1000) ~ 32
print("Energie E1 =",E1,"  magnitude M1 = ",magnitude(E1))
print("Energie E2 =",E2,"  magnitude M2 = ",magnitude(E2))

