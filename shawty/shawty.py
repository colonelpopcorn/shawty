import os
import sqlite3
from flask import Flask,session,redirect,request,jsonify
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

def get_db_conn():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def get_rows_from_db(query, args):
    conn = get_db_conn()
    cursor = conn.execute(query, args)
    rows = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return rows

def valid_login(json):
    query = """SELECT * FROM `users` WHERE `username`=? LIMIT 1"""
    user = json.get('uname')
    rows = get_rows_from_db(query, [user])
    user_row = None
    if len(rows) > 0:
        user_row = rows[0]
    if user_row is not None and user == user_row['username'] and pwd_context.verify(json.get('passwd'), user_row['password']):
        return True
    else:
        return False
        
def can_register_user(json):
    query = """SELECT * FROM `users` WHERE `username`=? LIMIT 1"""
    user = json.get("uname")
    rows = get_rows_from_db(query, [user])
    return (len(rows) == 0)

def register_user_with_db(json):
    something = True

@app.route('/', methods=['GET'])
def home():
    return app.send_static_file('index.html')

@app.route('/api/login', methods=['POST'])
def login():
    if valid_login(request.get_json()):
        return jsonify(msg="Logged in!", status=200)
    else:
        return jsonify(msg="Unable to login!", status=404)

@app.route('/<link_id>', methods=['GET'])
def redirect_to_url(link_id):
    query = """SELECT * FROM `urls` WHERE `hash`=? LIMIT 1"""
    rows = get_rows_from_db(query, [link_id])
    if (len(rows) > 0):
        return redirect(rows[0]['redirect_url'], 302)
    else:
        return jsonify(msg="ERROR: url not found! Unable to redirect", status=404)

@app.route('/api/register', methods=['POST'])
def register_user():
    json = request.get_json()
    if can_register_user(json):
        register_user_with_db(json)
        return jsonify(msg="Success! {0} has been successfully registered!".format(json.get("uname")),status=200)
    else:
        return jsonify(msg="Cannot register user!",status=404)
    