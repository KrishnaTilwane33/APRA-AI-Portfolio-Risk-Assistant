import streamlit as st
import pandas as pd
from pathlib import Path

# ----------------------------
# GLOBAL STYLES (Fintech Theme)
# ----------------------------
st.markdown("""
<style>

/* ===== Base Layout ===== */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* ===== Font ===== */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ===== Header ===== */
.app-header {
    background: #0B1220;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    padding: 12px 0 18px 0;
    margin-bottom: 24px;
}

.header-title {
    font-size: 26px;
    font-weight: 600;
}

.header-subtitle {
    color: #9CA3AF;
    font-size: 14px;
}

/* ===== Cards (30%) ===== */
.metric-card {
    background: #111827;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.05);
}

/* ===== Accent Colors (10%) ===== */
.text-primary { color: #2563EB; }
.text-success { color: #22C55E; }
.text-warning { color: #F59E0B; }
.text-danger  { color: #EF4444; }
.text-info    { color: #38BDF8; }

/* ===== Chart container spacing ===== */
.chart-title {
    margin-top: 8px;
    margin-bottom: 6px;
}

/* ===== Sidebar styling ===== */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* ===== Buttons ===== */
.stButton > button {
    background-color: #2563EB;
    color: white;
    border-radius: 8px;
    border: none;
}

.stButton > button:hover {
    background-color: #1D4ED8;
}

</style>
""", unsafe_allow_html=True)



# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="APRA Risk Intelligence",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# HEADER
# ----------------------------
st.markdown('<div class="header">', unsafe_allow_html=True)

col_logo, col_title = st.columns([1, 10])

with col_logo:
    st.image("assets/bull.png", width=42)

