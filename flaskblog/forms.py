from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, DataRequired,Email,EqualTo, ValidationError, Length
from wtforms import StringField, SubmitField, BooleanField, PasswordField, TextAreaField
from flaskblog.models import User
from flask_login import current_user

