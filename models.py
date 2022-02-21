"""
This module contains the models used in the database for
the application

Method for preventing circular imports comes from Ikenna Okonkwo 
on project-milestone-2 channel of class discord.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Account(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    reviews = db.relationship("Review", backref="account", lazy=True)


# How to use a relationship once it's in the model from:
# https://stackoverflow.com/a/16434931
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tmdb_id = db.Column(db.Integer)
    reviews = db.relationship("Review", backref="movie", lazy=True)

    def get_average_rating(self):
        if self.reviews:
            review_sum = 0
            for review in self.reviews:
                review_sum += review.rating
            average = review_sum / len(self.reviews)
            return round(average, 2)
        else:
            return 0


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    content = db.Column(db.String(512), nullable=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    username = db.Column(db.String(128))
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))
