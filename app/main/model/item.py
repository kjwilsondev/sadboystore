from .. import db, flask_bcrypt
import datetime
from ..config import key

from ..model.user import User

class Item(db.Model):
    """
    Item Model for storing item related details
    """
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    release_date = db.Column(db.DateTime)

    # Item fields
    name = db.Column(db.String(100), nullable=False, default="sadface")
    piece = db.Column(db.String(50), nullable=False, default="shirt") # type of clothing
    cost = db.Column(db.Float, nullable=False, default=15.0)

    # Item View fields
    color = db.Column(db.String(50))
    size = db.Column(db.String(10), nullable=False)
    available = db.Column(db.Integer, nullable=False)
    # picture = db.relationship("Picture", backref="item.name", lazy=True)

    # Store fields
    carts = db.relationship("Cart", secondary="cart_item")
    # closets = db.relationship("User", secondary="closet")
    # orders = db.relationship("User", secondary="order")
    
    @classmethod
    def update_cost(self, cost):
        old_cost, self.cost = self.cost, cost
        response_object = {
            'status': 'success',
            'message': 'Cost updated',
            'old_cost': old_cost,
            'cost': self.cost
        }
        return response_object, 201
    
    @classmethod
    def update_availability(self, update):
        self.available += update
        response_object = {
            'status': 'success',
            'message': 'Availability updated',
            'available': self.available
        }
        return response_object, 201

    @classmethod
    def add_to_cart(self, public_id):
        user = User.query.filter_by(public_id=public_id).first()
        user.cart.items.append(self)
        user.cart.cost += self.cost
        user.cart.size += 1
        print(user.cart.items)
        response_object = {
            'status': 'success',
            'message': 'Item added to cart',
            'item': self.name
        }
        return response_object, 201