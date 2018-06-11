"""
ccextractor-web | mod_auth/forms.py

Author   : Saurabh Shrivastava
Email    : saurabh.shrivastava54+ccextractorweb[at]gmail.com
Link     : https://github.com/saurabhshri

Based on https://github.com/CCExtractor/sample-platform/blob/master/mod_auth/forms.py
"""

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, ValidationError
from email_validator import validate_email, EmailNotValidError


def valid_password(form, field):
    pass_size = len(field.data)
    if pass_size == 0:
        raise ValidationError('The password can not be empty!')
    if pass_size < 8 or pass_size > 128:
        raise ValidationError(
            'Password needs to be between 8 and 128 characters long (you entered {char})'.format(char=pass_size)
        )

def valid_email(form, field):
    try:
        v = validate_email(field.data)
    except EmailNotValidError as e:
            raise ValidationError('Entered value is not a valid email address. ' + str(e))

class SignupForm(FlaskForm):
    name = StringField('Name', [DataRequired(message='Name is not filled in.')])
    email = EmailField('Email', [DataRequired(message='Email address is not filled in'), valid_email])
    password = PasswordField('Password', [DataRequired(message='Password is not filled in.'), valid_password])
    password_repeat = PasswordField('Repeat password', [DataRequired(message='Repeated password is not filled in.')])
    submit = SubmitField('Register')

    @staticmethod
    def validate_password_repeat(form, field):
        if field.data != form.password.data:
            raise ValidationError('The password needs to match the new password.')

class LoginForm(FlaskForm):
    email = EmailField('Email', [DataRequired(message='Email address is not filled in.'), valid_email])
    password = PasswordField('Password', [DataRequired(message='Password cannot be empty.')])
    submit = SubmitField('Login')



