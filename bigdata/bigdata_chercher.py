
##############################
# Big data
##############################

# Cours ordre alphabétique et Python
print("AA"<="AB")
print("CB"<="CA")

##############################
# Activité 2 - Chercher dans liste ordonnée
##############################

##############################
## Question 1 ##

def fichier_vers_liste_noms(fichier):
    fic_in = open(fichier,"r")

    liste_noms = []
    for ligne in fic_in:
        ligne = ligne.strip()  # Pour retirer la fin de ligne       
        liste = ligne.split(",")
        nom = liste[1]
        liste_noms = liste_noms + [nom]

    # Fermeture des fichiers
    fic_in.close()

    liste_noms.sort()

    return liste_noms 


print("--- Liste triée des noms ---")
liste_noms = fichier_vers_liste_noms("personnes_100.csv")
print(liste_noms[0:20])


##############################
## Question 2 ##

def est_debut(debut,chaine):
    if len(debut) > len(chaine):
        return False

    n = len(debut)
    if debut == chaine[:n]:
        return True
    else:
        return False


print("--- Début d'une chaîne ? ---")
print(est_debut("ABC","ABCDEF"))
print(est_debut("XYZ","ABCDEF"))
print(est_debut("ABCD","AB"))


##############################
## Question 3 ##

def chercher_1(liste,debut):
    N = 0               # Nb d'itérations
    for nom in liste:
        if est_debut(debut,nom):
            return nom, N
        N = N + 1
    return None, N


print("--- Chercher par dans la liste du premier au dernier ---")
print(chercher_1(liste_noms,"Bri")) 
print(chercher_1(liste_noms,"Xyz"))   


##############################
## Question 4 ##

def chercher_2(liste,debut):
    a = 0
    b = len(liste) - 1
    N = 0               # Nb d'itérations
    while b >= a:
        m = (b+a)//2
        # print(b,a,m,liste[m])

        if est_debut(debut,liste[m]):
            return liste[m], N
        
        if debut > liste[m]:
            a = m+1
        else: 
            b = m-1
        N = N + 1

    # A la fin a=m=b
    else:
        return None, N


print("--- Chercher par dichotomie ---")
print(chercher_2(liste_noms,"Bri")) 
print(chercher_2(liste_noms,"Xyz")) 


##############################
## Question 5 ##

from math import *

print("--- Comparaisons ---")
liste_noms = fichier_vers_liste_noms("personnes_10000.csv")
print(liste_noms[0:20])
n = len(liste_noms)
print("Longueur de la liste :",n)
print("Itération max recherche 1 :",n)
print("Itération max recherche 2 :",floor(log(n,2))+1)
print(chercher_1(liste_noms,"Bri")) 
print(chercher_2(liste_noms,"Bri"))
print(chercher_1(liste_noms,"Xyz")) 
print(chercher_2(liste_noms,"Xyz"))
