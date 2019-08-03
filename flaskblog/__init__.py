from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'de74e7b0fad76d362bfd1fcd0c0fd885'
#init db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db instance

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from flaskblog import routes