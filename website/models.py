from . import db 
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), unique = True)
    correct_guesses = db.Column(db.Integer)
    attempts_taken = db.Column(db.Integer)
    