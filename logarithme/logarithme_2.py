
##############################
# Logarithme
##############################

from math import *

##############################
# Activité 2 - Le logarithme décimal - Décibels
##############################

##############################
## Question 1 ##

def decibel(P):
    """ Calcule l nombre de décibels d'un son en fonction d'une puissance """
    P0 = 2 * 10**-5
    D = 20 * log(P/P0,10)
    return D

# Test
print("--- Décibels ---")
# Vérification -> D ~ 94
P = 1
print("Pression P =",P,"décibels D = ",decibel(P))


##############################
## Question 2 ##

# compléter tableau

def inverse_decibel(D):
    """ Calcule la puissance en fonction du nombre de décibels """
    P0 = 2 * 10**-5
    P = P0 * 10**(D/20)
    return P

# Test
print("--- Inverse décibels ---")
D = 94
print("Pression P =",inverse_decibel(D),"décibels D = ",D)

# Moteur d'avion à réaction (à 1 mètre) P = 632, D = 150
# Marteau-piqueur (à 1 mètre) P = 2, 
# Niveau de dommage à l'oreille P > 0.355, D > 85
# Niveau de gêne D > 70
# Conversation (à 1 mètre) P = 0.002 à 0.02 (D = 40 à 60)
# Chambre calme (son environnant)  D = 10 à 20
# Seuil de l'audition à 1kHz (à l'oreille)   P = 2*10**-5
# Chambre anéchoïque   D = -10 dB

print("--- Tableau ----")
# P -> D
for P in [632,2,0.355,0.02,0.002,2*10**-5]:
    print("Pression P =",P," - Décibels D = ",decibel(P))
    
# D -> P 
for D in [150,85,60,40,-10]:
    print("Pression P =",inverse_decibel(D)," - Décibels D = ",D)

