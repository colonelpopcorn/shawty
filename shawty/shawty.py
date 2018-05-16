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
    query = """SELECT * FROM `users` WHERE `username`=?"""
    user = json.get('uname')
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    cursor = conn.execute(query, [user])
    rows = cursor.fetchall()
    user_row = []
    for row in rows:
        user_row = row
        print()
    conn.commit()
    cursor.close()
    conn.close()
    if user_row != [] and user == user_row['username'] and pwd_context.verify(json.get('passwd'), user_row['password']):
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