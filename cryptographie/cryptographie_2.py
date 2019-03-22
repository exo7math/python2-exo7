
##############################
# Cryptographie
##############################

##############################
# Activité 2 - Substitution mono-alphabétique
##############################

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Génération d'un mélange aléatoire
# from random import *
# liste_lettre = list(Alphabet.lower())
# shuffle(liste_lettre)
# Melange = "".join(liste_lettre)


print("--- Alphabet mélangé ---") 
Melange = "ykcodmfjgzaxrnbutqiphwesvl"
print(Melange)


##############################
## Question 1 ##

def chiffre_substitution_caractere(car):
    """ Calcule la substitution d'une lettre """

    i = Alphabet.index(car)
    car_code = Melange[i]
    return car_code

# Test
print("--- Substitution d'un caractère ---")
print(chiffre_substitution_caractere('A'))


##############################
## Question 2 ##

def chiffre_substitution_phrase(phrase):
    """" Chiffre une phrase par substitution """

    phrase_codee = ""
    for car in phrase:
        if car not in Alphabet:
            phrase_codee += car
        else:
            car_code = chiffre_substitution_caractere(car)
            phrase_codee += car_code
    return phrase_codee


# Test
print("--- Chiffrement par substitution ---")
phrase = "PAS DE POTION POUR OBELIX !"
phrase_codee = chiffre_substitution_phrase(phrase)
print(phrase)
print(phrase_codee)

# Cours
phrase = "BONJOUR"
phrase_codee = chiffre_substitution_phrase(phrase)
print(phrase)
print(phrase_codee)

phrase = "AVE CESAR"
phrase_codee = chiffre_substitution_phrase(phrase)
print(phrase)
print(phrase_codee)

##############################
## Question 3 ##

def dechiffre_substitution_caractere(car):
    """ Calcule la substitution inverse d'une lettre """

    i = Melange.index(car)
    car_decode = Alphabet[i]
    return car_decode


def dechiffre_substitution_phrase(phrase):
    """" Déchiffre une phrase par substitution """

    phrase_decodee = ""
    for car in phrase:
        if car not in Melange:
            phrase_decodee += car
        else:
            car_decode = dechiffre_substitution_caractere(car)
            phrase_decodee += car_decode
    return phrase_decodee


# Test
print("--- Déchiffrement d'une phrase codée par substitution ---")

phrase_decodee = dechiffre_substitution_phrase(phrase_codee)
print(phrase_codee)
print(phrase_decodee)


exit()

##############################
## Question 4 ##

def attaque_cesar(phrase):
    """ Affichage de toutes les possibilités """

    for k in range(26):
        print(k,chiffre_cesar_phrase(phrase,-k))

    return

print("--- Attaque de César ---")
phrase = "PANORAMIX N A PLUS DE POTION"
phrase_codee = chiffre_cesar_phrase(phrase,18)
print(phrase_codee)
print("Attaque :")
attaque_cesar(phrase_codee)
