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

def register_user(self):
    return self.client.post(
        '/user/',
        data=json.dumps(dict(
            email='kj@test.com',
            password='kjtest'
        )),
        content_type='application/json'
    )

def create_test_item_1():
    return create_item({
        'name': 'test_item_1',
        'category': 'shirt',
        'cost': 14.99,
        'color': 'black',
        'size': 'S',
        'available': 1
    })

def create_test_item_2():
    return create_item({
        'name': 'test_item_1',
        'category': 'shirt',
        'cost': 14.99,
        'color': 'black',
        'size': 'L',
        'available': 1
    })

def add_item_to_cart(self, cart_route, item_id):
    return self.client.get(
        cart_route,
        data=json.dumps(dict(
            item_id=item_id
        )),
        content_type='application/json'
    )

class TestUserCart(BaseTestCase):
    def test_add_item_to_cart(self):
        """ Test for adding items to cart """
        data = create_test_item_1()
        # print(data)
        item1_id = data[0]['public_id']
        # print(f"item 1 {item1_id}")
        self.assertTrue(data[0]['status'] == 'success')
        data = create_test_item_2()
        item2_id = data[0]['public_id']
        # print(f"item2 {item2_id}")
        self.assertTrue(data[0]['status'] == 'success')
        with self.client:
            response = register_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            # print(f"user {data['public_id']}")
            cart_route = '/cart/{}/'.format(data['public_id'])
            # print(cart_route)
            response = self.client.get(
                cart_route,
                data=json.dumps(dict(item_id=item1_id)),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            # print(data)
            # print(response)
            
            
            