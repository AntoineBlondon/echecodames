from functions import *



def casesDispoFou(x,y,plateau):
    """Renvoie la liste des cases sur lesquelles un fou en (x,y) sur plateau peut se déplacer

    Args:
        x (int): Coordonnée x du fou
        y (int): Coordonnée y du fou
        plateau (matrice): Le plateau

    Returns:
        list: La liste des cases disponible pour un déplacement
    """
    liste=[]
    c=x
    v=y
    a=True
    while a:
        c+=1
        v+=1
        if not est_valide(c, v, plateau):
            a=False
        elif not isEmptyAt(c,v,plateau) and est_blanche(x,y,plateau) == est_blanche(c,v,plateau):
            a=False
        elif not isEmptyAt(c,v,plateau):#ici la case est ocupé par une piece enemie au fou (car on a deja verifié la possibilité ou c'est un alié) donc le fou peut y aller mais doi mangé et ne peut donc pas aller plus loin.
            liste.append((c,v))
            a=False
        else:liste.append((c,v))#la, la case est forcément vide, le fou peut donc y aller et meme éventuellment allr plus loin
    c=x
    v=y
    a=True
    while a:
        c+=1
        v-=1
        if not est_valide(c, v, plateau):
            a=False
        elif not isEmptyAt(c,v,plateau) and est_blanche(x,y,plateau) == est_blanche(c,v,plateau):
            a=False
        elif not isEmptyAt(c,v,plateau):#ici la case est ocupé par une piece enemie au fou (car on a deja verifié la possibilité ou c'est un alié) donc le fou peut y aller mais doi mangé et ne peut donc pas aller plus loin.
            liste.append((c,v))
            a=False
        else:liste.append((c,v))#la, la case est forcément vide, le fou peut donc y aller et meme éventuellment allr plus loin
    c=x
    v=y
    a=True
    while a:
        c-=1
        v+=1
        if not est_valide(c, v, plateau):
            a=False
        elif not isEmptyAt(c,v,plateau) and est_blanche(x,y,plateau) == est_blanche(c,v,plateau):
            a=False
        elif not isEmptyAt(c,v,plateau):#ici la case est ocupé par une piece enemie au fou (car on a deja verifié la possibilité ou c'est un alié) donc le fou peut y aller mais doi mangé et ne peut donc pas aller plus loin.
            liste.append((c,v))
            a=False
        else:liste.append((c,v))#la, la case est forcément vide, le fou peut donc y aller et meme éventuellment allr plus loin
    c=x
    v=y
    a=True
    while a:
        c-=1
        v-=1
        if not est_valide(c, v, plateau):
            a=False
        elif not isEmptyAt(c,v,plateau) and est_blanche(x,y,plateau) == est_blanche(c,v,plateau):
            a=False
        elif not isEmptyAt(c,v,plateau):#ici la case est ocupé par une piece enemie au fou (car on a deja verifié la possibilité ou c'est un alié) donc le fou peut y aller mais doi mangé et ne peut donc pas aller plus loin.
            liste.append((c,v))
            a=False
        else:liste.append((c,v))#la, la case est forcément vide, le fou peut donc y aller et meme éventuellment allr plus loin
    return liste