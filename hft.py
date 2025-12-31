import time

def hft_trade(api, symbol, volume, iterations=10):
    # Example: place many small trades rapidly
    results = []
    for _ in range(iterations):
        result = api.create_order(symbol=symbol, side="BUY", type_="MARKET", quantity=volume)
        results.append(result)
        time.sleep(0.1)  # 100ms between trades
    return results
