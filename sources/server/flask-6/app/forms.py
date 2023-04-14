from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length


class TaskForm(FlaskForm):
    name = StringField('Nom', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=200)])
    image = FileField('Image')
