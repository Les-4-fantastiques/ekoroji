from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    search_content = StringField('Nom de la recherche', validators=[
                             DataRequired(), Length(min=2, max=50)])
    search_validated = SubmitField('')