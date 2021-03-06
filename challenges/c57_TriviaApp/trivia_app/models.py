"""Defines the database for the app"""
from flask import current_app as app
from flask import g as flask_g
from flask.cli import with_appcontext
from sqlalchemy.dialects.postgresql import JSON
from . import db
from datetime import datetime

class User(db.Model):
    # SQLAlchemy adds an implicit constructor to all model classes which accepts
    # keyword arguments for all its columns and relationships
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

class Question(db.Model):
    # SQLAlchemy adds an implicit constructor to all model classes which accepts
    # keyword arguments for all its columns and relationships
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    edited = db.Column(db.DateTime, nullable=True)
    prompt = db.Column(db.Text, nullable=False)
    distractors = db.Column(db.JSON, nullable=False)
