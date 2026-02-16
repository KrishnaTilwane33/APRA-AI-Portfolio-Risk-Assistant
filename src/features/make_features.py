import pandas as pd
import numpy as np

def add_basic_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add basic time-series features to market data.

    Assumes df is sorted by date ascending.
    """
    df = df.copy()

    df["daily_return"] = df["close"].pct_change()
    df["log_return"] = np.log(df["close"] / df["close"].shift(1))

    df["ma_7"] = df["close"].rolling(window=7).mean()
    df["ma_20"] = df["close"].rolling(window=20).mean()

    df["vol_7"] = df["log_return"].rolling(window=7).std()
    df["vol_20"] = df["log_return"].rolling(window=20).std()

    delta = df["close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss
    df["rsi_14"] = 100 - (100 / (1 + rs))

    rolling_max = df["close"].cummax()
    df["drawdown"] = (df["close"] - rolling_max) / rolling_max

    return df
