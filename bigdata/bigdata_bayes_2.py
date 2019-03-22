
##############################
# Big data
##############################

##############################
# Activité 6 - Classification bayésienne naïve (suite)
##############################

# Inspiré par un post de Bruno Stecanella
# https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/

titres_sport = [
"un beau match de championnat",
"victoire de Paris en finale",
"défaite à Marseille",
"le coach viré après la finale",
"Paris change de coach"
]

titres_passport = [
"un beau printemps à Paris",
"un robot écrase un chien à Marseille",
"célébration de la victoire de la grande guerre",
"grève finale au lycée"
]

# Sport ou pas ?
phrase = "victoire de Marseille"
# phrase = "un beau chien"
# phrase = "Paris écrase Barcelone en finale"

##############################
## Question B.1 ##

def liste_mots(titres):
    liste = []
    for titre in titres:
        liste = liste + titre.split()
    return liste

mots_sports = liste_mots(titres_sport)
mots_passports = liste_mots(titres_passport)

print(mots_sports)
print(mots_passports)


## Question B.2 ##

def probabilite_mot(mot,liste_mots):
    nb = liste_mots.count(mot)
    nb_total = len(liste_mots)
    # print(mot,nb,nb_total)
    return nb/nb_total

# Test
print("--- Probabilité mot sachant sports (ou pas sport) ---")
mot = "Paris"
p_mot_sport = probabilite_mot(mot,mots_sports)
p_mot_passport = probabilite_mot(mot,mots_passports)
print("mot :",mot)
print("Donc probabilité du mot sachant sport =",p_mot_sport)
print("Donc probabilité du mot sachant pas sport =",p_mot_passport)


## Question B.3 ##

def probabilite_phrase(phrase,liste_mots):
    # Produit des probas de chaque mot
    nb_total = len(liste_mots)
    liste = phrase.split()
    p = 1
    for mot in liste:
        proba_mot = probabilite_mot(mot,liste_mots)
        p = p*proba_mot

    return p

# Test
print("--- Probabilité classique ---")
# phrase = "victoire de Marseille"
# phrase = "un beau chien"
# phrase = "Paris écrase Barcelone en finale"

phrase = "la finale de Paris"
phrase = "le coach perd la finale"


p_sport = probabilite_phrase(phrase,mots_sports)
p_passport = probabilite_phrase(phrase,mots_passports)
print("proba phrase sport =",p_sport)
print("proba phrase pas sport =",p_passport)
# print("Rapport =",p_sport/p_passport)

## Question B.4 ##

def probabilite_mot_bis(mot,liste_mots):
    nb = liste_mots.count(mot) + 1  # on ajoute 1, donc jamais nul
    nb_total = len(liste_mots)
    return nb/nb_total              # c'est plus un vraie proba

def probabilite_phrase_bis(phrase,liste_mots):
    # Produit des probas de chaque mot
    nb_total = len(liste_mots)
    liste = phrase.split()
    p = 1
    for mot in liste:
        proba_mot = probabilite_mot_bis(mot,liste_mots)
        p = p*proba_mot

    return p

# Test
print("--- Probabilité modifiée ---")

p_sport = probabilite_phrase_bis(phrase,mots_sports)
p_passport = probabilite_phrase_bis(phrase,mots_passports)
print("proba phrase sport =",p_sport)
print("proba phrase pas sport =",p_passport)
print("Rapport =",p_sport/p_passport)