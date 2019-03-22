
##############################
# Matrice
##############################



##############################
# Activité 1 - Convolution de matrices
##############################

##############################
## Question 1 ##

def afficher_matrice(M):
    """ Affichage propre d'une matrice dans la console """
    n = len(M)     # Nb de lignes
    p = len(M[0])  # Nb de colonnes
    for ligne in M:
        for x in ligne:
            if isinstance(x,int):
                print('{:3d}'.format(x),end=" ")
            else:
                print('{0:.3f}'.format(x),end=" ")
        print()
    return


# Test
print("--- Afficher une matrice ---")
M = [[1,2,3], [4,5,6], [7,8,9]]
afficher_matrice(M)


##############################
## Question 2 ##

def element_convolution(C,M):
    """ Calcul de l'élément de convolution d'une matrice 3x3 
    sur une matrice 3x3. Le résultat est un nombre """

    n = len(C)     # Nb de lignes
    p = len(C[0])  # Nb de colonnes    
    conv = 0
    for i  in range(n):
        for j in range(p):
            conv += C[i][j]*M[i][j]
    return conv

# Test
print("--- Convolution ---")
C = [[1,1,1], [1,5,1], [1,1,1]]
M = [[1,2,3], [4,5,6], [7,8,9]]
print(element_convolution(C,M))


##############################
## Question 3 ##

def convolution(C,M):
    """ Calcul de la matrice de convolution. 
    C est une matrice 3x3 qui agit sur M matrice nxp.
    Le résultat est une matrice nxp """

    n = len(M)     # Nb de lignes
    p = len(M[0])  # Nb de colonnes
    N = [[0 for j in range(p)] for i in range(n)]
    for i in range(n):
        for j in range(p):
            MM = [  [ M[(i-1)%n][(j-1)%p], M[(i-1)%n][j], M[(i-1)%n][(j+1)%p] ],
                    [ M[i][(j-1)%p],  M[i][j],  M[i][(j+1)%p] ],
                    [ M[(i+1)%n][(j-1)%p], M[(i+1)%n][j], M[(i+1)%n][(j+1)%p] ] ]

            N[i][j] = element_convolution(C,MM)
    return N

# Test
print("--- Convolution ---")
C = [[0,1,0], [0,0,0], [0,0,0]]
# C = [[0,1,0], [1,2,1], [0,1,0]]
M = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]


print(" C = ")
afficher_matrice(C)
print(" M = ")
afficher_matrice(M)
N = convolution(C,M)
print(" N = ")
afficher_matrice(N)


##############################
## Question 3 ##

def convolution_entiere(C,M):
    """ Comme convolution() 
    C matrice 3x3, M matrice nxp
    mais matrice résultat à coeff entiers, entre 0 et 255 """

    n = len(M)     # Nb de lignes
    p = len(M[0])  # Nb de colonnes
    N = convolution(C,M)
    NN = [[0 for j in range(p)] for i in range(n)]
    for i  in range(n):
        for j in range(p):
            conv = N[i][j]
            conv = round(conv)
            conv = max(0,conv)
            conv = min(255,conv)
            NN[i][j] = conv
    return NN

# Test
print("--- Convolution entière ---")
C = [[0,-1/2,0],[-1/2,3,-1/2],[0,-1/2,0]]

M = [[101,102,103,104],[201,151,101,51],[50,100,150,200]]
print(" C = ")
afficher_matrice(C)
print(" M = ")
afficher_matrice(M)
N = convolution_entiere(C,M)
print(" N = ")
afficher_matrice(N)
NN = convolution(C,M)
print(" NN = ")
afficher_matrice(NN)

##############################
# Activité 2 - Lire et écrire des images
##############################


##############################
## Question 1 ##

def pgm_vers_matrice_simple(fichier):
    """ Lit un fichier image au format pgm (format simple) et renvoie une matrice """

    # Fichier à lire
    fic_in = open(fichier,"r")

    i = 0  # Numéro de ligne du fichier
    matrice = []
    for ligne in fic_in:
        if i >= 3:
            liste_str = ligne.split()
            liste = [int(x) for x in liste_str]
            matrice += [liste]
        i = i + 1

    # Fermeture des fichiers
    fic_in.close()
    return matrice

# Test
print("--- Fichier pgm vers matrice (basique) ---")
M = pgm_vers_matrice_simple("exemple_image.pgm")
afficher_matrice(M)

##############################
## Question 1 ##

