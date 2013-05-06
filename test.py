import mtgox 
import urllib, pprint

# get the current buy and sell prices
output = mtgox.send_request('BTCUSD/MONEY/TICKER_FAST')
#pprint.pprint(output)
print('Last buy:', int(output['data']['buy']['value_int']))
print('Last sell:', int(output['data']['sell']['value_int']))


# place an order
order_id = mtgox.order('buy', .01*1e8, 1*1e5)
print('Order id:', order_id)

# cancel that last order!
method_args = {'oid': order_id} 
output = mtgox.send_request('BTCUSD/MONEY/ORDER/CANCEL', method_args)
pprint.pprint(output)
