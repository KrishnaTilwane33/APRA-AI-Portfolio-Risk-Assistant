# src/preprocessing/load_data.py

import pandas as pd
from pathlib import Path

def load_raw_csv(path: str):
    """
    Loads raw market data from CSV.
    Ensures 'date' column is parsed as datetime.
    Returns a pandas DataFrame.
    """
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"Raw data file not found at: {file_path}")

    df = pd.read_csv(file_path)

    # Standard column check
    required = {"date", "open", "high", "low", "close", "adj_close", "volume"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns in dataset: {missing}")

    # Parse date column
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    return df
