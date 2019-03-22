
##############################
# Récursivité
##############################

##############################
# Activité 1 - Pour bien commencer...
##############################

##############################
## Question 1 ##

def somme_carres_classique(n):
    """ Somme des carrés de 1 à n """
    S = 1
    for k in range(1,n+1):
        S = S + k**2
    return S


def somme_carres(n):
    """ Somme des carrés de 1 à n (fonction récursive) """
    if n==1:
        S = 1
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
    """ Inverser l'ordre des éléments d'une liste (fonction récursive) """
    if len(liste) <= 1:
        return liste
    else:
        fin_liste = liste[1:]
        fin_liste_inverse = inverser(fin_liste)
        nouv_liste =  fin_liste_inverse + [liste[0]]
        return nouv_liste

# Test
print("--- Inverser une liste ---")
liste = [1,2,3,4,5]
print("liste =",liste)
print("inverse = ",inverser(liste))
# print("inverse = ",inverser_classique(liste))  


##############################
## Question 3 ##

def maximum_classique(liste):
    """ Maximum des éléments d'une liste """
    M = liste[0]
    for x in liste:
        if x>= M:
            M = x

    return M


def maximum(liste):
    """ Maximum des éléments d'une liste (fonction récursive) """
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
    """ Ecriture binaire de l'netier n (fonction récursive) """

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


def est_palindrome_classique(mot):
    """ Tese si un mot est un palindrome 
    (c-à-d se lit dans les deux sens) """
    ok_palind = True  # drapeau 
    n = len(mot)
    for i in range(n//2):
        if mot[i] != mot[n-i-1]:
            ok_palind = False

    return ok_palind


def est_palindrome(mot):
    """ Tese si un mot est un palindrome 
    (c-à-d se lit dans les deux sens) (fonction récursive) """

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

