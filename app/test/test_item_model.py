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
from app.main.service.item_service import *

from app.test.base import BaseTestCase


def create_test_item_1():
    return create_item({
        'name': 'test_item_1',
        'piece': 'shirt',
        'cost': 14.99,
        'color': 'black',
        'size': 'S',
        'available': 1
    })

def create_test_item_2():
    return create_item({
        'name': 'test_item_1',
        'piece': 'shirt',
        'cost': 14.99,
        'color': 'black',
        'size': 'L',
        'available': 1
    })

def get_store_items(self):
    return self.client.get(
        '/item/',
        content_type='application/json'
    )

def get_an_item_by_name(self):
    return self.client.get(
        '/test',
        data=json.dumps(dict(
            email='kj1@test.com',
            password='pass'
        )),
        content_type='application/json'
    )

class TestUserCart(BaseTestCase):
    def test_get_all_items(self):
        """ Test for get all store items """
        data = create_test_item_1()
        self.assertTrue(data[0]['status'] == 'success')
        data = create_test_item_2()
        self.assertTrue(data[0]['status'] == 'success')
        with self.client:
            response = get_store_items(self)
            print(response)
            # self.assertTrue(data['status'] == 'success')

    # def test_create_items(self):
    #     data = create_test_item()
    #     self.assertTrue(data[0]['status'] == 'success')

    # def test_create_items(self):
    #     self.assertTrue(data[0]['status'] == 'success')



# class TestAuthBlueprint(BaseTestCase):
#     def test_registration(self):
#         """ Test for user registration """
#         with self.client:
#             response = register_user(self)
#             data = json.loads(response.data.decode())
#             self.assertTrue(data['status'] == 'success')
#             self.assertTrue(data['message'] == 'Successfully registered.')
#             self.assertTrue(data['Authorization'])
#             self.assertTrue(response.content_type == 'application/json')
#             self.assertEqual(response.status_code, 201)

#     def test_registered_with_already_registered_user(self):
#         """ Test registration with already registered email"""
#         register_user(self)
#         with self.client:
#             response = register_user(self)
#             data = json.loads(response.data.decode())
#             self.assertTrue(data['status'] == 'fail')
#             self.assertTrue(
#                 data['message'] == 'User already exists. Please Log in.')
#             self.assertTrue(response.content_type == 'application/json')
#             self.assertEqual(response.status_code, 409)