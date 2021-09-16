from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp, ValidationError
from app.models import User

# https://stackoverflow.com/questions/54582898/flaskform-validation-code-checking-if-a-user-already-exists-or-not
# https://wtforms.readthedocs.io/en/2.3.x/validators/


class Register(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(min=4, max=20),
        Regexp(
            r'^[\w.@+-]+$', message="Username can only contain lettes, numbers and symbols!")
    ])

    name = StringField('Name', validators=[
        DataRequired(),
    ])

    password = StringField('Password', validators=[
        DataRequired()
    ])

    confirmPassword = StringField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password')
    ])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                f'Username already exists! Please choose another.')


class Login(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(min=3, max=10)
    ])

    password = StringField('Password', validators=[
        DataRequired()
    ])

    submit = SubmitField('Login')
