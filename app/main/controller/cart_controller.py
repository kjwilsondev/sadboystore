from flask import request
from flask_restplus import Resource

from ..util.dto import CartDto
from ..util.dto import UserDto
from ..service.user_service import get_a_user
from ..service.cart_service import *

api = CartDto.api
_cart = CartDto.cart
_user = UserDto.user

@api.route('/')
class CartList(Resource):
    @api.doc('list of carts')
    @api.marshal_list_with(_cart, envelope='data')
    def get(self):
        """List all carts"""
        return get_all_carts()

@api.route('/<public_id>/')
@api.param('public_id', 'The User Cart identifier')
class Cart(Resource):
    @api.doc('get a cart')
    @api.marshal_with(_cart)
    def get(self, public_id):
        """Get a cart given user id"""
        items = get_cart_items(public_id)
        if not items:
            api.abort(404)
        else:
            return items
    
    @api.doc('add item to cart')
    @api.response(404, 'Cart or Item not found.')
    def post(self, public_id):
        """Get a cart given user id"""
        # resquest should be item public_id
        data = request.json
        return add_to_cart(public_id=public_id, item_data=data)
    
    # @api.doc('empty a cart')
    # @api.response(201, 'Cart empty.')
    # def delete(self, public_id):
    #     """Empty user cart"""
    #     user = get_a_user(public_id)
    #     if not user:
    #         api.abort(404)
    #     else:
    #         return empty_cart(public_id)
    