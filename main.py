import requests
import pandas as pd
import numpy as np

coinDCX_secret_key="b50a2baa78a4a6c10d3c2e7d2d26a6572b2725c66a4c77e2b61416d40a0ef6f2"
coinDCX_api_key="8eefcaa936b691876a6b4961690c321daefac3a7f547361a"

baseURL_API = "https://api.coindcx.com/"
baseURL_Public = "https://public.coindcx.com"  

def get_ticker(): 
    ticker = requests.get(baseURL_API + "exchange/ticker")
    return ticker.json()


def get_market_details(): 
    market_details = requests.get(baseURL_Public + "exchange/v1/markets_details")
    return market_details.json()


def get_orderbook(pair): 
    ob = requests.get(baseURL_Public + "market_data/orderbook?pair=" + pair)
    return ob.json()

