import requests
import base64
import hmac
import hashlib
import urllib
import json
import time

URL_EXTENSION = "/v1/book/"

def getOrderBook(base_url, currency_pair):

    url = base_url + URL_EXTENSION + currency_pair
    request_headers = {}

    response = requests.get(url,
                        headers=request_headers,
                        timeout=10,
                        verify=False)
    return (response)
    #print (response.content)
    #assert response.status_code == 200

