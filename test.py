from mtgox import create_nonce, send_request

output = send_request('BTCUSD/MONEY/TICKER_FAST', 'nonce=' + str(create_nonce()))

print(output)
