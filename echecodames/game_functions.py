#Class 6 file
from random import *
from tableau import *
from piece import *
from bot import *






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















def startBot(test=False,bot=botFacile):
    """Commence la partie contre le bot
    """

    plateau = deepcopy(tabDepart)



    while not isEnded(plateau):

        mange = False

        player_color_string = "Blanc"
        

        show(plateau)
        

        xs,ys = getCoordinatesFromInput(f"A vous de jouer, joueur {player_color_string}: \n")

        if xs == 100 and ys == 100:
            break
        unSelect(plateau)

        while isEmptyAt(xs,ys, plateau) or not est_blanche(xs,ys,plateau):
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
                
                if isEmptyAt(xs,ys, plateau) or not est_blanche(xs,ys,plateau):
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
        if isEnded(plateau):
            break
        
        if test:
            for i in plateauxPossibles(plateau, False):
                show(i)
                print(pointDuPlateau(i))
        jouer(plateau, bot, False, 2)

        





    show(plateau)
    gagnant = getColorString(whoWon(plateau))

    print(f"Le joueur {gagnant} à gagné !")







def commencer():
    print("Échecodames(best game ever) :")
    print("")
    show(tabDepart)
    print("")
    rep=""

    while not rep in ["multijoueur", "bot"]:    
        rep = input("Voulez-vous jouer en multijoueur ou contre le bot ? \n > multijoueur\n > bot\n").lower()
    
    
    if rep == "multijoueur":
        start()
    elif rep == "bot":
        difficulte = ""
        while not difficulte in ["aléatoire", "facile"]:
            difficulte = input("\nChoisissez la difficulté de votre adversaire virtuel, entre \n > aléatoire (donc très très difficile...de perdre)\n > facile (donc très très facile de gagner)\n").lower()
        
        if difficulte == "aléatoire":
            startBot(bot=botRandom)
        elif difficulte == "facile":
            startBot(bot=botFacile)
        

def botFight(bot1,bot2):
    """Commence la partie contre le bot
    """

    plateau = deepcopy(tabDepart)

    while not isEnded(plateau):
        jouer(plateau, bot1, True, 0)

        unSelect(plateau)
        if isEnded(plateau):
            break

        jouer(plateau, bot2, False, 0)

    show(plateau)
    gagnant = getColorString(whoWon(plateau))

    print(f"Le joueur {gagnant} à gagné !")
    return whoWon(plateau)


def modBot(bot,num):
    
    boti = bot

    for i in range(num):
        botList = []
        for a in range(5):
            newBot = deepcopy(bot)
            for index, c in enumerate(bot):
                newBot[index] = c + randint(-1,1)
            if botFight(newBot,botFacile):
                botList.append(newBot)
        if len(botList) > 0:
            pass

                
        
    return bot
