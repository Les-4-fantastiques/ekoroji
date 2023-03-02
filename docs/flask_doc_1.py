#réaliser l'incorporation de bibliothèques
from flask import Flask, flash, redirect, render_template, request, session, abort

app= Flask(__name__)

@app.route("/")
def home():
    return "Coucou tout le monde"

@app.route("/scan")
def scan():
    templateData= {
        "title":"ekoroji",
        "name" : "Ambre"
    }
    return render_template('index.html',**templateData)

@app.route("/informer")
def informer():
    return " Voici les nouveaux articles"

if __name__ == "__main__":
    app.run(host = "127.0.0.1")