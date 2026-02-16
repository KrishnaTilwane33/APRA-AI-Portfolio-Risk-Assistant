import pandas as pd

def create_volatility_target(df: pd.DataFrame, horizon: int = 20) -> pd.DataFrame:
    """
    Create future volatility regime target.

    horizon: number of days ahead to compute future volatility
    """
    df = df.copy()

    future_vol = (
        df["log_return"]
        .rolling(window=horizon)
        .std()
        .shift(-horizon)
    )

    df["risk_regime"] = pd.qcut(
        future_vol,
        q=3,
        labels=["low", "medium", "high"]
    )

    df = df.dropna(subset=["risk_regime"])

    return df
