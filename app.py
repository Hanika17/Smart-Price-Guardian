import streamlit as st
import pandas as pd
import random

st.title("🛒 Deceptive Pricing Detector")

df = pd.read_csv("cleaned_data.csv")

product = st.selectbox("Select Product", df['product'])

def generate_history(price):
    return [price + random.randint(-100, 100) for _ in range(5)]

if st.button("Analyze"):

    row = df[df['product'] == product].iloc[0]

    current_price = row['current_price']
    claimed_price = row['claimed_price']

    prices = generate_history(current_price)
    avg_price = sum(prices) / len(prices)

    if claimed_price > 1.5 * avg_price:
        verdict = "❌ FAKE DISCOUNT"
        trust = "2/10"
        reason = "Claimed price inflated"

    elif abs(current_price - avg_price) < 100:
        verdict = "⚠️ SUSPICIOUS"
        trust = "4/10"
        reason = "No real discount"

    else:
        verdict = "✅ GENUINE"
        trust = "8/10"
        reason = "Valid pricing pattern"

    st.subheader("Result")
    st.write(f"Verdict: {verdict}")
    st.write(f"Trust Score: {trust}")
    st.write(f"Reason: {reason}")

    st.line_chart(prices)