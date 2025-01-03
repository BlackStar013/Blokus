from classes import *
from main import *
import random as rd
import copy

def choisir_coup_aletoire(p : partie, ia : joueur_IA,) -> coup:
    # renvoie un coup aléatoire parmis ceux légaux
    id_partie = p.idpartie
    num_coup = p.num_coup
    joueur = ia

    # prend pièce, orientation, position aléatoires
    num_piece_initial = rd.randint(0, len(ia.pieces_jouees) - 1)
    symetrie_axiale_initiale = rd.choice([True, False])
    rotation_initiale = rd.randint(0, 3)
    i_initial = rd.randint(0, 19)
    j_initial = rd.randint(0, 19)

    # def les var qui vont servir à parcourir les coups si le coup initial n'est pas valide
    piece_suivante = rd.choice([-1, 1])
    rotation_suivante = rd.choice([-1, 1])
    i_suivant = rd.choice([-1, 1])
    j_suivant = rd.choice([-1, 1])

    # crée la pièce
    num_piece = num_piece_initial
    symetrie_axiale = symetrie_axiale_initiale
    rotation = rotation_initiale
    piece = ia.liste_pieces[num_piece]
    if symetrie_axiale:
        piece = recto_verso(piece)
    for r in range(rotation):
        piece = rotation_horraire_piece(piece)
    i = i_initial
    j = j_initial

    # parcourt tous les coups possibles
    while not test_ajout_piece(p, ia, num_piece, piece, i, j):
        i = (i + i_suivant) % 20
        if i == i_initial: # si on a testé tous les i de cette colonne
            j = (j + j_suivant) % 20
            if j == j_initial: # si on a testé toutes les positions pour cette piece
                rotation = (rotation + rotation_suivante) % 4
                if rotation == rotation_initiale: # si on a testé toutes les rotations
                    symetrie_axiale = not symetrie_axiale
                    if symetrie_axiale == symetrie_axiale_initiale: # si on a testé les 2 symétries axiales
                        num_piece = (num_piece + piece_suivante) % 21
                        if num_piece == num_piece_initial: # si on a testé toutes les pieces
                            raise Blokused

    position = (i,j)
    return coup(num_coup, joueur, piece, position, id_partie)

def coup_ia_aleatoire(p : partie, ia : joueur_IA) -> None:
    coup = choisir_coup_aletoire(p, ia)
    ligne, colonne = coup.position
    resolution_coup(p, ia, coup.piece, ligne, colonne)

def distance_bord(i : int, j : int) -> int:
    # donne la distance à la case au bord du plateau la plus proche
    d_i = min(i, 19-i)
    d_j = min(j, 19-j)
    return min(d_i, d_j)

def eval_partie(p : partie, joueur : joueur_humain | joueur_IA) -> int:
    # évalue le score d'un plateau pour un joueur en fonction de 
    # son score actuel, son nombre de cases jouables, le nombre de cases jouables des adversaires
    # avec bonus en fonction de la distance au centre
    #
    # complexité : O(len(p.partie) ** 2) + recup case jouable
    #
    # au niveau du score:
    # une case vers le centre est plus intéréssante
    # une case jouable est intéréssante, mais moins qu'une case où on a déjà joué (ici, 2x moins)
    # c'est plus intéressant de maximiser son score que de minimiser le score d'un seul adversaire

    score_case = 20
    score_case_jouable = 10

    jouable_j1 = recuperation_case_jouable(p, p.joueur1)
    jouable_j2 = recuperation_case_jouable(p, p.joueur2)
    if p.joueur3 == None:
        jouable_j3 = [(19, 19)]
    else:
        jouable_j3 = recuperation_case_jouable(p, p.joueur3)
    if p.joueur4 == None:
        jouable_j4 = [(19, 0)]
    else:
        jouable_j4 = recuperation_case_jouable(p, p.joueur4)
    jouable = [jouable_j1, jouable_j2, jouable_j3, jouable_j4]
    score = 0

    for i in range(len(p.plateau)):
        for j in range(len(p.plateau[i])):
            case = p.plateau[i][j]
            if case > 0:
                if case == joueur.couleur:
                    score += 3 * (score_case + 2 * distance_bord(i,j))
                else:
                    score -= score_case + 2 * distance_bord(i,j)
            else:
                for k in range(4):
                    if (i,j) in jouable[k]:
                        if k+1 == joueur.couleur:
                            score += 3 * (score_case_jouable + distance_bord(i,j))
                        else:
                            score -= score_case_jouable + distance_bord(i,j)
    return score

def joueur_suivant(p : partie, joueur : joueur_humain | joueur_IA) -> joueur_humain | joueur_IA:
    match joueur:
        case p.joueur1:
            return p.joueur2
        case p.joueur2:
            if p.joueur3 != None:
                return p.joueur3
            else:
                return p.joueur1
        case p.joueur3:
            if p.joueur4 != None:
                return p.joueur4
            else:
                return p.joueur1
        case p.joueur4:
            return p.joueur1

