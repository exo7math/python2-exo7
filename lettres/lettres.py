
##############################
# Des chiffres et des lettres
##############################

from random import *

# Nomenclature :
# * repertoire : liste de mots
# * indice : les lettres ordonnées du mot. ex : indice("BAC") = "ABC" 
# * dictionnaire et clé : seulement pour notion Python
# * éviter à tout prix la confusion dictionnaire (python) et dictionnaire (liste de mots)

# On peut travailler avec le répertoire simple (20239 mots) ou le répertoire complet (131896 mots)

##############################
# Activité 1 - Chercher un mot dans un répertoire
##############################

##############################
## Question 1 ##

def lire_repertoire(fichier):
    """ Lire un des deux fichiers qui contient tous les mots français
    et le transformer en une liste """

    # Fichier à lire
    fic_in = open(fichier,"r")

    repertoire = []
    for ligne in fic_in:
        mot = ligne.strip()
        repertoire.append(mot)

    fic_in.close()

    return repertoire

# Test
print("--- Liste obtenue par lecture d'un répertoire depuis un fichier ---")
repertoire = lire_repertoire("repertoire_francais_simple.txt")
# repertoire = lire_repertoire("repertoire_francais_tout.txt")

print("Nombre de mots dans le répertoire :",len(repertoire))


##############################
## Question 2 ##

def recherche_basique(mot,liste):
    """ Recherche séquentielle d'un mot dans une liste """
    i = 0
    while i<len(liste):
        if mot == liste[i]:
            return i
        i = i + 1

    return None

# Test
print("--- Recherche d'un mot dans le répertoire ---")
mot = "SERPENT"
trouve = recherche_basique(mot,repertoire)
print(mot,"dans répertoire ?",trouve)
mot = "PYTHON"
trouve = recherche_basique(mot,repertoire)
print(mot,"dans répertoire ?",trouve)


##############################
## Question 3 ##

# On profite du fait que la liste soit ordonnée 
# Python connaît l'ordre alphabétique

def recherche_dichotomie(mot,liste):
    """ Recherche d'un mot dans une liste ordonnée par dichotomie """

    a = 0
    b = len(liste)-1
    
    while b>=a:
        k = (a+b)//2
        if mot == liste[k]:
            return k
        elif mot > liste[k]:
            a = k+1
        else:
            b = k-1

    return None

# Test
print("--- Recherche dichotomique dans le répertoire ---")
mot = "SERPENT"
trouve = recherche_dichotomie(mot,repertoire)
print(mot,"dans répertoire ?",trouve)
mot = "PYTHON"
trouve = recherche_dichotomie(mot,repertoire)
print(mot,"dans répertoire ?",trouve)


# Test
from math import log,floor
print("--- Comparaison séquentielle/dichotomie ---")
print("  -- Répertoire simple --")
repertoire = lire_repertoire("repertoire_francais_simple.txt")
n = len(repertoire)
print("n =",n,"log_2 = ",floor(log(n,2)+1))

print("  -- Répertoire simple --")
repertoire = lire_repertoire("repertoire_francais_tout.txt")
n = len(repertoire)
print("n =",n,"log_2 = ",floor(log(n,2)+1))


##############################
# Activité 2 - Dictionnaire en Python
##############################

# à faire ....




##############################
# Activité 3 - Dictionnaire d'anagrammes
##############################

##############################
## Question 1 ##

def calculer_indice(mot):
    """ Réordonne les lettres d'un mot par ordre alphabétique : c'est l'indice du mot """
    liste = list(mot) 
    liste.sort()
    indice = "".join(liste)
    return indice 

# Test
print("--- Indice d'un mot ---")
mot = "KAYAK"
indice = calculer_indice(mot)

print("mot =",mot)
print("indice =",indice)


##############################
## Question 2 ##

def sont_anagrammes(mot1,mot2):
    """ Test si deux mots sont annagrammes
    C'est exactemment tester si ils ont le même indice """
    indice1 = calculer_indice(mot1)
    indice2 = calculer_indice(mot2)
    if indice1 == indice2:
        return True
    else:
        return False

# Test
print("--- Test anagramme ---")
mot1,mot2 = "PRIERES", "RESPIRE"
print("Les mots ",mot1," et ",mot2)
print("Sont anagrammes ?",sont_anagrammes(mot1,mot2))


##############################
## Question 3 ##

def dictionnaire_indices_mots(liste):
    """ Cosntruit le dictionnaire clé -> forme de la forme
    indice -> valeur=[mot1,mot2,...] """
    dico = {}
    for mot in liste:
        indice = calculer_indice(mot)
        if indice in dico:
            dico[indice].append(mot)
        else:
            dico[indice] = [mot]
    return dico

# Test
print("--- Dico des indice d'une liste de mots ---")
liste = ["CRIME","COUCOU","PRIERES","MERCI","RESPIRE","REPRISE"]
dico = dictionnaire_indices_mots(liste)
print("liste =",liste)
print("dico =",dico)


##############################
## Question 4 ##

def liste_anagrammes(liste):
    """ Trouve tous les annagrammes d'une liste """
    dico = dictionnaire_indices_mots(liste)
    liste_anag = []
    for cle in dico:
        if len(dico[cle])>1:
            liste_anag.append(dico[cle])

    return liste_anag


def afficher_anagrammes(liste):
    """ Affiche tous les annagrammes d'une liste """
    liste_anag = liste_anagrammes(liste)
    print("Nombre d'anagrammes :",len(liste_anag))
    for anag in liste_anag:
        for mot in anag:
            print(mot,end=" ")
        print()
    return

