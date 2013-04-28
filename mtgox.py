import time
import hmac, base64, hashlib, urllib2

base = 'https://data.mtgox.com/api/2/'

def create_nonce():
    return int(time.time() * 1000000)

def makereq(key, secret, path, data):
    hash_data = path + chr(0) + data
    secret2 = base64.b64decode(secret)
    sha512 = hashlib.sha512
    hmac2 = str(hmac.new(secret2, hash_data, sha512).digest())

    header = {
        'User-Agent': 'My-First-Trade-Bot',
        'Rest-Key': key,
        'Rest-Sign': base64.b64encode(hmac2),
#        'Accept-encoding': 'GZIP',
    }
    
    
    print(base+path)
    print(data)
    print(header)
    
    print(base64.b64encode(str(hmac.new(base64.b64decode(secret), path + chr(0) + data, hashlib.sha512).digest())))
    return urllib2.Request(base + path, data, header)
