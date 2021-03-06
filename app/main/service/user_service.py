import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.cart import Cart

from ..service.cart_service import create_cart
# from app.main.model.closet import Closet


def create_user(data):
    user = User.query.filter_by(email=data['email']).first()
    # if user has no password:
        # send user email to set password
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            registered_on=datetime.datetime.utcnow(),
            email=data['email'],
            password=data['password']
        )
        # create closet
        # new_user.closet = Closet()
        save_changes(new_user)
        new_user._cart = create_cart(new_user.public_id)
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
            'Authorization': auth_token.decode(),
            'public_id': user.public_id
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401

def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()

def get_all_users():
    # returns all user in order of when they registered
    # most recent will be at the top
    # return User.query.order_by(User.registered_on).all()
    return User.query.all()
    
# TEST TO SEE IF COMMENTS ARE DELETED AS WELL
# def delete_user(public_id):
#     user = User.query.filter_by(email=data['email']).first()
#     if user:
#         try:
#         # delete all cart items
#         db.session.delete(user._cart)
#         # delete all closet items
#         db.session.delete(user._closet)
#         # delete all order items
#         db.session.delete(user._orders)
#         db.session.delete(user)
#         db.session.commit()
#         except:
#             db.session.rollback()
#             raise
#         else:
    #         response_object = {
    #             'status': 'success',
    #             'message': 'User deleted.'
    #         }
    #         return response_object, 201
#     else:
#         response_object = {
#             'status': 'fail',
#             'message': 'User not found.',
#         }
#         return response_object, 409

def save_changes(data):
    # commits the changes to database
    db.session.add(data)
    db.session.commit()

__all__ = ['create_user', 'generate_token', 'get_a_user', 'get_all_users']