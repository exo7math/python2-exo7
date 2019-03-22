
##############################
# Cryptographie
##############################

##############################
# Activité 1 - Le chiffre de César
##############################

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

##############################
## Question 1 ##


def chiffre_cesar_caractere(car,k):
    """ Calcule le décalage de k lettres """

    i = Alphabet.index(car)
    j = (i+k) % 26
    car_code = Alphabet[j]
    return car_code

# Test
print("--- Codage d'un caractère ---")
print(chiffre_cesar_caractere('A',3))


##############################
## Question 2 ##

def chiffre_cesar_phrase(phrase,k):
    """" Chiffre une phrase par un décalage de k lettres """

    phrase_codee = ""
    for car in phrase:
        if car not in Alphabet:
            phrase_codee += car
        else:
            car_code = chiffre_cesar_caractere(car,k)
            phrase_codee += car_code
    return phrase_codee


# Test
print("--- Chiffre de César ---")
phrase = "CAPTUREZ IDEFIX !"
phrase_codee = chiffre_cesar_phrase(phrase,3)
print(phrase)
print(phrase_codee)

# Pour le cours 
phrase = "BLOQUEZ ASTERIX"
phrase_codee = chiffre_cesar_phrase(phrase,3)
print(phrase)
print(phrase_codee)

phrase = "OU EST PANORAMIX"
phrase_codee = chiffre_cesar_phrase(phrase,10)
print(phrase)
print(phrase_codee)



##############################
## Question 3 ##

def dechiffre_cesar_phrase(phrase,k):
    """" Déchiffre une phrase par un décalage de k lettres à rebours """   
    return chiffre_cesar_phrase(phrase,-k)

# Test
print("--- Déchiffrement de César ---")

phrase_decodee = dechiffre_cesar_phrase(phrase_codee,3)
print(phrase_codee)
print(phrase_decodee)


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

