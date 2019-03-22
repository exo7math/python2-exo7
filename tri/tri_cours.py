
##############################
# Tri
##############################


##############################
# Cours - Python
##############################

liste = [5,6,1,8,10]
liste = ["BATEAU", "ABRIS", "ARBRE", "BARBE"]

nouv_liste = sorted(liste)
print(nouv_liste)

# liste.sort()  # Modifie la liste en place
# print(liste)

# Renversé
nouv_liste = list(reversed(sorted(liste)))
print(nouv_liste)

print(liste)
# liste.reverse()  # Modifie la liste en place
print(liste)

# Tri inverse
nouv_liste = sorted(liste, reverse = True)
print(nouv_liste)


##############################
# Cours - Python
##############################

from math import *

def complexite_mutliplication(n):
    print("n =",n)
    print("Multiplication classique :",n**2)
    print("Multiplication classique :",n**log(3,2))
    print("Multiplication classique :",n*log(n)*log(log(n))) 
    return

for n in [10,100,1000]:
    complexite_mutliplication(n)

def complexite_recherche(n):
    print("n =",n)
    print("Recherche classique :",n)
    print("Recherche classique :",log(n,2))
    return

for n in [10**3,10**6,10**9]:
    complexite_recherche(n)


def complexite_voyageur(n):
    print("n =",n)
    print("Voyageur :",float(n**2 * 2**n))
    return

for n in [10,100,1000]:
    complexite_voyageur(n)