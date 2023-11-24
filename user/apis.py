from flask import Blueprint, request, jsonify
# import jwt, os
from user.models import User
from auth.utils import decode_jwt

user_blueprint = Blueprint("user",__name__)

@user_blueprint.route("/", methods=["GET"])
def get_user():
    payload = decode_jwt(request.headers.get('Authorization'))
    if not payload:
        return {"error": "Token is not valid!"}, 401
    
    user = User.query.get(payload["user_id"])

    # token = request.headers.get('Authorization')
    # payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms="HS256")

    # user_id = payload["user_id"]
    # user = User.query.get(user_id)

    if not user:
        return {"error": "User not found"}, 404
    
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email
    }