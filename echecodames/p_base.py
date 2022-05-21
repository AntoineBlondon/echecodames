from functions import *
from tableau import *
def casesDispoPion(xdepart, ydepart, plateau):
    """Renvoie la liste des cases sur lesquelles un pion basique en (x,y) sur plateau peut se déplacer

    Args:
        x (int): Coordonnée x du pion
        y (int): Coordonnée y du pion
        plateau (matrice): Le plateau

    Returns:
        list: La liste des cases disponible pour un déplacement
    """
    cases_dispo = []

    if est_blanche(xdepart, ydepart, plateau): 
        if est_valide(xdepart+1, ydepart-1, plateau) and isEmptyAt(xdepart+1, ydepart-1, plateau): #Si la case est dans le plateau && qu'elle est vide
            cases_dispo.append((xdepart+1, ydepart-1)) #L'ajouter à la liste des cases où le pion peut aller

        if est_valide(xdepart-1, ydepart-1, plateau) and isEmptyAt(xdepart-1, ydepart-1, plateau):
            cases_dispo.append((xdepart-1, ydepart-1))

    else: # Si le pion à bouger est noir
            if est_valide(xdepart-1, ydepart+1, plateau) and isEmptyAt(xdepart-1, ydepart+1, plateau):
                cases_dispo.append((xdepart-1, ydepart+1))

            if est_valide(xdepart+1, ydepart+1, plateau) and isEmptyAt(xdepart+1, ydepart+1, plateau):
                cases_dispo.append((xdepart+1, ydepart+1))

    return cases_dispo


def peutManger(x, y, plateau):
    """Vérifie si le pion peut manger sur une case autours

    Args:
        x (int): abscisse initiale du pion
        y (int): ordonnée initiale du pion
        plateau (matrice): Le plateau 

    Returns:
        list: La liste de tuples où le pion peut se déplacer en mangeant
    """
    sauter_cases_mangeables = []

    if plateau[y][x][1] == True: # Si le pion à bouger est blanc
        if est_valide(x+2, y-2, plateau) and not est_blanche(x+1,y-1): #si la case est dans le plateau && que le pion entre est noir
            sauter_cases_mangeables.append((x+2, y-2)) # Ajouter la case à la liste

        if est_valide(x-2, y-2, plateau) and not est_blanche(x+1,y+1):
            sauter_cases_mangeables.append((x-2, y-2))

    else: # Si le pion à bouger est noir
        if est_valide(x-2, y+2, plateau) and not est_blanche(x-1,y+1):
            sauter_cases_mangeables.append((x-2, y+2))

        if est_valide(x+2, y+2, plateau) and not est_blanche(x-1,y-1):
            sauter_cases_mangeables.append((x+2, y+2))
        
    return sauter_cases_mangeables