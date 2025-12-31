def backtest_strategy(strategy_func, historical_data):
    results = []
    for data_point in historical_data:
        result = strategy_func(data_point)
        results.append(result)
    return results
