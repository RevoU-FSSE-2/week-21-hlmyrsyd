from db import db
from follow.models import Followers

def user_is_following(follower_id, following_id):
    result = db.session.query(Followers).filter_by(follower_id=follower_id, following_id=following_id).first()
    return result is not None

def follow_user(follower_id, following_id):
    new_follow = Followers(follower_id=follower_id, following_id=following_id)
    db.session.add(new_follow)
    db.session.commit()

def unfollow_user(follower_id, following_id):
    follow_to_delete = db.session.query(Followers).filter_by(follower_id=follower_id, following_id=following_id).first()
    db.session.delete(follow_to_delete)
    db.session.commit()
