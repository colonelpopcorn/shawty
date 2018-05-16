import os
import sqlite3
from flask import Flask,session,redirect,request
from passlib.apps import custom_app_context as pwd_context

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'shawty.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='somepass',
    SALT='somesalt'
))
app.config.from_envvar('SHAWTY_SETTINGS', silent=True)

def valid_login(json):
    query = """SELECT * FROM users WHERE username LIKE ?"""
    user = json.get('uname')
    hashedPwd = pwd_context.hash(json.get('passwd'))
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.execute(query, user)
    if json.get('uname') == "bob" and hashedPwd == "$6$rounds=656000$4.duBrT786/TT3B0$up2G6MH9d9yTKCJbd/kn/gvMNJ.ZkaFWqZjdMhLOBLtrOJ.4GxHzF8ehJ6ABwCNOePdd8DAeGsrw5qLCFk6Ml1":
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