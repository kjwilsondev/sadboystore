import uuid
import datetime

from app.main import db
from app.main.model.cart import Cart

# TODO:
# add items to 
# delete items from cart
# add user to cart
# Get budgets by amount of money
# Get budgets by success

def create_cart(items):
    # number of items
    new_cart = Cart(
        set_on = datetime.datetime.utcnow()
    )
    if items:
        for item in items:
            

    save_changes(new_budget)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 201

# def get_all_budgets():
#     return Budget.query.all()


# def get_all_user_budgets(public_id):
#     return Budget.query.filter_by(public_id=public_id).all()

# def delete_user(public_id):
#     user = User.query.filter_by(email=data['email']).first()
#     if user:
#         db.session.delete(self)
#         db.session.commit()
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
    db.session.add(data)
    db.session.commit()