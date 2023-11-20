from flask import Flask, render_template, request, redirect
from os import getenv

from entities.book import Book
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


@app.route("/addbook", methods=["POST"])
def addbook_submit():
    author = request.form["author"]
    title = request.form["title"]
    publisher = request.form["publisher"]
    address = request.form["address"]
    year = request.form["year"]
    book = Book(author, title, publisher, address, int(year))
    saver = FileSaver("data.bib")
    saver.save(book)
    return redirect("/")


@app.route("/all_references")
def all_references():
    fetcher = FileFetcher("data.bib")
    data = fetcher.fetch()
    return render_template("all_references.html", data=data)
