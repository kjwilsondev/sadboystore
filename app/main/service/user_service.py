import uuid
import datetime

from app.main import db
from app.main.model.user import User

def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            fname=data['fname'],
            lname=data['lname'],
            email=data['email'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        # create cart
        # create closet
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401

def get_all_users():
    return User.query.all()

def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()

def delete_user(public_id):
    user = User.query.filter_by(email=data['email']).first()
    if user:
        db.session.delete(self)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'User deleted.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User not found.',
        }
        return response_object, 409


def save_changes(data):
    # commits the changes to database
    db.session.add(data)
    db.session.commit()