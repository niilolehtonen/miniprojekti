from flask import Flask, render_template, request, redirect
from os import getenv

from entities.book import Book
from entities.manual import Manual
from repositories.reference_repository import ReferenceRepository
from services.validator import Validator

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
    information_dict = dict()

    information_dict["author"] = request.form["author"] or None
    information_dict["title"] = request.form["title"] or None
    information_dict["publisher"] = request.form["publisher"] or None
    information_dict["year"] = request.form["year"] or None
    information_dict["volume"] = request.form["volume"] or None
    information_dict["series"] = request.form["series"] or None
    information_dict["address"] = request.form["address"] or None
    information_dict["edition"] = request.form["edition"] or None
    information_dict["month"] = request.form["month"] or None
    information_dict["note"] = request.form["note"] or None

    validator = Validator()
    validator.validate_book(information_dict)
    book = Book(information_dict["author"], information_dict["title"], information_dict["publisher"],
                int(information_dict["year"]), int(information_dict["volume"]), information_dict["series"],
                information_dict["address"], int(information_dict["edition"]), int(information_dict["month"]),
                information_dict["note"])
    saver = ReferenceRepository("data.bib")
    saver.save_book(book)
    return redirect("/")


@app.route("/addmanual", methods=["POST"])
def addmanual_submit():
    information_dict = dict()

    information_dict["author"] = request.form["author"] or None
    information_dict["title"] = request.form["title"] or None
    information_dict["year"] = request.form["year"] or None
    information_dict["organization"] = request.form["organization"] or None
    information_dict["address"] = request.form["address"] or None
    information_dict["edition"] = request.form["edition"] or None
    information_dict["month"] = request.form["month"] or None
    information_dict["note"] = request.form["note"] or None

    validator = Validator()
    validator.validate_manual(information_dict)
    manual = Manual(information_dict["title"], int(information_dict["year"]), information_dict["author"], information_dict["organization"], information_dict["address"], information_dict["edition"], information_dict["month"], information_dict["note"])
    saver = ReferenceRepository("data.bib")
    saver.save_manual(manual)
    return redirect("/")


@app.route("/all_references")
def all_references():
    fetcher = ReferenceRepository("data.bib")
    data = fetcher.fetch()
    data = data.split("\n")
    return render_template("all_references.html", data=data)
