from flask import Flask, render_template, request, url_for, flash
import sqlite3

app = Flask(__name__)


@app.route('/')
def page_accueil():
    return render_template("index.html")

@app.route('/sigin')
def page_signin():
    return render_template("signin.html")

@app.route('/login')
def page_login():
    return render_template("login.html")

def récupère_bd():
    connexion= sqlite3.connect(r'./joeur.db')
    query= 'SELECT pseudo, mdp FROM joeur'
    joeur=connexion.execute(query).fetchall() #liste de tuples ici
    connexion.close()
    return joeur

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




if __name__=="__main__":
    app.run(debug=True)
