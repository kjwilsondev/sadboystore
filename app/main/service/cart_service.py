import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.cart import Cart
from app.main.model.item import Item
from app.main.model.cart_item import CartItem


def create_cart(public_id):
    new_cart = Cart(
        user_id=public_id
    )
    db.session.add(new_cart)
    db.session.commit()
    return new_cart

def get_cart_items(public_id):
    items = CartItem.query.filter_by(cart_id=public_id).all()
    return items

def get_all_carts():
    # returns carts in order of cost
    # return Cart.query.order_by(Cart.cost).all()
    return Cart.query.all()

def add_to_cart(public_id, item_data):
    user = User.query.filter_by(public_id=public_id).first()
    item = Item.query.filter_by(public_id=item_data['item_id']).first()
    try:
        quantity = item_data['quantity']
    except KeyError:
        print("setting quantity to 1")
        quantity = 1

    if not user:
        message = "User not found"
    if not item:
        message = "Item not found"
    
    if user and item:
        # check if item already in cart
        cart_item = CartItem.query.filter_by(
            cart_id=public_id, 
            item_id=item_data['item_id']
        ).first()
        if cart_item:
            try:
                cart_item.quantity += quantity
                # need to write update cart cost function
                user._cart.cost += cart_item.cost * quantity
                user._cart.size += quantity
                db.session.commit()
            except:
                db.session.rollback()
                raise
        # if no item create item
        else:
            try:
                user._cart._items.append(CartItem(
                    cart_id=public_id,
                    item_id=item.public_id,
                    name=item.name,
                    cost=item.cost,
                    quantity=quantity
                ))
                db.session.commit()
            except:
                db.session.rollback()
                raise
            else:
                # need to write update cart cost function
                user._cart.cost += item.cost * quantity
                user._cart.size += quantity

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

def remove_cart_item(public_id, item_id):
    user = User.query.filter_by(public_id=public_id).first()
    item = CartItem.query.filter_by(cart_id=public_id,item_id=item_id).first()
    print(item)
    if not user:
        message = "User not found"
    if not item:
        message = "Item not found"
    if user and item:
        try:
            item_cost = item.cost
            item_quantity = item.quantity
            db.session.delete(item)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        else:
            # need to write update cart cost function
            user._cart.size -= item_quantity
            user._cart.cost -= item_cost * item_quantity
            response_object = {
                'status': 'success',
                'message': 'Item removed from cart',
                '_cart.cost': user._cart.cost,
                '_cart.size': user._cart.size
            }
            return response_object, 201
    response_object = {
        'status': 'fail',
        'message': message
    }
    return response_object, 404

def empty_cart(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    items = CartItem.query.filter_by(cart_id=public_id).all()
    if items:
        print(here)
        try:
            for item in items:
                # print(item)
                db.session.delete(item)
        except:
            db.session.rollback()
            raise
        else:
            # need to write update cart cost function
            user._cart.cost = 0
            user._cart.size = 0
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': 'Cart empty'
            }
            return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'No items found.'
        }
        print(user._cart)
        print(user._cart.cost)
        return response_object, 201

__all__ = ['create_cart', 'get_cart_items', 'get_all_carts', 'add_to_cart', 'remove_cart_item', 'empty_cart']