
from classes import *

# initialisation : 
#plateau = [ [0 for i in range(20)]for i in range(20) ]
#num_coup = 0

"""
# liste des 21 pieces, 1 pour la pièce, et -1 pour les cases qu'elle interdit
p0 = [[0,-1,0], [-1,1,-1], [0,-1,0]]
p1 = [[0,0,0,0,0], [0,0,-1,-1,0], [0,-1,1,1,-1], [0,0,-1,-1,0], [0,0,0,0,0]]
p2 = [[0,0,0,0,0], [0,0,-1,-1,0], [0,-1,1,1,-1], [0,0,-1,1,-1], [0,0,0,-1,0]]
p3 = [[0,0,0,0,0], [0,-1,-1,-1,0], [-1,1,1,1,-1], [0,-1,-1,-1,0], [0,0,0,0,0]]
p4 = [[0,0,0,0,0], [0,0,-1,-1,0], [0,-1,1,1,-1], [0,-1,1,1,-1], [0,0,-1,-1, 0]]
p5 = [[0,0,-1,0,0], [0,-1,1,-1,0], [-1,1,1,1,-1], [0,-1,-1,-1,0], [0,0,0,0,0]]
p6 = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,-1,-1,-1,-1,0], [0,-1,1,1,1,1,-1], [0,0,-1,-1,-1,-1,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
p7 = [[0,0,0,-1,0], [0,-1,-1,1,-1], [-1,1,1,1,-1], [0,-1,-1,-1,0], [0,0,0,0,0]]
p8 = [[0,0,0,0,0], [0,0,-1,-1,0], [0,-1,1,1,-1], [-1,1,1,-1,0], [0,-1,-1,0,0]]
p9 = [[0,0,0,0,0,0,0], [0,0,-1,0,0,0,0], [0,-1,1,-1,-1,-1,0], [0,-1,1,1,1,1,-1], [0,0,-1,-1,-1,-1,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
p10 = [[0,0,-1,0,0], [0,-1,1,-1,0], [0,-1,1,-1,0], [-1,1,1,1,-1], [0,-1,-1,-1,0]]
p11 = [[0,0,0,-1,0,0,0], [0,0,-1,1,-1,0,0], [0,0,-1,1,-1,-1,0], [0,0,-1,1,1,1,-1], [0,0,0,-1,-1,-1,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
p12 = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,-1,-1,-1,0], [0,0,-1,1,1,1,-1], [0,-1,1,1,-1,-1,0], [0,0,-1,-1,0,0,0], [0,0,0,0,0,0,0]]
p13 = [[0,0,0,-1,0], [0,-1,-1,1,-1], [-1,1,1,1,-1], [-1,1,-1,-1,0], [0,-1,0,0,0]]
p14 = [[0,0,0,-1,0,0,0], [0,0,-1,1,-1,0,0], [0,0,-1,1,-1,0,0], [0,0,-1,1,-1,0,0], [0,0,-1,1,-1,0,0], [0,0,-1,1,-1,0,0], [0,0,0,-1,0,0,0]]
p15 = [[0,0,-1,0,0], [0,-1,1,-1,0], [0,-1,1,1,-1], [0,-1,1,1,-1], [0,0,-1,-1,0]]
p16 = [[0,0,-1,-1,0], [0,-1,1,1,-1], [-1,1,1,-1,0], [-1,1,-1,0,0], [0,-1,0,0,0]]
p17 = [[0,0,-1,-1,0], [0,-1,1,1,-1], [0,-1,1,-1,0], [0,-1,1,1,-1], [0,0,-1,-1,0]]
p18 = [[0,0,-1,-1,0], [0,-1,1,1,-1], [-1,1,1,-1,0], [0,-1,1,-1,0], [0,0,-1,0,0]]
p19 = [[0,0,-1,0,0], [0,-1,1,-1,0], [-1,1,1,1,-1], [0,-1,1,-1,0], [0,0,-1,0,0]]
p20 = [[0,0,0,0,0,0,0], [0,0,0,-1,0,0,0], [0,0,-1,1,-1,-1,0], [0,-1,1,1,1,1,-1], [0,0,-1,-1,-1,-1,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
liste_pieces = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]
pieces_joueur = [False for i in range(len(liste_pieces))]     # liste des pieces jouées par le joueur, False = non jouée
"""

joueur1 = joueur_humain("BlackStar", 1)
joueur2 = joueur_humain("Tsubaki", 2)
joueur3 = joueur_IA("Maka", 3)
joueur4 = joueur_IA("Soul", 4)
partie = partie(13, "7janvier", "3hdumat", joueur1, joueur2, joueur3, joueur4, False)


def affiche_plateau(partie):
    '''affiche le plateau'''
    for i in partie.plateau:
        print(i)


def int_to_binaire(n):
    '''transforme le nombre négatif du plateau lié au droit des joueurs d'y jouer en binaire'''
    n = -n
    B = [0, 0, 0, 0]
    for i in range(4):
        q = n%2
        n = n//2
        if q == 1:
            B[i] = 1
    return B


