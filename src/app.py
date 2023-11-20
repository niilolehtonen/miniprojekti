from flask import Flask

app=Flask("ohtu_miniprojekti")


@app.route("/")
def index():
    return "yeet"
