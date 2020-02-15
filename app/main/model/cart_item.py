from .. import db, flask_bcrypt
from sqlalchemy.ext.associationproxy import association_proxy
from ..config import key
import json

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
    cost = db.Column(db.Float)
    quantity = db.Column(db.Integer, default=1)
    name = db.Column(db.String)

    # Cart fields
    cart_id = db.Column(db.String(100), db.ForeignKey('cart.user_id'), primary_key=True, nullable=False)
    # cartitems = db.relationship("Cart", backref=db.backref("_items"))
    # cartitems = db.relationship("Cart", back_populates="_items", single_parent=True, cascade="all, delete-orphan")

    # Item fields
    item_id = db.Column(db.String(100), db.ForeignKey('item.public_id'), primary_key=True)
    item = db.relationship('Item')
    # itemcarts = db.relationship("Item", backref=db.backref("_carts"))
    # itemcarts = db.relationship("Item", back_populates="_carts", cascade="all, delete-orphan")

    def __str__(self):
        return "<CartItem '{}', {}>".format(self.item_id, self.quantity)

    #TODO: Make a __repr__