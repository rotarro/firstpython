from flask import Flask
from flask import request
from flask import render_template
import api

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'


@app.route('/add')
def add():
	a = int(request.args.get(a))
    a = int(request.args.get('a'))
    b = int(request.args.get(b))
    return a + b

@app.route('/main')
@app.route('/main<name>')
def main():
	return render_template('index.html')
	

if __name__ == "__main__":
	app.jinja_jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(debug=True,use_reloader = True)

