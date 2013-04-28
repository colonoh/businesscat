from mtgox import send_request
import urllib, pprint

# get the current buy and sell prices
output = send_request('BTCUSD/MONEY/TICKER_FAST')
#pprint.pprint(output)
print('Last buy:', int(output['data']['buy']['value_int']))
print('Last sell:', int(output['data']['sell']['value_int']))


# place an order
method_args = {'type': 'bid', 'price_int': 1*1e5, 'amount_int': .01*1e8}
output = send_request('BTCUSD/MONEY/ORDER/ADD', method_args)
order_id = str(output['data'])
print('Order id:', order_id)

# cancel that last order!
method_args = {'oid': order_id} 
output = send_request('BTCUSD/MONEY/ORDER/CANCEL', method_args)
pprint.pprint(output)
