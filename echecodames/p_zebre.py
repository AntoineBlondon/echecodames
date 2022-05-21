from functions import *


#une_piece = ["identifiant", couleur=True/False]






def casesDispoZebre(x,y,plateau):
    """Renvoie la liste des cases sur lesquelles un zebre en (x,y) sur plateau peut se déplacer

    Args:
        x (int): Coordonnée x du zebre
        y (int): Coordonnée y du zebre
        plateau (matrice): Le plateau

    Returns:
        list: La liste des cases disponible pour un déplacement
    """
    a=0
    liste=[(x+1,y+3),(x-1,y+3),(x+1,y-3),(x-1,y-3),(x+3,y+1),(x-3,y-1),(x+3,y-1),(x-3,y+1)]
    for i in range(len(liste)):
        if not est_valide(liste[a][0], liste[a][1], plateau):
            liste.pop(a)
        elif isEmptyAt(liste[a][0], liste[a][1], plateau): # Si la case aux coordonnées liste[i][0], liste[i][1] est vide
            a+=1
        elif sontDeMemeCouleur(x,y,liste[a][0],liste[a][1],plateau): # Si la couleur du pion de base est égale à la couleur du pion de la case d'arrivé
            liste.pop(a)
        else:
            a+=1
        

    return liste