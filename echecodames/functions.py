#Class 1 file


def SauteMoutonMortel(x,y,plateau):
    """Renvoie la liste de coordonnées de plateau sur lesquelles le pion situé en (x,y) peut se déplacer

    Args:
        x (int): Coordonnée x du pion
        y (int): Coordonnée y du pion
        plateau (matrice): Le plateau

    Returns:
        list: La liste de tuples correspondant au coordonnées sur lesquelles le pion peut se déplacer
    """
    index=0
    casesDArrivee=[(x+2,y+2),(x-2,y+2),(x+2,y-2),(x-2,y-2)]
    for loop in range(len(casesDArrivee)):
        x1,y1 = casesDArrivee[index][0],casesDArrivee[index][1] # Coordonnées de la case d'arrivée

        x2,y2 = int((x1+x)/2),int((y1+y)/2) # Coordonnées de la case à manger (obtenue en faisant la moyenne de chaque coordonnée)

        if est_valide(x1,y1, plateau) and isEmptyAt(x1, y1, plateau) and not isEmptyAt(x2,y2 , plateau) and not sontDeMemeCouleur(x,y,x2,y2,plateau): # Si la case d'arrivée est vide et que celle que l'on mange n'est ni vide ni occupée par un pion de la même couleur:
            index+=1
            # On ne la supprime pas de la liste et on passe donc a la case suivante
        else:
            casesDArrivee.pop(index)
            # La variable "index" reste la même si on supprime car la case suivante a prit la place de celle que l'on vient de supprimer
    return casesDArrivee




def est_valide(x, y, plateau):
    """Renvoie si la case (x,y) est dans le plateau

    Args:
        x (int): Coordonnée x de la case
        y (int): Coordonnée y de la case
        plateau (matrice): Le plateau

    Returns:
        bool: La case (x,y) se situe sur plateau
    """
    return  0 <= x <= len(plateau[0])-1 and 0 <= y <= len(plateau)-1



def est_blanche(x,y,plateau):
    """Renvoie la couleur de la case (x,y) de plateau

    Args:
        x (int): Coordonnée x de la case
        y (int): Coordonnée y de la case
        plateau (matrice): Le plateau

    Returns:
        bool: True si la case est blanche
    """
    return plateau[y][x][1]

def getPionAt(x,y,plateau):
    """Renvoie la case (x,y) de plateau

    Args:
        x (int): Coordonnée x de la case
        y (int): Coordonnée y de la case
        plateau (matrice): Le plateau

    Returns:
        int or list: La case (x,y) de plateau
    """
    return plateau[y][x]

def getAbsolutePionAt(x,y,plateau):
    """Renvoie la valeur absolue de la case x,y de plateau
    Args:
        x (int): Coordonnée x de la case
        y (int): Coordonnée y de la case
        plateau (matrice): Le plateau

    Returns:
        int: La valeur du pion en case (x,y) de plateau

    Example:
        Si la case est ["f", True], renvoie "f"

        Si la case est 2, renvoie 2
    """
    if isEmptyAt(x,y,plateau): return plateau[y][x]
    return plateau[y][x][0]


def isEmptyAt(x,y,plateau):
    """Renvoie True si la case x,y de plateau n'est pas occupée par un pion (if case == 0, 1 ou 2)
    
    Args:
        x (int): Coordonnée x de la case
        y (int): Coordonnée y de la case
        plateau (matrice): Le plateau

    Returns:
        bool: La case (x,y) de plateau est vide
    """
    return type(plateau[y][x]) == type(1)


def getCoordinatesFromInput(message):
    """Demande à l'utilisateur d'entrer des coordonnées avec le message message et les renvoie

    Args:
        message (str): Le message à afficher

    Returns:
        tuple: Le tuple de coordonnées renseigné par l'utilisateur
    """
    coords = input(message)
    
    return translate(coords)
    

def isSelected(x,y,plateau):
    """Renvoie True si la case (x,y) de plateau est selectionnée par un joueur

    Args:
        x (int): Coordonnée x de la case
        y (int): Coordonnée y de la case
        plateau (matrice): Le plateau

    Returns:
        bool: La case est selectionnée
    """
    return plateau[y][x][2]


def sontDeMemeCouleur(x1,y1,x2,y2,plateau):
    """Renvoie True si les cases (x1,y1) et (x2,y2) de plateau sont de la même couleur

    Args:
        x1 (int): Coordonnée x de la première case
        y1 (int): Coordonnée y de la première case
        x2 (int): Coordonnée x de la seconde case
        y2 (int): Coordonnée y de la seconde case
        plateau (matrice): Le plateau

    Returns:
        bool: Les deux cases sont de la même couleur
    """
    return est_blanche(x1,y1,plateau) == est_blanche(x2,y2,plateau)


def translate(string):
    x=ord(string[0].upper()) - 65
    y=int(string[1])-1
    return x,y