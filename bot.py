'''Trading bot which buys low and sells high'''

import time

import mtgox

target_price = 126.381 # USD/BTC
percent_change = 0.03 # percent change at which to do the opposite action
action = 'Selling' # start with buying
amount = 1.00 # amount of BTC to play with

USD = 1e5 # conversion factor for USD
BTC = 1e8 # conversion factor for BTC

# convert all numbers so they are mtgox friendly
target_price = target_price*USD
amount = amount*BTC


def now():
    '''Returns the time in a nice format'''
    return '[' + time.strftime('%I:%M:%S %p') + ']'


# buy low, sell high
while(True):
    ## check the trend and adjust the target value accordingly
    buy_price, sell_price = mtgox.get_prices()
    # if below the adjusted target value, buy
    if action == 'Buying' and sell_price <= target_price:
        print(now(), action, amount/BTC, 'at', target_price/USD)
        order_id = mtgox.order('bid', amount, target_price)
        action = 'Selling'
        target_price = target_price*(1 + percent_change)
    # if above the adjusted target value, sell
    elif action == 'Selling' and buy_price >= target_price:
        print(now(), action, amount/BTC, 'at', target_price/USD)
        order_id = mtgox.order('ask', amount, target_price)
        action = 'Buying'
        target_price = target_price*(1 - percent_change)
    
    print(now(), 'Bid:', buy_price/USD, 'Ask:', sell_price/USD, action, 'at', target_price/BTC)
    time.sleep(60)
