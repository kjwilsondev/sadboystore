# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.cart_controller import api as cart_ns
from .main.controller.cart_item_controller import api as cartitem_ns
from .main.controller.item_controller import api as item_ns

blueprint = Blueprint('api', __name__)

# TODO: Authorizations
# authorizations = {
#     'apikey': {
#         'type': 'apiKey',
#         'in': 'header',
#         'name': 'X-API-KEY'
#     }
# }

api = Api(blueprint,
          title='Sad Boy Store Backend',
          version='1.0',
          # authorizations=authorizations,
          description='sad boy merch'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(cart_ns, path='/cart')
api.add_namespace(cartitem_ns, path='/cart')
api.add_namespace(item_ns, path='/item')
api.add_namespace(auth_ns)