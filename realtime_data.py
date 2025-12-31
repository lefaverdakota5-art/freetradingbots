import requests
import time

class RealTimeData:
    def get_kraken_ticker(self, pair="XXBTZUSD"):
        url = f"https://api.kraken.com/0/public/Ticker?pair={pair}"
        return requests.get(url).json()

    def get_binance_ticker(self, symbol="BTCUSDT"):
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        return requests.get(url).json()

    def get_coinbase_ticker(self, product_id="BTC-USD"):
        url = f"https://api.coinbase.com/v2/prices/{product_id}/spot"
        return requests.get(url).json()

    def get_kucoin_ticker(self, symbol="BTC-USDT"):
        url = f"https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={symbol}"
        return requests.get(url).json()
