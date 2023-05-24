import requests
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

coinDCX_secret_key = os.getenv("coinDCX_secret_key")
coinDCX_api_key = os.getenv("coinDCX_api_key")

baseURL_API = "https://api.coindcx.com/"
baseURL_Public = "https://public.coindcx.com"  

def get_ticker(): 
    ticker = requests.get(baseURL_API + "exchange/ticker")
    return ticker.json()

def get_market(): 
    markets = requests.get(baseURL_API + "exchange/v1/markets")
    return markets.json()

def get_market_details(): 
    market_details = requests.get(baseURL_Public + "exchange/v1/markets_details")
    return market_details.json()


def get_orderbook(pair): 
    ob = requests.get(baseURL_Public + "market_data/orderbook?pair=" + pair)
    return ob.json()

# m -> minutes, h -> hours, d -> days, w -> weeks, M -> months

# 1m
# 5m
# 15m
# 30m
# 1h
# 2h
# 4h
# 6h
# 8h
# 1d
# 3d
# 1w
# 1M
def get_candles(pair, interval, startTime, endTime, limit): 
    candles = requests.get(baseURL_Public + "market_data/candles?pair=" + pair + "&interval=" + interval + "&startTime=" + startTime + "&endTime=" + endTime + "&limit=" + limit)
    return candles.json()