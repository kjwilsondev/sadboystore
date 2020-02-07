import uuid
import datetime

from app.main import db
from app.main.model.user import User


def create_cart(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    new_cart = Cart(
        cost = 0.0,
        user_id = user.public_id
    )
    db.session.add(new_cart)
    db.session.commit()
    return new_cart

def get_all_carts():
    return Cart.query.all()

def get_a_cart(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    # return user.cart.items
    return user.cart

def empty_cart(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    cart = user.cart
    user.cart = Cart(
        cost = 0.0,
        user_id = user.public_id
    )
    print("new cart created")
    user.cart = new_cart
    db.session.delete(cart)
    db.session.add(new_cart)
    db.session.commit()
    return user.cart