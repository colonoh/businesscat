import time

def create_nonce():
    return int(time.time() * 1000000)
