# ===== Project Configuration =====
DATA_PATH = "data/raw/reliance_60yrs.csv"

FEATURE_COLS = [
    "daily_return",
    "ma_7",
    "ma_20",
    "vol_7",
    "vol_20",
    "rsi_14",
    "drawdown"
]

TARGET_COL = "risk_regime"
TEST_SIZE = 0.2
