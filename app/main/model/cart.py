from .. import db, flask_bcrypt
from ..config import key

from ..model.user import User
from ..model.cart_item import CartItem

class Cart(db.Model):
    """ 
    Cart Model for storing user related details
    """ 
    __tablename__ = "cart"

    # Cart fields
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cost = db.Column(db.Float, default=0.0)
    size = db.Column(db.Integer, default=0)

    # User fields
    user_id = db.Column(db.String(100), db.ForeignKey('user.public_id'), unique=True)

    # Item fields
    _items = db.relationship("Item", secondary="cart_item", lazy='subquery', backref=db.backref('cart', lazy=True))

    @classmethod
    def remove_cart_item(self, item_public_id):
        for item in self.items:
            if item.public_id == item_public_id:
                self.size -= 1
                self.cost -= item.cost
                response_object = {
                    'status': 'success',
                    'message': 'Successfully removed item.',
                    'item_name': item.name,
                }
                if item.quantity > 0:
                    item.quantity -= 1
                    return response_object, 201
                else:
                    db.session.delete(item)
                    db.session.commit()
                    return response_object, 201
        response_object = {
            'status': 'fail',
            'message': 'Item not in cart',
        }
        return response_object, 409
