from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
	return redirect(url_for("details"))

@app.route("/details")
def details():
	return render_template("details.html")

@app.route("/weapon")
def weapon():
	return render_template("weapon.html")

@app.route("/equipment")
def equipment():
	return render_template("equipment.html")

@app.route("/progression")
def progression():
	return render_template("progression.html")

@app.route("/spells")
def spells():
	return render_template("spells.html")


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug=True)
	# app.run(debug=True)