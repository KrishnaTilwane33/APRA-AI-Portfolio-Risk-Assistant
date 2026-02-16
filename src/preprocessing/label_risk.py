import pandas as pd
import numpy as np

def label_risk_regime(df: pd.DataFrame) -> pd.DataFrame:
    """
    Assigns risk regimes (low, medium, high) based on
    volatility percentiles and drawdown thresholds.
    """
    df = df.copy()

    vol_low = df["vol_7"].quantile(0.60)
    vol_high = df["vol_7"].quantile(0.85)

    df["risk_regime"] = "low"

    # medium risk
    medium_mask = (
        (df["vol_7"] >= vol_low) |
        (df["drawdown"] >= 0.10)
    )

    df.loc[medium_mask, "risk_regime"] = "medium"

    # high risk
    high_mask = (
        (df["vol_7"] >= vol_high) &
        (df["drawdown"] >= 0.20)
    )

    df.loc[high_mask, "risk_regime"] = "high"

    return df



