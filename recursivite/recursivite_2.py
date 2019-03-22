
##############################
# Récursivité
##############################

##############################
# Activité 2 - Fibonacci et Pascal
##############################

##############################
## Question 1 ##

 # Fibonacci
def fibonacci(n):
    """ Terme de rang n de la suite de Fibonacci (fonction doublement récursive) """
    if n==0:
        return 0
    elif n==1:
        return 1

    # if n == 2:
    #     print("Tiens je calcule encore F_2 !")

    # Cas n >= 2
    F_n_1 = fibonacci(n-1)
    F_n_2 = fibonacci(n-2)   
    return F_n_1 + F_n_2


# Test
print("--- Fibonacci ---")
n = 15
print("n =", n)
print("Fibonacci =",fibonacci(n)) 



##############################
## Question 2 ##

# Triangle de Pascal

def binome(k,n):
    """ Coefficient 'k parmi n' du binôme de Newton (fonction doublement récursive) """
    if (k == 0) or (k == n):
        return 1

    else:
        return binome(k-1,n-1) + binome(k,n-1)

# Test
print("--- Binôme de Newton ---")
k, n = 3, 10
print("k, n =", k, n)
print("k parmi n =",binome(k,n)) 



##############################
## Question 3 ##

def afficher_pascal(N):
    """ Affichage dans la console des coeff du binôme de Newton """
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
## Question 4 ##

def afficher_pascal_impair(N):
    """ Marquage des binômes impairs dans le triangle de Pascal """

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
afficher_pascal_impair(10)


##############################
## Question 5 ##

def somme_chiffres(n):
    """ Calcul la somme des chiffres de n (fonction récursive) """
    if n < 10:
        return n

    # Cas général
    unite = n%10
    nn = n//10
    S = unite + somme_chiffres(nn)

    return S

# Test
print("--- Somme des chiffres ---")
n = 1357869
print("n =", n)
print("Somme =",somme_chiffres(n)) 


##############################
## Question 6 ##


def residu_chiffres(n):
    """ Calcul le résidu obtenu en itérant la somme des chiffres 
    jusqu'à plus soif (fonction récursive) """

    if n < 10:
        return n

    # Cas général
    S = somme_chiffres(n)
    r = residu_chiffres(S)

    return r

# Test
print("--- Résidu des chiffres ---")
n = 1357869
print("n =", n)
print("Residu =",residu_chiffres(n)) 



