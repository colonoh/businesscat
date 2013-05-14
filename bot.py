'''Trading bot which buys low and sells high'''

import time

import mtgox

target_price = 126.381 # USD/BTC
percent_change = 0.03 # percent change at which to do the opposite action
action = 'selling' # start with buying
amount = 1.00 # amount of BTC to play with

USD = 1e5 # conversion factor for USD
BTC = 1e8 # conversion factor for BTC

# convert all numbers so they are mtgox friendly
target_price = target_price*USD
amount = amount*BTC


def now():
    '''Returns the time in a nice format'''
    return time.strftime('%I:%M:%S %p')


# buy low, sell high
while(True):
    ## check the trend and adjust the target value accordingly
    buy_price, sell_price = mtgox.get_prices()
    # if below the adjusted target value, buy
    if action == 'buying' and sell_price <= target_price:
        print('[{0}] Buying {1} BTC at {2} USD/BTC'.format(now(), amount/BTC, target_price/USD))
        order_id = mtgox.order('bid', amount, target_price)
        action = 'selling'
        target_price = target_price*(1 + percent_change)
    # if above the adjusted target value, sell
    elif action == 'selling' and buy_price >= target_price:
        print('[{0}] Selling {1} BTC at {2} USD/BTC'.format(now(), amount/BTC, target_price/USD))
        order_id = mtgox.order('ask', amount, target_price)
        action = 'buying'
        target_price = target_price*(1 - percent_change)
    
    print('[{0}] Bid: {1} Ask: {2} Target: {3} Amount: {4} {5}'.format(now(), buy_price/USD, sell_price/USD, target_price/USD, amount/BTC, action))
    time.sleep(60)
