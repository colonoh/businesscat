'''
buy low, sell high
'''
import mtgox
import time

target_price = '135' # USD/BTC
buying = True # start with buying

# every X minutes...
while(True):
    ## check the trend and adjust the target value accordingly
    buy_price, sell_price = mtgox.get_prices()
    
    # if below the adjusted target value, buy
    if buying and current_price() =< target_price:
        order_id = mtgox.order('bid', amount, target_price)
        # pick new target and switch to selling
        buying = False
        
    # if above the dajusted target value, sell
    elif not buying and current_price() >= target_price:
        order_id = mtgox.order('ask', amount, target_price)
        # pick new target and switch to buying
        buying = True
    
    # if neither, do nothing?
    
    time.sleep(60) # in any case, sleep for X minutes


