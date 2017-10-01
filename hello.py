from flask import Flask
app = Flask(__name__)

print ('a')

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/help')
def help():
	return 'help me to build sth'

