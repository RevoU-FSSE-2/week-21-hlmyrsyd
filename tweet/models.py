from db import db
from datetime import datetime

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    published_at = db.Column(db.DateTime, default=datetime.utcnow)
    tweet = db.Column(db.String(150), nullable=False)