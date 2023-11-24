from flask import Blueprint, request
import jwt, os
from user.models import User

user_blueprint = Blueprint("user",__name__)

@user_blueprint.route("/", methods=["GET"])
def get_user():
    token = request.headers.get('Authorization')
    payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithm="HS256")

    user_id = payload["user_id"]
    user = User.query.get(user_id)

    if not user:
        return {"message": "User not found"}, 404
    
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email
    }