from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL


class WasteForm(FlaskForm):
    waste_name = StringField('Nom du déchet', validators=[
                             DataRequired(), Length(min=2, max=20)])
    waste_validated = SubmitField('Ajouter le déchet')


class ArticleForm(FlaskForm):
    article_title = StringField('Titre', validators=[
        DataRequired(), Length(min=2, max=50)])
    article_content = StringField('Résumé', validators=[
                                  Length(min=2, max=200)])
    article_image = StringField('Image', validators=[DataRequired(), URL()])
    article_link = StringField('Lien', validators=[DataRequired(), URL()])
    article_validated = SubmitField("Ajouter l'article")