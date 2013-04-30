'''
buy low, sell high
'''
from mtgox import send_request
import time

target_price = '135' # USD/BTC
buying = True # start with buying

# every X minutes...
while(True):
    ## check the trend and adjust the target value accordingly
    
    # if below the adjusted target value, buy
    if buying and current_price() < target_price:
        buy()
        # pick new target and switch to selling
        buying = False
        
    # if above the dajusted target value, sell
    elif not buying and current_price() > target_price:
        sell()
        # pick new target and switch to buying
        buying = True
    
    # if neither, do nothing?
    
    time.sleep(60) # in any case, sleep for X minutes


