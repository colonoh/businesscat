'''
sell  if falling, buy lower
'''
import mtgox
import time

stoploss_percentage = 0.10
high_price = 150

# every X minutes...
while(True):
    # check the current price, set high price if needed
    buy_price, sell_price = mtgox.get_prices()
    high_price = max(sell_price, high_price)
    print('Buy=', buy_price, 'Sell=', sell_price, 'High=', high_price)
    
    # check to se if price is falling
    
    # if under a certain amount, sell
    if sell_price < high_price * (1 - stoploss_percentage):
        mtgox.place_sell()

    time.sleep(20)
