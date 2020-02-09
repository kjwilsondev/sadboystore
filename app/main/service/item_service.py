import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.cart import Cart

# TODO:
# create item
# get item
# check item sizes
# check item colors
# check item availability
# delete item

def create_item(data):
    name = data['name']
    piece = data['piece']
    color = data['color']
    size = data['size']
    item = Item.query.filter_by(
        name=name,
        piece=piece,
        color=color,
        size=size
        ).first()
    if not item:
        new_item = Item(
            release_date=datetime.datetime.utcnow(),
            name=name,
            piece=piece,
            cost=float(cost),
            color=color,
            size=size,
            availabile=data['available']
        )
        db.session.add(new_item)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully created item.',
            'item_name': name,
            'available': availability
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Item already exists.',
        }
        return response_object, 409

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
