liste_pieces = [ [[0,-1,0], [-1,1,-1], [0,-1,0]],
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

class joueur_humain:
    
    def __init__(self, pseudo, couleur):
        '''ajoute un joueur humain, avec un attribut pseudo, couleur, les pieces qu'il a joué, et sa liste de pieces générale'''
        print("ajout d'un joueur humain")
        self.nom = pseudo
        self.couleur = couleur
        self.pieces_jouees = [False for i in range(21)]
        self.liste_pieces = liste_pieces[:]


class joueur_IA:
    
    def __init__(self, nom, couleur):
        '''ajoute un joueur IA avec ses attributs nom, couleur, les pieces qu'il a joué, et sa liste de pieces générale'''
        print("ajout d'un joueur IA")
        self.nom = nom
        self.couleur = couleur
        self.pieces_jouees = [False for i in range(21)]
        self.liste_pieces = liste_pieces[:]

class partie:
    def __init__(self, idpartie, joueur1 : joueur_humain | joueur_IA, joueur2 : joueur_humain | joueur_IA, joueur3 : joueur_humain | joueur_IA, joueur4 : joueur_humain | joueur_IA, terminee, nb_joueur):
        '''créer une nouvelle partie avec une id unique, une date et une heure, les 4 joueurs avec None si non renseigné, un plateau vide, et un nombre de coup joué'''
        print("création d'une nouvelle partie")
        self.idpartie = idpartie
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.joueur3 = joueur3
        self.joueur4 = joueur4
        self.liste_joueur = [joueur1, joueur2, joueur3, joueur4]
        self.terminee = terminee
        self.plateau = [ [0 for i in range(20)]for i in range(20) ]
        self.num_coup = 0
        self.tour = 0
        self.nb_joueur = nb_joueur


class coup:
    def __init__(self, num_coup, joueur, num_piece, rotation, symetrie_axiale, piece, i, j , id_partie):
        '''ajoute un coup à la partie'''
        print("le joueur joue une piece sur le plateau")
        self.numcoup = num_coup
        self.joueur = joueur
        self.num_piece = num_piece
        self.rotation = rotation
        self.symetrie_axiale = symetrie_axiale
        self.piece = piece
        self.i = i
        self.j = j
        self.idpartie = id_partie


class Blokused(Exception):
    # erreur lorsque aucun coup n'est valide
    def __init__(self):
        super().__init__("Aucun coup n'est valide.")