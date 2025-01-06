from classes import *
from copy import deepcopy


#def affiche_plateau(partie):
#    '''affiche le plateau'''
#    for i in partie.plateau:
#        print(i)


liste_pieces =[ [[0,-1,0], [-1,1,-1], [0,-1,0]],
                             [[0,0,0,0,0], [0,0,-1,-1,0], [0,-1,1,1,-1], [0,0,-1,-1,0], [0,0,0,0,0]],
                             [[0,0,0,0,0], [0,0,-1,-1,0], [0,-1,1,1,-1], [0,0,-1,1,-1], [0,0,0,-1,0]],
                             [[0,0,0,0,0], [0,-1,-1,-1,0], [-1,1,1,1,-1], [0,-1,-1,-1,0], [0,0,0,0,0]],
                             [[0,0,0,0,0], [0,0,-1,-1,0], [0,-1,1,1,-1], [0,-1,1,1,-1], [0,0,-1,-1, 0]],
                             [[0,0,-1,0,0], [0,-1,1,-1,0], [-1,1,1,1,-1], [0,-1,-1,-1,0], [0,0,0,0,0]],
                             [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,-1,-1,-1,-1,0], [0,-1,1,1,1,1,-1], [0,0,-1,-1,-1,-1,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]],
                             [[0,0,0,-1,0], [0,-1,-1,1,-1], [-1,1,1,1,-1], [0,-1,-1,-1,0], [0,0,0,0,0]],
                             [[0,0,0,0,0], [0,0,-1,-1,0], [0,-1,1,1,-1], [-1,1,1,-1,0], [0,-1,-1,0,0]],
                             [[0,0,0,0,0,0,0], [0,0,-1,0,0,0,0], [0,-1,1,-1,-1,-1,0], [0,-1,1,1,1,1,-1], [0,0,-1,-1,-1,-1,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]],
                             [[0,0,-1,0,0], [0,-1,1,-1,0], [0,-1,1,-1,0], [-1,1,1,1,-1], [0,-1,-1,-1,0]],
                             [[0,0,0,-1,0,0,0], [0,0,-1,1,-1,0,0], [0,0,-1,1,-1,-1,0], [0,0,-1,1,1,1,-1], [0,0,0,-1,-1,-1,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]],
                             [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,-1,-1,-1,0], [0,0,-1,1,1,1,-1], [0,-1,1,1,-1,-1,0], [0,0,-1,-1,0,0,0], [0,0,0,0,0,0,0]],
                             [[0,0,0,-1,0], [0,-1,-1,1,-1], [-1,1,1,1,-1], [-1,1,-1,-1,0], [0,-1,0,0,0]],
                             [[0,0,0,-1,0,0,0], [0,0,-1,1,-1,0,0], [0,0,-1,1,-1,0,0], [0,0,-1,1,-1,0,0], [0,0,-1,1,-1,0,0], [0,0,-1,1,-1,0,0], [0,0,0,-1,0,0,0]],
                             [[0,0,-1,0,0], [0,-1,1,-1,0], [0,-1,1,1,-1], [0,-1,1,1,-1], [0,0,-1,-1,0]],
                             [[0,0,-1,-1,0], [0,-1,1,1,-1], [-1,1,1,-1,0], [-1,1,-1,0,0], [0,-1,0,0,0]],
                             [[0,0,-1,-1,0], [0,-1,1,1,-1], [0,-1,1,-1,0], [0,-1,1,1,-1], [0,0,-1,-1,0]],
                             [[0,0,-1,-1,0], [0,-1,1,1,-1], [-1,1,1,-1,0], [0,-1,1,-1,0], [0,0,-1,0,0]],
                             [[0,0,-1,0,0], [0,-1,1,-1,0], [-1,1,1,1,-1], [0,-1,1,-1,0], [0,0,-1,0,0]],
                             [[0,0,0,0,0,0,0], [0,0,0,-1,0,0,0], [0,0,-1,1,-1,-1,0], [0,-1,1,1,1,1,-1], [0,0,-1,-1,-1,-1,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]],
                             ]


def int_to_binaire(n):
    '''transforme le nombre négatif du plateau lié au droit des joueurs d'y jouer en binaire
    on se limite ici volontairement à 4 bits car il n'est pas nécéssaire d'en prendre plus'''
    n = -n
    B = [0, 0, 0, 0]
    for i in range(4):
        q = n%2
        n = n//2
        if q == 1:
            B[i] = 1
    return B


def ajout_interdit_binaire(n, tour):
    '''ajoute un interdit pour un joueur et renvoie le nouveau nombre l'indiquant
    si b[0] == 1, le joueur 1 ne peut pas y jouer, si b[0] et b[1] == 1, ni le joueur 1 ni le 2 ne peuvent, ...'''
    nombre = 0
    b = int_to_binaire(n)
    b[tour] = 1
    for i in range(4):
        nombre += b[i]*2**i
    return -nombre

