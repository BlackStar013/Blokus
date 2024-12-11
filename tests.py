from main import *

def test_intToBinaire():
    assert int_to_binaire(0) == [0, 0, 0, 0]
    assert int_to_binaire(-1) == [1, 0, 0, 0]
    assert int_to_binaire(-15) == [1, 1, 1, 1]


def test_ajoutInterditBinaire():
    assert ajout_interdit_binaire(0, joueur1) == (-1)
    assert ajout_interdit_binaire(-2, joueur4) == (-10)
    assert ajout_interdit_binaire(-1, joueur1) == (-1)


def test_recuperationCasesjouables():
    assert recuperation_case_jouable(joueur1) == [(0,0)]
    assert recuperation_case_jouable(joueur2) == [(0,19)]
    assert recuperation_case_jouable(joueur3) == [(19,19)]
    assert recuperation_case_jouable(joueur4) == [(19,0)]
    partie.plateau[3][3] = 1
    assert recuperation_case_jouable(joueur1) == [(2,2), (2,4), (4,2), (4,4), (0,0)]
    partie.plateau[3][3] = 0


def test_ajoutPiece():
    assert test_ajout_piece(joueur1, 0, joueur1.liste_pieces[0], 0, 0) == True
    assert test_ajout_piece(joueur2, 1, joueur2.liste_pieces[1], 0, 19) == False
    assert test_ajout_piece(joueur2, 1, rotation_horraire_piece(rotation_horraire_piece(joueur2.liste_pieces[1])), 0, 19) == True


def test_resolutionCoup():
    resolution_coup(joueur1, 0, joueur1.liste_pieces[0], 0, 0)
    assert partie.plateau[0][0] == 1
    assert partie.plateau[0][1] == -1
    assert partie.plateau[1][0] == -1
    assert partie.plateau[1][1] == 0
    resolution_coup(joueur3, 7, rotation_horraire_piece(joueur3.liste_pieces[7]), 18, 18)
    assert partie.plateau[19][19] == 3
    assert partie.plateau[19][18] == 3
    assert partie.plateau[18][18] == 3
    assert partie.plateau[17][18] == 3
    assert partie.plateau[19][17] == -4
    assert partie.plateau[18][17] == -4
    assert partie.plateau[18][19] == -4
    assert partie.plateau[17][17] == -4
    assert partie.plateau[17][19] == -4
    assert partie.plateau[16][18] == -4


def test_rectoVerso():
    assert recto_verso(joueur1.liste_pieces[19]) == joueur1.liste_pieces[19]
    assert recto_verso(joueur3.liste_pieces[15]) == [[0, 0, -1, 0, 0], [0, -1, 1, -1, 0], [-1, 1, 1, -1, 0], [-1, 1, 1, -1, 0], [0, -1, -1, 0, 0]]


def test_rotationHorrairePiece():
    assert rotation_horraire_piece(joueur4.liste_pieces[19]) == joueur3.liste_pieces[19]
    assert rotation_horraire_piece(joueur2.liste_pieces[10]) == [[0, -1, 0, 0, 0], [-1, 1, -1, -1, 0], [-1, 1, 1, 1, -1], [-1, 1, -1, -1, 0], [0, -1, 0, 0, 0]]


def test_compterPoints():
    joueurtest = joueur_humain("je m'en moque", 1)
    assert compter_points(joueurtest) == 89
    joueurtest.pieces_jouees[3] = True
    assert compter_points(joueurtest) == 86


test_intToBinaire()
test_ajoutInterditBinaire()
test_recuperationCasesjouables()
test_ajoutPiece()
test_resolutionCoup()
test_rectoVerso()
test_rotationHorrairePiece()
test_compterPoints()