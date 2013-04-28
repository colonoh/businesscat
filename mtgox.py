import hmac, urllib2, time
from hashlib import sha512
from base64 import b64encode

mtgox_url = 'https://data.mtgox.com/api/2/'

def create_nonce():
    return int(time.time() * 1000000)
    
'''

'''
def generate_request(key, secret, api_request, data):
    auth_code = hmac.new(secret, api_request + chr(0) + data, sha512)
    
    header = {
        'User-Agent': 'businesscat-bot',
        'Rest-Key': key,
        'Rest-Sign': b64encode(str(auth_code.digest())),
    }

    return urllib2.Request(mtgox_url + api_request, data, header)
