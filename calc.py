from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

FIRST_OPERAND = 'a'
SECOND_OPERAND = 'b'

def parse_operand(req):
	return (int(req.args.get(FIRST_OPERAND)), int(req.args.get(SECOND_OPERAND)))

@app.route('/add')
def add():
	operands = parse_operand(request)	
	return str(operands[0] + operands[1])

@app.route('/minus')
def minus():
	operands = parse_operand(request)	
	return str(operands[0] - operands[1])

@app.route('/multiple')
def multiple():
	operands = parse_operand(request)	
	return str(operands[0] * operands[1])

@app.route('/devide')
def devide():
	operands = parse_operand(request)	
	return str(operands[0] / operands[1])

@app.route('/main')
@app.route('/main<name>')
def main():
	return render_template('index.html')

if __name__ == "__main__":
	app.jinja_jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(debug=True,use_reloader = True)

