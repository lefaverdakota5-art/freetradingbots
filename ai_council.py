import random

class AICouncil:
    def __init__(self, n_models=3):
        self.n_models = n_models
        self.models = [self.dummy_model for _ in range(n_models)]

    def dummy_model(self, market_data):
        # Replace with real AI/ML logic
        return random.choice(["buy", "sell", "hold"])

    def vote(self, market_data):
        votes = [model(market_data) for model in self.models]
        decision = max(set(votes), key=votes.count)
        return decision, votes
