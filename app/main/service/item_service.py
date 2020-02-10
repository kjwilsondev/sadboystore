import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.item import Item
from app.main.model.cart import Cart


def create_item(data):
    name = data['name']
    piece = data['piece']
    cost = data['cost']
    color = data['color']
    size = data['size']
    available = data['available']
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
            available=available
        )
        db.session.add(new_item)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully created item.',
            'item_name': name,
            'available': available
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

# returns user carts that contain item
def get_cart_users(item_name):
    item = Item.query.filter_by(item_name=item_name).first()
    return item._carts

# draft delete function
# not sure how cart will handle deleted cart items
def delete_item(item_public_id):
    item = Item.query.filter_by(public_id=item_public_id).first()
    name = item.name
    if item:
        db.session.delete(item)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted item.',
            'item_name': name,
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Item not found.',
        }
        return response_object, 409

__all__ = ['create_item', 'get_items', 'get_item_info', 'get_cart_users', 'delete_item']