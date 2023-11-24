from flask import Blueprint, request
from db import db
from auth.utils import decode_jwt
from follow.utils import user_is_following, follow_user, unfollow_user

following_blueprint = Blueprint('following', __name__)

@following_blueprint.route('/', methods=['POST'])
def follow_user_api():
    current_user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
    data = request.get_json()
    user_id_to_follow = data.get('user_id_to_follow')

    if current_user_id == user_id_to_follow:
        return {'error_message': 'Tidak bisa follow diri sendiri'}, 400

    if user_is_following(current_user_id, user_id_to_follow):
        unfollow_user(current_user_id, user_id_to_follow)
        following_status = 'unfollow'
    else:
        follow_user(current_user_id, user_id_to_follow)
        following_status = 'follow'

    return {'following_status': following_status}, 200