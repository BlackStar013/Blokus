from flask import Flask, session
from flask import g

import sqlite3

DATABASE = 'data/blokus.db'
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db   


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/partie')
def selection_db():
    c = get_db().cursor()
    c.execute("select * from partie")
    content = '<ul>'
    for tpl in c.fetchall():
        content += '<li>'
        content += f'{tpl}'
        content += '</li>'
    content += '</ul>'
    return content

@app.route('/test')
def ajout_elements_db():
    c = get_db()
    id = int(input("donner une id de partie : "))
    j1 = str(input("donnez un premier joueur : "))
    j2 = str(input("donnez un deuxième joueur : "))
    j3 = str(input("donnez un troisième joueur : "))
    j4 = str(input("donnez un quatrième joueur : "))
    heure = int(input("quelle heure est-il : "))
    finie = bool(input("est-ce que la partie est finie : "))
    data = (id, j1, j2, j3, j4, heure, finie)
    c.execute("insert into partie values(?, ?, ?, ?, ?, ?, ?)", data)
    c.commit()
    c = get_db().cursor()
    c.execute("select * from partie")
    content = '<ul>'
    for tpl in c.fetchall():
        content += '<li>'
        content += f'{tpl}'
        content += '</li>'
        content += '</ul>'
    c.close()
    return content

@app.route('/toutsupprimer')
def tout_supprimer():
    c = get_db()
    c.execute("delete from partie")
    c.commit()
    c.close()
    return "a plus"