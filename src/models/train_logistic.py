"""
    Trains a multinomial logistic regression model to classify market risk regimes.

    Parameters
    ----------
    train_df : pd.DataFrame
        Training dataset with engineered features and risk_regime label.
    test_df : pd.DataFrame
        Testing dataset with engineered features and risk_regime label.

    Returns
    -------
    model : LogisticRegression
        Trained logistic regression model.
    scaler : StandardScaler
        Fitted scaler used for feature normalization.
    feature_cols : list
        List of feature names used during training.
    report : dict
        Classification report as dictionary.
    accuracy : float
        Overall accuracy score.
    """

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score


def train_logistic_model(X_train, y_train, X_test, y_test):
    feature_cols = [
        "daily_return",
        "ma_7", "ma_20",
        "vol_7", "vol_20",
        "rsi_14",
        "drawdown"
    ]

    # Select features
    X_train = X_train[feature_cols]
    X_test = X_test[feature_cols]

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train model
    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        solver="lbfgs",
    )

    model.fit(X_train_scaled, y_train)

    # Predictions
    y_pred = model.predict(X_test_scaled)

    report = classification_report(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)

    return model, report , accuracy ,y_pred
