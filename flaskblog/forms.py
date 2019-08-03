from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, DataRequired,Email,EqualTo, Length
from wtforms import StringField, SubmitField, BooleanField, PasswordField

class RegistrationForm (FlaskForm):
	username = StringField('Enter Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password',message='passwords must match')])
	submit = SubmitField('Sign Up')

class LoginForm (FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember  = BooleanField('Remember me', default=False)
	submit = SubmitField('Login')