from flask import Flask,redirect
app = Flask(__name__)

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