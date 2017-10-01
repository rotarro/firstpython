from flask import Flask
from flask import request
from flask import render_template
from examples.twitter.api import crawling_twitter_mention

app = Flask(__name__)

@app.route('/main')
@app.route('/main<name>')
def main():
	return render_template('index.html')

	return crawling_twitter_mention()