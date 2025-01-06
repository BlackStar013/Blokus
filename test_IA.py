from main import *
from classes import *
from IA import *

def test_choisir_coup_aletoire_aux():
    j1 = joueur_IA("IA", 1)
    p = partie(42, j1, None, None, None, False,1)
    piece = [[0,0,-1,-1,0],
             [0,-1,1,1,-1],
             [-1,1,1,-1,0],
             [-1,1,-1,0,0],
             [0,-1,0,0,0]]
    piece = recto_verso(piece)
    plateaurc, _ = resolution_coup(partie_et_joueur_to_donnees_joueur(p, j1), 16, piece, 1, 1, p.plateau, p.num_coup, p.nb_joueur)
    p.plateau = plateaurc
    j1.pieces_jouees[16] = True
    piece = [[0,0,0,0,0,0,0],
             [0,0,0,-1,0,0,0],
             [0,0,-1,1,-1,-1,0],
             [0,-1,1,1,1,1,-1],
             [0,0,-1,-1,-1,-1,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    piece = rotation_horraire_piece(piece)
    piece = rotation_horraire_piece(piece)
    plateaurc, _ = resolution_coup(partie_et_joueur_to_donnees_joueur(p, j1), 20, piece, 0, 5, p.plateau, p.num_coup, p.nb_joueur)
    p.plateau = plateaurc
    j1.pieces_jouees[20] = True
    c = choisir_coup_aletoire_aux(p, j1)
    assert test_ajout_piece(partie_et_joueur_to_donnees_joueur(p, j1), c.num_piece, c.piece, c.i, c.j, p.plateau, p.num_coup, p.nb_joueur)

def test_eval_partie():
    j1 = joueur_IA("IA", 1)
    j2 = joueur_humain("humain", 2)
    p = partie(42, j1, j2, None, None, False,2)
    assert eval_partie(p, j1) == 20

    piece = [[0,0,-1,-1,0],
             [0,-1,1,1,-1],
             [-1,1,1,-1,0],
             [-1,1,-1,0,0],
             [0,-1,0,0,0]]
    piece = recto_verso(piece)
    plateaurc, _ = resolution_coup(partie_et_joueur_to_donnees_joueur(p, j1), 16, piece, 1, 1, p.plateau, p.num_coup, p.nb_joueur)
    p.plateau = plateaurc
    j1.pieces_jouees[16] = True

    assert eval_partie(p, j1) == 446


    piece = [[0,-1,0], [-1,1,-1], [0,-1,0]]
    plateaurc, _ = resolution_coup(partie_et_joueur_to_donnees_joueur(p, j2), 16, piece, 19, 19, p.plateau, p.num_coup, p.nb_joueur)
    p.plateau = plateaurc
    j2.pieces_jouees[0] = True

    assert eval_partie(p, j1) == 425


    piece = [[0,0,0,0,0,0,0],
             [0,0,0,-1,0,0,0],
             [0,0,-1,1,-1,-1,0],
             [0,-1,1,1,1,1,-1],
             [0,0,-1,-1,-1,-1,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    piece = rotation_horraire_piece(piece)
    piece = rotation_horraire_piece(piece)
    plateaurc, _ = resolution_coup(partie_et_joueur_to_donnees_joueur(p, j1), 20, piece, 0, 5, p.plateau, p.num_coup, p.nb_joueur)
    p.plateau = plateaurc
    j1.pieces_jouees[20] = True

    assert eval_partie(p, j1) == 806

def test_joueur_suivant():
    j1 = joueur_IA("IA", 1)
    j2 = joueur_humain("humain", 2)
    j3 = joueur_IA("IA2", 3)
    j4 = joueur_humain("humain1697(bah quoi ?)", 4)
    p = partie(42, j1, j2, j3, j4, False,4)

    assert joueur_suivant(p, j1) == j2
    assert joueur_suivant(p, j2) == j3
    assert joueur_suivant(p, j3) == j4
    assert joueur_suivant(p, j4) == j1

    p2 = partie(4242, j1, j2, None, None, False, 2)

    assert joueur_suivant(p2, j1) == j2
    assert joueur_suivant(p2, j2) == j1

def test_minmax():
    j1 = joueur_IA("IA", 1)
    j2 = joueur_humain("humain", 2)
    p = partie(42, j1, j2, None, None, False,2)
    piece = [[0,0,-1,-1,0],
             [0,-1,1,1,-1],
             [-1,1,1,-1,0],
             [-1,1,-1,0,0],
             [0,-1,0,0,0]]
    piece = recto_verso(piece)
    plateaurc, _ = resolution_coup(partie_et_joueur_to_donnees_joueur(p, j1), 16, piece, 1, 1, p.plateau, p.num_coup, p.nb_joueur)
    p.plateau = plateaurc
    j1.pieces_jouees[16] = True
    piece = [[0,0,0,0,0,0,0],
             [0,0,0,-1,0,0,0],
             [0,0,-1,1,-1,-1,0],
             [0,-1,1,1,1,1,-1],
             [0,0,-1,-1,-1,-1,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    piece = rotation_horraire_piece(piece)
    piece = rotation_horraire_piece(piece)
    plateaurc, _ = resolution_coup(partie_et_joueur_to_donnees_joueur(p, j1), 20, piece, 0, 5, p.plateau, p.num_coup, p.nb_joueur)
    p.plateau = plateaurc
    j1.pieces_jouees[20] = True
    _,c = minmax(p, 1, j1, True, j1, None) # 500s pour prof = 2
    assert test_ajout_piece(partie_et_joueur_to_donnees_joueur(p, j1), c.num_piece, c.piece, c.i, c.j, p.plateau, p.num_coup, p.nb_joueur)

def test_alphabeta():
    j1 = joueur_IA("IA", 1)
    j2 = joueur_humain("humain", 2)
    p = partie(42, j1, j2, None, None, False, 2)
    piece = [[0,0,-1,-1,0],
             [0,-1,1,1,-1],
             [-1,1,1,-1,0],
             [-1,1,-1,0,0],
             [0,-1,0,0,0]]
    piece = recto_verso(piece)
    plateaurc, _ = resolution_coup(partie_et_joueur_to_donnees_joueur(p, j1), 16, piece, 1, 1, p.plateau, p.num_coup, p.nb_joueur)
    p.plateau = plateaurc
    j1.pieces_jouees[16] = True
    piece = [[0,0,0,0,0,0,0],
             [0,0,0,-1,0,0,0],
             [0,0,-1,1,-1,-1,0],
             [0,-1,1,1,1,1,-1],
             [0,0,-1,-1,-1,-1,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    piece = rotation_horraire_piece(piece)
    piece = rotation_horraire_piece(piece)
    plateaurc, _ = resolution_coup(partie_et_joueur_to_donnees_joueur(p, j1), 20, piece, 0, 5, p.plateau, p.num_coup, p.nb_joueur)
    p.plateau = plateaurc
    j1.pieces_jouees[20] = True
    _, c = alphabeta(p, 1, j1, True, j1, False, None, -float("inf"), float("inf")) # 100s pour prof = 2
    assert test_ajout_piece(partie_et_joueur_to_donnees_joueur(p, j1), c.num_piece, c.piece, c.i, c.j, p.plateau, p.num_coup, p.nb_joueur)