from flask import render_template, url_for, flash, redirect
from flaskblog import app, db , bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


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
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = Useer(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created for {form.username.data}. You can now login', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash(f'Login succesfull. Welcome!.', 'success')
		return redirect(url_for('home'))
	return render_template('login.html', title = 'Login', form = form)
