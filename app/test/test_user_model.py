import unittest
import datetime
import uuid

from app.main import db
from app.main.model.user import User
from app.test.base import BaseTestCase

from app.main.service.user_service import *

class TestUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        print("about to make a user")
        public = str(uuid.uuid4())
        print(public)
        user = create_user(
            public_id=public,
            email='test@test.com',
            password='test',
            registered_on=datetime.datetime.utcnow(),
        )
        print(user)
        print(user.cart)
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        # print(auth_token)
        self.assertTrue(isinstance(auth_token, bytes))

    # def test_decode_auth_token(self):
    #     user = User(
    #         email='test@test.com',
    #         password='test',
    #         registered_on=datetime.datetime.utcnow()
    #     )
    #     db.session.add(user)
    #     db.session.commit()
    #     auth_token = user.encode_auth_token(user.id)
    #     # print(auth_token)
    #     self.assertTrue(isinstance(auth_token, bytes))
    #     self.assertTrue(User.decode_auth_token(auth_token.decode("utf-8") ) == 1)


if __name__ == '__main__':
    unittest.main()