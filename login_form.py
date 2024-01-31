# https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/
# https://wtforms.readthedocs.io/en/3.0.x/
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length


class LoginForm(FlaskForm):
    email = StringField(
        label="Email",
        validators=[Email(message="Invalid email address."), DataRequired()]
    )
    password = PasswordField(
        label="Password",
        validators=[Length(min=8, message="Must be at least 8 characters"), DataRequired()]
    )
    submit = SubmitField(label="Log In")
