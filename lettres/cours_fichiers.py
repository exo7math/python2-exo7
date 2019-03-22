# Ecrire un fichier
fic = open("mon_fichier.txt","w")

for i in range(100):
    ligne = "Ligne numéro " + str(i) + "\n"
    fic.write(ligne)

fic.close()

# Lire un fichier
fic = open("mon_fichier.txt","r")

for ligne in fic:
    print(ligne.strip())

fic.close()