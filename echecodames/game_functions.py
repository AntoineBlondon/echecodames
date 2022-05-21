from os import unsetenv
from p_base import casesDispoPion, peutManger
from tableau import *
from piece import *


def isEnded(plateau):
    """Renvoie True si la partie est terminée

    Args:
        plateau (matrice): Le plateau

    Returns:
        bool: Il reste encore un roi en jeu
    """

    roi1 = True
    roi2 = True
    for y, ligne in enumerate(plateau):
        for x, case in enumerate(ligne):
            if getAbsolutePionAt(x,y,plateau) == "r":
                if est_blanche(x,y,plateau):
                    roi1 = False
                else:
                    roi2 = False
    
    return roi1 or roi2

def whoWon(plateau):
    """Renvoie le gagnant de la partie

    Args:
        plateau (matrice): Le plateau

    Returns:
        bool: Le joueur gagnant (True pour blanc et False pour noir)
    """
    roi2 = True
    for y, ligne in enumerate(plateau):
        for x, case in enumerate(ligne):
            if getAbsolutePionAt(x,y,plateau) == "r":
                if not est_blanche(x,y,plateau):
                    roi2 = False
    
    return roi2



def getColorString(color):
    """Renvoie le nom de la couleur color

    Args:
        color (bool): True pour blanc et False pour noir

    Returns:
        str: Le nom de color
    """
    colStr = "noir"

    if color: colStr = "blanc"

    return colStr



def start():
    """Commence la partie
    """

    plateau = deepcopy(tabDepart)



    tour = True

    while not isEnded(plateau):

        mange = False

        player_color_string = getColorString(tour)
        

        show(plateau)
        

        xs,ys = getCoordinatesFromInput(f"Au tour du joueur {player_color_string}: \n")

        if xs == 100 and ys == 100:
            break
        unSelect(plateau)

        while isEmptyAt(xs,ys, plateau) or est_blanche(xs,ys,plateau) != tour:
            print("c'est pas ton pion")
            xs,ys = getCoordinatesFromInput(f"Joueur {player_color_string}: \n")
            if xs == 100 and ys == 100:
                break
        select(xs,ys,plateau)
        show(plateau)

        hasmange = False

        while not mange:
            xa,ya = getCoordinatesFromInput(f"Joueur {player_color_string}, Sur quelle case voulez vous déplacer ? \n")
            if xa == 100 and ya == 100:
                break
            
            if not isEmptyAt(xa,ya,plateau) and sontDeMemeCouleur(xs,ys,xa,ya,plateau):
                xs,ys = xa, ya
            else:

                if getAbsolutePionAt(xs,ys,plateau) == "p":
                    if (xa,ya) in casesDispo(xs,ys,plateau):
                        if caseAManger(xs,ys,xa,ya,plateau) != False:
                            hasmange=True
                        manger(xs,ys,xa,ya,plateau)
                        mange = True
                elif getAbsolutePionAt(xs,ys,plateau) == "r":
                    if (xa,ya) in casesDispo(xs,ys,plateau):
                        if caseAManger(xs,ys,xa,ya,plateau) != False:
                            hasmange=True
                        manger(xs,ys,xa,ya,plateau)
                        mange = True
                        
                elif getAbsolutePionAt(xs,ys,plateau) in ["f","z"]:
                    if (xa,ya) in casesDispo(xs,ys,plateau):
                        move(xs,ys,xa,ya,plateau)
                        mange = True
                
                if isEmptyAt(xs,ys, plateau) or est_blanche(xs,ys,plateau) != tour:
                    print("impossible")

                
            unSelect(plateau)
            select(xs,ys,plateau)
            show(plateau)

        unSelect(plateau)
        select(xs,ys,plateau)
        show(plateau)
    
        if hasmange:
            xs,ys = xa, ya
            unSelect(plateau)
            selectPionQuiMange(xs,ys,plateau)
            show(plateau)
            mange = False
            
            if casesPionQuiMange(xs,ys,plateau) == []:
                mange = True
            
            while not mange:
                xa,ya = getCoordinatesFromInput(f"Joueur {player_color_string}, Sur quelle case voulez vous déplacer ? \n")
                if xa == 100 and ya == 100:
                    break
                if getAbsolutePionAt(xs,ys,plateau) in ["p", "r"]:
                    if (xa,ya) in casesDispo(xs,ys,plateau):
                        if canMangerSansDeplacer(xs,ys,xa,ya,plateau):
                            mangerSansDeplacer(xs,ys,xa,ya,plateau)
                            if not isEmptyAt(xa,ya,plateau) and SauteMoutonMortel(xa,ya, plateau) == []:
                                mange = True
                            else:
                                xs,ys = xa,ya
                        
                unSelect(plateau)
                selectPionQuiMange(xs,ys,plateau)
                show(plateau)

        atteintDerniereLigne(xa, ya, plateau)

                


        unSelect(plateau)

        
        
        
        tour = not tour # On change de joueur (True => False) et (False => True)  A garder en dernier dans la boucle while
    

    show(plateau)
    gagnant = getColorString(whoWon(plateau))

    print(f"Le joueur {gagnant} à gagné !")
