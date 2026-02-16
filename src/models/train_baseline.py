import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def train_baseline_model(train_df: pd.DataFrame, test_df: pd.DataFrame):
    feature_cols = [
        "daily_return",
        "ma_7", "ma_20",
        "vol_7", "vol_20",
        "rsi_14",
        "drawdown"
    ]

    X_train = train_df[feature_cols]
    y_train = train_df["risk_regime"]

    X_test = test_df[feature_cols]
    y_test = test_df["risk_regime"]

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression(
        multi_class="multinomial",
        max_iter=1000,
        class_weight="balanced"
    )

    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)

    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    return model, scaler
