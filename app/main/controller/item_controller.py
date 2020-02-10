from flask import request
from flask_restplus import Resource

from ..util.dto import ItemDto
from ..service.item_service import *

api = ItemDto.api
_item = ItemDto.item

@api.route('/')
class ItemList(Resource):
    @api.doc('list of store items')
    @api.marshal_list_with(_item, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_items()

    @api.response(201, 'Item successfully created.')
    @api.doc('create a new item')
    @api.expect(_item, validate=True)
    def post(self):
        """Creates a new Item"""
        data = request.json
        return create_item(data=data)

@api.route('/<name>/')
@api.param('name', 'Item Name')
@api.response(404, 'Item not found.')
class ItemList(Resource):
    @api.doc('get items by name')
    @api.marshal_with(_item)
    def get(self, name):
        """get a item given its name"""
        items = get_items(name)
        info = get_item_info(name)
        if not items:
            api.abort(404)
        else:
            return items, info
