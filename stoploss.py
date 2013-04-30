'''
sell  if falling, buy lower
'''
from mtgox import send_request
import time

stoploss_percentage = '0.05'
buy_percentage = '0.05'
selling = True
falling = False

# every X minutes...
while(True):
    # check the current price
    # check to se if price is falling
    
    # if falling quickly and a certain amount, sell
    if selling and falling and current_price() < last_price * (1-stoploss_percentage):
        sell()
        selling = False
        # special code to handle buying after a crash
       
    # if not stop-selling, have a floating buy order X% under the current price
    # BUT we want to catch the immediate drop too! not just buy in at the top on the way down
    if not selling:
        # see if buy orders exists
        
        # cancel last buy order and put new buy order in at correct price, if needed
        cancel()
        place_buy()
    
    #
    if selling:
        time.sleep(20)
    else:
        time.sleep(120)
