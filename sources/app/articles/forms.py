from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL, ValidationError
from app.models import Article

class ArticleForm(FlaskForm):
    """
    Formulaire pour ajouter un nouvel article
    """
    article_title = StringField('Titre', validators=[
        DataRequired(), Length(min=2, max=74)])
    article_content = StringField('Résumé', validators=[
                                  Length(min=2, max=200)])
    article_image = StringField('Image (lien)', validators=[
                                DataRequired(), URL()])
    article_link = StringField('Article (lien)', validators=[
                               DataRequired(), URL()])
    article_validated = SubmitField("Ajouter l'article")

    def validate_link(self, article_link):
        """
        Validation pour vérifier si le lien d'article est déjà utilisé
        """
        article = Article.query.filter_by(link=article_link.data).first()
        if article:
            raise ValidationError("Ce lien d'article est déjà utilisé.")