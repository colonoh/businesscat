'''
buy low, sell high
'''
import mtgox
import time

target_price = '135' # USD/BTC
percent_change = 0.03
buying = True # start with buying
USD = 1e8 # conversion factor for USD
BTC = 1e5 # conversion factor for BTC

# every X minutes...
while(True):
    ## check the trend and adjust the target value accordingly
    buy_price, sell_price = mtgox.get_prices()
    print(time.strftime(%I:%M:%S %p), 'Bid:', buy_price/USD, 'Ask:', sell_price/USD, 'Buying:', buying, 'Target:', target_price/USD)
    
    # if below the adjusted target value, buy
    if buying and sell_price =< target_price:
        print(time.strftime(%I:%M:%S %p), 'Buying at', target_price/USD)
        order_id = mtgox.order('bid', amount, target_price)
        # pick new target and switch to selling
        buying = False
        target_price = target_price*(1+percent_change)
        
    # if above the dajusted target value, sell
    elif not buying and buy_price >= target_price:
        order_id = mtgox.order('ask', amount, target_price)
        print(time.strftime(%I:%M:%S %p), 'Selling at', target_price/USD)
        # pick new target and switch to buying
        buying = True
        target_price = target_price*(1-percent_change)
    
    # if neither, do nothing?
    
    time.sleep(60) # in any case, sleep for X minutes


