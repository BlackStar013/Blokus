from flask import Flask, render_template, request, g
import sqlite3
from main import *
from classes import *
from IA import *
from cs50 import SQL


app = Flask(__name__)
db = SQL("sqlite:///data/blokus.db")

@app.route('/')
def page_accueil():
    return render_template("index.html")

@app.route('/sign_in')
def page_signin():
    return render_template("sign_in.html")

@app.route('/login')
def page_login():
    return render_template("login.html")


def get_db_connection():
    connection = getattr(g, '_database', None)
    if connection is None:
        connection = g._database = sqlite3.connect('data/blokus.db')
    return connection

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/login', methods=['POST', 'GET'])
def home_after_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        connection = get_db_connection().cursor()
        connection.execute("SELECT * FROM utilisateur WHERE pseudo = :val", {'val':username})
        content = []
        for tpl in connection.fetchone():
            content.append(f'{tpl}')
        connection.close()
        if content != []:
            if content[0] == username and content[1] == password:
                return render_template('option.html')
    return render_template('login.html')

@app.route("/sign_in2", methods=['GET', 'POST'])
def sign_in2():
    username = request.form["username"]
    password = request.form["password"]
    connection = get_db_connection()
    if not connection.execute("SELECT pseudo FROM utilisateur WHERE pseudo = :val", {'val':username}).fetchone():
        connection.execute("INSERT INTO utilisateur (pseudo, mot_de_passe) VALUES (?, ?)", (username, password))
        connection.commit()
        connection.close()
        return render_template("login.html")
    else :
        connection.close()
        return render_template("sign_in2.html")

@app.route("/option")
def option():
    return render_template('option.html')

@app.route("/rejoindre")
def rejoindre():
    return render_template('rejoindre_partie.html')

@app.route('/rejoindre_partie', methods=['GET', 'POST'])
def rejoindrePartie():
    id_partie = request.form["identifiantDePartie"]
    username = request.form["username"]
    return affichage(id_partie)

@app.route("/historique_partie")
def historique_partie():
    parties=db.execute("SELECT * FROM partie") #Liste de dictionnaires contenant les données relatives à une partie (joueurs, date etc...)
    return render_template('historique_partie.html', parties=parties)

@app.route('/creer')
def creer():
    return render_template('creer_partie.html')

