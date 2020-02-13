from flask import request
from flask_restplus import Resource

from ..util.dto import CartDto, UserDto, ItemDto
from ..service.user_service import get_a_user
from ..service.cart_service import *

api = CartDto.api
_cart = CartDto.cart
_user = UserDto.user
_item = ItemDto.item

@api.route('/')
class CartList(Resource):
    @api.doc('list of carts')
    @api.marshal_list_with(_cart, envelope='data')
    def get(self):
        """List all carts"""
        return get_all_carts()
    
    # @api.doc('empty a cart')
    # @api.response(201, 'Cart empty.')
    # def delete(self, public_id):
    #     """Empty user cart"""
    #     user = get_a_user(public_id)
    #     if not user:
    #         api.abort(404)
    #     else:
    #         return empty_cart(public_id)
    