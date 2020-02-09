from .. import db, flask_bcrypt
from ..config import key


class Cart(db.Model):
    """
    Cart Model association table for retrieving:
        items in user cart
        users with item in their cart
    """
    __tablename__ = "cart"

    # Cart fields
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    # User fields
    user_id = db.Column(db.String(100), db.ForeignKey('user.public_id'))
    user = relationship("User", back_populates="cart_items")

    # Item fields
    item_name = db.Column(db.String(100), db.ForeignKey('item.name'))
    item = relationship("Item", back_populates="carts")
