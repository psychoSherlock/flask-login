from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, SubmitField, FileField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp, ValidationError
from app.models import User

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

    password = PasswordField('Password', validators=[
        DataRequired()
    ])

    confirmPassword = PasswordField('Confirm Password', validators=[
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
        DataRequired(), Length(min=4, max=20)
    ])

    password = PasswordField('Password', validators=[
        DataRequired()
    ])

    submit = SubmitField('Login')


class UpdateAccount(FlaskForm):
    username = StringField('Username', validators=[
        Length(min=4, max=20),
        Regexp(
            r'^[\w.@+-]+$', message="Username can only contain lettes, numbers and symbols!")
    ])

    name = StringField('Name', validators=[
    ])

    password = PasswordField('Password')

    confirmPassword = PasswordField('Confirm Password', validators=[
        EqualTo('password')
    ])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    f'Username already exists! Please choose another.')
