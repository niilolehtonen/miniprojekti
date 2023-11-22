from flask import Flask, render_template, request, redirect
from os import getenv

from entities.book import Book
from entities.manual import Manual
from services.file_fetcher import FileFetcher
from services.file_saver import FileSaver

app = Flask("ohtu_miniprojekti")
app.secret_key = getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/addbook", methods=["GET"])
def addbook():
    return render_template("addbook.html")

@app.route("/addmanual", methods=["GET"])
def addmanual():
    return render_template("addmanual.html")


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
    saver = FileSaver("data.bib")
    saver.save(book)
    return redirect("/")

@app.route("/addmanual", methods=["POST"])
def addmanual_submit():
    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    organization = request.form["organization"]
    address = request.form["address"]
    edition = request.form["edition"]
    month = request.form["month"]
    note = request.form["note"]
    manual = Manual(title, int(year), author, organization, address, int(edition), int(month), note)
    saver = FileSaver("data.bib")
    saver.save(manual)
    return redirect("/")

@app.route("/all_references")
def all_references():
    fetcher = FileFetcher("data.bib")
    data = fetcher.fetch()
    data = data.split("\n")
    return render_template("all_references.html", data=data)
