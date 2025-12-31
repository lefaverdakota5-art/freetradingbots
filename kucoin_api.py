import os
import requests

class KuCoinAPI:
    def __init__(self, api_key=None, api_secret=None):
        self.api_key = api_key or os.getenv("KUCOIN_API_KEY")
        self.api_secret = api_secret or os.getenv("KUCOIN_API_SECRET")
        self.base_url = "https://api.kucoin.com"

    def get_accounts(self):
        url = f"{self.base_url}/api/v1/accounts"
        headers = {"KC-API-KEY": self.api_key}
        return requests.get(url, headers=headers).json()

    def create_order(self, symbol, side, size, price=None):
        url = f"{self.base_url}/api/v1/orders"
        headers = {"KC-API-KEY": self.api_key}
        data = {"symbol": symbol, "side": side, "size": size}
        if price:
            data["price"] = price
        return requests.post(url, headers=headers, json=data).json()
