from mtgox import *
from key import *
import urllib2
import json

# get ticker data
data = 'nonce=' + str(create_nonce())  
request = makereq(key, secret, 'BTCUSD/money/info', data) # create the request
response = urllib2.urlopen(request, data)

print(json.load(response)) # convert from readable format


