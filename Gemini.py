import requests
import base64
import hmac
import hashlib
import urllib
import json
import time

import Constants

from pprint import pprint
from Gemini_Heartbeat import heartbeat
from Gemini_Buy_Limit_Order import buyLimitOrder
from Gemini_Sell_Limit_Order import sellLimitOrder
from Gemini_Retrieve_Open_Orders import getOpenOrders
from Gemini_Cancel_All_Orders import cancelAllOrders
from Gemini_Retrieve_Order_Book import getOrderBook
from Class_Order_Book import OrderBook
from Gemini_Get_Balance import GeminiGetBtcBalance, GeminiGetEthBalance, GeminiGetUsdBalance

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


def GeminiGetOpenOrders():
    output = getOpenOrders(BASE_URL,GEMINI_API_KEY,GEMINI_API_SECRET)

    if output.status_code == 200:
        print ('Retrieve OK')
        print (output.content)

    else:
        print ('Get Open Orders error code ' + str(output.status_code))
        print (output.content)

def GeminiHeartbeat():
    output = heartbeat(BASE_URL,GEMINI_API_KEY,GEMINI_API_SECRET)

    if output.status_code == 200:
        print ('Heartbeat OK')

    else:
        print ('Heartbeat error code ' + str(output.status_code))
        print (output.content)


def GeminiPlaceBuyOrder(buyprice, quantity):

    output = buyLimitOrder(BASE_URL,GEMINI_API_KEY,GEMINI_API_SECRET,buyprice,quantity,CURRENCY_PAIR)
    if output.status_code == 200:
        print ('Buy Limit OK')
        print (output.content)
    else:
        print ('Buy Limit error code ' + str(output.status_code))
        print (output.content)

def GeminiPlaceSellOrder(sellprice,quantity):

    output = sellLimitOrder(BASE_URL,GEMINI_API_KEY,GEMINI_API_SECRET,sellprice,quantity,CURRENCY_PAIR)
    if output.status_code == 200:
        print ('Sell Limit OK')
        print (output.content)
    else:
        print ('Sell Limit error code ' + str(output.status_code))
        print (output.content)

def GeminiCancelOrders():
    output = cancelAllOrders(BASE_URL,GEMINI_API_KEY,GEMINI_API_SECRET)

    if output.status_code == 200:
        print ('Cancel Orders OK')

    else:
        print ('Cancel Orders error code ' + str(output.status_code))
        print (output.content)

def GeminiGetOrderBook():
    output = getOrderBook(LIVE_URL,CURRENCY_PAIR)

    if output.status_code == 200:
        print ('Get order book OK')
        return (output)
        

    else:
        print ('Get order book error code ' + str(output.status_code))
        return (output)




def GeminiGetLimitPriceData():
    output = GeminiGetOrderBook()
    if output.status_code != 200:
        #Cancel all orders 
        pass
    decoded_output = "[" + output.content.decode("utf-8") + "]"
    data = json.loads(decoded_output)[0]
    orderbook = OrderBook(data)

    ''' List of orderbook class variables
        self.BUY_total_vol = 0
        self.SELL_total_vol = 0
        self.buy_rows_checked = 0
        self.sell_rows_checked = 0
        self.buy_vol_at_limit = 0
        self.sell_vol_at_limit = 0
    '''
    return (orderbook)
    '''print ('Buy Limit Price: ' + str(orderbook.buy_limit_price))
    print ('Buy Vol at Limit: ' + str(orderbook.buy_vol_at_limit))
    print ('Total buy vol: ' + str(orderbook.BUY_total_vol) + ' BTC at row ' + str(orderbook.buy_rows_checked))

    print ('Sell Limit Price: ' + str(orderbook.sell_limit_price))
    print ('Sell Vol at Limit: ' + str(orderbook.sell_vol_at_limit))
    print ('Total sell vol: ' + str(orderbook.SELL_total_vol) + ' BTC at row ' + str(orderbook.sell_rows_checked))'''
    
def GeminiMarketMake():
    
    time.sleep(time.time() % 5)

    while True:

        price_data = GeminiGetLimitPriceData()
        GeminiPlaceBuyOrder(price_data.buy_limit_price, 0.1)
        GeminiPlaceSellOrder(price_data.sell_limit_price, 0.1)
        print ('Buy Limit: ' + str(price_data.buy_limit_price))
        print ('Sell Limit: ' + str(price_data.sell_limit_price))
        time.sleep(time.time() % 5)
        GeminiCancelOrders()

    ''' List of orderbook class variables
        self.BUY_total_vol = 0
        self.SELL_total_vol = 0
        self.buy_rows_checked = 0
        self.sell_rows_checked = 0
        self.buy_vol_at_limit = 0
        self.sell_vol_at_limit = 0
    '''
# Market making algorithm. Runs once every 5 seconds.
# 1) Pulls ETHUSD orderbook data from live Gemini exchange. Start timer.
# 2) Iterate through the ask order book TILL 1 ETH sell volume is accumulated.
# 3) If 1 ETH sell volume is accumulated before the 3rd row, set our ask prices to equal the 3rd row.
# 4) Repeat the same for bid data.
# 5) Market make on Gemini sandbox site, setting our market making bid and ask equal to the output values from step 3 and 4 using limit orders.
# 6) Once timer reaches 5 seconds, cancel all open orders. Go back to step 1.

GeminiMarketMake()
# Adjustable variables
# The market making bid/ask can be offset by 0.5% (or any % number) for higher margin/probability and lower trade frequency
# Amount of order book volume to accumulate can be increased. 
# Volume of crypto to market make can be adjusted using live order book data (Currently set at 0.1 Eth)

'''total_fees = 1.25/100

now=time.gmtime()
time.sleep(5 - now.tm_sec%5)
while (True):
    now=time.gmtime()
    print(str(now.tm_hour) + ':' + str(now.tm_min) + ':' + str(now.tm_sec))

    price = GeminiGetLimitPriceData()
    print ("bid = " + str(price.buy_limit_price))
    print ("ask = " + str(price.sell_limit_price))

    print ("Mkt make bid = " + str(price.buy_limit_price*0.9865*0.99))
    print ("Mkt make ask = " + str(price.sell_limit_price*1.0135*1.01))


    print ("No profit cut_off BID = " + str(price.buy_limit_price*0.9865))
    print ("No profit cut_off ASK = " + str(price.sell_limit_price*1.0135))
    time.sleep(5 - time.gmtime().tm_sec%5)
'''
