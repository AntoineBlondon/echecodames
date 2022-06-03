#Class 5 file
from hashlib import new
from random import *
from turtle import pendown
from piece import *
from time import sleep

lesPoints = {
"pionAlliéBaseSurPlateau": 1, "pionAlliéFouSurPlateau": 2, 
"pionAlliéZèbreSurPlateau": 3, "pionAlliéRoiSurPlateau": 5, 
"pionEnnemiBaseSurPlateau": -1, "pionEnnemiFouSurPlateau": -2, 
"pionEnnemiZèbreSurPlateau": -3, "pionEnnemiRoiSurPlateau": -5, 
"pionAlliéBaseAttaqué": -1, "pionAlliéFouAttaqué": -2, 
"pionAlliéZèbreAttaqué": -3, "pionAlliéRoiAttaqué": -5, 
"pionAlliéRoiUniqueAttaqué": -666,
"pionEnnemiBaseAttaqué": 1,
"pionEnnemiFouAttaqué": 2,
"pionEnnemiZèbreAttaqué": 3,
"pionEnnemiRoiAttaqué": 5}



def pointDuPlateau(plateau):
    """Renvoie les points d'un plateau
    > On rentre un plateau, on compte les points totaux du plateau selon les pions, les attaques possibles et les défenses possibles 
    
    Args:
        plateau (matrice): Le plateau
    
    Returns:
        int: Le nombre de point attribué au plateau
    """
    pointsDuPlateau = 0

    for y, ligne in enumerate(plateau):
        for x, case in enumerate(ligne):
            if getAbsolutePionAt(x,y,plateau) == "p":
                if est_blanche(x,y,plateau) == False:
                    pointsDuPlateau += 2
                else: pointsDuPlateau -= 2

            if getAbsolutePionAt(x,y,plateau) == "f":
                if est_blanche(x,y,plateau) == False:
                    pointsDuPlateau += 3
                else: pointsDuPlateau -= 3

            if getAbsolutePionAt(x,y,plateau) == "z":
                if est_blanche(x,y,plateau) == False:
                    pointsDuPlateau += 4
                else: pointsDuPlateau -= 4

            if getAbsolutePionAt(x,y,plateau) == "r":
                if est_blanche(x,y,plateau) == False:
                    pointsDuPlateau += 6
                else: pointsDuPlateau -= 6
            
            if not isEmptyAt(x,y,plateau):
                if len(statsAttaque(x,y,plateau)) > 0:
                    if getAbsolutePionAt(x,y,plateau)=="p":

                        if len(statsAttaque(x,y,plateau)) > len(statsDefense(x,y,plateau)):
                            if est_blanche(x,y,plateau) == False:
                                pointsDuPlateau-=1
                            else: pointsDuPlateau+=1

                    if getAbsolutePionAt(x,y,plateau) == 'f':
                        pion = False
                            
                        for i in statsAttaque(x,y,plateau):
                            if i[0] == 'p': pion == True
                        
                        if pion or len(statsAttaque(x,y,plateau)) > len(statsDefense(x,y,plateau)):
                            if est_blanche(x,y,plateau) == False:
                                pointsDuPlateau-=2
                            else: pointsDuPlateau+=2
                    
                    if getAbsolutePionAt(x,y,plateau) == 'z':
                        pion = False
                            
                        for i in statsAttaque(x,y,plateau):
                            if i[0] in ['p','f']: pion == True
                        
                        if pion or len(statsAttaque(x,y,plateau)) > len(statsDefense(x,y,plateau)):
                            if est_blanche(x,y,plateau) == False:
                                pointsDuPlateau-=3
                            else: pointsDuPlateau+=3
                    
                    if getAbsolutePionAt(x,y,plateau) == 'r':
                        roi = 0
                        for yd,lig in enumerate(plateau):
                            for xd,uneCase in enumerate(lig):
                                if getAbsolutePionAt(xd,yd,plateau) =='r' and not uneCase[2]: roi += 1
                        
                        
                        if not est_blanche(x,y,plateau):
                            if roi>1:
                                pointsDuPlateau-=5
                            else:
                                pointsDuPlateau-=666
                        else:
                            pointsDuPlateau+=5
            if isEnded(plateau):
                if not whoWon(plateau):
                    pointsDuPlateau += 666666
                else:
                    pointsDuPlateau -= 666666
        
    return pointsDuPlateau






def plateauxPossibles(plateau, couleur):
    """Renvoie la liste de tous les plateau possibles
    
    Args:
        plateau (matrice): Le plateau de départ
        couleur (bool): La couleur du bot (True => Blanc, False => Noir)
    
    Returns:
        list: La liste des plateaux possible
    """

    liste = []

    for ((xd,yd),(xa,ya)) in getAllDeplacements(plateau, couleur):
        newPlateau = deepcopy(plateau)
        if getAbsolutePionAt(xd,yd,newPlateau) == "p":
            manger(xd,yd,xa,ya,newPlateau)
        elif getAbsolutePionAt(xd,yd,newPlateau) == "r":
            manger(xd,yd,xa,ya,newPlateau)
                
        elif getAbsolutePionAt(xd,yd,newPlateau) in ["f","z"]:
            move(xd,yd,xa,ya,newPlateau)
        liste.append(newPlateau)

    return liste



def getBestMove(plateau, couleur):
    """Renvoie le meilleur déplacement

    Args:
        plateau (matrice): Le plateau
        couleur (bool): La couleur du bot
    
    Returns:
        tuple: tuple de couple de coordonnées ((xd,yd),(xa,ya))
    """
    listePlateaux = plateauxPossibles(plateau, couleur)
    listeMoves = getAllDeplacements(plateau, couleur)

    while len(listePlateaux) > 1 and len(listeMoves) > 1:
        p1 = pointDuPlateau(listePlateaux[0])

        p2 = pointDuPlateau(listePlateaux[1])

        if p1 > p2:
            listePlateaux.pop(1)
            listeMoves.pop(1)
        elif p1 > p2:
            listePlateaux.pop(0)
            listeMoves.pop(0)
        else:
            a = randint(0,1)
            listePlateaux.pop(a)
            listeMoves.pop(a)
        
    return listeMoves[0]






def jouer(plateau, couleur):
    """Fait jouer le bot

    Args:
        plateau (matrice): Le plateau
        couleur (bool): La couleur du bot
    """
    mange = False
    xs,ys = getBestMove(plateau, couleur)[0]
    select(xs,ys,plateau)
    show(plateau)

    hasmange = False

    while not mange:
        xa,ya = getBestMove(plateau, couleur)[1]
        

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


        
        
        if hasmange:
            xs,ys = xa, ya
            unSelect(plateau)
            selectPionQuiMange(xs,ys,plateau)
            show(plateau)
            sleep(0.5)
            mange = False
            
            if casesPionQuiMange(xs,ys,plateau) == []:
                mange = True
            
            while not mange:
                xa,ya = casesPionQuiMange(xs,ys,plateau)[randint(0,len(casesPionQuiMange(xs,ys,plateau)))]
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
        unSelect(plateau)
        select(xs,ys,plateau)
        show(plateau)

        atteintDerniereLigne(xa, ya, plateau)
    

def ca_depend(peutetre, oupas):
    return "ça dépend peut-être pas " +str(peutetre)+ "\nOu alors ça pourrait " +str(oupas)