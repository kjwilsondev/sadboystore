import unittest
import json

from app.main import db
from app.main.model.blacklist import BlacklistToken
from app.main.model.user import User
from app.main.model.cart import Cart
from app.main.model.cart_item import CartItem
from app.main.model.item import Item

from app.main.service.user_service import *
from app.main.service.cart_service import *

from app.test.base import BaseTestCase

# def register_user(self):
#     return self.client.post(
#         '/user/',
#         data=json.dumps(dict(
#             email='joe@gmail.com',
#             password='123456'
#         )),
#         content_type='application/json'
#     )


# def login_user(self):
#     return self.client.post(
#         '/auth/login',
#         data=json.dumps(dict(
#             email='joe@gmail.com',
#             password='123456'
#         )),
#         content_type='application/json'
#     )

class TestUserCart(BaseTestCase):
    def test_cart_returns_items(self):
        print("test cart returns items")
