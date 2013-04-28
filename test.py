from mtgox import create_nonce, send_request

data = 'nonce=' + str(create_nonce())  
api_method = 'BTCUSD/money/ticker_fast'

output = send_request(api_method, data)

print(output)