with col_title:
    st.markdown("""
    <div style="font-size:24px;font-weight:600;">
        APRA — AI Portfolio Risk Assistant
    </div>
    <div style="font-size:13px;color:#9CA3AF;">
        AI-driven portfolio monitoring • Risk regimes • Strategy intelligence
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# File Paths
# ----------------------------
pred_path = Path("outputs/predictions.csv")
backtest_path = Path("outputs/backtest_results.csv")
alerts_file = Path("outputs/alerts.txt")

# ----------------------------
# Check Required Files
# ----------------------------
if not pred_path.exists() or not backtest_path.exists():
    st.error("Outputs not found. Run main.py first.")
    st.stop()

# ----------------------------
# Load Data
# ----------------------------
df_pred = pd.read_csv(pred_path)
df_backtest = pd.read_csv(backtest_path)

# Ensure date column is datetime
if "date" in df_pred.columns:
    df_pred["date"] = pd.to_datetime(df_pred["date"]).dt.tz_localize(None)

# ----------------------------
# URL Query Parameters
# ----------------------------
query_params = st.query_params
start_param = query_params.get("start")
end_param = query_params.get("end")
risk_param = query_params.get("risk")

# ----------------------------
# Sidebar Filters
# ----------------------------
st.sidebar.header("Filters")

start_date = st.sidebar.date_input(
    "Start Date",
    value=pd.to_datetime(start_param).date() if start_param else None,
    key="start_date"
)

end_date = st.sidebar.date_input(
    "End Date",
    value=pd.to_datetime(end_param).date() if end_param else None,
    key="end_date"
)
time_range = st.sidebar.radio(
    "Time Horizon",
    ["1M", "3M", "6M", "1Y", "5Y"],
    horizontal=True
)

risk_options = ["All", "low", "medium", "high"]
risk_filter = st.sidebar.selectbox(
    "Risk Level",
    options=risk_options,
    index=risk_options.index(risk_param) if risk_param in risk_options else 0,
    key="risk_filter"
)

tickers = st.sidebar.multiselect(
    "Select Assets",
    options=["AAPL", "MSFT", "GOOGL", "NVDA", "AMZN"],
    default=["AAPL", "MSFT"]
)

# ----------------------------
# Apply Filters
# ----------------------------
filtered_df = df_pred.copy()

if start_date and end_date:
    mask = (filtered_df["date"] >= pd.to_datetime(start_date)) & (
        filtered_df["date"] <= pd.to_datetime(end_date)
    )
    filtered_df = filtered_df.loc[mask]

if risk_filter != "All":
    filtered_df = filtered_df[filtered_df["predicted_risk"] == risk_filter]

risk_map = {"low": 0, "medium": 1, "high": 2}
filtered_df["risk_numeric"] = filtered_df["predicted_risk"].map(risk_map)
# ----------------------------
# Load Alerts
# ----------------------------
alerts = []
if alerts_file.exists():
    with open(alerts_file, "r", encoding="utf-8") as f:
        alerts = f.readlines()

# ----------------------------
# KPI SECTION
# ----------------------------
def kpi_card(title, value, color_class="text-primary"):
    st.markdown(f"""
        <div class="metric-card">
            <div style="color:#9CA3AF;font-size:13px;">{title}</div>
            <div class="{color_class}" style="font-size:28px;font-weight:600;">
                {value}
            </div>
        </div>
    """, unsafe_allow_html=True)


st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

latest_risk = filtered_df["predicted_risk"].iloc[-1] if not filtered_df.empty else "N/A"
final_equity = df_backtest["equity_curve"].iloc[-1]
total_alerts = len(alerts)


with col1:
    kpi_card("Latest Risk", latest_risk, "text-warning")

with col2:
    kpi_card("Final Equity", f"{final_equity:.2f}x", "text-success")

with col3:
    kpi_card("Total Alerts", total_alerts, "text-danger")

# ----------------------------
# Risk Exposure Summary
# ----------------------------
risk_counts = filtered_df["predicted_risk"].value_counts(normalize=True) * 100

col1, col2, col3 = st.columns(3)

with col1:
    kpi_card("Low Risk %", f"{risk_counts.get('low',0):.1f}%")

with col2:
    kpi_card("Medium Risk %", f"{risk_counts.get('medium',0):.1f}%")

with col3:
    kpi_card("High Risk %", f"{risk_counts.get('high',0):.1f}%")


# ----------------------------
# Price vs Risk Overlay
# ----------------------------
st.markdown("### 📉 Price & Risk Overlay")

import plotly.graph_objects as go

fig_overlay = go.Figure()

# Price line
fig_overlay.add_trace(go.Scatter(
    x=filtered_df["date"],
    y=filtered_df["close"],
    mode="lines",
    name="Price"
))

# Risk shading
risk_colors = {"low": "rgba(34,197,94,0.15)",
               "medium": "rgba(234,179,8,0.15)",
               "high": "rgba(239,68,68,0.15)"}

for regime, color in risk_colors.items():
    regime_df = filtered_df[filtered_df["predicted_risk"] == regime]
    fig_overlay.add_trace(go.Scatter(
        x=regime_df["date"],
        y=regime_df["close"],
        mode="markers",
        marker=dict(size=4),
        name=f"{regime.capitalize()} Risk",
        fill=None
    ))

fig_overlay.update_layout(
    plot_bgcolor="#111827",
    paper_bgcolor="#0B1220",
    font_color="#E5E7EB",
    margin=dict(l=10, r=10, t=30, b=10)
)


st.plotly_chart(fig_overlay, use_container_width=True)


## Risk Timeline ##

import plotly.express as px

fig = px.line(
    filtered_df,
    x="date",
    y="risk_numeric",
    title="Risk Timeline"
)

fig.update_layout(
    plot_bgcolor="#151A23",
    paper_bgcolor="#0E1117",
    font_color="#E6EDF3"
)

st.plotly_chart(fig, use_container_width=True)


##  APRA Risk Intelligence ##

st.markdown("## 📊 APRA Risk Intelligence")
st.caption("AI-driven portfolio risk monitoring")

# st.markdown("<br>", unsafe_allow_html=True)


# ----------------------------
# Layout Columns
# ----------------------------
col1, col2 = st.columns(2)

# ----------------------------
# Risk Distribution
# ----------------------------
def card_container():
    return st.container(border=True)


with col1:
    st.subheader("Risk Regime Distribution")
    st.bar_chart(filtered_df["predicted_risk"].value_counts())

# ----------------------------
# Equity Curve
# ----------------------------
with col2:
    st.subheader("Strategy Equity Curve")
    st.line_chart(df_backtest["equity_curve"])

# ----------------------------
# Drawdown Chart
# ----------------------------
st.subheader("📉 Drawdown Analysis")

if "drawdown" in filtered_df.columns:
    st.area_chart(filtered_df.set_index("date")["drawdown"])
else:
    # compute if missing
    cumulative_max = filtered_df["close"].cummax()
    drawdown = (filtered_df["close"] - cumulative_max) / cumulative_max
    st.area_chart(drawdown)


# ----------------------------
# Alerts Section
# ----------------------------
st.subheader("Recent Risk Alerts")

if alerts:
    for alert in alerts[-10:]:
        st.markdown(
            f"<span class='text-danger'>⚠ {alert.strip()}</span>",
            unsafe_allow_html=True
        )

else:
    st.info("No alerts generated.")

# ----------------------------
# Strategy vs Buy & Hold
# ----------------------------
st.subheader("📊 Strategy vs Buy & Hold")

if "close" in df_backtest.columns:
    buy_hold = df_backtest["close"] / df_backtest["close"].iloc[0]

    chart_data = pd.DataFrame({
        "Strategy": df_backtest["equity_curve"],
        "Buy & Hold": buy_hold
    })

    st.line_chart(chart_data)
else:
    st.info("Buy & Hold comparison unavailable.")

# ----------------------------
# Data Preview
# ----------------------------

st.subheader("Predictions Preview")
st.dataframe(filtered_df.tail(20), use_container_width=True)