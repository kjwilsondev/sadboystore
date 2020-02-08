# Routes

## User Methods

---

## /user/

**GET** /user/

returns list of users
in order of when they registered

**POST** /user/

creates new user
returns response_object, 201

```python
response_object = {
    'status': 'success',
    'message': 'Successfully registered.',
    'authorization': auth_token.decode(),
    'public_id': user.public_id,
    'cart': user.cart_items
}
```

## /user/public_id

**GET** /user/public_id

returns user

## Cart Methods

---

## /user/carts

**GET** /user/carts

returns all carts

**POST** /user/carts

no post method for carts
carts are instantiated with create_user

## /user/public_id/cart

currently returns cart
should return cart.items
