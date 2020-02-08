from .. import db, flask_bcrypt
import datetime
from ..config import key

from app.main.model.cart import Cart

class Item(db.Model):
    """
    Item Model for storing item related details
    """
    __tablename__ = "item"

    # Item fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, default="sadface")
    piece = db.Column(db.String(50), nullable=False, default="shirt") # type of clothing
    cost = db.Column(db.Float, nullable=False, default=15.0)
    # picture = db.relationship("Picture", backref="item.name", lazy=True)

    # Cart fields
    carts = db.relationship("User", secondary="cart")
    # closets = db.relationship("User", secondary="closet")
    # orders = db.relationship("User", secondary="order")
    # parents = relationship("Association", back_populates="child")
    