def ajout_interdit_binaire(n, joueur):
    '''ajoute un interdit pour un joueur et renvoie le nouveau nombre l'indiquant'''
    nombre = 0
    b = int_to_binaire(n)
    b[joueur.couleur-1] = 1
    for i in range(4):
        nombre += b[i]*2**i
    return -nombre


#print("bonjour")
#print(int_to_binaire(-1))
#print(ajout_interdit_binaire(-2, joueur1))
#print("au revoir")


#affiche_plateau(plateau)
def recuperation_case_jouable(joueur):
    '''on parcourt le plateau, et pour chaque case vide, on regarde si il y a une case en diagonale du joueur'''
    liste_case_valide = []
    for i in range(len(partie.plateau)):
        for j in range(len(partie.plateau)):
            if int_to_binaire(partie.plateau[i][j])[joueur.couleur-1] == 0:
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
                    if partie.plateau[voisins[0]][voisins[1]] == joueur.couleur:
                        test_voisins_diagonaux = 1
                if test_voisins_diagonaux:
                    liste_case_valide.append((i, j))
    if partie.num_coup < 4:
        if joueur.couleur == 1:
            liste_case_valide.append((0, 0))
        elif joueur.couleur == 2:
            liste_case_valide.append((0, 19))
        elif joueur.couleur == 3:
            liste_case_valide.append((19, 19))
        else:
            liste_case_valide.append((19, 0))
    #print("les cases jouables pour le joueur", joueur , "sont :")
    return liste_case_valide

#plateau[19][19] = 1
#plateau[19][18] = -1
#plateau[18][19] = -1
#print(recuperation_case_jouable(joueur2))
#affiche_plateau(plateau)

def test_ajout_piece(joueur, numpiece, piece, ligne, colonne):     # ligne et colonne sont le centre de la piece nxn
    """on regarde la piece que l'on veut ajouter ne sort pas du plateau, est sur au moins une case_valide, et n'est pas sur une case invalide"""
    if not joueur.pieces_jouees[numpiece]:
        n = len(piece)
        sur_un_coin = False
        cases_jouable = recuperation_case_jouable(joueur)
        for i in range(n):
            for j in range(n):
                if piece[i][j] == 1:
                    if (ligne+i-(n//2), colonne+j-(n//2)) in cases_jouable:
                        sur_un_coin = True
                    if ligne+i-(n//2) >= 0 and colonne+j-(n//2) >= 0 and ligne+i-(n//2) <= 19 and colonne+j-(n//2) <= 19 and partie.plateau[ligne+i-(n//2)][colonne+j-(n//2)] <= 0 and int_to_binaire(partie.plateau[ligne+i-(n//2)][colonne+j-(n//2)])[joueur.couleur-1] == 0:
                        pass
                    else:
                        return False
        return sur_un_coin
    return False

#print(test_ajout_piece(1, 0, liste_pieces[0], 0, 0))

def resolution_coup(joueur, numpiece, piece, ligne, colonne):
    '''on applique le coup après avoir vérifié qu'il était valide'''
    if test_ajout_piece(joueur, numpiece, piece, ligne, colonne):
        n = len(piece)
        joueur.pieces_jouees[numpiece] = True
        partie.num_coup += 1
        for i in range(n):
            for j in range(n):
                if ligne+i-(n//2) >= 0 and colonne+j-(n//2) >= 0 and ligne+i-(n//2) <= 19 and colonne+j-(n//2) <= 19 :
                    if piece[i][j] == 1:
                        partie.plateau[ligne+i-(n//2)][colonne+j-(n//2)] = joueur.couleur
                    elif piece[i][j] == -1:
                        if partie.plateau[ligne+i-(n//2)][colonne+j-(n//2)] <= 0:
                            partie.plateau[ligne+i-(n//2)][colonne+j-(n//2)] = ajout_interdit_binaire(partie.plateau[ligne+i-(n//2)][colonne+j-(n//2)], joueur)
    else:
        print("coup invalide")


def recto_verso(piece):
    '''renvoie le piece retournée selon une symétrie axiale verticale, genre la piece ne change pas; mais la 2 oui, elle est tournée vers l'autre côté'''
    #piece = liste_pieces[numpiece]
    nouvelle_piece = [[0 for i in range(len(piece))]for i in range(len(piece))]
    for i in range(len(piece)):
        for j in range(len(piece)):
            nouvelle_piece[i][j] = piece[i][len(piece)-j-1]
    return nouvelle_piece

#print(liste_pieces[11])
#print(recto_verso(liste_pieces[11]))
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
#print(rotation_horraire_piece(liste_pieces[11]))
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

def compter_points(joueur):
    '''compte les points du joueurs selon les pieces qu'il lui reste'''
    points = 0
    for piece in range(len(joueur.liste_pieces)):
        if not joueur.liste_pieces[piece]:
            for i in range(len(joueur.liste_pieces[piece])):
                for j in range(len(joueur.liste_pieces[piece])):
                    if joueur.liste_pieces[piece][i][j] == 1:
                        points += joueur.liste_pieces[piece][i][j]
    return points

#print(compter_points(pieces_joueur))

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