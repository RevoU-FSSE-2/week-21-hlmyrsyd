from flask import Blueprint, request
from db import db
from tweet.models import Tweet

tweet_blueprint = Blueprint("tweet", __name__)

@tweet_blueprint.route("/", methods=["POST"])
def create_tweet():
    data = request.get_json()

    tweet_text = data.get("Tweet")
    if not tweet_text:
        return {"error_message": "Tweet tidak boleh kosong"}, 400

    if len(tweet_text) > 150:
        return {"error_message": "Tweet tidak boleh lebih dari 150 karakter"}, 400

    new_tweet = Tweet(tweet=tweet_text)
    
    db.session.add(new_tweet)
    db.session.commit()

    return {
        'id': new_tweet.id,
        'published_at': new_tweet.published_at,
        'tweet': new_tweet.tweet
    }, 200