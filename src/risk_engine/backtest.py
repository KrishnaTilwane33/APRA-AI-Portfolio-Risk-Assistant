import pandas as pd

def run_backtest(df: pd.DataFrame, predictions):
    """
    Backtest strategy using predicted risk regimes.
    Exposure rules:
        low    → 100% invested
        medium → 50% invested
        high   → 0% invested (cash)
    """

    df = df.copy()
    df["predicted_risk"] = predictions

    # Exposure mapping
    exposure_map = {
        "low": 1.0,
        "medium": 0.5,
        "high": 0.0
    }

    df["exposure"] = df["predicted_risk"].map(exposure_map)

    # Strategy returns
    df["strategy_return"] = df["daily_return"] * df["exposure"]

    # Equity curve (start at 1.0)
    df["equity_curve"] = (1 + df["strategy_return"]).cumprod()

    return df
