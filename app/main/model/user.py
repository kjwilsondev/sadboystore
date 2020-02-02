from .. import db, flask_bcrypt
import datetime
from ..config import key
# from app.main.model.blacklist import BlacklistToken
# import jwt

# User class inherits from db.Model class which declares the class as a model for sqlalchemy
class User(db.Model):
    """ 
    User Model for storing user related details
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # password_hash = db.Column(db.String(100))

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
    closet = relationship("Closet", uselist=False, back_populates="user.public_id")
    cart = relationship("Cart", uselist=False, back_populates="user.public_id")
    orders = db.relationship("Order", lazy='select', backref=db.backref("user.public_id", lazy='joined'))

    def __repr__(self):
        return "<User '{}'>".format(self.username)

    # @property
    # def password(self):
    #     raise AttributeError('password: write-only field')

    # password.setter uses flask-bcrypt to generate a hash using the provided password.
    # @password.setter
    # def password(self, password):
    #     self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    # def check_password(self, password):
    #     return flask_bcrypt.check_password_hash(self.password_hash, password)

    # @staticmethod
    # def encode_auth_token(user_id):
    #     """
    #     Generates the Auth Token
    #     :return: string
    #     """
    #     try:
    #         payload = {
    #             'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
    #             'iat': datetime.datetime.utcnow(),
    #             'sub': user_id
    #         }
    #         return jwt.encode(
    #             payload,
    #             key,
    #             algorithm='HS256'
    #         )
    #     except Exception as e:
    #         return e

    # @staticmethod
    # def decode_auth_token(auth_token):
    #     """
    #     Decodes the auth token
    #     :param auth_token:
    #     :return: integer|string
    #     """
    #     try:
    #         payload = jwt.decode(auth_token, key)
    #         is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
    #         if is_blacklisted_token:
    #             return 'Token blacklisted. Please log in again.'
    #         else:
    #             # returns user_id
    #             return payload['sub']
    #     except jwt.ExpiredSignatureError:
    #         return 'Signature expired. Please log in again.'
    #     except jwt.InvalidTokenError:
    #         return 'Invalid token. Please log in again.'
            