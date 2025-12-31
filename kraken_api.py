import os
import requests
import time
import hashlib
import hmac
import base64

class KrakenAPI:
    def __init__(self, api_key=None, api_secret=None):
        self.api_key = api_key or os.getenv("KRAKEN_API_KEY")
        self.api_secret = api_secret or os.getenv("KRAKEN_API_SECRET")
        self.base_url = "https://api.kraken.com"

    def _sign(self, urlpath, data, nonce):
        postdata = data.copy()
        postdata['nonce'] = nonce
        postdata = urlencode(postdata)
        encoded = (str(nonce) + postdata).encode()
        message = urlpath.encode() + hashlib.sha256(encoded).digest()
        mac = hmac.new(base64.b64decode(self.api_secret), message, hashlib.sha512)
        sigdigest = base64.b64encode(mac.digest())
        return sigdigest.decode()

    def private_request(self, method, data=None):
        urlpath = f"/0/private/{method}"
        url = self.base_url + urlpath
        nonce = str(int(1000*time.time()))
        headers = {
            'API-Key': self.api_key,
            'API-Sign': self._sign(urlpath, data or {}, nonce)
        }
        payload = data or {}
        payload['nonce'] = nonce
        resp = requests.post(url, headers=headers, data=payload)
        return resp.json()

    def get_balance(self):
        return self.private_request("Balance")

    def get_trade_balance(self, asset="ZUSD"):
        return self.private_request("TradeBalance", {"asset": asset})

    def add_order(self, pair, type_, ordertype, volume, price=None):
        data = {
            "pair": pair,
            "type": type_,
            "ordertype": ordertype,
            "volume": volume
        }
        if price:
            data["price"] = price
        return self.private_request("AddOrder", data)

    def withdraw(self, asset, key, amount):
        return self.private_request("Withdraw", {"asset": asset, "key": key, "amount": amount})
