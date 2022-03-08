from cgitb import text
import numbers
from flask import Flask, render_template
from datetime import datetime 

app = Flask(__name__)

@app.route("/")
def index():
	x = datetime.now()

	isChristmas = (x.month == 2 and x.day == 25)
	return render_template("index.html", isChristmas = isChristmas)

if __name__ == "__main__":
	app.run(debug=True)