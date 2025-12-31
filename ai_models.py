import random

def lstm_signal(market_data):
    # Placeholder for LSTM model prediction
    return random.choice(["buy", "sell", "hold"])

def transformer_signal(market_data):
    # Placeholder for transformer model prediction
    return random.choice(["buy", "sell", "hold"])

def ensemble_vote(market_data):
    votes = [lstm_signal(market_data), transformer_signal(market_data)]
    return max(set(votes), key=votes.count)
