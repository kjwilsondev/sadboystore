from flask import request
from flask_restplus import Resource

from ..util.dto import CartDto
from ..util.dto import UserDto
from ..service.cart_service import get_a_cart, get_all_carts, empty_cart

api = CartDto.api
_cart = CartDto.cart
_user = UserDto.user

@api.route('/carts')
class CartList(Resource):
    @api.doc('list of carts')
    @api.marshal_list_with(_cart, envelope='data')
    def get(self):
        """List all budgets"""
        return get_all_carts()

@api.route('/<public_id>/cart')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class Cart(Resource):
    @api.doc('get a user')
    @api.marshal_with(_cart)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user.cart
            # return user.cart.items
