import yfinance as yf
import pandas as pd
import os

STOCKS = [
    "RELIANCE.NS",
    "HDFCBANK.NS",
    "TCS.NS",
    "INFY.NS",
    "ICICIBANK.NS",
    "AXISBANK.NS",
    "KOTAKBANK.NS",
    "HINDUNILVR.NS",
    "ITC.NS",
    "SBIN.NS",
    "^NSEI"  # NIFTY50 Index
]

SAVE_DIR = "data/raw"

def download_data():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    for ticker in STOCKS:
        print(f"Downloading: {ticker} ...")
        df = yf.download(ticker, start="1990-01-01", end="2025-01-01")
        file_path = os.path.join(SAVE_DIR, f"{ticker.replace('^','')}.csv")
        df.to_csv(file_path)
        print(f"Saved → {file_path}")

if __name__ == "__main__":
    download_data()
