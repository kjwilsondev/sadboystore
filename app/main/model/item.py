from .. import db, flask_bcrypt
from sqlalchemy.ext.associationproxy import association_proxy

import datetime
from ..config import key


class Item(db.Model):
    """
    Item Model for storing item related details
    """
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    release_date = db.Column(db.DateTime)
    selling = db.Column(db.Boolean, nullable=False, default=True)

    # Item fields
    name = db.Column(db.String(100), nullable=False, default="sadface")
    category = db.Column(db.String(50), nullable=False, default="shirt") # type of clothing
    cost = db.Column(db.Float, nullable=False, default=15.0)

    # Item View fields
    color = db.Column(db.String(50))
    size = db.Column(db.String(10), nullable=False)
    available = db.Column(db.Integer, nullable=False)
    picture = db.Column(db.String)

    def __str__(self):
        return "<Item '{}', '{}'>".format(self.public_id, self.cost)

    #TODO: Make a __repr__

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
