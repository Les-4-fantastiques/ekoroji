from flask import Flask

app = Flask(__name__)


"""     index     """

@app.route("/")
def index():
    with open("sources/server/cacheindex.txt", "r") as file:
        return file.read()

"""     explorer     """

@app.route("/explorer")
def explorer():
    with open("sources/server/cacheexplorer.txt", "r") as file:
        return file.read()

"""     messcans     """

@app.route("/messcans")
def messcans():
    with open("sources/server/cachemesscans.txt", "r") as file:
        return file.read()

def run():
    if __name__=="__main__":
        app.run()

run()