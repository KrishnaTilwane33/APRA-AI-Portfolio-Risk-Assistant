import os
from pathlib import Path
from src.preprocessing.load_data import load_raw_csv
from src.preprocessing.clean_data import clean_market_data
from src.features.make_features import add_basic_features

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_PATH = os.path.join(BASE_DIR, "data/raw/reliance_60yrs.csv")
PROCESSED_PATH = os.path.join(BASE_DIR, "data/processed/reliance_processed.csv")

def main():
    print("Loading raw data...")
    df_raw = load_raw_csv(RAW_PATH)

    print("Cleaning data...")
    df_clean = clean_market_data(df_raw)

    print("Adding features...")
    df_features = add_basic_features(df_clean)

    print("Saving processed data...")
    df_features.to_csv(PROCESSED_PATH, index=False)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()