@app.route("/creer_partie", methods=['GET', 'POST'])
def creerPartie():
    username1 = request.form["username1"]
    username2 = request.form["username2"]
    username3 = request.form["username3"]
    username4 = request.form["username4"]
    type2 = request.form["type2"]
    type3 = request.form["type3"]
    type4 = request.form["type4"]
    niveau = request.form["niveau"]
    c = get_db_connection().cursor()
    c.execute("SELECT COUNT(*) FROM partie")
    nb_partie = c.fetchall()[0][0] + 1
    c.close()
    liste_joueur = [username1]
    if type2 != "Vide":
        if type2 == "H":
            liste_joueur.append(username2)
        elif type2 == "IA":
            username2 = "ordinateur2"
            liste_joueur.append("ordinateur2")
    if type3 != "Vide":
        if type3 == "H":
            liste_joueur.append(username3)
        elif type3 == "IA":
            username3 = "ordinateur3"
            liste_joueur.append("ordinateur3")
    if type4 != "Vide":
        if type4 == "H":
            liste_joueur.append(username4)
        elif type4 == "IA":
            username4 = "ordinateur4"
            liste_joueur.append("ordinateur4")
    c = get_db_connection()
    data = (nb_partie, 0, username1, username2, username3, username4, 0, 0, 0, 0, niveau)
    c.execute("INSERT INTO partie VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    for j in range(len(liste_joueur)):
        data2 = (nb_partie, liste_joueur[j], j+1, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)
        c.execute("INSERT INTO partie_en_cours VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data2)
    data3 = (nb_partie, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    c.execute("INSERT INTO plateau VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data3)
    c.commit()
    return affichage(str(nb_partie))


@app.route("/partie/<int:id>", methods=['GET', 'POST'])
def affiche_plateau(id:str):
    # recuperation du plateau
    c = get_db_connection().cursor()
    c.execute("SELECT L0C0, L0C1, L0C2, L0C3, L0C4, L0C5, L0C6, L0C7, L0C8, L0C9, L0C10, L0C11, L0C12, L0C13, L0C14, L0C15, L0C16, L0C17, L0C18, L0C19, L1C0, L1C1, L1C2, L1C3, L1C4, L1C5, L1C6, L1C7, L1C8, L1C9, L1C10, L1C11, L1C12, L1C13, L1C14, L1C15, L1C16, L1C17, L1C18, L1C19, L2C0, L2C1, L2C2, L2C3, L2C4, L2C5, L2C6, L2C7, L2C8, L2C9, L2C10, L2C11, L2C12, L2C13, L2C14, L2C15, L2C16, L2C17, L2C18, L2C19, L3C0, L3C1, L3C2, L3C3, L3C4, L3C5, L3C6, L3C7, L3C8, L3C9, L3C10, L3C11, L3C12, L3C13, L3C14, L3C15, L3C16, L3C17, L3C18, L3C19, L4C0, L4C1, L4C2, L4C3, L4C4, L4C5, L4C6, L4C7, L4C8, L4C9, L4C10, L4C11, L4C12, L4C13, L4C14, L4C15, L4C16, L4C17, L4C18, L4C19, L5C0, L5C1, L5C2, L5C3, L5C4, L5C5, L5C6, L5C7, L5C8, L5C9, L5C10, L5C11, L5C12, L5C13, L5C14, L5C15, L5C16, L5C17, L5C18, L5C19, L6C0, L6C1, L6C2, L6C3, L6C4, L6C5, L6C6, L6C7, L6C8, L6C9, L6C10, L6C11, L6C12, L6C13, L6C14, L6C15, L6C16, L6C17, L6C18, L6C19, L7C0, L7C1, L7C2, L7C3, L7C4, L7C5, L7C6, L7C7, L7C8, L7C9, L7C10, L7C11, L7C12, L7C13, L7C14, L7C15, L7C16, L7C17, L7C18, L7C19, L8C0, L8C1, L8C2, L8C3, L8C4, L8C5, L8C6, L8C7, L8C8, L8C9, L8C10, L8C11, L8C12, L8C13, L8C14, L8C15, L8C16, L8C17, L8C18, L8C19, L9C0, L9C1, L9C2, L9C3, L9C4, L9C5, L9C6, L9C7, L9C8, L9C9, L9C10, L9C11, L9C12, L9C13, L9C14, L9C15, L9C16, L9C17, L9C18, L9C19, L10C0, L10C1, L10C2, L10C3, L10C4, L10C5, L10C6, L10C7, L10C8, L10C9, L10C10, L10C11, L10C12, L10C13, L10C14, L10C15, L10C16, L10C17, L10C18, L10C19, L11C0, L11C1, L11C2, L11C3, L11C4, L11C5, L11C6, L11C7, L11C8, L11C9, L11C10, L11C11, L11C12, L11C13, L11C14, L11C15, L11C16, L11C17, L11C18, L11C19, L12C0, L12C1, L12C2, L12C3, L12C4, L12C5, L12C6, L12C7, L12C8, L12C9, L12C10, L12C11, L12C12, L12C13, L12C14, L12C15, L12C16, L12C17, L12C18, L12C19, L13C0, L13C1, L13C2, L13C3, L13C4, L13C5, L13C6, L13C7, L13C8, L13C9, L13C10, L13C11, L13C12, L13C13, L13C14, L13C15, L13C16, L13C17, L13C18, L13C19, L14C0, L14C1, L14C2, L14C3, L14C4, L14C5, L14C6, L14C7, L14C8, L14C9, L14C10, L14C11, L14C12, L14C13, L14C14, L14C15, L14C16, L14C17, L14C18, L14C19, L15C0, L15C1, L15C2, L15C3, L15C4, L15C5, L15C6, L15C7, L15C8, L15C9, L15C10, L15C11, L15C12, L15C13, L15C14, L15C15, L15C16, L15C17, L15C18, L15C19, L16C0, L16C1, L16C2, L16C3, L16C4, L16C5, L16C6, L16C7, L16C8, L16C9, L16C10, L16C11, L16C12, L16C13, L16C14, L16C15, L16C16, L16C17, L16C18, L16C19, L17C0, L17C1, L17C2, L17C3, L17C4, L17C5, L17C6, L17C7, L17C8, L17C9, L17C10, L17C11, L17C12, L17C13, L17C14, L17C15, L17C16, L17C17, L17C18, L17C19, L18C0, L18C1, L18C2, L18C3, L18C4, L18C5, L18C6, L18C7, L18C8, L18C9, L18C10, L18C11, L18C12, L18C13, L18C14, L18C15, L18C16, L18C17, L18C18, L18C19, L19C0, L19C1, L19C2, L19C3, L19C4, L19C5, L19C6, L19C7, L19C8, L19C9, L19C10, L19C11, L19C12, L19C13, L19C14, L19C15, L19C16, L19C17, L19C18, L19C19 FROM plateau WHERE id_partie = :val", {'val':id})
    plateautemp = []
    for case in c.fetchone():
        plateautemp.append(f'{case}')
    board = []
    for i in range(20):
        ligne = []
        for j in range(20):
            ligne.append(int(plateautemp[i*20+j]))
        board.append(ligne)
    #print(board)
    c.close()
    
    # recuperation de la liste des joueurs
    c = get_db_connection().cursor()
    c.execute("SELECT j1, j2, j3, j4 FROM partie WHERE id_partie = :val", {'val':id})
    liste_joueur = []
    for tpl in c.fetchone():
        if f'{tpl}' != 'Vide':
            liste_joueur.append(f'{tpl}')
    c.close()
    #print(liste_joueur)
    
    donnees_joueurs = []
    for joueur in range(len(liste_joueur)):
        if liste_joueur[joueur] != 'Vide':
    #recuperation des donnees du joueur 1
            c = get_db_connection().cursor()
            donnees = []
            c.execute("SELECT * FROM partie_en_cours WHERE id_partie = :val AND pseudo = :val2", {'val':id, 'val2':liste_joueur[joueur]})
            for elm in c.fetchone():
                donnees.append(f'{elm}')
            c.close()
            donnees_joueurs.append(donnees)
    #print(donnees_joueurs)
    
    # recuperation du tour
    c = get_db_connection().cursor()
    c.execute("SELECT tour FROM partie WHERE id_partie = :val", {'val':id})
    for elm in c.fetchone():
        tour = int(f'{elm}')
    c.close()
    #print(tour)
    
    # recuperation du nombre de coup deja joues
    c = get_db_connection().cursor()
    c.execute("SELECT nb_coup FROM partie WHERE id_partie = :val", {'val':id})
    for truc in c.fetchone():
        nb_coup = int(f'{truc}')
    c.close()
    #print(nb_coup)
    
    # recuperation du nombre de joueur qui ont passer à la suite
    c = get_db_connection().cursor()
    c.execute("SELECT nb_passer FROM partie WHERE id_partie = :val", {'val':id})
    for truc in c.fetchone():
        passer = int(f'{truc}')
    c.close()
    #print(passer)
    
    c = get_db_connection().cursor()
    c.execute("SELECT niveau FROM partie WHERE id_partie = :val", {'val':id})
    for truc in c.fetchone():
        niveau = int(f'{truc}')
    c.close()

    donnees_joueur_actif = donnees_joueurs[tour]
    donnees_joueur_actif[0] = int(donnees_joueur_actif[0])
    if donnees_joueur_actif[1] != 'ordinateur2' and donnees_joueur_actif[1] != 'ordinateur3' and donnees_joueur_actif[1] != 'ordinateur4':
        numpiece = request.form["numpiece"]
        nbrotation = request.form["rotation"]
        recto_verso = request.form["rectoverso"]
        ligne = request.form["ligne"]
        colonne = request.form["colonne"]
        passer_tour = request.form["passer"]
    else:
        liste_classes = []
        j1 = joueur_humain(donnees_joueurs[0][1], int(donnees_joueurs[0][2]))
        liste_classes.append(j1)
        if len(donnees_joueurs) == 2:
            j2 = donnees_joueur_to_joueur(donnees_joueurs[1])
            liste_classes.append(j2)
            party = partie(0, j1, j2, 'Vide', 'Vide', False, len(donnees_joueurs))
        elif len(donnees_joueurs) == 3:  
            j2 = donnees_joueur_to_joueur(donnees_joueurs[1])
            liste_classes.append(j2)
            j3 = donnees_joueur_to_joueur(donnees_joueurs[2])
            liste_classes.append(j3)
            party = partie(0, j1, j2, j3, 'Vide', False, len(donnees_joueurs))
        elif len(donnees_joueurs) == 4:    
            j2 = donnees_joueur_to_joueur(donnees_joueurs[1])
            liste_classes.append(j2)
            j3 = donnees_joueur_to_joueur(donnees_joueurs[2])
            liste_classes.append(j3)
            j4 = donnees_joueur_to_joueur(donnees_joueurs[3])
            liste_classes.append(j4)
            party = partie(0, j1, j2, j3, j4, False, len(donnees_joueurs))
        party.plateau = board
        if niveau == 1:
            numpiece, passer_tour, nbrotation, recto_verso, ligne, colonne = coup_aleatoire(party, liste_classes[tour])
        else:
            numpiece, passer_tour, nbrotation, recto_verso, ligne, colonne = choisir_coup_ia_alphabeta(party, liste_classes[tour], niveau-1)
    if passer_tour == "0" or passer_tour == False:
        numpiece = int(numpiece)
        nbrotation, recto_verso = int(nbrotation), int(recto_verso)
        ligne, colonne = int(ligne), int(colonne)
        piece = applique_changement(numpiece, nbrotation, recto_verso)
        if test_ajout_piece(donnees_joueur_actif, numpiece, piece, ligne, colonne, board, nb_coup, len(donnees_joueurs)):
            #print("je joue le coup")
            board2, donnees_joueur_actif = resolution_coup(donnees_joueur_actif, numpiece, piece, ligne, colonne, board, nb_coup, len(donnees_joueurs))
            c = get_db_connection()
            grille = [id]
            for i in range(len(board2)):
                for j in range(len(board2)):
                    grille.append(board2[i][j])
            #print(id, liste_joueur[tour])
            #print(donnees_joueur_actif)
            c.execute("DELETE from plateau WHERE id_partie = :val", {'val':id})
            c.execute("INSERT INTO plateau VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", grille)
            c.execute("DELETE from partie_en_cours WHERE id_partie = :val1 AND pseudo = :val2", {'val1':id, 'val2':str(liste_joueur[tour])})
            c.execute("INSERT INTO partie_en_cours VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", donnees_joueur_actif)
            c.execute("INSERT INTO coup VALUES(?, ?, ?, ?, ?, ?, ?)", (id, nb_coup, numpiece, ligne, colonne, nbrotation, recto_verso))
            tour += 1
            if tour > len(donnees_joueurs)-1:
                tour = 0
            c.execute("UPDATE partie SET tour = :nv_valeur WHERE id_partie = :val", {'nv_valeur':tour, 'val':id})
            c.execute("UPDATE partie SET nb_coup=nb_coup+1 WHERE id_partie = :val", {'val':id})
            c.execute("UPDATE partie SET nb_passer=0 WHERE id_partie = :val", {'val':id})
            c.commit()
            c.close()
            return render_template("menu.html", id_partie=id, board=board2 , donnees_joueurs=donnees_joueurs, tour=tour, liste_pieces=liste_pieces)
        else:
            return render_template("menu.html", id_partie=id, board=board , donnees_joueurs=donnees_joueurs, tour=tour, liste_pieces=liste_pieces)
    elif passer_tour == "1" or passer_tour == True:
        passer += 1
        tour += 1
        if tour > len(donnees_joueurs)-1:
            tour = 0
        if passer == len(donnees_joueurs):
            score = []
            for j in range(len(donnees_joueurs)):
                score.append((donnees_joueurs[j][1], compter_points(donnees_joueurs[j])))
            #print(score)
            gagnants = gagner(score)
            #print(gagnants)
            c = get_db_connection()
            c.execute("UPDATE partie SET terminee = True WHERE id_partie = :val", {'val':id})
            c.commit()
            c.close()
            return render_template("finDePartie.html", liste_joueur=liste_joueur, score=score, gagnants=gagnants)
        c = get_db_connection()
        c.execute("UPDATE partie SET tour = :nv_valeur WHERE id_partie = :val", {'nv_valeur':tour, 'val':id})
        c.execute("UPDATE partie SET nb_coup=nb_coup+1 WHERE id_partie = :val", {'val':id})
        c.execute("UPDATE partie SET nb_passer=nb_passer+1 WHERE id_partie = :val", {'val':id})
        c.commit()
        c.close()
    return render_template("menu.html", id_partie=id, board=board , donnees_joueurs=donnees_joueurs, tour=tour, liste_pieces=liste_pieces)

def affichage(id:str):
    # recuperation du plateau
    c = get_db_connection().cursor()
    c.execute("SELECT L0C0, L0C1, L0C2, L0C3, L0C4, L0C5, L0C6, L0C7, L0C8, L0C9, L0C10, L0C11, L0C12, L0C13, L0C14, L0C15, L0C16, L0C17, L0C18, L0C19, L1C0, L1C1, L1C2, L1C3, L1C4, L1C5, L1C6, L1C7, L1C8, L1C9, L1C10, L1C11, L1C12, L1C13, L1C14, L1C15, L1C16, L1C17, L1C18, L1C19, L2C0, L2C1, L2C2, L2C3, L2C4, L2C5, L2C6, L2C7, L2C8, L2C9, L2C10, L2C11, L2C12, L2C13, L2C14, L2C15, L2C16, L2C17, L2C18, L2C19, L3C0, L3C1, L3C2, L3C3, L3C4, L3C5, L3C6, L3C7, L3C8, L3C9, L3C10, L3C11, L3C12, L3C13, L3C14, L3C15, L3C16, L3C17, L3C18, L3C19, L4C0, L4C1, L4C2, L4C3, L4C4, L4C5, L4C6, L4C7, L4C8, L4C9, L4C10, L4C11, L4C12, L4C13, L4C14, L4C15, L4C16, L4C17, L4C18, L4C19, L5C0, L5C1, L5C2, L5C3, L5C4, L5C5, L5C6, L5C7, L5C8, L5C9, L5C10, L5C11, L5C12, L5C13, L5C14, L5C15, L5C16, L5C17, L5C18, L5C19, L6C0, L6C1, L6C2, L6C3, L6C4, L6C5, L6C6, L6C7, L6C8, L6C9, L6C10, L6C11, L6C12, L6C13, L6C14, L6C15, L6C16, L6C17, L6C18, L6C19, L7C0, L7C1, L7C2, L7C3, L7C4, L7C5, L7C6, L7C7, L7C8, L7C9, L7C10, L7C11, L7C12, L7C13, L7C14, L7C15, L7C16, L7C17, L7C18, L7C19, L8C0, L8C1, L8C2, L8C3, L8C4, L8C5, L8C6, L8C7, L8C8, L8C9, L8C10, L8C11, L8C12, L8C13, L8C14, L8C15, L8C16, L8C17, L8C18, L8C19, L9C0, L9C1, L9C2, L9C3, L9C4, L9C5, L9C6, L9C7, L9C8, L9C9, L9C10, L9C11, L9C12, L9C13, L9C14, L9C15, L9C16, L9C17, L9C18, L9C19, L10C0, L10C1, L10C2, L10C3, L10C4, L10C5, L10C6, L10C7, L10C8, L10C9, L10C10, L10C11, L10C12, L10C13, L10C14, L10C15, L10C16, L10C17, L10C18, L10C19, L11C0, L11C1, L11C2, L11C3, L11C4, L11C5, L11C6, L11C7, L11C8, L11C9, L11C10, L11C11, L11C12, L11C13, L11C14, L11C15, L11C16, L11C17, L11C18, L11C19, L12C0, L12C1, L12C2, L12C3, L12C4, L12C5, L12C6, L12C7, L12C8, L12C9, L12C10, L12C11, L12C12, L12C13, L12C14, L12C15, L12C16, L12C17, L12C18, L12C19, L13C0, L13C1, L13C2, L13C3, L13C4, L13C5, L13C6, L13C7, L13C8, L13C9, L13C10, L13C11, L13C12, L13C13, L13C14, L13C15, L13C16, L13C17, L13C18, L13C19, L14C0, L14C1, L14C2, L14C3, L14C4, L14C5, L14C6, L14C7, L14C8, L14C9, L14C10, L14C11, L14C12, L14C13, L14C14, L14C15, L14C16, L14C17, L14C18, L14C19, L15C0, L15C1, L15C2, L15C3, L15C4, L15C5, L15C6, L15C7, L15C8, L15C9, L15C10, L15C11, L15C12, L15C13, L15C14, L15C15, L15C16, L15C17, L15C18, L15C19, L16C0, L16C1, L16C2, L16C3, L16C4, L16C5, L16C6, L16C7, L16C8, L16C9, L16C10, L16C11, L16C12, L16C13, L16C14, L16C15, L16C16, L16C17, L16C18, L16C19, L17C0, L17C1, L17C2, L17C3, L17C4, L17C5, L17C6, L17C7, L17C8, L17C9, L17C10, L17C11, L17C12, L17C13, L17C14, L17C15, L17C16, L17C17, L17C18, L17C19, L18C0, L18C1, L18C2, L18C3, L18C4, L18C5, L18C6, L18C7, L18C8, L18C9, L18C10, L18C11, L18C12, L18C13, L18C14, L18C15, L18C16, L18C17, L18C18, L18C19, L19C0, L19C1, L19C2, L19C3, L19C4, L19C5, L19C6, L19C7, L19C8, L19C9, L19C10, L19C11, L19C12, L19C13, L19C14, L19C15, L19C16, L19C17, L19C18, L19C19 FROM plateau WHERE id_partie = :val", {'val':id})
    plateautemp = []
    for case in c.fetchone():
        plateautemp.append(f'{case}')
    board = []
    for i in range(20):
        ligne = []
        for j in range(20):
            ligne.append(int(plateautemp[i*20+j]))
        board.append(ligne)
    #print(board)
    c.close()
    
    # recuperation de la liste des joueurs
    c = get_db_connection().cursor()
    c.execute("SELECT j1, j2, j3, j4 FROM partie WHERE id_partie = :val", {'val':id})
    liste_joueur = []
    for tpl in c.fetchone():
        liste_joueur.append(f'{tpl}')
    c.close()
    #print(liste_joueur)
    
    donnees_joueurs = []
    for joueur in range(len(liste_joueur)):
        if liste_joueur[joueur] != 'Vide':
    #recuperation des donnees du joueur 1
            c = get_db_connection().cursor()
            donnees = []
            c.execute("SELECT * FROM partie_en_cours WHERE id_partie = :val AND pseudo = :val2", {'val':id, 'val2':liste_joueur[joueur]})
            for elm in c.fetchone():
                donnees.append(f'{elm}')
            c.close()
            donnees_joueurs.append(donnees)

    # recuperation du tour
    c = get_db_connection().cursor()
    c.execute("SELECT tour FROM partie WHERE id_partie = :val", {'val':id})
    for elm in c.fetchone():
        tour = int(f'{elm}')
    c.close()
    #print(tour)
    
    # recuperation du nombre de coup deja joues
    c = get_db_connection().cursor()
    c.execute("SELECT nb_coup FROM partie WHERE id_partie = :val", {'val':id})
    for truc in c.fetchone():
        nb_coup = int(f'{truc}')
    c.close()
    #print(nb_coup)
    
    # recuperation du nombre de joueur qui ont passer à la suite
    c = get_db_connection().cursor()
    c.execute("SELECT nb_passer FROM partie WHERE id_partie = :val", {'val':id})
    for truc in c.fetchone():
        passer = int(f'{truc}')
    c.close()
    #print(passer)
    return render_template("menu.html", id_partie=id, liste_joueur=liste_joueur, board=board , donnees_joueurs=donnees_joueurs, tour=tour, liste_pieces=liste_pieces)


def affichage_plateau_coup(id_partie, n):
    # fonction prenant en argument un id de partie et un numéro de coup n et qui renvoie
    # le plateau de la partie concernée après le n-ième coup
    plateau = [ [0 for i in range(20)]for i in range(20) ] # plateau initial
    liste_coup = db.execute("SELECT * FROM coup WHERE id_partie=? ORDER BY num_coup", id_partie) # liste de dictionnaires
    nb_coup_partie=len(liste_coup)
    if n > nb_coup_partie:
        return affichage_plateau_coup(id_partie, nb_coup_partie)
    if n < 0:
        return affichage_plateau_coup(id_partie, 0)
    nb_joueur=nb_joueur2(id_partie)
    for i in range(n):
        num_pièce=liste_coup[i]['num_piece']
        ligne=liste_coup[i]['ligne']
        colonne=liste_coup[i]['colonne']
        num_rotation=liste_coup[i]['num_rotation']
        rectoverso=liste_coup[i]['rectoverso']
        piece=applique_changement(num_pièce, num_rotation, rectoverso)
        num_joueur= (i+1)%nb_joueur
        if num_joueur == 0:
            num_joueur=nb_joueur
        plateau = resolution_coup2(num_joueur, num_pièce, piece, ligne, colonne, plateau )
    return plateau

def nb_joueur2(id_partie):
    game=db.execute("SELECT * FROM partie WHERE id_partie=?", id_partie)
    nb_joueur=0
    for i in range(1, 5):     
        if game[0]['j'+str(i)] != 'Vide':
            nb_joueur+=1
    return nb_joueur

@app.route("/historique_partie/<id_partie>/<coup>")
def voir_partie(id_partie, coup):
    board=[ [0 for i in range(20)]for i in range(20) ]
    id_partie=int(id_partie)
    coup=int(coup)
    nb_coup=db.execute("SELECT nb_coup FROM partie WHERE id_partie=?", id_partie)[0]['nb_coup']
    if coup!=0:
        board=affichage_plateau_coup(id_partie, coup)
    return render_template('visionnage_plateau.html', board=board, num_coup=coup, id_partie=id_partie, nb_coup=nb_coup)

if __name__=="__main__":
    app.run(debug=True)
