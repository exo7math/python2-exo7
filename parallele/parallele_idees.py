
##############################
# Calcul parallèle
##############################


##############################
# Activité 1 - Somme, produit
##############################

from math import *
# from time import *
# from random import *



def calcule_en_parallele(liste_instructions,N):
    # shuffle(liste_instructions)   # Mélange les instructions
    
    liste_resultats = []
    calculs = 0 # work
    temps = 0 # depth

    for instruction in liste_instructions:
        liste_resultats += [eval(instruction)]

    calculs += len(liste_instructions)
    temps += ceil(len(liste_instructions)/N)
        
    return liste_resultats, calculs, temps


# Exemple 1 : somme de deux vecteurs
N = 4  # Nombre de processeurs

v1 = [1,2,3,4]
v2 = [10,11,12,13]


# A la main
def addition(v1,v2,i):
    return v1[i] + v2[i]


# à modifier comme dans somme, avec eval et str pour éviter l'appel à addition
def addition_vecteur(v1,v2):
    liste_instructions = ['addition(v1,v2,0)','addition(v1,v2,1)','addition(v1,v2,2)','addition(v1,v2,3)']
    liste_resultats, calculs, temps = calcule_en_parallele(liste_instructions,N)
    v = liste_resultats
    return v, calculs, temps

v, calculs, temps = addition_vecteur(v1,v2)
print(v)
print('calculs =',calculs,', temps =',temps)


# Exemple 2 : multiplication terme à terme

def multiplication():
    pass



# Exemple 3 : somme avec 2 processeurs


def somme(v):
    s = 0
    calculs_total = 0
    temps_total = 0

    while len(v)>1:
        n = len(v)//2    
        liste_instructions = []
        for i in range(n):
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

print('Somme')
v = [1,2,3,4,5,6]
print(somme(v))


# Exemple 3 bis : somme récursif

def somme_recursif(v):
    n = len(v)
    if n==0: return 0,0,0
    if n==1: return v[0],0,0
    v_pair = [v[i] for i in range(0,n,2)]
    v_impair = [v[i] for i in range(1,n,2)]
    somme_paire,calculs_pair,temps_pair = somme_recursif(v_pair)
    somme_impaire,calculs_impair,temps_impair = somme_recursif(v_impair)
    somme =  somme_paire + somme_impaire
    calculs = calculs_pair + calculs_impair + 1
    temps = max(temps_pair,temps_impair) + 1

    return somme,calculs,temps

print('Somme récursive')
v = [1,2,3,4,5,6]
print(somme_recursif(v))  # vérifier temps et calculs !!!


# Exemple 4 : produit scalaire

# Exemple 5 : multiplication de matrices






##############################
# Activité 2 - Doublons
##############################


# Première méthode par indexation

# Liste d'entiers de 0 à 99
liste = [59,72,8,37,37,8,21,22,37,59]

def enlever_tous_doublons(liste):
    nouv_liste = []  # future liste sans doublons
    table = [0]*100  # liste de 100 zéros
    for x in liste:
        if table[x] == 0:  # si élément x pas déjà retenu
            table[x] = 1   # on le note
            nouv_liste += [x]  # et on le rajoute 

    return nouv_liste


# Test
print(enlever_tous_doublons(liste))



# Seconde méthode : table de hachage

ALPHBABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(ALPHBABET)

def hachage(mot,p):
    hach = 0
    i = 0
    for c in mot:
        k = ALPHBABET.index(c)
        hach = (hach + k*26**i) % p  # mieux avec pow(26,i,p)
        i = i + 1
    return hach

# Test
p = 11
print(hachage('LAPIN',p))
print(hachage('SAPIN',p))
print(hachage('LUTIN',p))
print(hachage('',p))

def enlever_des_doublons(liste,p):
    nouv_liste = []  # future liste avec moins de doublons
    table = [0]*p    # liste de p zéros
    for x in liste:
        hach = hachage(x,p)
        if table[hach] == 0:  # si élément x pas déjà retenu
            table[hach] = x   # on le note
            nouv_liste += [x] # et on le rajoute
        else:                 
            if x != table[hach]:   # dans le cas mot différent avec même hash
                nouv_liste += [x]  # on le rajoute


    return nouv_liste


