# src/preprocessing/clean_data.py

import pandas as pd

def clean_market_data(df: pd.DataFrame):
    """
    Cleans raw market data and converts columns to UPPERCASE.
    Handles missing values, duplicates, and sorting.
    """

    # Remove duplicated rows
    df = df.drop_duplicates()

    # Ensure correct dtypes
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Forward-fill numeric values
    numeric_cols = ["open", "high", "low", "close", "adj_close", "volume"]
    df[numeric_cols] = df[numeric_cols].ffill()

    # Backward-fill initial missing values if any remain
    df[numeric_cols] = df[numeric_cols].bfill()

    # Remove rows with still-missing critical values
    df = df.dropna(subset=["date", "close"])

    return df


def clean_dataframe(df):
    """Remove rows with missing values after feature engineering."""
    df = df.dropna().reset_index(drop=True)
    return df
