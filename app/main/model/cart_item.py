from .. import db, flask_bcrypt
from ..config import key

from ..model.item import Item

class CartItem(db.Model):
    """
    Cart Item Model association table for retrieving:
        cart items in user cart
        carts with item in their cart
    """
    __tablename__ = "cart_item"

    # Cart Item fields
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    quantity = db.Column(db.Integer, default=1)

    # Cart fields
    cart_id = db.Column(db.String(100), db.ForeignKey('cart.user_id'), primary_key=True)
    cartitems = db.relationship("Cart", back_populates="_items")

    # Item fields
    item_id = db.Column(db.String(100), db.ForeignKey('item.public_id'), primary_key=True, unique=True)
    itemcarts = db.relationship("Item", back_populates="_carts")
