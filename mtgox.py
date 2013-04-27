import hmac, base64, hashlib, urllib2
base = 'https://data.mtgox.com/api/2/'

def makereq(key, secret, path, data):
    hash_data = path + chr(0) + data
    secret = base64.b64decode(secret)
    sha512 = hashlib.sha512
    hmac = str(hmac.new(secret, hash_data, sha512))

    header = {
        'User-Agent': 'My-First-Trade-Bot',
        'Rest-Key': key,
        'Rest-Sign': base64.b64encode(hmac),
        'Accept-encoding': 'GZIP',
    }

    return urllib2.Request(base + path, data, header)
