from flask import Flask

app = Flask(__name__)


"""     index     """

@app.route("/")
def index():
    with open("sources/server/cacheindex.txt", "r") as file:
        return file.read()

"""     informer     """

@app.route("/informer")
def informer():
    with open("sources/server/cacheinformer.txt", "r") as file:
        return file.read()

"""     populaire     """

@app.route("/populaire")
def populaire():
    with open("sources/server/cachepopulaire.txt", "r") as file:
        return file.read()

def run():
    if __name__=="__main__":
        app.run()

run()