import pandas as pd

def time_based_split(df: pd.DataFrame, train_ratio: float = 0.7):
    """
    Splits a time-series dataframe into train and test sets
    without shuffling.
    """

    df = df.sort_index()
    split_idx = int(len(df) * train_ratio)

    train_df = df.iloc[:split_idx]
    test_df = df.iloc[split_idx:]

    return train_df, test_df
