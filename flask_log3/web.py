from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__)
app.jinja_env.globals.update(enumerate=enumerate)



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
            if password == profil[1] and username == profil[0]:
                return render_template('parties.html', board=board, pieces=pieces)
            else:
                return render_template('login.html')
        else:
            return render_template('login.html')



board = [[0 for _ in range(20)] for _ in range(20)]

@app.route('/menu',methods=['POST', 'GET'])
def plateau():
    return render_template("menu.html", board=board)

pieces = {
    "L": [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
}

@app.route('/creer_partie')
def page_creer_partie():
    return render_template("créer_partie.html")

@app.route('/rejoindre_partie')
def page_rejoindre_partie():
    return render_template("rejoindre_partie.html")




if __name__ == '__main__':
    app.run(debug=True)
