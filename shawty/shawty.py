import os
import sqlite3
from flask import Flask,session,redirect

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

@app.route('/')
def hello():
	return 'Needs to be a static SPA.'

@app.route('/login')
def login():
	return 'Login route'

@app.route('/modify')
def add():
	return 'Route for all url modifications, RESTful doncha know.'

@app.route('/<link_id>')
def redirect_to_route(link_id):
	print(link_id)
	return redirect('https://www.example.com', code=302)