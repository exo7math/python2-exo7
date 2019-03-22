
##############################
# Big data
##############################

##############################
# Activité 5 - Classification bayésienne naïve
##############################

from math import *

##############################
## Partie A ##
##############################

##############################
## Question A.1 ##

def moyenne(liste):
    n = len(liste)
    somme = sum(liste)
    if n==0: 
        return 0
    else:
        return somme/n

def variance(liste):
    n = len(liste)
    m = moyenne(liste)
    somme = 0
    for x in liste:
        somme = somme + (x-m)**2
    return somme/n

# Test
print("--- Moyenne, variance ---")
liste = [1,2,3,4,5]
print("liste : ",liste)
print("moyenne :",moyenne(liste)) 
print("variance :",variance(liste))


print("--- Echantillon hommes ---")
# on veut obtenir environ muh = 178, (sigmah = 8), sigma2h = 64
taille_hommes = [172,165,187,181,167,184,168,174,180,186]
print("taille hommes : ",taille_hommes)
print("moyenne :",moyenne(taille_hommes)) 
print("variance :",variance(taille_hommes))
print("écart-type :",sqrt(variance(taille_hommes)))

print("--- Echantillon femmes ---")
# on veut obtenir environ muf = 166, (sigmaf = 7), sigma2f = 49
taille_femmes = [172,156,164,182,171,164,162,170,161,167]
print("taille femmes : ",taille_femmes)
print("moyenne :",moyenne(taille_femmes)) 
print("variance :",variance(taille_femmes))
print("écart-type :",sqrt(variance(taille_femmes)))



##############################
## Question A.2 ##

def densite_gauss(x,mu,sigma2):
    p =  1/sqrt(2*pi*sigma2)*exp( -1/2 * (x-mu)**2 / sigma2 )
    return p

# Test 
print("--- Fonction de densité de la loi normale ---")
mu = 178         # moyenne
sigma2 = 64      # variance (= écart-type au carré)
x = 183
print(densite_gauss(x,mu,sigma2))


##############################
## Question A.3 ##

# Valeur taille homme/femme
muh = 178         # moyenne
sigma2h = 64      # variance
muf = 166         # moyenne
sigma2f = 49      # variance


def homme_ou_femme(taille):
    ph = densite_gauss(taille,muh,sigma2h)
    pf = densite_gauss(taille,muf,sigma2f)
    print('--- Homme ou femme ? ---')
    print('--- Taille donnée :',x)
    print("Probabilité homme ",'{0:.8f}'.format(ph))
    print("Probabilité femme ",'{0:.8f}'.format(pf))
    if ph>pf:
        print("C'est plus probablement un homme.")
    else:
        print("C'est plus probablement une femme.") 
    return

# Test 
print("--- Homme ou femme par la taille ---")
taille = 170
homme_ou_femme(taille) 


##############################
## Question A.4 ##

print("--- Echantillon hommes ---")
# mu_taille_h = 178 cm, (sigma_taille_h = 8), sigma2_taille_h = 64
# mu_poids_h = 75 kg, (sigma_poids_h = 10), sigma2_poids_h = 100
hommes = [(172,68),(165,71),(187,85),(181,73),(167,75),(184,93),(168,67),(174,83),(180,70),(186,73)]
taille_hommes = [x for x,y in hommes]
mu_taille_h = moyenne(taille_hommes)
sigma2_taille_h = variance(taille_hommes)

# print("liste tailles: ",taille_hommes)
# print("moyenne :",moyenne(taille_hommes)) 
# print("variance :",variance(taille_hommes))
# print("écart-type :",sqrt(variance(taille_hommes)))

poids_hommes = [y for x,y in hommes]
mu_poids_h = moyenne(poids_hommes)
sigma2_poids_h = variance(poids_hommes)
# print("liste poids: ",poids_hommes)
# print("moyenne :",moyenne(poids_hommes)) 
# print("variance :",variance(poids_hommes))
# print("écart-type :",sqrt(variance(poids_hommes)))


print("--- Echantillon femmes ---")
# mu_taille_f = 166 cm, (sigma_taille_f = 7), sigma2_taille_f = 49
# mu_poids_f = 63 kg, (sigma_poids_f = 10), sigma2_poids_f = 100
femmes = [(172,66),(156,57),(164,48),(182,71),(171,55),(164,68),(162,52),(170,68),(161,76),(167,67)]
taille_femmes = [x for x,y in femmes]
mu_taille_f = moyenne(taille_femmes)
sigma2_taille_f = variance(taille_femmes)

# print("liste tailles: ",taille_femmes)
# print("moyenne :",moyenne(taille_femmes)) 
# print("variance :",variance(taille_femmes))
# print("écart-type :",sqrt(variance(taille_femmes)))

poids_femmes = [y for x,y in femmes]
mu_poids_f = moyenne(poids_femmes)
sigma2_poids_f = variance(poids_femmes)

# print("liste poids: ",poids_femmes)
# print("moyenne :",moyenne(poids_femmes)) 
# print("variance :",variance(poids_femmes))
# print("écart-type :",sqrt(variance(poids_femmes)))

def homme_ou_femme_bis(taille,poids):
    p_taille_h = densite_gauss(taille,mu_taille_h,sigma2_taille_h)
    p_poids_h = densite_gauss(poids,mu_poids_h,sigma2_poids_h)
    p_taille_f = densite_gauss(taille,mu_taille_f,sigma2_taille_f)
    p_poids_f = densite_gauss(poids,mu_poids_f,sigma2_poids_f)  
    ph = p_taille_h*p_poids_h
    pf = p_taille_f*p_poids_f  
    print('--- Homme ou femme ? ---')
    print('--- Taille donnée :',x)
    print("Probabilité homme ",ph)
    print("Probabilité femme ",pf)
    if ph>pf:
        print("C'est plus probablement un homme.")
    else:
        print("C'est plus probablement une femme.") 
    return

# Test 
print("--- Homme ou femme par la taille et le poids ---")
taille = 176
poids = 64
homme_ou_femme_bis(taille,poids) 


##############################
## Partie B ##
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