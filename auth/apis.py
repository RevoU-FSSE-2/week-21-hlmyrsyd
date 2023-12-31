import jwt, os
from flask import Blueprint, request, jsonify
from user.models import User
from db import db
from common.bcrypt import bcrypt
from datetime import datetime, timedelta
from marshmallow import Schema, fields, ValidationError

auth_blueprint = Blueprint('auth', __name__)

class UserRegisterSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.String(required=True)
    bio = fields.String(required=True)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    schema = UserRegisterSchema()
    try:
        data = schema.load(data)
    except ValidationError as err:
        return {"error": err.messages}, 400

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password, email=data['email'], bio=data['bio'])

    existing_user_username = User.query.filter_by(username=data['username']).first()
    existing_user_email = User.query.filter_by(email=data['email']).first()

    if existing_user_username:
        return jsonify({'error': 'Username already registered.'}), 400

    if existing_user_email:
        return jsonify({'error': 'Email already registered.'}), 400

    db.session.add(new_user)
    db.session.commit()

    return {
        'id': new_user.id,
        'username': data['username'],
        'bio': data['bio']
    }

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data["username"]
    password = data["password"]

    user = User.query.filter_by(username=username).first()

    if not user:
        return {"error": "Username or Password isn't Correct"}, 400
    
    valid_password = bcrypt.check_password_hash(user.password, password)
    if not valid_password:
        return {"error": "Username or Password isn't Correct"}, 400

    payload = {
        'user_id': user.id,
        'username': user.username,
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(minutes=1)
    }
    token = jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm="HS256")

    return {
        'message': f'Welcome back, {username}!',
        'id': user.id,
        'username': user.username,
        'token': token
    }