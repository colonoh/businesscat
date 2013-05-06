import mtgox 
import urllib, pprint

# get the current buy and sell prices
buy_price, sell_price = mtgox.get_prices()
print('Last buy:', buy_price, 'Last sell:', sell_price)

# place an order
order_id = mtgox.order('buy', .01*1e8, 1*1e5)
print('Order id:', order_id)

# cancel that last order!
method_args = {'oid': order_id} 
output = mtgox.send_request('BTCUSD/MONEY/ORDER/CANCEL', method_args)
pprint.pprint(output)
