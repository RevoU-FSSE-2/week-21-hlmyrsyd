from db import db

class Followers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, nullable=False)
    following_id = db.Column(db.Integer, nullable=False)