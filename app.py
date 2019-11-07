from flask import Flask

app = Flask(__name__,
			template_folder="templates",
            static_folder="static")

@app.route("/ping")
def sanity_check():
	return "pong"

if __name__ == '__main__':
	app.run(debug=True)