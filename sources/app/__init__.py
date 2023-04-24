from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.configs import Config

db = SQLAlchemy()  # Initialisation de la base de données SQLAlchemy

"""
with app.app_context():
    db.drop_all()
    db.create_all()
"""

def create_app(config_class=Config):
    """
    Fonction qui crée l'application Flask avec les configurations passées en paramètre et initialise la base de données.
    Elle enregistre également les différentes blueprints correspondant aux différentes routes de l'application.
    """
    app = Flask(__name__)  # Création de l'application Flask
    app.config.from_object(config_class)  # Chargement des configurations passées en paramètre

    db.init_app(app)  # Initialisation de la base de données avec l'application Flask créée

    # Import des différentes blueprints correspondant aux différentes routes de l'application
    from app.main.routes import main_bp
    from app.articles.routes import articles_bp
    from app.wastes.routes import wastes_bp
    from app.errors.handlers import errors_bp

    # Enregistrement des blueprints
    app.register_blueprint(wastes_bp)
    app.register_blueprint(articles_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(errors_bp)

    return app  # Retourne l'application Flask créée