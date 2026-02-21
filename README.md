📊 APRA — AI Portfolio Risk Assistant

AI-powered market risk intelligence system for detecting volatility spikes, regime shifts, and portfolio risk exposure.
APRA is a full-stack FinTech analytics platform that monitors financial markets, classifies risk regimes, and provides interpretable insights through an interactive dashboard. Unlike trading bots, APRA focuses on risk awareness, capital preservation, and decision support.

🚀 Live Demo

👉 https://apra-risk-dashboard.streamlit.app

🎯 Project Objectives

Detect market risk regimes (Low, Medium, High).
Identify volatility spikes and trend breakdowns.
Provide interpretable risk insights instead of black-box predictions.
Compare risk-aware strategy vs. buy-and-hold.
Deliver real-time insights via an interactive dashboard.

🧠 Key Features
📈 Risk Regime Detection

Classifies market conditions into:

🟢 Low Risk

🟡 Medium Risk

🔴 High Risk

Uses interpretable logistic regression.

📊 Interactive Dashboard

KPI metrics (latest risk, equity, alerts).
Price & risk overlay visualization.
Equity curve vs. buy-and-hold.
Drawdown analysis.
Risk distribution charts.
Recent alerts feed.

⚙️ Modular ML Pipeline

Data ingestion & preprocessing.
Feature engineering (volatility, momentum, drawdown).
Risk classification model.
Backtesting engine.
Alert generation.

🚨 Alert Engine

Flags high-risk regimes.
Detects volatility spikes.
Provides early warning signals.

🏗️ Project Architecture
APRA
│
├── data/
│   ├── raw/                # Raw stock data
│   └── processed/          # Cleaned datasets
│
├── outputs/
│   ├── predictions.csv
│   ├── backtest_results.csv
│   ├── alerts.txt
│   └── model.joblib
│
├── src/
│   ├── preprocessing/      # Data cleaning & labeling
│   ├── features/           # Feature engineering
│   ├── models/             # Training & prediction
│   ├── risk_engine/        # Backtesting logic
│   └── alerts/             # Alert generation
│
├── scripts/
│   └── dashboard.py        # Streamlit dashboard
│
├── assets/
│   └── bull.png            # App logo
│
├── app.py                  # Pipeline runner
└── requirements.txt


🔬 Machine Learning Approach
Feature Engineering
Rolling volatility
Moving averages
Momentum indicators
Drawdown metrics

Model Choice: Logistic Regression

Why?
Interpretable coefficients
Stable performance
Suitable for regime classification
Lower overfitting risk

📊 Dashboard Preview
Key Visuals
Price & Risk Overlay
Risk Timeline
Equity Curve
Drawdown Analysis

Alerts Panel

#Screenshots
<img width="1863" height="936" alt="image" src="https://github.com/user-attachments/assets/afe467b3-5037-4787-a0bc-3c466cb74cbc" />
<img width="1860" height="938" alt="image" src="https://github.com/user-attachments/assets/7e8f1202-820b-41ab-b2a9-b3836520c8f7" />
<img width="1858" height="939" alt="image" src="https://github.com/user-attachments/assets/e884ad54-0496-4444-91f3-e796e4a4dc12" />



⚡ Quick Start
1️⃣ Clone Repository
git clone https://github.com/yourusername/APRA.git
cd APRA

2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Pipeline
python app.py

5️⃣ Launch Dashboard
streamlit run scripts/dashboard.py

🌐 Deployment (Streamlit Cloud)

Push project to GitHub.
Go to Streamlit Cloud.
Select repository.

Set main file:

scripts/dashboard.py


Deploy 🚀

📌 Use Cases

Portfolio risk monitoring.
Market regime analysis.
Volatility early warning system.
FinTech analytics demonstration.
Educational tool for risk modeling.

🏆 Key Achievements

Built a full-stack ML risk intelligence system.
Designed interpretable risk regime classification.
Implemented backtesting for strategy validation.
Developed a production-ready interactive dashboard.
Deployed a live FinTech analytics application.

🔮 Future Enhancements

Multi-asset portfolio support.
Real-time data streaming.
Hidden Markov Models for regime detection.

REST API for risk reporting.

Automated cloud pipeline scheduling.

🧑‍💻 Author

Krishna Tilwane
Machine Learning & FinTech Enthusiast

📄 License

MIT License — free to use and modify.
