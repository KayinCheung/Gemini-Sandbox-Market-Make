# Gemini Sandbox Market Make

These are python scripts for market making on Gemini's exchange. Built on Python 3.6.4.

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


## Suggestions to customize algorithm

- The market making bid/ask can be offset by 0.5% (or any % number) for higher margin/probability and lower trade frequency
- Amount of order book volume to accumulate can be increased. 
- Volume of crypto to market make can be adjusted using live order book data (Currently set at 0.1 Eth).
- The algorithm can pull orderbook data from multiple exchanges, not just Gemini's live site.

## Further development

- Implement best price execution by supporting multiple exchanges, and executing orders the exchange with best rates
- Implementing time-weighted average order execution
- Combine time-weighted average order and best price execution. Eg: Spreading a $10 million BTC sell order across 30 minutes, executing an equal portion every 10 seconds on the exchange with best rates.
