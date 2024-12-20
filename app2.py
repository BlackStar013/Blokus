from flask import Flask, render_template, request, url_for, flash
import sqlite3
from classes import *

Snitch = joueur_humain("Snitch", 1)
Bouthier = joueur_humain("Bouthier", 2)
Heurtel = joueur_humain("Heurtel", 3)
Tomczak = joueur_humain("Tomczak", 4)
liste_joueur = [Snitch, Bouthier, Heurtel, Tomczak]

app = Flask(__name__)
board = [ [0 for i in range(20)]for i in range(20) ]

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

piece = [ [0,0,0], [1,1,1], [2,2,2], [0,0,0] ]
@app.route("/menu")
def affiche_plateau():
    return render_template("menutest.html", board=board , liste_joueur=liste_joueur)


if __name__=="__main__":
    app.run(debug=True)
