# generates password from secret and url

import hmac
import base64
import hashlib

# Fix Python 2.x
try: input = raw_input
except NameError: pass

secret = input('Input keyword:\n')
url = input('Input site url:\nWarning! Different url forms will return different passwords. Use only one form (like domain.com or http://www.domain.com/):\n')
print(base64.b64encode(hmac.new(secret.encode('utf-8'), url.encode('utf-8'), hashlib.sha1).digest()).decode('utf-8'))
