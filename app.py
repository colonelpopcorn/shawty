from flask import Flask,redirect
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello, World!'

@app.route('/<link_id>')
def redirect_to_route(link_id):
	print(link_id)
	return redirect('https://www.example.com', code=302)