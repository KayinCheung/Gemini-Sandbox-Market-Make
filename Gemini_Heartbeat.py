import requests
import base64
import hmac
import hashlib
import urllib
import json
import time

URL_EXTENSION = "/v1/heartbeat"

def heartbeat(base_url,gemini_api_key,gemini_api_secret):

    #base_url = 'https://api.sandbox.gemini.com/v1'
    '''response = urllib.request.urlopen(base_url + '/pubticker/btcusd')
    #.hexdigest()
    print(response.read())'''

    url = base_url + URL_EXTENSION

    payload =  {
        "request": URL_EXTENSION,
        "nonce": time.time()
    }
    encoded_payload = json.dumps(payload)
    encoded_payload2 = bytes(encoded_payload , 'utf-8')
    b64 = base64.b64encode(encoded_payload2)
    signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()

    request_headers = {
        'Content-Type': "text/plain",
        'Content-Length': "0",
        'X-GEMINI-APIKEY': gemini_api_key,
        'X-GEMINI-PAYLOAD': b64,
        'X-GEMINI-SIGNATURE': signature,
        'Cache-Control': "no-cache"
        }

    response = requests.post(url, data=None, headers=request_headers, timeout=1, verify=False)
    return (response)
    #print (response.content)
    #assert response.status_code == 200

