from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.configs import Config

db = SQLAlchemy()

"""
with app.app_context():
    # db.drop_all()
    db.create_all()
"""

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.main.routes import main_bp
    from app.articles.routes import articles_bp
    from app.wastes.routes import wastes_bp
    from app.errors.handlers import errors_bp
    app.register_blueprint(wastes_bp)
    app.register_blueprint(articles_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(errors_bp)

    return app