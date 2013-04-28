import time
import hmac, urllib2, hashlib, base64, json
from key import key, secret

mtgox_url = 'https://data.mtgox.com/api/2/'
secret = base64.b64decode(secret)

def create_nonce():
    return int(time.time() * 1000000)
    
'''
Send an api request like "BTCUSD/money/ticker" to the server and return the output in JSON format
'''
def send_request(api_method, data):
    auth_code = hmac.new(secret, api_method + chr(0) + data, hashlib.sha512).digest()
    header = {
        'User-Agent': 'businesscat-bot',
        'Rest-Key': key,
        'Rest-Sign': base64.b64encode(str(auth_code)),
    }

    request = urllib2.Request(mtgox_url + api_method, data, header)
    response = urllib2.urlopen(request, data)

    return json.load(response) # return server output in JSON format
