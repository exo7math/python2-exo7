
##############################
# Big data
##############################

##############################
# Activité 1 - Sondage
##############################

# Fichiers pour tests (l'entier indique le nb d'entrées) :
# sexe,nom,prenom,naissance(jj/mm/aaaa),ville,poids,taille,groupe sanguin
# "personnes_100.csv"
# "personnes_1000.csv"
# "personnes_10000.csv"
# "personnes_100000.csv"

# généré par https://fr.fakenamegenerator.com/

##############################
## Question 1 ##

def age_moyen(debut,fin,fichier):

    annee_aujourdhui = 2019

    # Fichier à lire
    fic_in = open(fichier,"r")

    num = 0  # Numéro de ligne
    somme = 0
    for ligne in fic_in:
        if debut <= num < fin:
            ligne = ligne.strip()  # Pour retirer la fin de ligne
            liste = ligne.split(",")
            date = liste[3]
            annee_naissance = int(date.split("/")[2])
            age = annee_aujourdhui - annee_naissance
            somme = somme + age
        num = num + 1

    # Fermeture des fichiers
    fic_in.close()

    moyenne = somme / (fin-debut)

    return moyenne

print("--- Age moyen à partir d'un sondage ---")
moyenne = age_moyen(0,100,"personnes_1000.csv")
print("Moyenne sur échantillon",moyenne)
moyenne = age_moyen(0,1000,"personnes_1000.csv")
print("Moyenne sur tout",moyenne)


##############################
## Question 2 ##

def probabilite_initiale(lettre,debut,fin,fichier):

    # Fichier à lire
    fic_in = open(fichier,"r")

    num = 0    # Numéro de ligne
    nb = 0     # Nb d'initiales testées
    nb_ok = 0  # Nb de bonnes intiales
    for ligne in fic_in:
        if debut <= num < fin:
            ligne = ligne.strip()  # Pour retirer la fin de ligne
            liste = ligne.split(",")
            init = liste[1][0]   # La première lettre du premier mot

            if init == lettre:
                nb_ok = nb_ok + 1
            nb = nb + 1
        num = num + 1

    # Fermeture des fichiers
    fic_in.close()

    proba = nb_ok/nb

    return proba

print("--- Probabilité initiale ---")
proba = probabilite_initiale("D",0,1000,"personnes_100000.csv")
print("Probabilité sur échantillon :",proba)
print("Nb d'occurences attendues pour 26 noms :",proba*26)

##############################
## Question 3 ##

def probabilite_groupe_sanguin(debut,fin,fichier):
    # sortie nb de A+, A-, B+, B-, AB+, AB-, O+, O-

    # Fichier à lire
    fic_in = open(fichier,"r")

    dico_nb = {}
    dico_nb['A+'] = 0
    dico_nb['A-'] = 0
    dico_nb['B+'] = 0
    dico_nb['B-'] = 0
    dico_nb['O+'] = 0
    dico_nb['O-'] = 0    
    dico_nb['AB+'] = 0
    dico_nb['AB-'] = 0

    print(dico_nb)


    num = 0    # Numéro de ligne
    nb = 0     # Nb de personnes testées
    for ligne in fic_in:
        if debut <= num < fin:
            ligne = ligne.strip()  # Pour retirer la fin de ligne
            liste = ligne.split(",")
            groupe = liste[7]  # Le groupe
            dico_nb[groupe] += 1
            nb = nb + 1
        num = num + 1

    # Fermeture des fichiers
    fic_in.close()

    print(dico_nb)
    dico_proba = {}
    for cle in dico_nb:
        nb_groupe = dico_nb[cle]
        dico_proba[cle] = nb_groupe/nb

    return dico_proba

print("--- Probabilités groupe sanguin ---")
dico = probabilite_groupe_sanguin(0,10,"personnes_100.csv")
print("Probabilités groupe sanguin :",dico)
