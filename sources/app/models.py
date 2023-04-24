from datetime import datetime
from app import db


class Waste(db.Model):
    """Classe pour représenter les déchets dans la base de données

    Attributes:
        id (int): identifiant unique du déchet
        name (str): nom du déchet
        description (str): description du déchet
        list_recycling_possibilitites (str): liste des possibilités de recyclage pour ce déchet
        nb_views (int): nombre de vues de la page associée à ce déchet
        last_viewed (datetime): date de la dernière vue de la page associée à ce déchet
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    list_recycling_possibilitites = db.Column(db.Text, nullable=False)
    nb_views = db.Column(db.Integer, nullable=False, default=0)
    last_viewed = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)

    def __repr__(self):
        """Représentation du déchet sous forme de chaîne de caractères

        Returns:
            str: chaîne de caractères représentant le déchet
        """
        return f"Waste('{self.name}', '{self.description}', '{self.image}', '{self.list_recycling_possibilitites}', '{self.nb_views}', '{self.last_viewed}')"


class Article(db.Model):
    """Classe pour représenter les articles dans la base de données

    Attributes:
        id (int): identifiant unique de l'article
        title (str): titre de l'article
        date (datetime): date de publication de l'article
        image (str): URL de l'image associée à l'article
        link (str): lien vers l'article
        nb_views (int): nombre de vues de la page associée à l'article
        last_viewed (datetime): date de la dernière vue de la page associée à l'article
        content (str): contenu de l'article
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime)  # nullable=False
    image = db.Column(db.String(300), nullable=False)
    link = db.Column(db.String(300), unique=True, nullable=False)
    nb_views = db.Column(db.Integer, nullable=False, default=0)
    last_viewed = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        """Représentation de l'article sous forme de chaîne de caractères

        Returns:
            str: chaîne de caractères représentant l'article
        """
        return f"Article('{self.title}', '{self.date}', '{self.image}', '{self.link}', '{self.nb_views}', '{self.last_viewed}', '{self.content}')"
