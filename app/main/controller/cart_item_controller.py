from flask import request
from flask_restplus import Resource

from ..util.dto import CartItemDto
from ..service.cart_service import *

api = CartItemDto.api
_cartitem = CartItemDto.cartitem


# @api.route('/<public_id>/<item_id>')
# @api.param('public_id', 'User Cart identifier')
# @api.param('item_id', 'Item identifier')
# @api.response(404, 'User or Item not found')
# class CartItemList(Resource):
#     @api.doc('delete an item a cart')
#     # def get(self, public_id):
#     #     """Get a cart given user id"""
#     #     items = get_cart_items(public_id)
#     #     if not items:
#     #         api.abort(404)
#     #     else:
#     #         return items
