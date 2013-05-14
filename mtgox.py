'''Interface to MtGox'''
import hmac, urllib, urllib2, hashlib, base64, json, time

import key
    
# Send a request like "BTCUSD/money/ticker" to the server and return the output in JSON format
def _send_request(api_method, method_args={}):
    '''Sends a request to MtGox and returns the full output'''
    tries_left = 9    
    while tries_left > 0:
        try:
            # add the nonce and then create a percent encoded string
            method_args['nonce'] = int(time.time() * 1000000)
            method_args_url = urllib.urlencode(method_args.items())
            
            auth_code = hmac.new(base64.b64decode(key.secret), api_method + chr(0) + method_args_url, hashlib.sha512)
            header = {
                'User-Agent': 'businesscat-bot',
                'Rest-Key': key.key,
                'Rest-Sign': base64.b64encode(str(auth_code.digest())),
            }
            
            request = urllib2.Request('https://data.mtgox.com/api/2/' + api_method, method_args_url, header)
            response = urllib2.urlopen(request, method_args)
            return json.load(response)
    
        # catch things like HTTP Error 502: Bad Gateway
        except urllib2.HTTPError as e: 
            output = json.load(e)
            print('HTTPError:', output['error'])
            tries_left -= 1
            time.sleep(60)


def get_prices():
    '''return the latest bid and ask prices'''
    output = _send_request('BTCUSD/MONEY/TICKER_FAST')    
    return int(output['data']['buy']['value_int']), int(output['data']['sell']['value_int'])


def order(order_type, amount, price=None):
    '''send in an order and return the order ID'''
    args = {'amount_int': amount, 'type': order_type}
    
    # if there is a specified price, use it, otherwise it's a market order
    if price != None:
        args['price_int'] = price
    
    output = _send_request('BTCUSD/MONEY/ORDER/ADD', args)
    return str(output['data'])


def cancel(order_id):
    '''takes an order ID and requests that it be canceled'''
    return _send_request('BTCUSD/MONEY/ORDER/CANCEL', {'oid': order_id})
