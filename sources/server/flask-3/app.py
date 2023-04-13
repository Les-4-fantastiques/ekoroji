from flask import Flask, render_template
from models import db, Dechet, init_db, create_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dechets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

@app.route('/')
def index():
    #return render_template('index.html')
    return 'Bonjour, voici la page d\'accueil de mon site web de gestion de déchets !'

if __name__ == '__main__':
    create_db()
    app.run(debug=True)