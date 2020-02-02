from .. import db
import datetime
from ..config import key

# User class inherits from db.Model class which declares the class as a model for sqlalchemy
class User(db.Model):
    """ 
    User Model for storing user related details
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # User Contact fields
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True)
    address = db.Column(db.String(100))
    city = db.Column(db.String(100))
    zip_code = db.Column(db.String(5))

    # User fields
    registered_on = db.Column(db.DateTime, nullable=False)
    public_id = db.Column(db.String(100), unique=True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    admin = db.Column(db.Boolean, nullable=False, default=False)

    # Store fields
    closet = db.relationship("Closet", uselist=False, back_populates="user.public_id")
    cart = db.relationship("Cart", uselist=False, back_populates="user.public_id")
    orders = db.relationship("Order", lazy='select', backref=db.backref("user.public_id", lazy='joined'))

    def __repr__(self):
        return "<User '{}'>".format(self.username)
            