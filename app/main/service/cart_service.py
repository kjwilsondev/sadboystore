import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.cart import Cart


def create_cart(public_id):
    new_cart = Cart(
        cost = 0.0,
        user_id = public_id
    )
    db.session.add(new_cart)
    db.session.commit()
    return new_cart

def get_all_carts():
    # returns carts in order of cart cost
    # most expensive will be at the top
    return Cart.query.order_by(Cart.cost.desc()).all()

def get_a_cart(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    # return user.cart.items
    return user.cart

def empty_cart(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    cart = user.cart
    user.cart = create_cart(public_id)
    print("new cart created")
    db.session.delete(cart)
    print("old cart deleted")
    db.session.commit()
    return user.cart