from flask import Flask

app = Flask(__name__)


"""     index     """

@app.route("/")
def index():
    with open("templates/index.txt", "r") as file:
        return file.read().encode("utf-8")

"""     explorer     """

@app.route("/explorer")
def explorer():
    with open("templates/explorer.txt", "r") as file:
        return file.read().encode("utf-8")

"""     messcans     """

@app.route("/messcans")
def messcans():
    with open("templates/messcans.txt", "r") as file:
        return file.read().encode("utf-8")

if __name__=="__main__":
    app.run()