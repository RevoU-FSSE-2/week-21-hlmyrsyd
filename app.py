import os
from flask import Flask
from auth.apis import auth_blueprint
from user.apis import user_blueprint
from tweet.apis import tweet_blueprint
from follow.apis import following_blueprint
from db import db, db_init
from common.bcrypt import bcrypt

app = Flask(__name__)

database_url = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url

db.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(tweet_blueprint, url_prefix="/tweet")
app.register_blueprint(following_blueprint, url_prefix="/follow")

with app.app_context():
    db_init()