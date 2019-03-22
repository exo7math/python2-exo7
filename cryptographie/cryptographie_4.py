
##############################
# Cryptographie
##############################

##############################
# Activité 4 - Le chiffrement de Vigenère
##############################

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

##############################
## Question 1 ##

def chiffre_vigenere(phrase,cle):
    """" Chiffre une phrase par un décalage de Vigenère """

    phrase_codee = ""
    rang = 0
    n = len(cle)
    for car in phrase:
        if car not in Alphabet:
            phrase_codee += car
        else:
            i = Alphabet.index(car)
            j = (i+cle[rang]) % 26            
            car_code = Alphabet[j]
            phrase_codee += car_code
            rang = (rang + 1) % n
    return phrase_codee


# Test
print("--- Chiffrement de Vigenère ---")
phrase = "AAA ABC"
phrase_codee = chiffre_vigenere(phrase,[1,2,3])
print(phrase)
print(phrase_codee)

# Cours
phrase = "IL ETAIT UNE FOIS"
phrase = "ILE TAI TUN EFO IS"
phrase_codee = chiffre_vigenere(phrase,[4,2,3])
print(phrase)
print(phrase_codee)

# Cours
phrase = "MILOU ET TINTIN"
phrase_codee = chiffre_vigenere(phrase,[4,2,3])
print(phrase)
print(phrase_codee)

##############################
## Question 2 ##

phrase = "LE PROBLEME EN CE BAS MONDE EST QUE LES IMBECILES SONT SURS ET FIERS D EUX ALORS QUE LES GENS INTELLIGENTS SONT EMPLIS DE DOUTES"
cle = [18,7,10,16]
phrase_codee = chiffre_vigenere(phrase,cle)
print(phrase)
print(phrase_codee)