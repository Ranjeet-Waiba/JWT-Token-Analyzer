import jwt

# 1. Define your data payload and secret key
payload_data = {
    "sub": "1234567890",
    "name": "Sunny Thakuri",
    "admin": True
}
secret_key = "your_secret_key"

# 2. Encode the payload to get your token string
# By default, PyJWT uses the HS256 algorithm
token = jwt.encode(payload_data, secret_key, algorithm="HS256")

print(token)