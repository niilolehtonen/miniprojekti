from flask import Flask, render_template
from os import getenv

app = Flask("ohtu_miniprojekti")
app.secret_key = getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addbook")
def addbook():
    return render_template("addbook.html")


