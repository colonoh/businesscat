import hmac, urllib, urllib2, hashlib, base64, json, sys, time
from key import key, secret
    
# Send a request like "BTCUSD/money/ticker" to the server and return the output in JSON format
def _send_request(api_method, method_args={}):
    method_args['nonce'] = int(time.time() * 1000000) # add the nonce to the list of arguments
    method_args = urllib.urlencode(method_args.items()) # convert from a dictionary to a "percent-encoded" string
    
    auth_code = hmac.new(base64.b64decode(secret), api_method + chr(0) + method_args, hashlib.sha512)
    header = {
        'User-Agent': 'businesscat-bot',
        'Rest-Key': key,
        'Rest-Sign': base64.b64encode(str(auth_code.digest())),
    }

    # form and send the request
    request = urllib2.Request('https://data.mtgox.com/api/2/' + api_method, method_args, header)
    response = urllib2.urlopen(request, method_args)
    output = json.load(response) # decode the request
        
    # if MtGox returns and says it is unsuccessful, print raw output and abort
    if output['result'] == 'success':
        return output
    else:
        pprint.pprint(output)
        sys.exit('Error: MtGox request was unsuccessful.')


# get current prices for buy and sell orders
def get_prices():
    output = _send_request('BTCUSD/MONEY/TICKER_FAST')    
    return int(output['data']['buy']['value_int']), int(output['data']['sell']['value_int'])


# buy (or sell) some bitcoins, returns the order ID
def order(order_type, amount, price = None):
    args = {'amount_int': amount, 'type': order_type}
    
    # if there is no price argument, place a market order
    if price != None:
        args['price_int'] = price
    
    output = _send_request('BTCUSD/MONEY/ORDER/ADD', args)
    return str(output['data']) # return the order ID


def cancel(order_id):
    return _send_request('BTCUSD/MONEY/ORDER/CANCEL', {'oid': order_id})
