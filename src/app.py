from flask import Flask, render_template, request, redirect, flash
from os import getenv

from entities.book import Book
from entities.entry import Entry
from entities.key_generator import KeyGenerator
from entities.manual import Manual
from repositories.in_memory_repository import InMemoryRepository
from repositories.reference_repository import ReferenceRepository
from services.validator import Validator
from services.db_connection import get_database_connection

app = Flask("ohtu_miniprojekti")
app.secret_key = getenv("SECRET_KEY")

entryRepository = InMemoryRepository()


connection = get_database_connection()
reference_repository = ReferenceRepository(connection)

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
    validator = Validator()

    keygen = KeyGenerator()

    errors = validator.validate_book(request.form)
    if len(errors) > 0:
        for i in errors:
            flash(i)
        return redirect("/addbook")

    entry = Entry(request.form, Book(), keygen)

    entryRepository.save_entry(entry)
    return redirect("/")


@app.route("/addmanual", methods=["POST"])
def addmanual_submit():
    keygen = KeyGenerator()
    validator = Validator()

    errors = validator.validate_manual(request.form)
    if len(errors) > 0:
        for i in errors:
            flash(i)
        return redirect("/addmanual")

    entry = Entry(request.form, Manual(), keygen)
    entryRepository.save_entry(entry)
    return redirect("/")


@app.route("/all_references")
def all_references():
    data = entryRepository.as_human_readable()
    data = data.split("\n")
    return render_template("all_references.html", data=data)


@app.route("/download_formatted")
def download_formatted():
    return entryRepository.fetch()