# Test
print("--- Anagrammes français ---")
repertoire = lire_repertoire("repertoire_francais_simple.txt")
# repertoire = lire_repertoire("repertoire_francais_tout.txt")
print("Nombre d'anagrammes :",len(liste_anagrammes(repertoire)))
# afficher_anagrammes(repertoire)


##############################
## Question 5 ##

def fichier_indice_mots(fichier_in,fichier_out):
    """ Ecris le fichier associant à chaque indice la liste de mots correspondant.
    Chaque ligne est de la forme : "indice : mot1 mot2 mot3" """
    liste = lire_repertoire(fichier_in)
    dico = dictionnaire_indices_mots(liste)

    fic_out = open(fichier_out,"w")

    for cle,valeur in sorted(dico.items()):
            fic_out.write(cle+" : ")
            for mot in valeur:
                fic_out.write(mot+" ")
            fic_out.write("\n")

    fic_out.close()

    return

# Test
print("--- Conversion d'un répertoire vers liste de 'indice:mot1 mot2 mot3'  ---")
fichier_indice_mots("repertoire_francais_simple.txt","dico_indice_mots.txt")
# fichier_indice_mots("repertoire_francais_tout.txt","dico_indice_mots.txt")



##############################
# Activité 3 - Le mot le plus long
##############################

##############################
## Question 1 ##

def tirage_lettres(n):
    """ Tirage aléatoire de n lettres majuscules 
    (certaines lettres ont plus de chances d'ếtres tirées que d'autres) """
    Alphabet = "AEIOU"*5 + "BCDFGHLMNPRST"*2 + "KJQVWXYZ"
    print(Alphabet)
    print(len(Alphabet))
    tirage = []
    for __ in range(n):
        k = randint(0,len(Alphabet)-1)
        tirage.append(Alphabet[k])
    return tirage

# Test
print("--- Tirage de lettres ---")
n = 4
tirage = tirage_lettres(n)
print("Tirage :",tirage)


##############################
## Question 2 ##

def liste_binaire(n):
    """ Liste des écritures binaires de tous les entiers sur n bits """
    liste = []
    for k in range(2**n):

        b_str = list(format(k, '0'+str(n)+'b'))
        b_str.reverse()
        b = [int(bs) for bs in b_str]
        liste.append(b)

    return liste 

# Test
print("--- Listes binaires possibles ---")
n = 4
liste = liste_binaire(n)
print("n =",n)
print(liste)


##############################
## Question 3 ##

def indices_depuis_tirage(tirage):
    """ A partir d'un tirage de lettres, construit tous les sous-tirages possibles """
    tirage.sort() # Tri

    n = len(tirage)

    liste = []
    for k in range(1,2**n):

        b_str = list(format(k, '0'+str(n)+'b'))
        b_str.reverse()
        b = [int(bs) for bs in b_str]
        mot = ""
        for i in range(n):
            if b[i] == 1:
                mot = mot + tirage[i]

        liste.append(mot)

    return liste

# Test
print("--- Mots possibles depuis un tirage ---")
n = 4
tirage = tirage_lettres(n)
tirage = ['A','B','C','L']
print("Tirage :",tirage.sort())
liste = indices_depuis_tirage(tirage)

# Ordre de la plus longue au plus petit
liste.sort(key=lambda item:len(item),reverse=True)

print("Liste indices :",liste)



##############################
## Question 4 ##

def mot_le_plus_long(tirage,dico):
    """ Trouve tous les mots français à partir d'un tirage de lettres
    et d'un dictionnaire indice->liste de mots français """
    liste = indices_depuis_tirage(tirage)              # Tous les sous-tirages possibles
    liste.sort(key=lambda item:len(item),reverse=True) # Du plus long au plus court

    # Recherche des clés (= indices) qui existent 
    liste_cles = []
    for cle in liste:
        if cle in dico:
            liste_cles.append(cle)

    # Conversion en mots
    liste_mots = [dico[cle] for cle in liste_cles]
    return liste_mots

# Test
print("--- Génération des indices (à faire une seule fois) ---")
repertoire = lire_repertoire("repertoire_francais_simple.txt")
repertoire = lire_repertoire("repertoire_francais_tout.txt")

dico = dictionnaire_indices_mots(repertoire)
print("Nombre de mots dans le répertoire :",len(repertoire))
print("Nombre d'indices :",len(dico))


print("--- Le mot le plus long ---")
# tirage = ["A","B","C","E","F","H"]
# tirage = ['G', 'E', 'A', 'T', 'G', 'A', 'N']
# tirage = ['A','B','C','L']
n = 10
tirage = tirage_lettres(n)
print("Tirage :",tirage)
solutions = mot_le_plus_long(tirage,dico)
print("Liste :",*solutions)


print("--- Le mot le plus long - Exemples ---")

repertoire = lire_repertoire("repertoire_francais_simple.txt")
# repertoire = lire_repertoire("repertoire_francais_tout.txt")
dico = dictionnaire_indices_mots(repertoire)

# tirage = ['Z', 'M', 'O', 'N', 'U', 'E', 'G']
# tirage = ['H', 'O', 'I', 'P', 'E', 'U', 'C', 'R']
# tirage = ['H', 'A', 'S', 'T', 'I', 'D', 'O', 'I', 'T']
tirage = ['E', 'T', 'N', 'V', 'E', 'U', 'Z', 'O', 'V', 'N']
print("Tirage :",tirage)
solutions = mot_le_plus_long(tirage,dico)
print("Liste :",*solutions)



# Idées : 
# * recherche des palindromes (RADAR)
# * recherche des anacycliques (LEON <-> NOEL)

