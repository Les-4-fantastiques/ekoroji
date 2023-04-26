from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    """
    Classe représentant le formulaire de recherche.

    Attributes
    ----------
    search_content : StringField
        Champ de saisie de la recherche.
    search_validated : SubmitField
        Bouton de validation de la recherche.

    Methods
    -------
    None
    """
    search_content = StringField('Nom de la recherche', validators=[
                             DataRequired(), Length(min=2, max=50)])
    search_validated = SubmitField('')