liste = ['AA','BB','CC','AA','LAPIN','CHAT','CHIEN','AA','BB','CC','AA','LAPIN','CHAT','CHIEN']
print(liste)
print(enlever_des_doublons(liste,12))


def iterer_enlever_des_doublons(liste,nb_iter=3):
    p = 2*len(liste)
    for i in range(nb_iter):
        liste = enlever_des_doublons(liste,p)
        p = p+1
    return liste

print(liste)
print(iterer_enlever_des_doublons(liste,2))




##############################
# Activité 3 - Listes
##############################


# 2 processeurs

def maximum_recursif(liste):
    infini = 1000
    if len(liste)==0: return -infini
    if len(liste)==1: return liste[0]
    n = len(liste)//2
    liste_gauche = liste[:n]
    liste_droite = liste[n:]
    max_gauche = maximum_recursif(liste_gauche)
    max_droite = maximum_recursif(liste_droite)
    maxi = max(max_gauche,max_droite)
    return maxi

# Test
liste = [6,3,8,10,4]
print(maximum_recursif(liste))

def sous_maximum_recursif(liste):
    pass


# Le faire avec 3 processeurs
def extraire_pairs(liste):
    if len(liste)==0: return []
    if len(liste)==1:
        if liste[0]%2 == 0:
            return [liste[0]]
        else:
            return []

    # Le faire avec 3 processeurs
    n = len(liste)//2
    liste_gauche = liste[:n]
    liste_droite = liste[n:]
    liste_paire_gauche = extraire_pairs(liste_gauche)
    liste_paire_droite = extraire_pairs(liste_droite)
    liste_paire = liste_paire_gauche + liste_paire_droite 
    return liste_paire


liste = [6,3,8,10,7,4,11]
print(extraire_pairs(liste))



def premier_rang(liste):
    # if len(liste)==0: return None
    if len(liste)==1:
        if liste[0]==0:
            return None
        else:
            return 0

    n = len(liste)//2
    liste_gauche = liste[:n]
    liste_droite = liste[n:]
    premier_rang_gauche = premier_rang(liste_gauche)
    premier_rang_droite = premier_rang(liste_droite)
    if premier_rang_gauche != None:
        return premier_rang_gauche
    elif premier_rang_droite != None:
        return n + premier_rang_droite
    else:
        return None

liste = [0,0,0,0,0,0,1,0,1,1,0]
print(premier_rang(liste))


##############################
# Activité 4 - Prefix-sum
##############################

def sommes_partielles(liste):
    liste_sommes = []
    s = 0
    for x in liste:
        s = s + x 
        liste_sommes += [s]
    return liste_sommes

# Test
liste = [1,2,3,4,5,6,7,8]
print(sommes_partielles(liste))


def sommes_partielles_recursif(liste):
    # La liste doit être de longueur une puissance de 2

    n = len(liste)
    if n==1: return [liste[0]]
    
    sous_liste = [liste[2*i] + liste[2*i+1] for i in range(n//2)]
    print(sous_liste)

    liste_remontee = sommes_partielles_recursif(sous_liste)

    print(liste_remontee)

    liste_descente = [liste[0]] 
    for i in range(1,n):    
        print(liste,sous_liste,liste_remontee,i,i//2)
        if i%2 == 0:
            liste_descente += [liste_remontee[i//2-1] + liste[i]]
        else:
            liste_descente += [liste_remontee[(i-1)//2]]

    return liste_descente


# Test
print("--- prefix-sum ---")
liste = [1,2,3,4,5,6,7,8]*2
print(sommes_partielles_recursif(liste))
print(sommes_partielles(liste))

# A faire pour len(liste) pas puissance de 2

def liste_puissance_de_deux(liste):
    n = len(liste)
    return


# A faire : application rang non-zeros liste sparse

def rangs_non_nuls(liste):
    pass