def recuperer_cases_potentielles(p : partie, joueur : joueur_humain | joueur_IA) -> dict[tuple[int], None]:
    # renvoie un dictionnaire avec les positions où on peut potentiellement placer une pièce
    cases_jouables = recuperation_case_jouable(p, joueur)
    cases_potentielles = {}
    for (i_cj, j_cj) in cases_jouables:
        for i in range(i_cj-2, i_cj+3):
            for j in range(j_cj-3, j_cj+4):
                if (not (i,j) in cases_potentielles) and 0 <= i < 20 and 0 <= j < 20 and p.plateau[i][j] <= 0:
                    cases_potentielles[(i,j)] = None
    return cases_potentielles

def couleur_to_joueur(p : partie, c : int) -> joueur_humain | joueur_IA:
    match c:
        case 1:
            return p.joueur1
        case 2:
            return p.joueur2
        case 3:
            return p.joueur3
        case 4:
            return p.joueur4

def minmax(p : partie, profondeur : int, joueur : joueur_humain | joueur_IA, maximiser : bool, joueur_initial : joueur_IA, meilleur_coup : coup) -> tuple[int,coup]:
    if profondeur == 0 or p.terminee:
        return eval_partie(p,joueur), meilleur_coup
    if maximiser:
        valeur = - float("inf")
        for (i,j) in recuperer_cases_potentielles(p, joueur): # parcourt toutes les possibilités de position
            for i_piece in range(len(joueur.liste_pieces)): # parcourt toutes les possibilités de pièces
                if not joueur.pieces_jouees[i_piece]:
                    for rotation in range(3): # parcourt toutes les rotations et symétries de pièce
                        for symetrie in range(2):

                            # applique le coup sur une copie de la partie (si possible)
                            piece = joueur.liste_pieces[i_piece]
                            for k in range(rotation):
                                piece = rotation_horraire_piece(piece)
                            for k in range(symetrie):
                                piece = recto_verso(piece)
                            p2 = copy.deepcopy(p)
                            joueur2 = couleur_to_joueur(p2, joueur.couleur)
                            joueur_initial2 = couleur_to_joueur(p2, joueur_initial.couleur)
                            if test_ajout_piece(p2, joueur2, i_piece, piece, i, j):
                                resolution_coup(p2, joueur2, i_piece, piece, i, j)

                                # calcule la valeur du plateau après le coup selon l'algorithme minmax
                                valeur2, _ = minmax(p2, profondeur - 1, joueur_suivant(p2, joueur2), False, joueur_initial2, meilleur_coup)

                                # garde en mémoire le coup s'il est le meilleur
                                if valeur <= valeur2:
                                    valeur = valeur2
                                    meilleur_coup = coup(p.num_coup ,joueur, piece, (i,j), p.idpartie)
        return valeur, meilleur_coup
    else:
        valeur = float("inf")
        for (i,j) in recuperer_cases_potentielles(p, joueur): # parcourt toutes les possibilités de position
            for i_piece in range(len(joueur.liste_pieces)): # parcourt toutes les possibilités de pièces
                if not joueur.pieces_jouees[i_piece]:
                    piece = joueur.liste_pieces[i_piece]
                    for rotation in range(3): # parcourt toutes les rotations et symétries de pièce
                        for symetrie in range(2):
                        
                            # applique le coup sur une copie de la partie (si possible)
                            for k in range(rotation):
                                piece = rotation_horraire_piece(piece)
                            for k in range(symetrie):
                                piece = recto_verso(piece)
                            p2 = copy.deepcopy(p)
                            joueur2 = couleur_to_joueur(p2, joueur.couleur)
                            joueur_initial2 = couleur_to_joueur(p2, joueur_initial.couleur)
                            if test_ajout_piece(p2, joueur2, i_piece, piece, i, j):
                                resolution_coup(p2, joueur2, i_piece, piece, i, j)

                                # calcule la valeur du plateau après le coup selon l'algorithme minmax
                                js = joueur_suivant(p2, joueur2)
                                valeur2, _ = minmax(p2, profondeur - 1, js, js == joueur_initial2, joueur_initial2, meilleur_coup)

                                # garde en mémoire le coup s'il est le pire (le meilleur pour l'adversaire)
                                if valeur2 <= valeur:
                                    valeur = valeur2
                                    meilleur_coup = coup(p.num_coup ,joueur, piece, (i,j), p.idpartie)
        return valeur, meilleur_coup

def choisir_coup_ia_minmax(p : partie, ia : joueur_IA, profondeur : int) -> coup:
    _, meilleur_coup = minmax(p, profondeur, ia, True, ia, None)
    if meilleur_coup == None:
        raise Blokused
    return meilleur_coup

