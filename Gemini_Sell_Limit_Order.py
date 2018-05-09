import requests
import base64
import hmac
import hashlib
import urllib
import json
import time

URL_EXTENSION = "/v1/order/new"

def sellLimitOrder(base_url,gemini_api_key,gemini_api_secret,sell_price,quantity,currency_pair):

    url = base_url + URL_EXTENSION
    payload =  {
        "request": URL_EXTENSION,
        "nonce": time.time(),
        "client_order_id": 'SELL_' + str(time.time()),
        "symbol": currency_pair,
        "amount": quantity,
        "price": sell_price,
        "side": "sell",
        "type": "exchange limit"
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
