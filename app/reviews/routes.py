from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from app import db
from app.models import Review, User, Post
from app.reviews.forms import ReviewForm


#instatntiating the blueprint
reviews = Blueprint('reviews',__name__)

#POSTS
@reviews.route("/review/new", methods=['GET','POST'])
def new_review():
	form = ReviewForm()
	if form.validate_on_submit():
		reviews = Review(name = form.name.data, content = form.content.data, commentor = current_user)
		db.session.add(reviews)
		db.session.commit()
		flash('you have commented succesfully', 'success')
		return redirect(url_for('posts.user_posts'))
	return render_template('create_review.html', title = 'New Review', form = form, legend = 'New Review')


@reviews.route("/review/<int:review_id>")
def review(post_id):
	review = Review.query.get_or_404(review_id)
	return render_template('review.html', title = review.name, review = review)

#UPDATE REVIEW
@reviews.route("/review/<int:review_id>/update", methods=['GET','POST'])
@login_required
def update_review(review_id):
	review = Review.query.get_or_404(post_id)
	if review.author != current_user:
		abort(403)
	form = ReviewForm()
	if form.validate_on_submit():
		review.name =  form.name.data
		review.content= form.content.data
		db.session.commit()
		flash('Review update successfull', 'success')
		return redirect(url_for('posts.review', review_id = review.id))
	elif request.method == 'GET':
		form.name.data = review.name
		form.content.data = review.content
	return render_template('create_post.html', title = 'Update Review', 
		form = form, legend = 'Update Review')


#DELETE REVIEW
@reviews.route("/review/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_review(post_id):
	review = Review.query.get_or_404(post_id)
	if review.author != current_user:
		abort(403)
	db.session.delete(review)
	db.session.commit()
	flash('Review deleted', 'success')
	return redirect(url_for('main.home'))