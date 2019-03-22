
##############################
# Calculs en parallèle
##############################

##############################
# Activité 2 - Doublons
##############################

##############################
## Indéxation ##

# Première méthode par indexation

# Liste d'entiers de 0 à 99
liste = [59, 72, 8, 37, 37, 8, 21, 22, 37, 59]

def enlever_tous_doublons(liste):
    """ Ne garde qu'un exemplaire des éléments d'une liste """
    nouv_liste = []  # future liste sans doublons
    table = [0]*100  # liste de 100 zéros
    for i in liste:
        if table[i] == 0:  # si élément x pas déjà retenu
            table[i] = 1   # on le note
            nouv_liste += [i]  # et on le rajoute 

    return nouv_liste


# Test
print("--- Doublons : indexation ---")
print(enlever_tous_doublons(liste))


##############################
## Hachage ##

# Seconde méthode : table de hachage

print("--- Doublons : hachage ---")

##############################
## Question 1 ##

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(ALPHABET)

def hachage(mot,p):
    """ Une fonction de hachage d'un mot modulo p """
    hach = 0
    i = 0
    for c in mot:
        k = ALPHABET.index(c)
        hach = (hach + k*26**i) % p  # mieux avec pow(26,i,p) du module math
        i = i + 1
    return hach

# Test
print("--- Hachage ---")
p = 11
print('p =',p)
print(hachage('LAPIN',p))
print(hachage('CHAT',p))
print(hachage('CHIEN',p))
print(hachage('TORTUE',p))
print(hachage('SINGE',p))
print(hachage('',p))


##############################
## Question 2 ##

def enlever_des_doublons(liste,p):
    """ Retire certains doublons d'une liste en utilisant le hachage des mots modulo p """

    nouv_liste = []  # future liste avec moins de doublons
    table = ['']*p    # liste de p zéros
    for mot in liste:
        hach = hachage(mot,p)
        if table[hach] == '':  # si élément mot pas déjà retenu
            table[hach] = mot   # on le note au rang du hachage
            nouv_liste += [mot] # et on le rajoute
        else:                 
            if mot != table[hach]:   # dans le cas mot différent avec même hash
                nouv_liste += [mot]  # on le rajoute

    return nouv_liste

print("--- Doublons : une passe ---")
liste = ['AA','BB','CC','AA','LAPIN','CHAT','CHIEN','AA','BB','CC','AA','LAPIN','CHAT','CHIEN']
liste = ['LAPIN','CHAT','ZEBRE','CHAT','CHIEN','TORTUE','CHIEN','SINGE','SINGE','CHAT','CHAT','CHIEN']
liste = ['CHIEN','LAPIN','CHIEN','SINGE','SINGE']

print(liste)
print(enlever_des_doublons(liste,10))


##############################
## Question 3 ##

def iterer_enlever_des_doublons(liste,nb_iter=3):
    """ Itération pour enlever plus de doublons """
    p = 2*len(liste)
    for i in range(nb_iter):
        liste = enlever_des_doublons(liste,p)
        p = p+1
    return liste

print("--- Doublons : itération ---")
# liste = ['CHIEN','LAPIN','CHIEN','SINGE','SINGE']
liste = ['LAPIN','CHAT','ZEBRE','CHAT','CHIEN','TORTUE','CHIEN','SINGE','SINGE','CHAT','CHAT','CHIEN']
print(liste)
print(iterer_enlever_des_doublons(liste,2))

