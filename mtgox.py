import time
import hmac, base64, hashlib, urllib2

mtgox_url = 'https://data.mtgox.com/api/2/'

def create_nonce():
    return int(time.time() * 1000000)

def makereq(key, secret, api_request, data):
    hash_data = api_request + chr(0) + data
    secret2 = base64.b64decode(secret)
    sha512 = hashlib.sha512
    hmac2 = str(hmac.new(secret2, hash_data, hashlib.sha512).digest())

    header = {
        'User-Agent': 'My-First-Trade-Bot',
        'Rest-Key': key,
        'Rest-Sign': base64.b64encode(hmac2),
    }

    return urllib2.Request(mtgox_url + api_request, data, header)
