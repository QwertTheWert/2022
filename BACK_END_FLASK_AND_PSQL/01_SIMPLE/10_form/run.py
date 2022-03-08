import re
from flask import Flask, redirect, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/hello")
def hello():
	name = request.form.get("name")
	return render_template("hello.html", name=name)

@app.route("/search")
def search():
	query = request.args.get("query")
	return redirect("https://www.google.com/search?q="+query)

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port=8000)
	