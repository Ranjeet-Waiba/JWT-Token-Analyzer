Objective
--------------------------
JWT Token Analyzer is a Python-based web security project that checks whether a JSON Web Token (JWT) is properly secured. It helps security testers understand common JWT weaknesses without needing to manually inspect every token.

What the project does

The tool takes a JWT token as input and performs three main checks:

Decode the JWT

Separates the token into its header and payload.
Displays information such as the signing algorithm, issuer, subject, expiration time, etc.
Uses Python and PyJWT for JWT processing.

Check for alg: none

Tests whether the application accepts a JWT using the insecure none algorithm.
If accepted, the report identifies this as a potential JWT authentication vulnerability.

Test weak secrets

If the token uses a symmetric algorithm such as HS256, the tool can test a small authorized wordlist of common secrets.
If a secret matches, the report shows that the signing secret may be weak.


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

Screenshots of Project
------------------------------

