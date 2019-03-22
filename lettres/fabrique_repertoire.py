
##############################
# Pour : Le mot le plus long
##############################

# Conversion de la liste des mots en un répertoire (on reserve le mot dictionnaire à l'objet Python) :
# - on retire les noms propres (qui commence par une majuscule)
# - on retire les accents (et les doublons possibles)
# - on passe tout en majuscules
# - les mots sont par ordre alphabétique
# Il ne reste donc que des mots orodnnés ayant des caractères parmi:
#              "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Liste simple #

# Source de la liste simple : https://www.freelang.com/dictionnaire/dic-francais.php

# Depuis la page :
# "La liste compte 22 740 mots et est au format "txt" 
# Sauf erreur de notre part, cette liste est libre de droits. 
# Elle est fournie telle quelle et sans aucune garantie. 
# Merci à Bernard Vivier pour l'avoir entièrement revue et adaptée."" 

# Il y a en fait 22736 mots, et 20239 après nettoyage.
# Il manque le mot "python" !!

# Liste complète #

# Source de la liste complète 'hunspell', via http://www.fil.univ-lille1.fr/~L1S2API/CoursTP/tp_anagrammes.html#id3

# Il y a 139719 originaux et 131896 après nettoyage.

# import string
import unicodedata

def liste_vers_repertoire(fichier_in,fichier_out):

    # Fichier à lire
    fic_in = open(fichier_in,"r")

    # Fichier à écrire
    fic_out = open(fichier_out,"w")

    nb_in = 0    # Nombre de mots du fichiers initial
    nb_out = 0   # Nombre de mots du fichiers final
    mot_prec = "" # Mot précédent

    for mot in fic_in:
        nb_in += 1

        # mot1 = unicode(mot,'utf-8')
        mot_ascii = unicodedata.normalize('NFD', mot).encode('ascii', 'ignore')
        mot_utf8 = mot_ascii.decode('utf8')

        if mot_utf8[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": # Si nom propre on zappe
            continue

        if ("-" in mot_utf8) or (" " in mot_utf8) or ("'" in mot_utf8) or ("." in mot_utf8): # Si tiret ou espace ou apostrophe on zappe
            continue
        
        mot_clean = mot_utf8.upper().strip()  # Tout en majuscule

        for c in mot_clean:
            if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                print("Pb avec de caractère avec :",mot_clean)
        # Vérification ordre alphabétique
        if mot_prec > mot_clean:
            print("Problème d'ordre avec ",mot_prec,mot_clean)
            
        if mot_clean != mot_prec:  # pour éviter les doublons
            nb_out += 1
            fic_out.write(mot_clean+"\n") 
            mot_prec = mot_clean

    # Fermeture des fichiers
    fic_in.close()
    fic_out.close()

    print("Anciens mots  :",nb_in)
    print("Nouveaux mots :",nb_out)
    return

print("--- Conversion d'une liste en un repertoire propre ---")

print(" -- Liste simple --")
liste_vers_repertoire("liste_francais_simple.txt","repertoire_francais_simple.txt")

print(" -- Liste complète --")
liste_vers_repertoire("liste_francais_tout.txt","repertoire_francais_tout.txt")
