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
        try:
            new_item = Item(
                public_id=str(uuid.uuid4()),
                release_date=datetime.datetime.utcnow(),
                name=name,
                piece=piece,
                cost=float(cost),
                color=color,
                size=size,
                available=available
            )
            db.session.add(new_item)
        except:
            db.session.rollback()
            raise
        else:
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': 'Successfully created item.',
                'item_name': name,
                'public_id': new_item.public_id
            }
            return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Item already exists.',
        }
        return response_object, 409

# get all items by name
def get_all_items():
    # return Item.query.order_by(Item.release_date.desc()).all()
    return Item.query.all()

# get items by name
def get_items(name=None, piece=None):
    items = Item.query.filter_by(name=name).all()
    return items

# returns user carts that contain item
# def get_cart_users(item_name):
#     item = Item.query.filter_by(name=item_name).first()
#     return item._carts

# draft delete function
# not sure how cart will handle deleted cart items
# def delete_item(item_public_id):
#     item = Item.query.filter_by(public_id=item_public_id).first()
#     name = item.name
#     if item:
#         db.session.delete(item)
#         db.session.commit()
#         response_object = {
#             'status': 'success',
#             'message': 'Successfully deleted item.',
#             'item_name': name,
#         }
#         return response_object, 201
#     else:
#         response_object = {
#             'status': 'fail',
#             'message': 'Item not found.',
#         }
#         return response_object, 409

__all__ = ['create_item', 'get_items', 'get_all_items']