Installing
--------------------

Install with pip:

$ pip install PyJWT

Usage
-------------------

>>> import jwt
>>> encoded = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
>>> print(encoded)
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlN1bm55IFRoYWt1cmkiLCJhZG1pbiI6dHJ1ZX0.A0NKyOGWxLVuBKjcWuyPZiT7QGzRbHNKK2x-PJ0T4rE
>>> jwt.decode(encoded, "secret", algorithms=["HS256"])
{'some': 'payload'}

Documentation
---------------------------------

View the full docs online at https://pyjwt.readthedocs.io/en/stable/