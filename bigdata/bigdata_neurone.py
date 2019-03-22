
##############################
# Big data II 
##############################

##############################
# Activité 4 - Neurone
##############################

# Un neurone : 3 coeff réels
p1 = 1
p2 = 0.2
p3 = 0.2
neurone = [p1,p2,p3]

# le seuil vaut 1 : seuil = 1

# vitesse d'apprentissage 
epsilon = 0.2

# Une entrée : 3 réels [r,g,b] entre 0 et 1
entree = [1,1,1]

##############################
## Question 1 ##

def activation(neurone,entree):
    p1,p2,p3 = neurone
    e1,e2,e3 = entree
    q = p1*e1 + p2*e2 + p3*e3
    if q >= 1:
        sortie = 1
    else:
        sortie = 0
    return sortie

# Test
print("--- Activation (ou pas) ---")
p1 = 1
p2 = 2
p3 = 3
# neurone = [2,-2,-2]
# entree = [0,1,0]
# entree = [0,0,1]
# Pour les exemples 
neurone, entree = [1,2,3], [0.5,0,0]
neurone, entree = [1,2,3], [0,1,0.5]

neurone, entree = [1,0.5,2], [0.2,0.1,0.1]
neurone, entree = [1,0.5,2], [0.3,0.2,0.7]
print(activation(neurone,entree))


######################################
## Question 2 ##

def apprentissage(neurone,entree,objectif):
    p1,p2,p3 = neurone
    e1,e2,e3 = entree

    # epsilon = 0.2

    sortie = activation(neurone,entree)

    if sortie == objectif:
        nouv_neurone = list(neurone)
    else:
        pp1 = p1 + epsilon * (objectif-sortie)*e1
        pp2 = p2 + epsilon * (objectif-sortie)*e2
        pp3 = p3 + epsilon * (objectif-sortie)*e3
        nouv_neurone = [pp1,pp2,pp3]

    return nouv_neurone

# Test
print("--- Apprentissage pas à pas ---")


# Cas où objectif atteint : on garde le neurone inchangé
neurone = [1,1,1]
entree = [1,0,2]
objectif = 1
print(neurone)
neurone = apprentissage(neurone,entree,objectif)
print(neurone)

# Cas où objectif atteint : on garde le neurone inchangé
neurone = [1,1,1]
entree = [0.5,0.1,0.2]
objectif = 0
print(neurone)
neurone = apprentissage(neurone,entree,objectif)
print(neurone)

# Cas où objectif pas atteint : on change le neurone
neurone = [1,1,1]
entree = [0,1,1]
objectif = 0
print(neurone)
neurone = apprentissage(neurone,entree,objectif)
print(neurone)  # Le neurone a changé

# Cas où objectif pas atteint : on change le neurone
neurone = [1,1,1]
entree = [0.5,0.2,0]
objectif = 1
print(neurone)
neurone = apprentissage(neurone,entree,objectif)
print(neurone)  # Le neurone a changé

# On peut itérer :
neurone = apprentissage(neurone,entree,objectif)
print(neurone)  # Le neurone a encore changé


# neurone = apprentissage(neurone,[0.9,0.9,0],0)
# print(neurone)
# neurone = apprentissage(neurone,[1,1,1],0)
# print(neurone)
# neurone = apprentissage(neurone,[0,1,1],0)
# print(neurone)
# neurone = apprentissage(neurone,[0,0,1],0)
# print(neurone)
# neurone = apprentissage(neurone,[0.9,0.9,0],0)
# print(neurone)
# neurone = apprentissage(neurone,[1,1,1],0)
# print(neurone)
# neurone = apprentissage(neurone,[0,0,1],0)
# print(neurone)
# neurone = apprentissage(neurone,[0.9,0.9,0],0)
# print(neurone)
# neurone = apprentissage(neurone,[1,1,1],0)
# print(neurone)

# neurone = apprentissage(neurone,[0.9,0.1,0],1)
# print(neurone)
# neurone = apprentissage(neurone,[1,0,0],1)
# print(neurone)
# neurone = apprentissage(neurone,[1,0,0],1)
# print(neurone)


######################################
## Question 3 ##

def epoque_apprentissage(neurone_init,liste_entrees_objectifs):
    neurone = list(neurone_init)
    for entree,objectif in liste_entrees_objectifs:
        # print(entree,"neurone avant",neurone)
        neurone = apprentissage(neurone,entree,objectif)
        # print(" -> neurone après",neurone)
    return neurone


# Test
print("--- Apprentissage automatique ---")

neurone_init = [1,1,1]
liste_entrees_objectifs = [
([1,0,0],1),
([0,1,1],0),
([1,1,0],0),
([1,0,0.2],1),
([0,1,0],0),
([0,0,0],0),
([1,0,1],0),
([0.7,0,0],1),
([0.5,0.5,0.5],0),
([0.9,0.2,0],1),
([0.9,0,0],1),
([1,1,1],0),
([0.2,1,0],0),
([0.8,0.2,0],1),
([0.7,0.1,0.1],1)
]

print(neurone_init)
neurone = list(neurone_init)
for __ in range(10):
    neurone = epoque_apprentissage(neurone,liste_entrees_objectifs)
    print(neurone)


# Vérification du neurone
print("=== Vérification ===")
neurone = [1.66,-0.78,-0.66]  # donner par apprentissagege ci-dessus
liste_couleurs = [ [0.9,0,0], [1,0.2,0.2], [0,0,1], [1,0.5,0], [0.3,0.3,0.3], [0.7,0.5,0.4] ]
p1,p2,p3 = neurone
for couleur in liste_couleurs:
    e1,e2,e3 = couleur
    q = p1*e1 + p2*e2 + p3*e3
    print("couleur = ",couleur)
    print("q =",q)
    print("rouge ?",activation(neurone,couleur))

