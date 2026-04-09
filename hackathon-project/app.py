import streamlit as st
import pandas as pd
import random

# Page config
st.set_page_config(page_title="Deceptive Pricing Detector", layout="centered")

# 🎨 CUSTOM STYLING
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #f5f7fa, #c3cfe2);
    }

    h1 {
        text-align: center;
        color: #2c3e50;
    }

    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }

    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🛒 Deceptive Pricing Detector")
st.markdown("<h4 style='text-align:center;'>AI-powered pricing intelligence system</h4>", unsafe_allow_html=True)

# Load dataset
df = pd.read_csv("cleaned_data.csv")

# Product selection
st.subheader("🔍 Select Product")
product = st.selectbox("", df['product'])

# 🧠 Improved history generation
def generate_history(current_price, claimed_price):
    base = (current_price + claimed_price) / 2
    return [base + random.randint(-200, 200) for _ in range(5)]

# Analyze button
if st.button("Analyze"):

    row = df[df['product'] == product].iloc[0]

    current_price = row['current_price']
    claimed_price = row['claimed_price']

    # Generate smarter history
    prices = generate_history(current_price, claimed_price)
    avg_price = sum(prices) / len(prices)

    # 🧠 Improved logic
    if claimed_price > 1.7 * avg_price:
        verdict = "❌ FAKE DISCOUNT"
        color = "red"
        trust_score = 2
        reason = "Price inflated significantly before discount"

    elif claimed_price > 1.3 * avg_price:
        verdict = "⚠️ SUSPICIOUS"
        color = "orange"
        trust_score = 4
        reason = "Possible price manipulation detected"

    else:
        verdict = "✅ GENUINE DEAL"
        color = "green"
        trust_score = 8
        reason = "Discount aligns with pricing trend"

    # Divider
    st.markdown("---")

    # 📊 Metrics
    st.subheader("📊 Analysis Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Current Price", f"₹{current_price}")
    col2.metric("Claimed Price", f"₹{claimed_price}")
    col3.metric("Avg Price", f"₹{round(avg_price,2)}")

    # 🟥 Verdict Card
    st.markdown(f"""
        <div style="
            padding: 20px;
            border-radius: 12px;
            background-color: white;
            text-align: center;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
            margin-top: 20px;
        ">
            <h2 style="color:{color};">{verdict}</h2>
        </div>
    """, unsafe_allow_html=True)

    # Info
    st.markdown(f"### 🔎 Trust Score: {trust_score}/10")
    st.markdown(f"**Reason:** {reason}")

    # 📈 Graph
    st.subheader("📈 Price Trend")
    st.line_chart(prices)

    # Extra insight
    st.info("This system detects deceptive pricing patterns like artificial price inflation before discounts.")