import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.cart import Cart

# TODO:
# Edit cart_service methods to match new class
# Add to Cart
# Calculate cost of cart
# response object for 
# {
#     cart user,
#     cart cost,
#     cart length,
# }

def create_cart(public_id):
    new_cart = Cart(
        cost = 0.0,
        user_id = public_id
    )
    db.session.add(new_cart)
    db.session.commit()
    return new_cart

def get_cart_items(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    return user.cart_items

def get_cart_users(item_name):
    item = Item.query.filter_by(item_name=item_name).first()
    return item.carts

def empty_cart(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    cart = user.cart_items
    user.cart_items = create_cart(public_id)
    db.session.delete(cart)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Cart empty'
    }
    return response_object, 201

# @staticmethod
#     def check_cost(self, user_id): # O(n)
#         cost = 0.0
#         # n = number of items
#         # n iterations => O(n)
#         for item in Item.query.filter_by(cart_id=self.cart_id).all():
#             cost += item.cost
#         self.cost = cost
#         # print(f"cart {cart.id} updated cost: {cost}")
#         return cost