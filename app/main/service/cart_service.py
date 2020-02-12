import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.cart import Cart

# TODO:
# Calculate cost of cart
# response object for 
# {
#     cart user,
#     cart cost,
#     cart length,
# }

def create_cart(public_id):
    new_cart = Cart(
        user_id = public_id
    )
    db.session.add(new_cart)
    db.session.commit()
    return new_cart

def get_cart_items(public_id):
    cart = Cart.query.filter_by(user_id=public_id).first()
    # return user._cart._items
    return cart._items

def get_all_carts():
    # returns carts in order of cost
    # return Cart.query.order_by(User.registered_on).all()
    return Cart.query.all()

def add_to_cart(public_id, item_data):
    cart = Cart.query.filter_by(public_id=public_id).first()
    item = Item.query.filter_by(public_id=item_data['item_id']).first()

    if cart and item:
        cart._items.append(item)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Added item to cart',
        }
        return response_object, 201

    return 404


# def empty_cart(public_id):
#     user = User.query.filter_by(public_id=public_id).first()
#     cart = user._cart
#     if user:
#         db.session.delete(cart)
#         user._cart = create_cart(public_id)
#         db.session.commit()
#         response_object = {
#             'status': 'success',
#             'message': 'Cart empty'
#         }
#         return response_object, 201
#     else:
#         response_object = {
#             'status': 'fail',
#             'message': 'User not found.'
#         }

__all__ = ['create_cart', 'get_cart_items', 'get_all_carts', 'add_to_cart']