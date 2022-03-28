from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pet"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat', "Cat"), ('dog', "Dog"), ('porcupine', "Porcupine")])
    url = StringField("Photo URL", validators=[Optional(), URL(message='Please enter valid URL')])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Comments", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing pet"""

    url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Comments", validators=[Optional()])
    available = BooleanField("Available?")

