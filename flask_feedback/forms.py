from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, RadioField, BooleanField, TextAreaField, PasswordField
from wtforms.validators import URL, InputRequired, Length, NumberRange, Email

class AddUserForm(FlaskForm):
    """Form for adding users"""

    username = StringField("Username",
        validators = [InputRequired(), NumberRange(min = 0, max = 20)])

    password = PasswordField("Password",
        validators = [InputRequired()])

    email = StringField("Email",
        validators = [Email(), NumberRange(min = 0, max = 50)])

    first_name = StringField("First Name",
        validators = [InputRequired(), NumberRange(min = 0, max = 50)])

    last_name = StringField("Last Name",
        validators = [InputRequired(), NumberRange(min = 0, max = 50)])


class LoginForm(FlaskForm):
    """Form for logging users in"""

    username = StringField("Username",
        validators = [InputRequired(), NumberRange(min = 0, max = 20)])

    password = PasswordField("Password",
        validators = [InputRequired()])