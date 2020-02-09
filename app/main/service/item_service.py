import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.cart import Cart

# TODO:
# get item
# check item sizes
# check item colors
# check item availability
# delete item

# create item ✅
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

# get items by name
def get_items(name):
    items = Item.query.filter_by(name=name).all()
    return items

# get item by 
def get_item_info(name):
    items = Item.query.filter_by(name=name).all()
    cost = items[0].cost
    colors = {} # histgram (key: color, value: available)
    sizes = {} # histgram (key: size, value: available)

    if items:
        for item in items:
            if item.color in colors:
                colors[item.color] += 1
            else:
                colors[item.color] = 1
            if item.size in sizes:
                sizes[item.size] += 1
            else:
                sizes[item.size] = 1

        response_object = {
            'status': 'success',
            'message': 'Items located',
            'cost': cost,
            'colors': colors,
            'sizes': sizes
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Item not found.',
        }
        return response_object, 409

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
