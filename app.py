from flask import Flask, render_template, request
from cs50 import SQL

db =SQL("sqlite:///blokus.db")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login", methods=['GET', 'POST'])
def login2():
    identifiant = request.form["identifiant"]
    password = request.form["password"]
    if identifiant and password :
        vrai_mdp = db.execute("SELECT password FROM utilisateur WHERE pseudo = ?", identifiant)
        if str(vrai_mdp[0]['password']) == password :
            return render_template("menu_principal.html")
        else :
            return "Mot de passe ou identifiant incorrect"
    return render_template("login.html")

@app.route("/sign_in")
def sign_in():
    return render_template("sign_in.html")

@app.route("/sign_in", methods=['GET', 'POST'])
def sign_in2():
    identifiant = request.form["identifiant"]
    password = request.form["password"]
    if request.method == 'POST':
        if identifiant and password :
            if not db.execute("SELECT pseudo FROM utilisateur WHERE pseudo=?;", identifiant):
                db.execute("INSERT INTO utilisateur (pseudo, password) VALUES (?, ?);", identifiant, password)
                return render_template("login.html")
            else :
                return "Pseudo déjà utilisé"
    return render_template("sign_in.html")
