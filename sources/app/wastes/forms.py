from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import Waste

class WasteForm(FlaskForm):
    """
    Une classe de formulaire Flask utilisée pour valider les données entrées pour un déchet.
    """
    waste_name = StringField('Nom du déchet', validators=[
                             DataRequired(), Length(min=2, max=49)])
    waste_validated = SubmitField('Ajouter le déchet')

    def validate_name(self, name):
        """
        Vérifie si le nom du déchet entré est déjà utilisé dans la base de données.
        
        Args:
            - name: Nom du déchet entré par l'utilisateur.
        
        Raises:
            - ValidationError: si le nom de déchet est déjà utilisé.
        """
        waste = Waste.query.filter_by(name=name.data).first()
        if waste:
            raise ValidationError("Ce nom de déchet est déjà utilisé")