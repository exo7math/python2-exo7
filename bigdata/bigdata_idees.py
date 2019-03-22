
##############################
# Big data
##############################


from random import *

##############################
# Activité 1 - Sondage
##############################

# Fichiers pour tests (l'entier indique le nb d'entrées) :
# "personnes_100.csv"
# "personnes_1000.csv"
# "personnes_10000.csv"
# "personnes_100000.csv"


##############################
## Question 1 ##

def age_moyen(debut,fin,fichier):

    # Fichier à lire
    fic_in = open(fichier,"r")

    num = 0  # Numéro de ligne
    somme = 0
    for ligne in fic_in:
        if debut <= num < fin:
            liste = ligne.split(",")
            age = int(liste[2])
            somme = somme + age
        num = num + 1

    # Fermeture des fichiers
    fic_in.close()

    moyenne = somme / (fin-debut + 1)

    return moyenne

print("--- Age moyen à partir d'un sondage ---")
moyenne = age_moyen(0,50,"personnes_100.csv")
print("Moyenne sur échantillon",moyenne)


##############################
## Question 2 ##

def est_jeune(age,moyenne):
    return age <= moyenne

##############################
## Question 3 ##

def probabilite_initiale(lettre,debut,fin,fichier):

    # Fichier à lire
    fic_in = open(fichier,"r")

    num = 0    # Numéro de ligne
    nb = 0     # Nb d'initiales testées
    nb_ok = 0  # Nb de bonnes intiales
    for ligne in fic_in:
        if debut <= num < fin:
            liste = ligne.split(",")
            init = liste[0][0]   # La première lettre du premier mot

            if init == lettre:
                nb_ok = nb_ok + 1
            nb = nb + 1
        num = num + 1

    # Fermeture des fichiers
    fic_in.close()

    proba = nb_ok/nb

    return proba

print("--- Probabilité initiale ---")
proba = probabilite_initiale("M",0,1000,"personnes_100000.csv")
print("Probabilité sur échantillon :",proba)
print("Nb d'occurences attendues pour 26 noms :",proba*26)



##############################
# Activité 2 - Chercher dans liste ordonnée
##############################

##############################
## Question 1 ##

def fichier_vers_liste_noms(fichier):
    fic_in = open(fichier,"r")

    liste_noms = []
    for ligne in fic_in:
        liste = ligne.split(",")
        nom = liste[0]
        liste_noms = liste_noms + [nom]

    # Fermeture des fichiers
    fic_in.close()

    return liste_noms  

liste_noms = fichier_vers_liste_noms("personnes_100.csv")
print(liste_noms)


def chercher_1(liste,nom):
    for l in liste:
        if l == nom:
            return True
    return False

print("--- Chercher par ordre alphabétique ---")
print(chercher_1(liste_noms,"C")) 
print(chercher_1(liste_noms,"Z"))   


##############################
## Question 2 ##

print("AA"<="AB")
print("CB"<="CA")

def chercher_2(liste,nom):
    g = 0
    d = len(liste) - 1
    N = 0
    while d > g and N <= 10:
        m = g + (d-g)//2
        print(d,g,m)
        if nom > liste[m]:
            g = m+1
        else: 
            d = m-1
        N += 1

    # A la fin d=g=m
    if nom == liste[m]:
        return True
    else:
        return False


print("--- Chercher par ordre alphabétique ---")
print(chercher_2(liste_noms,"C")) 
print(chercher_2(liste_noms,"Z")) 


##############################
## Question 3 ##

# Mesure du temps n vs ln(n)




##############################
# Activité 3 - Tank
##############################


##############################
## Question 1 ##

def formule_tanks(echantillon):
    """ Applique la formule des tanks qui estime ... """
    k = len(echantillon)
    m = max(echantillon)
    N = m + m/k - 1
    return N

# Test
print("--- Formule des tanks ---")
echantillon = [163,87,222,32]
N = formule_tanks(echantillon)
print("Echantillon :",echantillon)
print("Nombre de tanks total estimé : ",round(N))


def double_moyenne(echantillon):
    """ Applique la formule des tanks qui estime ... """
    k = len(echantillon)
    S = sum(echantillon)
    N = 2 * S/k
    return N

# Test
print("--- Formule des tanks ---")
echantillon = [163,87,222,32]
N1 = formule_tanks(echantillon)
N2 = double_moyenne(echantillon)
print("Echantillon :",echantillon)
print("Nombre de tanks total estimé, par la formule des tanks : ",round(N1))
print("Nombre de tanks total estimé, par le double de la moyenne : ",round(N2))


##############################
## Question 2 ##

def tirage_sans_remise(N,k):
    tirage = []
    while len(tirage) < k:
        n = randint(0,N)
        if n not in tirage:
            tirage.append(n)
    return tirage

# Test
print("--- Tirage sans remise ---")
N = 100
k = 4
tirage = tirage_sans_remise(N,k)
print("N, k :",N,k)
print("Tirage : ",tirage)   


##############################
## Question 3 ##

