
##############################
# Big data
##############################

##############################
# Activité 4 - Problème du secrétaire
##############################

from random import *
from math import *

##############################
## Question 1 ##

def genere_liste(k,N):
    """ Génère une liste de k éléments entre 0 et N. """
    liste = []
    for i in range(k):
        n = randint(0,N)
        liste.append(n)
    return liste

# Test
print("--- Génération d'une liste ---")
N = 100    # Note max
k = 20     # Nb de secrétaires
liste_aleatoire = genere_liste(k,N)
print("k, N :",k,N)
print("Liste : ",liste_aleatoire)  


##############################
## Question 2 ##

def choix_secretaire(liste,p):
    k = len(liste)                          # longueur de la liste
    j = min(ceil(p/100*k),100)     # longueur de l'échantillon
    # print("j",j)
    Me = max(liste[:j])                     # le meilleur score dans l'échantillon
    # print("Me",Me)
    for i in range(j,k):                    # on cherche un meilleur parmi les suivants
        if liste[i] >= Me:
            return liste[i]
    return None                             # on n'a pas trouvé, on ne prend personne


# Test
print("--- Choix d'un secrétaire ---")
N = 100    # max note
k = 100    # nb de secrétaire
liste_aleatoire = genere_liste(k,N)
pourcentage = 25
MM = choix_secretaire(liste_aleatoire,pourcentage)
M = max(liste_aleatoire)  # le meilleur score d'un sécretaire
print("k, N:",k, N)
# print("Liste : ",liste_aleatoire)  
print("Meilleur valait :",M)
print("Choix vaut :",MM)

# Test
print("--- Choix d'un secrétaire : exemple cours ---")
liste = [2,5,3,4,1,6,4,5,8,3]
p = 25
MM = choix_secretaire(liste,p)
M = max(liste)  # le meilleur score d'un sécretaire
# print("Liste : ",liste)  
print("Meilleur valait :",M)
print("Choix vaut :",MM)

##############################
## Question 3 ##

def meilleurs_secretaires(k,N,p,nb_tirages):
    nb_meilleurs = 0
    for i in range(nb_tirages):
        liste = genere_liste(k,N)
        M = max(liste)  # le meilleur score d'un sécretaire    
        MM = choix_secretaire(liste,p)
        if M == MM:
            nb_meilleurs += 1

    return nb_meilleurs
# Test
print("--- Nb de fois où le choix d'un secrétaire est le meilleur ---")
N = 100
k = 100
pourcentage = 25
nb_tirages = 1000
nb_best = meilleurs_secretaires(k,N,pourcentage,nb_tirages)
print("k, N:",k, N)
print("Pourcentage : ",pourcentage)
print("Nb de meilleurs choisi : ",nb_best, "soit ",'{0:.2f}'.format(nb_best/nb_tirages*100),"%")  



##############################
## Question 4 ##

# Variante liste des erreurs (avec les mêmes tirages pour tous)
def liste_meilleurs_secretaires(k,N,nb_tirages):
    liste_nb_meilleurs = [0 for i in range(1,100)]
    for i in range(nb_tirages):
        liste = genere_liste(k,N)
        M = max(liste)   # le meilleur score d'un sécretaire    
        for p in range(1,100):
            MM = choix_secretaire(liste,p)
            if M == MM:           
                liste_nb_meilleurs[p-1] += 1   

    return liste_nb_meilleurs

# Test
print("--- Liste des erreurs choix d'un secrétaire ---")
N = 100
k = 100

liste_best = liste_meilleurs_secretaires(k,N,5000)  # Il faut au moins 1000 tirages pour obtenir 37%
print("k, N:",k, N)
print("Liste des nb de bons choix : ",liste_best)     
maximum = max(liste_best)
print("Meilleure stratégie : pourcentage = ",liste_best.index(maximum))


