
##############################
# Récursivité
##############################


##############################
# Activité 4 - Diviser pour régner
##############################


##############################
## Question 1 ##

def minimum(liste): 
    """ Renvoie le minimum d'une liste par fonction récursive """ 
    if len(liste) == 0:
        return None
    if len(liste) == 1:
        M = liste[0]
        return M
    else:
        n = len(liste)
        liste_gauche = liste[:n//2]
        liste_droite = liste[n//2:]

        Mgauche = minimum(liste_gauche)
        Mdroite = minimum(liste_droite)
        if Mgauche < Mdroite:
            return Mgauche
        else:
            return Mdroite

# Test
print("--- Minimum ---")
liste = [7,5,3,9,1,12,13]
print("liste =",liste)
print("min = ",minimum(liste))



##############################
## Question 2 ##

def distance_hamming(liste1,liste2):
    """ Calcule le nb d'endroit où les deux listes diffèrent """
    if len(liste1) == 0:
        return 0
    if len(liste1) == 1:
        if liste1[0] == liste2[0]:
            return 0
        else:
            return 1
    # Cas général

    n = len(liste1)
    liste_gauche1 = liste1[:n//2]
    liste_droite1 = liste1[n//2:]

    liste_gauche2 = liste2[:n//2]
    liste_droite2 = liste2[n//2:]

    Hgauche = distance_hamming(liste_gauche1,liste_gauche2)
    Hdroite = distance_hamming(liste_droite1,liste_droite2)
    H = Hgauche + Hdroite
    return H

# Test
print("--- Distance de Hamming ---")
liste1 = [1,2,3,4,5,6,7]
liste2 = [1,2,0,4,5,0,7]
print("liste1 =",liste1)
print("liste2 =",liste2)

print("Distance =",distance_hamming(liste1,liste2)) 



##############################
## Question 3 ##  

def produit(a,b):
    """ Produit des éléments : a(a+1)(a+2)...(b-2)(b-1) """ 
    if b==a:
        return 1
    if b==a+1:
        return a  

    # Cas général         
    k = b-a
    Pgauche =  produit(a,a+k//2)
    Pdroite = produit(a+k//2,b)
    P = Pgauche*Pdroite
    return P


# Test
print("--- Produit ---")
a, b = 5,10
print("a, b =",a, b)
print("produit = ",produit(a,b)) 


## Rappels ##

def factorielle(n):
    """ Factorielle par formule récursive classique """
    if n == 0:      # Cas terminal
        f = 1
    else:           # Cas général
        f = factorielle(n-1)*n
    return f

print("--- Factorielle ---")
n = 10
print("n =",n)
print("n! = ",produit(1,n+1)) 
print("n! = ",factorielle(n)) 

