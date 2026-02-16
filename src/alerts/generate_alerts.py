import pandas as pd

def generate_risk_alerts(df: pd.DataFrame, predictions):
    """
    Generate alerts when risk regime changes.
    Supports LOW, MEDIUM, HIGH.
    """

    df = df.copy()
    df["predicted_risk"] = predictions

    alerts = []
    previous_risk = None

    for i, row in df.iterrows():
        current_risk = row["predicted_risk"]

        if previous_risk is None:
            previous_risk = current_risk
            continue

        # LOW → MEDIUM
        if previous_risk == "low" and current_risk == "medium":
            alerts.append(
                f"⚠️ Risk increased to MEDIUM on {row.name} → Consider reducing exposure"
            )

        # MEDIUM → HIGH
        elif previous_risk in ["low", "medium"] and current_risk == "high":
            alerts.append(
                f"🚨 HIGH RISK on {row.name} → Defensive strategy recommended"
            )

        # HIGH → MEDIUM or LOW
        elif previous_risk == "high" and current_risk in ["medium", "low"]:
            alerts.append(
                f"✅ Risk decreased from HIGH on {row.name} → Conditions improving"
            )

        # MEDIUM → LOW
        elif previous_risk == "medium" and current_risk == "low":
            alerts.append(
                f"✅ Risk decreased to LOW on {row.name} → Market stabilizing"
            )

        previous_risk = current_risk

    return df, alerts
