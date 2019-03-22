
##############################
# Tri
##############################

##############################
# Activité 1 - Tri par sélection
##############################

def tri_selection(liste):
    """ Ordonne la liste du plus petit au plus grande.
    Méthode : tri par sélection """
    cliste = list(liste)
    n = len(cliste)

    for i in range(n):
        rg_min = i
        for j in range(i+1,n):
            if cliste[j] < cliste[rg_min]:
                rg_min = j

        if rg_min != i:  # alors échange
            cliste[i], cliste[rg_min] = cliste[rg_min], cliste[i]

    return cliste

# Test
liste = [4,3,2,1,6,5]
print(liste)
print(tri_selection(liste))


##############################
# Activité 2 - Tri par insertion
##############################

def tri_insertion(liste):
    """ Ordonne la liste par la méthode du tri par insertion """
    cliste = list(liste)
    n = len(cliste)

    for i in range(1,n):
        el = cliste[i]
        j = i
        while (j>0) and (cliste[j-1]>el):
            cliste[j] = cliste[j-1]
            j = j-1

        cliste[j] = el

    return cliste

# Test
liste = [4,3,2,1]
print(liste)
print(tri_insertion(liste))


##############################
# Activité 3 - Tri à bulles
##############################

def tri_a_bulles(liste):
    """ Ordonne la liste par le tri à bulles """
    cliste = list(liste)
    n = len(cliste)

    for i in range(n-1,-1,-1):
        for j in range(i):
            if cliste[j+1] < cliste[j]:
                cliste[j], cliste[j+1] = cliste[j+1], cliste[j]

    return cliste

# Test
liste = [4,3,2,1]
print(liste)
print(tri_a_bulles(liste))




##############################
# Activité 4 - Tri fusion
##############################

# def fusion_recursive(liste_g,liste_d):
#     if len(liste_g)==0: return liste_d
#     if len(liste_d)==0: return liste_g
#     if liste_g[0] <= liste_d[0]:
#         liste_fus = [liste_g[0]] + fusion_recursive(liste_g[1:],liste_d)
#     else:
#         liste_fus = [liste_d[0]] + fusion_recursive(liste_g,liste_d[1:])
#     return liste_fus

# # Test
# print("--- Fusion récursive ---")
# liste_g = [1,4,7]
# liste_d = [2,5,6,9]
# print(liste_g,liste_d)
# print(fusion_recursive(liste_g,liste_d))


def fusion(liste_g,liste_d):
    """ Fusionne et ordonne deux listes déjà ordonnées """
    n, m = len(liste_g), len(liste_d)
    i, j = 0, 0
    liste_fus = []
    while (i<n) and (j<m):
        if liste_g[i] < liste_d[j]:
            liste_fus.append(liste_g[i])
            i = i +1
        else:
            liste_fus.append(liste_d[j])
            j = j +1
    while (i<n):
        liste_fus.append(liste_g[i])
        i = i +1
    while (j<m):
        liste_fus.append(liste_d[j])
        j = j +1    

    return liste_fus    


# Test
print("--- Fusion boucle ---")
liste_g = [1,4,7]
liste_d = [2,5,6,9]
print(liste_g,liste_d)
print(fusion(liste_g,liste_d))



def tri_fusion(liste):
    """ Ordonne une liste par la méthode du tri fusion.
    La fonction est récursive et utilse la fonction fusion() """
    cliste = list(liste)
    n = len(cliste)
    if n <= 1:
        return cliste
    else:
        liste_g = tri_fusion(cliste[:n//2])
        liste_d = tri_fusion(cliste[n//2:])
        liste_tri = fusion(liste_g,liste_d)
    return liste_tri

# Test
print("--- Tri fusion ---")
liste = [4,3,2,1]
print(liste)
print(tri_fusion(liste))

