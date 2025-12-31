from kraken_api import KrakenAPI
import os

def auto_withdraw(profit, asset="ZUSD", threshold=10):
    if profit > threshold:
        kraken = KrakenAPI()
        withdrawal_key = os.getenv("KRAKEN_WITHDRAW_KEY")
        result = kraken.withdraw(asset=asset, key=withdrawal_key, amount=profit)
        return result
    return {"status": "No withdrawal, profit below threshold"}
