from copy import deepcopy
from functions import *
from colorama import Fore, Back, Style
from time import sleep

tabVide = [[0,1,0,1,0,1,0,1],
           [1,0,1,0,1,0,1,0],
           [0,1,0,1,0,1,0,1],
           [1,0,1,0,1,0,1,0],
           [0,1,0,1,0,1,0,1],
           [1,0,1,0,1,0,1,0],
           [0,1,0,1,0,1,0,1],
           [1,0,1,0,1,0,1,0]]

tabDepart = [[0,["z", False,False],0,["r", False,False],0,["r", False,False],0,["f", False,False]],
            [["p", False,False],0,["p", False,False],0,["p", False,False],0,["p", False,False],0],
            [0,["p", False,False],0,["p", False,False],0,["p", False,False],0,["p", False,False]],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [["p", True,False],0,["p", True,False],0,["p", True,False],0,["p", True,False],0],
            [0,["p", True,False],0,["p", True,False],0,["p", True,False],0,["p", True,False]],
            [["f", True,False],0,["r", True,False],0,["r", True,False],0,["z", True,False],0]]

tabTest = [[0,["p", True, False],0,1,0,1,0,["p", False, False]],
           [1,0,["f", True, False],0,1,0,["p", False, False],0],
           [0,1,0,1,0,1,0,1],
           [1,0,1,0,["p", False, False],0,1,0],
           [0,1,0,["p", True, False],0,1,0,1],
           [1,0,1,0,["p", True, False],0,["p", True, False],0],
           [0,["r", False,False],0,1,0,1,0,["p", True, False]],
           [1,["r", True,False],1,0,1,0,1,0]]



def nuclearBomb():
    """Renvoie une copie du tableau vide

    Returns:
        matrice: Une copie du tableau vide
    """
    return deepcopy(tabVide)

def nouveauTableau():
    """Renvoie une copie du tableau de départ

    Returns:
        matrice: Une copie du tableau de départ
    """
    return deepcopy(tabDepart)



def show(plateau):
    """Affiche le plateau

    Args:
        plateau (matrice): Le plateau à afficher
    """


    stringToPrint = """  0 1 2 3 4 5 6 7 \n"""

    for y, ligne in enumerate(plateau):
        stringToPrint += f"{str(y)} "
        for x, case in enumerate(ligne):
            stringToPrint += getStringCase(x,y,plateau)
        stringToPrint += "\n"
    print(stringToPrint)


def getStringCase(x,y,plateau):
    """Renvoie la chaine de caractères correspondant à la case (x,y) de plateau

    Args:
        x (int): Coordonnée x de plateau
        y (int): Coordonnée y de plateau
        plateau (matrice): Le plateau

    Returns:
        str: La chaîne de caractères correspondant à la case renseignée
    """
    case = plateau[y][x]
    case_string = ""
    if case == 0:
        case_string = "░░"
    elif case == 1:
        case_string = f"{Fore.BLACK}▓▓{Fore.RESET}"
    elif case ==2:
        case_string = "▓▓"
    elif case ==3:
        if tabVide[y][x] == 0:
            case_string = "░░"
        elif tabVide[y][x] == 1:
            case_string = f"{Fore.BLACK}▓▓{Fore.RESET}"
    else:
        fore, background = getColors(x,y,plateau)

        case_string = f"{fore}{case[0][0]}{background} {Back.RESET + Fore.WHITE}"
    return case_string


def getColors(x,y,plateau):
    """Renvoie les couleurs à afficher pour la case (x,y) de plateau

    Args:
        x (int): Coordonnée x de plateau
        y (int): Coordonnée y de plateau
        plateau (matrice): Le plateau

    Returns:
        tuple: Le Fore et Back de la case choisie
    """
    fore = Fore.LIGHTBLACK_EX
    background = Back.RESET
    
    if est_blanche(x,y,plateau): fore = Fore.WHITE
    if isSelected(x,y,plateau): background = Back.WHITE
    return fore, background
