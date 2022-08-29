from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, RadioField, BooleanField, TextAreaField
from wtforms.validators import URL, InputRequired, Length, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name",
        validators = [InputRequired()]
    )

    species = RadioField("species",
        choices = [('dog', 'Dog'),('cat', 'Cat'), ('porcuine', 'Porcupine')]
    )

    photo_url = StringField("Photo Url",
        validators = [URL()]    
    )

    age = FloatField("Age",
        validators = [NumberRange(min = 0, max = 30)]
    )

    notes = TextAreaField("Notes")

    available = BooleanField("is Available")