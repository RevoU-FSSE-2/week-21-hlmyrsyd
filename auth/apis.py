from flask import Blueprint, request, jsonify
from user.models import User
from db import db
from common.bcrypt import bcrypt

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data["username"]
    password = data["password"]
    email = data["email"]
    bio = data["bio"]

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password, email=email, bio=bio)

    existing_user_username = User.query.filter_by(username=username).first()
    existing_user_email = User.query.filter_by(email=email).first()

    if existing_user_username:
        return jsonify({'error': 'Username already registered.'}), 400

    if existing_user_email:
        return jsonify({'error': 'Email already registered.'}), 400

    db.session.add(new_user)
    db.session.commit()

    return {
        'id': new_user.id,
        'username': username,
        'bio': bio
    }

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': f'Welcome back, {username}!'})
    else:
        return jsonify({'error': 'It seems like you username or password is incorrect'}), 401
