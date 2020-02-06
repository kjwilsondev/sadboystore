from flask_restplus import Namespace, fields



class UserDto:
    api = Namespace('user', description='user operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'fname': fields.String(required=False, description='user first name'),
        'lname': fields.String(required=False, description='user last name'),
        'phone': fields.String(required=True, description='user phone number'),
        'address': fields.String(required=True, description='user address'),
        'city': fields.String(required=False, description='user city'),
        'zip_code': fields.String(required=False, description='user zip code'),
        'closet': fields.String(required=False, description='user closet'),
        'cart': fields.String(required=True, description='user closet'),
        'orders': fields.String(required=False, description='user closet')
    })

class CartDto:
    api = Namespace('cart', description='cart operations')
    cart = api.model('cart', {
        'cost': fields.String(required=False, description='cart cost'),
        'user_id': fields.String(required=False, description='user id'),
        # Items will be added by separate function
        # 'items': fields.String(required=True, description='cart items')
    })