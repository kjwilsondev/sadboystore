# Controller

## Resources

[User Controller](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/ "Free Code Camp")

[Token Based Auth](https://www.youtube.com/watch?v=xF30i_A6cRw "Pretty Printed")

## Terminology

- **api.route:**
  A decorator to route resources

- **api.marshal_with:**
  A decorator specifying the fields to use for serialization (Dto)

- **api.marshal_list_with:**
  A shortcut decorator for marshal_with above withas_list = True

- **api.doc:**
  A decorator to add some api documentation to the decorated object

- **api.response:**
  A decorator to specify one of the expected responses

- **api.expect:**
  A decorator to Specify the expected input model (Dto)

- **api.param:**
  A decorator to specify one of the expected parameters

## Draft Auth Function

```python
# TODO: Require Token Function
# f = function being decorated

def token_required(f):
    @wraps(f)
    # Positional args then key word args
    def decorated(*args, **kwargs):
        token = None
        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']
        if not token:
            return {'message' : 'Token is missing'}
        if token != 'mytoken':
            return {'message' : 'Invalid token'}
        print('TOKEN: {}'.format(token))
        return f(*args, **kwargs)
    return decorated

@api.doc('list_of_registered_users', security='apiKey')
@token_required
```
