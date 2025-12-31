import os
import requests

class CoinbaseAPI:
    def __init__(self, api_key=None, api_secret=None):
        self.api_key = api_key or os.getenv("COINBASE_API_KEY")
        self.api_secret = api_secret or os.getenv("COINBASE_API_SECRET")
        self.base_url = "https://api.coinbase.com/v2"

    def get_accounts(self):
        url = f"{self.base_url}/accounts"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        return requests.get(url, headers=headers).json()

    def create_order(self, product_id, side, funds):
        url = f"{self.base_url}/orders"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"product_id": product_id, "side": side, "funds": funds}
        return requests.post(url, headers=headers, json=data).json()
