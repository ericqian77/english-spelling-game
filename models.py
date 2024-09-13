from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Theme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    words = db.Column(db.Text, nullable=False)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String(50), nullable=False)
    words = db.Column(db.Text, nullable=False)
    attempts = db.Column(db.Integer, default=0)
    hint_points = db.Column(db.Integer, default=9)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
