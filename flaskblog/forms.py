from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, DataRequired,Email,EqualTo, ValidationError, Length
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from flaskblog.models import User


class RegistrationForm (FlaskForm):
	username = StringField('Enter Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password',message='passwords must match')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username = username.data).first()
		if user:
			raise ValidationError('That username is takes, please use another')

	def validate_email(self, email):
		user = User.query.filter_by(email = email.data).first()
		if user:
			raise ValidationError('That email is taken, please use another')
			
class LoginForm (FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember  = BooleanField('Remember me', default=False)
	submit = SubmitField('Login')