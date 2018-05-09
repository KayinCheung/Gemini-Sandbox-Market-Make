# Gemini Sandbox Market Make

## Getting started
1) Create an account at Gemini's sandbox exchange: https://exchange.sandbox.gemini.com/
2) Generate an API Key. Tick "trading" at API trading key settings during creation.
3) Open Constants.py file, on line 13 and 14, change GEMINI_API_KEY and GEMINI_API_SECRET to the keys you generated.
4) Run Gemini.py. It will market make according to below algorithm.

## Market making algorithm. Runs once every 5 seconds.
 1) Pulls ETHUSD orderbook data from live Gemini exchange. Start timer.
 2) Iterate through the ask order book TILL 1 ETH sell volume is accumulated.
 3) If 1 ETH sell volume is accumulated before the 3rd row, set our ask prices to equal the 3rd row.
 4) Repeat the same for bid data.
 5) Market make on Gemini sandbox site, setting our market making bid and ask equal to the output values from step 3 and 4 using limit orders.
 6) Once timer reaches 5 seconds, cancel all open orders. Go back to step 1.


## Adjustable variables
- The market making bid/ask can be offset by 0.5% (or any % number) for higher margin/probability and lower trade frequency
- Amount of order book volume to accumulate can be increased. 
- Volume of crypto to market make can be adjusted using live order book data (Currently set at 0.1 Eth)
