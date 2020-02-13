import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.cart import Cart
from app.main.model.item import Item
from app.main.model.cart_item import CartItem

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
        user_id=public_id
    )
    db.session.add(new_cart)
    db.session.commit()
    return new_cart

def get_cart_items(public_id):
    # cart = Cart.query.filter_by(user_id=public_id).first()
    items = CartItem.query.filter_by(cart_id=public_id).all()
    print(items)
    return items

def get_all_carts():
    # returns carts in order of cost
    # return Cart.query.order_by(User.registered_on).all()
    return Cart.query.all()

def add_to_cart(public_id, item_data):
    user = User.query.filter_by(public_id=public_id).first()
    item = Item.query.filter_by(public_id=item_data['item_id']).first()
    print(item)
    quantity = item_data['quantity']
    if not user:
        message = "User not found"
    if not item:
        message = "Item not found"
    if user and item:
        user._cart.size += 1
        user._cart._items.append(CartItem(
            cart_id=public_id,
            item_id=item.public_id,
            cost=item.cost,
            quantity=quantity
        ))
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Added item to cart',
            '_cart.cost': user._cart.cost,
            '_cart.size': user._cart.size
        }
        return response_object, 201

    response_object = {
        'status': 'fail',
        'message': message
    }
    return response_object, 404


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