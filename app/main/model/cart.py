from .. import db, flask_bcrypt
from sqlalchemy.ext.associationproxy import association_proxy
from ..config import key

from ..model.user import User
from ..model.cart_item import CartItem

class Cart(db.Model):
    """ 
    Cart Model for storing user cart related details
    """ 
    __tablename__ = "cart"

    # Cart fields
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cost = db.Column(db.Float, default=0.0)
    size = db.Column(db.Integer, default=0)

    # User fields
    user_id = db.Column(db.String(100), db.ForeignKey('user.public_id'), unique=True)

    # Item fields
    # _items = db.relationship("CartItem", back_populates="cartitems")
    # _items = db.relationship("Item", secondary="cart_item", viewonly=True)
    _items = db.relationship('CartItem', cascade='all, delete-orphan')
    cart_items = association_proxy('_items', 'item', creator=lambda item: CartItem(item=item))

    def __str__(self):
        return "<Cart '{}'>".format(self.user_id)

    #TODO: Make a __repr__
