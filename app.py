"""
Main flask app
Jpatel152@student.gsu.edu

This file usees the Flask framework to create a flask app
that will contain some basic information related to a randomly
selected movie and a poster associated with the movie.
"""
# pylint: disable=no-member
import os
import flask
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from werkzeug.security import generate_password_hash, check_password_hash
import tmdb
from models import db, Account, Movie, Review

app = flask.Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
DB_URL = os.getenv("DATABASE_URL")
if DB_URL.startswith("postgres://"):
    DB_URL = DB_URL.replace("postgres", "postgresql")
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

db.init_app(app)
with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.login_view = "/login"
login_manager.login_message = ""
login_manager.init_app(app=app)


@login_manager.user_loader
def load_user(user_id):  # pylint: disable=missing-function-docstring
    return Account.query.get(int(user_id))


@app.route("/")
@login_required
def main():
    """
    This route is the main page for the entire application. This route
    will load movie/review information related to a random movie.
    """
    movie_info = tmdb.get_random_favorite_movie()
    movie_reviews = []
    movie_average_rating = 0
    movie = Movie.query.filter_by(tmdb_id=movie_info["id"]).first()
    if movie:
        movie_reviews = movie.reviews
        movie_average_rating = movie.get_average_rating()

    return flask.render_template(
        "index.html",
        username=current_user.username,
        movie_id=movie_info["id"],
        movie_title=movie_info["title"],
        movie_tagline=movie_info["tagline"],
        movie_description=movie_info["description"],
        movie_genres=movie_info["genres"],
        movie_poster_url=movie_info["poster_url"],
        movie_wiki_url=movie_info["wiki_url"],
        movie_reviews=movie_reviews,
        movie_average_rating=movie_average_rating,
    )


@app.route("/signup", methods=["GET"])
def signup():
    """
    This route is the signup page for the applicaton. The user may only
    access this page if they are not currently logged in. If the user is
    logged in then they will be taken to the main page of the application.
    """
    if current_user.is_authenticated:
        return flask.redirect("/")
    return flask.render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    """
    This route accepts a post from the signup page to attempt to create a
    new user. If the username already exists then we flash a message to the
    user and refresh the page, otherwise we make create the user and redirect
    them to the login page.
    """
    username = flask.request.form.get("username").lower()
    password = flask.request.form.get("password")

    user = Account.query.filter_by(username=username).first()

    if user:
        flask.flash("User already exists.")
        return flask.redirect("/signup")

    new_user = Account(
        username=username, password=generate_password_hash(password, method="sha256")
    )

    db.session.add(new_user)
    db.session.commit()
    flask.flash("Account created. Please login.")

    return flask.redirect("/login")


@app.route("/login", methods=["GET"])
def login():
    """
    This route is the login page for the application. The user may only
    access this page if they are not logged in. If the user is logged in
    then they will be taken to the main page of the application.
    """
    if current_user.is_authenticated:
        return flask.redirect("/")
    return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    """
    This route accepts a post from the login page to attempt to sign in the
    user based on their username and password. If the user has entered a
    valid username/password combo then they are logged in, otherwise they
    are flashed a message notifying them and the page is refreshed.
    """
    username = flask.request.form.get("username").lower()
    password = flask.request.form.get("password")

    user = Account.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flask.flash("Incorrect username or password.")
        return flask.redirect("/login")

    login_user(user, remember=True)
    return flask.redirect("/")


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    """
    This route logs out the user and redirects them to the login page.
    """
    logout_user()
    return flask.redirect("/login")


@app.route("/review", methods=["POST"])
@login_required
def review_post():
    """
    This route accepts a post from the main page containing information
    related to a user written review. We create a review from the user
    with the specified information and then reload the main page.
    """
    username = current_user.username
    movie_id = flask.request.form.get("movie_id")
    rating = int(float(flask.request.form.get("review_rating")))
    content = flask.request.form.get("review_content").strip()

    movie = Movie.query.filter_by(tmdb_id=movie_id).first()

    if not movie:
        movie = Movie(tmdb_id=movie_id)
        db.session.add(movie)
        db.session.commit()

    user_review = Review(
        rating=rating, content=content, movie_id=movie_id, username=username
    )

    movie.reviews.append(user_review)
    current_user.reviews.append(user_review)

    db.session.add(user_review)
    db.session.commit()

    return flask.redirect("/")


@app.route("/profile", methods=["GET"])
@login_required
def profile():
    """
    This route is the profile page for the currently logged in user. The
    page currently uses React to load the user's written reviews and allow
    them to modify their rating or delete comments.
    """
    return flask.render_template("profile.html")


@app.route("/user_reviews")
@login_required
def get_user_reviews():
    """
    This route returns json data related to the currently logged in user's
    written reviews. The current use of this route is to send json data to
    a React webpage that will use the data to load the user's reviews.
    """
    review_content = []
    for movie_review in current_user.reviews:
        curr_review = {}
        curr_review["review_id"] = movie_review.id
        curr_review["rating"] = movie_review.rating
        curr_review["content"] = movie_review.content
        curr_review["movie_id"] = movie_review.movie_id
        review_content.append(curr_review)

    return flask.jsonify(review_content)


@app.route("/modify_reviews", methods=["POST"])
@login_required
def modify_reviews():
    """
    This route accepts a post containing json related to the user's modified
    review information. It loads all of the user's current reviews and
    finds the reviews to modify using the review_id and modifies the actual
    reviews to reflect any changes made. It keeps track of the reviews that
    still exist in the modified reviews so that it can find the reviews that
    have been deleted and remove them.
    """
    reviews = flask.request.json
    user_reviews = Review.query.filter_by(username=current_user.username).all()
    still_existing_reviews = set()
    for user_review in reviews:
        # The first thing we want to do is find the review
        # that represents this current object
        actual_review = Review.query.filter_by(id=user_review["review_id"]).first()
        still_existing_reviews.add(user_review["review_id"])
        actual_review.rating = user_review["rating"]

    for previous_review in user_reviews:
        review_id = previous_review.id
        if review_id not in still_existing_reviews:
            Review.query.filter_by(id=review_id).delete()

    db.session.commit()
    return flask.Response(status=200)
