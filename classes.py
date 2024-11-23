class joueur_humain:
    
    def __init__(self, pseudo, couleur, liste_pieces):
        '''ajoute un joueur humain'''
        print("ajout d'un joueur humain")
        self.nom = pseudo
        self.liste_pieces = liste_pieces
        self.couleur = couleur


class joueu_IA:
    
    def __init__(self, nom, couleur, liste_pieces):
        '''ajoute un joueur IA'''
        print("ajout d'un joueur IA")
        self.nom = nom
        self.liste_pieces = liste_pieces
        self.couleur = couleur


class partie:

    def __init__(self, idpartie, date_debut, heure_debut, joueur1, joueur2, joueur3, joueur4, terminee):
        '''créer une nouvelle partie'''
        print("création d'une nouvelle partie")
        self.idpartie = idpartie
        self.date_debut = date_debut
        self.heure_debut = heure_debut
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.joueur3 = joueur3
        self.joueur4 = joueur4
        self.terminee = terminee


class coup:

    def __init__(self, num_coup, joueur, piece, position, id_partie):
        '''ajoute un coup à la partie'''
        print("le joueur joue une piece sur le plateau")
        self.numcoup = num_coup
        self.joueur = joueur
        self.piece = piece
        self.position = position
        self.idpartie = id_partie