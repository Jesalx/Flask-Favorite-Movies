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
