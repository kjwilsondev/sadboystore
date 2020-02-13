from flask import request
from flask_restplus import Resource

from ..util.dto import CartItemDto
from ..service.cart_service import *

api = CartItemDto.api
_cartitem = CartItemDto.cartitem

@api.route('/<public_id>/')
@api.param('public_id', 'The User Cart identifier')
class Cart(Resource):
    @api.doc('get a cart')
    @api.marshal_list_with(_cartitem, envelope='data')
    def get(self, public_id):
        """Get a cart given user id"""
        items = get_cart_items(public_id)
        if not items:
            api.abort(404)
        else:
            return items

    @api.doc('add item to cart')
    @api.response(404, 'Cart or Item not found.')
    @api.expect(_cartitem)
    def post(self, public_id):
        """Add item to cart given user id"""
        data = request.json
        return add_to_cart(public_id=public_id, item_data=data)
