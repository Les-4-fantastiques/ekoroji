from flask import Flask

app = Flask(__name__)


"""     index     """

@app.route("/")
def index():
    with open("website/cacheindex.txt", "r") as file:
        return file.read()

"""     explorer     """

@app.route("/explorer")
def explorer():
    with open("website/cacheexplorer.txt", "r") as file:
        return file.read()

"""     messcans     """

@app.route("/messcans")
def messcans():
    with open("website/cachemesscans.txt", "r") as file:
        return file.read()

if __name__=="__main__":
    app.run()