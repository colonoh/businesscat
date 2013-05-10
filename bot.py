'''
buy low, sell high
'''
import mtgox
import time

USD = 1e8 # conversion factor for USD
BTC = 1e5 # conversion factor for BTC

# ==================================================================
# ==EDIT THESE BELOW================================================
# ==================================================================
target_price = 126.381 # USD/BTC
percent_change = 0.03 # percent change at which to do the opposite action
action = 'buying' # start with buying
amount = 0.01 # amount of BTC to play with
# ==================================================================

# all numbers are mtgox friendly
target_price = target_price*USD
amount = amount*BTC

# return the current time nicely formatted
def now():
    return time.strftime(%I:%M:%S %p)

# every X minutes...
while(True):
    ## check the trend and adjust the target value accordingly
    buy_price, sell_price = mtgox.get_prices()
    print '[{}]    Bid: {} $/BTC    Ask: {} $/BTC    Target: {} $/USD    Currently {}'.format(now(), buy_price/USD, sell_price/USD, target_price/USD, action)
    
    # if below the adjusted target value, buy
    if action == 'buying' and sell_price =< target_price:
        print '[{}]    Buying {} BTC at {} $/BTC'.format(now(), amount/BTC, target_price/USD)
        order_id = mtgox.order('bid', amount, target_price)
        # pick new target and switch to selling
        action = 'selling'
        target_price = target_price*(1 + percent_change)
        
    # if above the adjusted target value, sell
    elif action == 'selling' and buy_price >= target_price:
        print '[{}]    Selling {} BTC at {} $/BTC'.format(now(), amount/BTC, target_price/USD)
        order_id = mtgox.order('ask', amount, target_price)
        # pick new target and switch to buying
        action = 'buying'
        target_price = target_price*(1 - percent_change)
    
    time.sleep(60) # in any case, sleep for X minutes
