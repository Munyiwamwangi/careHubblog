from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from app.models import User


class RegistrationForm (FlaskForm):
	username = StringField('Enter Username', 
		validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', 
		validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	confirm_password = PasswordField('Confirm Password', 
		validators = [DataRequired(), EqualTo('password',message='passwords must match')])
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

#update account
class UpdateAccountForm (FlaskForm):
	username = StringField('Enter Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	bio = StringField('In a nutshell, tell us more abour you', validators=[DataRequired(), Length(min=10, max=100)])
	picture = FileField('Update Profile Picture', validators =[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username = username.data).first()
			if user:
				raise ValidationError('That username is takes, please use another')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email = email.data).first()
			if user:
				raise ValidationError('That email is taken, please use another')



#FORMS FOR RESET PASSWORDS
class RequestResetForm(FlaskForm):
	email = StringField('Email', 
		validators = [DataRequired(), Email()])
	submit = SubmitField('Request Password Reset')

	def validate_email(self, email):
		user = User.query.filter_by(email = email.data).first()
		if user is None:
			raise ValidationError('There is no account with that email, please register first...')

class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password',
		validators = [DataRequired()])
	confirm_password = PasswordField('Confirm Password', 
		validators = [DataRequired(), EqualTo('password',message='passwords must match')])
	submit = SubmitField('Reset Password')