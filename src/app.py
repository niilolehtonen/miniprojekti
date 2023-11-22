from flask import Flask, render_template, request, redirect
from os import getenv

from entities.book import Book
from repositories.reference_repository import ReferenceRepository

app = Flask("ohtu_miniprojekti")
app.secret_key = getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/addbook", methods=["GET"])
def addbook():
    return render_template("addbook.html")


@app.route("/addbook", methods=["POST"])
def addbook_submit():
    author = request.form["author"]
    title = request.form["title"]
    publisher = request.form["publisher"]
    year = request.form["year"]
    volume = request.form["volume"]
    series = request.form["series"]
    address = request.form["address"]
    edition = request.form["edition"]
    month = request.form["month"]
    note = request.form["note"]
    book = Book(author, title, publisher, int(year), int(volume), series, address, int(edition), int(month), note)
    saver = ReferenceRepository("data.bib")
    saver.save_book(book)
    return redirect("/")


@app.route("/all_references")
def all_references():
    fetcher = ReferenceRepository("data.bib")
    data = fetcher.fetch()
    data = data.split("\n")
    return render_template("all_references.html", data=data)