#print("bonjour")
#print(int_to_binaire(-1))
#print(ajout_interdit_binaire(-2, joueur1))
#print("au revoir")


def recuperation_case_jouable(tour, plateau, num_coup):
    '''on parcourt le plateau, et pour chaque case vide, on regarde si il y a une case en diagonale au joueur
    et si on est au 4 premiers coups, on rajoute artificiellement le coin du joueur'''
    liste_case_valide = []
    for i in range(len(plateau)):
        for j in range(len(plateau)):
            if int_to_binaire(plateau[i][j])[tour] == 0:
                test_voisins_diagonaux = 0
                liste_voisins_diagonale = []
                if i > 0 and j > 0:
                    liste_voisins_diagonale.append((i-1, j-1))
                if i > 0 and j < 19:
                    liste_voisins_diagonale.append((i-1, j+1))
                if i < 19 and j > 0:
                    liste_voisins_diagonale.append((i+1, j-1))
                if i < 19 and j < 19:
                    liste_voisins_diagonale.append((i+1, j+1))
                for voisins in liste_voisins_diagonale:
                    if plateau[voisins[0]][voisins[1]] == tour+1:
                        test_voisins_diagonaux = 1
                if test_voisins_diagonaux:
                    liste_case_valide.append((i, j))
    if num_coup < 4:
        if tour == 0:
            liste_case_valide.append((0, 0))
        elif tour == 1:
            liste_case_valide.append((0, 19))
        elif tour == 2:
            liste_case_valide.append((19, 19))
        else:
            liste_case_valide.append((19, 0))
    #print("les cases jouables pour le joueur", joueur , "sont :")
    return liste_case_valide

#plateau[19][19] = 1
#partie.plateau[3][3] = 1
#plateau[18][19] = -1
#print(recuperation_case_jouable(joueur1))
#affiche_plateau(plateau)


