
##############################
# Récursivité
##############################

from math import *

##############################
# Cours 1a - Factorielle
##############################

##############################
## Question 1 ##

def factorielle_classique(n):
    f = 1
    for k in range(1,n+1):
        f = f*k
    return f

##############################
## Question 2 ##

def factorielle(n):
    if n == 0:      # Cas terminal
        f = 1
    else:           # Cas général
        f = factorielle(n-1)*n
    return f

# Test
print("--- Factorielle ---")
n = 100
print("n =",n)
print("n! = ",factorielle_classique(n))
print("n! = ",factorielle(n))


##############################
# Cours 1b - Puissance de 2 ?
##############################

def est_puissance_de_2(n):
    if n == 1:
        return True    # 2^0 = 1 est une puissance de 2

    # Cas général
    if n%2 == 0:
        return est_puissance_de_2(n//2)
    else:
        return False

# Test
print("--- Test puissance de 2 ---")
n = 1100
print("n =",n)
print("puissance de 2 ?",est_puissance_de_2(n))
n = 1024
print("n =",n)
print("puissance de 2 ?",est_puissance_de_2(n))



##############################
# Activité 1 - Faciles
##############################

##############################
## Question 1 ##

def somme_carres_classique(n):
    S = 1
    for k in range(1,n+1):
        S = S + k**2
    return S


def somme_carres(n):
    if n==0:
        S = 0
    else:
        S = somme_carres(n-1) + n**2
    return S

# Test
print("--- Somme des carrés ---")
n = 100
print("n =",n)
print("S = ",somme_carres_classique(n))
print("S = ",somme_carres(n))


##############################
## Question 2 ##

def inverser_classique(liste):
    pass


def inverser(liste):
    if len(liste) <= 1:
        return liste
    else:
        fin_liste = liste[1:]
        nouv_liste = inverser(fin_liste) + [liste[0]]
        return nouv_liste

# Test
print("--- Inverser une liste ---")
liste = [1,2,3,4,5]
print("liste =",liste)
print("inverse = ",inverser_classique(liste))
# print("inverse = ",inverser(liste))  


##############################
## Question 3 ##

def maximum_classique(liste):
    M = liste[0]
    for x in liste:
        if x>= M:
            M = x

    return M


def maximum(liste):
    if len(liste) == 1:
        M = liste[0]
        return M
    else:
        M1 = liste[0]
        sous_liste = liste[1:]
        M2 = maximum(sous_liste)
        if M1 > M2:
            return M1
        else:
            return M2

# Test
print("--- Maximum ---")
liste = [7,5,3,9,1]
print("liste =",liste)
print("max = ",maximum_classique(liste))
print("max = ",maximum(liste))


##############################
## Question 4 ##

def binaire(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'

    # Cas général     
    if n%2 == 0:
        ecriture = binaire(n//2) + '0'
    else:
        ecriture = binaire(n//2) + '1'

    return ecriture

# Test
print("--- Binaire ---")
n = 23
print("n =",n)
print("binaire = ",binaire(n))
print("Python = ",bin(n))



##############################
## Question 5 ##

# A virer ??

def est_palindrome_classique(mot):
    ok_palind = True  # drapeau 
    n = len(mot)
    for i in range(n//2):
        if mot[i] != mot[n-i-1]:
            ok_palind = False

    return ok_palind


def est_palindrome(mot):
    if len(mot) <= 1:
        return True
    else:
        if mot[0] == mot[-1]:
            ok_debut_fin = True
        else:
            ok_debut_fin = False

        mot_milieu = mot[1:-1]
        ok_mileu = est_palindrome(mot_milieu)

        ok_palind = ok_debut_fin and ok_mileu

        return ok_palind

# Test
print("--- Palindrome ---")
mot = "RADAR"
print("mot =",mot)
print("Est palindrome ?",est_palindrome_classique(mot))
print("Est palindrome ?",est_palindrome(mot))
mot = "ABCXYCBA"
print("mot =",mot)
print("Est palindrome ?",est_palindrome_classique(mot))
print("Est palindrome ?",est_palindrome(mot))       



##############################
# Activité 2 - Double appel
##############################


##############################
## Question 1 ##

 # Fibonacci
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1

    # Cas n >= 2
    F_n_1 = fibonacci(n-1)
    F_n_2 = fibonacci(n-2)   
    return F_n_1 + F_n_2


# Test
print("--- Fibonacci ---")
n = 7
print("n =", n)
print("Fibonacci =",fibonacci(n)) 



##############################
## Question 2a ##

# Triangle de Pascal

def binome(k,n):

    if k == 0:
        return 1

    elif k > n:
        return 0

    else:
        return binome(k-1,n-1) + binome(k,n-1)

# Test
print("--- Binôme de Newton ---")
k, n = 3, 4
print("k, n =", k, n)
print("k parmi n =",binome(k,n)) 



##############################
## Question 2b ##

def afficher_pascal(N):
    for n in range(N+1):
        for k in range(n+1):
            C = binome(k,n)
            print(C,end=" ")
        print()
         
    return

# Test
print("--- Triangle de Pascal ---")
afficher_pascal(10)


##############################
## Question 2c ##

def afficher_pascal_pair(N):
    for n in range(N+1):
        for k in range(n+1):
            C = binome(k,n)
            if C%2 == 0:
                print(" ",end="")
            else:
                print("X",end="")
        print()
         
    return

# Test
print("--- Triangle de Pascal impair ---")
afficher_pascal_pair(10)



##############################
# Activité 3 - Parcourt d'arbre
##############################

##############################
## Question 1 ##

def pile_ou_face(n):
    if n == 0:
        return [""]

    # Cas général
    sous_arbre = pile_ou_face(n-1)
    arbre_gauche = [chaine + 'P' for chaine in sous_arbre]
    arbre_droite = [chaine + 'F' for chaine in sous_arbre]
    arbre = arbre_gauche + arbre_droite

    return arbre

# Test
print("--- Pile ou face ---")
print(pile_ou_face(4))


##############################
## Question 2 ##

def une_seule_liste(mes_listes):
    liste = []
    for l in mes_listes:
        if isinstance(l, list):
            liste = liste + une_seule_liste(l)
        else:
            liste = liste + [l]     # Cas terminal

    return liste

# Test
print("--- Une seule liste ---")
mes_listes = [[1,2],3,[9,8,7,[6,5],[4,3]],2,[[1],[1]],0]
print(mes_listes)
print(une_seule_liste(mes_listes))


##############################
## Question 3 ##

def somme_chiffres(n):
    if n < 10:
        return n

    # Cas général
    unite = n%10
    nn = n//10
    S = unite + somme_chiffres(nn)

    return S

# Test
print("--- Somme des chiffres ---")
n = 13579
print("n =", n)
print("Somme =",somme_chiffres(n)) 


##############################
## Question 4 ##


def residu_chiffres(n):
    if n < 10:
        return n

    # Cas général
    S = somme_chiffres(n)
    R = residu_chiffres(S)

    return R

# Test
print("--- Résidu des chiffres ---")
n = 13579
print("n =", n)
print("Residu =",residu_chiffres(n)) 


##############################
# Cours 2 - Binary splitting
##############################        


def somme(liste):
    if len(liste) == 0:
        return 0
    if len(liste) == 1:
        return liste[0]
    else:
        n = len(liste)
        liste_gauche = liste[:n//2]
        liste_droite = liste[n//2:]

        Sgauche = somme(liste_gauche)
        Sdroite = somme(liste_droite)
        S = Sgauche + Sdroite
        return S

# Test
print("--- Somme ---")
liste = [7,5,3,9,1,12]
print("liste =",liste)
print("somme = ",somme(liste)) 



##############################
# Activité 4 - Binary splitting
##############################


##############################
## Question 1 ##

def minimum(liste):  
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

# produit(a,b) = a(a+1)(a+2)...(b-2)(b-1)
def produit(a,b):
    if b==a:
        return 1
    if b==a+1:
        return a  

    # Cas général         
    n = b-a
    Pgauche =  produit(a,a+n//2)
    Pdroite = produit(a+n//2,b)
    P = Pgauche*Pdroite
    return P


# Test
print("--- Produit ---")
a, b = 5,10
print("a, b =",a, b)
print("produit = ",produit(a,b)) 

print("--- Factorielle ---")
n = 10
print("n =",n)
print("n! = ",produit(1,n+1)) 
print("n! = ",factorielle(n)) 



##############################
# Activité 5 - Dérangements
##############################


##############################
## Question 1 ##

def derangement_classique(n):
    d = 1
    for k in range(1,n+1):
        if k%2 == 0:
            e = 1
        else:
            e = -1
        d = d*k + e
    return d

##############################
## Question 2 ##

def derangement(n):
    if n==0:
        d = 1
    else:
        if n%2 == 0:
            e = 1
        else:
            e = -1        
        d = derangement(n-1)*n + e
    return d

# Test
print("--- Dérangement ---")
n = 100
print("n =",n)
print("n! = ",derangement_classique(n))
print("n! = ",derangement(n))

##############################
## Question 3 ##


def quotient(n):
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

# Idées 2 : permutation de n objets, puis recursivité avec n-1 (autres) objets



def toutes_permutations(liste):
    n = len(liste)
    if n == 1:
        permutations = [liste]
    else:
        permutations = []
        for i in range(n):
            element = liste[i]
            sous_liste =  liste[:i] + liste[i+1:]

            for permut in toutes_permutations(sous_liste):
                nouv_perm = [element] + permut
                permutations += [nouv_perm]
    return permutations

     
# Test
print("--- Toutes les permutations NEW ---")
liste = [1,2,3,4]
permutations = toutes_permutations(liste)
n = len(liste)
print(liste)
print(permutations)
print("Total =",len(permutations))
print("n! =",factorielle(n))

##############################
## Question 6 ##

def liste_derangements(n):
    derangements = []
    liste =  list(range(n))
    for permutation in toutes_permutations(liste):
        if est_derangement(permutation):
            derangements += [permutation]
    return derangements

# Test
print("--- Tous les dérangements ---")
n = 4
print("n =",n)
liste = liste_derangements(n)
print(liste)
print("Total =",len(liste))
print("d(n) =",derangement(n))


##############################
# Activité 6 - Tortue récursive 
##############################


##############################
## Question 1 ##

from turtle import *


# Le faire sans le paramètre l 
# mais avec longueur = cst fixée avant
def koch(l,n):
    if n==0:
        forward(l) 
        return

    koch(l/3,n-1)
    left(60)
    koch(l/3,n-1)
    right(120)
    koch(l/3,n-1)
    left(60)
    koch(l/3,n-1)
    
    return

# Test
# speed('fastest')
# up()
# goto(-200,-200)
# down()
# koch(600,5)
# exitonclick()


##############################
## Question 1 ##


def arbre(l,n):
    if n==0:
        return

    P = position()
    setheading(-140)    
    forward(l)
    arbre(l/2,n-1)
    goto(P)
    setheading(-40)    
    forward(l)
    arbre(l/2,n-1)
    goto(P)

    return

# Test
# speed('fastest')
# up()
# goto(0,200)
# down()
# arbre(200,6)
# exitonclick()



##############################
## Question 1 ##


def triangle(l,n):
    if n==0:
        return

    for __ in range(3):
        triangle(l/2,n-1)    
        forward(l)
        left(120)

    return

# Test
# speed('fastest')
# up()
# goto(-200,-200)
# down()
# triangle(400,6)
# exitonclick()


##############################
## Question 1 ##

# Depuis la doc du module 'turtle'
def hilbert(angle,n):
    if n == 0:
        return

    right(angle)
    hilbert(-angle,n-1)
    forward(longueur)
    left(angle)
    hilbert(angle,n-1)
    forward(longueur)
    hilbert(angle,n-1)
    left(angle)
    forward(longueur)
    hilbert(-angle,n-1)
    right(angle)

    return

# Test
# speed('fastest')
# up()
# goto(-200,200)
# down()
# longueur = 20
# hilbert(90,4)
# exitonclick()


##############################
## Question 1 ##

def quart_cercle(pas):
    for i in range(45):
        left(2)
        forward(pas)

# Test
# quart_cercle(1)
# exitonclick()

from random import *


def fractale_cercle(l,n):
    if n == 0:
        return

    for __ in range(4):    
        quart_cercle(l)
        hasard = randint(0,3)

        if hasard <= 2:
            fractale_cercle(l/3,n-1)

    return


# Test
# up()
# goto(0,-300)
# down()
# speed('fastest')
# width(2)
# l = 10
# fractale_cercle(l,4)
# exitonclick()    

