from realtime_data import RealTimeData

def find_arbitrage():
    data = RealTimeData()
    k = float(data.get_kraken_ticker()["result"]["XXBTZUSD"]["c"][0])
    b = float(data.get_binance_ticker()["price"])
    if b > k * 1.002:
        return "Buy Kraken, Sell Binance"
    elif k > b * 1.002:
        return "Buy Binance, Sell Kraken"
    else:
        return "No arbitrage"
