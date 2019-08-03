from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask (__name__)



app.config['SECRET_KEY'] = 'de74e7b0fad76d362bfd1fcd0c0fd885'
#init db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db instance
db = SQLAlchemy(app)

#USER OBJECT
class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique=True, nullable = False)
	username = db.Column(db.String(200), unique=True, nullable = False)
	image_file = db.Column(db.String(20),  nullable = False, default = 'default.jpg')
	username = db.Column(db.String(60), nullable = False)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"

#USER POSTER
class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(150), nullable = False)
	date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	content = db.Column(db.String(200), nullable = False )

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"



posts = [
{

'author':'joe munyi',
'title':'Blog Post 1',
'content':'bad ass coder',
'date_posted' : 'april 12 40'
},
{

'author':'sheri munyi',
'title':'Blog Post  2',
'content':'asf coder hot',
'date_posted' : 'april 12 2018'
}


]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)


@app.route("/about")
def about():
	return render_template ('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}.', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash(f'Login succesfull. Welcome!.', 'success')
		return redirect(url_for('home'))
	return render_template('login.html', title = 'Login', form = form)


if __name__ == '__main__':
	app.run(debug=True)
	