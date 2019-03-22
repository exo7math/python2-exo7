##############################
# Cours - Dictionnaire avec Python
##############################

# Dictionnaire identifiant/mot de passe
dico = {'jean':'rev1789', 'adele':'azerty', 'jasmine':'c3por2d2'}
print("Mot de passe de 'adele' :", dico['adele'])
print("Dictionnaire :",dico)

# Ajout d'une entrée
dico['lola'] = 'abcdef'
print("Dictionnaire :",dico)

# Modification d'une entrée
dico['adele'] = 'vwxyz'

print("Dictionnaire :",dico)

# Parcours
for prenom in dico:
    print(prenom + " a pour mot de passe " + dico[prenom])

# dico = {cle1:valeur1, cle2:valeur2,...}
# dico[cle]
# dico[cle] = valeur
# len(dico)
# for cle in dico:
# if cle in dico:
# dico = {}

# dico.keys()
# dico.values()
# for cle, valeur in dico.items():     

# Activité pour apprendre les dictionnaire

##############################
# Activité - Dictionnaire avec Python
##############################

##############################
## Question 1 ##

print("--- Dictionnaire - question 1 ---")

## Question 1.a ##
# Reprends le dictionnaire des mots de passe précédent et ajouter 'angela' avec le mot de passe 'qwerty'. 
# Afficher le nouveau dictionnaire et sa longueur.
dico['angela'] = 'qwerty'

# Test
print("Dictionnaire :",dico)
print("Nombre d'entrées :",len(dico))

## Question 1.b ##

# Programme une fonction qui affiche soit "untel a pour mot de passe ..." ou bien "untel n'a pas de mot passe".
# Indication "if cle in dico:"
def affiche_mot_de_passe(prenom):
    if prenom in dico:
        print(prenom + " a pour mot de passe " + dico[prenom])
    else:
        print(prenom + " n'a pas mot de passe !")
    return

# Test
affiche_mot_de_passe('jean')
affiche_mot_de_passe('toto')


##############################
## Question 2 ##

print("--- Dictionnaire - question 2 ---")


## Question 2.a ##
# Définis un dictionnaire des prénoms/âges. Note que lon' peut avoir deux valeurs identiques, mais deux clés identiques (d'où 'paul1' et 'paul2').
dico = {'zoe':7,'paul1':5,'zack':8,'eva':7,'paul2':6}


## Question 2.2 ##
# Programme une boucle qui calcule la somme des âges, puis la moyenne des âges.

somme = 0
for prenom in dico:
    somme = somme + dico[prenom]
n = len(dico)
moyenne = somme/n
print("Moyenne :",moyenne)


##############################
## Question 3 ##

print("--- Dictionnaire - question 3 ---")


## Question 3.a ##

# Pars d'un dictionnaire vide, puis définis un dictionnaire matière/liste de notes.


# Notes
notes = {}  # Dictionnaire vide
notes['maths'] = [13,15]
notes['anglais'] = [16,12,14]
notes['sport'] = [17]

## Question 3.b ##

# Nouvelle matière 'phyton'/18 et 17
notes['python'] = [18,17]

## Question 3.c ##

# Nouvelle note en maths : 16
notes['maths'].append(16)


## Question 3.d ##

# Crée un dictionnaire note_max qui contient pour chaque matière la note maximale.
# Pars d'un dictionnaire vide, parcours le dictionnaires 'notes' et remplis le dictionnaires 'note_max' 


# Note maximale dans chaque matière
note_max = {}
for matiere in notes:
    note_max[matiere] = max(notes[matiere])
print("Notes :",notes)
print("Notes maximales :",note_max)





