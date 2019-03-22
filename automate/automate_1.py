
##############################
# Automates
##############################

##############################
# Activité 1 - Une suite logique
##############################

# Programmation de la suite logique :
# 1
# 11
# 21
# 1211
# 111221
# 312211
# 13112221

# Une suite logique

def lecture(mot):
    """ Calcule la lecture du mot """

    carac_prec = ""
    nb = 0

    nouv_mot = ""

    for carac in mot:
        if (carac_prec == "") or (carac == carac_prec):
            nb = nb + 1
        else:
            nouv_mot = nouv_mot + str(nb) + carac_prec
            nb = 1

        carac_prec = carac

    # Fin
    nouv_mot = nouv_mot + str(nb) + carac_prec

    return nouv_mot


# Pour la répétition
def itere(n,mot):
    """ Répète n lectures """

    for __ in range(n):
        print(mot)
        mot = lecture(mot)
    return mot


# Test
print("--- Suite logique ---")

mot = "112"
print("Le mot suivant de",mot,"est", lecture(mot))

print("En partant de 1 on obtient :")
itere(12,"1")
