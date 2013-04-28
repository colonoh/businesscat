import time
import hmac, urllib2, hashlib, base64, json, sys
from key import key, secret

def create_nonce():
    return int(time.time() * 1000000)
    
# Send a request like "BTCUSD/money/ticker" to the server and return the output in JSON format
def send_request(api_method, data):
    auth_code = hmac.new(base64.b64decode(secret), api_method + chr(0) + data, hashlib.sha512)
    header = {
        'User-Agent': 'businesscat-bot',
        'Rest-Key': key,
        'Rest-Sign': base64.b64encode(str(auth_code.digest())),
    }

    try:
        request = urllib2.Request('https://data.mtgox.com/api/2/' + api_method, data, header) # create the request
        response = urllib2.urlopen(request, data) # send the request
        if response.getcode() == 200: # OK
            return json.load(response) # decode the request
    
    except Exception as err:
        sys.exit('Request to MtGox failed: %s' % err)
