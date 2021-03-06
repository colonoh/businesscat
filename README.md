businesscat
===========

Mtgox trade bot

## To run

Create a file named key.py with your key and secret inside:

    key = 'XXX'
    secret = 'XXXXXX'

Then, edit the user parameters in bot.py:

    target_price = 126.381 # USD/BTC
    percent_change = 0.03 # percent change at which to do the opposite action
    action = 'selling' # start with buying
    amount = 1.00 # amount of BTC to play with

Run the script using "python bot.py".  With the parameters above, it will wait until the ask price is 126.381 and then put in a sell order for 1.00 BTC at 126.381 USD/BTC.  Next it will adjust the target price so that it is 97% of 126.381 and switch to "buying" mode.  It then waits 60 seconds and repeats.

## Todo
- [x] add exception handling to mtgox requests
- [ ] consolidate buy/sell code?
- [ ] check to see if previous order fulfilled
- [ ] use floating orders?
- [ ] add trend checking?
- [ ] convert to Python3?

## References
* https://github.com/perol/funny-bot-bitcoin
* https://bitbucket.org/nitrous/mtgox-api/
