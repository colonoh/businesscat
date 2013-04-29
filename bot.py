'''
buy low, sell high
'''
from mtgox import send_request
import time

initial_target = '135' # USD/BTC

buying = True # start with buying

# every X minutes...
    
    ## check the trend and adjust the target value accordingly
    
    # if below the adjusted target value, buy
    if buying and current_price < buy_price:
        buy()
        # pick new target and switch to selling
        
    # if above the dajusted target value, sell
    elif not buying and current_price > sell_price:
        sell()
        # pick new target and switch to buying
    
    # if neither, do nothing?
    
    time.sleep(60) # in any case, sleep for X minutes


