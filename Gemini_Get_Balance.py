import requests
import base64
import hmac
import hashlib
import urllib
import json
import time

import Constants

URL_EXTENSION = "/v1/balances"

#Currency names
BTC = Constants.BTC
ETH = Constants.ETH
USD = Constants.USD

#Universal constants
BTC_REQUIRED_VOL = Constants.BTC_REQUIRED_VOL
CURRENCY_PAIR = Constants.CURRENCY_PAIR
MINIMUM_ROWS_TO_CHECK = Constants.MINIMUM_ROWS_TO_CHECK

#Sandbox Constants
BASE_URL = Constants.BASE_URL
GEMINI_API_KEY = Constants.GEMINI_API_KEY
GEMINI_API_SECRET = Constants.GEMINI_API_SECRET

#Live trading constants
LIVE_URL = Constants.LIVE_URL


def getBalance(base_url,gemini_api_key,gemini_api_secret):

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

    response = requests.post(url, data=None, headers=request_headers, timeout=10, verify=False)
    return (response)
    #print (response.content)
    #assert response.status_code == 200

def GeminiGetBalance(currency):
    output = getBalance(BASE_URL,GEMINI_API_KEY,GEMINI_API_SECRET)
    if output.status_code == 200:
        decoded_output = "[" + output.content.decode("utf-8") + "]"
        data = json.loads(decoded_output)[0]
        print ('Get balance OK')
        for row in data:
            if row["currency"] == currency:
                #print (row["amount"])
                return row["amount"]

    else:
        print ('Get balance error code ' + str(output.status_code))
        print (output.content)

def GeminiGetBtcBalance():
    return GeminiGetBalance(BTC)

def GeminiGetEthBalance():
    return GeminiGetBalance(ETH)

def GeminiGetUsdBalance():
    return GeminiGetBalance(USD)