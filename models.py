"""
This module contains the models used in the database for
the application

Method for preventing circular imports comes from Ikenna Okonkwo 
on project-milestone-2 channel of class discord.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    reviews = db.relationship("Review", backref="user", lazy=True)


# TODO: Follow advice from https://stackoverflow.com/a/16434931
# and see if using that information works for this method. We
# would like to be able to attach a review to both a person and
# a movie so that later on we could make a user profile page where
# they can see all of their reviews.
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tmdb_id = db.Column(db.Integer)
    reviews = db.relationship("Review", backref="movie", lazy=True)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    content = db.Column(db.String(512), nullable=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    username = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