def erreurs(N,k,nb_tirages=1000):
    erreur_tanks = 0
    erreur_double = 0
    for i in range(nb_tirages):
        echantillon = tirage_sans_remise(N,k)
        N1 = formule_tanks(echantillon)
        N2 = double_moyenne(echantillon)
        print(N1,N2)
        erreur_tanks += abs(N-N1)
        erreur_double += abs(N-N2)
        moyenne_erreur_tank = erreur_tanks/nb_tirages
        moyenne_erreur_double = erreur_double/nb_tirages
    return moyenne_erreur_tank,moyenne_erreur_double

# Test
print("--- Erreurs formules des tanks/double de la moyenne ---")
N = 1000
k = 5
E1,E2 = erreurs(N,k)
print("N, k :",N,k)
print("Erreurs formule des tanks : ",E1)  
print("Erreurs formule double de la moyenne : ",E2) 




##############################
# Activité 4 - Problème du secrétaire
##############################


##############################
## Question 1 ##

def genere_liste(k,N):
    """ Génère une liste de k éléments entre 0 et N. """
    liste = []
    for i in range(k):
        n = randint(0,N)
        liste.append(n)
    return liste

# Test
print("--- Génération d'une liste ---")
N = 1000
k = 20
liste_aleatoire = genere_liste(k,N)
print("k, N :",k,N)
print("Liste : ",liste_aleatoire)  


##############################
## Question 2 ##

from math import *

def choix_secretaire(liste,pourc_test):
    k = len(liste)  # longueur de la liste
    j = min(ceil(pourc_test/100*k),100)  # longueur de l'échantillon
    # print("j",j)
    Me = max(liste[:j])  # le meilleur score dans l'échantillon
    # print("Me",Me)
    for i in range(j,k):  # on cherche un meilleur parmi les suivants
        if liste[i] >= Me:
            return liste[i]
    return None    # on n'a pas trouvé, on ne prend personne


# Test
print("--- Choix d'un secrétaire ---")
N = 100
k = 10
liste_aleatoire = genere_liste(k,N)
M = max(liste_aleatoire)  # le meilleur score d'un sécretaire
pourcentage = 30
MM = choix_secretaire(liste_aleatoire,pourcentage)
print("k, N:",k, N)
print("Liste : ",liste_aleatoire)  
print("Meilleur valait :",M)
print("Choix vaut :",MM)



##############################
## Question 3 ##

def meilleurs_secretaires(k,N,pourc_test,nb_tirages):
    nb_meilleurs = 0
    for i in range(nb_tirages):
        liste = genere_liste(k,N)
        M = max(liste)  # le meilleur score d'un sécretaire    
        MM = choix_secretaire(liste,pourc_test)
        if M == MM:
            nb_meilleurs += 1

    return nb_meilleurs
# Test
print("--- Nb de fois où le choix d'un secrétaire est le meilleur ---")
N = 100
k = 100
pourcentage = 30
nb_best = meilleurs_secretaires(k,N,pourcentage,1000)
print("k, N:",k, N)
print("Pourcentage : ",pourcentage)
print("Nb de meilleurs choisi : ",nb_best)  



##############################
## Question 4 ##

# Variante liste des erreurs (avec les mêmes tirages pour tous)
def liste_meilleurs_secretaires(k,N,nb_tirages):
    liste_nb_meilleurs = [0 for i in range(1,100)]
    for i in range(nb_tirages):
        liste = genere_liste(k,N)
        M = max(liste)  # le meilleur score d'un sécretaire    
        for p in range(1,100):
            MM = choix_secretaire(liste,p)
            if M == MM:           
                liste_nb_meilleurs[p-1] += 1   

    return liste_nb_meilleurs

# Test
print("--- Liste des erreurs choix d'un secrétaire ---")
N = 1000
k = 100

liste_best = liste_meilleurs_secretaires(k,N,1000)
print("k, N:",k, N)
print("Liste des nb de bons choix : ",liste_best)     
maximum = max(liste_best)
print("Meilleure stratégie : pourcentage = ",liste_best.index(maximum))



##############################
# Activité 5 - Test bayésien naïf
##############################

from math import *

##############################
## Question 1 ##



def moyenne(liste):
    """ Calcule la moyenne des éléments
    Entrée : une liste de nombres
    Sortie : leur moyenne """    
    
    nbliste = len(liste)

    if nbliste == 0:
        moy = 0
    else:
        moy = sum(liste) / nbliste 

    return moy


# Test 
print("--- Moyenne ---")
liste = [5,18,6,3]
print(liste)
print(moyenne(liste))


##############################
## Question 2 ##

def variance(liste):
    """ Calcule la variance des éléments
    Entrée : une liste de nombres
    Sortie : leur variance """    

    if len(liste) == 0:
        return 0
 
    moy = moyenne(liste)

    somme_carres = 0
    for x in liste:
        somme_carres = somme_carres + (x-moy)**2
    
    var = somme_carres / len(liste)

    return var


# Test 
print("--- Variance ---")
liste = [6,8,2,10]
print(liste)
print(variance(liste))


##############################
## Question 2 ##

def densite_gauss(x,mu,sigma2):
    p =  1/sqrt(2*pi*sigma2)*exp( -1/2 * (x-mu)**2 / sigma2 )
    return p

# Test 
print("--- Fonction de densité de la loi normale ---")
mu = 178
sigma2 = 29.333
x = 183
print(densite_gauss(x,mu,sigma2))


##############################
## Question 1 ##


##############################
## Question 1 ##
