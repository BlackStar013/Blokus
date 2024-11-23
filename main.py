# initialisation : 
plateau = [ [0 for i in range(20)]for i in range(20) ]

#p0bis = [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
p0 = [[0,0,0,0,0], [0,0,0,0,0], [0,0,1,0,0], [0,0,0,0,0], [0,0,0,0,0]]
p1 = [[0,-1,-1,0], [-1,1,1,-1], [0,-1,-1,0]]
p2 = [[0,-1,-1,0], [-1,1,1,-1], [0,-1,1,-1], [0,0,-1,0]]
p3 = [[0,-1,-1,-1,0], [-1,1,1,1,-1], [0,-1,-1,-1,0]]
p4 = [[0,-1,-1,0], [-1,1,1,-1], [-1,1,1,-1], [0,-1,-1,0]]
p5 = [[0,0,-1,0,0], [0,-1,1,-1,0], [-1,1,1,1,-1], [0,-1,-1,-1,0]]
p6 = [[0,-1,-1,-1,-1,0], [-1,1,1,1,1,-1], [0,-1,-1,-1,-1]]
p7 = [[0,0,0,-1,0], [0,-1,-1,1,-1], [-1,1,1,1,-1], [0,-1,-1,-1,0]]
p8 = [[0,0,-1,-1,0], [0,-1,1,1,-1], [-1,1,1,-1,0], [0,-1,-1,0,0]]
p9 = [[0,-1,0,0,0,0], [-1,1,-1,-1,-1,0], [-1,1,1,1,1,-1], [0,-1,-1,-1,-1,0]]
p10 = [[0,0,-1,0,0], [0,-1,1,-1,0], [0,-1,1,-1,0], [-1,1,1,1,-1], [0,-1,-1,-1,0]]
p11 = [[0,-1,0,0,0], [-1,1,-1,0,0], [-1,1,-1,-1,0], [-1,1,1,1,-1], [0,-1,-1,-1,0]]
p12 = [[0,0,-1,-1,-1,0], [0,-1,1,1,1,-1], [-1,1,1,-1,-1,0], [0,-1,-1,0,0,0]]
p13 = [[0,0,0,-1,0], [0,-1,-1,1,-1], [-1,1,1,1,-1], [-1,1,-1,-1,0], [0,-1,0,0,0]]
p14 = [[0,-1,0], [-1,1,-1], [-1,1,-1], [-1,1,-1], [-1,1,-1], [-1,1,-1], [0,-1,0]]
p15 = [[0,-1,0,0], [-1,1,-1,0], [-1,1,1,-1], [-1,1,1,-1], [0,-1,-1,0]]
p16 = [[0,0,-1,-1,0], [0,-1,1,1,-1], [-1,1,1,-1,0], [-1,1,-1,0,0], [0,-1,0,0,0]]
p17 = [[0,-1,-1,0], [-1,1,1,-1], [-1,1,-1,0], [-1,1,1,-1], [0,-1,-1,0]]
p18 = [[0,0,-1,-1,0], [0,-1,1,1,-1], [-1,1,1,-1,0], [0,-1,1,-1,0], [0,0,-1,0,0]]
p19 = [[0,0,-1,0,0], [0,-1,1,-1,0], [-1,1,1,1,-1], [0,-1,1,-1,0], [0,0,-1,0,0]]
p20 = [[0,0,-1,0,0,0], [0,-1,1,-1,-1,0], [-1,1,1,1,1,-1], [0,-1,-1,-1,-1,0]]
liste_pieces = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]
pieces_joueur = [False for i in range(len(liste_pieces))]


def affiche_plateau(plateau):
    for i in plateau:
        print(i)

#affiche_plateau(plateau)
def recuperation_case_jouable(joueur):
    liste_case_valide = []
    for i in range(len(plateau)):
        for j in range(len(plateau)):
            if plateau[i][j] == 0:
                test_voisins_direct = 1
                test_voisins_diagonaux = 0
                liste_voisins_directs = []
                if i > 0:
                    liste_voisins_directs.append((i-1, j))
                if j > 0:
                    liste_voisins_directs.append((i, j-1))
                if i < 19:
                    liste_voisins_directs.append((i+1, j))
                if j < 19:
                    liste_voisins_directs.append((i, j+1))
                for voisins in liste_voisins_directs:
                    if plateau[voisins[0]][voisins[1]] == joueur:
                        test_voisins_direct = 0
                if test_voisins_direct:
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
                        if plateau[voisins[0]][voisins[1]] == joueur:
                            test_voisins_diagonaux = 1
                    if test_voisins_diagonaux:
                        liste_case_valide.append((i, j))
    #print("les cases jouables pour le joueur", joueur , "sont :")
    return liste_case_valide

plateau[19][19] = 1
#print(recuperation_case_jouable(1))

def test_ajout_piece(joueur, numpiece, ligne, colonne):
    coup_valide = True
    if not pieces_joueur[numpiece]:
        cases_jouable = recuperation_case_jouable(joueur)
        if (ligne, colonne) in cases_jouable:
            for i in range(5):
                for j in range(5):
                    if liste_pieces[numpiece][i][j] == 1:
                        if ligne+i-2 >= 0 and colonne+j-2 >= 0 and ligne+i-2 <= 19 and colonne+j-2 <= 19 and plateau[ligne+i-2][colonne+j-2] == 0:
                            coup_valide = coup_valide and True
                        else:
                            coup_valide = coup_valide and False
            return coup_valide
    return False

#print(test_ajout_piece(1, 0, 18, 18))

def resolution_coup(joueur, numpiece, ligne, colonne):
    if test_ajout_piece(joueur, numpiece, ligne, colonne):
        for i in range(5):
            for j in range(5):
                if ligne+i-2 >= 0 and colonne+j-2 >= 0 and ligne+i-2 <= 19 and colonne+j-2 <= 19:
                    plateau[ligne+i-2][colonne+j-2] += liste_pieces[numpiece][i][j]


#resolution_coup(1, 0, 18, 18)
#affiche_plateau(plateau)