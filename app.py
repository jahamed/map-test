#!/usr/bin/env python3

from flask import Flask
from flask import render_template
from flask_sqlalchemy import flask_sqlalchemy

app = Flask(__name__,
			template_folder="templates",
            static_folder="static")

@app.route("/ping")
def sanity_check():
	return "pong"

@app.route("/")
def homepage():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True, port=5000)