def pgm_vers_matrice(fichier):
    """ Lit un fichier image au format pgm (format qcq) et renvoie une matrice """

    # Fichier à lire
    fic_in = open(fichier,"r")

    i = 0  # Numéro de ligne du fichier (sans compter les lignes commentées)
    matrice = []  # Pour la matrice finale
    ligne_matrice = []    # Pour une ligne de la matrice
    for ligne in fic_in:
        if '#' in ligne: 
            continue              # On zappe les lignes commentées (i n'augmente pas)

        if i == 1:            # Taille de l'image
            liste_ligne = ligne.split()
            p = int(liste_ligne[0])
            n = int(liste_ligne[1])

        if i >= 3:
            liste_str = ligne.split()
            liste = [int(x) for x in liste_str]

            while len(liste)>0 :
                while len(liste)>0 and len(ligne_matrice) < p:
                    ligne_matrice += [liste.pop(0)]
                if len(ligne_matrice) == p:
                    matrice += [ligne_matrice]
                    ligne_matrice = []

        i = i + 1

    # Fermeture des fichiers
    fic_in.close()
    return matrice

# Test
print("--- Fichier pgm vers matrice (new) ---")
# M = pgm_vers_matrice("exemple_image.pgm")
M1 = pgm_vers_matrice("cours-matrice-pgm-1.pgm")
M2 = pgm_vers_matrice("cours-matrice-pgm-2.pgm")
M3 = pgm_vers_matrice("cours-matrice-pgm-3.pgm")
print("M1")
afficher_matrice(M1)
print("M2")
afficher_matrice(M2)
print("M3")
afficher_matrice(M3)


##############################
## Question 2 ##

def matrice_vers_pgm(M,fichier):
    """ Ecrit une matrice dans un fichier au format pgm """
    fic_out = open(fichier,"w")

    # Entête du fichier pgm
    n = len(M)     # Nb de lignes
    p = len(M[0])  # Nb de colonnes
    fic_out.write("P2\n")  # Image en niveaux de gris
    fic_out.write(str(p) + " " + str(n) + "\n")  # Nb de colonnes et de lignes
    fic_out.write("255\n")  # Niveaux de gris 
    for ligne in M:
        for x in ligne:
            fic_out.write('{:4d}'.format(x))
        fic_out.write('\n')

    fic_out.close()
    return

# Test
print("--- Matrice vers fichier pgm ---")
M = [[101,102,103],[104,105,106],[107,108,109]]
matrice_vers_pgm(M,"export_image.pgm")
MM = pgm_vers_matrice("export_image.pgm")
print('Avant, M = ')
afficher_matrice(M)
print('Après, M = ')
afficher_matrice(MM)

# Test
print("--- Matrice vers fichier pgm (exemple réel) ---")
M = pgm_vers_matrice("input/monde.pgm")
# afficher_matrice(M)
matrice_vers_pgm(M,"output/monde_export.pgm")


##############################
# Activité 3 - Convolution et image
##############################

##############################
## Question 1 ##

def convolution_image(C,fichier_in,fichier_out):
    """ Fait la convolution de la matrice C sur l'image du fichier d'entrée. 
    Le résultat est une image transformée écrite dans le fichier de sortie """
    M = pgm_vers_matrice(fichier_in)
    N = convolution_entiere(C,M)
    matrice_vers_pgm(N,fichier_out)
    return

# Test
print("--- Convolution sur image ---")

## Flou ## 
C = [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]           # flou classique
# C = [[1/16,2/16,1/16],[1/16,4/16,2/16],[1/16,2/16,1/16]]  # flou gaussien

# convolution_image(C,'exemple_image.pgm','exemple_image_conv.pgm')

# convolution_image(C,'input/chat.pgm','output/chat_conv_flou.pgm')
# convolution_image(C,'input/colonnes.pgm','output/colonnes_conv_flou.pgm')
# convolution_image(C,'input/totem.pgm','output/totem_conv_flou.pgm')
# convolution_image(C,'input/renne.pgm','output/renne_conv_flou.pgm')
# convolution_image(C,'input/monde.pgm','output/monde_conv_flou.pgm')

## Bord ##
C = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
# C = [[0,1,0],[1,-4,1],[0,1,0]]
# C = [[1,0,-1],[0,0,0],[-1,0,1]]

# convolution_image(C,'input/chat.pgm','output/chat_conv_bord.pgm')
# convolution_image(C,'input/colonnes.pgm','output/colonnes_conv_bord.pgm')
# convolution_image(C,'input/totem.pgm','output/totem_conv_bord.pgm')
# convolution_image(C,'input/renne.pgm','output/renne_conv_bord.pgm')
# convolution_image(C,'input/monde.pgm','output/monde_conv_bord.pgm')


