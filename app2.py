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
    if request.method == 'POST':
        if username and password :
            if not db.execute("SELECT pseudo FROM utilisateur WHERE pseudo=?;", username):
                db.execute("INSERT INTO utilisateur (pseudo, password) VALUES (?, ?);", username, password)
                return render_template("login.html")
            else :
                return "Pseudo déjà utilisé"
    return render_template("sign_in.html")



if __name__=="__main__":
    app.run(debug=True)
