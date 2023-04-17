from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ekoroji.db'
db = SQLAlchemy(app)

from app import models

with app.app_context():
    db.drop_all()
    db.create_all()

from app import routes