import hmac, urllib, urllib2, hashlib, base64, json, sys, time
from key import key, secret
    
# Send a request like "BTCUSD/money/ticker" to the server and return the output in JSON format
def send_request(api_method, method_args={}):
    method_args['nonce'] = int(time.time() * 1000000) # add the nonce to the list of arguments
    method_args = urllib.urlencode(method_args.items()) # convert from a dictionary to a "percent-encoded" string
    
    auth_code = hmac.new(base64.b64decode(secret), api_method + chr(0) + method_args, hashlib.sha512)
    header = {
        'User-Agent': 'businesscat-bot',
        'Rest-Key': key,
        'Rest-Sign': base64.b64encode(str(auth_code.digest())),
    }

    try:
        request = urllib2.Request('https://data.mtgox.com/api/2/' + api_method, method_args, header) # create the request
        response = urllib2.urlopen(request, method_args) # send the request
        if response.getcode() == 200: # OK
            output = json.load(response) # decode the request
            
            # if MtGox returns and says it is unsuccessful, print raw output and abort
            if output['result'] == 'success':
                return output
            else:
                pprint.pprint(output)
                sys.exit('MtGox respons result was NOT \'success\'...aborting.')
    except Exception as err:
        sys.exit('Request to MtGox failed: %s' % err)
