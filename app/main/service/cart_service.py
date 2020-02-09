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
        public_id=str(uuid.uuid4()),
        cost = 0.0,
        user_id = public_id
    )
    db.session.add(new_cart)
    db.session.commit()
    return new_cart

def get_cart_items(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    return user.cart.items

def get_all_carts():
    # returns carts in order of cost
    return Cart.query.order_by(User.registered_on).all()

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
