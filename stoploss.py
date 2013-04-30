'''
sell  if falling, buy lower
'''
from mtgox import send_request
import time

stoploss_percentage = 0.10
#buy_percentage = 0.05
high_price = 150

# every X minutes...
while(True):
    # check the current price, set high price if needed
    buy_price, sell_price = mtgox.get_price()
    high_price = max(buy_price, high_price)
    
    # check to se if price is falling
    
    # if under a certain amount, sell
    if buy_price < high_price * (1 - stoploss_percentage):
        mtgox.sell()
        # special code to handle buying after a crash
       
    # if not stop-selling, have a floating buy order X% under the current price
    # BUT we want to catch the immediate drop too! not just buy in at the top on the way down
    #if not selling:
        # see if buy orders exists
        
        # cancel last buy order and put new buy order in at correct price, if needed
        # new buy should be at least X% under high_price!
        #if:
            #cancel()
            #place_buy()
    
    #
    if selling:
        time.sleep(20)
    else:
        time.sleep(120)
