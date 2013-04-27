import hmac, base64, hashlib, urllib.request
import time

base = 'https://data.mtgox.com/api/2/'

def create_nonce():
    return int(time.time() * 1000000)

def makereq(key, secret, path, data):
    hash_data = (path + chr(0) + data).encode() # turn it a byte representation instead of string
    secret = base64.b64decode(secret.encode())
    sha512 = hashlib.sha512
    hmac = str(hmac.new(secret, hash_data, sha512))

    header = {
        'User-Agent': 'businesscat-bot',
        'Rest-Key': key,
        'Rest-Sign': base64.b64encode(hmac),
        'Accept-encoding': 'GZIP',
    }

    return urllib.request.Request(base + path, data, header)