from mtgox import send_request
import urllib


#method_args = {} # data dictionary used to add
#method_args['type'] = 'bid'
#method_args['amount'] = '1e8'

# place an order
#method_args = {'type': 'bid', 'price_int': 1*1e5, 'amount_int': .01*1e8}
#output = send_request('BTCUSD/MONEY/ORDER/ADD', method_args)

# cancel an order
method_args = {'oid': '0a2b3850-f2d5-42a4-bb5e-eead0c707fb4'} 
output = send_request('BTCUSD/MONEY/ORDER/CANCEL', method_args)


import pprint
pprint.pprint(output)
#print('Last buy:', int(output['data']['buy']['value_int']))
#print('Last sell:', int(output['data']['sell']['value_int']))