def alphabeta(p : partie, profondeur : int, joueur : joueur_humain | joueur_IA, maximiser : bool, joueur_initial : joueur_IA, maximiser_avant : bool, meilleur_coup : coup, alpha : int, beta : int) -> tuple[int,coup]:
    if profondeur == 0 or p.terminee:
        return eval_partie(p,joueur), meilleur_coup
    if maximiser:
        valeur = - float("inf")
        for (i,j) in recuperer_cases_potentielles(p, joueur): # parcourt toutes les possibilités de position
            for i_piece in range(len(joueur.liste_pieces)): # parcourt toutes les possibilités de pièces
                if not joueur.pieces_jouees[i_piece]:
                    for rotation in range(3): # parcourt toutes les rotations et symétries de pièce
                        for symetrie in range(2):

                            # applique le coup sur une copie de la partie (si possible)
                            piece = joueur.liste_pieces[i_piece]
                            for k in range(rotation):
                                piece = rotation_horraire_piece(piece)
                            for k in range(symetrie):
                                piece = recto_verso(piece)
                            p2 = copy.deepcopy(p)
                            joueur2 = couleur_to_joueur(p2, joueur.couleur)
                            joueur_initial2 = couleur_to_joueur(p2, joueur_initial.couleur)
                            if test_ajout_piece(p2, joueur2, i_piece, piece, i, j):
                                resolution_coup(p2, joueur2, i_piece, piece, i, j)

                                # calcule la valeur du plateau après le coup selon l'algorithme minmax
                                valeur2, _ = alphabeta(p2, profondeur - 1, joueur_suivant(p2, joueur2), False, joueur_initial2, True, meilleur_coup, alpha, beta)

                                # garde en mémoire le coup s'il est le meilleur
                                if valeur <= valeur2:
                                    valeur = valeur2
                                    meilleur_coup = coup(p.num_coup ,joueur, piece, (i,j), p.idpartie)

                                # élagage beta (si l'adversaire précédent a déjà un autre pire coup)
                                if valeur > beta:
                                    return valeur, meilleur_coup
                                alpha = max(alpha, valeur)
        return valeur, meilleur_coup
    else:
        valeur = float("inf")
        for (i,j) in recuperer_cases_potentielles(p, joueur): # parcourt toutes les possibilités de position
            for i_piece in range(len(joueur.liste_pieces)): # parcourt toutes les possibilités de pièces
                if not joueur.pieces_jouees[i_piece]:
                    piece = joueur.liste_pieces[i_piece]
                    for rotation in range(3): # parcourt toutes les rotations et symétries de pièce
                        for symetrie in range(2):
                        
                            # applique le coup sur une copie de la partie (si possible)
                            for k in range(rotation):
                                piece = rotation_horraire_piece(piece)
                            for k in range(symetrie):
                                piece = recto_verso(piece)
                            p2 = copy.deepcopy(p)
                            joueur2 = couleur_to_joueur(p2, joueur.couleur)
                            joueur_initial2 = couleur_to_joueur(p2, joueur_initial.couleur)
                            if test_ajout_piece(p2, joueur2, i_piece, piece, i, j):
                                resolution_coup(p2, joueur2, i_piece, piece, i, j)

                                # calcule la valeur du plateau après le coup selon l'algorithme minmax
                                js = joueur_suivant(p2, joueur2)
                                valeur2, _ = alphabeta(p2, profondeur - 1, js, js == joueur_initial2, joueur_initial2, False, meilleur_coup, alpha, beta)

                                # garde en mémoire le coup s'il est le pire (le meilleur pour l'adversaire)
                                if valeur2 <= valeur:
                                    valeur = valeur2
                                    meilleur_coup = coup(p.num_coup ,joueur, piece, (i,j), p.idpartie)
                            
                                if maximiser_avant: # si le joueur précédent ce coup est le joueur dont on cherche le meilleur coup
                                    # élagage alpha (si le joueur a déjà un autre meilleur coup)
                                    if valeur < alpha:
                                        return valeur, meilleur_coup
                                    beta = min(beta, valeur)
                                else: # si le joueur avant est un autre adversaire (on doit cherhcer le pire coup)
                                    # élagage beta (si l'adversaire précédent a déjà un autre pire coup)
                                    if valeur > beta:
                                        return valeur, meilleur_coup
                                    alpha = max(alpha, valeur)
        return valeur, meilleur_coup

def choisir_coup_ia_alphabeta(p : partie, ia : joueur_IA, profondeur : int) -> coup:
    _, meilleur_coup = alphabeta(p, profondeur, ia, True, ia, False, None, -float("inf"), float("inf"))
    if meilleur_coup == None:
        raise Blokused
    return meilleur_coup
