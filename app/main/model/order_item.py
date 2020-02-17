from .. import db, flask_bcrypt
from sqlalchemy.ext.associationproxy import association_proxy
from ..config import key

from ..model.item import Item

class OrderItem(db.Model):
    """
    Order Item Model association table for retrieving:
        order items in user cart
        TODO: orders with item in their cart
    """
    __tablename__ = "order_item"

    # Cart Item fields
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cost = db.Column(db.Float)
    quantity = db.Column(db.Integer, default=1)
    name = db.Column(db.String)

    # Cart fields
    order_id = db.Column(db.String(100), db.ForeignKey('order.user_id'), primary_key=True, nullable=False)

    # Item fields
    item_id = db.Column(db.String(100), db.ForeignKey('item.public_id'), primary_key=True)
    item = db.relationship('Item')

    def __str__(self):
        return "<CartItem '{}', {}>".format(self.item_id, self.quantity)

    #TODO: Make a __repr__