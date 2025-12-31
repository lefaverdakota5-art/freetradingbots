def check_risk(trade_history, max_drawdown=0.2, stop_loss=0.1):
    # Example: check if drawdown or loss exceeds limits
    pnl = [t['result'] for t in trade_history]
    if min(pnl) < -abs(stop_loss):
        return False, "Stop loss triggered"
    if (max(pnl) - min(pnl)) / max(abs(max(pnl)), 1) > max_drawdown:
        return False, "Max drawdown triggered"
    return True, "Risk OK"
