from flask import render_template, request, Blueprint
from app.models import Post, Review, User

#initlialize blueprint
main = Blueprint('main',__name__)


@main.route("/")
@main.route("/home")
def home():
	#PAGINATION
	page = request.args.get('page', 1, type = int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page, per_page = 5)
	reviews = Review.query.order_by(Review.date_posted.desc()).paginate(page = page, per_page = 5)
	return render_template('home.html', posts=posts, reviews=reviews)


@main.route("/about")
def about():
	return render_template ('about.html', title='About')

