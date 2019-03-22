
##############################
# Récursivité
##############################


##############################
# Cours 1a - Factorielle
##############################

##############################
## Question 1 ##

def factorielle_classique(n):
    f = 1
    for k in range(2,n+1):
        f = f*k
    return f

##############################
## Question 2 ##

def factorielle(n):
    if n == 1:      # Cas terminal
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
## Question 3 ##

# Variante avec sortie écran
def factorielle(n):
    if n == 1:      # Cas terminal
        print("Cas terminal. Appel de la fonction avec n =",n)
        f = 1
    else:           # Cas général
        print("Cas général.  Appel de la fonction avec n =",n)
        f = factorielle(n-1)*n
    return f


# Test
print("--- Factorielle (avec étapes à l'écran) ---")
n = 10
print("n =",n)
print("n! = ",factorielle(n))

##############################
# Cours 1b - Puissance de 2 ?
##############################

def est_puissance_de_2(n):
    if n == 1:         # Cas terminal
        return True    # 2^0 = 1 est une puissance de 2

    if n%2 == 0:       # Cas général
        return est_puissance_de_2(n//2)
    else:
        return False   # Cas terminal

# Test
print("--- Test puissance de 2 ---")
n = 1100
print("n =",n)
print("puissance de 2 ?",est_puissance_de_2(n))
n = 1024
print("n =",n)
print("puissance de 2 ?",est_puissance_de_2(n))


##############################
# Cours 1c - Enlever les zéros d'une liste
##############################

def enlever_zero(liste):
    # Cas terminal 
    if len(liste)==0:
        return []

    # Cas général
    if liste[0] == 0:
        nouv_liste = enlever_zero(liste[1:])
    else:
        nouv_liste = [liste[0]] + enlever_zero(liste[1:])
    return nouv_liste

# Test
print("--- Enlever les zéros ---")
liste = [0,1,0,2,0,0,3,0,4,0,0,0]
print("liste =",liste)
print(enlever_zero(liste))

##############################
# Cours 1d - Est palindrome ?
##############################


def est_palindrome(mot):
    n = len(mot)
    
    # Cas terminal 1
    if n <= 1:
        return True

    # Cas terminal 2
    if mot[0] != mot[n-1]:
        return False

    # Cas général
    mot_milieu = mot[1:n-1]
    ok_palind = est_palindrome(mot_milieu)
    
    return ok_palind

# Test
print("--- Palindrome ---")
mot = "RADAR"
print("mot =",mot)
print("Est palindrome ?",est_palindrome(mot))
mot = "ABCXYCBA"
print("mot =",mot)
print("Est palindrome ?",est_palindrome(mot))   
