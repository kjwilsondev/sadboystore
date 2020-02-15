import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.item import Item
from app.main.model.cart import Cart
from app.main.model.cart_item import CartItem


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
def get_items_by_name(name):
    items = Item.query.filter_by(name=name).all()
    return items

# get items by id
def get_item_by_id(public_id):
    item = Item.query.filter_by(public_id=public_id).first()
    return item

# returns user carts that contain item
# def get_cart_users(cart_id):
#     cart_items = CartItem.query.filter_by(=cart_id).first()
#     return item._carts

# delete item function
def delete_item_by_id(item_public_id):
    item = Item.query.filter_by(public_id=item_public_id).first()
    cart_items = CartItem.query.filter_by(item_id=item_public_id).all()
    if item:
        if cart_items:
            try:
                # delete all cart items
                for cart_item in cart_items:
                    cart = Cart.query.filter_by(user_id=cart_item.cart_id)
                    cart.cost -= cart_item.cost * cart_item.quantity
                    cart.size -= cart_item.quantity
                    db.session.delete(cart_item)
                db.session.commit()
            except:
                db.session.rollback()
                raise
        # checks if item is selling
        if item.selling:
            try:
                item.selling = False
                item.available = 0
                db.session.commit()
            except:
                db.session.rollback()
                raise
            else:
                response_object = {
                    'status': 'success',
                    'message': 'Successfully removed item from store.',
                    'item_name': item.name
                }
                return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Item already off store.',
            }
            return response_object, 409

    else:
        response_object = {
            'status': 'fail',
            'message': 'Item not found.',
        }
        return response_object, 409

__all__ = ['create_item', 'get_items_by_name', 'get_all_items', 'delete_item_by_id']