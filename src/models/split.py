import pandas as pd
from typing import Tuple


def time_based_split(
    df: pd.DataFrame,
    split_ratio: float = 0.8
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split time-series data into train and test sets without shuffling.
    """
    split_index = int(len(df) * split_ratio)

    train_df = df.iloc[:split_index]
    test_df = df.iloc[split_index:]

    return train_df, test_df