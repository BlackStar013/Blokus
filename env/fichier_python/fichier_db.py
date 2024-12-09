from flask import Flask
from flask import session
from flask import g

import sqlite3

DATABASE = 'blokus.db' # le nom du fichier de votre base sqlite3
app = Flask(__name__)

def get_db(): 
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
'''
@app.teardown_appcontext
def close_connection(exception): # pour fermer la connexion proprement
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
'''
@app.route('/')
def afficher_table():
    c = get_db().cursor() # on crée un curseur
    c.execute("select * from partie") # on exécute la requête
    
    content = '<b>Truc'
    content += '<ul>'
    for tpl in c.fetchall(): # on parcours les tuples résultat 1 par 1
        content += f'<li>{tpl}</li>'
        content += '</ul>'
    return content

'''
@app.route('/test')
def ajout_table():
    #c = get_db().cursor()
    #c.execute()
    db = getattr(g, '_database', None)
    db.session.add((5, "None", "None", "None", "None", 12, 0))
    db.session.commit()
'''