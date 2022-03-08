import re
from flask import Flask, redirect, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/more", methods=["GET","POST"])
def hello():
	if request.method == "GET":
		# return "Please submit the form instead!"
		return redirect(url_for("index", err_msg = "Please submit first."))
	name = request.form.get("name")
	return render_template("hello.html", name=name)


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port=8000)