def maximize_profit(bot_results):
    # Allocate more capital to best-performing bots
    sorted_bots = sorted(bot_results, key=lambda x: x['profit'], reverse=True)
    allocation = {}
    total = sum([b['profit'] for b in sorted_bots if b['profit'] > 0])
    for b in sorted_bots:
        allocation[b['name']] = (b['profit'] / total) if total > 0 else 1.0 / len(sorted_bots)
    return allocation
