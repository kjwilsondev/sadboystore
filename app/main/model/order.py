from .. import db, flask_bcrypt
from sqlalchemy.ext.associationproxy import association_proxy
from ..config import key

from ..model.order_item import OrderItem

class Order(db.Model):
    """ 
    Order Model for storing order related details
    """ 
    __tablename__ = "order"

    # Order fields
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    confirmation = db.Column(db.String(100), unique=True)
    cost = db.Column(db.Float, default=0.0)
    size = db.Column(db.Integer, default=0)
    ordered_on = db.Column(db.DateTime)

    # User fields
    user_id = db.Column(db.String(100), db.ForeignKey('user.public_id'), nullable=False, primary_key=True)

    # Item fields
    _items = db.relationship('OrderItem', cascade='all, delete-orphan')
    order_items = association_proxy('_items', 'item', creator=lambda item: OrderItem(item=item))


    def __str__(self):
        return "<Order '{}'>".format(self.user_id)

    #TODO: Make a __repr__

    # def address(self):
    #     user = User.query.filter_by()
