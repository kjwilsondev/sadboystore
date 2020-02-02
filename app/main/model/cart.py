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
    cost = db.Column(db.Integer, nullable=False)

    user = db.relationship("User", back_populates="cart")
    user_id = db.Column(db.Integer, db.ForeignKey('user.public_id'))
    items = db.relationship('Item', backref='cart', lazy=True)

    # @staticmethod
    # def sum_cost(self):
    #     for item in Item.query.filter_by(cart_id=cart_id).all():
    #         cost += item.cost
    #     self.cost = cost
    #     return


