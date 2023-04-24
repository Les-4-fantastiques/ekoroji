from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import Waste

class WasteForm(FlaskForm):
    waste_name = StringField('Nom du déchet', validators=[
                             DataRequired(), Length(min=2, max=20)])
    waste_validated = SubmitField('Ajouter le déchet')

    def validate_name(self, name):
        waste = Waste.query.filter_by(name=name.data).first()
        if waste:
            raise ValidationError("Ce nom de déchet est déjà utilisé")