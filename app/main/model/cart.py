from .. import db, flask_bcrypt
import datetime
from ..config import key

from app.main.model.user import User
# from app.main.model.item import Item

class Cart(db.Model):
    """
    Cart Model for storing cart related details
    """
    __tablename__ = "cart"

    # Cart fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cost = db.Column(db.Float)

    # User fields
    user_id = db.Column(db.String(100), db.ForeignKey('user.public_id'), nullable=False)

    # Item fields
    items = db.relationship('Item', backref='cart', lazy=True)
    # size = db.Column(db.Integer)

    @classmethod
    def add_to_cost(self, cost): # O(1)
        self.cost += cost
        return self.cost

    # @staticmethod
    # def check_cost(self): # O(n)
    #     cost = 0.0
    #     # n = number of items
    #     # n iterations => O(n)
    #     for item in Item.query.filter_by(cart_id=self.cart_id).all():
    #         cost += item.cost
    #     self.cost = cost
    #     # print(f"cart {cart.id} updated cost: {cost}")
    #     return cost


