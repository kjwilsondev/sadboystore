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
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password ')
    })

class CartDto:
    api = Namespace('cart', description='cart operations')
    cart = api.model('cart', {
        'user_id': fields.String(required=True, description='user id')
    })