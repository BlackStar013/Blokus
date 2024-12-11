from classes import *
from main import *
import random as rd

def choisir_coup_aletoire(partie : partie, ia : joueur_IA,) -> coup:
    id_partie = partie.idpartie
    num_coup = partie.num_coup
    joueur = ia.nom
    num_piece = rd.randint(0, len(ia.pieces_jouees) - 1)
    while ia.pieces_jouees[num_piece]:
        num_piece += 1
        num_piece = num_piece % len(ia.pieces_jouees)
    piece = ia.liste_pieces[num_piece]
    if rd.randint(0,1) == 1:
        piece = recto_verso(piece)
    x = rd.randint(0,3)
    for _ in range(x):
        piece = rotation_horraire_piece(piece)
    cases_jouables = recuperation_case_jouable(ia)
    i_pos = rd.randint(0, len(cases_jouables) - 1)
    position = cases_jouables[i_pos]
    return coup(num_coup, joueur, piece, position, id_partie)

def coup_ia(partie : partie, ia : joueur_IA) -> None:
    coup = choisir_coup_aletoire(partie, ia)
    ligne, colonne = coup.position
    resolution_coup(ia, coup.piece, ligne, colonne)


c = choisir_coup_aletoire(partie, joueur3)
print(c.idpartie, c.joueur, c.numcoup, c.piece, c.position)