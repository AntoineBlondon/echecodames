from tableau import *
from p_zebre import *
from p_roi import *
from p_base import *
from p_fou import *

def move(xd,yd,xa,ya, plateau):
    """Déplace le pion de coordonnées (xd,yd) en (xa,ya) sur plateau

    Args:
        xd (int): Coordonnée x du pion
        yd (int): Coordonnée y du pion
        xa (int): Coordonnée x de la case d'arrivée
        ya (int): Coordonnée y de la case d'arrivée
        plateau (matrice): Le plateau
    """
    plateau[ya][xa] = plateau[yd][xd]
    plateau[yd][xd] = tabVide[yd][xd]


def caseAManger(xd,yd,xa,ya,plateau):
    """Renvoie la case à manger entre (xd,yd) et (xa,ya) de plateau

    Args:
        xd (int): Coordonnée x de la première case
        yd (int): Coordonnée y de la première case
        xa (int): Coordonnée x de la seconde case
        ya (int): Coordonnée y de la seconde case
        plateau (matrice): Le plateau

    Returns:
        tuple or bool: Le tuple des coordonnées de la case à manger ou False si il n'y en a pas
    """
    c,v = 1, 1

    if xd>xa: c = -1
    if yd>ya: v = -1

    mx, my = xd, yd

    mx += c
    my += v

    while (mx, my) != (xa,ya):
        if not isEmptyAt(mx,my, plateau) and not sontDeMemeCouleur(xd,yd,mx,my,plateau): return (mx,my)
        mx += c
        my += v
    return False


def casesDispo(x,y,plateau):
    """Renvoi la liste des cases sur lesquels le pion (x,y) peut se déplacer sur plateau

    Args:
        x (int): Coordonnée x de la case
        y (int): Coordonnée y de la case
        plateau (matrice): Le plateau

    Returns:
        list: La liste des cases sur lesquelles le pion peut se déplacer
    """
    cases  = []

    pion = getAbsolutePionAt(x,y,plateau)

    if pion == "p":
        cases = casesDispoPion(x,y,plateau) + SauteMoutonMortel(x,y,plateau)
    elif pion == "f":
        cases = casesDispoFou(x,y,plateau)
    elif pion == "r":
        cases = casesDispoRoi(x,y,plateau) + SauteMoutonMortel(x,y,plateau)
    elif pion == "z":
        cases = casesDispoZebre(x,y,plateau)
    
    return cases


def select(x,y, plateau):
    """Met en couleur les cases sur lesquelles le pion (x,y) peut se déplacer sur plateau

    Args:
        x (int): Coordonnée x du pion
        y (int): Coordonnée y du pion
        plateau (matrice): Le plateau
    """
    color(casesDispo(x,y,plateau), plateau)

def selectPionQuiMange(x,y, plateau):
    """Met en couleur les cases sur lesquelles le pion (x,y) peut se déplacer sur plateau s'il à déjà mangé

    Args:
        x (int): Coordonnée x du pion
        y (int): Coordonnée y du pion
        plateau (matrice): Le plateau
    """
    cases = casesPionQuiMange(x,y,plateau)
    
    color(cases, plateau)

def casesPionQuiMange(x,y,plateau):
    """Renvoie les cases sur lesquelles le pion (x,y) peut se déplacer sur plateau s'il à déjà mangé

    Args:
        x (int): Coordonnée x du pion
        y (int): Coordonnée y du pion
        plateau (matrice)): Le plateau

    Returns:
        list: La liste de tuple des cases sur lesquelles le pion (x,y) peut se déplacer sur plateau s'il à déjà mangé
    """
    cases = casesDispo(x,y,plateau)
    if getAbsolutePionAt(x,y,plateau) in ["p","r"]:# Si le pion est un pion de base ou un roi
        index = 0
        for i in range(len(cases)):# Pour chaque case sur laquelle il pourrait se déplacer
            case = cases[index]
            if not canMangerSansDeplacer(x,y,case[0],case[1], plateau):# Si le pion ne peut pas manger en se déplaçant
                cases.pop(index)
            else:
                index += 1
    return cases


