import os
import requests

class BinanceAPI:
    def __init__(self, api_key=None, api_secret=None):
        self.api_key = api_key or os.getenv("BINANCE_API_KEY")
        self.api_secret = api_secret or os.getenv("BINANCE_API_SECRET")
        self.base_url = "https://api.binance.com"

    def get_account(self):
        url = f"{self.base_url}/api/v3/account"
        headers = {"X-MBX-APIKEY": self.api_key}
        return requests.get(url, headers=headers).json()

    def create_order(self, symbol, side, type_, quantity, price=None):
        url = f"{self.base_url}/api/v3/order"
        headers = {"X-MBX-APIKEY": self.api_key}
        data = {"symbol": symbol, "side": side, "type": type_, "quantity": quantity}
        if price:
            data["price"] = price
        return requests.post(url, headers=headers, data=data).json()
