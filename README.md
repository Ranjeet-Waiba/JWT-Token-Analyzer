Installing
Install with pip:

$ pip install PyJWT

Usage
>>> import jwt
>>> encoded = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
>>> print(encoded)
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg
>>> jwt.decode(encoded, "secret", algorithms=["HS256"])
{'some': 'payload'}

Documentation
View the full docs online at https://pyjwt.readthedocs.io/en/stable/

