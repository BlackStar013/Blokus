from main import *
from classes import *
from IA import *

def test_choisir_coup_aletoire():
    j1 = joueur_IA("IA", 1)
    p = partie(42, "42 février", "42:00", j1, None, None, None, False)
    piece = [[0,0,-1,-1,0],
             [0,-1,1,1,-1],
             [-1,1,1,-1,0],
             [-1,1,-1,0,0],
             [0,-1,0,0,0]]
    piece = recto_verso(piece)
    resolution_coup(p, j1, 16, piece, 1, 1)
    piece = [[0,0,0,0,0,0,0],
             [0,0,0,-1,0,0,0],
             [0,0,-1,1,-1,-1,0],
             [0,-1,1,1,1,1,-1],
             [0,0,-1,-1,-1,-1,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    piece = rotation_horraire_piece(piece)
    piece = rotation_horraire_piece(piece)
    resolution_coup(p, j1, 20, piece, 0, 5)
    c = choisir_coup_aletoire(p, j1)
    assert test_ajout_piece(p, j1, c.numcoup, c.piece, c.position[0], c.position[1])

def test_eval_partie():
    j1 = joueur_IA("IA", 1)
    j2 = joueur_humain("humain", 2)
    p = partie(42, "42 février", "42:00", j1, j2, None, None, False)
    score_attendu = 0
    assert eval_partie(p, j1) == score_attendu

    piece = [[0,0,-1,-1,0],
             [0,-1,1,1,-1],
             [-1,1,1,-1,0],
             [-1,1,-1,0,0],
             [0,-1,0,0,0]]
    piece = recto_verso(piece)
    resolution_coup(p, j1, 16, piece, 1, 1)

    score_attendu -= 30 # la case sur laquelle on a joué n'est plus jouable'
    score_attendu += 5*3*20 # score des cases jouées
    score_attendu += 4*3*2 # bonus distance
    score_attendu += 4*3*10 # score des cases jouables
    score_attendu += 4*3 # bonus distance

    assert eval_partie(p, j1) == score_attendu


    piece = [[0,-1,0], [-1,1,-1], [0,-1,0]]
    resolution_coup(p, j2, 0, piece, 0, 19)

    score_attendu -= 20 # l'adversaire a posé 1 carré
    score_attendu -= 1 # la seule case jouable est à une distance de 1 du bord
    assert eval_partie(p, j1) == score_attendu


    piece = [[0,0,0,0,0,0,0],
             [0,0,0,-1,0,0,0],
             [0,0,-1,1,-1,-1,0],
             [0,-1,1,1,1,1,-1],
             [0,0,-1,-1,-1,-1,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    piece = rotation_horraire_piece(piece)
    piece = rotation_horraire_piece(piece)
    resolution_coup(p, j1, 20, piece, 0, 5)

    score_attendu -= 30 # la case sur laquelle on a joué n'est plus jouable'
    score_attendu += 5*3*20 # score des cases jouées
    score_attendu += 1*3*2 # bonus distance
    score_attendu += 3*3*10 # score des cases jouables
    score_attendu += 5*3 # bonus distance

    assert eval_partie(p, j1) == score_attendu

def test_joueur_suivant():
    j1 = joueur_IA("IA", 1)
    j2 = joueur_humain("humain", 2)
    j3 = joueur_IA("IA2", 3)
    j4 = joueur_humain("humain1697(bah quoi ?)", 4)
    p = partie(42, "42 février", "42:00", j1, j2, j3, j4, False)

    assert joueur_suivant(p, j1) == j2
    assert joueur_suivant(p, j2) == j3
    assert joueur_suivant(p, j3) == j4
    assert joueur_suivant(p, j4) == j1

    p2 = partie(4242, "42 février 2042", "42:43", j1, j2, None, None, False)

    assert joueur_suivant(p2, j1) == j2
    assert joueur_suivant(p2, j2) == j1

def test_choisir_coup_ia_minmax():
    j1 = joueur_IA("IA", 1)
    j2 = joueur_humain("humain", 2)
    p = partie(42, "42 février", "42:00", j1, j2, None, None, False)
    piece = [[0,0,-1,-1,0],
             [0,-1,1,1,-1],
             [-1,1,1,-1,0],
             [-1,1,-1,0,0],
             [0,-1,0,0,0]]
    piece = recto_verso(piece)
    resolution_coup(p, j1, 16, piece, 1, 1)
    piece = [[0,0,0,0,0,0,0],
             [0,0,0,-1,0,0,0],
             [0,0,-1,1,-1,-1,0],
             [0,-1,1,1,1,1,-1],
             [0,0,-1,-1,-1,-1,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    piece = rotation_horraire_piece(piece)
    piece = rotation_horraire_piece(piece)
    resolution_coup(p, j1, 20, piece, 0, 5)
    c = choisir_coup_ia_minmax(p, j1, 1) # 500s pour prof = 2
    assert test_ajout_piece(p, j1, c.numcoup, c.piece, c.position[0], c.position[1])

def test_choisir_coup_ia_alphabeta():
    j1 = joueur_IA("IA", 1)
    j2 = joueur_humain("humain", 2)
    p = partie(42, "42 février", "42:00", j1, j2, None, None, False)
    piece = [[0,0,-1,-1,0],
             [0,-1,1,1,-1],
             [-1,1,1,-1,0],
             [-1,1,-1,0,0],
             [0,-1,0,0,0]]
    piece = recto_verso(piece)
    resolution_coup(p, j1, 16, piece, 1, 1)
    piece = [[0,0,0,0,0,0,0],
             [0,0,0,-1,0,0,0],
             [0,0,-1,1,-1,-1,0],
             [0,-1,1,1,1,1,-1],
             [0,0,-1,-1,-1,-1,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    piece = rotation_horraire_piece(piece)
    piece = rotation_horraire_piece(piece)
    resolution_coup(p, j1, 20, piece, 0, 5)
    c = choisir_coup_ia_alphabeta(p, j1, 1) # 100s pour prof = 2
    assert test_ajout_piece(p, j1, c.numcoup, c.piece, c.position[0], c.position[1])