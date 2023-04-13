from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dechet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    description_courte = db.Column(db.String(255), nullable=False)
    recyclage = db.Column(db.String(255), nullable=False)
    photo = db.Column(db.String(255), nullable=True)
    nb_vues = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f"Dechet(nom='{self.nom}', description_courte='{self.description_courte}', recyclage='{self.recyclage}', photo='{self.photo}', nb_vue='{self.nb_vue}')"

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

def create_db():
    db.create_all()
    # Ajout de quelques déchets de démonstration
    dechet1 = Dechet(nom="Bouteille en plastique", description_courte="Bouteille en plastique vide", recyclage="Recyclable dans les poubelles de tri sélectif", photo="https://via.placeholder.com/150", nb_vues=0)
    dechet2 = Dechet(nom="Pile usagée", description_courte="Pile usagée de type AA", recyclage="A rapporter en magasin ou en déchèterie", photo="https://via.placeholder.com/150", nb_vues=0)
    db.session.add(dechet1)
    db.session.add(dechet2)
    db.session.commit()
