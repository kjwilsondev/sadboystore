from flask_restplus import Namespace, fields

class AuthDto:
    api = Namespace('auth', description='authentication operations')
    user_auth = api.model('auth', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password ')
    })

class UserDto:
    api = Namespace('user', description='user operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='email address'),
        'password': fields.String(required=True, description='password'),
        'fname': fields.String(required=False, description='first name'),
        'lname': fields.String(required=False, description='last name'),
        'phone': fields.String(required=False, description='phone number'),
        'address': fields.String(required=False, description='user address'),
        'city': fields.String(required=False, description='city'),
        'zip_code': fields.Integer(required=False, description='zip code')
    })

class CartDto:
    api = Namespace('cart', description='cart operations')
    cart = api.model('cart', {
        'user_id': fields.String(required=True, description='cart user id'),
        'cost': fields.Float(required=True, description='cart cost')
    })

class ItemDto:
    api = Namespace('item', description='item operations')
    item = api.model('item', {
        'name': fields.String(required=True, description='item name'),
        'piece': fields.String(required=True, description='item piece'),
        'cost': fields.Float(required=True, description='item cost'),
        'color': fields.String(required=True, description='item color'),
        'size': fields.String(required=True, description='item size'),
        'available': fields.Integer(required=True, description='item available'),
    })