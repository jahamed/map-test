#!/usr/bin/env python3

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,
			template_folder="templates",
            static_folder="static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.sqlite3'
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)

class School(db.Model):
	__tablename__ = 'schools-geocoded'
	__table_args__ = { 'extend_existing': True }
	LOC_CODE = db.Column(db.Text, primary_key=True)   

#####

@app.route("/ping")
def sanity_check():
	return "pong"

@app.route("/")
def homepage():
	print("Total number of schools is", School.query.count())

	school = School.query.filter_by(LOC_CODE='X270').first()
	print("School's name is", school.SCHOOLNAME)

	zip_schools = School.query.filter_by(ZIP='10466').all()
	for zip_school in zip_schools:
  		print(zip_school.SCHOOLNAME)

	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True, port=5000)