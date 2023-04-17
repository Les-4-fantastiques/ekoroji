from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL, ValidationError
from app.models import Waste, Article


class WasteForm(FlaskForm):
    waste_name = StringField('Nom du déchet', validators=[
                             DataRequired(), Length(min=2, max=20)])
    waste_validated = SubmitField('Ajouter le déchet')
    def validate_name(self, name):
        waste = Waste.query.filter_by(name=name.data).first()
        if waste:
            raise ValidationError("Ce nom de déchet est déjà utilisé")


class ArticleForm(FlaskForm):
    article_title = StringField('Titre', validators=[
        DataRequired(), Length(min=2, max=50)])
    article_content = StringField('Résumé', validators=[
                                  Length(min=2, max=200)])
    article_image = StringField('Image', validators=[DataRequired(), URL()])
    article_link = StringField('Lien', validators=[DataRequired(), URL()])
    article_validated = SubmitField("Ajouter l'article")

    def validate_link(self, article_link):
        article = Article.query.filter_by(link=article_link.data).first()
        if article:
            raise ValidationError("Ce lien d'article est déjà utilisé.")