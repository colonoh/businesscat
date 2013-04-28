from mtgox import *
from key import *
import urllib

import json


#post_data = 'nonce=' + str(create_nonce())
#post_data = urllib.urlencode(urllib.urlencode)
inp = {}
inp['nonce'] = str(int(time.time() * 1e6))
print(inp)
post_data = urllib.urlencode(inp.items())
request = makereq(key, secret, 'BTCUSD/money/ticker', post_data)
print('Request done.')
output = json.load(response)
print(output)