def unSelect(plateau):
    """Décolore les cases séléctionnées de plateau

    Args:
        plateau (matrice): Le plateau
    """
    newPlateau = plateau
    for y, ligne in enumerate(plateau):
        for x, case in enumerate(ligne):
            if isEmptyAt(x,y,plateau):
                newPlateau[y][x] = tabVide[y][x]
            else:
                newPlateau[y][x][2] = False
    plateau = newPlateau



def color(liste_cases, plateau):
    """Colore les cases de liste_cases de plateau

    Args:
        liste_cases (list): Liste des cases à colorer
        plateau (matrice): Le plateau
    """
    newPlateau = plateau
    for case in liste_cases:
        if isEmptyAt(case[0],case[1],plateau): 
            newPlateau[case[1]][case[0]] = 2
        else:
            newPlateau[case[1]][case[0]][2] = True
    plateau = newPlateau




def manger(xd,yd,xa,ya,plateau):
    """Déplace le pion (xd,yd) sur la case (xa,ya) en mangeant

    Args:
        xd (int): Coordonnée x du pion
        yd (int): Coordonnée y du pion
        xa (int): Coordonnée x de la case d'arrivée
        ya (int): Coordonnée y de la case d'arrivée
        plateau (matrice): Le plateau
    """
    case = caseAManger(xd,yd,xa,ya,plateau)
    move(xd,yd,xa,ya,plateau)
    if case != False:
        plateau[case[1]][case[0]] = tabVide[case[1]][case[0]]
    
def mangerSansDeplacer(xd,yd,xa,ya,plateau):
    """Déplace le pion (xd,yd) sur la case (xa,ya) en mangeant si le pion à déjà mangé

    Args:
        xd (int): Coordonnée x du pion
        yd (int): Coordonnée y du pion
        xa (int): Coordonnée x de la case d'arrivée
        ya (int): Coordonnée y de la case d'arrivée
        plateau (matrice): Le plateau
    """
    case = caseAManger(xd,yd,xa,ya,plateau)
    if case != False:
        move(xd,yd,xa,ya,plateau)
        plateau[case[1]][case[0]] = tabVide[case[1]][case[0]]

def canMangerSansDeplacer(xd,yd,xa,ya,plateau):
    """Renvoie True si le pion (xd,yd) peut se déplacer sur la case (xa,ya) en mangeant

    Args:
        xd (int): Coordonnée x du pion
        yd (int): Coordonnée y du pion
        xa (int): Coordonnée x de la case d'arrivée
        ya (int): Coordonnée y de la case d'arrivée
        plateau (matrice): Le plateau

    Returns:
        bool: Le pion peut manger un pion
    """
    case = caseAManger(xd,yd,xa,ya,plateau)
    if case != False:
        return True
    return False

def atteintDerniereLigne(x, y, plateau):
    """Change le pion (x,y) s'il a atteint la ligne de font

    Args:
        x (int): Coordonnée x du pion
        y (int): Coordonnée y du pion
        plateau (int): Le plateau
    """
    newPlateau = plateau
    if getAbsolutePionAt(x, y, plateau)=="p": #si c'est un pion
        couleur = est_blanche(x, y, plateau)
        if couleur == True and y == 0: # Si le pion est blanc et qu'il est sur la ligne du haut
            choix_nouveau_pion = input("Veuillez choisir s'il vous plait un nouveau pion entre :\n- roi\n- zebre\n- fou\n")

            if choix_nouveau_pion == "roi":
                newPlateau[y][x][0]="r"
            if choix_nouveau_pion == "zebre":
                newPlateau[y][x][0]="z"
            if choix_nouveau_pion == "fou":
                newPlateau[y][x][0]="f"
            
        if couleur == False and y == 7: # Si le pion est noir
            choix_nouveau_pion = input("Veuillez choisir s'il vous plait un nouveau pion entre :\n- roi\n- zebre\n- fou\n")

            if choix_nouveau_pion == "roi":
                newPlateau[y][x][0]="r"
            if choix_nouveau_pion == "zebre":
                newPlateau[y][x][0]="z"
            if choix_nouveau_pion == "fou":
                newPlateau[y][x][0]="f"
    plateau = newPlateau
    