
##############################
# Suites
##############################


##############################
# Activité 2 - Suites arithmétiques
##############################

# But : rechercher dans une liste s'il existe trois termes
# qui forment un partie d'une suite arithmétiques.
# Il s'agit donc de trouver trois termes u[i],u[j],u[k] tels que 
# u[i] = u[j] - r, u[k] = u[j] + r (pour un certain r>0).
# On suppose la liste ordonnée.

# Ref : "Finding longest arithmetic progressions" by Jeff Erickson


def chercher_arithmetique(u):
    """ Renvoie trois termes de la liste qui forme une
    progression arithmétique (ou None) """

    n = len(u)-1
    for j in range(1,n-1):
        i = j-1
        k = i + 1
        while (i>=0) and (k<n):
            if u[j]-u[i] == u[k]-u[j]:
                return u[i],u[j],u[k]
            if u[j]-u[i] < u[k]-u[j]:
                i = i - 1
            if u[j]-u[i] > u[k]-u[j]:
                k = k + 1                

    return None

# Test
print("--- Recherche d'une progression arithmétique ---")

u = [10,11,13,17,19,23,29,31]
print(chercher_arithmetique(u))