## Piqué ##
C = [[0,-1,0],[-1,5,-1],[0,-1,0]]
# convolution_image(C,'input/chat.pgm','output/chat_conv_pique.pgm')
# convolution_image(C,'input/colonnes.pgm','output/colonnes_conv_pique.pgm')
# convolution_image(C,'input/totem.pgm','output/totem_conv_pique.pgm')
# convolution_image(C,'input/renne.pgm','output/renne_conv_pique.pgm')
# convolution_image(C,'input/monde.pgm','output/monde_conv_pique.pgm')


## Estampé ##
C = [[-2,-1,0],[-1,1,1],[0,1,2]]
# convolution_image(C,'input/chat.pgm','output/chat_conv_estampe.pgm')
# convolution_image(C,'input/colonnes.pgm','output/colonnes_conv_estampe.pgm')
# convolution_image(C,'input/totem.pgm','output/totem_conv_estampe.pgm')
# convolution_image(C,'input/renne.pgm','output/renne_conv_estampe.pgm')
# convolution_image(C,'input/monde.pgm','output/monde_conv_estampe.pgm')



##############################
## Question 2 ##

def decalage_haut_image(k,fichier_in,fichier_out):
    """ Translate une image vers le haut de k pixels """

    M = pgm_vers_matrice(fichier_in)
    C = [[0,0,0],[0,0,0],[0,1,0]]
    for __ in range(k):
        M = convolution_entiere(C,M)
    matrice_vers_pgm(M,fichier_out)
    return

# Test
print("--- Convolution sur image ---")
# decalage_haut_image(15,'input/chat.pgm','output/chat_conv_decal.pgm')
# decalage_haut_image(75,'input/monde.pgm','output/monde_conv_decal.pgm')

## Commande bash pour conversion simple pgm vers png :
## convert toto.pgm toto.png
## Conversion multiple :
## for fic in $(ls *.pgm); do convert "$fic" $(basename $fic .pgm).png; done


##############################
# Activité 4 - Transformation 
##############################

from math import *

##############################
## Question 1 ##

