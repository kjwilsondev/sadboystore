from flask_restplus import Namespace, fields

class AuthDto:
    api = Namespace('auth', description='authentication operations')
    user_auth = api.model('auth', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
    
class UserDto:
    api = Namespace('user', description='user operations')
    user = api.model('user', {
        'fname': fields.String(required=False, description='user first name'),
        'lname': fields.String(required=False, description='user last name'),
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password')
        # TODO: plaid token
        # TODO: phone numbers for texting updates
    })

class BudgetDto:
    api = Namespace('budget', description='budget operations')
    budget = api.model('budget', {
        'length': fields.String(required=True, description='time length of budget'),
        'amount': fields.String(required=True, description='budget amount'),
        'success': fields.String(required=False, description='True if user spent less than budget'),
        'public_id': fields.String(required=True, description='True if user spent less than budget')
    })