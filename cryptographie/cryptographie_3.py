
##############################
# Cryptographie
##############################

##############################
# Activité 2 - Attaque du chiffrement par substitution
##############################

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Génération d'un mélange aléatoire
from random import *
liste_lettre = list(Alphabet.lower())
shuffle(liste_lettre)
Melange = "".join(liste_lettre)


print("--- Alphabet mélangé ---")
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
Melange  = "bzryjxscwqiveguopldmtanfhk"
print(Melange)


##############################
## Question 1 ##

def substitution(phrase,Alphabet_depart,Alphabet_arrivee):
    """" Transforme une phrase par substitution """

    phrase_subs = ""
    for car in phrase:
        if car not in Alphabet_depart:
            phrase_subs += car
        else:
            i = Alphabet_depart.index(car)
            car_subs = Alphabet_arrivee[i]
            phrase_subs += car_subs
    return phrase_subs


# Test
print("--- Substitution avec alphabet partiel ---")


Alphabet_depart  = "abcdefghijklmnopqrstuvwxyz"
Alphabet_arrivee = "...S.....E..T............."

phrase = "ESPRIT ES TU LA ?"
phrase_codee = substitution(phrase,Alphabet,Melange)
phrase_decodee = substitution(phrase_codee,Alphabet_depart,Alphabet_arrivee)
print(phrase)
print(phrase_codee)
print(phrase_decodee)


##############################
## Question 2 ##

Minuscules = "abcdefghijklmnopqrstuvwxyz"

def statistique(phrase,mon_alphabet=Minuscules):
    """ Nb d'apparition pour chaque lettre """

    stat = [0]*26
    for car in phrase:
        if car in mon_alphabet:
            i = mon_alphabet.index(car)
            stat[i] += 1

    return stat


def affiche_statistiques(phrase,mon_alphabet=Minuscules):
    print("-- Statistique --")
    print(phrase)
    stat = statistique(phrase,mon_alphabet)
    for i in range(26):
        if stat[i] != 0:
            print(mon_alphabet[i],stat[i])
    return

# Test
print("--- Apparition des lettres ---")
phrase = "jdolwm jd mt vb ?"
stat = statistique(phrase)
print(phrase)
affiche_statistiques(phrase)



##############################
## Question 3 ##   

def frequence(phrase,mon_alphabet=Minuscules):
    """ Fréquence de chaque lettre """

    stat = [0]*26
    nb = 0
    for car in phrase:
        if car in mon_alphabet:
            i = mon_alphabet.index(car)
            stat[i] += 1
            nb += 1

    freq = [s/nb for s in stat]

    return freq

def affiche_frequences(phrase,mon_alphabet=Minuscules):
    print("-- Fréquence --")
    print(phrase)
    freq = frequence(phrase,mon_alphabet)
    for i in range(26):
        if freq[i] != 0:
            print(mon_alphabet[i],'{0:.2f}'.format(freq[i]*100),"%")
    return

# Test
print("--- Apparition des lettres ---")
phrase = "jdolwm jd mt vb ?"
freq = frequence(phrase)
print(phrase)
affiche_frequences(phrase)

# Cours
print("--- Apparition des lettres ---")
phrase = "ESPRIT ES TU LA ?"
freq = frequence(phrase,Alphabet)
print(phrase)
affiche_frequences(phrase,Alphabet)



# Cours
print("--- Exemple cours ---")
phrase = "ET SI ON ESSAYAIT D ETRE HEUREUSES"

affiche_statistiques(phrase,Alphabet)
freq = frequence(phrase,Alphabet)
affiche_frequences(phrase,Alphabet)


Melange = "bzryjxscwqiveguopldmtanfhk"
phrase_codee = substitution(phrase,Alphabet,Melange)
print(phrase_codee)

affiche_statistiques(phrase_codee)
freq = frequence(phrase_codee)
affiche_frequences(phrase_codee)


##############################
## Question 4 ##  

from random import *
liste_lettre = list(Alphabet.lower())
shuffle(liste_lettre)
Melange = "".join(liste_lettre)
print(Melange)

##############################

Melange1 = "ybzfvotenupajgisxhdmlwqckr"
# # Les frères de Goncourt
print("--- Les frères Goncourt :")
phrase1 = "LA STATISTIQUE EST LA PREMIERE DES SCIENCES INEXACTES"
# affiche_frequences(phrase1,Alphabet)
enigme1 = substitution(phrase1,Alphabet,Melange1)
print(enigme1)
# # affiche_frequences(enigme1,Minuscules)


##############################

Melange2 = "oufkplzivxqamnbwtjygdsechr"
# Charles Darwin
print("--- Charles Darwin :")
phrase2 = "LES ESPECES QUI SURVIVENT NE SONT PAS LES ESPECES LES PLUS FORTES NI LES PLUS INTELLIGENTES MAIS CELLES QUI S ADAPTENT LE MIEUX AUX CHANGEMENTS"
# affiche_frequences(phrase2,Alphabet)
enigme2 = substitution(phrase2,Alphabet,Melange2)
print(enigme2)
# # affiche_frequences(enigme2,Minuscules)

##############################

Melange3 = "whixnabjctdkepzolfmyqsrvug"
# Albert Einstein
print("--- Albert Einstein :")
phrase3 = "LA THEORIE, C EST QUAND ON SAIT TOUT ET QUE RIEN NE FONCTIONNE. LA PRATIQUE, C EST QUAND TOUT FONCTIONNE ET QUE PERSONNE NE SAIT POURQUOI. ICI, NOUS AVONS REUNI THEORIE ET PRATIQUE : RIEN NE FONCTIONNE ET PERSONNE NE SAIT POURQUOI !"
# affiche_frequences(phrase3,Alphabet)
enigme3 = substitution(phrase3,Alphabet,Melange3)
print(enigme3)
# affiche_frequences(enigme3,Minuscules)