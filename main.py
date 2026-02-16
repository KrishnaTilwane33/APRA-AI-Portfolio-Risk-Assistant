from config.config import DATA_PATH, FEATURE_COLS, TARGET_COL, TEST_SIZE
from src.preprocessing.load_data import load_raw_csv
from src.preprocessing.clean_data import clean_dataframe
from src.preprocessing.label_risk import  label_risk_regime
from src.features.make_features import add_basic_features
from src.models.train_logistic import train_logistic_model
from src.alerts.generate_alerts import generate_risk_alerts
from src.risk_engine.backtest import run_backtest
from sklearn.model_selection import train_test_split
from src.models.save_model import save_model

import os

def main():
    print(" Loading data...")
    df = load_raw_csv(DATA_PATH)

    print(" Creating features...")
    df = add_basic_features(df)

    print(" Creating risk labels...")
    df = label_risk_regime(df)

    print(" Cleaning missing values...")
    df = clean_dataframe(df)

    print(" Splitting data...")
    x = df[FEATURE_COLS]
    y = df[TARGET_COL]

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=TEST_SIZE, shuffle=False
    )


    print(" Training model...")
    model, report,accuracy , y_pred = train_logistic_model(x_train, y_train, x_test, y_test)

    #saving model
    save_model(model)

    print("\n✅ Model Evaluation:\n")
    print(f'Model accuracy score {accuracy*100}%' )
    print(report)


    OUTPUT_DIR = "outputs"
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Save predictions
    df_test = df.iloc[-len(y_test):].copy()
    df_test["predicted_risk"] = y_pred
    df_test.to_csv(f"{OUTPUT_DIR}/predictions.csv", index=False)

    print("💾 Predictions saved → outputs/predictions.csv")


    print("🔹 Running backtest...")
    df_backtest = run_backtest(
        df.iloc[-len(y_test):].reset_index(drop=True),
        y_pred
    )

    final_equity = df_backtest["equity_curve"].iloc[-1]
    print(f"\n📈 Strategy Final Equity: {final_equity:.2f}x")

    # Save Backtest
    df_backtest.to_csv(f"{OUTPUT_DIR}/backtest_results.csv", index=False)
    print("💾 Backtest saved → outputs/backtest_results.csv")

    print("Generating alerts...")
    df_alerts, alerts = generate_risk_alerts(df_test, y_pred)

    # Save alerts
    with open(f"{OUTPUT_DIR}/alerts.txt", "w" ,encoding='utf-8') as f:
        for alert in alerts:
            f.write(alert + "\n")

    print("💾 Alerts saved → outputs/alerts.txt")

    print("\n🚨 Risk Alerts:")
    for alert in alerts[:10]:
        print(alert)


if __name__ == "__main__":
    main()
