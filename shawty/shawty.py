import os
import sqlite3
from flask import Flask,session,redirect,request

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'shawty.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='somepass'
))
app.config.from_envvar('SHAWTY_SETTINGS', silent=True)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def valid_login(json):
    if json.get('uname') == "bob" and json.get('passwd') == "bobsupersecret":
        return True
    else:
        return False

@app.route('/', methods=['GET'])
def home():
    return app.send_static_file('index.html')

@app.route('/api/login', methods=['POST'])
def login():
    if valid_login(request.get_json()):
        return "Good!"
    else:
        return "Bad!", 404