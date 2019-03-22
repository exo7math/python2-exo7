
##############################
# Calculs en parallèle
##############################


##############################
# Activité 1 - Somme, produit
##############################

from math import *

##############################
## Question 1 ##

def calcule_en_parallele(liste_instructions,N):
    """ Effectue une liste d'instructions données sous la forme de chaîne
    en simulant un calcul en parallèle avec N processeurs.
    Renvoie la liste des résultats, le nb de calculs et le temps des calculs """
    
    liste_resultats = []
    calculs = 0 # work
    temps = 0   # depth

    for instruction in liste_instructions:
        liste_resultats += [eval(instruction)]

    calculs += len(liste_instructions)
    temps += ceil(len(liste_instructions)/N)
        
    return liste_resultats, calculs, temps


# Test
print("--- Machine à calculs parallèles ---")
instructions = ['2+3','6*7','8-2','5+4','4*3','12//3']
print(instructions)
for N in range(1,7):
    print('Nombre de processeurs :',N)
    print(calcule_en_parallele(instructions,N))


##############################
## Question 2 ##

# Addition de deux vecteurs

def addition_vecteurs(v1,v2):
    """ Addition de deux vecteurs en utilisant le calcul en parallèle """
    n = len(v1)
    liste_instructions = []
    for i in range(n):
        instruction = str(v1[i]) + '+' + str(v2[i])
        liste_instructions += [instruction]
    liste_resultats, calculs, temps = calcule_en_parallele(liste_instructions,N)
    v = liste_resultats
    return v, calculs, temps

# Test
print("--- Addition de deux vecteurs ---")
N = 2  # Nombre de processeurs
v1 = [1,2,3,4]
v2 = [10,11,12,13]
v, calculs, temps = addition_vecteurs(v1,v2)
print('v1 =',v1)
print('v2 =',v2)
print('addition =',v)
print('Nombre de processeurs :',N)
print('calculs =',calculs,', temps =',temps)



##############################
## Question 3 ##

# Somme avec 2 processeurs


def somme(v):
    """ Somme des termes de la liste v en utilisant le calcul en parallèle """
    s = 0
    calculs_total = 0
    temps_total = 0

    while len(v)>1:
        k = len(v)//2    
        liste_instructions = []
        for i in range(k):
            instruction = str(v[2*i]) + '+' + str(v[2*i+1])
            liste_instructions += [instruction]
        
        w, calculs, temps = calcule_en_parallele(liste_instructions,N)

        if len(v) % 2 != 0:   # si nombre impair de termes
            w += [v[-1]]

        v = w

        calculs_total += calculs
        temps_total += temps

    resultat = v[0]
    return resultat, calculs_total, temps_total

# Test
print('--- Somme ---')
N = 2  # Nombre de processeurs
v = [1,2,3,4,5,6,7,8]
resultat, calculs, temps = somme(v)
print("Liste :",v)
print("Somme :",resultat)
print('Nombre de processeurs :',N)
print('calculs =',calculs,', temps =',temps)


##############################
## Question 4 ##

def somme_recursive(v):
    """ Somme des termes de la liste v en utilisant une formule récursive 
    et le calcul en parallèle """
    n = len(v)
    if n==0: return 0,0,0
    if n==1: return v[0],0,0
    v_gauche = v[:n//2]
    v_droite = v[n//2:]
    somme_gauche,calculs_gauche,temps_gauche = somme_recursive(v_gauche)
    somme_droite,calculs_droite,temps_droite = somme_recursive(v_droite)
    somme =  somme_gauche + somme_droite
    calculs = calculs_droite + calculs_droite + 1
    temps = max(temps_droite,temps_droite) + 1

    return somme,calculs,temps

# Test
print('--- Somme récursive---')
# On suppose de suffisement de processeurs : N est grand (N>=n//2)
v = [1,2,3,4,5,6,7,8]
resultat, calculs, temps = somme_recursive(v)
print("Liste :",v)
print("Somme :",resultat)
print('calculs =',calculs,', temps =',temps)


##############################
## Question 5 ##

def multiplication_vecteurs(v1,v2):
    """ Multiplication terme à terme de deux vecteurs """

    n = len(v1)
    liste_instructions = []
    for i in range(n):
        instruction = str(v1[i]) + '*' + str(v2[i])
        liste_instructions += [instruction]
    liste_resultats, calculs, temps = calcule_en_parallele(liste_instructions,N)
    v = liste_resultats
    return v, calculs, temps

def produit_scalaire(v1,v2):
    """ Produit scalaire de deux vecteurs """
    v, calculs1, temps1 = multiplication_vecteurs(v1,v2)
    S, calculs2, temps2 = somme(v)
    calculs = calculs1 + calculs2
    temps = temps1 + temps2
    return S, calculs, temps

# Test
print("--- Multiplication de deux vecteurs ---")
N = 8  # Nombre de processeurs
v1 = [1,2,3,4]*100
v2 = [2,3,4,5]*100
v, calculs, temps = multiplication_vecteurs(v1,v2)
print('v1 =',v1)
print('v2 =',v2)
print('multiplication =',v)
print('Nombre de processeurs :',N)
print('calculs =',calculs,', temps =',temps)

print("--- Produit scalaire ---")
produit, calculs, temps = produit_scalaire(v1,v2)
print('produit scalaire =',produit)
print('Nombre de processeurs :',N)
print('calculs =',calculs,', temps =',temps)




# Projet : multiplication de matrices



