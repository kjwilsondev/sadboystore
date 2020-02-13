from flask import request
from flask_restplus import Resource

from ..util.dto import ItemDto
from ..service.item_service import *

api = ItemDto.api
_item = ItemDto.item

@api.route('/')
class ItemList(Resource):
    @api.doc('List of store Items')
    @api.marshal_list_with(_item, envelope='data')
    def get(self):
        """Lists all store Items"""
        return get_all_items()

    @api.response(201, 'Item successfully created.')
    @api.doc('Create a new Item')
    @api.expect(_item, validate=True)
    def post(self):
        """Creates a new Item"""
        data = request.json
        return create_item(data=data)

@api.route('/<name>/')
@api.param('name', 'Item Name')
@api.response(404, 'Item not found.')
class ItemList(Resource):
    @api.doc('Get list of Items by name')
    @api.marshal_with(_item, envelope='data')
    def get(self, name):
        """Get Items by name property"""
        items = get_items(name)
        # info = get_item_info(name)
        if not items:
            api.abort(404)
        else:
            return items
