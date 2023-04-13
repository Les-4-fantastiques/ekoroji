from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    templateData = {
        "title":"monSuperSite",
        "name":"Ambre"
    }
    return render_template('index.html', **templateData)

if __name__ == "__main__":
    app.run(debug=True)