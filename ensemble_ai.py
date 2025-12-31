from ai_models import lstm_signal, transformer_signal
import xgboost as xgb
import numpy as np
import random

def xgboost_signal(market_data):
    # Placeholder for XGBoost model prediction
    return random.choice(["buy", "sell", "hold"])

def sentiment_signal(news_data):
    # Placeholder for sentiment analysis
    score = random.uniform(-1, 1)
    if score > 0.2:
        return "buy"
    elif score < -0.2:
        return "sell"
    else:
        return "hold"

def ensemble_decision(market_data, news_data):
    votes = [
        lstm_signal(market_data),
        transformer_signal(market_data),
        xgboost_signal(market_data),
        sentiment_signal(news_data)
    ]
    return max(set(votes), key=votes.count)
