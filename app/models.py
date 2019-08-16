from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from . import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

#USER OBJECT
class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique=True, nullable = False)
	email = db.Column(db.String(200), unique=True, nullable = False)
	image_file = db.Column(db.String(20),  nullable = False, default = 'default.jpg')
	password = db.Column(db.String(60), nullable = False)
	# bio = db.Column(db.String(1000))
	post = db.relationship('Post', backref = 'user', lazy = True)
	reviews = db.relationship('Review', backref = 'user', lazy = True)

#email config .. passing a token that expires in 1800 seconds; to reset password
	def get_reset_token(self, expires_sec=1800):
		s=Serializer(current_app.config['SECRET_KEY'], expires_sec)
		return s.dumps({'user_id':self.id}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):#TAKES TOKEN AS ARGUMENT
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			user_id = s.loads(token)['user_id']
		except:
			return None #RETURNS NONE IF WE GET AN EXCEPTION
		return User.query.get(user_id) #IF WE DONT, RETURNS USERS IS

		'''
		STATIC METHOD, RETURN IS NOT USED, WE TELL PYTHON NOT TO EXPECT THAT SELF PARAMETER AS AN ARGUMENT
		BUT THIS RETURNED USER IS NOT USED IN ANY WAY, H
		ENCE WE GO UP THERE AND OVERRULE IT WITH STATIC DECORATOR AND METHOD

		'''

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"

#USER POSTER
class Post(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(150), nullable = False)
	date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	content = db.Column(db.String(1000), nullable = False )
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	reviews = db.relationship('Review', backref = 'post', lazy = 'dynamic')

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"

#COMMENTS OBJECT
class Review(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(150), nullable = False)
	date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	content = db.Column(db.String(1000), nullable = False )
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

	def save_review(self):
		db.session.add(self)
		db.session.commit()

	def my_function():
		with app.app_context():
			user = db.User(...)
			db.session.add(user)
			db.session.commit()

	def __repr__(self):
		return f"Review('{self.name}', '{self.date_posted}')"