def test_ajout_piece(donnes_joueur, numpiece, piece, ligne, colonne, plateau, num_coup):     # ligne et colonne sont le centre de la piece nxn
    """on vérifie que la piece que l'on veut ajouter ne sort pas du plateau, est sur au moins une case_valide, 
    et n'est pas sur une case invalide"""
    if donnes_joueur[numpiece+3] == '0':
        tour = int(donnes_joueur[2])-1
        n = len(piece)
        diagonale_piece = False
        cases_jouable = recuperation_case_jouable(tour, plateau, num_coup)
        for i in range(n):
            for j in range(n):
                if piece[i][j] == 1:
                    if (ligne+i-(n//2), colonne+j-(n//2)) in cases_jouable:
                        diagonale_piece = True
                    if ligne+i-(n//2) >= 0 and colonne+j-(n//2) >= 0 and ligne+i-(n//2) <= 19 and colonne+j-(n//2) <= 19 and plateau[ligne+i-(n//2)][colonne+j-(n//2)] <= 0 and int_to_binaire(plateau[ligne+i-(n//2)][colonne+j-(n//2)])[tour] == 0:
                        pass
                    else:
                        return False
        return diagonale_piece
    return False

#print(test_ajout_piece(joueur1, 0, joueur1.liste_pieces[0], 0, 0))

def applique_changement(numpiece, nbrotation, rectoverso):
    piece = liste_pieces[numpiece]
    piecetemp = deepcopy(piece)
    for i in range(nbrotation):
        piecetemp = rotation_horraire_piece(piecetemp)
    piece = piecetemp
    if rectoverso == 1:
        piece = recto_verso(piecetemp)
    return piece


def resolution_coup(donnees_joueur, numpiece, piece, ligne, colonne, plateau, num_coup):
    '''on applique le coup après avoir vérifié qu'il était valide, et on passe la piece à jouée dans la liste du joueur'''
    if test_ajout_piece(donnees_joueur, numpiece, piece, ligne, colonne, plateau, num_coup):
        n = len(piece)
        donnees_joueur[numpiece+3] = True
        num_coup += 1
        for i in range(n):
            for j in range(n):
                if ligne+i-(n//2) >= 0 and colonne+j-(n//2) >= 0 and ligne+i-(n//2) <= 19 and colonne+j-(n//2) <= 19 :
                    if piece[i][j] == 1:
                        plateau[ligne+i-(n//2)][colonne+j-(n//2)] = donnees_joueur[2]
                    elif piece[i][j] == -1:
                        if plateau[ligne+i-(n//2)][colonne+j-(n//2)] <= 0:
                            plateau[ligne+i-(n//2)][colonne+j-(n//2)] = ajout_interdit_binaire(plateau[ligne+i-(n//2)][colonne+j-(n//2)], int(donnees_joueur[2])-1)
    return plateau, donnees_joueur

def resolution_coup2(num_joueur,numpiece, piece, ligne, colonne, plateau):
    # version modifiée qui prend seulement le numéro du joueur et renvoie le plateau après que la pièce ait été jouée
    n = len(piece)
    for i in range(n):
        for j in range(n):
            if ligne+i-(n//2) >= 0 and colonne+j-(n//2) >= 0 and ligne+i-(n//2) <= 19 and colonne+j-(n//2) <= 19 :
                if piece[i][j] == 1:
                    plateau[ligne+i-(n//2)][colonne+j-(n//2)] = num_joueur
    return plateau


def recto_verso(piece):
    '''renvoie le piece retournée selon une symétrie axiale verticale, genre la piece 5 ne change pas
    mais la 2 oui, elle est tournée vers l'autre côté'''
    #piece = liste_pieces[numpiece]
    nouvelle_piece = [[0 for i in range(len(piece))]for i in range(len(piece))]
    for i in range(len(piece)):
        for j in range(len(piece)):
            nouvelle_piece[i][j] = piece[i][len(piece)-j-1]
    return nouvelle_piece

#print(liste_pieces[11])
#print(recto_verso(joueur3.liste_pieces[15]))
#resolution_coup(1, 18, recto_verso(liste_pieces[18]), 17, 18)
#affiche_plateau(plateau)


def rotation_horraire_piece(piece):
    '''pivote la piece de 90 degrés dans le sens horraire'''
    #piece = liste_pieces[numpiece]
    nouvelle_piece = [[0 for i in range(len(piece))]for i in range(len(piece))]
    for i in range(len(piece)):
        for j in range(len(piece)):
            nouvelle_piece[i][j] = piece[len(piece)-j-1][i]
    return nouvelle_piece

#print(liste_pieces[11])
#print(rotation_horraire_piece(joueur2.liste_pieces[10]))
#resolution_coup(1, 18, rotation_horraire_piece(liste_pieces[18]), 17, 17)
#affiche_plateau(plateau)

'''
#non nécessaire, mais pourquoi pas
def rotation_antihorraire_piece(piece):
    #piece = liste_pieces[numpiece]
    nouvelle_piece = [[0 for i in range(5)]for i in range(5)]
    for i in range(len(piece)):
        for j in range(len(piece)):
            nouvelle_piece[i][j] = piece[j][4-i]
    return nouvelle_piece
'''


def compter_points(donnees_joueur):
    '''compte les points du joueurs selon les pieces qu'il lui reste'''
    points = 0
    for piece in range(len(liste_pieces)):
        if donnees_joueur[piece+3] == '0':
            for i in range(len(liste_pieces[piece])):
                for j in range(len(liste_pieces[piece])):
                    if liste_pieces[piece][i][j] == 1:
                        points += liste_pieces[piece][i][j]
    return points

#print(compter_points(joueur1))


# simulation de partie pour vérifier que les interdictions de jouer entre les joueurs ne créent pas de conflits
'''
resolution_coup(joueur1, 0, joueur1.liste_pieces[0], 0, 0)
#affiche_plateau(partie)
#print(partie.num_coup)
resolution_coup(joueur2, 0, joueur2.liste_pieces[0], 0, 19)
#affiche_plateau(partie)
#print(partie.num_coup)
resolution_coup(joueur3, 2, joueur3.liste_pieces[2], 18, 18)
#affiche_plateau(partie)
#print(partie.num_coup)
resolution_coup(joueur4, 3, joueur4.liste_pieces[3], 19, 1)
#affiche_plateau(partie)
#print(partie.num_coup)
resolution_coup(joueur1, 4, joueur1.liste_pieces[4], 1, 1)
#affiche_plateau(partie)
#print(partie.num_coup)
#print(joueur1.pieces_jouees)
#print(joueur3.pieces_jouees)
resolution_coup(joueur1, 14, rotation_horraire_piece(joueur1.liste_pieces[14]), 3, 5)
resolution_coup(joueur2, 14, rotation_horraire_piece(joueur2.liste_pieces[14]), 1, 16)
resolution_coup(joueur1, 1, rotation_horraire_piece(joueur1.liste_pieces[1]), 3, 0)
resolution_coup(joueur1, 9, joueur1.liste_pieces[9], 2, 9)
affiche_plateau(partie)
print("----------------------")
resolution_coup(joueur1, 12, joueur1.liste_pieces[12], 0, 13)
affiche_plateau(partie)
'''

def gagner(listetupple):
    m = listetupple[0][0]
    n = listetupple[0][1]
    L = []
    for i in range(len(listetupple)):
        if listetupple[i][1] < n:
            m = listetupple[i][0]
            n = listetupple[i][1]
            L = []
            L.append(listetupple[i][0])
        elif listetupple[i][1] == n:
            L.append(listetupple[i][0])
    return L

#print(gagnants([("Moi", 67), ("Toi", 67), ("Boris", 90)]))