#Class 2 file
from functions import *

def casesDispoRoi(x,y,plateau):
    """Renvoie la liste des cases sur lesquelles un roi en (x,y) sur plateau peut se déplacer

    Args:
        x (int): Coordonnée x du roi
        y (int): Coordonnée y du roi
        plateau (matrice): Le plateau

    Returns:
        list: La liste des cases disponible pour un déplacement
    """
    cases_dispo = []
    
    if est_valide(x+1, y-1, plateau) and isEmptyAt(x+1, y-1, plateau): #Si la case est dans le plateau && qu'elle est vide
        cases_dispo.append((x+1, y-1)) #L'ajouter à la liste des cases où le pion peut aller

    if est_valide(x-1, y-1, plateau) and isEmptyAt(x-1, y-1, plateau):
        cases_dispo.append((x-1, y-1))

    if est_valide(x-1, y+1, plateau) and isEmptyAt(x-1, y+1, plateau):
        cases_dispo.append((x-1, y+1))

    if est_valide(x+1, y+1, plateau) and isEmptyAt(x+1, y+1, plateau):
        cases_dispo.append((x+1, y+1))
    return cases_dispo
