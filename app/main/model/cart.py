from .. import db, flask_bcrypt
import datetime
from ..config import key
from app.main.model.user import User

# Cart class inherits from db.Model class which declares the class as a model for sqlalchemy
class Cart(db.Model):
    """
    Cart Model for storing cart related details
    """
    __tablename__ = "cart"

    # Cart fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    set_on = db.Column(db.DateTime, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    # One to One
    user = db.relationship("User", back_populates="cart")
    user_id = db.Column(db.Integer, db.ForeignKey('user.public_id'))
    # One to Many
    items = db.relationship('Item', backref='cart', lazy=True)

    @staticmethod
    def add_cost(self, cost): # O(1)
        self.cost += cost
        return self.cost

    @staticmethod
    def sum_cost(self): # O(n)
        cost = 0.0
        # n = number of items
        # n iterations => O(n)
        for item in Item.query.filter_by(cart_id=self.cart_id).all():
            cost += item.cost
        self.cost = cost
        # print(f"cart {cart.id} updated cost: {cost}")
        return cost


