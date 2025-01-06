from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from main import *
from classes import *
from cs50 import SQL

Snitch = joueur_humain("Snitch", 1)
Bouthier = joueur_humain("Bouthier", 2)
Heurtel = joueur_humain("Heurtel", 3)
Tomczak = joueur_humain("Tomczak", 4)
liste_joueur = [Snitch, Bouthier, Heurtel, Tomczak]
partie = partie(13, "7janvier", "3hdumat", Snitch, Bouthier, Heurtel, Tomczak, False)

app = Flask(__name__)
board = partie.plateau

@app.route('/')
def page_accueil():
    return render_template("index.html")

@app.route('/sigin')
def page_signin():
    return render_template("signin.html")

@app.route('/login')
def page_login():
    return render_template("login.html")


def get_db_connection():
    connection = sqlite3.connect('joueur.db')
    connection.row_factory = sqlite3.Row  # résultats sous forme de dictionnaires
    return connection


@app.route('/login', methods=['POST', 'GET'])
def home_after_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = get_db_connection()
        profil = connection.execute("SELECT pseudo, mdp FROM joeur WHERE pseudo = ?", (username,)).fetchone()
        connection.close()
        if profil != None:
            if password == profil[1] and username == profil[0] :
                return render_template('parties.html')
            else:
                return render_template('login.html')
        else:
            return render_template('login.html')

@app.route("/sign_in")
def sign_in():
    return render_template("sign_in.html")

@app.route("/sign_in", methods=['GET', 'POST'])
def sign_in2():
    username = request.form["pseudo"]
    password = request.form["mdp"]
    connection = get_db_connection()
    profil = connection.execute("SELECT pseudo, mot_de_passe FROM utilisateur WHERE pseudo = ?", (username,)).fetchone()
    connection.close()
    if username and password :
        if not connection.execute("SELECT pseudo FROM utilisateur WHERE pseudo=?;", username):
            connection.execute("INSERT INTO utilisateur (pseudo, password) VALUES (?, ?);", username, password)
            return render_template("login.html")
        else :
            return "Pseudo déjà utilisé"
    return render_template("sign_in.html")

@app.route("/menutest", methods=['GET', 'POST'])
def affiche_plat_init():
    return render_template("menutest.html", board=board, liste_joueur=liste_joueur)

@app.route("/menu", methods=['GET', 'POST'])
def affiche_plateau():
    j = request.form["joueur"]
    numpiece = request.form["numpiece"]
    ligne = request.form["ligne"]
    colonne = request.form["colonne"]
    if j and numpiece and ligne and colonne:
        print("coup jouer")
        j, numpiece = int(j), int(numpiece)
        ligne, colonne = int(ligne), int(colonne)
        print(partie.plateau)
        if test_ajout_piece(liste_joueur[j], numpiece, liste_joueur[j].liste_pieces[numpiece], ligne, colonne, partie):
            print("coup possible")
            board2 = resolution_coup(liste_joueur[j], numpiece, liste_joueur[j].liste_pieces[numpiece], ligne, colonne, partie)
            return render_template("menu.html", board=board2 , liste_joueur=liste_joueur)
        else:
            print('coup impossible')
            return render_template("menu.html", board=board , liste_joueur=liste_joueur)
    return render_template("menu.html", board=board , liste_joueur=liste_joueur)


if __name__=="__main__":
    app.run(debug=True)


db =SQL("sqlite:///blokus.db")
@app.route("/historique_partie")
def historique_partie():
    parties=db.execute("SELECT * FROM partie") #Liste de dictionnaires contenant les données relatives à une partie (joueurs, date etc...)
    return render_template('historique_partie.html', parties=parties)
print(db)

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
        if game[0]['j'+str(i)]!=None:
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