def dilatation_matrice(kx,ky,M):
    """ Agrandit une matrice selon la direction horizontale (facteur kx)
    et verticale (facteur ky) """

    # kx,ky entiers
    n = len(M)     # Nb de lignes
    p = len(M[0])  # Nb de colonnes
    N = [[0 for j in range(kx*p)] for i in range(ky*n)]
    for i  in range(ky*n):
        for j in range(kx*p):
            N[i][j] = M[i//ky][j//kx]
    return N

# Test
print("--- Dilatation ---")
M = [[1,2,3],[4,5,6],[7,8,9]]
print(" M = ")
afficher_matrice(M)
N = dilatation_matrice(3,2,M)
print(" N = ")
afficher_matrice(N)

# Test
print("--- Dilatation sur image ---")
# fichier_in = 'input/chat.pgm'
# fichier_out = 'output/chat_biho.pgm'
# M = pgm_vers_matrice(fichier_in)
# N = dilatation_matrice(2,3,M)
# matrice_vers_pgm(N,fichier_out)


##############################
## Question 2 ##

def vecteur_image(T,x,y):
    """ Image d'un vecteur (x,y) par une matrice T de taille 2x2 """
    a,b,c,d = T[0][0],T[0][1],T[1][0],T[1][1]
    xx = a*x + b*y
    yy = c*x + d*y
    return xx,yy



def inverse_matrice(T):
    """ Inverse de la matrice T de taille 2x2 """
    a,b,c,d = T[0][0],T[0][1],T[1][0],T[1][1]
    det = a*d-b*c
    aa,bb,cc,dd = d/det,-b/det,-c/det,a/det
    Tinv = [[aa,bb],[cc,dd]]
    return Tinv

# Test
print("--- Matrice de transformation ---")
theta = pi/3
Ttheta = [[cos(theta),-sin(theta)],[sin(theta),cos(theta)]]
x,y = 4,5
xx,yy = vecteur_image(Ttheta,x,y)
print("Matrice T(theta) :",Ttheta,"  x,y :",x,y,"  x',y' :",xx,yy)

theta = -pi/3
Tmoinstheta = [[cos(theta),-sin(theta)],[sin(theta),cos(theta)]]
print("Matrice T(-theta) :          ", Tmoinstheta)
print("Matrice inverse de T(theta) :", inverse_matrice(Ttheta))


##############################
## Question 3 ##

def transformation(T,M):
    """ Transformation de la matrice M en faisant agir la matrice T """

    n = len(M)     # Nb de lignes
    p = len(M[0])  # Nb de colonnes

    x1, y1 = vecteur_image(T,0,n)
    x2, y2 = vecteur_image(T,p,n)
    x3, y3 = vecteur_image(T,p,0)

    xmin = round(min(0,x1,x2,x3))
    xmax = round(max(0,x1,x2,x3))
    ymin = round(min(0,y1,y2,y3))
    ymax = round(max(0,y1,y2,y3))

    pp = xmax-xmin
    nn = ymax-ymin

    Tinv = inverse_matrice(T)

    N = [[0 for jj in range(pp)] for ii in range(nn)]
    for ii  in range(nn):
        for jj in range(pp):
            j, i = vecteur_image(Tinv,jj+xmin,ii+ymin)
            j, i = floor(j), floor(i)
            if (0 <= i < n) and (0 <= j < p):
                N[ii][jj] = M[i][j] 
            else:
                N[ii][jj] = 0

    return N


# Test
print("--- Transformation de matrice ---")
T = [[4/3,0],[0,2]]
print(" T = ")
afficher_matrice(T)
M = [[1,2,3],[4,5,6],[7,8,9]]
print(" M = ")
afficher_matrice(M)
N = transformation(T,M)
print(" N = ")
afficher_matrice(N)


# Test 
print("--- Transformation sur image : dilatation ---")
# T = [[pi,0],[0,1]]
# fichier_in = 'input/chat.pgm'
# fichier_out = 'output/chat_dilatation.pgm'
# M = pgm_vers_matrice(fichier_in)
# N = transformation(T,M)
# matrice_vers_pgm(N,fichier_out)

# Test
print("--- Transformation sur image : rotation ---")
# theta = pi/3
# T = [[cos(theta),-sin(theta)],[sin(theta),cos(theta)]]
# fichier_in = 'input/chat.pgm'
# fichier_out = 'output/chat_rotation.pgm'
# M = pgm_vers_matrice(fichier_in)
# N = transformation(T,M)
# matrice_vers_pgm(N,fichier_out)

# Test
print("--- Transformation sur image : symétrie ---")
# T = [[1,0],[0,-1]]
# fichier_in = 'input/chat.pgm'
# fichier_out = 'output/chat_symetrie.pgm'
# M = pgm_vers_matrice(fichier_in)
# N = transformation(T,M)
# matrice_vers_pgm(N,fichier_out)

# Test
print("--- Transformation sur image : quelconque ---")
# T = [[3,1],[1,5]]
# fichier_in = 'input/chat.pgm'
# fichier_out = 'output/chat_transfo.pgm'
# M = pgm_vers_matrice(fichier_in)
# N = transformation(T,M)
# matrice_vers_pgm(N,fichier_out)




##############################
## Question 4 (old) ##

def ajout_bord(M,k,l):
    """ Rajoute des bords """
    n = len(M)     # Nb de lignes
    p = len(M[0])  # Nb de colonnes
    nn = n + 2*k
    pp = n + 2*l

    N = [[0 for j in range(pp)] for ii in range(nn)]
    for ii  in range(nn):
        for jj in range(pp):  
            i = ii - k
            j = jj - l
            if (0 <= i < n) and (0 <= j < p):
                N[ii][jj] = M[i][j] 
            else:
                N[ii][jj] = 0
            
    return N 

# Test
# print("--- Test ---")
# afficher_matrice(T)
# M = [[1,2,3],[4,5,6],[7,8,9]]
# print(" M = ")
# afficher_matrice(M)
# N = ajout_bord(M,1,2)
# print(" N = ")
# afficher_matrice(N)

# Test
# print("--- Test sur image ---")
# T = [[sqrt(3)/2,-1/2],[1/2,sqrt(3)/2]]
# fichier_in = 'input/chat.pgm'
# fichier_out = 'output/chat_transfo.pgm'
# M = pgm_vers_matrice(fichier_in)
# MM = ajout_bord(M,100,200)
# N = transformation(T,MM)
# matrice_vers_pgm(N,fichier_out)


##############################
## Question 5 (old) ##

def transformation_centre(T,M):
    """ Action à partir du centre de l'image """
    n = len(M)     # Nb de lignes
    p = len(M[0])  # Nb de colonnes

    Tinv = inverse_matrice(T)

    N = [[0 for jj in range(p)] for ii in range(n)]
    for ii  in range(n):
        for jj in range(p):
            j, i  = vecteur_image(Tinv,jj-p/2,ii-n/2)
            j, i = floor(j+p/2), floor(i+n/2)
            if (0<= i <n) and (0<= j <p):
                N[ii][jj] = M[i][j] 
            else:

    return N


# Test
# print("--- Test sur image ---")
# # T = [[sqrt(3)/2,-1/2],[1/2,sqrt(3)/2]]
# T = [[1,0],[0,-1]]
# fichier_in = 'input/chat.pgm'
# fichier_out = 'output/chat_transfo.pgm'
# M = pgm_vers_matrice(fichier_in)
# MM = ajout_bord(M,100,200)
# N = transformation_centre(T,MM)
# matrice_vers_pgm(N,fichier_out)