import os

print(" Running APRA pipeline...")

# Step 1 — Load & clean data
os.system("python src/preprocessing/load_data.py")
os.system("python src/preprocessing/clean_data.py")

# Step 2 — Feature engineering
os.system("python src/features/make_features.py")

# Step 3 — Train / Predict risk
os.system("python src/models/train_logistic.py")

# Step 4 — Backtest strategy
os.system("python src/risk_engine/backtest.py")

# Step 5 — Generate alerts
os.system("python src/alerts/generate_alerts.py")

print("✅ Pipeline complete.")
print(" Ready to Launch dashboard with: streamlit run scripts/dashboard.py")
