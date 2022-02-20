"""
Milestone 2 - Main flask app
Jpatel152@student.gsu.edu

This file usees the Flask framework to create a flask app
that will contain some basic information related to a randomly
selected movie and a poster associated with the movie.
"""
import os  # pylint: disable=unused-import
import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from werkzeug.security import generate_password_hash, check_password_hash
import tmdb
from models import db, User, Movie, Review

app = flask.Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
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
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
@login_required
def main():  # pylint: disable=missing-function-docstring
    movie = tmdb.get_random_favorite_movie()
    return flask.render_template(
        "index.html",
        username=current_user.username,
        movie_id=movie["id"],
        movie_title=movie["title"],
        movie_tagline=movie["tagline"],
        movie_description=movie["description"],
        movie_genres=movie["genres"],
        movie_poster_url=movie["poster_url"],
        movie_wiki_url=movie["wiki_url"],
    )


@app.route("/signup", methods=["GET"])
def signup():
    return flask.render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    username = flask.request.form.get("username").lower()
    password = flask.request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if user:
        flask.flash("User already exists.")
        return flask.redirect("/signup")

    new_user = User(
        username=username, password=generate_password_hash(password, method="sha256")
    )

    db.session.add(new_user)
    db.session.commit()
    flask.flash("Account created. Please login.")

    return flask.redirect("/login")


@app.route("/login", methods=["GET"])
def login():
    return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    username = flask.request.form.get("username").lower()
    password = flask.request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flask.flash("Incorrect username or password.")
        return flask.redirect("/login")

    login_user(user, remember=True)
    return flask.redirect("/")


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return flask.redirect("/login")


@app.route("/review", methods=["POST"])
@login_required
def review():
    username = flask.request.form.get("username")
    movie_id = flask.request.form.get("movie_id")
    rating = flask.request.form.get("review_rating")
    content = flask.request.form.get("review_content")

    movie = Movie.query.filter_by(tmdb_id=movie_id).first()
    user = User.query.filter_by(username=username).first()

    if not movie:
        movie = Movie(tmdb_id=movie_id)
        db.session.add(movie)
        db.session.commit()

    review = Review(
        rating=rating, content=content, movie_id=movie_id, username=username
    )

    movie.reviews.append(review)
    user.reviews.append(review)

    db.session.add(review)
    db.session.commit()

    return flask.redirect("/")


# The following runs for me locally, but if there are issues you can
# also try: "app.run(debug=True)" without the host and port parameters
app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 8080)),  # pylint: disable=invalid-envvar-default
    debug=True,
)
